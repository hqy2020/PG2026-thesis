# Pacific Graphics 2026 论文

## 会议信息

- **会议**: Pacific Graphics 2026 (PG2026)
- **地点**: Singapore
- **日期**: October 6-9, 2026
- **官网**: https://pacificgraphics2026.github.io/

## 投稿截止日期（AoE）

| 节点 | 日期 |
|------|------|
| Abstract due | **June 1, 2026** |
| Paper submission | **June 8, 2026** |
| Rebuttal period | July 17-21, 2026 |
| Decision notification | July 31, 2026 |
| Final revision | August 14, 2026 |
| Final acceptance notification | August 21, 2026 |
| Camera-ready submission | August 31, 2026 |

## 论文类型

| Track | 页数 | 发表 |
|-------|------|------|
| **Journal Paper** | 10-12 pages | Computer Graphics Forum (CGF) special issue |
| **Conference Paper** | 7-8 pages (不含参考文献和纯图页) | PG2026 proceedings in EG digital library |

## 投稿方式

- 投稿系统: [SRM system](https://www.srm-system.org/)
- 审稿方式: **双盲** (doubly anonymous)
- 有 rebuttal 阶段

## 文件结构

```
├── main.tex              # 主论文文件
├── references.bib        # 参考文献
├── figures/              # 图片目录
│   └── ...
├── egPublStyle-PG2026/   # EG LaTeX 模板样式文件
│   ├── egpubl.cls        # 文档类
│   ├── pg2026s.sty       # PG2026 style
│   └── ...
└── README.md
```

## 编译方式

```bash
# 使用 biber（推荐）
pdflatex main
biber main
pdflatex main
pdflatex main

# 或使用 Makefile（如果有的话）
make
```

## 关键 Notes

- 投稿用 `\ConferenceSubmission`，最终版改为 `\ConferencePaper`
- 投稿阶段不需要填写作者信息（双盲）
- 如果投 Journal track，在提交时选择
- 模板从官网下载: https://pacificgraphics2026.github.io/ → LaTeX-template
