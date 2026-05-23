## 需求描述

补齐 progressive component ablation 表中缺失的中间配置 SSIM2D，并核对 PSNR2D 是否与同一批 checkpoint / config 对齐。该请求用于支撑 `main.tex` 中“across all metrics”单调不退化的论断。

## 输入

- Table：`assets/tables/tab_experiment_component.tex`
- Configs：
  - Baseline (R2-Gaussian backbone)
  - +SPS
  - +SPS+GAP
  - Full XRA-GS (+SPS+GAP+ADM)
- Views：2, 3, 4。
- Organs：Chest, Head, Abdomen, Foot, Pancreas。
- Metrics：PSNR2D, SSIM2D。
- 当前表中已有 PSNR2D：
  - Baseline：21.27 / 27.80 / 29.10
  - +SPS：21.44 / 28.01 / 29.16
  - +SPS+GAP：21.44 / 28.22 / 29.20
  - Full XRA-GS：21.44 / 28.22 / 29.20
- 当前表中只有 Full XRA-GS 的 SSIM2D：0.797 / 0.904 / 0.924。

## 期望输出

- `assets/data/experiment_tab_progressive_ablation.csv`

字段：

```csv
config,organ,views,psnr2d,ssim2d,case_count,checkpoint,config_path,log_path,commit
```

要求：

- 输出 per-organ 原始值与 five-organ average。
- 补齐 Baseline / +SPS / +SPS+GAP 的 2v/3v/4v SSIM2D。
- 确认 Full XRA-GS 的 PSNR2D / SSIM2D 是否与主表 Avg 完全一致。
- 确认 +SPS、+SPS+GAP、Full 三者是否确实是 progressive 累加配置，而不是 single-module 配置。
- 若某个配置缺失，请说明是否需要重跑、预计耗时、可否先用 PSNR-only 表述替代。

### 可替换 LaTeX 行

请在 answer 中附上 `assets/tables/tab_experiment_component.tex` 可替换的四行 LaTeX 内容。

### 回包说明

请写入：

- `assets/answer/experiment_2026-05-23_T03_progressive_ablation_ssim.md`

内容包括：

- 完成文件路径。
- 每个配置的 checkpoint / config / log path。
- average 计算过程。
- 是否支持“monotonically non-decreasing trend across all metrics”这句话；若不支持，请指出哪一项下降。

## 优先级

P0（当前表中存在 `--` 和 `data-pending`，且正文已有 all metrics 结论）。

## 截止时间

尽快。
