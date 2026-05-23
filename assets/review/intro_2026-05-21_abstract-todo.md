# Abstract Todo（2026-05-21 snapshot）

> 单节路线图。综合视图见 [[experiment_REVIEW_2026-05-21_section-issues]] §1。
> ID 沿用 `A*` 系列，便于跨文档交叉引用。

## 1. 当前状态

- **主稿位置**：`main.tex` L54–56（`\begin{abstract}` 区块）。
- **文字**：英文摘要完整，骨架 `problem → gap → core insight → method → strongest evidence` 清晰；无中文残留、无 `--` 占位、无 `TODO`。
- **术语 / 设定一致性**：
  - 方法名 `XRA-GS`、任务名 `Sparse Tomographic View Synthesis`：✅
  - 三模块 `SPS / GAP / ADM` 顺序：✅
  - 主指标 `PSNR2D` / `SSIM2D`：✅
  - 测试设定 `5 organs × {2,3,4} views`：✅
- **依赖资产**：本节无图无表；strongest-evidence 一句依赖 T01 (PSNR2D 主表) / T02 (SSIM2D 主表) / T04 (efficiency) 数据。

## 2. 顶会标准目标

- G-A1：摘要骨架保持稳定，不重写。
- G-A2：strongest-evidence 数值与主表完全一致，可被审稿人逐字核对。
- G-A3：句式紧凑、被动语态克制、避免 conversational tone；具备英文顶会会议级阅读流畅度。

## 3. 待解决问题

| ID  | 优先级 | 类型     | 问题                                                                                                            | 定位          | 依赖                                                          | 备注                                  |
| --- | ------ | -------- | --------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------- | ------------------------------------- |
| A1  | P1     | 数据回填 | strongest-evidence 中 PSNR2D gain 幅度需用最终主表数值验证                                                       | `main.tex` L54–56 | [[experiment_T01_req_tab_main_psnr2d]]                        | 等 T01 数据回包后核对                 |
| A2  | P1     | 数据回填 | "leading or tied SSIM2D" 措辞需用最终 SSIM2D 主表验证；4-view 下若为 tie 必须显式承认                            | `main.tex` L54–56 | [[experiment_T02_req_tab_main_ssim2d]]                        | 等 T02 数据回包后核对                 |
| A3  | P2     | 润色     | 投稿前做一次英文母语级润色，去除冗余过渡词、对齐顶会语气                                                          | `main.tex` L54–56 | —                                                             | 在所有数据 / 图都到位后再做           |
| A4  | P2     | 一致性   | 摘要末段 method 概述句的 wording 与 intro contributions 列表如有重叠，需轻微差异化                                  | `main.tex` L54–56 + L58–84 | [[intro_2026-05-21_intro-todo]]                       | 与 intro 一起改                       |

## 4. 验证清单

- [ ] `latexmk` 仍能编译（abstract 区块无 tex 语法错误）。
- [ ] 摘要中 PSNR2D / SSIM2D 数值与 `tab_experiment_comparison.tex` / `tab_experiment_comparison_ssim.tex` 完全一致。
- [ ] 5 organs × {2,3,4} views 设定被显式提及。
- [ ] 三模块名称按 `SPS → GAP → ADM` 顺序出现。
- [ ] 与 intro 的 contributions 列表无 wording 重叠（不重复同一句话）。

## 5. 关联资产

- **主稿**：`main.tex` L54–56。
- **依赖表**：
  - `assets/tables/tab_experiment_comparison.tex`（PSNR2D 主表）
  - `assets/tables/tab_experiment_comparison_ssim.tex`（SSIM2D 主表）
  - `assets/tables/tab_experiment_efficiency.tex`（效率表，目前全 `--`）
- **依赖需求文档**：
  - [[experiment_T01_req_tab_main_psnr2d]]
  - [[experiment_T02_req_tab_main_ssim2d]]
  - [[experiment_T04_req_tab_efficiency]]
- **ask / answer**：
  - `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md`（已发出，待回复）
- **综合视图**：[[experiment_REVIEW_2026-05-21_section-issues]] §1。

## 6. 执行顺序提示

`A3`、`A4` 必须放在所有 P0/P1 任务之后；`A1`、`A2` 在 T01/T02 数据到位的当天就完成核对，避免数据漂移。
