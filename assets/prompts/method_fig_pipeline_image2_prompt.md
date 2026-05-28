# method_fig_pipeline — image2 绘图提示词（顶会风格单行三段式）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.2 Overall Framework 配图。展示 `Input → SPS · GAP · ADM → Output` 一条直线流程。
- 风格基准：X-Gaussian (ECCV 2024) Fig.1 + R²-Gaussian (NeurIPS 2024) Fig.3-4 的顶会示意图风。
- 必须与同章节的 SPS / GAP / ADM 三张图视觉完全统一：同一调色板、同一无衬线字体、同一头骨几何风格、同一箭头粗细、同一椭球比例。
- 输出文件名：`method_fig_pipeline.png`，落地 `assets/fig/`。
- backup 规则：旧的 pipeline 图若存在 → 移为 `method_fig_pipeline_backup.png`；若 backup 已存在则跳过备份直接覆盖。

## 总版式

- 整体布局：**单行 1 行 × 3 列**，等宽等高，列间用浅灰右向箭头连接。
- 图幅宽高比约 **16:5**（约 1600 × 500 px，dpi ≥ 300），白底。
- 顶部居中加粗无衬线小标题（8–9pt）从左到右依次：`Input`、`Training Loop`、`Output`。
- 列标题下方留出工作区。

## 每列内容

| 列 | 视觉构成 |
|---|---|
| Col-1 *Input* | 上半部分一组 5 张缩略的稀疏 X-ray 投影（灰度，沿圆周等距分布的几何示意，**不**画合成数据集名）；下半部分一个浅灰 cube 缩略图，旁边小字标 `V_FDK`。整列底部一行小字 `sparse projections + coarse FDK`。 |
| Col-2 *Training Loop* | 三个等高、白底、圆角矩形 badge 水平等距排列，**仅描边颜色不同**：左 badge 蓝描边 `#1F77B4` 写 `SPS`；中 badge 橙描边 `#FF7F0E` 写 `GAP`；右 badge 绿描边 `#2CA02C` 写 `ADM`。三个 badge 下方各加一行 7pt 小字：`seed`、`prune`、`refine`。在三个 badge 外面再画一个浅灰圆角矩形虚线大框，框顶部居中标极小字 `iterative` 表示训练循环。从大框右上方画一条细灰色回环箭头返回 `GAP` badge 左侧（表示循环）。 |
| Col-3 *Output* | 上半部分一张目标解剖体（侧位头骨灰色线稿轮廓，与同组 SPS/GAP/ADM 图保持几何对应）的渲染 X-ray 投影示意（淡蓝色调）；下半部分一个浅灰 cube 缩略图，旁边小字标 `recovered volume`。整列底部一行小字 `novel-view projection + tomographic volume`。 |

## 列间连接

- Col-1 → Col-2：一条灰色实线右向箭头，箭头中段不加文字。
- Col-2 → Col-3：一条灰色实线右向箭头。

## 配色规范（与 figure_design.md 一致）

- 蓝 `#1F77B4`：SPS badge 描边
- 橙 `#FF7F0E`：GAP badge 描边
- 绿 `#2CA02C`：ADM badge 描边
- 中性灰 `#888888` / `#BFBFBF`：所有箭头、循环大框虚线、解剖轮廓线稿、列标题、底部说明
- 淡蓝灰 `#D9E5F0`：Col-3 输出投影的底色，避免高饱和度
- 不使用：彩虹渐变、霓虹色、热力图、3D 阴影、卡片式 UI 背景

## 字体规范

- 全图无衬线（Helvetica/Arial 风），列标题 8–9pt 加粗；badge 内字 10pt 加粗；badge 下方副词 7pt 常规；底部说明 7pt 灰色
- **严禁** 在图内出现 `(a)(b)(c)` panel 编号

## 文字烘焙白名单

- 可烘焙：`Input` / `Training Loop` / `Output` / `SPS` / `GAP` / `ADM` / `seed` / `prune` / `refine` / `V_FDK` / `sparse projections + coarse FDK` / `novel-view projection + tomographic volume` / `iterative`
- 严禁烘焙：dataset 名、view 数（2/3/4）、PSNR、SSIM、baseline 名、任何完整句子、caption 文字

## 反例

- 严禁画带 GPU / 服务器 icon 的"系统架构图"风格
- 严禁加 emoji、人物、卡通元素
- 严禁把循环写成 `for t in range(T)` 这种代码风
- 严禁解剖体使用照片（与 intro_fig_compare 不同：本图都用线稿，保持机制图属性）

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

一张顶会论文用的科学示意流程图，干净纯白底，宽高比约 16:5。整图严格采用单行 1 行 × 3 列网格，三列等宽等高，列与列之间用浅灰色实线右向箭头连接。顶部居中加粗无衬线小标题，从左到右依次为 `Input`、`Training Loop`、`Output`。整体风格参考 X-Gaussian (ECCV 2024) Figure 1 与 R²-Gaussian (NeurIPS 2024) Figure 3 的顶会简洁示意图风。

**Col-1 Input**：上半部分画 5 张缩略的稀疏 X-ray 投影矩形（小尺寸、灰度、沿一条圆弧等距排列暗示圆周采集），不要写数据集名；下半部分画一个浅灰色 3D cube 缩略图代表 FDK 重建体积，cube 右下角小字标 `V_FDK`；整列底部一行 7pt 灰色小字 `sparse projections + coarse FDK`。

**Col-2 Training Loop**：水平等距排列三个等高、白底、圆角矩形 badge（半径约高度 30%），三个 badge 内部 10pt 加粗字分别写 `SPS`、`GAP`、`ADM`；三个 badge 仅描边颜色不同：左 badge 蓝色描边 `#1F77B4`、中 badge 橙色描边 `#FF7F0E`、右 badge 绿色描边 `#2CA02C`；三个 badge 正下方各一行 7pt 灰色字 `seed`、`prune`、`refine`。在三个 badge 整体外面再画一个浅灰色虚线圆角大框，大框顶部居中标极小字 `iterative`；从大框右上角拉一条细灰色弧形回环箭头返回 `GAP` badge 上方，提示这是一个训练循环。

**Col-3 Output**：上半部分画一张目标头骨（**灰色 0.8pt 线稿轮廓**，不要照片）的 X-ray 投影示意，底色浅蓝灰 `#D9E5F0`，整张投影呈柔和的内透感；下半部分画一个浅灰色 3D cube 缩略图代表恢复后的 CT 体积，cube 右下角小字 `recovered volume`；整列底部一行 7pt 灰色小字 `novel-view projection + tomographic volume`。

**箭头与连接**：Col-1 与 Col-2 之间画一条 1.5pt 灰色 `#888888` 实线右向箭头；Col-2 与 Col-3 之间同样一条 1.5pt 灰色实线右向箭头；两条箭头位于图中线，不加任何文字。

**风格强约束**：白底干净，仅使用以下有限调色板——蓝 `#1F77B4`（SPS badge 描边）、橙 `#FF7F0E`（GAP badge 描边）、绿 `#2CA02C`（ADM badge 描边）、中性灰 `#888888`/`#BFBFBF`（箭头、循环虚线框、线稿轮廓、列标题、底部说明）、淡蓝灰 `#D9E5F0`（Col-3 输出投影底色）。绝不使用红黄热力图、彩虹渐变、霓虹、3D 软阴影、玻璃质感、UI 卡片背景、技术博客封面、解释漫画。全图统一无衬线字体（Helvetica/Arial）。严禁出现 `(a)(b)(c)` 这种独立 panel 编号；标号系统只有顶部列标题一层。严禁在图中出现 dataset 名、view 数、PSNR、SSIM、baseline 方法名、任何完整句子；严禁烘焙 caption 文字。最终目标：不读正文的人 30 秒内能复述——左侧输入是稀疏 X-ray 投影加 FDK 体积；中间训练循环里依次走 SPS·GAP·ADM 三个模块；右侧输出是新视角投影加恢复的体积。
