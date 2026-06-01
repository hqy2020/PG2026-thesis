# 命名规则：方法名 / 任务名 / 标题 / CT 描述口径

## 方法名 / 任务名 / 标题（默认准绳）

- 方法名：`RAttAGS`
- 任务名：`Sparse Tomographic View Synthesis`（`Sparse` 在前、`Tomographic` 在后）
- 标题：`RAttAGS: X-Ray Attenuation-Aligned 3D Gaussian Splatting for Sparse Tomographic View Synthesis`
- 物理关键词：`attenuation`；标题里 `X-Ray Attenuation-XXX 3D Gaussian Splatting` 默认 `XXX = Aligned`
- 英文拼写默认 `X-ray`（与论文标题、CT 术语一致；不要漂成 `X-Ray` / `Xray`）

## sparse-view 用法

- `sparse-view` 是设定/条件描述，不是任务名本体；默认写 `sparse-view setting` / `sparse-view condition` / `sparse-view acquisition`
- 作为复合形容词必须保留连字符 `-`

## CT 描述口径

- CT 概念上是一种 X-ray computed tomography，但**不写**为 `X-ray computed tomography (CT)` 这种紧贴同位语
- 缩写定义统一：`Computed tomography (CT) is an essential imaging technique for ...`（参考 R²-Gaussian、LB、DGR 开篇）
- 不要在 CT 定义句里同时出现两次 `X-ray`
- X-ray 默认在第二句单独引入：`During a CT acquisition, an X-ray source rotates around the object while a detector records multi-angle attenuation measurements, from which ... can be recovered through tomographic reconstruction.`
- 基本成像描述默认含一组固定概念：`tomographic` / `X-ray attenuation` / `multi-angle projections` / `tomographic reconstruction` / `cross-sectional images`
- `CT scan` 仅用于临床场景（如 "a patient undergoes a CT scan"），不作为任务名或主文核心术语
- 区分任务目标与采集设定：任务名 `Sparse Tomographic View Synthesis`；采集设定 `sparse-view setting` / `sparse-view condition`

## 同步检查清单

任何改动须同步检查以下位置，避免标题 / 图注 / 方法名漂移：

- `main.tex` 的 `\title[...]{}`
- 正文中方法名、缩写、图注、表注
- 图中的方法标签
- 所有实验说明文档中的方法名

用户最新指令为最高优先级；否则默认保持上述命名。
