# F06. ADM — Adaptive Density Modulation 模块图

> 类型: figure
> 状态: ready-to-draw
> 优先级: P0
> 主文/补充: main

## 1. 目的 (Why)
- 把 ADM 的"K-Planes 提取空间上下文 → 双头 MLP 输出位置依赖密度 offset 与 confidence gate"机制可视化。
- 回答审稿人："为什么不用 vanilla MLP？K-Planes 起到什么作用？confidence gate 又是干嘛的？"
- 没有这张图，ADM 会被误以为是 deformable density 的简单 wrapper。

## 2. 排版位置建议
- 主文 §3.4 ADM 子节。
- 宽度：`\linewidth`（单栏）。
- 与 [[req_fig_module_sps]]、[[req_fig_module_gap]] 风格三胞胎对齐。

## 3. 期望元素 (What must be in it)
- 三 panel 横排：
  - **(a) Spatial Context (K-Planes)**：一个 organ 体积的 3 个轴对齐切面 (axial / coronal / sagittal) 缩略，每个切面叠加一张 K-Planes 解码出的 feature map (`viridis`)，强调"位置不同特征不同"。
  - **(b) Mechanism**：一个 schematic flow：
    - 输入 `x ∈ ℝ³` → `K-Planes(x) ∈ ℝ^F` → 双头 MLP
    - 头 1：`Δσ(x)`（density offset，输出走橙色调制曲线）
    - 头 2：`g(x) ∈ [0,1]`（confidence gate，输出走青色 sigmoid 曲线）
    - 最终 `σ_final = σ_base + g(x) · Δσ(x)`
  - **(c) Effect**：同一 slice 上 baseline density vs ADM-modulated density 的差值图 (`inferno`)，标注 ADM 在哪些区域加密、哪些区域降密。
- panel 下方 sub-caption 8pt 英文，单行
- (b) 中所有箭头黑色实线，按 [[VISUAL_STYLE]] §3

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3：
  - ADM 主色：Warm Orange `#E07B39`（与 pipeline 块同色）
  - K-Planes feature map：`viridis`
  - density offset 调制曲线：橙色 (ADM 色)
  - confidence gate sigmoid 曲线：青色 GAP 色？ 不可——避免撞 GAP 语义，改用 Slate Blue `#5B7C99` 作为"门控"信号色
  - 差值图：`inferno`（VISUAL_STYLE §2 error 类）
- 参考论文锚点：
  - `参考论文/DGR.pdf` 中后段（discretized density refinement 的 schematic 风格）
  - `参考论文/dngs.pdf` **Fig. 4**（depth-normalization MLP head 的 双头分支 风格）
  - `参考论文/XField.pdf` 物理→特征→输出的 layer 块图
- 不借鉴：XField 的密集物理符号；DNGaussian 的彩色 depth panel。

## 5. 数据来源/依赖
- (a) K-Planes feature map：训练完成的 XRA-GS checkpoint 必须能 dump 任意位置的 K-Planes feature；建议固定 Chest 3-view checkpoint。
- (b) schematic：纯手绘，TikZ / Illustrator。
- (c) density 差值图：dump 一对密度场 `σ_base(x)` 与 `σ_final(x)` 体素采样。
- 数据缺口：
  - `assets/data/kplanes_feat_chest_3v.npy`（axial/coronal/sagittal × feature channel）
  - `assets/data/density_base_chest_3v.npy`
  - `assets/data/density_adm_chest_3v.npy`
- 依赖：[[req_fig_module_sps]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Adaptive Density Modulation (ADM).** A K-Planes encoder extracts continuous spatial context at every Gaussian location; a dual-head MLP predicts a position-dependent density offset Δσ(x) and a confidence gate g(x) ∈ [0,1] that controls how much of the offset is applied. ADM concentrates additional density where the attenuation support requires fine detail and damps modulation where evidence is uncertain.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] (a) 三切面 K-Planes 特征非平凡，可见空间变化 (不是纯色)
- [ ] (b) schematic 同时画出两个 head + 最终融合公式 `σ_final = σ_base + g·Δσ`
- [ ] (c) 差值图与 [[req_fig_intro_compare]] 共享同一 vmax (全篇 error map 统一)
- [ ] 没有让 confidence gate 用 GAP 青色 (语义冲突)
- [ ] ADM 块色与 [[req_fig_pipeline]] 一致
- [ ] caption 单独读懂"输入 → 两个 head → 怎么融合 → 想达到什么效果"
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 把 ADM 画成单 head MLP（丢失 confidence gate 创新点）。
- 用 K-Planes 三个 plane 同色，看不出空间变化。
- (c) 用与 intro_compare 不同 vmax 的 error map。
- 公式只贴 `Δσ = MLP(...)` 而不写融合形式。

## 9. 备注
- 当前 `assets/fig/fig_method_adm.png` 与 `_image2.png` 是早期生成图，缺真实 K-Planes feature 与差值图，按本需求重画。
- 与 `assets/prompts/method_fig_adm_image2_prompt.md` 的关键差异：本需求强制双 head 可见 + 真实 dump。
