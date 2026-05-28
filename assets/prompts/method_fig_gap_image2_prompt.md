# method_fig_gap — image2 绘图提示词（顶会风格单行三段式）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.4 Geometry-aware Pruning 配图。展示 GAP 如何在密化后用 KNN 近邻 + 梯度活动双条件回收边界冗余高斯，并把容量释放给内部欠表征区域。
- 与 pipeline / SPS / ADM 三图视觉完全统一：同一调色板、同一无衬线字体、同一头骨几何风格、同一箭头粗细、同一椭球比例。GAP 主色橙 `#FF7F0E`。
- 输出文件名：`method_fig_gap.png`，落地 `assets/fig/`。
- backup 规则：之前不存在同名图 → **不创建** backup，直接首次生成。

## 总版式

- 整体布局：**单行 1 行 × 3 列**，等宽等高，列间用浅灰右向箭头连接。
- 图幅宽高比约 **16:5**（约 1600 × 500 px，dpi ≥ 300），白底。
- 顶部居中加粗无衬线小标题（8–9pt）从左到右依次：`After Densification`、`Joint Criterion`、`After Pruning`。
- 全图主色橙 `#FF7F0E`（区别于 SPS 蓝、ADM 绿、naïve baseline 红）。

## 每列内容

| 列 | 视觉构成 |
|---|---|
| Col-1 *After Densification* | 同源头骨灰色线稿轮廓。轮廓内部沿颅骨/软组织高对比度**边界**密集堆积约 60 个橙色实心椭球 `#FF7F0E`，明显"挤在一圈"；轮廓**内部深部** path interior 区域几乎空白，仅有 3–5 个椭球零散。整列底部一行 7pt 灰色小字 `boundary over-densification by gradient-driven growth`。 |
| Col-2 *Joint Criterion* | 同源头骨灰色线稿轮廓的**局部放大**（轮廓只画一小段边界区段），里面只剩约 20 个椭球的局部 patch。其中：① 用**红色实心 ×** 标 6–8 个 Gaussians（表示双条件同时命中的 redundancy candidate）；② 用**绿色空心 ○** 标其余椭球（表示 retained）。底部居中烘焙判据短式 `prune if s_i < τ ∧ ḡ_i < δ`（8pt LaTeX 风格，深灰）。判据左右两侧各画一个小图例：左侧灰色背景方块加一个迷你 KNN 示意（一个中心点 + 5 条短线连到 5 个邻居），右侧灰色背景方块加一个向下的梯度箭头加 `ḡ_i`。整列底部一行 7pt 灰色小字 `low proximity ∧ low gradient activity`。 |
| Col-3 *After Pruning* | 同源头骨灰色线稿轮廓（与 Col-1 同尺寸同几何）。轮廓内部仍保留橙色实心椭球，但**边界处椭球数量明显减少**（约剩 30 个，原来红 × 标的位置改为空白），同时**内部 path interior 出现 8–10 个新增椭球**（暗示密化在下一轮把容量分配给欠表征区域，但此处仅画"释放出空间"即可）。整列底部一行 7pt 灰色小字 `capacity reclaimed from saturated boundaries`。 |

## 列间连接

- Col-1 → Col-2：一条灰色实线右向箭头，箭头中段标极小字 `KNN + gradient`。
- Col-2 → Col-3：一条灰色实线右向箭头，箭头中段标极小字 `prune & shrink`。

## 配色规范

- 橙 `#FF7F0E`：所有 Gaussians 椭球（GAP 主色）
- 红 `#D62728`：Col-2 redundancy candidate `×` 标记（失败/淘汰）
- 绿 `#2CA02C`：Col-2 retained `○` 标记（保留）
- 中性灰 `#888888` / `#BFBFBF`：解剖轮廓线稿、箭头、列标题、底部说明、判据公式、KNN/gradient 图例
- **不使用**：蓝（属于 SPS）、viridis 热图、霓虹、3D 阴影

## 字体规范

- 全图无衬线（Helvetica/Arial 风），列标题 8–9pt 加粗；底部说明 7pt 灰色；烘焙判据 8pt LaTeX 风格；箭头中段标注 6pt 灰色
- **严禁** 在图内出现 `(a)(b)(c)` panel 编号

## 文字烘焙白名单

- 可烘焙：`After Densification` / `Joint Criterion` / `After Pruning` / `prune if s_i < τ ∧ ḡ_i < δ` / `ḡ_i` / `KNN + gradient` / `prune & shrink` / 三行底部说明
- 严禁烘焙：dataset 名、view 数、PSNR、SSIM、K 邻居数（如 5）、τ / δ / β_prune 的数值、[2K, 20K] 迭代区间、任何完整句子、caption 文字

## 反例

- 严禁把 Col-2 画成全切片（必须是边界小 patch 放大）
- 严禁 Col-3 把所有椭球清空（必须保留大部分橙色椭球 + 边界变稀疏 + 内部新增）
- 严禁 redundancy candidate 用其他颜色（必须红 ×）
- 严禁出现 SPS·GAP·ADM 三 badge 排列（badge 只在 pipeline 图出现）

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

一张顶会论文用的科学示意图，干净纯白底，宽高比约 16:5。整图严格采用单行 1 行 × 3 列网格，三列等宽等高，列与列之间用浅灰色实线右向箭头连接。顶部居中加粗无衬线小标题，从左到右依次为 `After Densification`、`Joint Criterion`、`After Pruning`。整体风格参考 X-Gaussian (ECCV 2024) Figure 1 与 R²-Gaussian (NeurIPS 2024) Figure 3 的顶会简洁示意图风。全图主色为橙色 `#FF7F0E`（区别于 SPS 蓝、ADM 绿）。

**Col-1 After Densification**：画一张轴向头骨切片的灰色 0.8pt 线稿轮廓（与 SPS 图同源几何）。轮廓内部沿颅骨与软组织的高对比度边界**密集**堆积约 60 个橙色 `#FF7F0E` 实心椭球，每个椭球 6–10 像素，明显"挤在一圈"形成可见的过密化簇；轮廓内部深部 path interior 区域几乎空白，仅有 3 到 5 个椭球零散分布。整列底部一行 7pt 灰色字 `boundary over-densification by gradient-driven growth`。

**Col-2 Joint Criterion**：画同一头骨灰色 0.8pt 线稿轮廓的**局部放大**——只画一小段边界区段，里面只显示约 20 个椭球的局部 patch。其中 6 到 8 个椭球用**红色 `#D62728` 实心 × 号**覆盖标记（表示双条件同时命中的冗余候选），其余椭球用**绿色 `#2CA02C` 空心 ○ 号**覆盖标记（表示保留）。在 patch 正下方居中烘焙判据短公式 `prune if s_i < τ ∧ ḡ_i < δ`，使用 8pt LaTeX 风格深灰字。判据左侧画一个极小的浅灰色背景方块作为 KNN 示意——一个中心点连出 5 条短线到 5 个邻居小点；判据右侧画一个极小的浅灰色背景方块作为梯度活动示意——一个向下的灰色箭头旁边标小字 `ḡ_i`。整列底部一行 7pt 灰色字 `low proximity ∧ low gradient activity`。

**Col-3 After Pruning**：画同一头骨灰色 0.8pt 线稿轮廓（与 Col-1 同尺寸同几何）。轮廓内部仍保留橙色 `#FF7F0E` 实心椭球，但**边界处椭球数量明显减少**到约 30 个，原来在 Col-2 被红 × 标记的对应位置现在改为空白；同时**轮廓内部 path interior 区域出现 8 到 10 个新增椭球**，暗示密化在下一轮把释放出来的容量分配给欠表征的深部区域。整列底部一行 7pt 灰色字 `capacity reclaimed from saturated boundaries`。

**箭头与连接**：Col-1 与 Col-2 之间画一条 1.5pt 灰色 `#888888` 实线右向箭头，箭头中段上方标 6pt 灰色字 `KNN + gradient`；Col-2 与 Col-3 之间画一条同样 1.5pt 灰色实线右向箭头，箭头中段上方标 6pt 灰色字 `prune & shrink`。

**风格强约束**：白底干净，仅使用以下有限调色板——橙色 `#FF7F0E`（所有 Gaussians 椭球，GAP 主色）、红色 `#D62728`（Col-2 redundancy candidate `×` 标记）、绿色 `#2CA02C`（Col-2 retained `○` 标记）、中性灰 `#888888`/`#BFBFBF`（解剖轮廓线稿、箭头、列标题、底部说明、烘焙判据、KNN 与 gradient 图例）。**严禁** 使用蓝色（属于 SPS）、viridis 热图、彩虹渐变、霓虹、3D 软阴影、玻璃质感、UI 卡片背景、技术博客封面、解释漫画。全图统一无衬线字体（Helvetica/Arial）。严禁出现 `(a)(b)(c)` 这种独立 panel 编号；标号系统只有顶部列标题一层。严禁在图中出现 dataset 名、view 数、PSNR、SSIM、baseline 方法名、K 邻居数、τ / δ / β_prune 等超参数值、训练迭代区间、任何完整句子；严禁烘焙 caption 文字。最终目标：不读正文的人 30 秒内能复述——左列在密化后高斯都挤在边界一圈，内部空白；中列对每个高斯算 KNN 近邻距离和梯度活动，两者都低的红 × 是冗余，其它绿 ○ 保留；右列裁剪后边界稀疏了一些，深部内部多出新的高斯落点。
