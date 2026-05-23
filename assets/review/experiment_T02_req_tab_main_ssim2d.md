# T02. Main SSIM2D — 主对比表 (SSIM2D)

> 类型: table
> 状态: data-pending
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 与 [[req_tab_main_psnr2d]] 构成主对比的"双指标"，SSIM2D 是 X-ray 投影任务里比 PSNR 更能反映结构保真度的指标。
- 回答审稿人："SSIM 上你也赢吗？还是只赢 PSNR？"
- 缺这张表，主对比只能给出一个指标的优势，容易被指为"挑指标"。

## 2. 排版位置建议
- 主文 §4.2 Main Results 第二张表，紧跟 [[req_tab_main_psnr2d]]。
- 宽度：`\textwidth`（跨双栏，table*）。
- 与 [[req_tab_main_psnr2d]] 上下排版，表头、列宽完全对齐。

## 3. 期望元素 (What must be in it)
- 行 / 列结构与 [[req_tab_main_psnr2d]] 完全相同：
  - 7 行方法（顺序锁定，Ours 末行）
  - 16 列（5 organ × 3 view + Avg）
- 单位：SSIM2D ↑（无量纲）
- 数值精度：保留 3 位小数（`0.872` 不写成 `0.87` 或 `0.8723`）
- 高亮规则与 [[req_tab_main_psnr2d]] 完全一致（best 加粗+背景、2nd-best 下划线）
- Ours 行行名加粗 + Crimson 下划线
- 表头 `↑` 与 PSNR2D 表同位置

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5（与 [[req_tab_main_psnr2d]] 一致）
- 参考论文锚点：
  - `参考论文/r2gs.pdf` **Tab. 1**（SSIM 子表）
  - `参考论文/xgs.pdf` **Tab. 2**（SSIM2D 3 位小数风格）
  - `参考论文/dngs.pdf` **Tab. 1**（双指标表分页对齐）
- 不借鉴：在 SSIM 表里改用 PSNR 表不同的高亮颜色（造成审稿人混淆）。

## 5. 数据来源/依赖
- 7 方法 × 5 organ × 3 view = 105 个 SSIM2D 数值
- 输出路径：`assets/data/tab_main_ssim2d.csv`（cols: method, organ, views, ssim2d）
- 数据缺口：当前 `assets/tables/tab_experiment_comparison_ssim.tex` 只覆盖 3 方法，缺 6 baseline 完整数据。**P0 阻塞**，跟踪 `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md` 回包。
- 依赖：[[VISUAL_STYLE]]、[[req_tab_main_psnr2d]]。

## 6. Caption 草稿骨架 (英文)
> **Quantitative comparison on SSIM2D (higher is better).** Same setting as Table [[req_tab_main_psnr2d]]. XRA-GS attains the highest SSIM2D on all view counts and on every organ except for [<P0: organ where 2nd>], where it remains within [<P0: gap>] of the best. The gap widens under the 2-view setting, consistent with the qualitative gain in [[req_fig_qual_main]].

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 表头与 [[req_tab_main_psnr2d]] 完全对称
- [ ] 7 方法行顺序与 [[VISUAL_STYLE]] §4 一致
- [ ] 5 organ 顺序：Chest, Head, Abdomen, Foot, Pancreas
- [ ] 每 organ 内 2v / 3v / 4v
- [ ] 单位 SSIM2D ↑ 标注
- [ ] 数值精度统一 3 位小数
- [ ] 每列 best 加粗 + Crimson 背景；2nd-best 下划线
- [ ] Ours 行名加粗 + Crimson 下划线
- [ ] 表格不是截图，是 `tab_main_ssim2d.tex` 由 `\input` 引入
- [ ] caption 独立读懂，与 [[req_tab_main_psnr2d]] 配套

## 8. 反例 (Do NOT do this)
- SSIM 表只列 average 列、省略 organ×view 细节（弱化结构保真证据）。
- SSIM 与 PSNR 表用不同的方法顺序。
- 数值精度与 PSNR 表混用（PSNR 2 位、SSIM 应 3 位，但内部都要统一）。
- 把 SSIM 表合并进 PSNR 表"省版面"（两个独立指标，独立呈现）。

## 9. 备注
- 当前 `assets/tables/tab_experiment_comparison_ssim.tex` 是 average-only 占位，按本需求扩到全矩阵。
- 与 [[req_tab_supp_per_organ_ssim2d]] 关系：本表是主文 Avg+矩阵，supplementary T06 给更细的 per-view fine-grained 拆分（按需）。
