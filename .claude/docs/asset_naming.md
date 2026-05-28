# assets/ 命名前缀规范

`assets/` 下所有论文资产文件的**文件名开头**必须是以下四个章节关键词之一。

## 章节前缀

- `intro_`：teaser、引言用比较示意、引言用概念图
- `related_`：相关工作小节专属示意
- `method_`：pipeline、SPS / GAP / ADM 模块图、机制解释图
- `experiment_`：定量表、消融、定性对比、效率、视角扫描、超参图、失败案例、训练曲线、per-organ 数据等所有实验产物

## 命名形式

- `<section>_<原描述>.<ext>`
- 原有功能词（`fig_*`、`tab_*`、`req_*`）以及 F01 / T01 这类 ID 编号，保留在 section 前缀**之后**作为辅助标识
- 例：
  - `intro_F01_req_fig_teaser.md`
  - `method_fig_pipeline_image2_prompt.md`
  - `experiment_2026-05-21_efficiency-and-ssim.md`
  - `experiment_T04_req_tab_efficiency.md`

## 适用范围

`assets/ask/`、`assets/answer/`、`assets/data/`、`assets/fig/`、`assets/prompts/`、`assets/review/`、`assets/scripts/`、`assets/tables/` 下所有论文资产文件统一遵守。

## 豁免清单（工作流附件，不是章节资产）

- `assets/data/image2.md`（gpt-image-2 API 工具文档）
- `assets/review/README.md`（目录索引）
- `assets/review/VISUAL_STYLE.md`（全局视觉规范）
- 任何 `.gitkeep`、`.DS_Store` 等占位 / 系统文件

## ID 兼容性

- `assets/review/` 内部 md 之间的 wiki-link `[[F0X_xxx]]` / `[[T0X_xxx]]` 视为 ID 别名，可继续保留旧编号不带章节前缀；此类引用方式不强制改写
- 但 `README.md` 中的 markdown 链接（`[label](F0X_xxx.md)` 形式）必须指向真实文件名，需同步带上章节前缀
