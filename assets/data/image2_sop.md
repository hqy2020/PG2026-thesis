# SOP: 示意图生成（image2 API）

适用范围：论文中所有 **示意图（concept/schematic figure）**，包括 teaser、pipeline、SPS/GAP/ADM 模块图、引言对比图等。
**实验图（曲线、bar chart、定量对比）不走此流程，改用 `assets/scripts/` 中的 matplotlib 脚本。**

---

## 1. 环境准备（一次性）

```bash
# 安装依赖（已有则跳过）
pip install requests
```

API Key 和代理设置已写入 `<repo_root>/.env`，脚本启动时自动加载，**无需每次手动 export**。

`.env` 文件内容（勿提交 git，已加入 `.gitignore`）：

```
IMAGE2_API_KEY=sk-xxxx
NO_PROXY=mikucode.xyz
```

> 若需要临时使用不同的 Key，在命令行 export 即可覆盖 `.env`：
> ```bash
> IMAGE2_API_KEY="sk-other" python assets/scripts/image2_generate.py ...
> ```

---

## 2. 快速调用（已有 prompt 的图）

```bash
cd /Users/openingcloud/Documents/PG2026-thesis

# 查看所有可用 prompt 文件
python assets/scripts/image2_generate.py --list

# 生成指定图（prompt stem → output stem，均不含扩展名）
python assets/scripts/image2_generate.py \
    --prompt intro_fig_compare_image2_prompt \
    --output intro_fig_compare

# 自定义尺寸（默认 1840x820，适合跨双栏图）
python assets/scripts/image2_generate.py \
    --prompt method_fig_pipeline_image2_prompt \
    --output fig_method_pipeline \
    --size 1980x800
```

API Key 和代理由 `.env` 自动注入，无需额外参数。

输出自动保存到 `assets/fig/<output>.png`。

---

## 3. 新增一张图的完整流程

### 步骤 1：确认图类型

| 类型 | 走此流程？ | 备注 |
|------|-----------|------|
| teaser / pipeline / 模块示意图 / 引言对比图 | ✅ | 走 image2 API |
| 曲线图 / bar chart / 误差分布 / 超参扫描 | ❌ | 走 matplotlib 脚本 |

### 步骤 2：创建 prompt 文件

文件位置：`assets/prompts/<section>_<name>_image2_prompt.md`
命名前缀规范（§13）：`intro_` / `method_` / `experiment_` / `related_`

```
assets/prompts/
├── intro_fig_compare_image2_prompt.md       ← F02
├── method_fig_pipeline_image2_prompt.md     ← F03
├── method_fig_sps_image2_prompt.md          ← F04
├── method_fig_gap_image2_prompt.md          ← F05
└── method_fig_adm_image2_prompt.md          ← F06
```

**Prompt 文件必须包含的内容（参考 `VISUAL_STYLE.md`）：**

```markdown
# Image2 Prompt: <Figure Title>

Use case: scientific-educational
Asset type: top-conference paper figure for <section>
Target file: assets/fig/<output_name>.png
Aspect ratio: <WxH px>

[约束段落：flat 2D、白背景、无阴影、学术风格等]

Primary request:
<完整英文 prompt，包含布局、颜色、标签、内容描述>

Color palette (strictly enforced):
- XRA-GS / Ours: #D7263D (Crimson Red)
- SPS 模块: #7B5CA6 (Soft Purple)
- GAP 模块: #3CA897 (Teal)
- ADM 模块: #E07B39 (Warm Orange)
- Baselines: #5B7C99 (Slate Blue)
- 参考/对照: #888888 (Neutral Gray)
- CT slice / 投影: grayscale (gray colormap)
- Error map: inferno colormap
- Background: pure white

Allowed short English labels (exhaustive list):
<仅列出允许出现的标签，防止模型生成幻觉>

Style constraints:
White background, flat 2D, no shadows, no 3D effects, no watermark, no legend box.
Academic top-conference figure style.
```

### 步骤 3：生成图片

```bash
cd /Users/openingcloud/Documents/PG2026-thesis
NO_PROXY="mikucode.xyz" IMAGE2_API_KEY="sk-xxxx" \
python assets/scripts/image2_generate.py \
    --prompt <section>_<name>_image2_prompt \
    --output <section>_<name> \
    [--size WxH] [--quality high]
```

### 步骤 4：检查图片质量

生成后用图片查看器检查：
- 三列/多列结构是否清晰
- 配色是否符合 `VISUAL_STYLE.md`（XRA-GS 用红色 #D7263D 等）
- 有无幻觉标签（模型自创的文字）
- 是否有 3D 效果/阴影/透视（不符合学术风格）

**若质量不满意：** 修改 prompt 文件中的描述，重新执行步骤 3 覆盖输出。

### 步骤 5：更新 main.tex 引用

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{assets/fig/<section>_<name>.png}
  \caption{<Caption>.}
  \label{fig:<label>}
\end{figure}
```

### 步骤 6：编译验证

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

---

## 4. 现有图片与 prompt 对应表

| 图 ID | prompt 文件 stem | 输出文件（`assets/fig/`） | 尺寸 | 状态 |
|-------|----------------|--------------------------|------|------|
| F02   | `intro_fig_compare_image2_prompt` | `intro_fig_compare.png` | 1840×820 | ✅ 已生成 |
| F03   | `method_fig_pipeline_image2_prompt` | `fig_method_pipeline.png` | 1980×800 | ⏳ 待生成 |
| F04   | `method_fig_sps_image2_prompt` | `fig_method_sps.png` | 1840×820 | ⏳ 待生成 |
| F05   | `method_fig_gap_image2_prompt` | `fig_method_gap.png` | 1840×820 | ⏳ 待生成 |
| F06   | `method_fig_adm_image2_prompt` | `fig_method_adm.png` | 1840×820 | ⏳ 待生成 |

> **注**：F03–F06 的输出文件名使用 `fig_method_*` 前缀（非 §13 的 `method_fig_*`），
> 原因是 `main.tex` 中 `\includegraphics` 引用路径尚未迁移到新规范。
> 待统一做命名规范迁移时，同步修改 `main.tex` 引用路径即可切换到 `method_fig_*.png`。

**一键生成所有 method 图：**

```bash
cd /Users/openingcloud/Documents/PG2026-thesis

python assets/scripts/image2_generate.py \
    --prompt method_fig_pipeline_image2_prompt --output fig_method_pipeline --size 1980x800

python assets/scripts/image2_generate.py \
    --prompt method_fig_sps_image2_prompt --output fig_method_sps

python assets/scripts/image2_generate.py \
    --prompt method_fig_gap_image2_prompt --output fig_method_gap

python assets/scripts/image2_generate.py \
    --prompt method_fig_adm_image2_prompt --output fig_method_adm
```

---

## 5. 常见问题

| 错误 | 原因 | 解决 |
|------|------|------|
| `ProxyError` / `RemoteDisconnected` | 系统代理拦截 API 请求 | 加 `NO_PROXY="mikucode.xyz"` 前缀 |
| `IMAGE2_API_KEY is not set` | 未 export API Key | `export IMAGE2_API_KEY="sk-xxxx"` |
| `Prompt file not found` | stem 拼写错误 | `python image2_generate.py --list` 查看可用列表 |
| 图中出现幻觉文字 | prompt 未穷举 allowed labels | 在 prompt 末尾加 "Do not invent any other labels" |
| 图有 3D 效果/阴影 | prompt 约束不足 | 在 style constraints 中补充 "no shadows, no 3D effects, no perspective" |

---

## 6. 参考文档

- API 接口文档：`assets/data/image2.md`
- 视觉规范（色板/字号/colormap）：`assets/review/VISUAL_STYLE.md`
- 图表需求规格：`assets/review/<section>_F0X_req_fig_*.md`
- 通用生成脚本：`assets/scripts/image2_generate.py`
