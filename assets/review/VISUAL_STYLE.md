# XRA-GS 论文图表全局视觉规范

**所有 figure 需求文档（包括示意图与实验图）必须遵守这一套规范。不在自己的 md 里另起色板、另起字号、另起线宽。**

## 1. 角色色板 (Role palette)

每个 hex 都有固定语义。色码即"它代表什么"，不要在别处复用。

| 角色                    | 名称 (固定)        | Hex          | 适用场景                                                            |
| ----------------------- | ------------------ | ------------ | ------------------------------------------------------------------- |
| **Ours / XRA-GS**       | Crimson Red        | `#D7263D`    | 高亮 XRA-GS 在性能散点、qualitative 列、Ours 行、误差地图最劣区域   |
| **SPS module**          | Soft Purple        | `#7B5CA6`    | pipeline 与模块图中 SPS 块、SPS 点云、SPS 曲线                      |
| **GAP module**          | Teal               | `#3CA897`    | pipeline 与模块图中 GAP 块、GAP 标记的剪枝点、GAP 曲线              |
| **ADM module**          | Warm Orange        | `#E07B39`    | pipeline 与模块图中 ADM 块、ADM 调制曲线                            |
| **Baselines (generic)** | Slate Blue         | `#5B7C99`    | 所有 baseline 在散点、bar、line plot 中的默认颜色                   |
| **Reference / Neutral** | Neutral Gray       | `#888888`    | random init、coarse FDK、对照基线、灰底注释                         |
| **Zoom-in box A**       | Crimson (= Ours)   | `#D7263D`    | qualitative 图上红色 zoom-in 框 + 下方对应裁剪边框                  |
| **Zoom-in box B**       | Royal Blue         | `#1F6FB2`    | qualitative 图上蓝色 zoom-in 框 + 下方对应裁剪边框                  |

**禁用色**：默认 `matplotlib` 调色板 `#1F77B4 #FF7F0E #2CA02C` 等（与上面 baseline 灰蓝撞色却语义不同），任何饱和荧光色，任何霓虹紫粉。

## 2. 数据可视化色映射 (Continuous colormaps)

固定 colormap，不在不同图里换：

| 用途                            | colormap                  | 数值范围                            |
| ------------------------------- | ------------------------- | ----------------------------------- |
| CT slice / 投影                 | `gray`                    | 输入归一化到 [0,1] 后线性映射       |
| Error / |GT − pred|             | `inferno`                 | 0 到全表/全图最大值，统一 vmax      |
| Density / sampling probability  | `viridis`                 | 0 到 1，统一 vmax=1                 |
| Attenuation μ                   | `magma`                   | 与 GT 同一物理量级                  |

**关键**：同一篇论文里任何 error map 必须共享同一 vmax；同一篇论文里任何 density map 必须共享同一 vmax。否则审稿人无法横向对比。

## 3. 排版规范

### 字号
- Figure title (顶部): **10 pt 加粗**
- Sub-caption / panel label `(a) (b) (c)`: **9 pt 加粗**
- Axis label: **8 pt 正常**
- Tick label: **7 pt 正常**
- Method name annotation (qualitative 列首 / scatter bubble 名): **8 pt 正常**，外加 0.5pt 白色 halo 防遮挡
- 任何中文：禁止出现在图内

### 字体
- 正文风格 sans-serif，推荐 Helvetica / Arial / Inter
- 公式严格用 LaTeX 字体（Computer Modern），不用图形软件 Embed Text 假装公式

### 线宽
- 数据流 / pipeline 实线: **1.2 pt 黑**
- 梯度流 / 反向连接虚线: **1.0 pt 黑 dashed (3pt-2pt)**
- 数据曲线 / scatter line: **1.5 pt**，每条线必须可以用颜色区分（不依赖虚线类型区分方法，色弱友好）
- panel 边框: **0.5 pt 灰 `#CCCCCC`**

### 箭头
- 单一头部样式：实心三角，长 6 pt、宽 4 pt
- 不混用 latex/stealth/open 三种箭头

### 留白
- panel 间隙：水平 6 pt，垂直 8 pt
- panel 内左右边距：≥ 4 pt，避免标注贴框

### 图例
- 位置：右上角，半透明白底框 (alpha=0.85)，0.5 pt 边框
- 与方法颜色直接对照，方法名右对齐
- 不写 "Method 1 / Method 2"，全部写真名 (`XRA-GS (Ours)` 等)

## 4. 方法名 / 模块名命名

引用 CLAUDE.md §1 / §2 / §10：

- 主方法名：`XRA-GS`（带连字符，全大写）
- 三模块：`SPS` / `GAP` / `ADM`（不带句点，不写全称缩写如 `S.P.S.`）
- 6 个 baseline 顺序（在 qualitative 图、散点 legend、表头中默认按此固定序）：
  1. `CoR-GS`
  2. `DNGaussian`
  3. `FSGS`
  4. `X-Field`
  5. `X-Gaussian`
  6. `R2-Gaussian`
  7. `XRA-GS (Ours)` ← 最后一列/最后一行，红色高亮

任何变体（`XRA*GS`、`XField`、`R2GS`、`Co-RGS`）都属于失败案例。

## 5. 高亮规则

### qualitative 图
- Ours 列首方法名加粗 + 下划 Crimson 短线 (2 pt)
- 同一行同 organ + 同 view 严格保持
- 红框 zoom-in（A 色）+ 蓝框 zoom-in（B 色），下方放大图边框与上方框颜色一致

### 表格
- best per column: 数字加粗 + 背景填色 `#FCE4E5`（Crimson 10% tint）
- 2nd best: 数字下划线，无背景
- 3rd best：仅 italic（可选，主表不强制）
- ↑ / ↓ 箭头紧跟 metric 名，不省略

### 散点
- Ours bubble 填色 Crimson，描边 0.8 pt 黑
- 其他 bubble 填色 Slate Blue + 30% alpha，无描边
- Ours 必须位于图最优方向（顶会通行：右上）

## 6. 文件输出规范

- 矢量优先：示意图（pipeline / 模块）一律输出 PDF (TikZ / Illustrator / Inkscape)
- 实验图（含 CT 切片）：PNG 300dpi 或 PDF（matplotlib `savefig(..., dpi=300, bbox_inches='tight')`）
- 落地路径：图源全部进 `assets/fig/`，文件名与 md ID 对齐（如 F03 → `fig_method_pipeline.pdf`）
- 配套 source：用 Python / TikZ 生成的图必须在 `assets/scripts/` 留可重跑脚本

## 7. 反例汇总（全局禁止）

- 在不同图里给"Ours"换色（一会儿红一会儿绿）
- 在 pipeline 图里用 matplotlib 默认蓝（撞 baselines slate blue）
- 在示意图里出现照片级渲染但实验图却用极简线稿（风格分裂）
- 图例里用图标 emoji ⭐ / 🟢 / 🟠 代替色块
- 同一个 error map 在不同图里 vmax 不同却没在 caption 注明
- 同一篇论文里 SPS 在 pipeline 是紫色，在 module 图却画成蓝色

## 8. 与本目录其它 md 的关系

后续 figure 需求 md **不再单独列色码**，只写「Ours 用红高亮（见 VISUAL_STYLE §1）」「error map 用 `inferno`（见 VISUAL_STYLE §2）」之类的引用。若某张图必须破例（非常罕见），需在该 md 第 4 节显式声明"破例理由"。
