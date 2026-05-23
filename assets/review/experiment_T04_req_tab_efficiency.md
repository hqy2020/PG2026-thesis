# T04. Efficiency — 效率与资源对比表

> 类型: table
> 状态: BLOCKED (data-pending)
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 与主对比表配套：证明 XRA-GS 不仅效果好，还在训练时间 / 显存 / 高斯数量 / 渲染速度上具备竞争力。
- 回答审稿人："你的方法是不是堆资源换效果？"
- 缺这张表，正文 "efficient" 类陈述没有支撑，顶会审稿易判为"未量化效率"。

## 2. 排版位置建议
- 主文 §4.2 Main Results 末尾或 §4.4 Efficiency 子节。
- 宽度：`\linewidth`（单栏）。
- 与 [[req_tab_main_psnr2d]] / [[req_tab_main_ssim2d]] 配套，单独成表。

## 3. 期望元素 (What must be in it)
- 行 = 3 方法（聚焦最相关对比，避免堆 6 baseline）：
  1. `X-Gaussian`
  2. `R2-Gaussian`（最强 baseline）
  3. `XRA-GS (Ours)`
- 列 = 5：
  - `Train Time ↓ (min)`
  - `#Gaussians ↓ (×10³)`
  - `GPU Mem ↓ (GB)`
  - `Render FPS ↑`
  - `PSNR2D ↑ (dB, 3-view Avg)` ← 用一列锚定"在相同质量下比效率"
- setting 锁定：3-view，5 organ 平均
- 数值精度：
  - Train Time：整数分钟
  - #Gaussians：保留 1 位小数
  - GPU Mem：保留 1 位小数
  - Render FPS：整数
  - PSNR2D：2 位小数
- 高亮规则（[[VISUAL_STYLE]] §5）：
  - 每列 best：加粗 + Crimson 背景
  - 表头 ↑/↓ 紧跟单位
- Ours 行名加粗 + Crimson 下划线

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5
- 参考论文锚点：
  - `参考论文/xgs.pdf` **Tab. 3**（训练时间 + 显存 + FPS 三栏）
  - `参考论文/r2gs.pdf` **Tab. 4**（效率与质量同表锚定）
  - `参考论文/FSGS.pdf` **Tab. 5**（少行多指标紧凑布局）
- 不借鉴：把效率与主对比合并到一个超大表（信息超载）。

## 5. 数据来源/依赖
- 3 方法 × 5 列 = 15 个数值，需要在同一硬件下复现实验
- 输出路径：`assets/data/tab_efficiency_3view.csv`（cols: method, train_time_min, n_gaussians_k, gpu_mem_gb, render_fps, psnr2d）
- **数据缺口**：实验 agent 还未交付 — 跟踪 `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md`，待 `assets/answer/` 回包。
- 依赖：[[VISUAL_STYLE]]、[[req_tab_main_psnr2d]]（PSNR2D 列必须与主表 3v Avg 一致）。

## 6. Caption 草稿骨架 (英文)
> **Efficiency comparison under the 3-view setting (averaged over five organs).** Train Time and GPU memory are measured on a single NVIDIA <P0: device>. XRA-GS uses fewer Gaussians than R2-Gaussian, trains in less wall-clock time, and renders at a comparable frame rate while delivering the highest PSNR2D — XRA-GS does not trade quality for cost.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 行 = 3 方法，顺序：X-Gaussian → R2-Gaussian → XRA-GS
- [ ] 列 = 5：Train Time / #Gaussians / GPU Mem / Render FPS / PSNR2D
- [ ] 单位与方向 ↑↓ 完整标注
- [ ] 数值精度按本节规定
- [ ] PSNR2D 列与 [[req_tab_main_psnr2d]] 3v Avg 一致
- [ ] 每列 best 加粗 + Crimson 背景
- [ ] Ours 行名加粗 + Crimson 下划线
- [ ] caption 注明硬件
- [ ] 当前不写编造数值，所有未到位单元格用 `--` 占位
- [ ] 表格不是截图，独立 `.tex` 文件

## 8. 反例 (Do NOT do this)
- 在表里编造效率数值"凑齐"。等不来就保留 `--` 加 caption "to be completed"。
- 把 6 个 baseline 全列进效率表（信息过载，主对比已在 [[req_tab_main_psnr2d]] 覆盖）。
- 单独成图（折线图）展示训练时间（更细的训练动力学留给 [[req_fig_supp_training_curve]]）。
- 显存数值用不同硬件混测。

## 9. 备注
- 当前 `assets/tables/tab_efficiency.tex` 是占位版，含 `--`。等 [[req_tab_efficiency]] 数据到位后整体重渲。
- 与 [[req_fig_supp_training_curve]] 共享 dump（曲线给细，表给收敛终值）。
