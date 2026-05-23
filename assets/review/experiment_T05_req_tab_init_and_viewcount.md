# T05. Init + Viewcount — 初始化消融 + 视角趋势 (合并表)

> 类型: table
> 状态: ready-to-draw
> 优先级: P1
> 主文/补充: main

## 1. 目的 (Why)
- 把"初始化方式 (random / FDK / SPS) 对最终质量影响"与"视角数 (2 → 4) 对各方法稳定性影响"两件相关的消融合并到一张表，节省主文版面。
- 回答审稿人 1："你强调 SPS 比 random 强，到底领先多少？"
- 回答审稿人 2："视角从 2 → 4，XRA-GS 比 baseline 衰减得快还是慢？"
- 缺这张表，[[req_fig_module_sps]] 与正文"sparse-view 稳定性"陈述都没有数字。

## 2. 排版位置建议
- 主文 §4.3 / §4.4 之间，作为补充消融。
- 宽度：`\textwidth`（跨双栏，因左右两个 sub-table）。
- LaTeX 用 `\begin{table*}` + `\begin{minipage}{0.48\linewidth}` × 2 实现左右并排。

## 3. 期望元素 (What must be in it)

### 左半 — Init Ablation
- 行 = 3 初始化方式：
  1. `Random`
  2. `FDK only` (用 FDK 粗重建作 dense init)
  3. `SPS (Ours)`
- 列 = 2：`PSNR2D ↑` / `SSIM2D ↑`，setting = Chest 3-view（与 [[req_fig_module_sps]] 同 setting）
- SPS 行加粗 + Crimson 下划线

### 右半 — View-count Trend
- 行 = 4 方法（精选）：
  1. `FSGS`
  2. `X-Gaussian`
  3. `R2-Gaussian`
  4. `XRA-GS (Ours)`
- 列 = 3：`2v` / `3v` / `4v`，单一 metric = PSNR2D ↑（5 organ Avg）
- 表底加一行 `Δ(4v−2v)`：每方法在 4v 比 2v 涨了多少（小越好则证明 sparse 鲁棒；本图反之，看绝对值越小越鲁棒？这里写"涨幅越小越说明 baseline 已经接近饱和、Ours 在 2v 上更有优势"）—— caption 解释方向

### 两个 sub-table 顶部共用一个 9pt 加粗 label：`Table T05. Initialization ablation (left) and view-count trend (right).`

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5
- 参考论文锚点：
  - `参考论文/FSGS.pdf` **Tab. 3**（初始化消融）
  - `参考论文/Corgs.pdf` **Tab. 5**（view-count trend）
  - `参考论文/xgs.pdf` **Tab. 4**（左右并排表的版式）
- 不借鉴：把 init 与 view-count 揉成一个 4D 表（行=方法×init，列=view，难读）。

## 5. 数据来源/依赖
- 左半：3 init × 1 organ × 1 view × 2 metric = 6 数值
- 右半：4 方法 × 3 view × 1 metric = 12 数值
- 输出路径：
  - `assets/data/tab_init_ablation.csv`
  - `assets/data/tab_view_count_trend.csv`
- 数据缺口：
  - 左半 需要实验 agent 跑 random / FDK-only 两份消融
  - 右半 数据从 [[req_tab_main_psnr2d]] 直接取，但要包含 FSGS（如未在主表则需补）
- 依赖：[[req_fig_module_sps]]、[[req_tab_main_psnr2d]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Left:** Initialization ablation on Chest 3-view. SPS substantially improves both PSNR2D and SSIM2D over random and FDK-only initialization, validating that the attenuation-aligned seeding is responsible for the early-stage gain in Figure [[req_fig_supp_training_curve]]. **Right:** PSNR2D trend across view counts averaged over five organs. While all methods degrade as views decrease, XRA-GS maintains the smallest absolute drop from 4-view to 2-view.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 左半 3 行 init 顺序固定：Random → FDK only → SPS
- [ ] 右半 4 行方法顺序：FSGS → X-Gaussian → R2-Gaussian → XRA-GS
- [ ] 左半 SPS 行、右半 XRA-GS 行均加粗 + Crimson 下划线
- [ ] 左半 Chest 3-view、右半 5 organ Avg，caption 明确区分
- [ ] PSNR 2 位小数、SSIM 3 位小数
- [ ] 单一 LaTeX `table*` 容器、两个 minipage 并排
- [ ] 表底 Δ(4v−2v) 行有明确方向说明（越小越稳）
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 把左右两表用不同精度（左 2 位、右 3 位等内部冲突）。
- 用 view-count 趋势画折线图替代表（折线图留给 [[req_fig_supp_training_curve]] 或 [[req_fig_hparam]]，主文用表更紧凑）。
- 在 init 消融里加 `+random+SPS` 这种无意义混合行。
- 把左右两表分两张独立 table 排两个版面（违反合并意图）。

## 9. 备注
- 当前 `assets/tables/tab_init_ablation.tex` 与 `tab_view_count.tex` 是分立的，按本需求合并为单一 `tab_init_and_viewcount.tex` 或保留两个 sub-tex 由主 tex 拼装。
- 与 [[req_fig_module_sps]] 共享 SPS 行的视觉论证。
