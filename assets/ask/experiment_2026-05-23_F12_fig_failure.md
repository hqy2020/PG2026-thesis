## 需求描述

生成论文 F12 failure cases 图，用于 Discussion / Limitations 中展示 XRA-GS 在极端 sparse-view setting 下仍存在的失败模式。该图必须使用真实失败 case，不要挑选成功样例伪装为 failure。

## 输入

- Methods：GT, R2-Gaussian, XRA-GS。
- Setting：2-view。
- Organs：Foot 与 Pancreas。
- 优先复用 F07 的原始渲染数据；若 F07 中样例不够典型，可另选 case，但需说明选择理由。

## 期望输出

### 原始数据

请输出到 `assets/data/experiment_f12_failure_cases/`：

- `foot_gt.png`, `foot_r2_gaussian.png`, `foot_xra_gs.png`, `foot_xra_gs_error.png`
- `pancreas_gt.png`, `pancreas_r2_gaussian.png`, `pancreas_xra_gs.png`, `pancreas_xra_gs_error.png`
- `metadata.csv`

`metadata.csv` 字段：

```csv
organ,case_id,views,novel_angle,method,render_path,gt_path,error_path,psnr2d,ssim2d,failure_region,crop_x,crop_y,crop_w,crop_h,checkpoint,config,log_path
```

### 最终图

- `assets/fig/experiment_fig_failure_cases.png`
  - 2 rows：Foot 2-view / Pancreas 2-view。
  - Columns：GT / R2-Gaussian / XRA-GS / XRA-GS error map。
  - 每行包含 zoom box，标出主要失败区域。
  - 每行右侧或 caption metadata 中提供不超过 25 words 的英文 failure description。

建议 failure description：

- Foot：`Fine trabecular structures remain ambiguous under two-view supervision.`
- Pancreas：`Low-contrast boundaries remain difficult to separate from surrounding tissue.`

### 回包说明

请在 `assets/answer/experiment_2026-05-23_F12_fig_failure.md` 中说明：

- 是否复用 F07 case；如不复用，说明为什么。
- 每个 failure case 的 PSNR2D / SSIM2D。
- error map vmax 是否与 F07 共用。
- 所选失败区域的坐标和现象。

## 优先级

P2（Discussion 支撑图；F07 完成后再处理）。

## 截止时间

F07 回包后完成即可。
