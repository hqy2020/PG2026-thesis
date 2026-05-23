# F12. Failure — XRA-GS 失败案例分析

> 类型: figure
> 状态: data-pending
> 优先级: P2
> 主文/补充: main

## 1. 目的 (Why)
- 主动暴露 XRA-GS 在极端 sparse-view 与高难 organ 下仍未解决的问题，证明论文 limitation 节有据可依。
- 回答审稿人："你哪些 case 没赢？为什么？"
- 缺这张图，limitation 节只能空谈，顶会审稿易判为 "no failure analysis"。

## 2. 排版位置建议
- 主文 §5 Discussion / Limitation 节末尾。
- 宽度：`\textwidth`（跨双栏）。
- 与 [[req_fig_qual_main]]、[[req_fig_ablation_visual]] 视觉风格保持一致。

## 3. 期望元素 (What must be in it)
- 行 = 2 个 case：
  - `Foot 2-view`（解剖结构细、视角极少）
  - `Pancreas 2-view`（软组织对比度低）
- 列 = 4：
  1. `GT`
  2. `R2-Gaussian`（最强 baseline，作对照）
  3. `XRA-GS (Ours)`
  4. `Error: |Ours − GT|`
- 每个 case 在 `Ours` 与 `R2-Gaussian` 列上加红框 zoom-in，标记失败区域
- 每行右侧贴一段 ≤ 25 词的英文 failure 描述（8pt）：
  - Foot：例如 "thin metatarsal boundaries collapse under 2-view constraint"
  - Pancreas：例如 "low-contrast soft tissue under-attenuated, residual streak"
- 行首 organ 名 9pt 加粗

## 4. 视觉效果与参考锚点
- 严格遵守 [[VISUAL_STYLE]] §1-§5：
  - 投影渲染 `gray`、error map `inferno`，vmax 与 [[req_fig_intro_compare]] 共享
  - Ours 列方法名加粗 + Crimson 下划线
  - 红框 zoom-in Crimson 1.5 pt
- 参考论文锚点：
  - `参考论文/r2gs.pdf` **Fig. 9** / limitation panel（最强 baseline 与 Ours 并列暴露失败）
  - `参考论文/FSGS.pdf` 末页 limitation 行排版
- 不借鉴：在失败图里加炫酷视觉装饰、做"自我表扬"。

## 5. 数据来源/依赖
- 2 case × 4 列 = 8 个 cell + 2 行 error map = 10 张图
- 输出路径：`assets/data/failure/{organ}_2v_{column}.png`
- 数据缺口：与 [[req_fig_qual_main]] 共用渲染 dump，但额外要求"在 Ours 失败最明显的视角"上重采，可能需要额外 1-2 个 view angle 的 sweep。
- 依赖：[[req_fig_qual_main]]、[[VISUAL_STYLE]]。

## 6. Caption 草稿骨架 (英文)
> **Failure cases.** XRA-GS still struggles on thin bony structures under a 2-view Foot setting and on low-contrast soft tissue under a 2-view Pancreas setting. Despite outperforming the strongest baseline (R2-Gaussian) globally, residual streaks remain inside the red boxes; the error map highlights where additional priors (e.g., anatomical segmentation) would help.

## 7. 验收指标 (Pass/Fail checklist)
- [ ] 2 行 organ 固定为 Foot 2-view + Pancreas 2-view
- [ ] 4 列顺序：GT / R2-Gaussian / Ours / Error
- [ ] 红框位置严格对应失败区域，不出现"无意义红框"
- [ ] error map 与 [[req_fig_intro_compare]] 共享 vmax
- [ ] failure 描述 ≤ 25 词，纯英文，不写"未解决"，写具体观察
- [ ] caption 不写"我们方法也能完美解决"这类自夸话
- [ ] 不出现中文、不出现 emoji

## 8. 反例 (Do NOT do this)
- 用 4-view 或 3-view 当 failure case（不是真正的极端 setting）。
- 把 Ours 列的失败用文字否认（"虽然有 streak 但不影响结论"——避免）。
- 不放 error map，让审稿人没法定位失败位置。
- 选 Chest / Head 这类 baseline 都做得好的 organ 来"伪造" failure。

## 9. 备注
- 当前 `assets/fig/` 无对应文件，纯新增。
- 若版面紧张，可将本图移至 supplementary，但主文 limitation 节仍要 `\ref{}` 引用。
