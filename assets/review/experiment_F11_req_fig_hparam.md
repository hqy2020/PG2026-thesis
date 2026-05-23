# F11. Hparam — 关键超参敏感性 (合并图)

> 类型: figure
> 状态: data-pending
> 优先级: P1
> 主文/补充: main

## 1. 目的 (Why)
- 把 SPS α / GAP τ / GAP β / ADM warmup 四个核心超参的敏感性合并到一张 2×2 panel，证明 XRA-GS 在合理区间内稳定。
- 回答审稿人："你这些超参是不是 cherry-pick？换一档掉多少？"
- 缺这张图，三模块每个引入一个超参，正文要分别为 sweep 写文字、画图，版面会非常碎。

## 2. 排版位置建议
- 主文 §4.4 Robustness/Hparam 子节单图。
- 宽度：`\textwidth`（跨双栏）。
- 取代当前 `fig:hparam_compact` 与 `fig:gap_sweep` 两张分图。

## 3. 期望元素 (What must be in it)
- 2×2 panel 布局：
  - **(a) SPS α**：x = α ∈ {0.0, 0.25, 0.5, 0.75, 1.0}（混合系数）；左 y = SSIM2D ↑，右 y = PSNR2D ↑
  - **(b) GAP τ**：x = τ（KNN 距离阈值，归一化到 5 档）；同样双 y 轴
  - **(c) GAP β**：x = β（剪枝预算比例 ∈ {0%, 1%, 2%, 5%, 10%}）；双 y 轴
  - **(d) ADM warmup**：x = warmup 迭代数 / total iter ∈ {0%, 10%, 25%, 50%, 75%}；双 y 轴
- 每 panel：
  - 主曲线 SSIM2D：Crimson Red 实线 1.5 pt（与 Ours 同色）
  - 副曲线 PSNR2D：Crimson Red 虚线 1.5 pt（同色不同 dash）
  - 默认配置位置打一个填充黑色圆点 + 8pt 文字标注 `default`
  - panel 顶部 8pt 标题：(a) SPS α / (b) GAP τ / (c) GAP β / (d) ADM warmup
- setting 锁定：Chest 3-view（单 organ + 单 view，sweep 时数据量可控）；caption 必须显式注明
- 每 panel 右上角加 8pt 文字图例：实线 = SSIM2D ↑、虚线 = PSNR2D ↑

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3：
  - 线宽 1.5 pt
  - axis 8pt、tick 7pt、panel 标号 9pt
  - 双 y 轴左右刻度颜色统一（避免左红右蓝那种 mismatched style）
- 参考论文锚点：
  - `参考论文/GR.pdf` **Fig. 7**（多 panel hparam sweep 双 y 轴）
  - `参考论文/FSGS.pdf` **Fig. 6**（紧凑 2×2 hparam grid）
- 不借鉴：FSGS 的 marker 涂色风格（撞 baseline 色）；GR 的网格背景。

## 5. 数据来源/依赖
- 4 个 hparam × 5 档 × {SSIM2D, PSNR2D} × Chest 3-view = 40 个数值
- 输出路径：`assets/data/hparam_sweep_chest_3v.csv`（cols: hparam, value, ssim2d, psnr2d）
- 数据缺口：实验 agent 需要按 4 个 hparam 各做 5 次小 sweep，全部固定 seed 与 iter 数。
- 依赖：[[VISUAL_STYLE]]、[[req_tab_progressive_ablation]]（default 点必须落在 Full XRA-GS 默认配置上）。

## 6. Caption 草稿骨架 (英文)
> **Sensitivity of the four key hyperparameters.** Each panel sweeps one hyperparameter on Chest 3-view while fixing the others to the default (black dot). Solid lines report SSIM2D and dashed lines PSNR2D. XRA-GS remains within 0.5 dB / 0.01 SSIM of its default across a wide range of values for SPS α, GAP τ, GAP β and ADM warmup, indicating the design is not cherry-picked.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 2×2 panel 标号顺序 (a)(b)(c)(d) 锁定为 SPS α / GAP τ / GAP β / ADM warmup
- [ ] 每 panel 默认值位置必须显式标注 `default`
- [ ] 双 y 轴方向 ↑ 一致（都是越大越好）
- [ ] 主线 SSIM2D 实线、副线 PSNR2D 虚线，颜色统一 Crimson
- [ ] caption 显式注明 setting = Chest 3-view
- [ ] 数值与正文/表格一致，不存在与 [[req_tab_progressive_ablation]] 默认行不同的"暗中调参"
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 把 4 个 hparam 拆成 4 张分图（违反合并意图）。
- 4 个 panel 用 4 种不同颜色（破坏视觉一致性，方法只有一个，颜色统一就好）。
- 默认点不标注（读者无法判断 sweep 中心）。
- 在 Chest 3-view 之外再叠加其他 organ 曲线（信息超载，留给 supplementary）。

## 9. 备注
- 当前 `assets/fig/fig_experiment_hparam.png` 仅覆盖 GAP 单一超参，按本需求扩到 4 panel。
- 与 [[req_fig_supp_training_curve]] 共用 sweep dump pipeline。
