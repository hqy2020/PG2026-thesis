# 论文核心物理论证骨架（α-compositing vs Beer–Lambert）

固定本论文「为什么传统 3DGS 在 X-ray 上失效」的论证立场。后续新对话来重写 intro、abstract 或 method overview，必须按本骨架走，不允许回到「梯度驱动 densification 本身有问题」这种与本方法自相矛盾的写法（本方法自身就用梯度做 split/clone）。

## 必备公式（首次出现处必须配引用）

- 可见光 α-compositing：`C(r) = Σ_i T_i α_i c_i, T_i = ∏_{j<i}(1 − α_j)`，必引 `\cite{kerbl20233d, max1995optical}`
  - 这是 **emission–absorption volume rendering integral**（Max 1995）的离散化形式
- X-ray Beer–Lambert line integral：`−log(I/I_0) = ∫_r μ(x) dl`，必引 `\cite{kak2001principles}`
- 这两个公式是 intro 物理 gap 段的论证基石，**不可只引一个**；任何「α-compositing」「Beer–Lambert」叙述若没有引用视为不完整

## 公式出现位置约束

- intro 第 2 段：只出现两个术语**名字**（`α-compositing` 与 `Beer–Lambert law` / `Beer–Lambert line integral`），**不出现公式本体**
- method preliminaries（§4.1）：完整给出两个公式，并配引用——这是公式的唯一落地点

## intro 第 2 段固定骨架（imaging-physics gap）

1. 提出 imaging-physics gap：两种成像由根本不同的渲染方程支配
2. **可见光侧**：α-compositing（emission–absorption volume rendering integral）下，累计透射率 `T_i = ∏(1−α_j)` 沿 path 乘法衰减；不透明场景下首-hit 表面附近 α 接近 1 → 后续 Gaussians 贡献被 `T_i` 几乎归零 → integrand 集中在 first-hit surface 附近。这是 **transmittance-induced concentration**，**不是「fortunate coupling」**
3. **可证佐证**：SuGaR / 2DGS 都需要额外正则才把 3D Gaussians 拉齐到表面（说明 surface alignment 是渲染方程驱动而非自动属性）→ 必引 `\cite{guedon2024sugar, huang20242dgs}`
4. **X-ray 侧**：Beer–Lambert 取对数后是**线性、order-independent** 的 path-wise sum；没有 transmittance 衰减项，没有遮挡，因此 path 上每个 Gaussian 的贡献权重只取决于其在 path 上的几何长度与衰减系数，与排列顺序无关
5. 收束：现有 X-ray Gaussian 方法换了 renderer 但继承了 surface-rendering 的 evolution rule（densification / pruning / 初始化），这才是失配的根因

## intro 第 3 段固定骨架（不否定梯度）

1. 开头必须有一句明确「问题不在 gradient-driven densification 本身」的免责句，例如：`Crucially, the issue is not gradient-driven densification itself.`
2. 承认本方法保留 split/clone 机制：`our method retains exactly this mechanism`
3. 把失效定位到「X-ray residual gradient 仍集中在 attenuation-contrast 边界 → naïve port 仍把 Gaussians 堆在 boundary」，命名为 `capacity misallocation`
4. 落到修法：augment gradient-driven densification with three attenuation-aligned stages = `SPS / GAP / ADM`

## 文献支撑（已加入 references.bib）

- `max1995optical`：emission–absorption volume rendering integral 的经典论文（Max 1995, IEEE TVCG §IV）
- `kak2001principles`：Beer–Lambert line integral 的标准来源（Kak & Slaney 2001）
- `kerbl20233d`：3DGS 原文
- `guedon2024sugar`：SuGaR (CVPR 2024)——surface-aligned 3DGS variant 旁证
- `huang20242dgs`：2DGS (SIGGRAPH 2024)——surface-aligned 3DGS variant 旁证

## 禁忌写法清单（出现一律改回）

- ❌ `gradient-driven densification is fundamentally misaligned`
- ❌ `redesign the evolution rule itself`
- ❌ `replace the densification mechanism`
- ❌ 任何把「梯度」「split/clone」整体打成错误的措辞
- ❌ `a fortunate coupling between renderer and opaque scenes`（主观猜测性表达）
- ❌ `attenuation-aware`（与标题不对齐）
- ✅ `augment gradient-driven densification with three attenuation-aligned stages`
- ✅ `the evolution rule inherited from surface rendering`
- ✅ `capacity misallocation under line-integral rendering`
- ✅ `transmittance-induced concentration`（surface clustering 的客观机制）
- ✅ `linear, order-independent line integral`（X-ray 全 path 平权的客观机制）

## attenuation-aligned 命名硬规则

全文统一使用 `attenuation-aligned`，**不用** `attenuation-aware`：
- 与标题 `X-Ray Attenuation-Aligned 3D Gaussian Splatting` 严格对齐
- 改稿后默认抽查 `grep -n -i "attenuation-aware" main.tex` 必须无命中

## 适用范围

abstract / intro / related work 对 X-Gaussian 系列的定位 / method overview 第一段 / discussion 的 limitation 反思。改稿后默认抽查这几处是否仍维持「α-compositing vs Beer–Lambert + 不否定梯度 + transmittance-induced concentration + attenuation-aligned」立场。
