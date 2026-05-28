# 顶会论文写作要求

默认目标：把 `PG2026` 写成符合英文顶会审稿预期的论文，不是技术博客也不是期刊式综述。凡是「润色」「重写」「补图」「补表」「整理版式」类请求，若用户未指定，统一按本节执行。

## 行文要求

- 全文默认英文；当前草稿中文部分仅视为过渡稿，定稿统一改写为顶会英文表达。覆盖标题/摘要/引言/related/method/experiments/conclusion 以及图注表注
- 摘要骨架：`problem → gap → core insight → method → strongest evidence`
- 引言骨架：先交代任务价值与难点 → 指出已有方法缺口 → 引出 `XRA-GS` 核心思想与三点贡献
- 学术语气：克制、证据对齐、审稿人友好；不要教程口吻 / 经验分享口吻 / 产品介绍口吻
- 不写博客式铺垫，不用「我们来看看」「下面详细聊聊」「这个技巧非常直观」等衔接语
- 小节名、图注、表注使用论文式功能命名，不用吸睛标题或营销表达
- 文字组织成完整论证链，不只是高压缩信息密度；该展开处展开
- 若顶会写法与其他写法冲突，默认以英文顶会审稿阅读习惯为先

## 引言故事线（默认梯度）

允许在草稿设计阶段出现的桥接说法：
- `Novel View Synthesis → Sparse View Synthesis`
- `Novel View Synthesis → Tomographic Novel View Synthesis`
- `Sparse View Synthesis → Sparse Tomographic View Synthesis`

最终落点固定要求：
- 默认收束到 `Sparse Tomographic View Synthesis`
- 引言故事：从通用 NVS → 经 `Sparse View Synthesis` 与 `Tomographic Novel View Synthesis` 两条约束 → 汇合到本文 `Sparse Tomographic View Synthesis`

## Related Work 骨架（反向递进，2026-05-28 落定）

三段式，**从远到近**：

1. `Gaussian Splatting` — 底层工具
   - 引出 3DGS（`kerbl20233d`）+ surface / dynamic / SLAM / 3D 生成 / 效率扩展各一句
   - 末段收束到「densification 与 SH color 都假设 dense view + surface radiance」
2. `Sparse View Synthesis` — 稀疏视角下的退化与正则
   - NeRF 系（depth / semantic / patch+frequency）+ 3DGS 系（FSGS/CoR-GS/DNGaussian/DropGaussian + feed-forward 一族）+ K-Planes 复用提示（`fridovich2022kplanes` 标注 ADM 中复用）
   - 末段收束到「这些 sparse-view 方案仍共享 error/gradient-driven densification + 高对比度表面优先」
3. `Tomographic Novel View Synthesis` — X-ray/CT 物理特殊性
   - 传统 (FDK / SART) → 隐式 (IntraTomo / NAF / SAX-NeRF / Geometry-Aware) → 显式 radiative (X-Gaussian / R²-Gaussian / X-Field) + 旁支 (DGR / GR-Gaussian / X²-Gaussian / Layer-Based) 并附「不进入主比较」免责
   - 末段必须收束到「三阶段错误分配 → SPS/GAP/ADM」与 `XRA-GS`，与 §3 Method 硬连接

每段末尾用**一句轻量桥接句**点出局限、引出下一段；不重复 intro 论点，不预告 method 细节。

句式可借鉴 R²-Gaussian §2 / CoR-GS §2 / X-Field §2 / X²-Gaussian §2 的扩展列举节奏，但全部改写为 `XRA-GS` 口径，**保持 §14 物理论证骨架**（attenuation-aligned，不写 attenuation-aware；禁用 fortunate coupling / replace the densification mechanism）与 §15 术语（`Gaussians` 不写 `primitive`）。

引用建议合并到一个 `\cite{a,b,c}`，避免单段散落 5+ 个 `\cite`。

## 图片要求

- 图片服务论文论证而非展示感；优先支持方法流程、定性对比、误差分析、模块机制解释
- 同一组 figure 内的术语、字体、线宽、箭头、配色、panel 标号保持一致
- 干净白底、有限配色、清晰 panel 结构；避免博客封面式装饰、夸张渐变、卡片化 UI、解释漫画风
- caption 可独立阅读，说明 setting、比较对象、关键观察，不只一句泛化描述
- 图按期刊插图标准做可印刷、可缩放、可独立理解

具体绘图规则见 [[figure_design]]。

## 表格要求

- 主对比表、消融表、效率表分开，每表只承担一个核心论证任务
- 表头写清楚 dataset / views / metrics / unit，不依赖正文补充关键信息
- 默认把 best 结果突出显示，并保持命名、缩写、ablation 行名与正文完全一致
- 不把表格做成截图图像，不塞进大拼图 figure 凑版面
- 即使脱离正文，读者也能从 caption、表头、行名和注释看懂比较对象、设定和核心结论

## 排版要求

- 主文只保留最强证据；补充材料承接额外可视化、更多 case、扩展 ablation、实现细节
- figure/table 尽量靠近首次引用位置
- 整体阅读感受优先接近英文顶会论文
- 若用户只说「按论文标准改」「更学术一点」「更像正式投稿」，默认解释为「按英文顶会论文要求处理」

## 编译验证

只要改了标题、图注、表注、figure 引用或 table 引用，默认做最小验证：

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

验证目标：
- 标题正确显示为 `XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`
- figure / table 引用正常
- 没有因图表拆分造成缺图、缺表、编号错乱
