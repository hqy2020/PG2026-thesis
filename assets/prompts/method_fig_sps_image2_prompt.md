# method_fig_sps — image2 绘图提示词（顶会风格单行三段式）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.3 Support-Profile Seeding 配图。展示 SPS 如何把 FDK 体积转成密度加权采样分布，再得到路径锚定的初始高斯集。
- 与 pipeline / GAP / ADM 三图视觉完全统一：同一调色板、同一无衬线字体、同一头骨几何风格、同一箭头粗细、同一椭球比例。SPS 主色蓝 `#1F77B4`。
- 输出文件名：`method_fig_sps.png`，落地 `assets/fig/`。
- backup 规则：之前不存在同名图 → **不创建** backup，直接首次生成。

## 总版式

- 整体布局：**单行 1 行 × 3 列**，等宽等高，列间用浅灰右向箭头连接。
- 图幅宽高比约 **16:5**（约 1600 × 500 px，dpi ≥ 300），白底。
- 顶部居中加粗无衬线小标题（8–9pt）从左到右依次：`FDK volume`、`Density-Weighted Mixture`、`Seeded Gaussians`。
- 全图主色蓝 `#1F77B4`（区别于 GAP 橙、ADM 绿）。

## 每列内容

| 列 | 视觉构成 |
|---|---|
| Col-1 *FDK volume* | 一张轴向头骨 CT 切片的灰色线稿轮廓（与 pipeline 图同源几何，0.8pt 灰线），内部 cube 框出体素栅格暗示 `Ω`。切片下方叠一条横向 attenuation profile 曲线，曲线用深蓝 `#1F77B4` 实线，两端低、中间在颅骨位置突起两个峰，明确给出"支撑轮廓"的形状感。整列底部一行 7pt 灰色小字 `attenuation profile from V_FDK`。 |
| Col-2 *Density-Weighted Mixture* | 同切片轮廓（灰线），内部叠一张概率密度热图（**viridis 配色**，亮区落在颅骨与软组织高衰减区，背景几乎透明）。切片底部居中烘焙短公式 `q = α/|Ω| + (1−α) p`（8pt LaTeX 风格，深灰）。公式左下方一个小 `+` 号表示混合，并用一个极小的浅灰背景方块作为均匀分布示意。整列底部一行 7pt 灰色小字 `mixture: uniform prior + attenuation profile`。 |
| Col-3 *Seeded Gaussians* | 同切片轮廓（灰线），内部撒约 40–50 个深蓝实心椭球 `#1F77B4`，椭球大小约 6–10px，分布**贴附在颅骨与软组织支撑轮廓**上（不是只落在边界尖峰，而是沿支撑面均匀但有偏好地分布），背景空气区**少量**散落（体现 uniform mixture 项保留全局覆盖）。整列底部一行 7pt 灰色小字 `path-anchored initial Gaussians`。 |

## 列间连接

- Col-1 → Col-2：一条灰色实线右向箭头，箭头中段标极小字 `weight by V_FDK^γ`。
- Col-2 → Col-3：一条灰色实线右向箭头，箭头中段标极小字 `sample`。

## 配色规范

- 蓝 `#1F77B4`：Col-1 attenuation profile 曲线、Col-3 初始 Gaussians 椭球（SPS 主色）
- viridis 配色（黄→绿→紫）：Col-2 概率密度热图
- 中性灰 `#888888` / `#BFBFBF`：解剖轮廓线稿、箭头、列标题、底部说明、公式
- **不使用**：橙（属于 GAP）、绿（属于 ADM）、红、霓虹、3D 阴影

## 字体规范

- 全图无衬线（Helvetica/Arial 风），列标题 8–9pt 加粗；底部说明 7pt 灰色；烘焙公式 8pt LaTeX 风格；箭头中段标注 6pt 灰色
- **严禁** 在图内出现 `(a)(b)(c)` panel 编号

## 文字烘焙白名单

- 可烘焙：`FDK volume` / `Density-Weighted Mixture` / `Seeded Gaussians` / `q = α/|Ω| + (1−α) p` / `V_FDK^γ` / `Ω` / `weight by V_FDK^γ` / `sample` / 三行底部说明
- 严禁烘焙：dataset 名、view 数、PSNR、SSIM、α 与 γ 的具体数值、50K 初始高斯数、`small local search` 等超参描述、任何完整句子、caption 文字

## 反例

- 严禁把 Col-1 画成完整 CT 切片照片（必须是线稿 + profile 曲线）
- 严禁概率密度热图使用红黄热力图（必须 viridis）
- 严禁 Col-3 椭球只画在颅骨边界一圈（必须沿整个支撑面分布 + 少量背景散布，体现 mixture 的双重性质）
- 严禁出现 SPS·GAP·ADM 三 badge 排列（badge 只在 pipeline 图出现一次）

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

一张顶会论文用的科学示意图，干净纯白底，宽高比约 16:5。整图严格采用单行 1 行 × 3 列网格，三列等宽等高，列与列之间用浅灰色实线右向箭头连接。顶部居中加粗无衬线小标题，从左到右依次为 `FDK volume`、`Density-Weighted Mixture`、`Seeded Gaussians`。整体风格参考 X-Gaussian (ECCV 2024) Figure 1 与 R²-Gaussian (NeurIPS 2024) Figure 3 的顶会简洁示意图风。全图主色为深蓝 `#1F77B4`（区别于同章节 GAP 橙色与 ADM 绿色）。

**Col-1 FDK volume**：画一张轴向头骨 CT 切片的灰色 0.8pt 线稿轮廓（轮廓内极少阴影，体现"是 FDK 粗体积而非清晰 CT"），轮廓内部用一个极淡的灰色细网格框出体素栅格暗示 `Ω`。在切片正下方叠加一条横向 attenuation profile 曲线，曲线用深蓝 `#1F77B4` 实线 1.5pt 绘制，两端低、中间在颅骨位置突起两个对称峰，明确呈现"支撑轮廓"的形状感。整列底部一行 7pt 灰色字 `attenuation profile from V_FDK`。

**Col-2 Density-Weighted Mixture**：画同一头骨切片的灰色 0.8pt 线稿轮廓（与 Col-1 形状几何对应），轮廓内部叠加一张概率密度热图，热图严格使用 **viridis 配色**（黄→绿→紫），亮黄色区域落在颅骨与软组织高衰减区，背景空气区透明；轮廓底部居中烘焙一行短公式 `q = α/|Ω| + (1−α) p`，使用 8pt LaTeX 风格深灰字；公式左侧画一个极小的浅灰背景方块作为均匀分布示意，方块与 viridis 热图之间画一个小 `+` 号表示混合。整列底部一行 7pt 灰色字 `mixture: uniform prior + attenuation profile`。

**Col-3 Seeded Gaussians**：画同一头骨切片的灰色 0.8pt 线稿轮廓，轮廓内部撒约 40 到 50 个深蓝 `#1F77B4` 实心椭球，每个椭球大小约 6 到 10 像素，椭球**贴附在颅骨与软组织的支撑轮廓**上，沿整个支撑面分布而不仅落在边界尖峰；背景空气区**少量散落**几个椭球，体现 uniform mixture 项保留了全局覆盖。整列底部一行 7pt 灰色字 `path-anchored initial Gaussians`。

**箭头与连接**：Col-1 与 Col-2 之间画一条 1.5pt 灰色 `#888888` 实线右向箭头，箭头中段上方标 6pt 灰色字 `weight by V_FDK^γ`；Col-2 与 Col-3 之间画一条同样 1.5pt 灰色实线右向箭头，箭头中段上方标 6pt 灰色字 `sample`。

**风格强约束**：白底干净，仅使用以下有限调色板——深蓝 `#1F77B4`（attenuation profile 曲线与初始 Gaussians 椭球，SPS 主色）、viridis（Col-2 概率密度热图）、中性灰 `#888888`/`#BFBFBF`（解剖轮廓、箭头、列标题、底部说明、烘焙公式）。**严禁** 使用橙色（属于 GAP）、绿色（属于 ADM）、红色、红黄热力图、彩虹渐变、霓虹、3D 软阴影、玻璃质感、UI 卡片背景、技术博客封面、解释漫画。全图统一无衬线字体（Helvetica/Arial）。严禁出现 `(a)(b)(c)` 这种独立 panel 编号；标号系统只有顶部列标题一层。严禁在图中出现 dataset 名、view 数、PSNR、SSIM、baseline 方法名、α 与 γ 的具体数值、50K 初始高斯数等超参描述、任何完整句子；严禁烘焙 caption 文字。最终目标：不读正文的人 30 秒内能复述——左列从稀疏 X-ray 得到 FDK 粗体积与衰减剖面；中列把衰减剖面与均匀分布混合成采样概率（viridis 热图）；右列从这个分布采样得到一组沿支撑面分布的初始高斯（深蓝椭球），背景还少量散布以保留全局覆盖。
