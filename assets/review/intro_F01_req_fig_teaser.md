# F01. Teaser — XRA-GS 性能定位 + 问题示意

> 类型: figure
> 状态: planned
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 论文打开页给审稿人最强的一眼证据：XRA-GS 在 `Sparse Tomographic View Synthesis` 上以更少的高斯数与更短的训练时间得到更高 `PSNR2D`。
- 回答审稿人开篇的三连问：你解决什么问题？提升了多少？为什么读下去？
- 缺这张图，会让 abstract 与 intro 的"我们最好"在第一页没有视觉佐证，审稿人很难 form first impression。

## 2. 排版位置建议
- 主文 §1 Introduction 第一段后，紧贴 `\maketitle` 之后第一张图。
- 宽度：`\textwidth`（顶头一张大图，跨双栏）。
- 与 [[req_fig_intro_compare]] 接力：teaser 给"我多强"，intro_compare 给"我为什么这样设计"。

## 3. 期望元素 (What must be in it)
- 左 panel (≈ 0.42\textwidth)：**问题示意**
  - 一对 2D X-ray 投影切片，左上是 conventional gradient-driven 3DGS 的 boundary over-densification 现象（红色高亮 over-bright streak），左下是 XRA-GS 沿 attenuation 路径分布的结果。
  - 顶部小标题：`Gradient-Driven Densification` vs `Attenuation-Aligned Densification (Ours)`。
- 右 panel (≈ 0.55\textwidth)：**性能散点**
  - 横轴：Training time (min, log scale)
  - 纵轴：`PSNR2D` (dB)
  - bubble 半径：#Gaussians
  - 每个方法一个 bubble：CoR-GS / DNGaussian / FSGS / X-Field / X-Gaussian / R2-Gaussian / **XRA-GS (Ours)**
  - **XRA-GS** bubble 必须填色 `#D7263D` 红，置于图右上区域；其他 bubble 用统一柔灰蓝 `#5B7C99` 加 30%-50% 透明度
  - 右上角小图标 `↑ better` 注明右上方向更优
- 全图右下小字标注 setting：`5 organs avg, 3-view setting, GPU=A100 40GB`

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3：
  - 左 panel CT slice 用 `gray` colormap；conventional 一行的 streak 区域用 Crimson Red `#D7263D` 标注高亮 (Ours 角色色被借用一次表示"严重错误"，因为整图无 Ours-vs-baseline 散点叠加冲突)
  - 右 panel bubble：Ours = Crimson Red `#D7263D`（VISUAL_STYLE §1），所有 baseline = Slate Blue `#5B7C99` + 30% alpha；不使用 matplotlib 默认调色板
  - 横轴 log scale，"↑ better" 注明优化方向
- 字号：axis label 8pt、tick 7pt、方法名 8pt + 0.5pt 白色 halo（VISUAL_STYLE §3）
- 参考论文锚点：
  - `参考论文/xgs.pdf` **Fig. 1**（quality-vs-speed bubble 布局；只借鉴坐标轴选择与右上 Ours 突出，不借鉴它的具体颜色组合）
  - `参考论文/FSGS.pdf` **Fig. 1** 右半 FPS-vs-SSIM 散点（借鉴 log scale 与 bubble 直径编码额外维度）
- 不借鉴：X-Gaussian 那种深色背景；Ours 不用 emoji 或 stars 装饰。

## 5. 数据来源/依赖
- 左 panel 切片：需要 `assets/data/teaser_slice_chest_2v.png`（待生成；可由 [[req_fig_qual_main]] 选 Chest 2-view 的 baseline-vs-XRA-GS 对取裁剪）。
- 右 panel 散点数值：依赖 `assets/data/efficiency_3view.csv`（来自 [[req_tab_efficiency]] 的数据，列：method, train_time_min, num_gaussians, psnr2d）。
- blocker：实验 agent 未交付 `efficiency_3view.csv`，参见 `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md`。
- 依赖文档：[[req_tab_efficiency]]、[[req_fig_qual_main]]。

## 6. Caption 草稿骨架 (英文)
> **XRA-GS achieves the best PSNR2D-efficiency trade-off on Sparse Tomographic View Synthesis.** Left: conventional gradient-driven Gaussian densification over-allocates capacity near high-gradient boundaries, whereas XRA-GS distributes Gaussians along the X-ray attenuation support. Right: across five organs under a 3-view setting, XRA-GS (red) reaches the highest PSNR2D with fewer Gaussians and shorter training time than CoR-GS, DNGaussian, FSGS, X-Field, X-Gaussian, and R2-Gaussian.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 方法名严格写作 `XRA-GS`、`R2-Gaussian`、`X-Gaussian`、`X-Field`、`CoR-GS`、`DNGaussian`、`FSGS`（CLAUDE.md §10）
- [ ] 右 panel 同时编码三维信息：x、y、bubble 半径，且都有图例说明
- [ ] Ours 在右上区域且为红色，与其他 bubble 颜色对比度足够
- [ ] 横轴 log scale，所有数值刻度可读
- [ ] 缩到双栏宽 88mm 时，最小方法名仍可读
- [ ] caption 单独读懂"我比谁强、强在哪、setting 是什么"三件事
- [ ] 不出现"图表"或中英混排，全图英文

## 8. 反例 (Do NOT do this)
- 把性能散点改成柱状图（信息维度退化）。
- 把 Ours 放在左下或图中央而不是右上。
- 在 bubble 上叠加 emoji、star、闪光等装饰。
- 把 "5 organs avg" 这种关键 setting 信息省略。

## 9. 备注
- 当前 `assets/fig/` 没有对应文件，需要 0 到 1 生成。
- 生成路径：左 panel 走 [[req_fig_qual_main]] 同源切片；右 panel 用 Python (`matplotlib`) + `assets/data/efficiency_3view.csv` 出 PDF，最后用 LaTeX 组合或 Illustrator 拼版。
