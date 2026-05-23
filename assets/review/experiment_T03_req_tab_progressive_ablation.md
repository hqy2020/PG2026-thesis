# T03. Progressive Ablation — 渐进消融表

> 类型: table
> 状态: ready-to-draw
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 用一张表证明三模块叠加是单调有效：Baseline → +SPS → +SPS+GAP → Full XRA-GS。
- 回答审稿人："三个模块各自有用吗？还是只有一个真起作用？"
- 缺这张表，正文"三模块贡献相互补充"的陈述没有数字。

## 2. 排版位置建议
- 主文 §4.3 Ablation 第一张表，先于 [[req_fig_ablation_visual]]。
- 宽度：`\linewidth`（单栏）；若实在不够可改 `\textwidth`。
- 与 [[req_fig_ablation_visual]] 配套：表给数字，图给视觉。

## 3. 期望元素 (What must be in it)
- 行 = 4 配置（顺序锁定）：
  1. `Baseline` (vanilla 3D-GS)
  2. `+SPS`
  3. `+SPS+GAP`
  4. `Full XRA-GS` (+ ADM)
- 列 = 6：
  - `PSNR2D ↑ (2v)` / `PSNR2D ↑ (3v)` / `PSNR2D ↑ (4v)`
  - `SSIM2D ↑ (2v)` / `SSIM2D ↑ (3v)` / `SSIM2D ↑ (4v)`
- 全部在 5 organs 上做平均（与 [[req_tab_main_psnr2d]] 的 Avg 列一致）
- 数值精度：PSNR 2 位小数、SSIM 3 位小数
- 高亮规则：
  - 每列最优值（一定是 Full 行）：加粗 + Crimson 背景 `#FCE4E5`
  - 同列前后行差值标注（可选）：右侧加 `(+0.43)` 小字 7pt 灰色
- Full 行行名加粗 + Crimson 下划线

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5
- 参考论文锚点：
  - `参考论文/r2gs.pdf` **Tab. 3**（ablation 表渐进风格）
  - `参考论文/dngs.pdf` **Tab. 2**（行=模块组合、列=多 setting）
  - `参考论文/Corgs.pdf` **Tab. 4**（每行加增量标注）
- 不借鉴：DNGaussian 在 ablation 表里掺杂超参 sweep（混淆两个论证）。

## 5. 数据来源/依赖
- 4 配置 × 5 organ × 3 view × 2 metric = 120 个数值，但表里只显示对 organ 维度的 Avg（24 个数值）
- 输出路径：`assets/data/tab_progressive_ablation.csv`（cols: config, organ, views, psnr2d, ssim2d）
- 数据缺口：实验 agent 跑 3 个新 checkpoint（baseline / sps / sps_gap），Full 沿用主表数据。
- 依赖：[[req_tab_main_psnr2d]]、[[req_tab_main_ssim2d]]（Full 行数值必须与主表 Avg 一致）、[[req_fig_ablation_visual]]。

## 6. Caption 草稿骨架 (英文)
> **Progressive ablation on the three XRA-GS modules.** Each row adds one module on top of the previous configuration. SPS already gives a strong starting point under sparse views; GAP further suppresses redundant boundary Gaussians; ADM closes the remaining gap with position-dependent density modulation. The full configuration improves PSNR2D by [<P0>] dB and SSIM2D by [<P0>] over the baseline averaged across five organs.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 4 行配置顺序锁定：Baseline → +SPS → +SPS+GAP → Full
- [ ] 6 列：3 view × 2 metric，单位与方向标注完整
- [ ] PSNR 2 位小数、SSIM 3 位小数
- [ ] 每列最优值加粗 + Crimson 背景，必然落在 Full 行
- [ ] Full 行名加粗 + Crimson 下划线
- [ ] Full 行数值与 [[req_tab_main_psnr2d]] Avg 列完全一致
- [ ] caption 独立读懂"每加一个模块涨了多少"
- [ ] 表格不是截图，独立 `.tex` 文件 `\input` 引入

## 8. 反例 (Do NOT do this)
- 把 4 配置打乱顺序，或加 `+GAP only` / `+ADM only` 这类非渐进行（留给 [[req_tab_supp_single_module_ablation]]）。
- Full 行数值与主表 Avg 不一致（必须严格对齐）。
- 列只放 average，不分 2v/3v/4v（弱化跨 view 趋势）。
- 用 PSNR/SSIM 同一个精度（违反 [[VISUAL_STYLE]] §5）。

## 9. 备注
- 当前 `assets/tables/tab_ablation_progressive.tex` 已有原型，按本需求核对行列顺序与精度。
- 与 [[req_fig_ablation_visual]] 共用同一 dump 数据。
