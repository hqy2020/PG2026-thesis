# intro_fig_compare — image2 绘图提示词（顶会风格 2×3 版 v3）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- Introduction 章节首图（teaser），与 intro 改写后的 Para 2（imaging-physics gap：α-compositing 有遮挡 vs X-ray line integral 无遮挡）和 Para 3（继承梯度规则在线积分渲染下仍导致 capacity misallocation）严格绑定。
- 风格基准：参考 X-Gaussian (Cai et al., ECCV 2024) Figure 1 的顶会示意图风格——**实物（玩具 / 头骨）用照片，其余抽象量（射线、Gaussians、capacity）一律用色块、椭球、线、点、常见图例**；区分仅靠实/虚线、渐变、颜色。
- 关键设计原则：字少、要素少、对比强；整图只讲机制，绝不出现实验性内容（不画合成投影、不画与 GT 的残差热力图、不写任何 dataset / view 数 / baseline / 指标）。
- 与本 prompt 一起阅读：`main.tex` 第 60–88 行（intro 改写后版本）、CLAUDE.md §1 / §2 / §7 / §12。
- 默认出图通道：`gpt-image-2` skill。
- 输出文件名保持 `intro_fig_compare.png`；本次为第二次覆盖，旧 backup 已删除，按 CLAUDE.md §8.1「已存在 backup 时不再覆盖 backup」**不重建 backup**，直接覆盖。

## 总版式

- 整体布局：**2 行 × 3 列网格**，上下行平行、列对齐、等宽等高。
- 图幅宽高比约 **17 : 7.5**（约 1700 × 750 px，dpi ≥ 300），白底。
- 左侧留一道行标签柱（rotated 90°）：
  - 上行标签：`(a) Visible Light`
  - 下行标签：`(b) X-ray`
- 三列共享顶部小标题（居中、加粗 sans-serif，8–9pt）：
  - Col-1：`Imaging Physics`
  - Col-2：`Where Capacity Sits`
  - Col-3：`Method`
- 上下行之间不强制水平虚线分隔；行标签柱本身已经把两行视觉分开。

## 每个 panel 的内容（顶会简洁示意图风）

### Row (a) Visible Light

| Panel | 视觉构成 |
|---|---|
| (a) Col-1 *Imaging Physics* | 左侧一个小相机三角图标 → 一束橙色实线 ray 射向一个**实物玩具照片**（推荐：乐高小推土机或同类彩色玩具，参考 X-Gaussian Fig.1 上行用过的素材风格）的可见表面；ray 在表面停止（用一个加粗的橙色圆点标"hit point"）。面板上方一行 LaTeX 风格公式：`C = Σ Tᵢ αᵢ cᵢ,  Tᵢ = ∏(1 − αⱼ)`；面板底部一行加粗深灰小字：`occlusion: front blocks back`。 |
| (a) Col-2 *Where Capacity Sits* | **同一玩具的纯线稿轮廓**（不再使用照片，灰色 0.8pt 细线 outline）。橙色实心椭球（Gaussians）密集**贴附在轮廓的外表面一圈**，内部基本为空；右下角放一个极小图例：一个橙色椭球 + 文字 `● Gaussian on surface`。 |
| (a) Col-3 *Method* | 几乎留白：面板中心仅一行灰色斜体小字 `natural fit — no realignment needed`，外加一个浅灰色对勾 `✓`；不画任何回路 / 箭头 / badge。目的是让读者一眼看出"可见光行不需要修正"，从而对照下行 X-ray 行的 Method 列。 |

### Row (b) X-ray

| Panel | 视觉构成 |
|---|---|
| (b) Col-1 *Imaging Physics* | 左侧一个小蓝色圆点作为 X-ray source → **一束蓝色实线 ray 贯穿一张半透明头骨实物照片**（参考 X-Gaussian Fig.1 下行的 skull 风格），ray 不在表面停止、整条射线穿过头骨抵达右侧一个小灰色 detector 像素方块；ray 颜色保持均匀（不要渐变），强调"无遮挡、order-independent"。面板上方一行公式：`−log(I / I₀) = ∫ μ(x) dl`；面板底部一行加粗深灰小字：`no occlusion: all path Gaussians contribute`。 |
| (b) Col-2 *Where Capacity Sits* | 同**头骨的纯线稿轮廓**（与 (b) Col-1 同形，灰色 0.8pt outline）；**红色实心椭球（Gaussians）仍然聚集在颅骨/软组织高对比度边界上**，内部沿穿透路径基本为空；用一条贯穿头骨内部的蓝色虚线提示"deep-path interior 应该有 capacity 但被忽略了"；右上加粗红色小字 `naïve gradient-driven densification → boundary clustering`；右下角小图例：一个红色椭球 + 文字 `● Gaussian on boundary`。 |
| (b) Col-3 *Method* | 同头骨线稿轮廓；**绿色实心椭球沿那条贯穿头骨的射线均匀分布**（从入射点到出射点连续覆盖深部），边界处只有极少数椭球；上方加粗深绿小字 `XRA-GS: path-anchored capacity`；面板右下角放 3 个等高、白底、圆角矩形 badge，仅描边色不同，水平排列：第 1 个蓝色描边 `#1F77B4` `SPS`，第 2 个橙色描边 `#FF7F0E` `GAP`，第 3 个绿色描边 `#2CA02C` `ADM`；badge 下方一行更小字 `seed · prune · refine`。 |

## 配色规范（4 色 + 中性灰）

- 橙 `#FF7F0E`：可见光 ray、(a) Col-2 surface Gaussians、(a) hit point
- 蓝 `#1F77B4`：X-ray ray、X-ray source 点、(b) Col-2 内部虚线、SPS badge 描边
- 红 `#D62728`：(b) Col-2 boundary-clustered Gaussians 与 naïve 标注
- 绿 `#2CA02C`：(b) Col-3 path-anchored Gaussians、XRA-GS 标注、ADM badge 描边
- 中性灰 `#888888` / `#BFBFBF`：phantom / 头骨 / 玩具的纯线稿轮廓、行列标签、公式、底部说明文字、detector 方块
- 不使用：彩虹渐变、霓虹色、热力图（red-yellow heatmap）、3D 阴影、UI 卡片背景

## 线型规范

- **实线** = 实际物理射线（橙色 = visible light ray；蓝色 = X-ray ray）
- **虚线** = 概念性提示路径（如 (b) Col-2 中贯穿头骨的蓝色虚线，提示 deep-path interior 应有 capacity）
- 实物照片仅用于 (a) Col-1 玩具 与 (b) Col-1 头骨；其他 panel 中同一物体一律改成**纯线稿轮廓**（灰 0.8pt outline），让读者直接对比"capacity 落点"

## 字体与字号

- 字体：sans-serif（Helvetica / Arial 系），与 LaTeX 正文 sans-serif 视觉接近
- 行标签柱：10pt 粗体；列顶部小标题：8–9pt 粗体；公式：8pt LaTeX 风格；panel 底部说明文字：7–8pt 加粗深灰；图例 / badge 内文：7pt 常规
- panel 标号系统只有「行标签 + 列标题」两层；**严禁**在图内出现 `(a)(b)(c)` 这种独立 panel 编号

## 输出要求

- 格式：PNG，白底，dpi ≥ 300
- 尺寸：约 1700 × 750 px（宽高比 ≈ 17 : 7.5），适配 `\textwidth` 引入
- 文件名：`intro_fig_compare.png`，落地路径 `assets/fig/intro_fig_compare.png`
- 覆盖策略：**不重建 backup**（旧 backup 已删除，按 §8.1 规则直接覆盖现图）

## 反例 / 禁止事项

- 严禁画合成 X-ray 投影、严禁画 GT 残差热力图
- 严禁出现 (a)(b)(c) panel 编号、严禁出现 dataset / view 数 / baseline / PSNR / SSIM
- 严禁把 caption 文字烘焙进图里
- 严禁把 SPS / GAP / ADM 散布在多个 panel；只在 (b) Col-3 右下角 badge 出现一次
- 严禁上下行只是"颜色换皮"——上下行差异必须落在三件事上：**Col-1 物理（occlusion vs no occlusion + 公式不同） / Col-2 capacity 落点（surface vs boundary） / Col-3 方法（natural fit vs SPS·GAP·ADM）**
- 严禁卡片式 UI、SaaS 截图风、技术博客封面风、彩虹渐变、霓虹、3D 阴影、解释漫画风
- 严禁把实物照片用在 Col-2 / Col-3 —— 这两列一律纯线稿轮廓 + 抽象元素

## 30 秒可读性测试（验收标准）

把生成的 png 单独给一个不读正文的人看 30 秒，他应当能复述出：

> 上行可见光：α-compositing 让前面的 Gaussians 遮挡后面，所以 Gaussians 只需要分布在表面就够了，因此 Method 列是"无需修正"。
> 下行 X-ray：line integral 让整条射线上的所有 Gaussians 都贡献，但如果继承梯度驱动 densification，Gaussians 仍然堆在 boundary（红色椭球），留下深部射线空缺；XRA-GS 用 SPS · GAP · ADM 把 capacity 拉回沿路径分布（绿色椭球）。

若不能复述出这套对偶（occlusion vs line integral → surface vs path → no realignment vs SPS·GAP·ADM），说明三列对比不够显式，需要重出。

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

一张顶会论文用的科学示意图，干净纯白底，宽高比约 17:7.5。整图严格采用 2 行 × 3 列网格，上下两行严格平行、列对齐、等宽等高。左侧一道旋转 90 度的行标签柱，上行用深灰加粗写 `(a) Visible Light`，下行用深蓝加粗写 `(b) X-ray`。三列共享顶部小标题，居中加粗无衬线，从左到右依次为 `Imaging Physics`、`Where Capacity Sits`、`Method`。整图风格参考 X-Gaussian (ECCV 2024) 论文 Figure 1：实物对象用真实照片，其余抽象量一律用色块、椭球、线、点、常见图例；区分仅靠实/虚线、渐变、颜色。

**第 (a) 行 Visible Light。** Col-1 *Imaging Physics*：左侧一个小相机三角图标，从相机发出一束橙色实线 ray，撞到一张彩色乐高玩具推土机照片的可见表面就停下，停止处放一个加粗橙色圆点。面板上方写公式 `C = Σ Tᵢ αᵢ cᵢ,  Tᵢ = ∏(1 − αⱼ)`，面板底部加粗深灰小字 `occlusion: front blocks back`。Col-2 *Where Capacity Sits*：同一玩具改成纯灰色 0.8pt 线稿轮廓（不要照片），约 20 个橙色实心椭球（Gaussians）密集贴附在轮廓外表面一圈，玩具内部基本为空；右下角小图例：一个橙色椭球 + 7pt 字 `● Gaussian on surface`。Col-3 *Method*：面板几乎留白，居中放一行灰色斜体小字 `natural fit — no realignment needed` 和一个浅灰对勾 `✓`，不画任何回路或 badge。

**第 (b) 行 X-ray。** Col-1 *Imaging Physics*：左侧一个小蓝色圆点作为 X-ray source，发出一束蓝色实线 ray，整条 ray 贯穿一张半透明侧位头骨实物照片（不要在表面停止），最终落到右侧一个小灰色 detector 像素方块上；ray 颜色保持均匀，不要渐变。面板上方写公式 `−log(I / I₀) = ∫ μ(x) dl`，面板底部加粗深灰小字 `no occlusion: all path Gaussians contribute`。Col-2 *Where Capacity Sits*：同一头骨改成纯灰色 0.8pt 线稿轮廓（不要照片），红色实心椭球（Gaussians）仍然聚集在颅骨与软组织高对比度边界上，头骨内部沿原 ray 方向基本为空；用一条贯穿头骨内部的蓝色虚线提示"deep-path interior 应该有 capacity 但被忽略了"；右上加粗红色小字 `naïve gradient-driven densification → boundary clustering`；右下角小图例：一个红色椭球 + 7pt 字 `● Gaussian on boundary`。Col-3 *Method*：同一头骨线稿轮廓；约 20 个绿色实心椭球沿那条贯穿头骨的射线均匀分布（从入射点到出射点连续覆盖深部），边界处只剩极少数椭球；上方加粗深绿小字 `XRA-GS: path-anchored capacity`；面板右下角水平排列 3 个等高、白底、圆角矩形 badge，仅描边色不同：蓝描边 `#1F77B4` 写 `SPS`，橙描边 `#FF7F0E` 写 `GAP`，绿描边 `#2CA02C` 写 `ADM`；badge 正下方一行更小字 `seed · prune · refine`。

**风格强约束。** 白底干净；仅允许使用以下有限调色板：橙 `#FF7F0E`（visible-light ray、(a) Col-2 surface Gaussians、hit point）；蓝 `#1F77B4`（X-ray ray、X-ray source、(b) Col-2 内部虚线、SPS badge 描边）；红 `#D62728`（(b) Col-2 boundary 椭球与 naïve 标注）；绿 `#2CA02C`（(b) Col-3 path-anchored 椭球、XRA-GS 标注、ADM badge 描边）；中性灰 `#888888`/`#BFBFBF`（玩具与头骨的纯线稿轮廓、行列标签、公式、底部说明、detector）。绝不使用红黄热力图、彩虹渐变、霓虹、3D 阴影、UI 卡片背景、解释漫画风。实物照片仅出现在 (a) Col-1 玩具与 (b) Col-1 头骨两处；Col-2 与 Col-3 中同一物体一律改成纯线稿轮廓。线型规范：实线 = 实际物理射线；虚线 = 概念性提示路径。全图统一无衬线字体（Helvetica/Arial 风格）。严禁出现 `(a)(b)(c)` 这种独立 panel 编号；标号系统只有「左侧行标签 + 顶部列标题」两层。图中严禁出现 dataset 名、view 数、baseline 方法名、PSNR、SSIM；严禁画合成 X-ray 投影；严禁画与 GT 的残差热力图；严禁把 caption 文字烘焙进图。最终目标：一个完全不读正文的人 30 秒内能复述——可见光因 α-compositing 有遮挡，Gaussians 只需贴表面，Method 列无需修正；X-ray 因 line integral 无遮挡，整条射线上所有 Gaussians 都应贡献，但 naïve 梯度驱动仍把 Gaussians 推到 boundary 留下深部空白，XRA-GS 用 SPS·GAP·ADM 把 capacity 重新沿路径分布。
