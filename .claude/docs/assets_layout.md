# 资产目录硬规则：图片、表格、数据、脚本分离

后续统一执行「图片、表格分离」原则，不再混成笼统的「图表」。

## 目录分工硬规则

- 图片资产 → `assets/fig/`
- 表格资产 → `assets/tables/`
- 数值结果、实验原始数据、可视化中间文件 → `assets/data/`
- 仅在需要基于 `assets/data/` 生成实验图或对数据做可重复检查时，才在 `assets/scripts/` 下写 Python；其他正文、图注、表注、版式修改一律直接改 `tex`
- 图片以 figure 处理，用 `\includegraphics`
- 表格以 table 处理，优先用独立 `tab_*.tex` 文件并由 `\input{assets/tables/...}` 引入
- 不要把表格截图塞进图片，除非用户明确要求做可视化 figure
- 不要把多张定性图和定量表揉成混合版式凑「图表」
- 需要其他 Agent 或人工介入的待办放 `assets/review/`

## 写作规则

- 讨论实验重构时，单独列「图片计划」和「表格计划」，不要混写
- 主文中先明确该证据属于 qualitative figure 还是 quantitative table，再决定放图还是放表
- caption 中不要把 figure/table 混称为「图表」

具体绘图分工见 [[figure_design]]，资产命名前缀规范见 [[asset_naming]]。
