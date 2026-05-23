# `assets/review/` — XRA-GS 论文图表需求文档目录

本目录是 **PG2026** 全部主文 + 补充材料图表的**单一事实源**。任何画图、跑实验、出生成图的协作者（人或 Agent）在动手前都必须先读对应 md，画完后用 md 末尾的「验收指标」自检。

## 使用约定

- 每个图/表对应一份独立 md，文件名形如 `<section>_F0X_*.md` / `<section>_T0X_*.md`，其中 `<section>` 取自 `intro` / `related` / `method` / `experiment`（见根目录 `CLAUDE.md` §13）；F01–F13、T01–T07 编号继续作为 ID 索引
- 用户按 ID 顺序逐个处理，处理一份再开下一份
- md 之间用 `[[F0X_xxx]]` / `[[T0X_xxx]]` 风格交叉引用（保留 wiki-link 语法，不含 `.md` 扩展名）
- 涉及实验数值，一律写占位符 `<P0: from assets/data/...>`，不得编造
- 全局命名/配色/任务定义请回看 `PG2026-thesis/CLAUDE.md` §1 / §2 / §10，本目录里不重复
- 全局视觉规范（配色、字号、线宽、colormap）见 [VISUAL_STYLE.md](VISUAL_STYLE.md)，所有 md 都引用它
- 参考论文锚点路径相对仓库根 `/Users/openingcloud/Desktop/参考论文/`
- 修改任何 md 前先 `git pull` 并与 `main.tex` 现状对照，避免漂移

## 主文需求清单

| ID  | 文件                                                                           | 类型 | 状态           | 优先级 |
| --- | ------------------------------------------------------------------------------ | ---- | -------------- | ------ |
| F01 | [intro_F01_req_fig_teaser.md](intro_F01_req_fig_teaser.md)                                 | 图   | planned        | P0     |
| F02 | [intro_F02_req_fig_intro_compare.md](intro_F02_req_fig_intro_compare.md)                   | 图   | ready-to-draw  | P0     |
| F03 | [method_F03_req_fig_pipeline.md](method_F03_req_fig_pipeline.md)                           | 图   | ready-to-draw  | P0     |
| F04 | [method_F04_req_fig_module_sps.md](method_F04_req_fig_module_sps.md)                       | 图   | ready-to-draw  | P0     |
| F05 | [method_F05_req_fig_module_gap.md](method_F05_req_fig_module_gap.md)                       | 图   | ready-to-draw  | P0     |
| F06 | [method_F06_req_fig_module_adm.md](method_F06_req_fig_module_adm.md)                       | 图   | ready-to-draw  | P0     |
| F07 | [experiment_F07_req_fig_qual_main.md](experiment_F07_req_fig_qual_main.md)                 | 图   | data-pending   | P0     |
| F08 | [experiment_F08_req_fig_qual_detail_consistency.md](experiment_F08_req_fig_qual_detail_consistency.md) | 图 | data-pending   | P1     |
| F09 | [experiment_F09_req_fig_ablation_visual.md](experiment_F09_req_fig_ablation_visual.md)     | 图   | data-pending   | P0     |
| F10 | [experiment_F10_req_fig_spatial_distribution.md](experiment_F10_req_fig_spatial_distribution.md) | 图 | data-pending   | P1     |
| F11 | [experiment_F11_req_fig_hparam.md](experiment_F11_req_fig_hparam.md)                       | 图   | data-pending   | P1     |
| F12 | [experiment_F12_req_fig_failure.md](experiment_F12_req_fig_failure.md)                     | 图   | data-pending   | P2     |
| T01 | [experiment_T01_req_tab_main_psnr2d.md](experiment_T01_req_tab_main_psnr2d.md)             | 表   | data-pending   | P0     |
| T02 | [experiment_T02_req_tab_main_ssim2d.md](experiment_T02_req_tab_main_ssim2d.md)             | 表   | data-pending   | P0     |
| T03 | [experiment_T03_req_tab_progressive_ablation.md](experiment_T03_req_tab_progressive_ablation.md) | 表 | ready-to-draw  | P0     |
| T04 | [experiment_T04_req_tab_efficiency.md](experiment_T04_req_tab_efficiency.md)               | 表   | **BLOCKED**    | P0     |
| T05 | [experiment_T05_req_tab_init_and_viewcount.md](experiment_T05_req_tab_init_and_viewcount.md) | 表 | ready-to-draw  | P1     |

## 补充材料清单

| ID  | 文件                                                                                 | 类型 | 状态         | 优先级 |
| --- | ------------------------------------------------------------------------------------ | ---- | ------------ | ------ |
| F13 | [experiment_F13_req_fig_supp_training_curve.md](experiment_F13_req_fig_supp_training_curve.md)             | 图   | data-pending | P2     |
| T06 | [experiment_T06_req_tab_supp_per_organ_ssim2d.md](experiment_T06_req_tab_supp_per_organ_ssim2d.md)         | 表   | data-pending | P1     |
| T07 | [experiment_T07_req_tab_supp_single_module_ablation.md](experiment_T07_req_tab_supp_single_module_ablation.md) | 表 | data-pending | P1     |

## 当前 P0 阻塞项

| 文档     | 阻塞内容                                                              | 等待对象                                              |
| -------- | --------------------------------------------------------------------- | ----------------------------------------------------- |
| T04 效率 | Training time / #Gaussians / GPU memory / Render FPS（3-view setting） | `assets/ask/experiment_2026-05-21_efficiency-and-ssim.md` 的回包 |
| T02 SSIM2D 主表 | 6 个 baseline 完整 SSIM2D 矩阵                                   | 同上                                                  |
| F07/F09 定性图 | XRA-GS 与 6 baseline 在同一 organ/view 上的 2D 投影                | 同上                                                  |

## 状态字段

- `planned`：只有需求，没有数据也没有素材
- `data-pending`：素材生成或实验数据还没回，需求文档先冻结
- `ready-to-draw`：素材齐了，可以直接画或排版
- `BLOCKED`：有外部依赖未解，需求文档里已标注阻塞对象

## 反例（目录级别）

- 不要在本目录里堆 PSD/AI/Sketch 工程文件，工程文件放各画图工具自己的位置
- 不要把"实验结论"塞进 md，结论只写在 `main.tex`；md 只描述图表样子
- 不要把多张图/表混写到一个 md

## Paper Todo Snapshot 2026-05-21

按顶会审稿口径的六节解耦路线图（每节一份，独立可读，互不依赖；ID 与 [experiment_REVIEW_2026-05-21_section-issues.md](experiment_REVIEW_2026-05-21_section-issues.md) 同源）：

| Section | 文件 | 关键 P0 阻塞 |
| ------- | ---- | ----------- |
| Abstract | [intro_2026-05-21_abstract-todo.md](intro_2026-05-21_abstract-todo.md) | 等 T01/T02/T04 数据回填 |
| Introduction | [intro_2026-05-21_intro-todo.md](intro_2026-05-21_intro-todo.md) | F02 intro-compare 图缺失 + §13 命名迁移 |
| Related Work | [related_2026-05-21_related-todo.md](related_2026-05-21_related-todo.md) | 无 P0（文字阶段） |
| Method | [method_2026-05-21_method-todo.md](method_2026-05-21_method-todo.md) | F03–F06 四张方法图缺失 + §13 命名迁移 |
| Experiments | [experiment_2026-05-21_experiment-todo.md](experiment_2026-05-21_experiment-todo.md) | T04 efficiency 全空 + view-count avg 不一致 + 7 张图全缺 |
| Conclusion / Discussion | [experiment_2026-05-21_conclusion-todo.md](experiment_2026-05-21_conclusion-todo.md) | 等实验数据回填 |

使用约定：
- 每个 todo 文件统一骨架（当前状态 / 顶会目标 / 待解决问题表 / 验证清单 / 关联资产 / 执行顺序提示）
- 跨文件引用用 `[[name]]` wiki-link 语法
- 任务全部用 P0 / P1 / P2 标注，逐节攻克即可
- 综合视图保留在 `experiment_REVIEW_2026-05-21_section-issues.md`，作为单一汇总入口
