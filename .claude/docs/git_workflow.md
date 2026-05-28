# Git / GitHub 协作工作流

用户希望每次改完一版就 push 到 GitHub，他通过 `git diff` 远端 ↔ 本地的 commit 间快速 review。本节固化这套工作流，避免下次新对话再问一次或漏 push。

## 核心硬规则

- 每完成**一组逻辑完整的改动**，必须执行：`commit → push origin main`
- 「一组逻辑完整的改动」=一次用户请求收尾时；不要把多轮改动堆成一个超大 commit
- push 完才算「这一版交付」，否则视为本轮任务未完成
- 远端：`https://github.com/hqy2020/PG2026-thesis.git`（origin/main）

## commit 范围决策

push 前先 `git status`，把改动分成三类：

1. **本轮专属**：本次用户请求直接驱动的文件改动 → 必须 commit
2. **历史未提交**：工作树里已有但跟本轮无关的变动（之前未 push 的）→ 默认**跟本轮一起 commit**，避免 diff 越积越复杂；除非用户明确说要分多个 commit
3. **垃圾/临时文件**：
   - `main 2.synctex(busy)` / `main 3.synctex(busy)` 等 latexmk 多开产生的临时文件 → **不 commit**，可删
   - `main.aux` / `main.log` / `main.bbl` / `main.fls` / `main.fdb_latexmk` / `main.out` / `main.toc` 等 LaTeX 中间产物 → 跟随 `.gitignore`；若已被跟踪保留现状，未跟踪不要新加
   - `.DS_Store` → 不 commit

`main.pdf` 当前在仓库里跟踪，重新编译后的更新随 commit；不要单独移除。

## commit message 规范

- 中英文均可，跟随历史 commit style（看 `git log --oneline -10`）
- 现有风格：`feat(paper): <one-line summary>` / `完成<动词>` 等中英混合
- 主要描述 **why**（为什么改）+ 关键变更点；不要逐文件列 diff
- 使用 HEREDOC 传 message，避免引号转义问题
- 默认尾部加 Co-Authored-By trailer：

```
Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
```

## push 流程模板

```bash
# 1. 看状态
git status

# 2. 明确加文件（不要 git add -A）
git add main.tex references.bib CLAUDE.md .claude/ ...

# 3. 清理临时文件（不 add 进 commit；可删）
rm -f main\ [0-9].synctex* main\ [0-9].fls main\ [0-9].aux 2>/dev/null

# 4. commit（HEREDOC 传 message）
git commit -m "$(cat <<'EOF'
feat(paper): <one-line summary>

- bullet1
- bullet2

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"

# 5. push
git push origin main

# 6. 验证
git status   # 应是 clean / nothing to commit
git log --oneline -1   # 确认最新 commit
```

## 不允许的操作（除非用户显式要求）

- `git push --force` / `git push -f`（尤其对 main 分支）
- `git reset --hard`
- `git commit --amend`（默认创建新 commit，不修改已有 commit）
- `git add -A` / `git add .`（容易把 `.env`、credentials、binary、临时文件误加）
- `--no-verify`（不跳过 hook）
- 修改 git config

## 与现有规则的交叉

- 「不要 `git log` 查找过期文件」（见主 CLAUDE.md §4）依然成立——push 流程里允许 `git log --oneline` 看 commit 风格，但不要把它当成发现工作树状态的手段
- 单一事实源原则（§5）保留——`main.tex` 是主稿，commit 描述围绕 `main.tex` / `assets/` 的实际改动

## 自检 checklist

每次 push 收尾必查：

- [ ] `git status` 显示 `nothing to commit, working tree clean`
- [ ] `git log --oneline -1` 是本次新 commit
- [ ] `git rev-list --left-right --count origin/main...HEAD` 输出 `0\t0`（已同步）
- [ ] 没有把 `main N.synctex(busy)` / `.DS_Store` 之类临时文件 commit 进去

## 询问范围

`git status` 显示有大量「历史未提交」改动且与本轮无明显关联时，先向用户确认范围再 commit，不要默默打包。
