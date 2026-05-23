## 需求描述

生成论文 F08：局部细节放大与跨视角一致性图。该图用于支撑 XRA-GS 相比 R2-Gaussian / X-Gaussian 在局部边界、骨结构和不同 novel angle 下更稳定的定性结论。

## 输入

- 依赖 F07：`assets/data/experiment_f07_qual_main/` 中的原始 render、GT、error map 和 crop metadata。
- Detail cases：Chest 与 Foot，使用 F07 中标出的 zoom box。
- Consistency case：Chest 2-view，同一 case 在 0° / 45° / 90° 三个 novel angles 下的结果。
- Methods：GT, R2-Gaussian, X-Gaussian, XRA-GS。

## 期望输出

### 原始数据

- `assets/data/experiment_f08_detail_consistency/detail_crops.csv`

字段：

```csv
organ,case_id,views,method,source_path,crop_x,crop_y,crop_w,crop_h,crop_path,psnr2d,ssim2d
```

- `assets/data/experiment_f08_detail_consistency/consistency.csv`

字段：

```csv
organ,case_id,views,novel_angle,method,render_path,gt_path,error_path,psnr2d,ssim2d,checkpoint,config,log_path
```

- 对应 crop/render PNG 文件放在 `assets/data/experiment_f08_detail_consistency/` 子目录下。

### 最终图

- `assets/fig/experiment_fig_qual_detail_consistency.png`
  - 上半部分：Chest 与 Foot 的 zoom-in crops，列为 GT / R2-Gaussian / X-Gaussian / XRA-GS。
  - 下半部分：Chest 2-view 在 0° / 45° / 90° 下的 GT / R2-Gaussian / X-Gaussian / XRA-GS 对比。
  - grayscale window 与 F07 对齐；如包含 error map，必须复用 F07 的 `vmax`。

### 拼图脚本

如方便，请提供：

- `assets/scripts/experiment_build_qual_detail_consistency.py`

### 回包说明

请在 `assets/answer/experiment_2026-05-23_F08_fig_qual_detail_consistency.md` 中说明：

- 是否完全复用 F07 的 case 与 crop box。
- 三个 novel angles 的定义和渲染命令。
- 每个方法的 checkpoint / config / log path。
- 若 F07 尚未完成，请先返回依赖阻塞说明，不要生成不一致的临时图。

## 优先级

P1（依赖 F07；用于增强主结果的细节和跨视角论证）。

## 截止时间

F07 回包后尽快完成。
