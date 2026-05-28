# 顶会科研示意图绘图规则

把成功的「2 行 × 3 列」范式固化为后续**比较类 figure**默认模板，避免回到 4-panel 拥挤 icon 风。所有 `intro_*`、`method_*`、`experiment_*` 章节里需要做并排对照的示意图，默认按本节出。

## 风格基准

- 视觉参考：X-Gaussian (ECCV 2024) Figure 1
- 整体观感：白底、极简、几何化、印刷友好；像顶会论文 teaser，不像产品介绍页

## 元素分工硬规则

- **实物**（玩具、头骨、phantom、CT slice、真实器官切片）→ 用真实照片或近似真实渲染；只有在「这就是物体本身」时才用图像
- **抽象量**（射线、Gaussians、capacity 分布、流程、模块、梯度、概率密度等）→ 一律用色块、椭球、线、点、箭头、常见图例
- **区分手段**只允许：实线 / 虚线、纯色 / 渐变、颜色、形状；不允许靠材质感、纹理、阴影、霓虹做区分
- 同一物体跨列出现时：最左列用真实照片，右侧列改为同一物体的灰色线稿轮廓，保持几何对应

## 禁用清单

- 彩虹渐变、霓虹色、red-yellow 热力图（除非显式做误差可视化）
- 3D 软阴影、玻璃质感、塑料反光
- UI 卡片、SaaS 截图风、dashboard 风
- 解释漫画、人物、表情符号
- 技术博客封面风、知乎 / Medium 头图风

## 网格规范（比较类默认模板）

- 默认 2 行 × N 列（N 通常 3）
- 左侧加 rotated 90° 行标签柱（如 `Visible Light` / `X-ray`），加粗，颜色与该行主色一致
- 顶部居中加粗列标题（如 `Imaging Physics` / `Where Capacity Sits` / `Method`）
- **严禁图内 (a)(b)(c) panel 编号**：列标题与行标签已经足够定位，再加 panel 字母会和 caption 冲突
- 上下行严格等宽等高对齐；列间留白一致
- 实物照片只出现在最左列；右侧列同一物体用纯线稿轮廓
- 图整体宽高比建议 16:7 ~ 17:8，便于占双栏顶部

## 固定调色板

- 蓝 `#1F77B4`：X-ray 路径 / SPS
- 橙 `#FF7F0E`：可见光路径 / GAP
- 绿 `#2CA02C`：XRA-GS（我们方法）/ ADM
- 红 `#D62728`：naïve baseline 的失效现象（仅用于误差/失败标注）
- 灰 `#888888` / `#BFBFBF`：物体轮廓、辅助线、参考网格

## 文字烘焙（写入图像）规范

- **可以烘焙**：短公式（`C=ΣT_iα_ic_i`、`−log(I/I_0)=∫μdl`）、模块短名（`SPS` / `GAP` / `ADM`）、轴标短词（`x`, `μ(x)`）
- **绝不烘焙**：dataset 名 / view 数 / baseline 名 / PSNR / SSIM 数值 / 任意句子级文字 / caption 文字。这些一律由 LaTeX 在外面加 `\node`、`\caption`、`\put` 标注
- 烘焙文字字号至少要在 1/3 尺寸缩印后仍清晰可读

## SPS / GAP / ADM badge 规范

- 只在「我们方法」那一列出现一次，**不**散布在多 panel 强化记忆
- 三个 badge 等高、白底、圆角矩形（半径约高度 30%），仅描边颜色不同（蓝 / 橙 / 绿）
- 排列顺序固定 `SPS → GAP → ADM`，水平等距，下方可配单箭头串起来
- 字体一致；不加 emoji、不加图标、不加阴影

## caption 规范

- 长度 ≤ 3 句，自包含可读
- 第 1 句概括对比对象与核心 dichotomy；第 2 句解释中间列「capacity 分布」差异；第 3 句给出本方法如何对齐
- **不允许**在 caption 里逐列详细描述每个 panel；非要逐列展开 → 当前 figure 信息量过载，拆成两张图
- 不写「图中展示了……」「我们绘制了……」这类冗余引导

## 可复用模板

- 比较类 (intro teaser)：列 = `Imaging Physics | Where Capacity Sits | Method`，行 = `Visible Light | X-ray`
- pipeline 图：横向 `Input → SPS → GAP → ADM → Output`，每模块一个 badge，下方对应中间产物缩略
- 定性对比 (experiments)：行 = method（`XRA-GS` + 6 baseline + `GT`），列 = view 数或 organ；不混合行列含义
- 误差/失败案例：用红色 `#D62728` 描边或叠加误差热力图，仅在 experiments 或 discussion 出现

## 迭代纪律

- 出图后做 30 秒可读性测试：让不读正文的人看 30 秒，是否能复述图的核心 dichotomy
- 不能 → 修 prompt 再出，遵守 [[image2_workflow]] 的三次法则
- 每次重出前先回看本文件的调色板、网格规范、文字烘焙清单，避免迭代过程中悄悄走偏
