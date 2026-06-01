# PG2026 / RAttAGS 投稿推进路线图

按 CLAUDE.md §13 维护：每完成阶段性工作后同步勾选已完成项、记录验收状态与下一步。

最近更新：2026-05-26（intro 对齐 + teaser 重构 完成）

---

## 1. 写作链（main.tex）

### 1.1 Abstract
- ☑ 顶会式 problem → gap → core insight → method → strongest evidence 骨架
- ☐ 待 §4 实验数据最终化后回填 strongest evidence 表述

### 1.2 Introduction（2026-05-26 重写完成）
- ☑ Para 1：CT 定义 / X-ray 二句引入 / `Sparse Tomographic View Synthesis` 任务化
- ☑ Para 2：相关工作总览收束到 `where new primitives are spawned` 论点
- ☑ Para 3：与 teaser 上行严格绑定的 capacity-misallocation 论证
- ☑ Para 4：SPS → GAP → ADM 三段式 attenuation-aligned evolution
- ☑ Fig 引用 caption：脱离正文可读，对齐 X-Field 风格
- ☑ Contributions：4 条无 dataset/view/baseline/metric 泄露
- ☑ D.1 数字泄露 grep / D.2 任务名口径 grep 全部 PASS
- ☑ D.3 latexmk 编译验证 19 页通过，无 intro-area warning

### 1.3 Related Work
- ☐ 待按英文顶会写法收紧三类工作的衔接句

### 1.4 Method
- ☐ SPS / GAP / ADM 三模块章节结构稳定，符号统一性最终对齐
- ☐ Algorithm box 内容核对

### 1.5 Experiments
- ☐ 主指标表（5 organs × {2,3,4} views，SSIM2D / PSNR2D）数据回填
- ☐ Efficiency 表 #Gaussians / training time / GPU memory 数据回填
- ☐ Progressive ablation 数据回填
- ☐ Qualitative 主图与 detail consistency 图素材回填

### 1.6 Discussion / Limitation
- ☑ Limitations 已从独立章移入 Discussion

### 1.7 Conclusion
- ☐ 待 §4 收敛后回扣三模块与 evolution-rule 主线

---

## 2. 资产链（assets/）

### 2.1 Figures（assets/fig/）
- ☑ `intro_fig_compare.png`（2026-05-26 重画，drawio 源 + matplotlib 等价渲染脚本并存；旧版备份为 `intro_fig_compare_backup.png`）
- ☑ `intro_fig_compare.drawio`（可编辑源）
- ☐ `method_fig_pipeline.png`（pipeline）
- ☐ `method_fig_sps.png` / `method_fig_gap.png` / `method_fig_adm.png`
- ☐ 各 experiment_fig_*.png（待实验 agent 答复）

### 2.2 Tables（assets/tables/）
- ☐ `experiment_tab_main_psnr2d.tex` / `experiment_tab_main_ssim2d.tex`
- ☐ `experiment_tab_efficiency.tex`
- ☐ `experiment_tab_ablation.tex`

### 2.3 Prompts / Scripts
- ☑ `assets/prompts/intro_fig_compare_image2_prompt.md`（中文备份提示词，可一键 image2 重出）
- ☑ `assets/scripts/intro_fig_compare_render.py`（matplotlib 渲染脚本，与 drawio 源版式等价）

---

## 3. 实验链（assets/ask ↔ assets/answer）

- ☐ P0：`tab_experiment_efficiency` 中 training time / #Gaussians / GPU memory（3-view setting）
- ☐ P0：per-organ SSIM2D / PSNR2D 数据
- ☐ P1：progressive ablation per-organ 细分
- ☐ P2：hparam sensitivity 补图

---

## 4. 当前阻塞 / 下一步

- 主线下一步：进入 §4 Experiments 数据回填闭环（依赖实验 agent answer）
- 次线下一步：method 章节符号 / algorithm box 与新 intro 论点的一致性复核
- 30 秒可读性人工抽查：新 teaser `intro_fig_compare.png` 已可单独阅读，等下一次协作者审阅
