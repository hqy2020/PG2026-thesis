

## 核心结论

### 1. 方法名、任务名与标题命名固定

当前稿件的统一方法名是：

`XRA-GS`

当前稿件的统一任务名是：

`Sparse Tomographic View Synthesis`

命名顺序固定要求：
- 默认使用 `Sparse Tomographic View Synthesis`，即 `Sparse` 在前，`Tomographic` 在后
- `sparse-view` 是设定/条件描述，不是最终任务名本体；因此默认写 `sparse-view setting`、`sparse-view condition`、`sparse-view acquisition`
- 只要 `sparse-view` 作为复合形容词出现，就必须保留连字符 `-`

当前论文标题的默认准绳是：

`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`

标题命名补充约束：
- 默认使用 `attenuation` 作为核心物理关键词
- 在 `X-ray Attenuation-XXX Gaussian Splatting` 这组命名里，固定使用 `XXX = Aligned`
- 英文拼写默认使用 `X-ray`，与现有论文标题和 CT 术语用法保持一致；除非投稿模板或用户另行指定，否则不要改成其他大小写变体

CT 描述口径固定要求：
- 根据 `CT scan` 的标准定义，CT 是一种 `X-ray computed tomography`
- 其基本成像描述应默认写成：CT 通过从多个角度采集 X-ray attenuation measurements，并通过 tomographic reconstruction 形成 tomographic / cross-sectional images
- 因此，本文在引言和方法定义中默认把 CT 任务描述为 `tomographic`、`X-ray attenuation`、`multi-angle projections` 这一组概念
- 若需要区分任务目标与采集设定：任务名用 `Sparse Tomographic View Synthesis`，采集设定用 `sparse-view setting` 或 `sparse-view condition`

后续任何改动都必须同步检查以下位置，避免再次出现标题、图注、方法名不一致：
- `PG2026-thesis/main.tex` 的 `\title[...]{}`
- 正文中方法名、缩写、图注、表注
- 图中的方法标签
- 所有实验说明文档中的方法名

如果用户后续明确改标题，以用户最新指令为最高优先级；否则默认保持 `XRA-GS` 与上述标题不变。

### 2. 三个创新点固定为 SPS / GAP / ADM

`XRA-GS` 的方法主体默认由三个创新模块组成，不要在后续改稿中漂移成别的三件套，也不要遗漏其中任何一个：

- `SPS`：初始化模块，负责基于 FDK 粗重建提供的前景支撑与粗衰减轮廓进行路径锚定初始化
- `GAP`：结构控制模块，负责回收边界附近由误差/梯度驱动带来的冗余高斯
- `ADM`：细化模块，负责基于连续空间上下文做位置相关的密度调制与局部稳定细化

后续写作统一要求：
- 正文介绍创新点时，默认就是这三个模块，顺序也默认按 `SPS -> GAP -> ADM`
- 图中模块名、表格中的 ablation 行名、补充材料中的小节名，统一使用 `SPS / GAP / ADM`
- 如果做消融，优先使用 `w/o SPS`、`w/o GAP`、`w/o ADM`、`full XRA-GS` 这类一致命名
- 不要把 `XRA-GS` 和三个模块写成互相替代关系；`XRA-GS` 是总方法名，`SPS / GAP / ADM` 是其内部三个核心创新点

### 3. 图片、表格、数据、脚本必须分离

这篇稿件后续统一执行“图片、表格分离”原则，不再把它们混成一个笼统的“图表”产物。

硬规则：
- 图片资产只放在 `PG2026-thesis/assets/fig/`
- 表格资产只放在 `PG2026-thesis/assets/tables/`
- 数值结果、实验原始数据和可视化中间文件只放在 `PG2026-thesis/assets/data/`
- 只有在需要基于 `assets/data/` 生成实验图，或者对现有数据做可重复检查时，才在 `PG2026-thesis/assets/scripts/` 下写 Python；其他正文、图注、表注和版式修改一律直接改 `tex`
- 图片一律作为 figure 处理，使用 `\includegraphics`
- 表格一律作为 table 处理，优先使用独立的 `tab_*.tex` 文件并由 `\input{assets/tables/...}` 引入
- 不要把表格截图塞进图片里，除非用户明确要求做成可视化 figure
- 不要把多张定性图和定量表揉成一个混合版式来凑“图表”

写作规则：
- 讨论实验重构时，单独列“图片计划”和“表格计划”，不要混写
- 主文中先明确该证据属于 qualitative figure 还是 quantitative table，再决定放图还是放表
- caption 中不要把 figure/table 混称为“图表”

### 4. 不要git查找过期的文件

尽量不要git log 查找过期的文件，否则会导致错误。

### 5. 单一事实源

后续协作时，以下文件是优先检查对象：
- 主稿源文件：`PG2026-thesis/main.tex`
- 图片目录：`PG2026-thesis/assets/fig/`
- 表格目录：`PG2026-thesis/assets/tables/`
- 数据目录：`PG2026-thesis/assets/data/`
- 脚本目录：`PG2026-thesis/assets/scripts/`

如果 Markdown 讨论文档与 `main.tex` 冲突，以用户最新要求和 `main.tex` 最终落地结果为准，并及时同步说明文档。

### 6. 修改后的最低验证

只要改了标题、图注、表注、图片引用或表格引用，默认做一次最小验证：

```bash
cd PG2026-thesis
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

验证目标：
- 标题正确显示为 `XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`
- figure 引用正常
- table 引用正常
- 没有因为图表拆分造成缺图、缺表、编号错乱

### 7. 参考论文语料是固定风格锚点

当前目录下 `参考论文/` 中这批论文，默认作为 `PG2026` 后续写作与实验呈现的固定参考语料。后续如果用户说“对齐顶会风格”“参考这些论文整理”，默认就是参考这批语料，而不是参考技术博客、教程贴或产品文案。

固定参考名单：
- `参考论文/Corgs.pdf`：`CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization`
- `参考论文/DGR.pdf`：`Discretized Gaussian Representation for Tomographic Reconstruction`
- `参考论文/dngs.pdf`：`DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization`
- `参考论文/FSGS.pdf`：`FSGS: Real-Time Few-shot View Synthesis using Gaussian Splatting`
- `参考论文/GR.pdf`：`GR-Gaussian: Graph-Based Radiative Gaussian Splatting for Sparse-View CT Reconstruction`
- `参考论文/LB.pdf`：`Layer-Based 3D Gaussian Splatting for Sparse-View CT Reconstruction`
- `参考论文/r2gs.pdf`：`R2-Gaussian: Rectifying Radiative Gaussian Splatting for Tomographic Reconstruction`
- `参考论文/x2gs.pdf`：`X2-Gaussian: 4D Radiative Gaussian Splatting for Continuous-time Tomographic Reconstruction`
- `参考论文/XField.pdf`：`X-Field: A Physically Informed Representation for 3D X-ray Reconstruction`
- `参考论文/xgs.pdf`：`Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis`
- `参考论文/XLRM.pdf`：`X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second`

使用原则：
- 这些论文首先是“风格锚点”和“呈现锚点”，用于对齐论文行文、图片组织、表格设计、版式节奏
- 这些论文不是 `XRA-GS` 的事实源替代品；涉及我们方法、实验、数据、结论时，仍以 `PG2026-thesis/main.tex`、当前图、当前表为准
- 可以借鉴它们的叙述密度、图表结构、caption 写法和主文/补充材料取舍，但不要直接复制其措辞、贡献表达或视觉排版细节

### 8. 默认按英文顶会论文要求组织文字、图片、表格、排版

后续默认目标不是把 `PG2026` 写成技术博客，也不是写成偏期刊式的长篇综述，而是把它写成符合英文顶会审稿预期的论文。凡是“润色”“重写”“补图”“补表”“整理版式”这类请求，若用户没有另行指定，统一按下面标准执行。

行文要求：
- 论文全文文字默认使用英文撰写；若当前草稿含有中文，只将其视为中间过渡稿，后续定稿需统一改写为符合英文顶会要求的英文表述。这一要求覆盖标题、摘要、引言、related work、method、experiments、conclusion 以及图注、表注等全文文字部分
- 摘要优先采用英文顶会论文可接受的 `problem -> gap -> core insight -> method -> strongest evidence` 骨架
- 引言优先先交代任务价值与难点，再指出已有方法缺口，再引出 `XRA-GS` 的核心思想与三点贡献
- 正文默认使用克制、证据对齐、审稿人友好的学术语气，不写成教程口吻、经验分享口吻或产品介绍口吻
- 不写博客式铺垫，不用“我们来看看”“下面详细聊聊”“这个技巧非常直观”这类技术博客衔接语
- 小节名、图注、表注优先使用论文式功能命名，不用吸睛标题、口语化标题或营销式表达
- 默认把文字组织成更适合期刊阅读的完整论证链，而不是只追求 conference 式的高压缩信息密度；该展开处展开，该交代实验设定、局限性和观察时要交代清楚
- 若更紧凑的顶会写法与其他写法冲突，默认以英文顶会审稿阅读习惯为先：更强调叙述完整性、图表自解释性、实验设定透明度和讨论闭环

引言故事线默认按以下梯度组织，并且这些桥接说法都允许在草稿设计阶段出现：
- `Novel View Synthesis -> Sparse View Synthesis`
- `Novel View Synthesis -> Tomographic Novel View Synthesis`
- `Sparse View Synthesis -> Sparse Tomographic View Synthesis`

最终落点固定要求：
- 默认把上述桥接收束到 `Sparse Tomographic View Synthesis`
- 引言里要把故事讲成：从通用 `Novel View Synthesis`，过渡到 `Sparse View Synthesis` 与 `Tomographic Novel View Synthesis` 这两条约束，再汇合到本文的 `Sparse Tomographic View Synthesis`
- 后续若用户要求“按这版要求改成英文翻译并润色”，默认就是按这套任务命名、CT 描述和 intro 故事线来统一重写当前论文英文表述

图片要求：
- 图片默认服务于论文论证，而不是服务于展示感；优先支持方法流程、定性对比、误差分析、模块机制解释
- 同一组 figure 内的术语、字体、线宽、箭头、配色、panel 标号保持一致
- 优先使用干净白底、有限配色、清晰 panel 结构，避免博客封面式装饰、夸张渐变、卡片化 UI、解释漫画风
- caption 需要可独立阅读，说明 setting、比较对象、关键观察，而不是只写一句泛化描述
- 图默认按期刊插图标准追求可印刷、可缩放、可独立理解；避免只在大屏展示时好看、缩小后信息就失真的排版

表格要求：
- 主对比表、消融表、效率表默认分开，各表只承担一个核心论证任务
- 表头中写清楚 dataset / views / metrics / unit，不依赖正文补充关键信息
- 默认把 best 结果突出显示，并保持命名、缩写、ablation 行名与正文完全一致
- 不把表格做成截图图像，不把表格塞进大拼图 figure 里凑版面
- 表格默认满足顶会审稿中的独立可读性：即使脱离正文，读者也能从 caption、表头、行名和注释看懂比较对象、设定和核心结论

排版要求：
- 主文只保留最强证据，补充材料承接额外可视化、更多 case、扩展 ablation 和实现细节
- figure/table 尽量靠近首次引用位置，避免读者在正文和附页之间来回跳转
- 整体 PDF 阅读感受应优先接近英文顶会论文，而不是博客长文、实验笔记、技术方案说明书或只偏期刊式铺陈的写法
- 若用户只说“按论文标准改”“更学术一点”“更像正式投稿稿件”，默认解释为“按英文顶会论文要求处理”，除非用户随后明确指定其他 venue 或风格

### 9. 生成式图片的默认协作约定

当任务涉及“辅助生成论文用图片”“生成概念图底图”“生成定性图素材”“补充视觉化示意”时，默认约定如下：
- 默认优先使用openai的 `image2` 模型生成图片
- 默认导出格式为 `png`
- 默认把生成结果视为 figure 素材，而不是直接替代最终论文排版成品
- 默认落地到 `PG2026-thesis/assets/fig/`，并继续通过论文工作流统一加 panel 标号、caption、方法标签和版式编排
- 如果图片里包含论文术语、模块名、坐标轴、数字标注，优先把这些文字后置到排版阶段处理，不依赖生成模型直接烘焙到位
- 如果当前会话工具链不支持 `image2`，需要显式说明并退回到可用图像工具，但目标输出仍以 `png` 素材为准

### 10. 对比实验协议默认锁定

后续只要涉及主文实验、实验规划、结果汇报、表格设计、图注撰写或摘要中对实验结论的概括，默认采用下面这套固定协议，避免对比对象、指标、数据设定来回漂移。

固定对比方法：
- `CoR-GS`
- `DNGaussian`
- `FSGS`
- `R2-Gaussian`
- `X-Gaussian`
- `X-Field`

对比规则：
- 默认主对比实验就是上述 6 个方法，不再临时替换成别的方法集合
- 如果后续需要补充额外 baseline，默认放在补充材料或经用户明确指令后再进入主文
- 主文中的 qualitative figure、quantitative table、caption、正文分析、摘要结果概述，默认都围绕这 6 个方法展开
- 方法名统一使用论文名对应的标准写法，不混用文件名、缩写变体或临时别名

主指标规则：
- 主指标固定为 `SSIM2D` 和 `PSNR2D`
- 主文表格、结果分析、摘要/引言中提炼实验结论时，优先围绕 `SSIM2D` 和 `PSNR2D` 组织
- 若后续需要报告额外指标，默认将其视为辅助指标，不能盖过 `SSIM2D` / `PSNR2D` 的主指标地位
- 默认保持指标命名统一，不写成 `SSIM` / `PSNR` 的模糊形式，除非上下文已经明确限定为 2D 投影指标

测试设定规则：
- 测试数据集默认是 `5` 个器官
- 视角设置默认固定在 `2`、`3`、`4` 视角
- 主对比表、主结果图、摘要中提到的 strongest result、引言中概括的实验结论，默认都应建立在这套 `5 organs x {2,3,4} views` 设定上
- 若某个结果不是来自这套设定，正文和 caption 中必须显式标明，避免和默认主设定混淆

呈现要求：
- 设计主表时，优先让读者一眼看出 `2/3/4` 视角下、`5` 个器官上的 `SSIM2D` / `PSNR2D` 对比结果
- 写实验段落时，优先总结跨视角趋势、极稀疏视角表现、以及在 `5` 个器官上的整体稳定性
- 若需要压缩主文篇幅，优先保留这套固定协议下最强的 figure/table，把更细的扩展分析放进补充材料

## 推荐工作方式

当任务涉及实验呈现重组时，优先按下面结构输出：

1. 图片侧要补什么
2. 表格侧要补什么
3. 哪些证据必须进主文，哪些适合补充材料

不要直接给一个混杂的“图表优化建议”大列表。
