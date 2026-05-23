# F04. SPS — Support-Profile Seeding 模块图

> 类型: figure
> 状态: ready-to-draw
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 把 SPS 的"FDK 粗重建 → attenuation 支撑分析 → 路径锚定初始化"机制可视化，让审稿人不依赖正文公式也能看懂。
- 回答审稿人："SPS 比 random init 强在哪里？" — 给"random init vs SPS init"的 before/after 点云对比 + attenuation profile 曲线。
- 没有这张图，SPS 节会被认为是普通的 random sampling 变体，看不出它对 sparse-view 的特异性。

## 2. 排版位置建议
- 主文 §3.2 SPS 子节，紧接公式块后。
- 宽度：`\linewidth`（单栏）。
- 与 [[req_fig_module_gap]]、[[req_fig_module_adm]] 视觉风格三胞胎，可在版面上前后挨着出现以便对照。

## 3. 期望元素 (What must be in it)
- 三 panel 横排或上下：
  - **(a) Input**：FDK coarse reconstruction 切片（grayscale）+ 一条横向 attenuation profile 曲线（沿一条扫描线的衰减值）
  - **(b) Mechanism**：在 (a) 上叠加 weighted sampling probability map（heatmap, viridis），高 attenuation 区域亮，低 attenuation 区域暗；右下角小公式 `p(x) ∝ μ̂(x)^α · uniform^(1-α)`
  - **(c) Output**：两份初始化点云对比：左 `Random Init` 全空间均匀点云；右 `SPS Init` 沿衰减路径聚集且保留全局少量散点
- panel 标号 (a)(b)(c) 必须左上角白底黑字
- 每 panel 下方一行简短英文 sub-caption（≤ 8 词）

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3：
  - (a) FDK slice 用 `gray` colormap；(a) 的 attenuation profile 曲线用 SPS 紫 `#7B5CA6`
  - (b) sampling probability map 用 `viridis`（VISUAL_STYLE §2 density 类）
  - (c) random init 点云用 Neutral Gray `#888888`，SPS init 点云用 SPS Purple `#7B5CA6`，与 [[req_fig_pipeline]] 的 SPS 色块完全一致
- 字号按 VISUAL_STYLE §3：panel 标号 9pt 加粗、sub-caption 8pt，公式用 LaTeX 字体；不出现 emoji
- 参考论文锚点：
  - `参考论文/FSGS.pdf` **Fig. 3 Unpooling**（before/mechanism/after 三联布局；借鉴 panel 节奏与小 schematic 风格）
  - `参考论文/GR.pdf` **Fig. 2 中段 denoised init**（借鉴 attenuation map + sampling 概率叠加）
- 不借鉴：FSGS 的卡通箭头风；GR-Gaussian 的复杂 Laplacian icon。

## 5. 数据来源/依赖
- (a) FDK 切片：来自任一 organ + 任一 view 的输入（推荐 Chest 3-view），需要 `assets/data/fdk_chest_3v.npy`（待生成）。
- (b) Sampling probability map：基于 attenuation 值 + α=0.5 的混合得分，脚本 `assets/scripts/sps_visualize.py`（待写）。
- (c) 点云：需要 random init 与 SPS init 的 3D 高斯坐标 dump：`assets/data/init_random_chest_3v.npy`、`assets/data/init_sps_chest_3v.npy`。
- 数据缺口：以上 3 份 npy 全部待实验 agent 输出；放进 `assets/ask/` 时与现有 `experiment_2026-05-21_efficiency-and-ssim.md` 合并或新建一份。
- 依赖：[[req_fig_pipeline]] 的 SPS 配色锁定。

## 6. Caption 草稿骨架 (英文)
> **Support-Profile Seeding (SPS) initialization.** From the FDK coarse reconstruction, SPS forms a sampling probability that blends a uniform prior with the local X-ray attenuation, and draws Gaussians along the attenuation support while preserving global coverage. Compared with random initialization, SPS concentrates capacity on anatomically relevant regions before any optimization step.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 三 panel 同尺寸、同坐标系，便于眼睛在 (a)→(b)→(c) 中追踪同一空间位置
- [ ] (b) 中的 sampling 公式至少包含一个 attenuation 符号 `μ` 与混合参数 `α`
- [ ] (c) 中 random 与 SPS 点云数量相同，仅分布差异
- [ ] 点云 panel 用同一相机视角与同一 axes，不偷换视角
- [ ] panel 标号一致采用 `(a) (b) (c)` 小括号 + 加粗
- [ ] 模块块名 `SPS` 与 pipeline 紫色一致 (CLAUDE.md §2)
- [ ] caption 单独读懂"是什么 → 怎么做 → 比 random 好在哪"

## 8. 反例 (Do NOT do this)
- 把 sampling 概率图当成主 panel 而把 FDK 切片缩成附属。
- 用三组完全不同的器官切片做 (a)(b)(c)（破坏对照）。
- random 点云用 100 点而 SPS 用 10k 点，制造视觉错觉。
- panel 之间用箭头连接但箭头方向不一致（如混用 (a)→(c)→(b)）。

## 9. 备注
- 当前 `assets/fig/fig_method_sps.png` 与 `_image2.png` 偏概念示意，缺真实 attenuation profile 曲线与真实点云 dump，按本需求重画。
- 三胞胎模块图共用一份 `assets/scripts/module_figure_common.py` 出图风格 (推荐写一个 helper)。
