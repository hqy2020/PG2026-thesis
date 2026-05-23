# F13. Supp Training Curve — 训练曲线 (补充材料)

> 类型: figure
> 状态: data-pending
> 优先级: P2
> 主文/补充: supplementary

## 1. 目的 (Why)
- 给补充材料一张训练动力学图，证明 SPS 提供更好起点、GAP 不引入震荡、ADM 进入后稳定收敛。
- 回答审稿人："你们方法是否训练更稳定？三个模块进入时是否有副作用？"
- 缺这张图，效率表（[[req_tab_efficiency]]）只能给出"总训练时间"，看不出收敛动力学。

## 2. 排版位置建议
- 补充材料 §A.x（训练细节节）。
- 宽度：`\linewidth`（单栏）。
- 与 [[req_tab_efficiency]] 配套，给"为什么训练更快"提供视觉解释。

## 3. 期望元素 (What must be in it)
- 1 个 panel：
  - x 轴：训练 iteration（log scale 或线性，由 sweep 决定，统一一种）
  - y 轴：测试集 PSNR2D ↑（在 Chest 3-view 上）
  - 3 条曲线：
    1. `Baseline (vanilla 3D-GS)`：Slate Blue 实线
    2. `+SPS`：SPS Purple 实线
    3. `Full XRA-GS`：Crimson Red 实线（粗 1.5 pt 强调）
  - 2 条垂直虚线（黑色 1.0 pt dashed）：
    - `GAP first triggered`：标注 GAP 第一次剪枝迭代
    - `ADM enters`：标注 ADM warmup 结束、开始调制
  - 右上角图例（[[VISUAL_STYLE]] §3）

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§3：
  - 3 条曲线颜色按模块/方法角色色板
  - 虚线类型严格按 §3 (3pt-2pt dashed)
- 参考论文锚点：
  - `参考论文/GR.pdf` **Fig. 7**（训练曲线 + 阶段标记）
  - `参考论文/Corgs.pdf` **Fig. 4**（iteration 轴 + 多方法对比 + 模块进入标线）
  - `参考论文/r2gs.pdf` **Fig. 8**（log-scale x 轴训练曲线）
- 不借鉴：CoR-GS 的填充阴影方差带（与本图无方差数据，避免假装方差）。

## 5. 数据来源/依赖
- 3 个 checkpoint × Chest 3-view × N 个 logging 步 × PSNR2D = N×3 数值
- 输出路径：`assets/data/training_curve_chest_3v.csv`（cols: iter, baseline, sps, full）
- 数据缺口：实验 agent 需要保留训练过程中每 K 步的 test-set PSNR2D（而非只保终值），以及记录 GAP/ADM 触发 iteration。
- 依赖：[[req_tab_efficiency]]、[[req_tab_progressive_ablation]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Training dynamics on Chest 3-view.** SPS gives the model a meaningful starting PSNR that the baseline only reaches after thousands of iterations. When GAP first triggers (vertical dashed line), the curve dips briefly but recovers without instability; when ADM enters, XRA-GS gains an additional margin and converges to the highest plateau.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 3 条曲线颜色与角色色板一致（Baseline = Slate Blue, SPS = Purple, Full = Crimson）
- [ ] 2 条垂直虚线分别标注 GAP / ADM 触发位置
- [ ] x 轴单位与 iter scale 类型明确标注
- [ ] y 轴单位 PSNR2D (dB) ↑
- [ ] 图例位置 [[VISUAL_STYLE]] §3 右上角
- [ ] caption 描述"模块触发后曲线发生了什么"
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 在曲线下加假方差带（无实验依据）。
- 用不同 organ 的 3 条曲线（要 1 organ × 3 方法，不要 3 organ × 1 方法混杂）。
- 不标 GAP/ADM 触发位置，让读者无法理解动力学拐点。
- 把图放主文（应放补充材料，主文版面给定性与表格）。

## 9. 备注
- 当前 `assets/fig/` 无对应文件，纯新增。
- 若实验 agent 已经把 log dump 出来，可直接用 `assets/scripts/plot_training_curve.py` 复用现成接口。
