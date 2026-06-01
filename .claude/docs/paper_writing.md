# 顶会论文写作要求

默认目标：把 `PG2026` 写成符合英文顶会审稿预期的论文，不是技术博客也不是期刊式综述。凡是「润色」「重写」「补图」「补表」「整理版式」类请求，若用户未指定，统一按本节执行。

## 行文要求

- 全文默认英文；当前草稿中文部分仅视为过渡稿，定稿统一改写为顶会英文表达。覆盖标题/摘要/引言/related/method/experiments/conclusion 以及图注表注
- 摘要骨架：`problem → gap → core insight → method → strongest evidence`
- 引言骨架：先交代任务价值与难点 → 指出已有方法缺口 → 引出 `RAttAGS` 核心思想与三点贡献
- 学术语气：克制、证据对齐、审稿人友好；不要教程口吻 / 经验分享口吻 / 产品介绍口吻
- **禁用破折号 `---`（em-dash）**：AI 味过重；改用逗号、分号、括号或拆句重写
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
   - 末段必须收束到「三阶段错误分配 → SPS/GAP/ADM」与 `RAttAGS`，与 §3 Method 硬连接

每段末尾用**一句轻量桥接句**点出局限、引出下一段；不重复 intro 论点，不预告 method 细节。

句式可借鉴 R²-Gaussian §2 / CoR-GS §2 / X-Field §2 / X²-Gaussian §2 的扩展列举节奏，但全部改写为 `RAttAGS` 口径，**保持 §14 物理论证骨架**（attenuation-aligned，不写 attenuation-aware；禁用 fortunate coupling / replace the densification mechanism）与 §15 术语（`Gaussians` 不写 `primitive`）。

引用建议合并到一个 `\cite{a,b,c}`，避免单段散落 5+ 个 `\cite`。

### 同行工作叙述语气（2026-05-28 增补）

- 讨论同行 sparse-view / X-ray Gaussian 工作时，默认采用"不同角度都可能成立 + 实验已证 work"的平和措辞：`approach this limitation from complementary angles` / `explores a similarly diverse set of perspectives` / `these different angles all yield empirical gains, which suggests ... multiple compatible explanations rather than a single root cause`。
- 避免"都错只有我们对"的语气：禁用 `inherits the same diagnosis`、`whether the remedy is X or Y, all share Z` 这类把同行论点压扁成单一 backbone 的句式。
- 在 §2.2 末尾必须显式衔接到我们的 `\adm`（"takes inspiration from this line of work / we adopt the lesson that ..."），让 K-Planes 的引用不再只是孤立顺带。

### Tomographic NVS 同类工作压缩节奏（2026-05-28 增补）

X-ray Gaussian / 隐式神经场同类工作在 Related Work 中按 implicit / explicit 两族归纳一句话即可，**不**逐方法细讲：

1. 一句任务背景 + 传统 FDK/SART 限制；
2. 一句 implicit 族：4 类技术路线（self-supervised sinogram / hash encoding / transformer 结构建模 / population-level encoder–decoder），单 `\cite{...}` 引一组；
3. 一句 explicit 族：3 类主线 (radiative kernel + rasterizer / integration-bias + voxelization / material-aware + segment-length) + 旁支 4 个 (discretized voxel / artifact-suppression / 4D / slice-wise) 括号内一笔免责"outside our sparse-view novel-view protocol, omitted from main comparison"；
4. 一句共性问题（focus 落在 imaging equation 或 kernel 上，不在 evolution rule）；
5. 一句 `\RAttAGS\` 代入（`\sps` / `\gap` / `\adm` 对齐 initialization / pruning / refinement 到 attenuation path）。

末尾不再展开三阶段诊断（这是与 §3 Method 的硬连接，但要简短），避免重复 intro。

## Method 章节密度（2026-05-28 落定，对齐 R²GS §3+§4.1 / X-Field §3.1）

§3 Method 总长度目标 **≈ 1.5 页**，结构固定：

1. `§ Preliminary`（半页）：分两段 paragraph，不再分小节
   - 段 A：X-ray attenuation imaging（Beer–Lambert + 对数化，1 公式：`−log(I/I₀)=∫μdl`）
   - 段 B：Radiative Gaussian backbone（核函数 + 密度场 + 渲染算子，2 公式：`G(x)`、`σ(x)=ΣG_i` / `Î=R(G;π)`）
   - 段末一句 problem statement：backbone 对齐了 renderer，本文要 realign 的是 evolution rule
2. `§ Overall Framework`（一段 + pipeline 图）：一句话串起 SPS→GAP→ADM 在 init/loop/refine 的位置；**不写 algorithm 伪代码块**
3. `§ SPS / § GAP / § ADM`：每模块一段 paragraph，结构「motivation 一句 + 单/双公式 + 一句作用机制」
4. `§ Training Loss`：单式 `L = L₁ + λ_d L_dssim + λ_v L_3DTV + λ_p L_pTV` + 一句各项含义；不再拆 4 个 align 子公式

### 公式瘦身规则

| 模块 | 保留 | 删除 |
|---|---|---|
| Preliminary | Beer–Lambert / Gaussian kernel / 密度场 / 渲染算子 共 3 式 | 视觉光 α-compositing（已在 intro 提到名字） |
| SPS | 单式 `q(x)=α/\|Ω\|+(1−α)V_FDK(x)^γ/Z` | α、γ 数值 / 50K 初值 / "small local search" 描述 |
| GAP | `d_i=⟨‖p_i−p_j‖⟩_{j∈N_K(i)}` + `c_i={1 if d_i<τ ∧ ḡ_i<δ}` | τ、δ、K、β_prune 数值 / Σ shrink 公式 / [2K,20K] 区间 |
| ADM | `F(x)=concat(bilinear)` + `ρ_final=ρ_base(1+g(Δσ−Δσ̄))` | β(t) 三段调度 / s_view 数值 / r_max / warm-up·hold·decay 描述 |
| Loss | 单 L 公式 | 4 个子损失的 align 块 |

### 超参数清零（论文不是技术报告）

正文严禁出现以下技术报告式描述（一律下沉到补充材料或代码）：

- 具体数值：`50K initial Gaussians` / `2K, 20K iterations` / `α = 0.2` / `γ = 1.0` / `K = 5` / `τ = 0.05` / `δ = 0.0002` / `β_prune = 0.03` / `s_view = {0.5, 0.7, 1.0}` / `gap_scale_shrink_factor = 0.8` 等
- 训练调度：`warm-up phase` / `hold phase` / `exponential decay` / `[2K, 20K] interval` 等
- 实现枝节：`small local search` / `bilinear interpolation` 作为独立强调 / 内存优化技巧
- 验证命令：`grep -n -E "50K|2K|20K|warm-up|hold phase|exponential decay" main.tex` 在 §3 范围内应清零

### 代码-论文对齐措辞（不写超参数但学术化提及机制）

公式与文字必须与 GitHub 代码（`hqy2020/PG2026`）实现对齐，**但学术化为机制描述**而非配置项。例：

- SPS 写「density-weighted mixture distribution that interpolates between a uniform prior and a power-shaped attenuation profile」（对齐 `initialize_pcd.py` 的 `weights^γ` + `uniform_ratio` + `density_rescale`，不写出 γ / α / 50K）
- GAP 写「flag Gaussians that are simultaneously locally crowded and recently inactive as redundancy candidates, prune a bounded fraction per cycle, slightly contract the covariance of retained neighbors」（对齐 `proximity_densifier.py` 双条件 + shrink，不写 K / τ / δ / β_prune）
- ADM 写「dual-head MLP outputs a density offset and a confidence gate; the offset is batch-centered and applied as a relative modulation, with magnitude scaled by the number of input views」（对齐 `kplanes.py` + `gaussian_model.py` 双头 + zero-mean + view-adaptive，不写 K-Planes 分辨率 / r_max / s_view）

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
- 标题正确显示为 `RAttAGS: X-Ray Attenuation-Aligned 3D Gaussian Splatting for Sparse Tomographic View Synthesis`
- figure / table 引用正常
- 没有因图表拆分造成缺图、缺表、编号错乱
