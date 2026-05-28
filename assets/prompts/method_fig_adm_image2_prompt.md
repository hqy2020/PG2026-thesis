# method_fig_adm — image2 绘图提示词（顶会风格单行三段式）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.5 Adaptive Density Modulation 配图。展示 ADM 如何用三平面 K-Planes 编码位置上下文，经双头 MLP 输出密度偏移与置信度门，最终作用为相对密度调制。
- 与 pipeline / SPS / GAP 三图视觉完全统一：同一调色板、同一无衬线字体、同一头骨几何风格、同一箭头粗细、同一椭球比例。ADM 主色绿 `#2CA02C`。
- 输出文件名：`method_fig_adm.png`，落地 `assets/fig/`。
- backup 规则：之前不存在同名图 → **不创建** backup，直接首次生成。

## 总版式

- 整体布局：**单行 1 行 × 3 列**，等宽等高，列间用浅灰右向箭头连接。
- 图幅宽高比约 **16:5**（约 1600 × 500 px，dpi ≥ 300），白底。
- 顶部居中加粗无衬线小标题（8–9pt）从左到右依次：`Gaussian Position`、`K-Planes + MLP`、`Modulated Density`。
- 全图主色绿 `#2CA02C`（区别于 SPS 蓝、GAP 橙）。

## 每列内容

| 列 | 视觉构成 |
|---|---|
| Col-1 *Gaussian Position* | 同源头骨灰色线稿轮廓，内部撒约 25 个浅灰色椭球作为整个 Gaussian 集，其中**1 个高亮深绿色 `#2CA02C` 实心椭球**位于颅骨内部某处（比其它略大），旁边小字标 `x`，表示"我们要查询的位置"。整列底部一行 7pt 灰色小字 `query position of one Gaussian center`。 |
| Col-2 *K-Planes + MLP* | 上半部分横向并排三张小方形 K-Planes 平面（xy / yz / xz），三张平面**严格使用 viridis 配色**，每张右上角小字标 `xy` / `yz` / `xz`；从 Col-1 的高亮椭球 `x` 引出一条浅灰虚线分别投影到三张平面上对应坐标点，并用一个小**绿色** `#2CA02C` 圆点标记每张平面上的采样点；三张平面正下方画一个小三角形指向一个浅灰圆角矩形 box，box 内 10pt 加粗深灰字写 `MLP`，box 左侧标极小字 `concat`。MLP box 右侧分出两条小箭头，上分支输出标 `Δσ`（深灰），下分支输出标 `g`（深灰）。整列底部一行 7pt 灰色小字 `tri-plane feature → dual-head MLP`。 |
| Col-3 *Modulated Density* | 同源头骨灰色线稿轮廓（与 Col-1 同尺寸同几何），内部叠一张**密度差异图**（**inferno 配色**：低值黑色 / 高值黄色），亮区位于颅骨与软组织高衰减区，背景空气区接近黑色（表示调制后差异）。轮廓内部仍保留若干浅灰色椭球轮廓提示这是同一 Gaussian 集，其中那个高亮位置 `x` 的椭球现在用绿色边描出（表示已应用调制）。轮廓底部居中烘焙短公式 `ρ_final = ρ_base · (1 + g (Δσ − Δσ̄))`（8pt LaTeX 风格，深灰）。整列底部一行 7pt 灰色小字 `batch-centered relative modulation`。 |

## 列间连接

- Col-1 → Col-2：一条灰色实线右向箭头，箭头中段标极小字 `bilinear sample`。
- Col-2 → Col-3：一条灰色实线右向箭头，箭头中段标极小字 `modulate`。

## 配色规范

- 绿 `#2CA02C`：Col-1 高亮椭球、Col-2 三平面上的采样点、Col-3 被调制椭球的描边（ADM 主色）
- viridis（黄→绿→紫）：Col-2 三张 K-Planes 平面
- inferno（黑→橙→黄）：Col-3 密度差异图
- 中性灰 `#888888` / `#BFBFBF`：解剖轮廓线稿、其它非高亮椭球、箭头、列标题、底部说明、烘焙公式、`MLP` box、`Δσ` 与 `g` 标注
- **不使用**：蓝（属于 SPS）、橙（属于 GAP）、红、霓虹、3D 阴影

## 字体规范

- 全图无衬线（Helvetica/Arial 风），列标题 8–9pt 加粗；底部说明 7pt 灰色；烘焙公式 8pt LaTeX 风格；MLP box 内 10pt 加粗；`Δσ` / `g` / `x` 等符号 7pt 深灰；箭头中段标注 6pt 灰色
- **严禁** 在图内出现 `(a)(b)(c)` panel 编号

## 文字烘焙白名单

- 可烘焙：`Gaussian Position` / `K-Planes + MLP` / `Modulated Density` / `xy` / `yz` / `xz` / `MLP` / `concat` / `Δσ` / `g` / `x` / `ρ_final = ρ_base · (1 + g (Δσ − Δσ̄))` / `bilinear sample` / `modulate` / 三行底部说明
- 严禁烘焙：dataset 名、view 数、PSNR、SSIM、K-Planes 分辨率（如 64）、特征维度（如 32）、s_view = {0.5,0.7,1.0}、warm-up/hold/decay 等超参描述、任何完整句子、caption 文字

## 反例

- 严禁三平面用普通灰度或红黄热力图（必须 viridis）
- 严禁密度差异图用 jet 或彩虹（必须 inferno）
- 严禁画两个独立 MLP（必须是**一个**MLP box 双头输出 Δσ 与 g）
- 严禁出现 SPS·GAP·ADM 三 badge 排列（badge 只在 pipeline 图出现）

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

一张顶会论文用的科学示意图，干净纯白底，宽高比约 16:5。整图严格采用单行 1 行 × 3 列网格，三列等宽等高，列与列之间用浅灰色实线右向箭头连接。顶部居中加粗无衬线小标题，从左到右依次为 `Gaussian Position`、`K-Planes + MLP`、`Modulated Density`。整体风格参考 X-Gaussian (ECCV 2024) Figure 1 与 R²-Gaussian (NeurIPS 2024) Figure 3 的顶会简洁示意图风。全图主色为深绿 `#2CA02C`（区别于同章节 SPS 蓝、GAP 橙）。

**Col-1 Gaussian Position**：画一张轴向头骨切片的灰色 0.8pt 线稿轮廓（与 SPS / GAP 图同源几何），轮廓内部撒约 25 个浅灰色 `#BFBFBF` 椭球作为整个 Gaussian 集，其中**1 个高亮深绿色 `#2CA02C` 实心椭球**位于颅骨内部某个位置（比其它椭球略大，8–12 像素），椭球右上方用 7pt 深灰字标 `x`，表示这是我们要查询的位置。整列底部一行 7pt 灰色字 `query position of one Gaussian center`。

**Col-2 K-Planes + MLP**：上半部分横向并排三张小尺寸方形 K-Planes 特征平面，三张平面严格使用 **viridis 配色**（黄→绿→紫），每张平面右上角各用 6pt 深灰字标 `xy`、`yz`、`xz`；从 Col-1 的高亮椭球位置 `x` 引出一条浅灰色虚线，分别投影到三张平面上对应的 2D 坐标点，并在每张平面上用一个小绿色 `#2CA02C` 圆点标记该采样位置。三张平面正下方画一个小三角形 funnel 指向一个浅灰色圆角矩形 box，box 内部居中用 10pt 加粗深灰字写 `MLP`，box 左侧标极小字 `concat`，表示三张平面的特征经 bilinear 采样后拼接送入这一个 MLP。MLP box 右侧分出两条短小箭头：上分支末端标 `Δσ`（7pt 深灰），下分支末端标 `g`（7pt 深灰），表示这一个 MLP 同时输出密度偏移与置信度门两个头。整列底部一行 7pt 灰色字 `tri-plane feature → dual-head MLP`。

**Col-3 Modulated Density**：画同一头骨切片的灰色 0.8pt 线稿轮廓（与 Col-1 同尺寸同几何），轮廓内部叠加一张密度差异图，差异图严格使用 **inferno 配色**（低值黑色 / 高值橙黄色），亮黄区域落在颅骨与软组织高衰减区，背景空气区接近黑色。轮廓内部仍保留若干浅灰色椭球轮廓提示这是同一 Gaussian 集，**其中那个高亮位置 `x` 的椭球现在用绿色 `#2CA02C` 边描出 1.5pt 描边**，表示已应用调制。轮廓底部居中烘焙一行短公式 `ρ_final = ρ_base · (1 + g (Δσ − Δσ̄))`，使用 8pt LaTeX 风格深灰字。整列底部一行 7pt 灰色字 `batch-centered relative modulation`。

**箭头与连接**：Col-1 与 Col-2 之间画一条 1.5pt 灰色 `#888888` 实线右向箭头，箭头中段上方标 6pt 灰色字 `bilinear sample`；Col-2 与 Col-3 之间画一条同样 1.5pt 灰色实线右向箭头，箭头中段上方标 6pt 灰色字 `modulate`。

**风格强约束**：白底干净，仅使用以下有限调色板——深绿 `#2CA02C`（Col-1 高亮椭球、Col-2 三平面上的采样点、Col-3 被调制椭球的描边，ADM 主色）、viridis（Col-2 三张 K-Planes 平面）、inferno（Col-3 密度差异图）、中性灰 `#888888`/`#BFBFBF`（解剖轮廓、非高亮椭球、箭头、列标题、底部说明、烘焙公式、MLP box、`Δσ` 与 `g` 标注）。**严禁** 使用蓝色（属于 SPS）、橙色（属于 GAP）、红色、jet 或彩虹热图、霓虹、3D 软阴影、玻璃质感、UI 卡片背景、技术博客封面、解释漫画。全图统一无衬线字体（Helvetica/Arial）。严禁出现 `(a)(b)(c)` 这种独立 panel 编号；标号系统只有顶部列标题一层。严禁在图中出现 dataset 名、view 数、PSNR、SSIM、baseline 方法名、K-Planes 分辨率、特征维度、s_view 数值、warm-up/hold/decay 等超参描述、任何完整句子；严禁烘焙 caption 文字。Col-2 必须画**一个** MLP box 双头输出而不是两个独立 MLP。最终目标：不读正文的人 30 秒内能复述——左列从所有高斯里挑出一个位置 `x`；中列把 `x` 投到三个 K-Planes 平面上 bilinear 采样后 concat 送入一个 MLP，MLP 双头同时吐出 Δσ 与 g；右列把 g 与 Δσ 用作"(1 + g · (Δσ − Δσ̄))" 的相对调制，得到最终密度，差异图体现哪里被增强哪里被衰减。
