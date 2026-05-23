# PG2026 Submission Roadmap and Milestones

> 目标：把当前 `XRA-GS` 中后期草稿推进到可投稿 PG 顶会论文。这里不是日常检查清单，而是版本化统筹路线图：每一版明确达成什么、验收什么、什么时候和用户确认、什么时候 push 一版。

## 全局版本约定

- 当前起点：`V0.6 Current Baseline`，论文主线和方法已基本成型，但实验资产、回包数据和投稿级验收尚未完成。
- 每个版本完成后，先和用户讨论确认，再 push 一版；不自动 push。
- 建议版本节点：
  - `v0.6-draft-baseline`
  - `v0.7-experiment-assets`
  - `v0.8-result-integrated`
  - `v0.9-review-ready`
  - `v1.0-submission-candidate`
  - `v1.1-final-submission`
- push 前必须说明：本版新增内容、已解决风险、仍未解决风险、是否影响投稿判断。
- 科学结论只在 `V0.8` 前允许根据真实实验回包调整；进入 `V1.1` 后只允许修格式、错别字、路径、编译错误。

---

## V0.6 Current Baseline：当前中后期草稿冻结版

### 阶段目标

冻结当前论文起点，明确哪些内容已经可以作为后续基础，哪些内容还只是占位或待实验 agent 回包。

### 当前已具备

- `main.tex` 已有完整标题、摘要、引言、相关工作、方法、实验、讨论/局限、结论。
- 方法名、任务名和创新模块已固定：`XRA-GS`、`Sparse Tomographic View Synthesis`、`SPS / GAP / ADM`。
- 主 PSNR2D / SSIM2D 平均结果已有初版。
- intro figure 和 method figures 已基本落盘。

### 当前硬缺口

- `assets/answer/` 为空，已有 11 个 `assets/ask/` 请求尚未形成正式回包。
- 主实验图缺失：qualitative main、detail consistency、ablation visual、spatial distribution、hparam、failure cases、training curve。
- `tab_experiment_efficiency.tex` 中 Time / #Gaussians / Mem / FPS 仍是 `--`。
- `tab_experiment_component.tex` 中 Baseline / +SPS / +SPS+GAP 的 SSIM2D 仍是 `--`。
- view-count 相关表存在数值冲突。
- X-Field per-organ PSNR2D 缺失，只能谨慎使用 average-level comparison。

### 验收条件

- [☑] 用户确认当前论文定位为“中后期草稿”，不是从零重写。
- [☑] 用户确认后续优先级是补齐实验资产、统一结果版本、校准 claim，而不是大改方法主线。
- [☑] 明确当前 baseline 需要先 push 一版留档。

### Push 约定

- 若用户确认当前 baseline 有保存价值，push `v0.6-draft-baseline`。
- 若用户认为当前状态仍太乱，则先不 push，直接进入 `V0.7`。

### 需要和用户讨论

- 是否把现有 baseline 作为一个可回退版本保存？
- 是否保留当前 `Discussion and Limitations` 在 Experiments 内部，还是后续改成独立 section？

---

## V0.7 Experiment Assets Completion：实验资产补齐版

### 阶段目标

把论文从“有完整叙事但有占位”推进到“关键实验资产齐全、缺失项有明确处理方式”。

### 入口条件

- `V0.6` 起点已确认。
- `assets/ask/` 中 P0/P1 请求的优先级已明确。

### 核心交付物

- [ ] `assets/answer/` 中出现对应回包说明文件。
- [ ] 主结果相关 CSV / 数据文件落入 `assets/data/`。
- [ ] 主实验图落入 `assets/fig/`：
  - `experiment_fig_qual_main.png`
  - `experiment_fig_qual_detail_consistency.png`
  - `experiment_fig_ablation_visual.png`
  - `experiment_fig_spatial_distribution.png`
  - `experiment_fig_hparam.png` 或明确降级到补充材料/移出主文
  - `experiment_fig_failure_cases.png` 或明确移入补充材料
- [ ] 表格缺口处理完成：
  - efficiency 表不再保留无解释的 `--`
  - component ablation 中间 SSIM2D 补齐，或删去不能支撑的列/claim
  - view-count 冲突表确认唯一事实源
  - 旧表 `tab_experiment_densify_vs_gap.tex` 是否废弃得到确认

### 关键检查点

- P0：`experiment_2026-05-23_T01_T02_T04_main_metrics_efficiency.md` 是否回包。
- P0：`experiment_2026-05-23_T03_progressive_ablation_ssim.md` 是否回包。
- P0：`experiment_2026-05-23_F07_fig_qual_main.md` 是否回包。
- P0：`experiment_2026-05-23_F09_fig_ablation_visual.md` 是否回包。
- P1：hparam / spatial distribution / failure cases 是否足够进入主文。

### 验收条件

- [ ] 主文不再依赖空白实验图 placeholder。
- [ ] 主文关键表格没有未解释的 `--`。
- [ ] 所有保留在主文的结果都有真实回包来源。
- [ ] 无法补齐的数据已转化为透明说明、降级到补充材料，或从主文 claim 中移除。

### Push 约定

- 关键实验资产补齐并能编译后，和用户确认 push `v0.7-experiment-assets`。
- 如果还有 P1/P2 缺口，但不阻塞主文，可在 push 说明中列为 remaining risks。

### 需要和用户讨论

- hparam sensitivity 是否必须进主文？如果数据回包慢，是否移到 supplementary？
- failure cases 是否作为主文 discussion 证据，还是只放补充材料？
- X-Field per-organ 缺失时，是否只保留 average comparison？

---

## V0.8 Result Integration and Claim Calibration：结果整合与结论校准版

### 阶段目标

把真实实验数据写回论文，统一图、表、正文、摘要、结论中的说法，避免 claim 强于数据。

### 入口条件

- `V0.7` 的主实验资产和关键表格已补齐或明确降级处理。
- 主 PSNR2D / SSIM2D / efficiency / ablation / view-count 的最终采用版本已确认。

### 核心交付物

- [ ] 更新 `main.tex` 中摘要、实验段落、讨论和结论的结果表述。
- [ ] 更新 figure captions 和 table captions，让 setting、method、metric、unit 清楚。
- [ ] 校准 SSIM2D 相关 claim：2-view / 3-view 可以强调领先，4-view 与 R2-Gaussian 第三位持平时必须谨慎。
- [ ] 校准 efficiency claim：只有在 Time / #Gaussians / Mem / FPS 真实回包后才写效率优势。
- [ ] 消融段落与 `SPS / GAP / ADM` 的真实贡献一致，不把未验证的中间结果写成强结论。

### 关键检查点

- 主文 strongest result 是否来自 `5 organs x {2,3,4} views`。
- `XRA-GS` 与 R2-Gaussian 的提升幅度是否在摘要/引言/结论中一致。
- 表格中的 Avg、正文中的提升幅度、caption 中的描述是否一致。
- 所有 `pending logs`、`to be completed`、实验占位语句是否删除或改写。

### 验收条件

- [ ] `main.tex` 不再写任何等待实验日志的句子。
- [ ] 摘要中的定量结果能在主表中直接找到。
- [ ] 每张主文 figure/table 都有明确首次引用。
- [ ] reviewer 不会因为 claim 过强而抓住 4-view SSIM 持平或 efficiency 缺失问题。

### Push 约定

- 用户确认“结果和 claim 已经统一，可以进入审稿视角打磨”后，push `v0.8-result-integrated`。

### 需要和用户讨论

- 摘要中最强结果到底用 PSNR2D、SSIM2D、efficiency 还是 ablation 表达？
- 如果某些 baseline 的 SSIM2D 不完整，是否在主文保留 SSIM 表，还是移到 supplement？

---

## V0.9 Review-Ready Draft：PG 顶会审稿视角版

### 阶段目标

从审稿人视角检查论文是否像一篇可外审的 PG 顶会论文：故事线清楚、创新点突出、实验充分、局限诚实、格式稳定。

### 入口条件

- `V0.8` 已完成结果整合。
- 主文不再有实验占位或待确认数值。

### 核心交付物

- [ ] 完整英文稿通读修改一轮。
- [ ] 摘要按 `problem -> gap -> insight -> method -> strongest evidence` 收紧。
- [ ] 引言贡献点与 `SPS / GAP / ADM` 对齐。
- [ ] Related Work 明确给出与 CoR-GS、DNGaussian、FSGS、R2-Gaussian、X-Gaussian、X-Field 的定位差异。
- [ ] Method 中三模块动机、公式、算法、图示一致。
- [ ] Experiments 中主结果、消融、效率、敏感性、失败案例的主次关系明确。
- [ ] 准备 reviewer 可能质疑点清单：提升幅度、baseline 公平性、X-Field 缺失项、parallel-beam 限制、2-view 失败模式。

### 关键检查点

- 是否仍有中文、口语化表达、博客式衔接。
- 图表是否靠近首次引用位置。
- figure/table caption 是否能独立阅读。
- 是否存在重复 label、缺失引用、未引用图表。
- 参考文献是否足够覆盖 sparse-view NVS、tomographic reconstruction、X-ray Gaussian methods。

### 验收条件

- [ ] 用户确认“可以给外部同学/导师/审稿视角阅读”。
- [ ] `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` 通过。
- [ ] PDF 阅读上没有明显空白、错图、错表、编号错乱。

### Push 约定

- 用户确认 review-ready 后，push `v0.9-review-ready`。

### 需要和用户讨论

- 是否需要再找其他 AI agent 做一轮 code-review / paper-review？
- 是否需要补一个 supplementary material 初稿？
- 目标 PG 模板是否已经最终确定？

---

## V1.0 Submission Candidate：正式投稿候选版

### 阶段目标

形成可以上传投稿系统的候选包，重点是格式、匿名性、完整性和最终资产一致性。

### 入口条件

- `V0.9` 已通过用户和至少一轮审稿视角检查。
- 所有科学结论已锁定。

### 核心交付物

- [ ] 最终 `main.pdf`。
- [ ] 最终 `main.tex`、`references.bib`、`assets/fig/`、`assets/tables/`。
- [ ] 如需要，补充材料 PDF / zip。
- [ ] 匿名性检查：作者、机构、路径、致谢、自引措辞。
- [ ] 格式检查：页数、字体、图表清晰度、参考文献格式、编译无错误。
- [ ] 文件打包检查：投稿系统需要的 PDF、source、supplement 均准备好。

### 关键检查点

- 无占位符。
- 无未解释的 `--`。
- 无 `pending`、`to be completed`、`TODO`。
- 无缺图、缺表、重复 label、未解析引用。
- 所有图片可印刷、缩小后可读。

### 验收条件

- [ ] 用户口头确认 `V1.0 ok`。
- [ ] 最终 PDF 与源码状态一致。
- [ ] 任何未完成项都不影响正式投稿，或已明确记录为后续 rebuttal / extension 准备。

### Push 约定

- 用户确认后 push `v1.0-submission-candidate`。
- 建议同时打 tag，但是否打 tag 需用户明确确认。

### 需要和用户讨论

- 是否需要 cover letter 或投稿系统 metadata 草稿？
- 是否需要提前准备 reviewer response 风险表？
- supplement 是否单独提交，还是暂不提交？

---

## V1.1 Final Submission Lock：提交前锁版

### 阶段目标

投稿前最后锁定版本。此阶段不再改变科学结论和实验选择，只修提交阻塞问题。

### 入口条件

- `V1.0` 已被用户确认可投。
- 投稿系统要求已经明确。

### 允许修改

- 编译错误。
- 文件路径错误。
- 错别字。
- 图表编号或引用错误。
- 投稿系统格式要求导致的页边距、匿名信息、补充材料打包问题。

### 不允许修改

- 不新增未经验证实验。
- 不改变核心 claim。
- 不替换 baseline 集合。
- 不重写方法主线。

### 验收条件

- [ ] 最终提交文件与仓库状态一致。
- [ ] 投稿系统上传预览无格式问题。
- [ ] 提交后记录 submission ID、提交时间、最终 push/tag 状态。

### Push 约定

- 提交前最后 push `v1.1-final-submission`。
- 提交后如有 submission ID，可在用户允许后记录到本地非匿名管理文件；不要写入投稿源码中。

### 需要和用户讨论

- 最终提交是否由用户手动完成。
- 提交后是否需要创建 rebuttal preparation todo。

---

## 当前下一步建议

1. 先和用户确认是否将当前状态作为 `V0.6` push 留档。
2. 若不 push baseline，直接推进 `V0.7`：优先处理 P0 ask 回包与主实验图/表缺口。
3. 到 `V0.7` 验收时再决定哪些实验进入主文，哪些降级到 supplementary。
