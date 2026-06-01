# method_fig_pipeline — image2 绘图提示词（XRA-GS Overall Framework）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.2 Overall Framework 配图。展示 XRA-GS 整体 pipeline：三个模块（SPS/GAP/ADM）如何在训练的三个阶段重组 Radiative Gaussian 骨干网络的密度控制。
- 与 SPS / GAP / ADM 三张模块图视觉统一：SPS 蓝 `#1F77B4`、GAP 琥珀 `#F57F17`、ADM 绿 `#388E3C`。
- 输出文件名：`method_fig_pipeline.png`，落地 `assets/fig/`。

## 设计决策

- **结构模式**：时序/阶段式水平流 — 从左到右展示训练时间线，三个彩色面板区分三个阶段
- **参考风格**：framework-xfield（三彩色面板横排）+ framework-dngs（主干+分支）
- **核心信息**：Input → SPS(初始化) → Training Loop with GAP(密度控制) → ADM(密度精修) → Output

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

绘制一张学术论文方法总览 pipeline 示意图，白色背景(#FFFFFF)，现代扁平矢量风格，Apple 式圆润美感，CVPR/NeurIPS 顶会论文级别质量。

**方法名**: XRA-GS

**整体布局**: 从左到右水平流动的 pipeline 图，宽高比约 16:6（约 1600×600 px），纯白底。整个 pipeline 分为五个视觉区域从左到右排列：Input → SPS → Training Backbone (含 GAP) → ADM → Output。三个创新模块分别用蓝/琥珀/绿三种颜色的面板背景区分。区域间用黑色实线圆润箭头(2px)连接。

**【对齐硬规则 — 最高优先级】**:
- 所有面板框（SPS / Backbone / ADM）的**上边缘必须在同一条水平线上，下边缘也必须在同一条水平线上**
- 三个面板高度完全相同（拉伸至统一高度）
- 面板间距均匀（SPS→Backbone 间距 = Backbone→ADM 间距）
- Input 区域和 Output 区域的视觉重心也与面板上下对齐
- GAP 子面板嵌在 Backbone 内部，不影响外层 Backbone 面板的边缘对齐
- **自检：画一条水平线穿过所有面板顶边，应完全重合；底边同理**

**区域 1 — Input（最左侧，无面板背景）**:
上方放 3-4 张灰度 X-ray 投影影像略带透视地错位堆叠（矩形灰度影像，内容是模糊的解剖轮廓），每张图带 1px 灰色(#BDBDBD) 4px 圆角边框。上方标题 `Sparse Projections`（8pt 灰色 #757575 加粗 sans-serif）。
下方放一个小型 3D 等轴测线框立方体（细灰线边框），内部渲染半透明灰白色体积（模糊的解剖结构，表示 FDK 粗重建）。下方标题 `FDK Volume`。
上方投影图和下方立方体用两条汇聚的灰色细箭头连向右侧 SPS 区域。

**区域 2 — SPS: Seed（淡蓝面板 #EBF3FD，16px 圆角）**:
面板左上角标题 `SPS: Seed`（蓝色 #1F77B4 加粗 sans-serif）。
面板内从左到右：一个小型 FDK 立方体图标 → 灰色箭头标注 `sample` → 约 10-12 个蓝色(#1F77B4)半透明扁平 2D 椭圆松散散布在一个 3D 线框立方体内，大椭圆在中心区域（高密度），小椭圆在外围（低密度）。
**Gaussian 必须画成扁平纯色 2D 椭圆，绝对禁止 3D 球体。**
底部标注 `Initialization`（7pt 灰色）。

**区域 3 — Backbone Training（最大的中央区域，浅灰面板 #F8F8F8，16px 圆角）**:
面板左上角标题 `Radiative Gaussian Backbone`（灰色 #555555 加粗 sans-serif）。

主干流程（水平）：左侧放一组彩色扁平 2D 椭圆（蓝+少量琥珀+少量绿，表示训练中的 Gaussians）→ 黑色箭头 → 一个灰色模块框（12px 圆角，#F5F5F5 填充，1px #BDBDBD 边框），内写 `X-ray Rasterizer` → 黑色箭头 → 一张小型渲染投影图（灰度，带 4px 圆角 1px 灰色边框），下方标注 `Rendered`。

右侧放一张小型 GT 投影图（灰度，带边框），下方标注 `GT`。渲染图和 GT 图之间用蓝色(#1565C0)实线箭头连向一个小模块框 `Loss`（12px 圆角，#E3F2FD 填充，1px #1565C0 边框）。

从 Loss 框向左引出一条红色(#D32F2F)虚线箭头（2px，dash 6px gap 4px），标注 `gradient`，反馈回到 Gaussians，形成训练循环。

**GAP 子面板**（嵌在 Backbone 面板内部下方）：一个琥珀色面板（#FFF9EE 背景，12px 圆角），标题 `GAP: Prune`（琥珀色 #F57F17 加粗），内部简化展示：几个蓝色椭圆 + 2-3 个灰色(#BDBDBD)椭圆打上小 × 号表示被剪枝，用橙色细线(1px #FF7F0E)连接相邻椭圆中心表示 KNN proximity。GAP 子面板与主干的 densification 步骤用虚线框连接。

底部标注 `Optimization (Densification Loop)`（7pt 灰色）。

**区域 4 — ADM: Refine（淡绿面板 #EEF7EE，16px 圆角）**:
面板左上角标题 `ADM: Refine`（绿色 #388E3C 加粗 sans-serif）。
面板内从左到右：三个小型正交 2D 特征网格（每个约 4×4 方格，分别用淡绿/淡蓝/淡紫色系填充，标注 P_xy, P_xz, P_yz）以等轴测视角排列 → 灰色箭头 → 一个绿色模块框（12px 圆角，#E8F5E9 填充，1px #388E3C 边框），内写 `MLP` → 灰色箭头 → 2-3 个绿色扁平 2D 椭圆，颜色深浅不同表示调制后的不同密度。
底部标注 `Later Optimization`（7pt 灰色）。

**区域 5 — Output（最右侧，无面板背景）**:
一张较大的渲染投影图（灰度，清晰的解剖结构，带 4px 圆角 1px 灰色边框），下方标注 `Novel View Synthesis`（8pt 灰色加粗）。

**箭头系统**:
- 区域间：黑色实线箭头(2px, #333333)，圆润三角箭头头部，转折处圆角过渡
- Training loop 内梯度：红色虚线箭头(2px, #D32F2F, dash 6,4)，空心三角箭头
- Loss 连接：蓝色实线箭头(2px, #1565C0)
- 区域内部：灰色实线箭头(1.5px, #888888)

**底部时间线标注**:
在五个区域下方，对齐各区域中心，用 7pt 灰色 sans-serif 依次标注：
`Input` → `Initialization` → `Optimization (Densification Loop)` → `Later Optimization` → `Inference`
这些标注之间用灰色细虚线水平连接，暗示时间进展。

**全局字体规范（5 张图统一）**:
- 全图仅使用 2 种字体样式：①标题=加粗无衬线（Helvetica Bold / Arial Bold 风格），②描述性文字=常规无衬线（Helvetica Regular / Arial Regular 风格）
- 面板标题（SPS: Seed / GAP: Prune / ADM: Refine 等）: 加粗无衬线，8-9pt，对应模块色
- 模块框内文字（X-ray Rasterizer / Loss 等）: 加粗无衬线，7-8pt
- 底部标注（Input / Initialization / Optimization 等）: 常规无衬线，7pt，灰色 #757575
- 公式: 8pt LaTeX 风格深灰斜体
- 严禁出现衬线体（Times/Serif）、手写体、装饰体
- 所有文字字号与本系列其他 4 张图（intro/SPS/GAP/ADM）保持一致

**风格强约束**:
- 白色背景 #FFFFFF，现代扁平矢量风格，Apple 式圆润美感
- 所有元素扁平 2D，不使用 3D 光影/高光/立体渲染
- Gaussian 必须画成扁平纯色 2D 椭圆，绝对禁止画成 3D 球体/有高光的球/有光影的椭球
- 模块框 12px 大圆角，1px 边框 + 浅色填充
- 面板区域 16px 大圆角，极淡色背景
- 【对齐硬规则】所有面板框的上边缘和下边缘必须严格水平对齐，面板高度统一、间距均匀
- 文字尽量精简，强调视觉元素表达
- 不使用 emoji、卡通元素
- 质量对标 CVPR/NeurIPS 顶会论文配图
- 严禁出现 dataset 名、view 数、PSNR、SSIM
- 有限调色板：蓝 #1F77B4（SPS）、琥珀 #F57F17（GAP）、绿 #388E3C（ADM）、灰 #757575（骨干）、红 #D32F2F（梯度）、蓝 #1565C0（Loss）
