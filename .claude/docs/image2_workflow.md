# 生成式图片协作约定（gpt-image-2 skill）

当任务涉及「辅助生成论文用图片」「生成概念图底图」「生成定性图素材」「补充视觉化示意」时，默认协作约定如下。

## 通用约定

- 默认使用 `gpt-image-2` 模型（简称 `image2`）
- 默认导出 `png`
- 生成结果视为 figure **素材**，不是最终论文排版成品
- 落地到 `assets/fig/`，由后续工作流统一加 panel 标号、caption、方法标签、版式编排
- 图中的论文术语、模块名、坐标轴、数字标注，优先后置到排版阶段处理，不依赖生成模型直接烘焙到位
- 当前默认绘图链路为 `gpt-image-2 skill`：**禁止用 drawio 源文件或 matplotlib 渲染脚本代替** image2 主流程。drawio / matplotlib 仅作为冷备份，且必须在 image2 三次以上迭代均不达标时才允许启用，并显式说明原因

## 当前默认通道：gpt-image-2 skill（基于 codex CLI 复用 ChatGPT 订阅）

> 不再走第三方 HTTP API（zenmux / mikucode 已封存为冷备份），新任务默认按本节走。

### 标准调用模板

```bash
# 1) 抽 prompt 浓缩段（## image2 PROMPT marker 之后所有内容）
awk '/^## image2 PROMPT/{flag=1; next} flag' \
  assets/prompts/<section>_<figname>_image2_prompt.md > /tmp/<figname>_prompt.txt

# 2) 调 skill，--out 必须绝对路径
PROMPT_BODY=$(cat /tmp/<figname>_prompt.txt)
bash /Users/openingcloud/.claude/skills/gpt-image-2/scripts/gen.sh \
  --prompt "$PROMPT_BODY" \
  --out /absolute/path/to/assets/fig/<section>_<figname>.png \
  --timeout-sec 480
```

### 复用约束

- prompt 文件位置、命名、marker：`## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)`；脚本只读这一段
- 文件命名遵循 [[asset_naming]]：`<section>_<figname>_image2_prompt.md`
- **图片提示词默认必须使用中文**；备份英文版只允许出现在该 marker 之外的章节
- backup 规则：**首次**覆盖时把同名旧图移动为 `<figname>_backup.png`；**已存在 backup 时不重建 backup**，避免把上一版渲染产物当作原始基准
- skill 不接受 `--size` 参数，输出尺寸由 prompt 内文决定 → 中文 prompt 起始句必须明确写 `宽高比约 X:Y`
- 调用前确认 codex CLI 已 `codex login` 且账号含 image-generation 权限
- 失败定位看 skill 退出码（详见 `~/.claude/skills/gpt-image-2/SKILL.md` 列出的 0–7 含义）

### 调用脚本规范

- 调用代码（若需脚本化）放在 `assets/scripts/`，命名遵循 [[asset_naming]]，例如 `intro_fig_compare_image2_generate.sh`
- prompt 文本统一存放在 `assets/prompts/` 下
- 每次成功调用都要在 stdout 打印保存路径、文件大小、prompt 文件指纹，便于审计

### 论文图四步迭代法

1. 写好中文 prompt（写入 `assets/prompts/<section>_<figname>_image2_prompt.md` 的 `## image2 PROMPT (中文...)` 块）
2. 调 skill 生成图片
3. 拿到返回图后**逐项**对照顶会图要求（见 [[figure_design]]）+ [[paper_writing]] 视觉规范评估，同时评估「手工修整到投稿水平的工作量」——只有手工修整工作量合理时才接受
4. 不达标则修改 prompt 重新生成；连续 3 次仍不达标才允许退回 drawio / matplotlib 冷备份，并在 `assets/todolist/todo.md` 显式说明原因
