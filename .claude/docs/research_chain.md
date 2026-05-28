# AI agent 辅助科研的链路完整性原则

后续使用 AI agent 辅助 `PG2026` 论文科研与写作时，默认目标不是把文字写得更顺，而是建立和检查完整的科研链路：数据链、证据链、逻辑链必须闭合，并且最终表达要突出 `XRA-GS` 的核心创新点。

## 执行要求

- **数据链**：所有实验数值、定量表、实验图和结论性描述都必须能追溯到 `assets/data/`、`assets/answer/` 或明确的实验 agent 输出；缺失数据按 [[experiment_agent]] 通过 `assets/ask/` 发起请求，不编造数据
- **证据链**：每个主文核心结论都要对应至少一种明确证据，优先是 quantitative table、qualitative figure、ablation、efficiency result、failure / limitation analysis
- **逻辑链**：写作与改稿默认检查 `problem → gap → method → evidence → limitation/discussion` 是否连贯，避免只堆结果或只润色局部句子
- **创新点**：所有摘要、引言贡献、方法概述、消融分析和结论总结都要回扣 `XRA-GS` 以及 `SPS / GAP / ADM`，避免把创新点写散、写弱或漂移成其他模块
- **Agent 协作**：需要实验、复核、风格对齐、图表设计或逻辑审查时可分工，但每次协作都要保留输入、输出、路径与未解决问题，确保后续可追踪
- **可见待办**：投稿推进路线图统一维护在 `assets/todolist/project_research_chain_todolist.md`；每次阶段性工作完成后必须同步更新，及时把已完成事项勾选为 `☑`，并记录当前版本、验收状态与下一步

## 单一事实源

后续协作时优先检查对象：
- 主稿源文件：`main.tex`
- 图片目录：`assets/fig/`
- 表格目录：`assets/tables/`
- 数据目录：`assets/data/`
- 脚本目录：`assets/scripts/`

如果 Markdown 讨论文档与 `main.tex` 冲突，以用户最新要求和 `main.tex` 最终落地结果为准，并及时同步说明文档。

## 注意事项

- **不要 `git log` 查找过期的文件**，否则会导致错误判断
