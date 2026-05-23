# T01. Main PSNR2D — 主对比表 (PSNR2D)

> 类型: table
> 状态: data-pending
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 全文最重的定量证据之一：在 5 organs × {2,3,4} views 上，XRA-GS 与 6 baseline 的 PSNR2D ↑ 全矩阵对比。
- 回答审稿人："你的主指标到底领先多少？在哪些 organ/view 上领先？哪里没赢？"
- 缺这张表，正文 "consistently outperforms" 类陈述就没有可验证的数字支撑。

## 2. 排版位置建议
- 主文 §4.2 Main Results 第一张表，先于 [[req_tab_main_ssim2d]] 与 [[req_fig_qual_main]]。
- 宽度：`\textwidth`（跨双栏，table*）。
- 与 [[req_tab_main_ssim2d]] 上下排版，共用 baseline 顺序与高亮规则。

## 3. 期望元素 (What must be in it)
- 行 = 7 方法，按 [[VISUAL_STYLE]] §4 固定顺序：
  1. `CoR-GS`
  2. `DNGaussian`
  3. `FSGS`
  4. `X-Field`
  5. `X-Gaussian`
  6. `R2-Gaussian`
  7. `XRA-GS (Ours)` ← 最后一行
- 列 = 5 organs × 3 views + Avg = 16 列：
  - 多层表头：top row = `Chest | Head | Abdomen | Foot | Pancreas | Avg`
  - sub row = `2v | 3v | 4v | 2v | 3v | 4v | ...`
- 单位：PSNR2D ↑ (dB)
- 数值精度：保留 2 位小数（`27.43` 不写成 `27.430` 或 `27.4`）
- 高亮规则（[[VISUAL_STYLE]] §5）：
  - 每列 best：加粗 + 背景填色 `#FCE4E5`
  - 每列 2nd-best：下划线
  - 每列 3rd-best：italic（可选）
- Ours 行（最后一行）：行名加粗 + Crimson 下划线，无整行背景色（避免与单元格背景冲突）
- 表头中 `↑` 紧跟 metric 名（在 caption 第一句或表注里写一次即可，单元格不重复）
- 行间细横线 0.4pt 灰、组间 0.6pt 黑

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5：
  - 字号 8pt（表内）、9pt（表头）、表注 8pt
  - 不使用三线表外其他装饰；遵循 `booktabs` `\toprule \midrule \bottomrule`
- 参考论文锚点：
  - `参考论文/r2gs.pdf` **Tab. 1**（主对比表 organ × view × method 三层表头）
  - `参考论文/xgs.pdf` **Tab. 1**（best/2nd-best 高亮规则）
  - `参考论文/GR.pdf` **Tab. 1**（baseline 顺序与 Avg 列收尾）
- 不借鉴：把 Ours 整行高亮成大块红底（与单元格 best 高亮冲突）。

## 5. 数据来源/依赖
- 7 方法 × 5 organ × 3 view = 105 个 PSNR2D 数值，全部需要实验 agent 输出。
- 输出路径：`assets/data/tab_main_psnr2d.csv`（cols: method, organ, views, psnr2d）
- 数据缺口：与 [[req_fig_qual_main]] 同一批 baseline 复现实验共享，跟踪 `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md` 回包。
- 依赖：[[VISUAL_STYLE]]、[[req_tab_main_ssim2d]]（必须同表头同顺序）。

## 6. Caption 草稿骨架 (英文)
> **Quantitative comparison on PSNR2D (dB, higher is better).** We report PSNR2D on five organs under 2/3/4-view settings for all six baselines and XRA-GS. Best in each column is bolded with a light Crimson background; second best is underlined. XRA-GS achieves the highest average PSNR2D across all view counts, with the largest margin on the extreme 2-view setting.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 7 行方法顺序与 [[VISUAL_STYLE]] §4 完全一致，Ours 最后一行
- [ ] 5 organ 顺序：Chest, Head, Abdomen, Foot, Pancreas
- [ ] view 顺序：每 organ 内 2v / 3v / 4v
- [ ] 单位 dB ↑ 标注一次，不重复
- [ ] 数值精度统一 2 位小数
- [ ] 每列 best 加粗 + 背景；2nd-best 下划线
- [ ] Ours 行行名加粗 + Crimson 下划线
- [ ] 表格不是截图，是 `tab_main_psnr2d.tex` 由 `\input` 引入
- [ ] caption 独立读懂 setting + 高亮规则 + 关键观察
- [ ] 与 [[req_tab_main_ssim2d]] 表头结构对称

## 8. 反例 (Do NOT do this)
- Ours 放在第一行或表中间（顶会通行末行）。
- 用 `R2GS / X-Field* / Co-RGS` 等非标准缩写。
- best 用红字而不是加粗+背景（不符合 [[VISUAL_STYLE]] §5）。
- 数值精度混用（部分 2 位、部分 3 位）。
- 表格做成截图嵌图（违反 CLAUDE.md §3）。

## 9. 备注
- 当前 `assets/tables/tab_experiment_comparison_psnr.tex` 已有原型但 baseline 数 < 6，按本需求补齐。
- 建议用脚本 `assets/scripts/build_main_tables.py` 从 CSV 渲染 tex，避免人工 typo。
