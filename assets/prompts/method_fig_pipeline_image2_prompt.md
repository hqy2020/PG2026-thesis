# method_fig_pipeline — image2 绘图提示词（Image #3 彩色分段风格 v2）

## 用途

- 论文：`XRA-GS`（PG2026 投稿）§3.2 Overall Framework 配图
- 展示 XRA-GS 的三模块 pipeline：SPS → GAP → ADM
- **风格基准**：参考 Image #3（半监督学习 pipeline 图）——彩色背景分段、header banner、圆角模块、嵌入缩略图、底部图例、现代排版
- 输出文件名：`method_fig_pipeline.png`，直接覆盖

## 总版式

- 整体布局：**3 个彩色 step 区域水平排列**，包裹在一个大圆角外框中
- 宽高比约 **3:1**（约 2100 × 700 px，dpi ≥ 300）
- 每个 step 顶部有**彩色 header banner**（圆角上边缘），白色粗体文字
- 每个 step 有独立的**淡色背景洗**
- step 之间用粗灰色箭头连接
- 底部有一条**图例条**
- 整体风格：现代、柔和色调、充裕间距、无衬线字体

## 配色

| 元素 | 颜色 |
|------|------|
| SPS header banner | `#1F77B4` |
| SPS 背景洗 | `#E8F0FA` |
| GAP header banner | `#FF7F0E` |
| GAP 背景洗 | `#FFF0E0` |
| ADM header banner | `#2CA02C` |
| ADM 背景洗 | `#E8F5E0` |
| 模块内圆角矩形 | 比背景深一档的同色系 |
| 箭头/辅助线 | `#888888` |
| 边界聚集标记 | `#D62728` |
| 外框 | `#CCCCCC` 1px 圆角 |

## 各 Step 内容

### Step 1: SPS（蓝色系）
- Header: 蓝色 banner，白字 `Step 1: Support-Profile Seeding`
- 左侧：3 张小灰度 X-ray 投影缩略图（圆角边框），暗示多角度 + 一个浅灰 3D cube 图标标 `FDK`
- 中间：蓝色填充圆角矩形模块标 `Density-Weighted Sampling`
- 右侧：灰色圆形解剖轮廓内部散布蓝色小圆点（seeded Gaussians），密度不均匀

### Step 2: GAP（橙色系）
- Header: 橙色 banner，白字 `Step 2: Geometry-aware Pruning`
- 左侧：灰色解剖轮廓，红色小圆点密集聚集在边界，标 `After Densification`
- 中间：橙色填充圆角矩形模块标 `Dual Criterion`，旁注 `proximity + gradient`
- 右侧：同一轮廓但圆点更少更均匀，标 `After Pruning`

### Step 3: ADM（绿色系）
- Header: 绿色 banner，白字 `Step 3: Adaptive Density Modulation`
- 左侧：3 个小正交平面图标（网格），标 `K-Planes`
- 中间：绿色填充圆角矩形模块标 `MLP`
- 右侧：灰度 X-ray 投影缩略图 + 浅灰 3D cube 标 `CT Volume`

### 底部图例条
蓝色圆点 `Seeded Gaussians` / 红色圆点 `Boundary Clustered` / 绿色圆点 `Refined` / 灰色 cube `Volume`

## 禁止事项

- 严禁公式、dataset 名、PSNR/SSIM、baseline 名
- 严禁 (a)(b)(c) panel 编号
- 严禁照片级实物（用简洁线稿轮廓和灰度缩略图）
- 严禁彩虹渐变、霓虹、3D 软阴影

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

一张顶会论文用的方法流程图，宽高比约 3:1（约 2100×700 像素），白底。整图由一个大的浅灰色 1px 圆角外框包裹，内部水平排列 3 个 step 区域，每个 step 等宽。step 之间有灰色粗箭头连接。整图底部有一条水平图例条。风格参考现代半监督学习论文的 pipeline 图：柔和彩色背景分段、顶部 header banner、圆角模块、嵌入小缩略图、充裕间距。

**Step 1（左侧三分之一，蓝色系）**：顶部一条蓝色 #1F77B4 圆角 header banner，内白色粗体字 `Step 1: Support-Profile Seeding`。banner 下方是淡蓝色 #E8F0FA 背景洗区域。区域左侧画 3 张小矩形灰度 X-ray 投影缩略图（每张约 40×50px，带浅灰圆角边框，沿一条弧线排列暗示圆周多角度采集）。缩略图下方画一个浅灰色 3D 立方体小图标，旁边标 `FDK`。从立方体引出一条灰色箭头指向右侧一个蓝色 #1F77B4 填充的圆角矩形模块，模块内白字写 `Density-Weighted Sampling`。模块右侧画一个灰色圆形解剖轮廓（简洁的头骨横截面线稿），轮廓内部散布约 20 个蓝色 #1F77B4 实心小圆点，圆点密度不均匀——在轮廓边缘略密、中心略疏——表示按 FDK 密度加权采样的初始化 Gaussian 分布。

**Step 2（中间三分之一，橙色系）**：顶部一条橙色 #FF7F0E 圆角 header banner，内白色粗体字 `Step 2: Geometry-aware Pruning`。banner 下方是淡橙色 #FFF0E0 背景洗区域。区域左侧画一个灰色圆形解剖轮廓（与 Step 1 右侧同形），轮廓内部和边界上密集分布约 25 个红色 #D62728 实心小圆点，绝大多数圆点聚集在轮廓边缘（表示边界 clustering 问题），圆点下方小灰色字 `After Densification`。从这个轮廓引出灰色箭头指向中间一个橙色 #FF7F0E 填充的圆角矩形模块，模块内白字写 `Dual Criterion`，模块正下方两个小灰色字 `proximity` 和 `gradient`。模块右侧画同样的灰色圆形解剖轮廓，但内部只剩约 12 个橙色 #FF7F0E 实心小圆点，分布明显比左侧更均匀（边界不再密集），圆点下方小灰色字 `After Pruning`。

**Step 3（右侧三分之一，绿色系）**：顶部一条绿色 #2CA02C 圆角 header banner，内白色粗体字 `Step 3: Adaptive Density Modulation`。banner 下方是淡绿色 #E8F5E0 背景洗区域。区域左侧画 3 个小正交平面图标（每个平面是一个带浅绿色网格的小正方形，三个平面以互相垂直的角度略微倾斜堆叠），下方小灰色字 `K-Planes`。从三个平面引出灰色箭头汇入中间一个绿色 #2CA02C 填充的圆角矩形模块，模块内白字写 `MLP`。MLP 模块右侧引出箭头指向输出区域：上方一张小灰度 X-ray 投影缩略图（带浅灰圆角边框），下方一个浅灰色 3D 立方体图标旁标 `CT Volume`。

**step 间连接**：Step 1 与 Step 2 之间画一条粗灰色 #888888 水平右向箭头；Step 2 与 Step 3 之间同样画一条粗灰色水平右向箭头。箭头在 step 区域之间的间隙中，不叠加在 step 区域上。

**底部图例条**：在大外框的最底部居中，水平排列 4 个图例项：一个蓝色 #1F77B4 实心小圆点后接灰色字 `Seeded Gaussians`、一个红色 #D62728 实心小圆点后接灰色字 `Boundary Clustered`、一个橙色 #FF7F0E 实心小圆点后接灰色字 `Pruned Gaussians`、一个灰色小立方体后接灰色字 `Volume`。

**风格硬约束**：每个 step 的 header banner 只有上边两个角是圆角，下边两个角是直角，与背景洗区域紧密衔接。所有模块内部都是白色文字。所有缩略图用灰度而非彩色。解剖轮廓全部用简洁的灰色线稿圆形，不使用照片。字体全部无衬线。不出现公式、dataset 名、数值指标、panel 编号。不使用彩虹渐变、霓虹、3D 软阴影。整体干净、现代、专业，像一篇发表在 CVPR/NeurIPS/MICCAI 的论文 pipeline 图。
