# Method Todo（2026-05-21 snapshot）

> 单节路线图。综合视图见 [[experiment_REVIEW_2026-05-21_section-issues]] §4。
> ID 沿用 `M*` 系列。

## 1. 当前状态

- **主稿位置**：`main.tex` L98–281（`\section{Method}`）。
- **小节结构**：
  - Problem Formulation
  - 3DGS Background
  - Overall Framework
  - SPS (L174–193)
  - GAP (L195–222)
  - ADM (L224–265)
  - Training Loss
- **公式 / 算法**：方程编号连续（Eq.(1)–(11)）；Algorithm 1（L139–165）已给出训练流程。
- **文字**：英文完整；模块顺序与 abstract / intro 一致（SPS → GAP → ADM）。
- **图片引用 + 磁盘状态**：
  - `fig_method_pipeline.png`（L169 附近）：**物理缺失**
  - `fig_method_sps.png`（L190 附近）：**物理缺失**
  - `fig_method_gap.png`（L219 附近）：**物理缺失**
  - `fig_method_adm.png`（L262 附近）：**物理缺失**
- **表格 / 数据**：本节无表；ADM 引用 K-Planes（fridovich2022kplanes），引用键已核实。
- **需求文档**：[[method_F03_req_fig_pipeline]] / [[method_F04_req_fig_module_sps]] / [[method_F05_req_fig_module_gap]] / [[method_F06_req_fig_module_adm]]。

## 2. 顶会标准目标

- G-M1：每张方法图都能"看图 + caption 即懂"，不依赖正文细节。
- G-M2：图中变量名、模块边界、箭头标签与正文公式一致；文字标注后置到 tex 排版阶段，不烘焙到生成图中（§12 image2 工作流）。
- G-M3：Algorithm 1 在 training loop 中清晰标注 SPS / GAP / ADM 的触发时机和阶段。
- G-M4：所有方程符号首次出现处给出定义；Implementation Details 收纳所有超参数。
- G-M5：行文紧凑，避免与 method 主线弱关联的 padding 段落。

## 3. 待解决问题

| ID  | 优先级 | 类型     | 问题                                                                                          | 定位                          | 依赖 / 工作流                                                | 备注                          |
| --- | ------ | -------- | --------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------ | ----------------------------- |
| M1  | P0     | 图缺失   | `fig_method_pipeline.png` 物理缺失（整体框架图，P0 核心资产）                                  | `main.tex` L169 附近          | image2 API（§12 概念图）/ [[method_F03_req_fig_pipeline]]    | 文件名同步迁移为 `method_fig_pipeline.png` |
| M2  | P0     | 图缺失   | `fig_method_sps.png` 物理缺失                                                                  | `main.tex` L190 附近          | image2 / [[method_F04_req_fig_module_sps]]                   | 同上前缀迁移                  |
| M3  | P0     | 图缺失   | `fig_method_gap.png` 物理缺失                                                                  | `main.tex` L219 附近          | image2 / [[method_F05_req_fig_module_gap]]                   | 同上前缀迁移                  |
| M4  | P0     | 图缺失   | `fig_method_adm.png` 物理缺失                                                                  | `main.tex` L262 附近          | image2 / [[method_F06_req_fig_module_adm]]                   | 同上前缀迁移                  |
| M5  | P1     | 文字精简 | SPS 中 CBCT landmark 引用段（shahidi2014, chen2023）偏长，与主线关系弱                          | `main.tex` L174–193 内段       | —                                                            | 可压成一句或下沉到 supplementary |
| M6  | P1     | 超参表   | Eq.(10) 中 `s_view` 在正文仅口头描述，未给具体取值                                              | `main.tex` ADM 段             | —                                                            | 写进 Implementation Details   |
| M7  | P1     | 超参表   | Eq.(10) 中 view-dependent scaling `s_view` 的具体值                                            | `main.tex` ADM 段             | —                                                            | 与 M6 一并处理                |
| M8  | P1     | 超参表   | Algorithm 1 中 `T_gap` / `T_gap,end` 的具体值                                                  | `main.tex` L139–165 + GAP 段  | —                                                            | 与 M6 / M7 合并到一个超参表   |
| M9  | P1     | 超参表   | Training Loss 中 `ω_p(t)` 的 time-varying 公式未给出                                            | `main.tex` Training Loss 段   | —                                                            | 给出公式 + 取值表             |
| M10 | P2     | 引用准确 | R²-Gaussian voxelization / densification 细节的引用准确性（hu2024r2）                          | `main.tex` 相关位置           | `参考论文/r2gs.pdf`                                          | 投稿前最后核对                |
| M11 | P1     | 命名规范 | 4 张方法图文件名前缀从 `fig_method_*` 改为 §13 规范 `method_fig_*`，tex 引用同步               | `main.tex` L169/190/219/262   | M1–M4                                                        | latexmk 验证                  |
| M12 | P1     | caption  | 4 张方法图 caption 是否都"独立可读"（setting / 输入 / 输出 / 关键观察）                          | `main.tex` 各 figure caption  | M1–M4                                                        | 与图同批检视                  |
| M13 | P2     | 文字     | 每个方程符号首次出现处是否都有定义（systematic check）                                          | `main.tex` L98–281            | —                                                            | 一次性扫描                    |

## 4. 验证清单

- [ ] `latexmk` 编译无 `Missing image` 警告。
- [ ] `assets/fig/method_fig_pipeline.png` / `method_fig_sps.png` / `method_fig_gap.png` / `method_fig_adm.png` 均存在。
- [ ] 每张图 caption 独立可读且术语与正文一致。
- [ ] Algorithm 1 中 SPS / GAP / ADM 的触发点用清晰标注（注释或行号锚点）展示。
- [ ] Implementation Details 段包含 `s_view` / `T_gap` / `T_gap,end` / `ω_p(t)` 全部超参数。
- [ ] 所有公式符号首次出现处有定义。
- [ ] 模块顺序与 abstract / intro 完全一致（SPS → GAP → ADM）。

## 5. 关联资产

- **主稿**：`main.tex` L98–281。
- **图（计划落地，§13 前缀已规范化）**：
  - `assets/fig/method_fig_pipeline.png`
  - `assets/fig/method_fig_sps.png`
  - `assets/fig/method_fig_gap.png`
  - `assets/fig/method_fig_adm.png`
- **需求文档**：
  - [[method_F03_req_fig_pipeline]]
  - [[method_F04_req_fig_module_sps]]
  - [[method_F05_req_fig_module_gap]]
  - [[method_F06_req_fig_module_adm]]
- **生成工具文档**：`assets/data/image2.md`（API 用法）。
- **配色 / 字体规范**：[VISUAL_STYLE.md](VISUAL_STYLE.md)。
- **综合视图**：[[experiment_REVIEW_2026-05-21_section-issues]] §4。
- **关联节文档**：
  - [[intro_2026-05-21_intro-todo]]（三模块顺序一致性）
  - [[related_2026-05-21_related-todo]]（gap statement 接入点 + K-Planes 锚点）

## 6. 执行顺序提示

M1–M4 是 P0 图生成任务，可并行；M11 是图落地后的命名迁移；M5 / M6–M9 / M12 在图到位后做；M10 / M13 留到投稿前批量检查。
