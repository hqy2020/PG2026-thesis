# 补实验方法与最新 SOTA 跟进

更新时间：2026-05-11

## 当前论文主协议

- 主任务：static sparse-view CT novel view synthesis（NVS）
- 当前设定：5 个器官，2/3/4-view
- 主评价：投影质量为主（PSNR，SSIM），并辅以效率与 cross-view consistency
- 当前最公平的 CT/X-ray direct baseline：X-Gaussian、R²-Gaussian

## 2025 之后最值得关注的方法

### 第一优先级：X-Field（NeurIPS 2025 Spotlight）

定位：目前和本文最接近的最新工作，同时覆盖 X-ray NVS 与 CT reconstruction。

为什么重要：
- 它不是继续沿用标准 Gaussian，而是改成带材料衰减系数的 3D ellipsoid。
- 它在论文里同时声称对 X-ray NVS 和 CT reconstruction 都优于先前方法。
- 如果 reviewer 问“2025 以后有没有更强方法”，它是最难绕开的名字。

为什么现在不能直接并表：
- 公开结果主要基于 10-view 训练。
- 数据组成与本文 2/3/4-view、5 organs 的主协议不完全一致。
- 如果直接拿对方论文数字并进主表，会有协议不公平的问题。

建议动作：
- 如果只补一个最新 baseline，优先重跑 X-Field。
- 最小重跑范围先放在 3-view，再决定是否扩到 2/4-view。

### 第二优先级：GR-Gaussian（ICLR 2026 submission）

定位：CT-specific 的最新 radiative GS 路线，强调图结构先验与梯度修正。

为什么值得看：
- 它和本文一样，核心矛盾不是“继续补点”，而是“怎样避免错误 densification 带来的 artifact”。
- 它的叙事和本文关于结构冗余、边界误导梯度的主线存在直接对话关系。

为什么不建议先于 X-Field：
- 目前更偏 reconstruction 叙事。
- 还是较新的公开版本，稳定复现风险通常高于已正式发表方法。

建议动作：
- 如果时间有限，不必先补。
- 如果 X-Field 跑通且还有精力，可在 3-view representative subset 上补 GR-Gaussian。

### 只放 related work / discussion，不建议直接进主表的方法

#### DGR（ICCV 2025）
- 更偏 direct volume reconstruction。
- 表示与评价层都偏体重建，不是当前 static NVS 主协议的直接比较对象。

#### X²-Gaussian（ICCV 2025）
- 面向 continuous-time 4D CT。
- 和当前 static 3D sparse-view NVS 不同任务，不建议拉进主表。

#### CvG-Diff（MICCAI 2025）
- 更广义的 sparse-view CT reconstruction SOTA。
- 可以在 discussion 里提，但不建议与当前 GS-based NVS 主表直接混比。

## 建议补实验：按优先级排序

## A. 最小必补包（推荐）

### A1. X-Field 同协议重跑（3-view）

目标：回答“有没有 2025 之后的更强方法”。

最小协议：
- 与本文完全相同的数据划分
- 相同 3-view 设置
- 相同测试视角与指标统计方式
- 报告 PSNR / SSIM / FPS / training time / final primitive count

建议输出：
- 主结果表补一列 X-Field
- 主定性图或 supplementary qualitative 中补 2 到 3 个器官案例
- 若 primitive 数量与速度差异明显，补效率表或气泡图

为什么先做 3-view：
- 3-view 是本文最核心工作点。
- 也是当前方法增益最稳定、最有说服力的设定。
- 能以最小代价回答 reviewer 最关心的问题。

### A2. X-Field 的公平性说明

如果只来得及跑 3-view，需要在文中明确写：
- X-Field 是 2025 年后最接近的同期方法。
- 由于其原文公开协议与本文不完全一致，本文仅在核心 3-view 设定下做 same-protocol rerun。
- 2/4-view 的完整补充可放 supplement 或 future work。

### A3. 一组与 X-Field 的局部定性对比

建议选：
- Chest：看高对比边界与背景噪声
- Head：看骨性边界与 cross-view consistency
- Pancreas 或 Foot：看难例表现与 failure boundary

观察重点：
- 边界外溢
- 条纹/针状 artifact
- 低对比区域是否被边界高密度簇吞噬
- 不同 target views 下结构是否稳定

## B. 可选增强包（有余力再做）

### B1. X-Field 全设定扩展到 2/3/4-view

价值：
- 如果 X-Field 在 3-view 上很强，扩到 2/4-view 能更完整回答“你的方法到底在哪个稀疏区间最占优”。
- 如果 X-Field 在 2-view 或 4-view 并不占优，反而更能强化本文“中等稀疏区间最受益”的结论。

### B2. GR-Gaussian 的 representative 3-view subset

建议最小范围：
- 只跑 3-view
- 只跑 2 到 3 个代表器官
- 只做 PSNR / SSIM + 1 张定性图

目的：
- 不是扩主表，而是防止 reviewer 说“2025 之后还有 CT-specific GS 你没看”。

### B3. reconstruction-oriented supplementary evidence

如果 reviewer 持续把任务往 CT reconstruction 上拉，可以补：
- CT slice consistency figure
- FDK / R²-Gaussian / SPAGS / GT 的 slice-level 对比
- 代表 case 的 error map

这个补充的定位应该是：
- 证明本文虽然主任务是 NVS，但结果与体结构恢复一致
- 不要把全文主任务改写成 direct reconstruction

## 不建议扩的方向

- 不建议为了“看起来更全”把 DGR、X²-Gaussian、CvG-Diff 全拉进主表。
- 不建议现在扩到 4D CT、cone-beam 新协议或新数据集。
- 不建议把任务表述从 NVS 改成 direct reconstruction，只为了迎合某些新 baseline。

## 推荐执行顺序

1. 先检查 X-Field 是否能在当前数据与 scanner setting 下稳定复现。
2. 跑 X-Field 的 same-protocol 3-view 全器官结果。
3. 补一组与 X-Field 的主定性或 supplementary 定性对比。
4. 根据结果决定是否继续扩到 2/4-view。
5. 如果还有时间，再考虑 GR-Gaussian 的 representative 3-view subset。

## 一句话结论

如果这轮只补一件和“最新 SOTA”最相关的实验，那就补：

**X-Field 在本文 same-protocol 3-view 设定下的重跑结果。**

这组实验的信息密度最高，也最能正面回答 reviewer 对“2025 年后最新方法”的追问。
