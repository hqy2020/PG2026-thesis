# F02. Intro Compare — Gradient-Driven vs Attenuation-Aligned 概念对比

> 类型: figure
> 状态: ready-to-draw
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 把 XRA-GS 的 motivation 一图讲清：为什么 gradient-driven densification 在 `Sparse Tomographic View Synthesis` 下会失败，XRA-GS 用 attenuation profile 锚定可以避开。
- 回答审稿人："motivation 是不是有点空？" — 给一对像素级证据 + 一对 schematic。
- 没有这张图，正文中的 boundary over-densification 论证只能靠文字，审稿人不会买。

## 2. 排版位置建议
- 主文 §1 Introduction 第二/第三段之间，紧接 [[req_fig_teaser]] 之后。
- 宽度：`\textwidth`（跨双栏）。
- 与 [[req_fig_teaser]] 接力：teaser 给"我多强"，本图给"我为什么"。

## 3. 期望元素 (What must be in it)
- 上行 (Conventional Gradient Densification)：
  - (a) 输入 Sparse Views (示意 2 角度投影缩略图)
  - (b) 概念示意：在 2D attenuation map 上叠加高斯分布点，高斯密集在高梯度边界处（红色 cluster）
  - (c) 渲染结果切片，high-bright streak 在边界沿伸；error map 用 viridis colormap
- 下行 (XRA-GS Attenuation-Aligned, Ours)：
  - (a) 同样输入 Sparse Views + FDK coarse 衰减图（增加灰底）
  - (b) 概念示意：高斯沿 attenuation support 内部均匀分布
  - (c) 渲染结果切片，streak 大幅减弱；error map 颜色更冷
- 各 panel 列宽对齐，列首加列标题 `Sparse Input` / `Gaussian Allocation` / `Rendering & Error`
- 行间用一条灰色虚线分隔；每行行首贴红/绿色标签 "Conventional" / "Ours (XRA-GS)"

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3。具体到本图：
  - CT slice / FDK：`gray` colormap（VISUAL_STYLE §2）
  - error map：`inferno`，与全文 error map 共享 vmax（VISUAL_STYLE §2）
  - Gaussian 点 cluster：conventional 用 Neutral Gray `#888888`（"对照"语义），Ours/XRA-GS 用 Crimson Red `#D7263D`（"我方"语义）；不引入 matplotlib 默认蓝橙
  - 行标签色块：上行 Neutral Gray，下行 Crimson Red，与图内点云色一致
- 字号：列标题 9pt，行标签 9pt，axis 数值可省略（这是概念图不需要刻度），其余按 VISUAL_STYLE §3。
- 参考论文锚点：
  - `参考论文/Corgs.pdf` **Fig. 1**（two-row degradation-vs-recovery narrative，借叙事节奏与左右排版）
  - `参考论文/dngs.pdf` **Fig. 1**（dense / sparse / ours 三态叙事，借颜色分行的强对比）
- 不借鉴：CoR-GS 的不透明 Gaussian ellipsoid 叠加风格（会让 CT slice 不可读）；DNGaussian 的彩色 depth map 反差（会与本图 error map 撞色）。

## 5. 数据来源/依赖
- (a) Sparse input 缩略图：截自 [[req_fig_qual_main]] 同源数据的输入投影。
- (b) Gaussian allocation 示意：需要 Python 脚本基于 attenuation map + 高斯中心坐标渲染散点图；脚本放 `assets/scripts/intro_allocation.py`（待写）。
- (c) Rendering & Error：从 [[req_fig_qual_main]] 取 Chest 2-view 的 baseline (X-Gaussian) vs XRA-GS 输出 + 与 GT 的差值图。
- 数据缺口：高斯中心坐标 dump 必须由实验 agent 输出 `gaussian_centers_chest_2v_{baseline,xragns}.npy`，参见 `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md`。
- 依赖：[[req_fig_qual_main]]、[[req_fig_module_gap]]。

## 6. Caption 草稿骨架 (英文)
> **Motivation: gradient-driven Gaussian densification misallocates capacity under sparse tomographic views.** Top row: conventional densification clusters Gaussians near high-gradient boundaries and produces high-intensity streaks. Bottom row: XRA-GS distributes Gaussians along the X-ray attenuation support and yields cleaner renderings with substantially lower error.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 上下两行内容严格平行（同器官、同视角、同 colormap），方便直接对比
- [ ] Gaussian allocation 示意必须可以肉眼看出 cluster 模式差异，不是凭文字声称
- [ ] Error map 用同一 colormap 与同一数值范围 (注明 `max=...`)
- [ ] 行标签贴在最左侧、列标题在最上方，符合 Western reading order
- [ ] 上下行各自子图比例完全相同，避免审稿人怀疑"是不是 Ours 缩放过"
- [ ] caption 单独读懂"上是 conventional 下是 Ours、上 bad 下 good"

## 8. 反例 (Do NOT do this)
- 只画 schematic 不放真实 rendering（"概念图骗人"）。
- 把 Ours 放在上行（顶会习惯把 Ours 放在最后一行，叙事 dense → degraded → recovered）。
- error map 用两套不同 colormap。
- 把高斯散点画得遮住 CT slice，导致 slice 完全看不见。

## 9. 备注
- 当前 `assets/fig/fig_intro_compare.png` 与 `fig_intro_compare_image2.png` 已存在，但与本需求差距较大（缺 Gaussian allocation panel、缺 error map），按本需求重画或重生成。
- 参考 `assets/prompts/intro_fig_compare_image2_prompt.md` 是早期生成提示词，本需求覆盖其全部约束。
