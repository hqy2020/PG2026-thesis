## 需求描述

生成论文 F09：progressive ablation 定性可视化，展示 Baseline → +SPS → +SPS+GAP → Full XRA-GS 的局部视觉改善和 residual/error map 变化，并提供与 T03 ablation 表一致的指标追溯。

## 输入

- Setting：Chest 3-view。
- Configs：Baseline (R2-Gaussian backbone), +SPS, +SPS+GAP, Full XRA-GS。
- Required visual columns：GT, Baseline, +SPS, +SPS+GAP, Full XRA-GS, error/residual map。
- 需与 `assets/tables/tab_experiment_component.tex` 的 progressive ablation 定义一致。

## 期望输出

### 原始数据

请输出到 `assets/data/experiment_f09_ablation_visual/`：

- `gt_chest_3v.png`
- `baseline_chest_3v.png`
- `sps_chest_3v.png`
- `sps_gap_chest_3v.png`
- `full_xra_gs_chest_3v.png`
- 各配置对应 error map PNG。
- `metrics.csv`

`metrics.csv` 字段：

```csv
config,organ,case_id,views,novel_angle,psnr2d,ssim2d,delta_psnr2d_vs_baseline,delta_ssim2d_vs_baseline,render_path,error_path,checkpoint,config_path,log_path
```

### 最终图

- `assets/fig/experiment_fig_ablation_visual.png`
  - 显示 GT / Baseline / +SPS / +SPS+GAP / Full XRA-GS。
  - 下方标注相对 Baseline 的 `ΔSSIM2D`；GT 不标，Baseline 标为 0 或省略。
  - error map 使用 inferno，vmax 与 F07/F08 可比；若不能共用，需说明原因。

### 与表格一致性

请同时确认：

- `assets/tables/tab_experiment_component.tex` 中 Baseline / +SPS / +SPS+GAP / Full 的 PSNR2D 是否来自同一批 checkpoint。
- Full XRA-GS 的 3-view PSNR2D / SSIM2D 是否与主表 Avg 一致。
- 中间配置的 SSIM2D 是否可用于补齐 T03 表。

### 回包说明

请在 `assets/answer/experiment_2026-05-23_F09_fig_ablation_visual.md` 中列出完成文件、case ID、checkpoint、日志路径、vmax、crop 坐标和指标来源。

## 优先级

P0（支撑 Module Analysis，且与 T03 progressive ablation 表直接相关）。

## 截止时间

尽快；优先级与 F07 相同。
