# Gaussians 术语统一规范

本稿件全文默认使用 `Gaussians`，**不再使用** `primitives`。后续生成或润色文字时若再出现 `primitive(s)`，必须自动替换。

## 默认替换规则

- `Gaussian primitives` → `Gaussians`
- 单独的 `primitives` 当指代「3DGS 的几何/辐射单元」时 → `Gaussians`
- `primitive` 作定语（如 `primitive count`, `primitive position`）→ `Gaussian`（`Gaussian count`, `Gaussian position`）
- `per-primitive` → `per-Gaussian`

## 兼容词组（继续使用，不需要改）

- `radiative Gaussians`
- `Gaussian set`
- `Gaussian evolution rule`
- `per-Gaussian density`
- `Gaussian count`
- `anisotropic Gaussians`

## 例外保留 `primitives` 的情形

- 真正与图形学一般几何图元（triangles / quads / meshes / NURBS surfaces 等）并列讨论时
- 引用其他文献原文术语时（直接引述、不改写其措辞）
- bibtex 字段、URL、作者命名空间，一律不改

## 验证手段

- 大改稿后跑 `grep -n -i "primitive" main.tex`，结果应清零或只剩通用图形学并列语义
- 若全文检索到新增的 `primitive`，按上述规则归一后再 commit
- 同步检查 `assets/prompts/`、`assets/ask/`、`assets/review/`、`assets/tables/*.tex`、`assets/scripts/*` 中是否漂出 `primitive` 字样

## 适用范围

abstract / intro / related / method / experiments / conclusion / figure caption / table caption / 贡献点列表 / algorithm 伪代码 / 补充材料。**不动** bibtex、原文献作者命名、外部 API 字段。
