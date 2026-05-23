# F09. Ablation Visual — 渐进消融定性可视化

> 类型: figure
> 状态: data-pending
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 用一张图把 [[req_tab_progressive_ablation]] 的数字趋势翻译成视觉证据：从 Baseline 到 Full XRA-GS，"加一个模块多回收一点什么"。
- 回答审稿人："你的渐进消融在数字上提升了 0.x，到底视觉上看得出来吗？"
- 缺这张图，主表的 progressive ablation 只能用 PSNR/SSIM 数字说话，看不出每个模块解决的"具体伪影"是哪一类。

## 2. 排版位置建议
- 主文 §4.3 Ablation 子节，紧接 [[req_tab_progressive_ablation]] 之后。
- 宽度：`\textwidth`（跨双栏）。
- 与 [[req_tab_progressive_ablation]] 共用同一 setting；这张图给视觉、表给数值。

## 3. 期望元素 (What must be in it)
- 行 = 1 个 case：`Chest 3-view`（与 [[req_tab_progressive_ablation]] 主行同步）
- 列 = 6（顺序锁定）：
  1. `GT`
  2. `Baseline`（vanilla 3D-GS，无 SPS / GAP / ADM）
  3. `+SPS`（仅加初始化）
  4. `+SPS+GAP`（加结构控制）
  5. `Full XRA-GS`（再加 ADM）
  6. `Error: |Full − GT|`（error overlay，单独成列以便对照）
- 每个 cell 是同一新视角的 2D X-ray 投影；error overlay 用 `inferno`（按 [[VISUAL_STYLE]] §2）
- 列首方法名 9pt 加粗；`Full XRA-GS` 列方法名加粗 + Crimson Red 下划线
- 行下方留一条 8pt 行内描述（英文）：`"PSNR2D: <P0> → <P0> → <P0> → <P0>"`（数字按 [[req_tab_progressive_ablation]] 同步）
- 每个非 GT 列底部贴一行 ↑Δ 标注：相对前一列的 SSIM2D 增量（保留 3 位小数）
- 全图右下角加一个红色 zoom-in 框，集中放大 Baseline 与 Full 在同一边界处的差异

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§5：
  - 投影渲染：`gray` colormap，全行共享 vmin/vmax
  - error map：`inferno`，与 [[req_fig_intro_compare]]、[[req_fig_module_adm]] 共享 vmax
  - Ours 列高亮 + 红色 zoom-in box
- 参考论文锚点：
  - `参考论文/dngs.pdf` **Fig. 8**（progressive ablation 多列示意 + error 列收尾）
  - `参考论文/Corgs.pdf` **Fig. 5**（baseline → +module → full 三段式视觉）
  - `参考论文/r2gs.pdf` **Fig. 7**（行下方贴指标增量的版式）
- 不借鉴：DNGaussian 的 depth panel；CoR-GS 的椭球填充。

## 5. 数据来源/依赖
- 4 个 checkpoint × 1 organ (Chest) × 1 view setting (3-view) × 1 novel view = 4 张投影 + 1 张 GT + 1 张 error map = 6 cell
- 输出路径：`assets/data/ablation_visual_chest_3v/{stage}.png`，stage ∈ {gt, baseline, sps, sps_gap, full, error_full}
- 数据缺口：实验 agent 需要 dump 4 个渐进 checkpoint 的同一新视角渲染（已在 [[req_tab_progressive_ablation]] 数据请求里覆盖一部分，本图额外要求"图像"输出而非仅数字）。
- 依赖：[[req_tab_progressive_ablation]]、[[VISUAL_STYLE]]、[[req_fig_intro_compare]]（error map vmax 同步）。

## 6. Caption 草稿骨架 (英文)
> **Progressive ablation, qualitative view.** Starting from a vanilla Gaussian Splatting baseline, we incrementally add SPS, GAP and ADM under a 3-view Chest setting. SPS recovers global attenuation support, GAP suppresses boundary over-densification, and ADM sharpens fine anatomical detail; the rightmost error map confirms that residual energy concentrates only in low-signal soft-tissue regions.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 6 列顺序固定：GT → Baseline → +SPS → +SPS+GAP → Full XRA-GS → Error
- [ ] 所有非 error 列共享同一 vmin/vmax
- [ ] error 列 colormap 与 [[req_fig_intro_compare]] 共享 vmax
- [ ] 每列 ↑Δ SSIM2D 数值与 [[req_tab_progressive_ablation]] 一致
- [ ] `Full XRA-GS` 列高亮 + 列首加粗红下划线
- [ ] zoom-in 框颜色 Crimson Red，与下方放大图边框一致
- [ ] caption 单独读懂"每加一个模块解决什么"
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 不同列用不同 organ 或不同视角（破坏可比性）。
- 在 Full 与 Baseline 之间额外插入"+GAP only"或"+ADM only"列（单模块消融留给 [[req_tab_supp_single_module_ablation]]，主图只走渐进路径）。
- error 列与投影列共享同一 colormap。
- 在 Caption 里写中文术语或写 "提升了一些"，必须给具体 ↑Δ。

## 9. 备注
- 当前 `assets/fig/fig_experiment_ablation.png` 仅 3 列且缺 error，按本需求重画到 6 列。
- 与 [[req_tab_progressive_ablation]] 同一份 dump 数据共享，避免实验 agent 重跑。
