# T07. Supp Single-module Ablation — 补充材料：单模块消融表

> 类型: table
> 状态: data-pending
> 优先级: P1
> 主文/补充: supplementary

## 1. 目的 (Why)
- 主文 [[req_tab_progressive_ablation]] 走的是渐进消融（+SPS → +SPS+GAP → Full），无法回答"单独一个模块能不能 work"。
- 回答审稿人："只加 GAP 不加 SPS 行吗？只加 ADM 行吗？模块之间有依赖关系吗？"
- 缺这张表，三模块的"必要性"只有渐进证据，没有独立证据。

## 2. 排版位置建议
- 补充材料 §B Quantitative details，紧跟 [[req_tab_supp_per_organ_ssim2d]]。
- 宽度：`\linewidth`（单栏）。

## 3. 期望元素 (What must be in it)
- 行 = 5 配置（顺序锁定）：
  1. `Baseline`
  2. `+SPS only`
  3. `+GAP only`
  4. `+ADM only`
  5. `Full XRA-GS` (SPS+GAP+ADM)
- 列 = 6：
  - `PSNR2D ↑ (2v)` / `(3v)` / `(4v)`
  - `SSIM2D ↑ (2v)` / `(3v)` / `(4v)`
- 全部 5 organ 平均
- 数值精度：PSNR 2 位小数、SSIM 3 位小数
- 高亮规则：
  - 每列 best：必然落在 Full 行 → 加粗 + Crimson 背景
  - 每列 2nd-best：下划线
- Full 行行名加粗 + Crimson 下划线
- 表内可加一栏右侧 "Notes" 列（可选）：标注模块间是否依赖（如 "GAP only" 失败原因是缺好初始化）

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §3 / §5
- 参考论文锚点：
  - `参考论文/dngs.pdf` **Tab. 3**（单模块独立行 + Full 行收尾）
  - `参考论文/Corgs.pdf` **Tab. 4**（带 Notes 的补充消融）
- 不借鉴：把单模块消融和渐进消融混到一张表（混淆论证）。

## 5. 数据来源/依赖
- 5 配置 × 5 organ × 3 view × 2 metric = 150 数值，平均后 30 数值
- 输出路径：`assets/data/tab_supp_single_module_ablation.csv`（cols: config, organ, views, psnr2d, ssim2d）
- 数据缺口：实验 agent 需要新跑 `+GAP only` 与 `+ADM only` 两份消融（`+SPS only` 复用 [[req_tab_progressive_ablation]]）
- 依赖：[[req_tab_progressive_ablation]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Single-module ablation on XRA-GS.** Adding any single module on top of the baseline improves quality, but GAP and ADM in isolation deliver smaller gains than SPS — confirming that the attenuation-aligned initialization is what unlocks the subsequent structure-control and density-modulation behavior. The full configuration substantially outperforms all single-module variants.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 5 行配置顺序锁定：Baseline → +SPS only → +GAP only → +ADM only → Full
- [ ] 6 列：3 view × 2 metric
- [ ] PSNR 2 位小数、SSIM 3 位小数
- [ ] 每列 best 落在 Full 行，加粗 + Crimson 背景
- [ ] Full 行行名加粗 + Crimson 下划线
- [ ] `+SPS only` 行数值与 [[req_tab_progressive_ablation]] 的 `+SPS` 行一致
- [ ] caption 解释"为何 GAP/ADM 单独效果不如 SPS 单独"
- [ ] 不出现中文、不出现 emoji
- [ ] 表格不是截图，独立 `.tex` 文件 `\input` 引入

## 8. 反例 (Do NOT do this)
- 把 5 行顺序打乱，把 Full 放第一行。
- 与 [[req_tab_progressive_ablation]] 行名不一致（用 "GAP only" vs "+GAP only" 等小写不一致）。
- 写 caption "GAP 单独不 work" — 太绝对；应写"smaller gains than SPS"。
- 把单模块消融搬到主文（信息冗余，主文渐进消融已经足够）。

## 9. 备注
- 当前 `assets/tables/` 无对应文件，纯新增。
- 若实验 agent 排期紧，本表可降至 P2 暂缓，但补充材料 §B 应保留 placeholder 章节。
