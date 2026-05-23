# F07. Qualitative Main — 主定性对比 (5 organs × 7 methods)

> 类型: figure
> 状态: data-pending
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 主文最重的视觉证据：在 5 个器官、固定 view setting 下，XRA-GS 对比 6 个 baseline 的 2D 投影渲染差异。
- 回答审稿人："数值我看到了，可视化呢？XRA-GS 视觉上真的更好吗？"
- 缺这张图，主表 PSNR2D/SSIM2D 的领先只有数字、没有眼睛能看到的证据。

## 2. 排版位置建议
- 主文 §4.2 Main Results 第一张图，紧接 [[req_tab_main_psnr2d]] 与 [[req_tab_main_ssim2d]] 引用之后。
- 宽度：`\textwidth`（跨双栏）。
- 与 [[req_fig_qual_detail_consistency]] 接力（本图给"全局对比"，后者给"细节 zoom + 跨视角"）。

## 3. 期望元素 (What must be in it)
- 行 = 5 organs：Chest, Head, Abdomen, Foot, Pancreas（顺序锁定）
- 列 = 8 个 (按 [[VISUAL_STYLE]] §4 baseline 顺序)：
  1. `GT`
  2. `CoR-GS`
  3. `DNGaussian`
  4. `FSGS`
  5. `X-Field`
  6. `X-Gaussian`
  7. `R2-Gaussian`
  8. `XRA-GS (Ours)`
- 全图 view setting 固定为 **2-view**（最稀疏、最难，最能拉开差距）；4-view 与 3-view 留给 [[req_fig_qual_detail_consistency]] 与 supplementary
- 每个 cell 是同一个新视角下的 2D X-ray 投影渲染（CT slice 也可，但本图主推投影，与任务名 `Sparse Tomographic View Synthesis` 对齐）
- 每行右侧 1 列放对应行 organ 的 error map (`inferno`, 与 XRA-GS 列对比)；可选行，若版面紧张则放进 supplementary
- 列首方法名 9pt 加粗；Ours 列方法名加粗 + Crimson Red 下划线 (2pt)，整列背景给极淡 Crimson `#FCE4E5` (5%) 高亮
- 行首 organ 名 9pt 加粗，竖排或横排均可
- 每行右下角加一个红色 zoom-in 框，下方对应放大裁剪（裁剪同样按 8 列展开还是只在 Ours 列展开见 [[req_fig_qual_detail_consistency]] 决定；本图只标主图红框，不展开放大）

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§5：
  - 投影渲染 / GT：`gray` colormap，全行共享 vmin/vmax (organ 内归一化)
  - error map：`inferno`，全图共享 vmax
  - Ours 列高亮 + 红色 zoom-in box (VISUAL_STYLE §5)
  - 列首方法名严格按 §4 顺序与拼写
- 参考论文锚点：
  - `参考论文/r2gs.pdf` **Fig. 3**（rows × cols 网格主对比 + Ours 末列加亮）
  - `参考论文/xgs.pdf` **Fig. 5**（多 organ 行排版与列首方法名风格）
  - `参考论文/GR.pdf` **Fig. 4-5**（sparse-view CT 主定性图列宽与 zoom 框）
- 不借鉴：R2-Gaussian 的灰底装饰；X-Gaussian 的彩色背景画框。

## 5. 数据来源/依赖
- 7 个方法 × 5 organ × 1 view setting (2-view) × 1 novel view angle = 35 张投影渲染 PNG
- 5 organ × 1 GT novel view = 5 张
- 每个 organ × 1 error map (Ours - GT) = 5 张
- 全部需要实验 agent 输出 `assets/data/qual_main/{method}/{organ}_2v_view{angle}.png` 与 `{organ}_2v_gt.png`
- 数据缺口：`assets/ask/experiment_2026-05-21_efficiency-and-ssim.md` 已经请求 baseline 复现，但还未交付。需要追加确认这一批投影 dump 在请求范围内。
- 依赖：[[req_tab_main_psnr2d]]、[[req_tab_main_ssim2d]]、[[VISUAL_STYLE]]、[[req_fig_qual_detail_consistency]]。

## 6. Caption 草稿骨架 (英文)
> **Qualitative comparison on five organs under a 2-view setting.** Each row is one organ; columns show GT, six baselines, and XRA-GS (Ours, last column). Across all organs, XRA-GS reproduces global X-ray attenuation more faithfully and suppresses boundary streaks and over-bright accumulations that are visible in the gradient-driven baselines. Red boxes mark regions enlarged in Figure [[req_fig_qual_detail_consistency]].

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 8 列顺序与 [[VISUAL_STYLE]] §4 完全一致，GT 在首列，Ours 在末列
- [ ] 5 行 organ 顺序与 CLAUDE.md §10 一致：Chest, Head, Abdomen, Foot, Pancreas
- [ ] 每行全部 8 个 cell 共享同一新视角与同一归一化范围
- [ ] error map (若保留) 与 [[req_fig_intro_compare]] 共享 vmax
- [ ] Ours 列高亮 + 列首加粗红下划线
- [ ] 红框 zoom-in 标记位置与 [[req_fig_qual_detail_consistency]] 的放大图严格对应
- [ ] caption 单独读懂 setting + 对比对象 + 关键观察 + zoom 转引
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 把 Ours 列放在中间或左边（顶会通行右末列）。
- 不同 organ 用不同的 view angle（破坏可比性）。
- error map 与 GT 共享 colormap (一定要用 inferno 分开)。
- 在主图里直接展开 zoom-in 放大裁剪占据半张图 (放大留给 [[req_fig_qual_detail_consistency]])。
- 列首方法名出现 `R2GS / R2`、`XField`、`Cor-GS` 等非标准变体。

## 9. 备注
- 当前 `assets/fig/fig_experiment_qual_main.png` 只覆盖 4 个 baseline (FSGS / X-Gaussian / R2-Gaussian / XRA-GS) — 必须扩到 6 baseline。
- 强烈建议出图用 Python 脚本拼版：`assets/scripts/build_qual_main.py` 读 `assets/data/qual_main/` 目录后按行/列输出 PDF，避免人工 PSD 出错。
