# Experiments Todo（2026-05-21 snapshot）

> 单节路线图。综合视图见 [[experiment_REVIEW_2026-05-21_section-issues]] §5。
> ID 沿用 `E-T*`（表）/ `E-F*`（图）/ `E-W*`（文字）/ `E-S*`（结构）系列。

## 1. 当前状态

- **主稿位置**：`main.tex` L282–407（`\section{Experiments}`）。
- **小节结构**（7 个）：Setup / Main Results / Module & Initialization Analysis / View-count Analysis / Computational Cost / Hyperparameter Sensitivity / Discussion and Limitations。
- **协议一致性**：
  - 对比方法：CoR-GS / DNGaussian / FSGS / R²-Gaussian / X-Gaussian / X-Field（CLAUDE.md §10）✅
  - 主指标：SSIM2D + PSNR2D ✅
  - 测试设定：5 organs × {2,3,4} views ✅
- **表格现状**：
  - `tab_experiment_comparison.tex`（PSNR2D 主表）：X-Field* 行在 Chest / Head / Abdomen 全空白（9 格）。
  - `tab_experiment_comparison_ssim.tex`（SSIM2D 主表）：仅有 3 个方法的平均；缺 DNGaussian / CoR-GS / FSGS / X-Gaussian 完整矩阵。
  - `tab_experiment_efficiency.tex`：3 行 × 3 列全 `--`（**投稿阻塞**）。
  - `tab_experiment_component.tex` / `densify_vs_gap.tex` / `init_ablation.tex` / `view_count.tex`：完整。
- **图片现状**（7 张全部物理缺失）：
  - `fig_experiment_qual_main.png`
  - `fig_experiment_qual_zoom.png`
  - `fig_experiment_consistency.png`
  - `fig_experiment_ablation_visual.png`
  - `fig_experiment_spatial_distribution.png`
  - `fig_experiment_hparam_compact.png`
  - `fig_experiment_gap_sweep.png`
  - `fig_experiment_failure_cases.png`
- **数据 / 脚本**：
  - `assets/data/` 仅有 `image2.md`（工作流文档），无任何 CSV。
  - `assets/scripts/` 仅有 `.gitkeep`，无 Python 脚本。
- **ask 进度**：`assets/ask/experiment_2026-05-21_efficiency-and-ssim.md`（P0）已发出，`assets/answer/` 为空。

## 2. 顶会标准目标

- G-E1：主文用最小篇幅最强证据回答两个问题——"为何 XRA-GS > 6 个 baseline" + "三模块各负责什么"。
- G-E2：每张图、每个表 caption 独立可读：setting / 比较对象 / 指标 / unit / best 高亮。
- G-E3：每个实验段落给出三层观察：跨视角 trend / 极稀疏视角 (2-view) 表现 / 5 organ 稳定性。
- G-E4：定性图 / 定量表分开，不混入同一 figure。
- G-E5：所有数值来自实验 agent 真实产出，不编造；占位符 `--` 数据到位前不进 PDF。
- G-E6：图 / 表 / 数据 / 脚本按 §12 / §13 分管线 + 前缀。
- G-E7：主文只保留最强证据；扩展可视化下沉到 supplementary。

## 3. 待解决问题

### 3.1 表格问题（E-T*）

| ID    | 优先级 | 问题                                                                                          | 定位                                         | 依赖 / ask                                                              | 备注                          |
| ----- | ------ | --------------------------------------------------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------- |
| E-T1  | P0     | `tab_experiment_efficiency.tex` 3 行 × 3 列全 `--`（training time / #Gaussians / GPU memory） | `assets/tables/tab_experiment_efficiency.tex` L10–12 | `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md` 回包 | **投稿阻塞**                  |
| E-T2  | P0     | SSIM2D 主表仅 3 方法平均；缺 4 方法完整矩阵                                                    | `tab_experiment_comparison_ssim.tex`           | 同上                                                                    | [[experiment_T02_req_tab_main_ssim2d]] |
| E-T3  | P1     | X-Field* 行在 PSNR2D 表中 Chest / Head / Abdomen per-organ 为空（9 格）                          | `tab_experiment_comparison.tex` L21          | 实验 agent                                                              | 若无法补则在 caption 显式说明 |
| E-T4  | P1     | Progressive ablation 表中 2-view 下 +SPS / +SPS+GAP / full 三行相同 (21.44)，需核实             | `tab_experiment_component.tex`                | 核实实验数据                                                            | 是否真平局，还是数据缺失      |
| E-T5  | P0     | View-count 表与主对比表 PSNR2D avg 不一致（2-view 21.44 vs 21.52；3-view 28.22 vs 28.09；4-view 29.20 vs 29.15） | `tab_experiment_view_count.tex` vs `tab_experiment_comparison.tex` | 实验 agent 确认数据源差异                                              | 严重一致性问题，必须解决      |

### 3.2 图片问题（E-F*）

| ID   | 优先级 | 问题                                                | 定位                          | 工作流                                                            | 依赖              |
| ---- | ------ | --------------------------------------------------- | ----------------------------- | ----------------------------------------------------------------- | ----------------- |
| E-F1 | P0     | `fig_experiment_qual_main.png` 缺失（主定性对比图）  | `main.tex` L309 附近          | Python 脚本（§12 实验图工作流）+ 实验 agent 投影数据             | [[experiment_F07_req_fig_qual_main]] |
| E-F2 | P0     | `fig_experiment_qual_zoom.png` 缺失（局部放大对比）  | `main.tex` L318 附近          | 同上                                                              | 同 F07            |
| E-F3 | P1     | `fig_experiment_consistency.png` 缺失（跨视角一致性） | `main.tex` L327 附近          | Python 脚本                                                       | [[experiment_F08_req_fig_qual_detail_consistency]] |
| E-F4 | P0     | `fig_experiment_ablation_visual.png` 缺失（消融可视化）| `main.tex` L342 附近          | 混合：定性区走 image2 / 定量数值标注走脚本                        | [[experiment_F09_req_fig_ablation_visual]] |
| E-F5 | P1     | `fig_experiment_spatial_distribution.png` 缺失（高斯空间分布演化） | `main.tex` L357 附近 | Python 脚本                                                       | [[experiment_F10_req_fig_spatial_distribution]] |
| E-F6 | P1     | `fig_experiment_hparam_compact.png` 缺失（超参敏感性）| `main.tex` L380 附近          | Python 脚本（折线 / heatmap）                                     | [[experiment_F11_req_fig_hparam]] |
| E-F7 | P1     | `fig_experiment_gap_sweep.png` 缺失（GAP 超参扫描）  | `main.tex` L389 附近          | Python 脚本                                                       | 同 F11 或单独     |
| E-F8 | P2     | `fig_experiment_failure_cases.png` 缺失（失败案例） | `main.tex` L404 附近          | Python 脚本 + 实验 agent failure cases 输出                       | [[experiment_F12_req_fig_failure]] |

### 3.3 文字问题（E-W*）

| ID   | 优先级 | 问题                                                                                  | 定位                       | 依赖              |
| ---- | ------ | ------------------------------------------------------------------------------------- | -------------------------- | ----------------- |
| E-W1 | P1     | Main Results 中 "average PSNR2D gains +0.19 / +0.26 / +0.02 dB" 需与最终表二次核对    | `main.tex` Main Results 段 | T01 数据回包      |
| E-W2 | P1     | Discussion 中 "approach or match our result in some organs" 措辞模糊，应具体到 organ × view | `main.tex` Discussion 段   | T01 / T02 数据    |
| E-W3 | P0     | Computational Cost 小节几乎无定量结论（因 T04 全空），数据到位后必须补写                | `main.tex` L370–372       | T04 数据          |
| E-W4 | P2     | Hyperparameter Sensitivity 结论偏弱（"concentrated working point"），可加 robustness 量化 | `main.tex` L380 附近       | F11 / F07 数据    |

### 3.4 结构问题（E-S*）

| ID   | 优先级 | 问题                                                            | 依赖                       | 备注                  |
| ---- | ------ | --------------------------------------------------------------- | -------------------------- | --------------------- |
| E-S1 | P0     | 主文 8 张图 + 7 张表是否能塞进 PG 页数限制；超出需下沉到 supplementary | PG 2026 页数限制确认       | 与 [[intro_2026-05-21_intro-todo]] I3 联动 |
| E-S2 | —      | Discussion & Limitations 已从 Conclusion 独立，结构合理         | —                          | 无需调整              |
| E-S3 | P1     | 所有图 / 表文件名前缀从旧格式迁移到 §13 规范 `experiment_fig_*` / `experiment_tab_*` 形式 | E-F1–E-F8 完成后同步       | tex 引用同步改        |

## 4. 验证清单

- [ ] `latexmk` 编译无 `Missing image` / `Citation undefined` 警告。
- [ ] `tab_experiment_efficiency.tex` 无任何 `--`，所有数据来源标注（实验 agent 输出路径）。
- [ ] PSNR2D / SSIM2D 主表互相一致，且与 view-count 表一致（E-T5 解决）。
- [ ] 8 张实验图均存在于 `assets/fig/` 且文件名以 `experiment_` 前缀开头。
- [ ] 每张图 / 表 caption 独立可读，包含 setting / 比较对象 / 指标 / unit / best 高亮。
- [ ] 每个实验小节末尾给出 trend / 极稀疏 view / 5-organ 稳定性 三层观察。
- [ ] Computational Cost 段有具体定量结论（training time / #Gaussians / GPU memory 三项至少各引用一次）。
- [ ] `assets/scripts/` 下每张实验图都有对应的 Python 脚本，可重复运行（从 `assets/data/` 读 CSV）。
- [ ] `assets/data/` 下每个数值产物来源可追溯到 `assets/answer/` 或实验 agent commit。

## 5. 关联资产

- **主稿**：`main.tex` L282–407。
- **表**（现存 / 计划）：
  - `assets/tables/tab_experiment_comparison.tex`
  - `assets/tables/tab_experiment_comparison_ssim.tex`
  - `assets/tables/tab_experiment_efficiency.tex`
  - `assets/tables/tab_experiment_component.tex`
  - `assets/tables/tab_experiment_densify_vs_gap.tex`
  - `assets/tables/tab_experiment_init_ablation.tex`
  - `assets/tables/tab_experiment_view_count.tex`
- **图**（计划落地，§13 前缀规范）：
  - `assets/fig/experiment_fig_qual_main.png`
  - `assets/fig/experiment_fig_qual_zoom.png`
  - `assets/fig/experiment_fig_consistency.png`
  - `assets/fig/experiment_fig_ablation_visual.png`
  - `assets/fig/experiment_fig_spatial_distribution.png`
  - `assets/fig/experiment_fig_hparam_compact.png`
  - `assets/fig/experiment_fig_gap_sweep.png`
  - `assets/fig/experiment_fig_failure_cases.png`
- **数据 / 脚本（待补）**：
  - `assets/data/<TBD>.csv`（来自实验 agent 回包）
  - `assets/scripts/<TBD>.py`（本仓 Python 出图）
- **需求文档**：
  - 表：[[experiment_T01_req_tab_main_psnr2d]] / [[experiment_T02_req_tab_main_ssim2d]] / [[experiment_T03_req_tab_progressive_ablation]] / [[experiment_T04_req_tab_efficiency]] / [[experiment_T05_req_tab_init_and_viewcount]] / [[experiment_T06_req_tab_supp_per_organ_ssim2d]] / [[experiment_T07_req_tab_supp_single_module_ablation]]
  - 图：[[experiment_F07_req_fig_qual_main]] / [[experiment_F08_req_fig_qual_detail_consistency]] / [[experiment_F09_req_fig_ablation_visual]] / [[experiment_F10_req_fig_spatial_distribution]] / [[experiment_F11_req_fig_hparam]] / [[experiment_F12_req_fig_failure]] / [[experiment_F13_req_fig_supp_training_curve]]
- **ask / answer**：
  - `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md`（P0，待回复）
- **配色 / 字体规范**：[VISUAL_STYLE.md](VISUAL_STYLE.md)。
- **综合视图**：[[experiment_REVIEW_2026-05-21_section-issues]] §5。
- **关联节文档**：[[intro_2026-05-21_abstract-todo]]（strongest evidence 数据收敛）、[[experiment_2026-05-21_conclusion-todo]]（结论数据收敛）。

## 6. 执行顺序提示

1. **立即可做**（无 ask 依赖）：E-T5 数据一致性核实、E-S1 页数规划。
2. **等 ask 回包后开做**：E-T1 / E-T2 / E-W3。
3. **数据到位后批量产图**：E-F1–E-F8，先 P0 后 P1 后 P2。
4. **图表全部落地后**：E-S3 命名迁移、E-W1 / E-W2 文字数据收敛。
5. **投稿前**：E-W4 robustness 强化、整体英文润色。
