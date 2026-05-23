# Conclusion / Discussion / Limitations Todo（2026-05-21 snapshot）

> 单节路线图。综合视图见 [[experiment_REVIEW_2026-05-21_section-issues]] §6。
> ID 沿用 `C*` 系列。

## 1. 当前状态

- **主稿位置**：
  - Discussion and Limitations：`main.tex` L400 附近（已从 Conclusion 独立成实验末段）。
  - Conclusion：`main.tex` L411–414。
- **文字**：一段式 Conclusion，涵盖 core insight（capacity allocation > Gaussian count）/ 三模块 / 实验结论 / 适用范围；篇幅适中。
- **设定回顾**：5-organ × 2/3/4-view 设定在 conclusion 中再次确认。
- **图表 / 数据**：本节无图无表；定量声明依赖 main results 数据。

## 2. 顶会标准目标

- G-C1：与实验段落数据收敛——数值表述与 main results 完全一致。
- G-C2：limitations 覆盖实验中已暴露的边界（2-view / 4-view / 各 organ 的失败模式）。
- G-C3：若有 supplementary material，提供一句引导。
- G-C4：保持简洁；避免重复 abstract 与 intro 的句子。
- G-C5：英文表达紧凑、被动语态克制。

## 3. 待解决问题

| ID  | 优先级 | 类型     | 问题                                                                                            | 定位            | 依赖                                  | 备注                              |
| --- | ------ | -------- | ----------------------------------------------------------------------------------------------- | --------------- | ------------------------------------- | --------------------------------- |
| C1  | P1     | 数据收敛 | "consistent improvements in both PSNR2D and SSIM2D" 需用最终数据验证；4-view SSIM2D 若为 tie 必须显式承认 | `main.tex` L411–414 | [[experiment_T02_req_tab_main_ssim2d]] | 与 abstract A2 联动               |
| C2  | P1     | 数据收敛 | 等 efficiency 数据回填后，conclusion 中 efficiency / parameter budget 论述同步更新                | `main.tex` L411–414 | [[experiment_T04_req_tab_efficiency]] | 与 experiment E-W3 联动           |
| C3  | P1     | 补充材料 | 若有 supplementary material，加一句引导句                                                        | `main.tex` L411–414 | supplementary 是否最终独立            | 与 [[intro_2026-05-21_intro-todo]] I3 联动 |
| C4  | P2     | 内容扩展 | 是否加 broader impact 或 future work 段（投顶会通常加 1–2 句）                                    | `main.tex` L411–414 | —                                     | 视篇幅决定                        |
| C5  | P2     | 检查     | Limitations 是否覆盖 2-view / 4-view 边界 + 5 organ 失败模式                                     | `main.tex` Discussion 段 + [[experiment_F12_req_fig_failure]] | F12 数据 | F12 出图后回看 limitations 文字   |
| C6  | P2     | 润色     | 英文最终润色，避免与 abstract 重句                                                                | `main.tex` L411–414 | —                                     | 与 A3 联动                        |

## 4. 验证清单

- [ ] `latexmk` 编译无警告。
- [ ] Conclusion 中所有定量声明可在 main results 表中逐字核对。
- [ ] 4-view SSIM2D 是否平局已显式承认或回避（无歧义）。
- [ ] Computational efficiency / parameter budget 论述与 `tab_experiment_efficiency.tex` 一致。
- [ ] Limitations 段提及 2-view / 4-view 边界 + 至少 1–2 个 organ 失败模式。
- [ ] 若 supplementary 存在，conclusion 末段有引导句。
- [ ] 没有与 abstract 重句的句子。

## 5. 关联资产

- **主稿**：`main.tex` L400 附近（Discussion）+ L411–414（Conclusion）。
- **依赖表**：
  - `assets/tables/tab_experiment_comparison.tex`
  - `assets/tables/tab_experiment_comparison_ssim.tex`
  - `assets/tables/tab_experiment_efficiency.tex`
- **依赖图**：[[experiment_F12_req_fig_failure]]（限制讨论用）。
- **综合视图**：[[experiment_REVIEW_2026-05-21_section-issues]] §6。
- **关联节文档**：
  - [[intro_2026-05-21_abstract-todo]]（A2 数据一致；A4 wording 差异化）
  - [[experiment_2026-05-21_experiment-todo]]（数据收敛 + F12 联动）
  - [[intro_2026-05-21_intro-todo]]（supplementary 引导联动）

## 6. 执行顺序提示

C1 / C2 在主表 / 效率表数据到位的当天就核对；C3 在确定 supplementary 是否独立后加；C4 / C5 / C6 在投稿前最后一轮润色时处理。
