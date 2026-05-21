# CLAUDE.md

## Scope
`PG2026-thesis/` only.

## Core Rules
- Use `XRA-GS` for the method name and `Sparse Tomographic View Synthesis` for the task name.
- Keep `SPS -> GAP -> ADM` as the fixed module order.
- Keep figures and tables separate.
- Put figures in `assets/fig/`, tables in `assets/tables/`, numeric data in `assets/data/`, and Python figure scripts in `assets/scripts/`.
- Only use `assets/scripts/` when generating experiment figures from `assets/data/`; otherwise edit the `.tex` source directly.
- Write in English with a top-conference paper style.
- Keep figure and table captions self-contained and concise.

## Validation
After changing title, captions, or figure/table references, run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
