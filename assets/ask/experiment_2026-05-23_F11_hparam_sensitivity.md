## 需求描述

补齐 hyperparameter sensitivity 实验数据，并确认 ADM warmup 默认值冲突。当前 `assets/data/experiment_tab_hparam_sensitivity.csv` 中 PSNR2D / SSIM2D 全为空，无法支持 `main.tex` 中 local optimum / robust conclusion 的表述。

## 输入

- Existing placeholder CSV：`assets/data/experiment_tab_hparam_sensitivity.csv`
- Existing script：`assets/scripts/experiment_fig_hparam_generate.py`
- Figure target：`assets/fig/experiment_fig_hparam.png`
- Setting：请先确认是 Chest 3-view 单器官，还是 five-organ average。
- Sweep params：
  - `sps_alpha`: 0.00, 0.25, 0.50, 0.75, 1.00
  - `gap_threshold`: 0.01, 0.02, 0.04, 0.08, 0.16
  - `adm_rank`: 4, 8, 16, 32, 64
  - `adm_warmup`: 0.00, 0.10, 0.25, 0.50, 0.75 fraction of 30K iterations

## 期望输出

### 数据

请填充或重建：

- `assets/data/experiment_tab_hparam_sensitivity.csv`

字段保持为：

```csv
param,value,psnr2d,ssim2d,is_default
```

如需要更强追溯，请额外输出：

- `assets/data/experiment_tab_hparam_sensitivity_meta.csv`

字段：

```csv
param,value,organ,case_id,views,psnr2d,ssim2d,checkpoint,config,log_path,commit
```

### ADM warmup 默认值确认

当前存在冲突：

- `main.tex` 写 ADM activates after 15K iterations。
- `assets/scripts/experiment_fig_hparam_generate.py` 将 0.25 标为 `7.5K (default)`。
- `assets/data/experiment_tab_hparam_sensitivity.csv` 也将 `adm_warmup,0.25` 标为 default。

请用真实训练 config / command / log 确认默认值到底是：

- 0.25 = 7.5K，还是
- 0.50 = 15K。

如果默认值是 15K，请把 CSV 中 `is_default` 标记改为 0.50；如果默认值是 7.5K，请明确说明主文的 15K 应改掉。

### 图像

如果数据补齐，请运行或提供可运行方式生成：

- `assets/fig/experiment_fig_hparam.png`

若无法生成图，请至少返回完整 CSV，主仓库可自行绘图。

### 回包说明

请写入：

- `assets/answer/experiment_2026-05-23_F11_hparam_sensitivity.md`

说明：

- sweep 是否每次只改一个参数。
- 其他参数的固定默认值。
- metric 是 Chest-only 还是 five-organ average。
- 是否支持主文中的 “default lies close to local optimum” 和 “remains above R2 baseline across most tested range”。
- 对不支持的主文表述给出建议改写。

## 优先级

P1（当前数据全空；若主文保留该图和相关结论，则会升级为 P0）。

## 截止时间

主结果表回包后尽快。
