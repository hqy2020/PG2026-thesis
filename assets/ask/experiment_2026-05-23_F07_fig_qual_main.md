## 需求描述

生成论文主定性对比图 F07：在统一 2-view setting 下，对 Chest、Head、Abdomen、Foot、Pancreas 五个器官展示 GT、六个 baseline 与 XRA-GS 的 novel-view X-ray projection，对应支持 `main.tex` 中 Figure `fig:qual-main` 的定性结论。

## 输入

- Methods：GT, CoR-GS, DNGaussian, FSGS, X-Field*, X-Gaussian, R2-Gaussian, XRA-GS。
- Organs：Chest, Head, Abdomen, Foot, Pancreas。
- View count：2-view setting。
- Novel view：每个 organ 选择同一个有代表性的 novel angle，优先 45°；如不同 organ 使用不同 angle，必须在 answer 中说明。
- 主文目标图路径：`assets/fig/experiment_fig_qual_main.png`。

## 期望输出

### 原始数据

请将原始渲染结果放入：`assets/data/experiment_f07_qual_main/`。

建议结构：

- `assets/data/experiment_f07_qual_main/gt/{organ}_2v_gt.png`
- `assets/data/experiment_f07_qual_main/{method}/{organ}_2v_novel.png`
- `assets/data/experiment_f07_qual_main/{method}/{organ}_2v_error.png`
- `assets/data/experiment_f07_qual_main/vmax.txt`
- `assets/data/experiment_f07_qual_main/metadata.csv`

`metadata.csv` 字段：

```csv
organ,case_id,views,novel_angle,method,render_path,gt_path,error_path,psnr2d,ssim2d,checkpoint,config,log_path
```

### 最终图

- `assets/fig/experiment_fig_qual_main.png`
  - 5 rows：Chest / Head / Abdomen / Foot / Pancreas。
  - Columns：GT / CoR-GS / DNGaussian / FSGS / X-Field* / X-Gaussian / R2-Gaussian / XRA-GS / Error map。
  - XRA-GS 列置于最后一个方法列。
  - 每行 grayscale render 使用同一 window；error map 使用 inferno，并全图共享 `vmax`。
  - 为 Chest 和 Foot 标出可供 F08 使用的 zoom box，并在 metadata 中记录 crop 坐标。

### 拼图脚本

如方便，请同时提供：

- `assets/scripts/experiment_build_qual_main.py`

脚本应从 `assets/data/experiment_f07_qual_main/` 读取数据并生成 `assets/fig/experiment_fig_qual_main.png`，不要把数值或路径硬编码到论文外部目录。

### 回包说明

请在 `assets/answer/experiment_2026-05-23_F07_fig_qual_main.md` 中列出：

- 完成的文件路径。
- 每个 organ 的 case ID、input view angles、novel view angle。
- 各方法 checkpoint / config / log path。
- error map 的 vmax 计算方式。
- 若某个 baseline 暂缺，明确说明是未跑完、日志缺失、还是无法复现；不要用空白图或伪造图补位。

## 优先级

P0（主结果定性图，且 F08/F12 依赖它的原始渲染输出）。

## 截止时间

尽快；当前主文对应位置仍是 placeholder。
