# Related Work Todo（2026-05-21 snapshot）

> 单节路线图。综合视图见 [[experiment_REVIEW_2026-05-21_section-issues]] §3。
> ID 沿用 `R*` 系列。

## 1. 当前状态

- **主稿位置**：`main.tex` L85–97（`\section{Related Work}`）。
- **文字**：两个子小节 `Sparse-view NVS` + `X-ray NVS and Tomographic Reconstruction`；篇幅紧凑（约 3 段）。
- **覆盖**：FSGS / CoR-GS / DNGaussian 在 sparse-view NVS 中提及；X-Gaussian / R²-Gaussian / X-Field / X²-Gaussian / DGR 在 X-ray 小节提及；GR-Gaussian 末尾一笔带过；Layer-Based 未提及。
- **引用完整性**：6 个对比方法的 `\cite{}` key 均存在 `references.bib` 中（已在 section-issues 阶段核实）。
- **图表 / 数据**：本节无图无表。

## 2. 顶会标准目标

- G-R1：读完 related 即可预判 XRA-GS 的差异化（"哪一类 baseline 缺什么，XRA-GS 补什么"）。
- G-R2：每个进入主对比的 baseline 在 related 中都有 1–2 句精确定位 + 与本文差异点。
- G-R3：末段一句干净的 gap statement，桥接到 Method 节，不留断层。
- G-R4：紧凑、高密度，避免博客式罗列；删除可推断内容。

## 3. 待解决问题

| ID  | 优先级 | 类型   | 问题                                                                                            | 定位          | 依赖                       | 备注                                       |
| --- | ------ | ------ | ----------------------------------------------------------------------------------------------- | ------------- | -------------------------- | ------------------------------------------ |
| R1  | P1     | 覆盖   | 6 baseline（CoR-GS / DNGaussian / FSGS / R²-Gaussian / X-Gaussian / X-Field）每个是否都有"定位 + 差异"两句 | `main.tex` L85–97 | —                          | 当前 X-Field 描述偏单薄                    |
| R2  | P1     | 桥接   | 末段缺一句强 gap statement → 直接引出 SPS/GAP/ADM 的设计动机                                     | `main.tex` L97  | [[method_2026-05-21_method-todo]] | 不要写成简单的过渡词                       |
| R3  | P1     | 覆盖   | Layer-Based (LB) 未提；若不进主对比可不展开，但需检查是否有审稿人会问                              | `main.tex` L85–97 | `参考论文/LB.pdf`           | 可作为补充材料中讨论                       |
| R4  | P2     | 措辞   | X²-Gaussian / DGR / GR-Gaussian 提到但不进主对比表，需保证措辞让审稿人理解"为何提及不对比"        | `main.tex` L91–97 | —                          | 例如：明确说 4D / discretized 不在本文范围 |
| R5  | P2     | 锚点   | K-Planes（用于 ADM）是否在 related 中作为 representation 锚点提一句                               | `main.tex` L85–97 | `main.tex` L224–265 (ADM)  | 让 method 节 K-Planes 出现不显突兀         |
| R6  | P2     | 密度   | 顶会标准下做一次密度压缩，删除可从前文 / 引文推断的句子                                            | `main.tex` L85–97 | —                          | 投稿前最后一轮做                           |

## 4. 验证清单

- [ ] `latexmk` 编译无 `Citation ... undefined` 警告。
- [ ] 6 个进入主对比的 baseline 在 related 中各有 1–2 句定位。
- [ ] 末段 gap statement 能被读者复述（"我们和现有方法的本质差异是 X"）。
- [ ] 不存在"博客式过渡词"（`Recently`, `In recent years` 等开头连续出现）。
- [ ] K-Planes 在 method 节首次出现前，related 节有铺垫（若 R5 决定接入）。

## 5. 关联资产

- **主稿**：`main.tex` L85–97。
- **风格锚点**（CLAUDE.md §7 固定参考论文）：
  - `参考论文/Corgs.pdf` / `参考论文/dngs.pdf` / `参考论文/FSGS.pdf`（sparse-view NVS）
  - `参考论文/r2gs.pdf` / `参考论文/xgs.pdf` / `参考论文/XField.pdf`（X-ray NVS）
  - `参考论文/x2gs.pdf` / `参考论文/DGR.pdf` / `参考论文/GR.pdf` / `参考论文/LB.pdf`（X-ray 周边）
  - `参考论文/XLRM.pdf`（极稀疏视角参考）
- **引用文件**：`references.bib`。
- **综合视图**：[[experiment_REVIEW_2026-05-21_section-issues]] §3。
- **关联节文档**：[[method_2026-05-21_method-todo]]（gap statement 接入处）、[[intro_2026-05-21_intro-todo]]（避免与 intro 重复列举）。

## 6. 执行顺序提示

R1 / R2 / R3 在 method 节文字基本稳定后再做；R4 / R5 / R6 是润色阶段的工作。本节无 P0 阻塞。
