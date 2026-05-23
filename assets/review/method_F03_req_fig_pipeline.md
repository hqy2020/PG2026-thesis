# F03. Pipeline — XRA-GS 总体方法框架图

> 类型: figure
> 状态: ready-to-draw
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 在 §3 Method 开头给读者一张"看一眼就知道流程"的总览，把 SPS / GAP / ADM 在训练循环里的位置交代清楚。
- 回答审稿人："这三个模块到底是串联、并联、还是嵌入到训练 loop 里？" — 用 block diagram 把数据流与梯度流分开画。
- 缺这张图，§3 三个模块小节会被审稿人各看各的，无法形成整体方法叙事。

## 2. 排版位置建议
- 主文 §3.1 (Overview / Framework) 第一段后立即出现。
- 宽度：`\textwidth`（跨双栏）。
- 单独成图，不与其他图共享 caption。

## 3. 期望元素 (What must be in it)
- 输入区（最左）：
  - `Sparse 2/3/4 X-ray Projections`（小图标，2 条射线 + 探测器）
  - `FDK Coarse Reconstruction`（一个 grayscale 体素小立方体）
- 初始化区：
  - 块名 `SPS: Support-Profile Seeding`（紫色块）
  - 输出 `Path-Anchored Gaussian Init`（一个点云缩略）
- 训练循环区（用一个大圆形/方形 loop 框包起来）：
  - 块名 `ADM: Adaptive Density Modulation`（橙色块），内含小公式 `Δσ = MLP(K-Planes(x))`
  - 块名 `GAP: Gradient-Aware Pruning`（青色块），标注 `prune redundant Gaussians`
  - 两个块之间双向箭头：`ADM ⇄ GAP`
  - loop 周围有 `Render → Loss → ∇` 闭环，梯度流用**黑色虚线**箭头（VISUAL_STYLE §3，避免与 ADM 橙色撞色）
- 输出区（最右）：
  - 一对 `Novel View Rendering` 投影图
  - `Tomographic Reconstruction` 体素切片
- 数据流：实线黑色箭头 1.2pt；梯度流：虚线黑色箭头 1.0pt（VISUAL_STYLE §3 dashed 3pt-2pt）
- 顶部三色色块图例：紫=Init, 青=Pruning, 橙=Refinement，分别对应论文 §3.2 / §3.3 / §3.4 小节号

## 4. 视觉效果与参考锚点
- 配色严格遵守 [[VISUAL_STYLE]] §1：SPS = 紫 `#7B5CA6`，GAP = 青 `#3CA897`，ADM = 橙 `#E07B39`，Ours/XRA-GS 不在此图额外高亮（这是 overview 不是 result 图）；背景白。
- 箭头规范见 [[VISUAL_STYLE]] §3：数据流黑实线 1.2pt，梯度流黑虚线 1.0pt，不引入第三种颜色或第三种线型。
- 字号：块名 10pt 加粗，子标注 8pt 正常体，其余按 VISUAL_STYLE §3；任何手写公式必须用 LaTeX 字体后期植入。
- 块边角：圆角 2pt，避免锐角图标化感。
- 参考论文锚点：
  - `参考论文/GR.pdf` **Fig. 2**（"sparse proj → denoise → init → graph GS → render"线性 pipeline 加 gradient flow 虚线箭头）
  - `参考论文/xgs.pdf` **Fig. 2**（输入/初始化/优化/渲染四段式块图，借鉴块大小比例）
- 不借鉴：XField 那种密集的物理公式排布（这是 overview 不是 derivation）；FSGS Fig 2 的彩色多边形装饰（过于花哨）。

## 5. 数据来源/依赖
- 不依赖实验数据，纯 schematic。
- 用 Adobe Illustrator / Inkscape / TikZ 手画即可；建议 TikZ 出 PDF 矢量。
- 依赖文档：[[req_fig_module_sps]]、[[req_fig_module_gap]]、[[req_fig_module_adm]] 三张模块图，确保块名、配色一致。

## 6. Caption 草稿骨架 (英文)
> **Overall framework of XRA-GS.** Given sparse X-ray projections and an FDK coarse reconstruction, SPS seeds path-anchored Gaussians along the attenuation support, after which an iterative refinement loop interleaves GAP (gradient-aware pruning of redundant Gaussians) and ADM (adaptive density modulation conditioned on continuous spatial context) to produce the final novel-view renderings and tomographic reconstruction. Solid arrows denote data flow; orange dashed arrows denote gradient flow.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 三模块块名严格写作 `SPS` / `GAP` / `ADM`，配色与色块图例一致（CLAUDE.md §2）
- [ ] 数据流（黑实线）与梯度流（橙虚线）肉眼可区分
- [ ] 输入端列出 FDK 与 sparse views 两件输入（与 SPS 输入一致）
- [ ] loop 区视觉上明确成"闭环"而不是线性串接
- [ ] 全图放大 200% 后块名仍清晰，矢量图源可缩放无损
- [ ] caption 单独读懂"什么进什么出 + 三个模块分别干嘛"
- [ ] 不含中文字符

## 8. 反例 (Do NOT do this)
- 把 SPS / GAP / ADM 画成纯串联（误导审稿人以为没有训练 loop）。
- 用 PNG 位图代替矢量，导致打印模糊。
- 在块内塞超过 1 行的 sub-label。
- 在 pipeline 图里塞 PSNR/SSIM 数值（数值留给表）。

## 9. 备注
- 当前 `assets/fig/fig_method_pipeline.png` 与 `fig_method_pipeline_image2.png` 已存在，但都缺 loop 闭环表达 + 梯度流颜色规范，建议按本需求重画为矢量。
- 与 `assets/prompts/method_fig_pipeline_image2_prompt.md` 的差异：本需求强制 loop 表达，强制橙色梯度虚线，强制三色图例。
