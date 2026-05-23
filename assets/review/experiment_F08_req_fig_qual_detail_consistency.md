# F08. Detail & Consistency — 细节 zoom-in + 跨视角一致性 (合并图)

> 类型: figure
> 状态: data-pending
> 优先级: P1
> 主文/补充: main

## 1. 目的 (Why)
- 把"细粒度结构是否保住"与"跨视角是否一致"两件原本分图讲的事并到一张图：上半 zoom-in，下半三角度。
- 回答审稿人两个问题："局部纹理（如肋骨边缘）你重建出来了吗？" 与 "换一个新视角会不会塌？"
- 缺这张图，主对比 [[req_fig_qual_main]] 只能讲全局，看不出 XRA-GS 在细节与一致性上的两项优势。

## 2. 排版位置建议
- 主文 §4.2 Main Results 第二张图，紧接 [[req_fig_qual_main]]。
- 宽度：`\textwidth`（跨双栏）。
- 不独立成节，与 [[req_fig_qual_main]] 共同承担 Main Results 的视觉论证。

## 3. 期望元素 (What must be in it)
- 上半 (Detail Zoom-in)：
  - 2 个 case（与 [[req_fig_qual_main]] 中的红框严格对应）：
    - Case A：`Chest 2-view`，红框对应 [[req_fig_qual_main]] Chest 行红框位置
    - Case B：`Foot 2-view`，红框对应 [[req_fig_qual_main]] Foot 行红框位置
  - 每个 case 一行，列 = 4：`GT zoom | R2-Gaussian zoom | X-Gaussian zoom | XRA-GS zoom`
  - 每个 zoom cell 边框颜色 = 上文红色 zoom-in box 一致（Crimson Red）
  - 行首贴标 `Chest 2-view` / `Foot 2-view`
- 下半 (Cross-view Consistency)：
  - 1 个 case：`Chest 2-view`，3 个新视角 (0°, 45°, 90°)
  - 列 = 4：`GT | R2-Gaussian | X-Gaussian | XRA-GS`
  - 行 = 3：每行一个角度
  - 行首贴角度标签 `0°` / `45°` / `90°`
- 上下半之间用 0.5pt 灰色横线分隔
- 全图右侧加一条小图例：方法名 + ↑↓ SSIM2D 简要数值（可选）

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§5：
  - zoom 边框：Crimson Red 1.5pt，与 [[req_fig_qual_main]] 红框颜色一致
  - 全部投影渲染：`gray` colormap，同 case 同 vmin/vmax
  - Ours 列高亮：列首方法名加粗 + Crimson 下划线
- 参考论文锚点：
  - `参考论文/dngs.pdf` **Fig. 6**（zoom-in 放大块 + 多 case 行布局）
  - `参考论文/LB.pdf` **Fig. 5**（angular consistency 多角度行布局）
  - `参考论文/r2gs.pdf` **Fig. 4**（zoom 框对应主图位置的引线风格）
- 不借鉴：DNGaussian 的 depth panel 装饰；LB 的多色背景。

## 5. 数据来源/依赖
- 上半 zoom 裁剪：基于 [[req_fig_qual_main]] 中 35 张主投影渲染裁剪 (脚本 `assets/scripts/build_qual_main.py` 输出对应坐标 bbox)。
- 下半跨视角：
  - 实验 agent 必须在 Chest 2-view checkpoint 上额外渲染 3 个新角度 × 4 方法 = 12 张投影
  - 输出路径：`assets/data/consistency_chest_2v/{method}_{angle}.png`
- 数据缺口：上半依赖 [[req_fig_qual_main]] 的数据；下半 12 张投影是新增。
- 依赖：[[req_fig_qual_main]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Detail recovery and cross-view consistency.** Top: zoomed crops from the red boxes in [[req_fig_qual_main]] for Chest and Foot under a 2-view setting; XRA-GS retains anatomical structure where R2-Gaussian and X-Gaussian show over-bright streaking. Bottom: novel views at 0°/45°/90° on the same Chest 2-view checkpoint; XRA-GS preserves a stable global attenuation profile across angles, whereas baselines drift.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 上半 zoom 位置必须与 [[req_fig_qual_main]] 红框严格对齐
- [ ] 上半每个 case 4 列方法名顺序固定且一致
- [ ] 下半 3 行角度顺序固定（0°→45°→90°）
- [ ] zoom 边框颜色与主图红框一致 (Crimson Red)
- [ ] Ours 列在两个半区都加粗高亮
- [ ] 同一 case 内所有 cell 共享归一化范围
- [ ] caption 同时交代上半与下半的不同 setting
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- zoom 边框换成蓝色或绿色（与主图红框语义脱钩）。
- 上下半用不同 organ（破坏论证连贯性）。
- 下半 3 个角度选 0°/180°/360° 这种缺乏区分度的组合。
- 把跨视角的"漂移"问题用文字描述但视觉上看不出（要选漂移最明显的角度）。

## 9. 备注
- 当前 `assets/fig/fig_experiment_qual_zoom.png` 与 `fig_experiment_consistency.png` 分别承担本图上下半，合并版本是新增需求。
- 上下半合并后版面更紧凑，正文段落里 `\ref{}` 只引用一次即可。
