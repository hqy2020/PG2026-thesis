## 需求描述

补齐主实验表与 efficiency 表的阻塞数据，重建此前断链的 `experiment_2026-05-21_efficiency-and-ssim.md` 所覆盖的核心任务。所有数值必须来自统一实验协议下的真实日志，不允许编造或从图中估计。

## 输入

- Task：Sparse Tomographic View Synthesis。
- Method name：XRA-GS。
- Main protocol：5 organs × 2/3/4 views。
- Organs：Chest, Head, Abdomen, Foot, Pancreas。
- Main metrics：PSNR2D, SSIM2D。
- Main baselines：CoR-GS, DNGaussian, FSGS, X-Field*, X-Gaussian, R2-Gaussian, XRA-GS。
- Efficiency setting：3-view，五器官平均；methods 为 X-Gaussian, R2-Gaussian, XRA-GS。
- 相关主稿/表格：
  - `assets/tables/tab_experiment_comparison.tex`
  - `assets/tables/tab_experiment_comparison_ssim.tex`
  - `assets/tables/tab_experiment_efficiency.tex`

## 期望输出

### T01：主 PSNR2D 矩阵

- `assets/data/experiment_tab_main_psnr2d.csv`

字段：

```csv
method,organ,views,psnr2d,case_count,log_path,checkpoint,config,commit
```

要求：

- 覆盖 7 methods × 5 organs × 3 view counts。
- 特别补齐当前表中缺失的 X-Field* per-organ PSNR2D。
- 额外输出 five-organ average 校验表：`assets/data/experiment_tab_main_psnr2d_avg_check.csv`。
- 确认 X-Field* Avg 是否为 20.57 / 24.97 / 26.41。
- 确认 XRA-GS Avg 是否为 21.44 / 28.22 / 29.20，若不是请说明当前主表中数值来自哪里。

### T02：主 SSIM2D 矩阵

- `assets/data/experiment_tab_main_ssim2d.csv`

字段：

```csv
method,organ,views,ssim2d,case_count,log_path,checkpoint,config,commit
```

要求：

- 优先覆盖 7 methods × 5 organs × 3 view counts。
- 若 CoR-GS / DNGaussian / FSGS / X-Gaussian 的统一协议 SSIM2D 日志不可用，请逐项说明不可用原因。
- 至少补齐 X-Field*, R2-Gaussian, XRA-GS 的 per-organ SSIM2D，并输出 average 校验。
- 当前主表中的 X-Field* / R2-Gaussian / XRA-GS SSIM2D Avg 为：
  - X-Field*: 0.717 / 0.850 / 0.880
  - R2-Gaussian: 0.794 / 0.903 / 0.924
  - XRA-GS: 0.797 / 0.904 / 0.924
  请确认这些数值是否来自五器官平均。

### T04：Efficiency 表

- `assets/data/experiment_tab_efficiency_3view.csv`

字段：

```csv
method,organ,views,train_time_min,n_gaussians_k,gpu_mem_gb,render_fps,psnr2d,ssim2d,hardware,log_path,checkpoint,config,commit
```

要求：

- Methods：X-Gaussian, R2-Gaussian, XRA-GS。
- View count：3-view。
- 输出 per-organ 原始值与 five-organ average。
- 统计口径必须说明：
  - train time 是否为完整训练 wall-clock minutes。
  - `n_gaussians_k` 是否为 final Gaussian count。
  - GPU memory 是否为 peak allocated / peak reserved / nvidia-smi peak。
  - render FPS 的分辨率、batch size、测量 view 数。
- PSNR2D 需与主表 3-view Avg 对齐：X-Gaussian 23.19，R2-Gaussian 27.83，XRA-GS 28.22；如不一致，请说明原因。

### 可替换 LaTeX 行

在 answer 中附上可替换的 LaTeX 表格行，但 CSV 是第一优先级。

### 回包说明

请将说明写入：

- `assets/answer/experiment_2026-05-23_T01_T02_T04_main_metrics_efficiency.md`

说明必须包含：

- 完成的文件路径列表。
- 每个方法的代码版本、checkpoint、config、日志路径。
- 是否完全同一协议。
- 任何缺失项的原因和建议替代写法。

## 优先级

P0（阻塞主结果表、SSIM2D 表和 computational cost 段落）。

## 截止时间

尽快；这是当前最关键的数据回包。
