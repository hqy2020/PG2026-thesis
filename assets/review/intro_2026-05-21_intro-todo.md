# Introduction Todo（2026-05-21 snapshot）

> 单节路线图。综合视图见 [[experiment_REVIEW_2026-05-21_section-issues]] §2。
> ID 沿用 `I*` 系列。

## 1. 当前状态

- **主稿位置**：`main.tex` L58–84（`\section{Introduction}`）。
- **文字**：英文 intro 完整；故事线 `Novel View Synthesis → Sparse View Synthesis → Tomographic Novel View Synthesis → Sparse Tomographic View Synthesis` 按 CLAUDE.md §8 桥接路径展开；三贡献顺序 `SPS → GAP → ADM` 与 method 一致；对比方法名 `FSGS / CoR-GS / DNGaussian / X-Gaussian / R²-Gaussian / X-Field` 全部使用标准写法。
- **图片**：
  - 引用：`\includegraphics{assets/fig/fig_intro_compare.png}`（`main.tex` L73 附近）。
  - 磁盘：**物理缺失**。文件名前缀仍是旧格式 `fig_intro_*`，应迁移到 §13 规范 `intro_fig_*`。
- **表格 / 数据**：本节无表。
- **需求文档**：
  - [[intro_F01_req_fig_teaser]]（teaser，状态 planned，是否进主文待定）。
  - [[intro_F02_req_fig_intro_compare]]（intro 对比示意图，状态 ready-to-draw）。

## 2. 顶会标准目标

- G-I1：首页一图秒懂 —— intro 对比示意图能让读者在不读正文的情况下抓到"why this paper"。
- G-I2：三贡献一一对应 SPS / GAP / ADM，且与 abstract 用词不重叠（避免冗余）。
- G-I3：末段明确实验设定（5 organs × {2,3,4} views, SSIM2D + PSNR2D）并预告 strongest evidence。
- G-I4：英文表达不出现 conversational tone、教程口吻、营销式标题。

## 3. 待解决问题

| ID  | 优先级 | 类型     | 问题                                                                                       | 定位                          | 依赖 / 工作流                                  | 备注                                       |
| --- | ------ | -------- | ------------------------------------------------------------------------------------------ | ----------------------------- | ---------------------------------------------- | ------------------------------------------ |
| I1  | P0     | 图缺失   | `fig_intro_compare.png` 物理缺失，主稿引用解析为空                                          | `main.tex` L73 附近            | image2 API（§12 概念图工作流） / [[intro_F02_req_fig_intro_compare]] | 缺图导致编译警告 + 排版破洞                |
| I2  | P0     | 命名规范 | 旧文件名 `fig_intro_compare.png` 不符合 §13 前缀；新图落地为 `intro_fig_compare.png`，tex 引用同步改 | `main.tex` L73 附近            | I1 完成后同步                                  | 命名一致后才能 latexmk 通过                |
| I3  | P2     | 范围决策 | F01 teaser 图是否进主文需定夺（受 PG 页数限制）                                              | —                             | [[intro_F01_req_fig_teaser]]                   | 若不进主文则降级到 supplementary           |
| I4  | P1     | 文字     | 三贡献描述与 abstract 是否存在 wording 重叠，需做差异化                                      | `main.tex` L58–84 + L54–56     | [[intro_2026-05-21_abstract-todo]]             | 与 abstract 同步处理                       |
| I5  | P1     | 文字     | 末段是否清晰交代 5 organs × {2,3,4} views 设定 + 主指标 + strongest evidence 锚点            | `main.tex` L58–84 末段         | —                                              | 让审稿人第一页就知道实验规模               |
| I6  | P2     | 润色     | 校对：避免 `we can see`, `let's`, `it turns out` 等 conversational 表述                       | `main.tex` L58–84              | —                                              | 投稿前批量润色                             |
| I7  | P2     | 引用     | 引言中提到的方法（FSGS / CoR-GS / DNGaussian / X-Gaussian / R²-Gaussian / X-Field）需保证全部有 `\cite{}` | `main.tex` L58–84             | `references.bib`                               | 引用键已核实存在，但要检查每处都加 `\cite` |

## 4. 验证清单

- [ ] `latexmk` 编译无 `Missing image` / `LaTeX Warning: Reference ... undefined`。
- [ ] `assets/fig/intro_fig_compare.png` 存在且 `main.tex` 中 `\includegraphics` 路径同步。
- [ ] caption 独立可读（不依赖正文上下文）。
- [ ] 三贡献描述与 abstract 句式有显著差异。
- [ ] 5 organs / 2-3-4 views / SSIM2D / PSNR2D 至少在末段出现一次。
- [ ] 引言桥接路径完整：`Novel View Synthesis → Sparse View Synthesis → Tomographic NVS → Sparse Tomographic View Synthesis`。

## 5. 关联资产

- **主稿**：`main.tex` L58–84。
- **图（计划落地）**：
  - `assets/fig/intro_fig_compare.png`（image2 生成）
  - `assets/fig/intro_fig_teaser.png`（可选，若进主文）
- **需求文档**：
  - [[intro_F01_req_fig_teaser]]
  - [[intro_F02_req_fig_intro_compare]]
- **配色 / 字体规范**：[VISUAL_STYLE.md](VISUAL_STYLE.md)。
- **综合视图**：[[experiment_REVIEW_2026-05-21_section-issues]] §2。
- **关联节文档**：
  - [[intro_2026-05-21_abstract-todo]]（三贡献用词差异化）
  - [[method_2026-05-21_method-todo]]（三模块顺序一致性）

## 6. 执行顺序提示

I1 / I2 是 P0，先做；I4 / I5 是 P1，可在 I1 完成后顺手处理；I6 / I7 留到所有数据 / 图到位后做一次性英文润色。

## 7. 实现记录（2026-05-21 closing snapshot）

本次润色完成情况：

| ID  | 状态 | 落地说明                                                                                                                              |
| --- | ---- | ------------------------------------------------------------------------------------------------------------------------------------- |
| I1  | ⏳   | `assets/scripts/intro_fig_compare_image2_call.py` 已就绪，`assets/prompts/intro_fig_compare.md` 描述完整。`IMAGE2_API_KEY` 未注入，主稿暂以 `\fbox{Placeholder: ...}` fallback 渲染，待 key 提供后一键生成 PNG 即可解除 placeholder。 |
| I2  | ✓    | `main.tex` L73 的 `\includegraphics{assets/fig/intro_fig_compare.png}` 路径已迁移到 §13 规范前缀；旧 `fig_intro_*.png` 资产已在工作树清理（见 git status `D assets/fig/fig_intro_compare.png` 等）。 |
| I3  | ⏳   | F01 teaser 暂不进主文；保留为 supplementary 候选，详见 [[intro_F01_req_fig_teaser]]。                                                  |
| I4  | ✓    | 三贡献已重写为「capacity-allocation reframe / evolution-rule intervention / unified 5-organ × 2-3-4-view benchmark」三句，与 abstract 措辞做了显著差异化（abstract 强调机制因果，contributions 强调贡献声明）。 |
| I5  | ✓    | 引言末段已显式声明 `five organs (Chest, Head, Abdomen, Foot, Pancreas)`、`2, 3, and 4 input views`、对比六个 baseline，并锚定 strongest evidence 在 3-view regime（与 §4 主结果一致）。 |
| I6  | ✓    | L65、L67 已批量替换 conversational/教程式表达；当前 intro 全段无 `we can see` / `let's` / `it turns out` 类口吻。                          |
| I7  | ✓    | intro 中 6 个对比方法 + 3 个 X-ray/CT 物理参考的 `\cite{}` 全部存在于 `references.bib`，biber 已成功消费 25 个 citekey（详见 `main.blg`）。  |

验证清单同步：

- ✅ `latexmk -xelatex` 全流水线（xelatex → biber → xelatex → xelatex → xdvipdfmx）通过；`main.log` 中 `Citation undefined` / `Reference undefined` / `Empty bibliography` 警告数为 0；最终 `main.pdf` 19 页。
- ⏳ `assets/fig/intro_fig_compare.png` 物理生成待 `IMAGE2_API_KEY` 提供；当前 `\IfFileExists` fallback 保证编译可通过。
- ✅ caption 已重写为可独立阅读（说明 setting、对比对象、关键观察）。
- ✅ 三贡献描述与 abstract 句式差异化。
- ✅ `5 organs / {2,3,4} views / SSIM2D / PSNR2D` 已在引言末段一次性出现。
- ✅ 桥接路径 `Novel View Synthesis → Sparse View Synthesis → Tomographic Novel View Synthesis → Sparse Tomographic View Synthesis` 在 §1 完整展开。

遗留事项（不阻塞当前投稿草稿编译）：

- IMAGE2_API_KEY 注入后运行 `python assets/scripts/intro_fig_compare_image2_call.py` 一键生成 `assets/fig/intro_fig_compare.png`，placeholder 即自动解除。
- F01 teaser 是否升级到主文，待主图页数预算锁定后再决定。
- xdvipdfmx `Object @figure.N already defined` 为 PG 模板 + hyperref 已知兼容性 warning，不影响 PDF 正确性。
