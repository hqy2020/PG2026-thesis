# 实验 Agent 协作协议

论文有一个独立的实验 agent 运行在 GPU 服务器上，负责训练、推理、指标统计与可视化生成。当稿件需要实验数据或可视化图但当前 `assets/data/`、`assets/fig/` 缺失时，通过以下协议协作。

## 沟通方式

- 发起请求：在 `assets/ask/` 创建 markdown，文件名 `YYYY-MM-DD_<brief-task>.md`（章节前缀见 [[asset_naming]]）
- 接收回复：实验 agent 完成后在 `assets/answer/` 放对应结果文件与数据，文件名与 ask 对应
- 实验 agent 仓库：`https://github.com/hqy2020/PG2026`

## 请求文件规范（assets/ask/*.md）

```markdown
## 需求描述
<!-- 一句话说清楚要什么 -->

## 输入
- 用到的设定（dataset / view count / method）
- 已有的中间产物路径（如果有的话）

## 期望输出
- 具体文件列表，含格式和路径
- 例如：
  - `assets/data/tab_efficiency_3view.csv`（training time, #Gaussians, GPU memory for X-Gaussian, R2-Gaussian, RAttAGS）
  - `assets/fig/fig_experiment_gaussian_count.png`（Gaussian count 变化曲线）

## 优先级
<!-- P0（阻塞投稿）/ P1（重要但不阻塞）/ P2（锦上添花）-->

## 截止时间
<!-- 如果有 -->
```

## 回复文件规范（assets/answer/*）

- 文件名与 ask 请求对应，例如 `2026-05-21_efficiency-table.md`
- 包含：完成的输出文件路径列表 + 每个文件简要说明
- 若部分需求无法完成，说明原因和替代方案

## 当前待补实验数据（P0）

- `tab_experiment_efficiency` 中的 training time、#Gaussians、GPU memory 数据（3-view setting）
- per-organ SSIM2D 数据（用于补充 SSIM2D average-only 表或未来扩展）
- progressive ablation 的 per-organ 细分数据（用于 supplementary material）

## 使用原则

- 表格中出现 `--` 占位符或 caption 标注 "to be completed" → 自动触发向实验 agent 发起请求
- 不要编造实验数据；数值必须来自实验 agent 真实产出
- 请求发出后先继续处理其他可独立完成的修改，等 answer 到位再填表并编译验证
- `ask` 文件名遵循 [[asset_naming]] 章节前缀规范，写作 `<section>_YYYY-MM-DD_<brief-task>.md`
- 不要直接给一个混杂的「图表优化建议」大列表
