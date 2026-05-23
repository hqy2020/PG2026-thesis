## 需求描述

导出真实 Gaussian spatial distribution 数据，用于生成 F10 spatial distribution figure。当前仓库中只有 image2 概念图脚本/提示，缺少真实 Gaussian centers、profile 和 stage-wise counts；该图应基于真实实验数据，而不是生成式示意图。

## 输入

- Target figure：`assets/fig/experiment_fig_spatial_distribution.png`
- Existing prompt/script reference：
  - `assets/prompts/experiment_fig_spatial_distribution_image2_prompt.md`
  - `assets/scripts/experiment_fig_spatial_distribution_image2_call.py`
- Setting：优先 Chest 3-view。
- Stages：
  - Uniform Init / Baseline initialization
  - +SPS
  - +SPS+GAP
  - Full XRA-GS
- 需要与 progressive ablation / method module 定义一致。

## 期望输出

### 数据

请输出到 `assets/data/experiment_f10_spatial_distribution/`：

- `uniform_init_xyz.npy` 或 `.csv`：Uniform Init / baseline stage 的 Gaussian center 坐标。
- `sps_xyz.npy` 或 `.csv`：+SPS stage 的 Gaussian center 坐标。
- `sps_gap_xyz.npy` 或 `.csv`：+SPS+GAP stage 的 Gaussian center 坐标。
- `full_xra_gs_xyz.npy` 或 `.csv`：Full XRA-GS 的 Gaussian center 坐标。
- `profile_chest_3v.csv`：沿选定 axis 的 density/profile 曲线。
- `counts.csv`

`counts.csv` 字段：

```csv
stage,organ,case_id,views,n_gaussians,checkpoint,config,log_path,commit
```

`profile_chest_3v.csv` 字段：

```csv
stage,axis,bin_center,density_or_count
```

### 图像

如方便，请生成：

- `assets/fig/experiment_fig_spatial_distribution.png`

图应展示 stage-wise Gaussian spatial distribution，并标注真实 #Gaussians。若只提供数据不生成最终图，也可以接受。

### 追溯说明

请写入：

- `assets/answer/experiment_2026-05-23_F10_spatial_distribution_data.md`

说明：

- 使用的 organ / case ID / view count。
- Gaussian center 坐标单位和坐标系。
- 各 stage 对应的 checkpoint 或训练迭代。
- 当前主文中 `≈50K → ≈42K → ≈38K → ≈35K` 是否真实；若不是，请给出真实数值和建议改写。

## 优先级

P1（机制分析支撑图；当前主文有 “will be confirmed from experiment logs” 风险）。

## 截止时间

主指标和 ablation 数据回包后尽快。
