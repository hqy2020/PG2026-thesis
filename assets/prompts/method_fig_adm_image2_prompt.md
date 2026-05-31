# method_fig_adm — image2 绘图提示词（ADM 模块机制图）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.5 Adaptive Density Modulation 配图。展示 ADM 如何通过 K-Planes 三平面空间编码 + 双头 MLP 实现 position-dependent density modulation。
- 与 pipeline / SPS / GAP 三图视觉统一。ADM 主色绿 `#388E3C`。
- 输出文件名：`method_fig_adm.png`，落地 `assets/fig/`。

## 设计决策

- **结构模式**：水平三阶段流程图（与 SPS/GAP 风格一致）
- **核心机制**：K-Planes 空间特征编码 → 特征拼接 → 双头 MLP 密度调制
- **视觉元素**：三正交特征网格 + 特征向量色条 + MLP 模块框 + Gaussian 密度调制前后对比（扁平 2D 椭圆）

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

绘制一张学术论文模块细节示意图，白色背景(#FFFFFF)，现代扁平矢量风格，Apple 式圆润美感，CVPR/NeurIPS 顶会论文级别质量。

模块名: Adaptive Density Modulation (ADM)

整体布局: 水平三阶段流程图，从左到右，宽高比约 16:6（约 1600×600 px），白色背景。三阶段之间用灰色(#888888) 1.5pt 实线右向箭头连接（圆润三角箭头头部）。每阶段上方有加粗 sans-serif 标题。全图主色绿 #388E3C。

Stage 1 K-Planes 空间编码（左侧）:
标题 `K-Planes Feature Planes`（绿色 #388E3C 加粗）。展示三个正交的 2D 特征网格以等轴测视角排列，形成三面体结构：P_xy 平面水平放置（淡绿色系方格），P_xz 平面竖直放在左侧（淡蓝色系方格），P_yz 平面竖直放在右侧（淡紫色系方格）。每个平面是 5×5 的彩色方格网格，格子颜色深浅不同代表特征值高低。三个平面交汇处的 3D 空间中有一个绿色(#388E3C)实心圆点标注为 x（代表 Gaussian 中心）。从这个绿色圆点引出三条绿色虚线分别投影到三个平面上的对应位置，每个投影落点处用一个小黄色方格高亮标注（表示双线性插值采样位置）。三个平面旁分别标注 P_xy、P_xz、P_yz（7pt 灰色 sans-serif）。

Stage 1 到 Stage 2 之间箭头中段上方标 6pt 灰色字 `project & sample`。

Stage 2 特征拼接（中间）:
标题 `Feature Concat`（绿色 #388E3C 加粗）。上方纵向排列三个短的特征向量色条——每个色条是一行紧密排列的约 6 个小色块。第一个色条用淡绿色系（标注 f_xy），第二个用淡蓝色系（标注 f_xz），第三个用淡紫色系（标注 f_yz）。三个色条下方汇合（用大括号或汇聚箭头），连接到一个更长的联合特征色条（约 18 个色块，三种颜色依次排列），标注 F(x)。底部放一个公式框（8px 圆角，#F5F5F5 浅灰背景，1px #E0E0E0 边框），内写斜体公式 `F(x) = [f_xy ; f_xz ; f_yz]`。

Stage 2 到 Stage 3 之间箭头中段上方标 6pt 灰色字 `MLP`。

Stage 3 密度调制（右侧）:
标题 `Density Modulation`（绿色 #388E3C 加粗）。左侧放一个绿色主题的模块框（12px 圆角，浅绿 #E8F5E9 填充，1px 绿色 #388E3C 边框），内写加粗 `Dual-Head MLP`。从 MLP 框右侧引出两个分支箭头——上分支指向一个标注 `Δσ` 的小标签（标注 "Density Offset"），下分支指向一个标注 `g` 的小标签（标注 "Confidence Gate"）。两个分支再汇合到右侧的密度调制效果展示区域：展示 3 个扁平 2D 纯色椭圆（绝对禁止 3D 球体），每个椭圆代表一个 Gaussian。用颜色深浅表示密度高低——深绿色椭圆标注 `high ρ`，中绿色椭圆标注 `mid ρ`，浅绿色椭圆标注 `low ρ`。每个实线椭圆旁边有一个更小的灰色虚线椭圆表示原始 base 密度，小箭头从虚线椭圆指向实线椭圆表示密度调整方向（有的变大有的变小）。底部公式框（8px 圆角，浅绿 #E8F5E9 背景，1px 绿色边框）：`ρ_final = ρ_base(1 + g(Δσ − Δσ̄))`。

底部图例（紧凑融入 Stage 3 下方空白处，不独占一整行）:
- 绿色方格图标 + "K-Planes Feature"
- 绿色实线椭圆图标 + "Modulated ρ"
- 灰色虚线椭圆图标 + "Base ρ"

**全局字体规范（5 张图统一）**:
- 全图仅使用 2 种字体样式：①标题=加粗无衬线（Helvetica Bold / Arial Bold 风格），②描述性文字=常规无衬线（Helvetica Regular / Arial Regular 风格）
- 阶段标题（K-Planes Feature Planes / Feature Concat / Density Modulation）: 加粗无衬线，8-9pt，绿色 #388E3C
- 模块框内文字（Dual-Head MLP）: 加粗无衬线，7-8pt
- 图例/标注文字: 常规无衬线，7pt，灰色 #757575
- 箭头中段标注: 常规无衬线，6pt，灰色 #888888
- 公式: 8pt LaTeX 风格深灰斜体
- 严禁出现衬线体（Times/Serif）、手写体、装饰体
- 所有文字字号与本系列其他 4 张图（intro/pipeline/SPS/GAP）保持一致

设计规范（必须严格遵守）：
- 白色背景(#FFFFFF)，现代扁平矢量风格，Apple 式圆润美感
- 所有元素扁平 2D，不使用 3D 光影/高光/立体渲染
- Gaussian 必须画成扁平纯色 2D 椭圆，绝对禁止画成 3D 球体/有高光的球/有光影的椭球
- 不同颜色深浅代表不同密度高低
- 模块框：12px 大圆角，1px 边框 + 浅色填充
- 公式框：8px 圆角，浅灰或浅绿背景
- 箭头：1.5-2px 圆润箭头，实线灰色/黑色=操作流，转折处圆角过渡
- 文字尽量精简，强调视觉元素表达
- 图例融入面板空白区域，不独占一行或一列
- 不使用 emoji、卡通元素
- 不使用蓝色 #1F77B4（属于 SPS）、橙色 #F57F17（属于 GAP）
- 质量对标 CVPR/NeurIPS 顶会论文配图
- 严禁出现 (a)(b)(c) panel 编号
- 严禁出现 dataset 名、view 数、PSNR、SSIM、K-Planes 分辨率具体数值
