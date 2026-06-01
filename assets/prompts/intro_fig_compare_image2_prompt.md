---
figure: intro_fig_compare
section: intro
type: intro / physics contrast
output: assets/fig/intro_fig_compare.png
---

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

绘制一张学术论文 intro 概念对比图，白色背景，CVPR/NeurIPS 顶会论文 Figure 1 级别质量。

**参考素材（image-to-image）**:
- 可见光场景物体: `assets/data/light.jpg`（博物馆展厅中的三角龙化石头骨，正面特写，灰棕色骨质纹理）
- X-ray 投影图像: `assets/data/chest.png`（XRA-GS 实验数据 chest X-ray 投影，深底灰度肋骨/心影）

**论文标题**: XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis

**图类型**: 物理对比 — 可见光反射/折射 vs X-ray 穿透/衰减

**整体布局**: 上下两行，宽高比约 16:7。每行从左到右三个区域：成像物理过程 → 成像结果 → Gaussian 分布。上下行之间用灰色细虚线水平分隔。

**【对齐硬规则】**:
- 上下两行中，三个列（Imaging Process / Image / Gaussian Distribution）必须严格左右对齐
- 上行和下行同一列的内容宽度相同，左右边界对齐
- 行高统一：上下两行高度相等
- 所有外框（如果有）的边缘必须严格对齐

**内容结构**:

行(a) Visible Light（白色背景，左侧竖排标注 "(a) Visible Light"）:
- 左区「Imaging Process」: 一个太阳形光源图标在左上方发出多条彩色光线（红/绿/蓝/黄表示不同波长），光线射向一个**博物馆中的三角龙化石头骨**（灰棕色骨质表面，正面视角，与参考图 light.jpg 一致的三角龙头骨外观），光线到达头骨表面后折回/散射（箭头方向从物体表面反弹回来），一个小型扁平 camera 图标在右侧接收反射光。在物体表面附近标注 "Reflection" 和 "Scattering"，在光源旁标注 "Source"，在 camera 旁标注 "Pixel"。
- 中区「Image」: 直接使用三角龙化石头骨的真实照片（与参考图同款三角龙头骨，博物馆正面拍摄视角），带浅灰边框圆角。
- 右区「Gaussian Distribution」: 三角龙头骨的简洁虚线轮廓（黑色虚线，不填充），12-15 个扁平 2D 半透明粉色/品红色椭圆紧贴在头骨虚线轮廓表面外侧排列，形成表面聚集的分布。底部标注 "Surface-clustered"。

行(b) X-ray（白色背景，左侧竖排标注 "(b) X-ray"）:
- 左区「Imaging Process」: 一个 X-ray source 倒三角形在左侧，发出数条浅灰色射线直线，射线完全穿透一个**人体胸腔区域的简化轮廓**（肋骨和心影的示意形态），到达右侧的一个窄长矩形 detector。射线是直线贯穿不折回。在射线路径上标注 "Penetration"，在 source 旁标注 "Source"，在 detector 旁标注 "Attenuation" 和 "Pixel"。
- 中区「Image」: 使用真实胸部 X-ray 投影图（与参考图 chest.png 风格一致，深色背景灰度肋骨/心影轮廓），带浅灰边框圆角。
- 右区「Gaussian Distribution」: 胸腔的简洁虚线轮廓（黑色虚线，不填充），12-15 个扁平 2D 半透明多色椭圆（绿色、蓝色、橙色，代表不同材料/密度）沿一条射线路径均匀分布在胸腔内部。所有椭圆大小相同、透明度相同，体现 equal contribution / no occlusion 效果。底部标注 "Path-distributed"。

**视觉元素**:
- 三角龙头骨: 博物馆展厅中的三角龙化石头骨正面照片（灰棕色骨质，三只角清晰可见）
- 胸部 X-ray: 真实 chest X-ray 投影风格（深色背景灰度肋骨/心影）
- 光源: 太阳形图标（可见光）/ 倒三角形（X-ray source）
- 射线: 彩色细线带箭头（可见光，反射折回）/ 灰色直线贯穿（X-ray，不折回）
- Gaussians: 扁平 2D 半透明纯色椭圆，绝对不画成 3D 球体或有高光的球
- GT 轮廓: 黑色虚线勾勒物体形状，不填充

**颜色方案**:
- 白色背景
- 可见光射线: 红/绿/蓝/黄多色
- X-ray 射线: 灰色细线
- 可见光 Gaussians: 粉色/品红 半透明
- X-ray Gaussians: 多色（浅青绿/蓝/橙）半透明，代表不同材料

**标注要求**:
- (a) 左侧竖排 "(a) Visible Light"
- (b) 左侧竖排 "(b) X-ray"
- 列标题: "Imaging Process", "Image", "Gaussian Distribution"（或 "3D Representation"）
- 物理过程标注: "Source", "Reflection", "Scattering", "Penetration", "Attenuation", "Pixel"
- 分布标注: "Surface-clustered", "Path-distributed"
- 所有文字水平排列（竖排标注除外），sans-serif

**全局字体规范（5 张图统一）**:
- 全图仅使用 2 种字体样式：①标题=加粗无衬线（Helvetica Bold / Arial Bold 风格），②描述性文字=常规无衬线（Helvetica Regular / Arial Regular 风格）
- 列标题 / 行标题: 加粗无衬线，8-9pt
- 物理过程标注（Source, Reflection 等）: 常规无衬线，7pt，灰色 #757575
- 分布标注（Surface-clustered, Path-distributed）: 常规无衬线，7pt，灰色 #555555
- 严禁出现衬线体（Times/Serif）、手写体、装饰体
- 所有文字字号与本系列其他 4 张图（pipeline/SPS/GAP/ADM）保持一致

设计规范（必须严格遵守）：
- 白色背景(#FFFFFF)
- 三角龙头骨使用真实照片风格，胸部 X-ray 使用真实 X-ray 投影风格
- Gaussian 必须画成扁平纯色 2D 椭圆，绝对禁止画成 3D 球体/有高光的球/有光影的椭球
- 不同颜色代表不同材料/密度
- 【对齐硬规则】上下两行的三列必须严格左右对齐，行高统一，所有外框边缘对齐
- 文字尽量精简，强调视觉元素表达
- 不使用 emoji、卡通元素
- 质量对标 CVPR/NeurIPS 顶会论文配图
