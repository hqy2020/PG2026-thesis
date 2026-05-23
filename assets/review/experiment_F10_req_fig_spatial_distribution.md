# F10. Spatial Distribution — 高斯空间分布演化

> 类型: figure
> 状态: data-pending
> 优先级: P1
> 主文/补充: main

## 1. 目的 (Why)
- 用一张图把"SPS 放在哪里 → GAP 砍掉哪里 → ADM 又在哪里调密度"这一条 3D 空间故事讲清楚。
- 回答审稿人："你说三个模块分别在改空间分布，能看到吗？" — 给点云演化 + attenuation profile 双轨证据。
- 缺这张图，三模块只能各自靠模块图说话，没有"它们叠起来对整体分布的累积作用"。

## 2. 排版位置建议
- 主文 §3.5 / §4.4 之间（取决于章节最终命名），作为方法整体性收尾或消融小节的视觉收尾。
- 宽度：`\textwidth`（跨双栏）。
- 与 [[req_fig_ablation_visual]] 接力：前者讲"投影变化"，本图讲"空间分布变化"。

## 3. 期望元素 (What must be in it)
- 4 个 panel 横排（顺序锁定）：
  1. `Uniform Init`（baseline 起点，灰色点云）
  2. `+SPS`（按衰减支撑重采，紫色点云）
  3. `+SPS+GAP`（剪除边界冗余，青色高亮被剪点）
  4. `Full XRA-GS`（ADM 调制后，橙色高亮加密区）
- 4 panel 必须用同一 organ × 同一视角 × 同一 axes scale × 同一相机
- 每 panel 下方 8pt 英文 sub-caption：`"<stage> · #G = <P0>"`，注明该阶段高斯数量
- 顶部叠加一条公用的 **attenuation profile 曲线**（沿同一扫描线，灰底）：
  - 用 [[VISUAL_STYLE]] §2 `magma` 半透明背景表示 GT attenuation
  - 4 条曲线叠加：对应每个 stage 在同一扫描线上的密度积分
  - x 轴 = 扫描线位置；y 轴 = 累积密度（归一化）
  - 4 条曲线颜色：Neutral / SPS Purple / GAP Teal / ADM Orange（按角色色板）
- panel 标号 `(a)(b)(c)(d)` 9pt 加粗，左上角

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3：
  - 各阶段点云颜色与 pipeline 模块色一一对应（见 [[VISUAL_STYLE]] §1）
  - attenuation 背景：`magma`
  - 点云透明度统一 0.5，size 统一 4 pt²
- 参考论文锚点：
  - `参考论文/xgs.pdf` **Fig. 6**（point cloud evolution 横排，4 个 stage 同视角）
  - `参考论文/LB.pdf` **Fig. 7**（分层点云上色 + 顶部 profile 曲线叠加）
  - `参考论文/r2gs.pdf` **Fig. 2** 末段（剪枝前后点云对照）
- 不借鉴：X-Gaussian 的彩色背景；LB 的多色 axes。

## 5. 数据来源/依赖
- 4 个 stage × 1 organ (Chest 3-view) × 完整 3D 高斯坐标 dump
- 输出路径：
  - `assets/data/spatial_dist/{stage}_xyz.npy`（cols: x,y,z）
  - `assets/data/spatial_dist/profile_chest_3v.csv`（cols: pos, gt_att, baseline_acc, sps_acc, sps_gap_acc, full_acc）
- 数据缺口：与 [[req_fig_module_gap]]、[[req_fig_module_sps]] 的 dump 可以共用一份 checkpoint，但要求多 stage 都保存坐标。
- 依赖：[[req_fig_module_sps]]、[[req_fig_module_gap]]、[[req_fig_module_adm]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Evolution of the Gaussian spatial distribution.** From left to right: uniform initialization, after SPS, after SPS+GAP, and the final XRA-GS distribution. The top profile shows the cumulative density along a horizontal scan line against the GT X-ray attenuation; XRA-GS concentrates Gaussians along the attenuation support while remaining lean elsewhere, matching the GT profile more closely than any intermediate stage.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 4 panel 同 organ、同视角、同 axes、同相机
- [ ] 每 panel 颜色对应 [[VISUAL_STYLE]] §1 角色色板
- [ ] 顶部 profile 曲线 4 条颜色与下方 4 panel 一一对照
- [ ] panel 标号 (a)(b)(c)(d) 顺序与文字顺序一致
- [ ] 每 panel 注出 `#G` 数量（来自实验 dump，不编造）
- [ ] attenuation 背景 colormap = `magma`
- [ ] caption 单独读懂"4 个阶段在空间上发生了什么"
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 4 panel 用不同视角，让读者无法对位（必须同视角）。
- profile 用 4 种不同 colormap 而不是 4 条不同颜色线。
- 在 panel 上同时画散点 + 椭球填充（在 CT 切片背景上不可读）。
- 顶部 profile 与下方 panel 标号顺序错位（左到右必须一致）。

## 9. 备注
- 当前 `assets/fig/` 无对应文件，纯新增。
- 推荐与 [[req_fig_module_gap]] 共用一份 dump pipeline。
