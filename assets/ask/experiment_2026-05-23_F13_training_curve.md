## 需求描述

导出 supplementary training curve 数据，用于展示 Baseline / +SPS / Full XRA-GS 的训练收敛过程，并标注 GAP 与 ADM 的关键触发/启动迭代。

## 输入

- Setting：Chest 3-view。
- Curves：Baseline, +SPS, Full XRA-GS。
- Metric：training/evaluation PSNR2D over iterations；如果 SSIM2D 也有日志，可一并提供。
- Key events：
  - GAP first triggered iteration。
  - ADM warmup / activation iteration。
- 相关 review：`assets/review/experiment_F13_req_fig_supp_training_curve.md`。

## 期望输出

### 数据

- `assets/data/experiment_f13_training_curve_chest_3v.csv`

字段：

```csv
config,organ,case_id,views,iteration,psnr2d,ssim2d,loss,n_gaussians,event,checkpoint,config_path,log_path,commit
```

要求：

- 至少每 500 或 1000 iterations 采样一次。
- 覆盖完整训练过程，默认 0–30K iterations。
- 如果训练日志中没有 SSIM2D，可留空，但必须说明。
- `event` 字段用于标记 GAP first trigger、ADM activation 等关键节点。

### 图像

如方便，请生成：

- `assets/fig/experiment_fig_supp_training_curve.png`

如果只提供 CSV，也可以接受，主仓库可用脚本绘图。

### 回包说明

请写入：

- `assets/answer/experiment_2026-05-23_F13_training_curve.md`

说明：

- 使用的 case ID / checkpoint / config。
- 曲线是 train view 指标还是 validation/novel view 指标。
- GAP 与 ADM 的事件迭代是否与主文方法描述一致。
- 如果 ADM 默认启动迭代与 F11 请求确认结果冲突，请以真实 config 为准并明确指出。

## 优先级

P2（supplementary 增强项，不阻塞主文，但有助于解释收敛行为）。

## 截止时间

P0/P1 数据回包后处理。
