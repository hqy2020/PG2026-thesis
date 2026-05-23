# XRA-GS 论文各部分问题清单与解决目标

> 生成日期：2026-05-21
> 用途：系统性梳理论文各部分现存问题，解耦为可独立执行的任务单元，方便后续逐项解决并留痕溯源。

---

## 总览：当前论文状态

- 主稿 `main.tex` 已有完整的 Abstract / Introduction / Related Work / Method / Experiments / Conclusion 六大节
- 文字骨架基本成型，叙述逻辑清晰
- **图片目录 `assets/fig/` 当前为空**（git status 显示旧图已被删除，新图尚未生成）
- 效率表 T04 全部为 `--` 占位符，等待实验 agent 回包
- SSIM2D 主表 T02 仅有 3 个方法的平均数据，缺 6 个 baseline 的完整矩阵
- 多个定性图（F07/F08/F09/F10/F11/F12）状态为 `data-pending`

---

## 1. Abstract

### 当前状态
- 已有完整英文摘要，骨架为 `problem → gap → core insight → method → strongest evidence`
- 长度适中，信息密度合理

### 待解决问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| A1 | 实验数据回包后需更新 strongest evidence 的具体数值（如 PSNR2D gain 幅度） | P1 | T01/T02 回包 |
| A2 | 需确认 SSIM2D 的措辞是否精确（当前写 "leading or tied SSIM2D"，需用最终数据验证） | P1 | T02 回包 |

### 目标
- 数据到位后微调数值表述，确保摘要中的定量声明与主表完全一致
- 不改变整体骨架和逻辑链

---

## 2. Introduction (sec:intro)

### 当前状态
- 故事线完整：NVS → Sparse NVS → Tomographic NVS → Sparse Tomographic View Synthesis
- 三点贡献已列出
- Figure 1 (intro-compare) 在 tex 中有引用，但 `assets/fig/fig_intro_compare.png` **文件不存在**

### 待解决问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| I1 | **fig_intro_compare.png 缺失** — 当前 `assets/fig/` 为空目录，编译时该图无法显示 | P0 | image2 生成或手动绘制 |
| I2 | F01 teaser 图规划为 `planned` 状态，未开始制作；如果最终需要 teaser，需规划 | P2 | 无 |
| I3 | 贡献 2 中 "path-anchored initialization, boundary redundancy removal, and local density refinement" 的措辞与 Method 节中 SPS/GAP/ADM 的对应关系已正确，无需改动 | — | — |
| I4 | ~~引言中引用 X-Field 和 DGR 需确认 references.bib 中条目完整性~~ — 已核实，bib 条目完整 | ✅ | — |

### 目标
- P0：生成 fig_intro_compare.png，确保编译通过且图可正常显示
- Teaser 图视篇幅和页数决定是否最终加入

---

## 3. Related Work (sec:related)

### 当前状态
- 两个小节：Sparse-view NVS + X-ray NVS and Tomographic Reconstruction
- 覆盖面合理，引用了主要 baseline
- 篇幅偏短（约 1.5 段 + 1.5 段），但在 PG 短文格式下可能已足够

### 待解决问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| R1 | **Layer-Based (LB) 未在 related work 中出现** — GR-Gaussian 在第二小节末尾一笔带过；如果这两个方法在对比表中没有出现，related work 中也无需展开 | P1 | 无 |
| R2 | 当前 related work 中 X²-Gaussian 和 DGR 提到但不在主对比表中 — 这本身没问题（related work 不必与主对比表一一对应），但需确认措辞不会让审稿人误以为我们遗漏了对比 | P2 | 无 |
| R3 | 缺少一个段落总结"我们的定位"与"现有方法的本质差异"，目前只有一句话过渡到 Method 节 | P2 | 无 |

### 目标
- 确保提到的每个方法都有合理定位（"提到但不对比"需有清晰理由）
- 如篇幅允许，加一句更强的过渡句桥接到 Method
- 保持紧凑，不做大幅扩写

---

## 4. Method (sec:method)

### 当前状态
- 六个小节：Problem Formulation / 3DGS Background / Overall Framework / SPS / GAP / ADM / Training Loss
- 数学公式完整，Algorithm 1 已给出
- 四张方法图引用：fig_intro_compare（共用）、fig_pipeline、fig_sps、fig_gap、fig_adm
- **所有方法图文件均不存在**（`assets/fig/` 为空）

### 待解决问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| M1 | **fig_method_pipeline.png 缺失** — 整体框架图是 P0 核心资产 | P0 | image2 生成 |
| M2 | **fig_method_sps.png 缺失** — SPS 模块示意图 | P0 | image2 生成 |
| M3 | **fig_method_gap.png 缺失** — GAP 模块示意图 | P0 | image2 生成 |
| M4 | **fig_method_adm.png 缺失** — ADM 模块示意图 | P0 | image2 生成 |
| M5 | SPS 小节中关于 CBCT landmark 的引用段（shahidi2014, chen2023）论述偏长，与主线逻辑关系较弱，可能被审稿人认为 padding | P1 | 无 |
| M6 | Eq.(10) 中 `s_view` 参数在正文中仅口头说明，未给具体取值表 | P1 | 无 |
| M7 | Eq.(10) 的 view-dependent scaling `s_view` 需要在 Implementation Details 中补充具体值 | P1 | 无 |
| M8 | Algorithm 1 中 `T_gap` 和 `T_gap,end` 的具体值未在 Implementation Details 给出 | P1 | 无 |
| M9 | Training Loss 小节中 `ω_p(t)` 的 time-varying 权重公式未给出 | P1 | 无 |
| M10 | 需确认 R²-Gaussian 的 voxelization 和 densification 细节引用是否准确（hu2024r2） | P2 | 无 |

### 目标
- P0：生成四张方法示意图（pipeline / SPS / GAP / ADM）
- P1：精简 SPS 中偏冗长的 CBCT landmark 论述
- P1：补充 Implementation Details 中缺失的超参数值（s_view, T_gap, T_gap,end, ω_p(t)）
- 保持方法节的数学自洽性和公式编号连续

---

## 5. Experiments (sec:experiments)

### 当前状态
- 七个小节：Setup / Main Results / Module Analysis / View-count Analysis / Computational Cost / Hyperparameter Sensitivity / Discussion and Limitations
- 主对比表 (PSNR2D) 有数据，SSIM2D 表仅 3 个方法
- 所有实验图文件均不存在

### 待解决问题

#### 5a. 表格问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| E-T1 | **效率表 T04 全部 `--`** — Training time / #Gaussians / GPU memory 全部空缺 | P0 | 实验 agent 回包 |
| E-T2 | **SSIM2D 主表 T02 仅有 3 方法平均** — 缺 DNGaussian / CoR-GS / FSGS / X-Gaussian 的 SSIM2D 数据 | P0 | 实验 agent 回包 |
| E-T3 | X-Field* 行在 PSNR2D 表中 per-organ 数据为空，只有 avg | P1 | 实验 agent 回包 |
| E-T4 | Progressive ablation 表中 2-view 下 +SPS / +SPS+GAP / full 三行 2-view 值完全相同 (21.44)，需确认是否准确 | P1 | 核实实验数据 |
| E-T5 | **View-count 表与主对比表 PSNR2D avg 全部不一致** — 2-view: 21.44 vs 21.52; 3-view: 28.22 vs 28.09; 4-view: 29.20 vs 29.15 — 需向实验 agent 确认数据源差异 | P0 | 核实实验数据 |

#### 5b. 图片问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| E-F1 | **fig_experiment_qual_main.png 缺失** — 主定性对比图 | P0 | 实验 agent 回包 + 脚本绘制 |
| E-F2 | **fig_experiment_qual_zoom.png 缺失** — 局部放大对比 | P0 | 同上 |
| E-F3 | **fig_experiment_consistency.png 缺失** — 跨视角一致性 | P1 | 同上 |
| E-F4 | **fig_experiment_ablation_visual.png 缺失** — 消融可视化 | P0 | 同上 |
| E-F5 | **fig_experiment_spatial_distribution.png 缺失** — 高斯空间分布演化 | P1 | 同上 |
| E-F6 | **fig_experiment_hparam_compact.png 缺失** — 超参敏感性 | P1 | 同上 |
| E-F7 | **fig_experiment_gap_sweep.png 缺失** — GAP 超参扫描 | P1 | 同上 |
| E-F8 | **fig_experiment_failure_cases.png 缺失** — 失败案例 | P2 | 同上 |

#### 5c. 文字问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| E-W1 | Main Results 正文提到 "average PSNR2D gains +0.19/+0.26/+0.02 dB"，需与最终表格数据二次核对 | P1 | T01 数据回包 |
| E-W2 | Discussion 中 "approach or match our result in some organs" 措辞模糊，如果 4-view 下 R²-Gaussian 确实在个别 organ 打平，应更具体地指出 | P1 | 无 |
| E-W3 | Computational Cost 小节几乎无定量结论（因 T04 全空），数据到位后需补写 | P0 | T04 回包 |
| E-W4 | Hyperparameter Sensitivity 小节的结论偏弱（"concentrated working point"），审稿人可能要求更强的 robustness 分析 | P2 | 无 |

#### 5d. 结构问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| E-S1 | 实验节图多且分散（8 张主文 + 多张补充），需确认 PG 页数限制下是否能全部放入主文 | P0 | 无 |
| E-S2 | Discussion and Limitations 已经从 Conclusion 独立出来，结构合理，无需调整 | — | — |

### 目标
- P0：等待实验 agent 回包，补齐效率表和 SSIM2D 主表
- P0：核实 view-count avg 数据不一致问题 (E-T5)
- P0：根据页数限制决定哪些图进主文、哪些进补充材料
- P1：实验图数据到位后批量生成
- P1：补写 Computational Cost 定量结论

---

## 6. Conclusion (sec:conclusion)

### 当前状态
- 一段式结论，涵盖了 core insight / 三模块 / 实验结论 / 适用范围
- 篇幅适中

### 待解决问题
| # | 问题 | 优先级 | 依赖 |
|---|------|--------|------|
| C1 | 结论中 "consistent improvements in both PSNR2D and SSIM2D" 需用最终数据验证（4-view SSIM2D 是 tie） | P1 | T02 回包 |
| C2 | 可考虑加一句 broader impact 或 future work 方向的展望 | P2 | 无 |
| C3 | 当前未提及 supplementary material 的存在，如最终有补充材料需加一句引导 | P1 | 无 |

### 目标
- 数据到位后微调定量声明
- 如有补充材料，加引导句
- 保持结论简洁

---

## 7. 跨节系统性问题

| # | 问题 | 优先级 | 影响范围 |
|---|------|--------|----------|
| X1 | **`assets/fig/` 为空** — 所有图片文件已删除但新图未生成，当前编译 PDF 全部缺图 | P0 | 全文 |
| X2 | ~~references.bib 完整性~~ — **已核实：25 个 cite key 全部在 bib 中有对应条目；bib 有 21 个未引用条目（正常）** | ✅ | 全文 |
| X3 | **补充材料未开始** — F13 (training curve), T06 (per-organ SSIM2D), T07 (single-module ablation) 均为 data-pending | P1 | 补充材料 |
| X4 | **VISUAL_STYLE.md 中的配色规范与当前论文图/表尚未对齐** — 新图生成时必须遵守 | P0 | 所有图片 |
| X5 | 页数限制检查 — PG 2026 的页数限制需确认，当前稿件 + 全部图片/表格是否超标 | P0 | 全文 |

---

## 执行优先级排序

### 第一梯队：立即可做（无外部依赖）
1. ~~**[X2]** 验证 references.bib 完整性~~ — 已完成 ✅
2. **[E-T5]** 核实 view-count avg 与主对比表 PSNR2D 数据不一致
3. **[M5]** 精简 SPS 中 CBCT landmark 论述
4. **[M7/M8/M9]** 补充 Implementation Details 缺失超参数
5. **[X5]** 确认 PG 2026 页数限制，规划主文/补充材料分配

### 第二梯队：需 image2 生成（示意图）
6. **[M1]** fig_method_pipeline.png
7. **[M2]** fig_method_sps.png
8. **[M3]** fig_method_gap.png
9. **[M4]** fig_method_adm.png
10. **[I1]** fig_intro_compare.png

### 第三梯队：需实验 agent 回包（BLOCKED）
11. **[E-T1]** 效率表 T04 数据填充
12. **[E-T2]** SSIM2D 主表 T02 完整数据
13. **[E-F1~E-F8]** 所有实验图素材
14. **[A1/A2]** Abstract 数值更新
15. **[E-W3]** Computational Cost 文字补写

### 第四梯队：后期优化
16. **[R3]** Related Work 过渡句加强
17. **[C2/C3]** Conclusion 展望和补充材料引导
18. **[X3]** 补充材料制作
