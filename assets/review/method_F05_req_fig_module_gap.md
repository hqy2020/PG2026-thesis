# F05. GAP — Gradient-Aware Pruning 模块图

> 类型: figure
> 状态: ready-to-draw
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 把 GAP 的"边界过密 → 用世界坐标邻近+梯度活性判定 → 删冗余"机制讲清楚。
- 回答审稿人："GAP 与传统 densify-by-gradient 有什么本质区别？" — 给"梯度散布 + 邻近度阈值"双判据可视化。
- 没有这张图，正文公式与文字会让 GAP 与普通梯度剪枝混为一谈。

## 2. 排版位置建议
- 主文 §3.3 GAP 子节，紧接公式块后。
- 宽度：`\linewidth`（单栏）。
- 与 [[req_fig_module_sps]]、[[req_fig_module_adm]] 三胞胎布局对齐。

## 3. 期望元素 (What must be in it)
- 三 panel 横排：
  - **(a) Before pruning**：训练中段一个 organ slice (推荐 Chest 3-view) 的高斯空间分布散点，叠加 attenuation map 灰底。能肉眼看到边界处 over-densification cluster。
  - **(b) Mechanism**：在 (a) 同视角上叠加两类标记：
    - 红色 ✕：被 GAP 判定为"邻近过密 + 梯度活性低"将被剪除的 Gaussian
    - 绿色 ○：保留的高斯
    - 右下角小公式 `prune if (KNN_dist < τ) ∧ (|∇g| < g_min)`
  - **(c) After pruning**：剪除后的高斯分布，边界冗余消失，#Gaussians 数量在 panel 内贴一个小标 `−β·N`（β = max prune ratio）
- 三 panel 必须用同一组高斯、同一视角、同一切面
- panel 下方 sub-caption 8pt 英文，单行

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3：
  - 高斯散点底色：attenuation 用 `magma` 半透明（alpha=0.3）做背景
  - 保留高斯：GAP 青 `#3CA897`（与 pipeline 块同色）
  - 剪除高斯标记：Crimson Red `#D7263D` ✕（"被淘汰"语义）
  - panel 标号 (a)(b)(c) 9pt 加粗
- 参考论文锚点：
  - `参考论文/Corgs.pdf` **Fig. 2**（disagreement Gaussian 可视化方式，借鉴"两类标记叠加"思路）
  - `参考论文/r2gs.pdf` **Fig. 2** 中段（高斯剪枝/纠正示意）
  - `参考论文/FSGS.pdf` **Fig. 3** 中 panel（before/after 点状示意）
- 不借鉴：CoR-GS 的椭球体填充（在 CT slice 上不可读）。

## 5. 数据来源/依赖
- 训练过程 dump：在 SPS init 之后 / GAP 第一次触发之前，dump 一次高斯坐标 + 梯度模 + KNN 距离；GAP 触发后再 dump 一次。
- 输出：
  - `assets/data/gap_before_chest_3v.npy`（cols: x,y,z,grad_norm,knn_dist）
  - `assets/data/gap_after_chest_3v.npy`
  - `assets/data/gap_pruned_flag_chest_3v.npy`（bool）
- 数据缺口：实验 agent 需要在训练管线里加 dump 钩子。
- 依赖：[[req_fig_module_sps]] 共用脚本 `assets/scripts/module_figure_common.py`、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Gradient-Aware Pruning (GAP).** Mid-training, conventional gradient-driven densification accumulates Gaussians around high-gradient boundaries. GAP identifies a Gaussian as redundant when it is spatially close to its neighbors (KNN distance below τ) **and** its gradient activity has saturated (below g_min), and removes such Gaussians up to a budget β. The pruned distribution preserves the attenuation support while reclaiming capacity for under-served regions.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] (a)(b)(c) 同 organ、同视角、同切面、同 colormap
- [ ] (b) 中"被剪 vs 保留"两类标记数量比例与 β=2% 的设定一致 (注明 β 值)
- [ ] 公式至少包含 `τ`、`g_min`、`KNN` 三个符号
- [ ] GAP 块名 / GAP 青色与 [[req_fig_pipeline]] 完全一致
- [ ] panel 标号 (a)(b)(c) 加粗、位置左上一致
- [ ] caption 单独读懂"判据是什么 + 剪了多少 + 保留了什么"
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 用纯散点图表示高斯位置但不叠加 attenuation 背景（丢失"为什么要剪在这里"的解释）。
- 把剪除标记用绿色 ✕、保留用红色 ○（与 VISUAL_STYLE 语义反转）。
- 三 panel 用不同 organ 切片对照（破坏视觉延续性）。
- 在 (b) 中同时叠加 ADM 的调制曲线（混淆模块归属）。

## 9. 备注
- 当前 `assets/fig/fig_method_gap.png` 与 `_image2.png` 偏概念示意，缺真实 KNN/gradient dump，按本需求重画。
- 推荐生成顺序：先跑实验拿 dump，再用 `module_figure_common.py` 出图，最后版面与 SPS/ADM 一起对齐。
