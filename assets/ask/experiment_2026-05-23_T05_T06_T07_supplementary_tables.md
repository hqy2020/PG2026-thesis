## 需求描述

补齐 supplementary tables 所需数据，并核对当前未引用/旧表中的数值一致性。该请求覆盖 init ablation、view-count consistency、per-organ SSIM2D supplementary、single-module ablation。

## 输入

- Main protocol：5 organs × 2/3/4 views。
- Organs：Chest, Head, Abdomen, Foot, Pancreas。
- Metrics：PSNR2D, SSIM2D。
- 相关文件：
  - `assets/tables/tab_experiment_init_viewcount.tex`
  - `assets/tables/tab_experiment_view_count.tex`
  - `assets/tables/tab_experiment_densify_vs_gap.tex`
  - `assets/review/experiment_T05_req_tab_init_and_viewcount.md`
  - `assets/review/experiment_T06_req_tab_supp_per_organ_ssim2d.md`
  - `assets/review/experiment_T07_req_tab_supp_single_module_ablation.md`

## 期望输出

### T05：Init ablation 与 view-count consistency

- `assets/data/experiment_tab_init_ablation.csv`

字段：

```csv
config,organ,views,psnr2d,ssim2d,checkpoint,config_path,log_path,commit
```

Configs：Random, SPS-guided, Full XRA-GS。

- `assets/data/experiment_tab_view_count_trend.csv`

字段：

```csv
method,organ,views,psnr2d,ssim2d,checkpoint,config_path,log_path,commit
```

请特别核对当前冲突：

- `tab_experiment_view_count.tex` 中 XRA-GS Avg：21.52 / 28.09 / 29.15。
- 主表和 `tab_experiment_init_viewcount.tex` 中 XRA-GS Avg：21.44 / 28.22 / 29.20。

请确认哪一组是最终统一协议下的真实结果，另一组是否为旧实验或不同设定。

### T06：Per-organ SSIM2D supplementary

- `assets/data/experiment_tab_supp_per_organ_ssim2d.csv`

字段：

```csv
method,organ,views,ssim2d,case_count,checkpoint,config_path,log_path,commit
```

优先覆盖所有主 baseline：CoR-GS, DNGaussian, FSGS, X-Field*, X-Gaussian, R2-Gaussian, XRA-GS。

若部分 baseline 无法提供，请说明原因，并给出论文中应如何表述 “unavailable logs”。

### T07：Single-module ablation

- `assets/data/experiment_tab_supp_single_module_ablation.csv`

字段：

```csv
config,organ,views,psnr2d,ssim2d,checkpoint,config_path,log_path,commit
```

Configs：

- Baseline
- +SPS only
- +GAP only
- +ADM only
- Full XRA-GS

请明确 `+GAP only` 和 `+ADM only` 的定义是否合理：它们是在 baseline 上单独加模块，还是在 SPS 初始化下替换/禁用其他模块。

### 旧表状态确认

请确认：

- `assets/tables/tab_experiment_densify_vs_gap.tex` 是否为旧版/废弃表。
- 若不是废弃，请说明其中 `+ADM` / `+GAP` 行的实验定义和指标来源。

### 回包说明

请写入：

- `assets/answer/experiment_2026-05-23_T05_T06_T07_supplementary_tables.md`

说明每个 CSV 的完成情况、不可用项、日志路径、average 校验和建议正文/补充材料表述。

## 优先级

P1（补充材料和一致性核对；其中 view-count 冲突若进入主文会升级为 P0）。

## 截止时间

P0 主表和 F07/F09 完成后处理。
