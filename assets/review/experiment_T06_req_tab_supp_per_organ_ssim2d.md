# T06. Supp Per-organ SSIM2D — 补充材料：器官级 SSIM2D 细矩阵

> 类型: table
> 状态: data-pending
> 优先级: P1
> 主文/补充: supplementary

## 1. 目的 (Why)
- 主文 [[req_tab_main_ssim2d]] 已经给出 organ×view 矩阵，但若版面紧张需要把主文降级为 Avg-only，本表承接完整 5 organ × 3 view × 7 方法 的细矩阵到补充材料。
- 回答审稿人："在每个 organ 上分别长什么样？有哪些 organ 你不占优？"
- 缺这张表，补充材料对结构保真度的支撑不完整。

## 2. 排版位置建议
- 补充材料 §B Quantitative details。
- 宽度：`\textwidth`（跨双栏，table*）。
- 与 [[req_tab_supp_single_module_ablation]] 同章。

## 3. 期望元素 (What must be in it)
- 行 = 7 方法（顺序与 [[req_tab_main_ssim2d]] 一致，Ours 末行）
- 列 = 5 organ × 3 view = 15 列 + Avg = 16 列（与主表完全对称）
- 单位：SSIM2D ↑
- 数值精度：3 位小数
- 高亮规则：每列 best 加粗 + Crimson 背景；2nd-best 下划线
- Ours 行行名加粗 + Crimson 下划线
- 如果主文 [[req_tab_main_ssim2d]] 已经给完整矩阵，本表退化为补充材料的"备份/per-seed std"扩展版：每数值再加一个 ±std 小字（如 `0.872 ± 0.004`，7pt 灰色），要求实验 agent 跑 3 个 seed。

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5
- 参考论文锚点：
  - `参考论文/r2gs.pdf` **Supp Tab. S1**（补充材料 organ × view × method full matrix）
  - `参考论文/xgs.pdf` **Supp Tab. S2**（带 ±std 的 supp 表）
- 不借鉴：把 ±std 放在 LaTeX `\substack{}` 里弄成两层堆叠（缩放后不可读），用 inline 7pt 灰色就行。

## 5. 数据来源/依赖
- 与 [[req_tab_main_ssim2d]] 同一批 baseline 复现，但额外要求 3 seed 跑 std
- 输出路径：`assets/data/tab_supp_per_organ_ssim2d.csv`（cols: method, organ, views, ssim2d_mean, ssim2d_std）
- 数据缺口：主表数据 + std 数据，后者新增。
- 依赖：[[req_tab_main_ssim2d]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Per-organ SSIM2D with standard deviation over three seeds.** Same setting as the main table; numbers are mean ± std. XRA-GS keeps the best mean SSIM2D on [<P0: count>] out of 15 (organ, view) cells, and the small std confirms that the improvement is not driven by initialization variance.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 7 行 / 16 列结构与 [[req_tab_main_ssim2d]] 完全对称
- [ ] 数值精度 3 位小数，±std 同精度 7pt 灰
- [ ] 每列 best 加粗 + Crimson 背景；2nd-best 下划线
- [ ] Ours 行行名加粗 + Crimson 下划线
- [ ] caption 明确写"3 seed mean±std"，不写"我们做了多次实验"
- [ ] 单元格未到位时用 `--` 占位
- [ ] 表格不是截图，独立 `.tex` 文件 `\input` 引入

## 8. 反例 (Do NOT do this)
- 用与主表不同的方法顺序（破坏交叉对照）。
- ±std 用 1 位小数（与 mean 精度不一致）。
- 在补充表里隐去 Avg 列（必须保留，便于与主表对照）。
- 把 std 用百分号表示（`±0.4%`），与 SSIM 量纲不一致。

## 9. 备注
- 当前 `assets/tables/` 无对应文件，纯新增。
- 若实验 agent 暂时无法跑 3 seed，可先出 mean-only 版本，待补 std。
