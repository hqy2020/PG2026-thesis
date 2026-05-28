# PG2026 / XRA-GS — 协作约定（主索引）

> 本文件是**索引 + 高频硬结论**，详细规则在 `.claude/docs/` 中。每对话生效。
> 主文件硬上限 **< 200 行**（见 §16 meta 工作流）。

---

## 1. 方法名 / 任务名 / 标题 → [.claude/docs/naming.md](.claude/docs/naming.md)

- 方法名：`XRA-GS`
- 任务名：`Sparse Tomographic View Synthesis`（`Sparse` 在前）
- 标题：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`
- 物理关键词默认 `attenuation`；`X-ray Attenuation-XXX Gaussian Splatting` 默认 `XXX = Aligned`
- CT 缩写定义统一 `Computed tomography (CT) is ...`，**不写** `X-ray computed tomography (CT)` 同位语

## 2. 三个创新模块 SPS / GAP / ADM → [.claude/docs/modules.md](.claude/docs/modules.md)

- `SPS`（初始化）/ `GAP`（结构控制）/ `ADM`（细化）
- 顺序固定 `SPS → GAP → ADM`；消融命名 `w/o SPS / w/o GAP / w/o ADM / full XRA-GS`
- `XRA-GS` 是总方法名，三模块是其内部创新点，不互相替代

## 3. 资产分离 → [.claude/docs/assets_layout.md](.claude/docs/assets_layout.md)

- 图 → `assets/fig/`，表 → `assets/tables/`，数据 → `assets/data/`，脚本 → `assets/scripts/`
- 表格独立 `tab_*.tex` 由 `\input{...}` 引入；不要把表格截图塞进图
- 待办或外部协作产物 → `assets/review/`

## 4. 不要 `git log` 查找过期文件

直接读 `main.tex` 与 `assets/` 当前内容；`git log` 会引入过期判断。

## 5. 单一事实源

主稿：`main.tex`；图：`assets/fig/`；表：`assets/tables/`；数据：`assets/data/`；脚本：`assets/scripts/`。
md 讨论文档与 `main.tex` 冲突时以 `main.tex` 最终落地结果为准。

## 6. 编译验证

改了标题、图注、表注、figure/table 引用，默认跑：

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## 7. Git / GitHub 工作流 → [.claude/docs/git_workflow.md](.claude/docs/git_workflow.md)

- 每完成一组逻辑完整的改动 → `commit + push origin main`（远端 `hqy2020/PG2026-thesis`），不 push 不算交付
- commit 范围：`git status` 看清；明确加文件，不用 `git add -A`；`main N.synctex(busy)` 等临时文件不入库
- commit message 用 HEREDOC；尾部加 `Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>`
- 禁止：`push --force` / `reset --hard` / `commit --amend` / `--no-verify`（除非用户显式要求）
- 历史未提交改动与本轮无明显关联时，先和用户确认 commit 范围

## 8. 顶会论文写作 → [.claude/docs/paper_writing.md](.claude/docs/paper_writing.md)

- 全文英文；摘要骨架 `problem → gap → core insight → method → strongest evidence`
- 引言故事线收束到 `Sparse Tomographic View Synthesis`
- 学术语气，不写博客式铺垫；图/表独立可读
- 「按论文标准改」「更学术一点」默认解释为「按英文顶会论文要求处理」

## 9. 出图 → [.claude/docs/image2_workflow.md](.claude/docs/image2_workflow.md) + [.claude/docs/figure_design.md](.claude/docs/figure_design.md)

- 默认通道：`gpt-image-2` skill（基于 codex CLI 复用 ChatGPT 订阅）
- prompt 文件 `assets/prompts/<section>_<figname>_image2_prompt.md`，唯一 marker `## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)`
- backup 规则：**首次**覆盖移旧图为 `_backup.png`；已存在 backup 时**不重建**
- 比较类 figure 默认 2 行 × N 列网格，**严禁图内 (a)(b)(c) panel 编号**
- 文字烘焙白名单：短公式、模块短名、轴标短词；其他全部由 LaTeX 在外面加

## 10. 实验协议 → [.claude/docs/experiment_protocol.md](.claude/docs/experiment_protocol.md)

- 固定 6 个 baseline：`CoR-GS / DNGaussian / FSGS / X-Gaussian / R2-Gaussian / X-Field`
- 主指标：`SSIM2D` 和 `PSNR2D`
- 测试设定：`5 organs × {2, 3, 4} views`

## 11. 实验 agent 协作 → [.claude/docs/experiment_agent.md](.claude/docs/experiment_agent.md)

- 请求：`assets/ask/<section>_YYYY-MM-DD_<task>.md`；回复：`assets/answer/...`
- 实验 agent 仓库：`https://github.com/hqy2020/PG2026`
- 不编造实验数据；表中 `--` 占位符触发 ask 请求

## 12. 资产命名前缀 → [.claude/docs/asset_naming.md](.claude/docs/asset_naming.md)

- 章节前缀：`intro_` / `related_` / `method_` / `experiment_`
- 形式：`<section>_<原描述>.<ext>`；F0X/T0X 等 ID 保留在前缀之后
- 豁免：`assets/data/image2.md`、`assets/review/README.md`、`assets/review/VISUAL_STYLE.md`、`.gitkeep` 等

## 13. 科研链路完整性 → [.claude/docs/research_chain.md](.claude/docs/research_chain.md)

- 数据链 / 证据链 / 逻辑链必须闭合；所有结论回扣 `XRA-GS` 与 `SPS / GAP / ADM`
- 投稿路线图：`assets/todolist/project_research_chain_todolist.md`

## 14. 物理论证骨架 → [.claude/docs/physics_argument.md](.claude/docs/physics_argument.md)

- intro 第 2 段：只出现 `α-compositing` 与 `Beer–Lambert law` 的**名字**，公式落到 method preliminaries
- surface clustering = **transmittance-induced concentration**（必引 `max1995optical`、`guedon2024sugar`、`huang20242dgs`）
- X-ray 全 path 平权 = `linear, order-independent line integral`（必引 `kak2001principles`）
- intro 第 3 段必须有「问题不在 gradient-driven densification 本身」免责句
- 全文统一 `attenuation-aligned`，**不用** `attenuation-aware`
- 禁用：`fortunate coupling` / `gradient-driven densification is fundamentally misaligned` / `replace the densification mechanism`

## 15. Gaussians 术语 → [.claude/docs/terminology.md](.claude/docs/terminology.md)

- 全文用 `Gaussians`，**不用** `primitives`
- `primitive count` → `Gaussian count`；`per-primitive` → `per-Gaussian`
- 验证：`grep -n -i "primitive" main.tex` 应清零或只剩通用图形学并列语义
- 例外：与 triangles/quads/meshes 并列、引述外文献原文、bibtex 字段

## 16. 修改后沉淀经验工作流（meta-rule） → [.claude/docs/meta_workflow.md](.claude/docs/meta_workflow.md)

每次用户提完一组修改请求并完成改动后，**必须**执行：
1. 按类型归档本轮反馈（命名 / 物理论证 / 写作 / 绘图 / 实验设定 / 工作流 / 其他）
2. 判定哪些是**可复用硬规则**，哪些是一次性问题（不沉淀）
3. 把可复用规则追加到对应 `.claude/docs/<topic>.md`；找不到主题就新建 md 并在本文件加一行索引
4. `wc -l CLAUDE.md` 验证 < 200；超出则拆出更多内容到子 md
5. 不沉淀：一次性 typo、单次拼写、临时数据修正
6. 最终调用 `commit + push origin main`（见 §7），不 push 不算交付
