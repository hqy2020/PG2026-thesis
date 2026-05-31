# method_fig_gap — image2 绘图提示词（GAP 模块机制图）

## 用途

- 论文：`XRA-GS: X-ray Attenuation-Aligned Gaussian Splatting for Sparse Tomographic View Synthesis`（PG2026 投稿）
- §3.4 Geometry-aware Pruning 配图。展示 GAP 如何通过 KNN proximity + gradient 双判据回收边界冗余 Gaussians。
- 与 pipeline / SPS / ADM 三图视觉统一。GAP 主色琥珀 `#F57F17`。
- 输出文件名：`method_fig_gap.png`，落地 `assets/fig/`。

## 设计决策

- **结构模式**：Pattern II 分步可视化（参考 method-fsgs.png 极简机制图范式）
- **每面板 ≤5-8 个 Gaussian**，用少量元素以小见大
- **视觉元素**：GT 虚线轮廓 + Gaussian 状态色（蓝=retained, 灰=prune candidate）+ KNN proximity 连接边（橙红线）+ zoom-in 放大

## image2 PROMPT (中文，浓缩版，可直接喂给生图模型)

绘制一张学术论文模块细节示意图，白色背景(#FFFFFF)，现代扁平矢量风格，Apple 式圆润美感，CVPR/NeurIPS 顶会论文级别质量。

模块名: Geometry-aware Pruning (GAP)

整体布局: 水平三列并排，宽高比约 16:6（约 1600×375 px），白色背景。三列从左到右用黑色实线圆润箭头（2px 线宽，圆润三角箭头头部）连接。每列上方有加粗 sans-serif 标题。

面板 (a) After Densification（左侧）:
- 底层放一个简洁的黑色虚线轮廓形状，代表解剖结构边界（画一个简化的 L 形或弧形组织轮廓，不画真实器官细节）
- 约 8-10 个蓝色(#1976D2)扁平 2D 半透明椭圆密集聚集在轮廓边缘/边界处，互相紧挨、有重叠
- 仅 1-2 个蓝色小椭圆孤零零地散布在内部区域（远离边界）
- 视觉效果：边界处拥挤堆叠 vs 内部空旷稀疏，传达"容量被边界垄断"
- 左上角放 (a) 标记，加粗黑色

面板 (b) Joint Criterion（中间）:
- 与 (a) 完全相同的虚线轮廓和 Gaussian 位置布局
- 新增：橙色细线(1px, #FF7F0E)连接相邻 Gaussian 椭圆的中心点，形成 KNN 连接图（约 8-12 条连接线）
- 边界处 3-4 个最拥挤的椭圆变为灰色(#BDBDBD)，旁边各标一个小 × 号（表示 prune candidates：拥挤且不活跃）
- 保留的蓝色椭圆保持不变（活跃或不拥挤的）
- 底部居中放一个公式框（8px 圆角，#F5F5F5 浅灰背景，1px #E0E0E0 边框），内写斜体公式: c_i = 1[d_i < τ ∧ ḡ_i < δ]
- 左上角放 (b) 标记

面板 (c) After Pruning（右侧）:
- 相同虚线轮廓
- 灰色 candidates 已消失（被移除）
- 保留的蓝色 Gaussians 分布更均匀：边界处数量减少（约 4-5 个）但仍有覆盖，内部 1-2 个保留
- 从边界区域用橙色(#F57F17)细线矩形框标注一个小区域，用折线引出 zoom-in 放大视图
- Zoom-in 放大面板（橙色边框）内部展示 2-3 个蓝色椭圆的细节：
  - 虚线椭圆表示原来的较大协方差
  - 实线椭圆表示收缩后的较小协方差
  - 小箭头从虚线椭圆指向实线椭圆，表示"收缩"
  - 文字标注 "contract σ"
- 左上角放 (c) 标记

底部图例（紧凑融入面板 (c) 的下方空白处，不独占一整行）:
- 蓝色椭圆图标 + "Retained"
- 灰色椭圆图标 + × + "Prune Candidate"  
- 橙色细线图标 + "KNN Edge"
- 虚线椭圆图标 + "Original σ"

**全局字体规范（5 张图统一）**:
- 全图仅使用 2 种字体样式：①标题=加粗无衬线（Helvetica Bold / Arial Bold 风格），②描述性文字=常规无衬线（Helvetica Regular / Arial Regular 风格）
- 面板标题（After Densification / Joint Criterion / After Pruning）: 加粗无衬线，8-9pt
- 图例文字（Retained / Prune Candidate / KNN Edge）: 常规无衬线，7pt，灰色 #757575
- 公式: 8pt LaTeX 风格深灰斜体
- Zoom-in 标注（contract σ）: 常规无衬线，7pt
- 严禁出现衬线体（Times/Serif）、手写体、装饰体
- 所有文字字号与本系列其他 4 张图（intro/pipeline/SPS/ADM）保持一致

设计规范（必须严格遵守）：
- 白色背景(#FFFFFF)，现代扁平矢量风格，Apple 式圆润美感
- 所有元素扁平 2D，不使用 3D 光影/高光/立体渲染
- Gaussian 必须画成扁平纯色 2D 椭圆，绝对禁止画成 3D 球体/有高光的球/有光影的椭球
- 公式框：8px 圆角，浅灰背景
- 箭头：2px 圆润箭头，实线黑色=操作流，转折处圆角过渡
- 文字尽量精简，强调视觉元素表达
- 图例融入面板空白区域
- 不使用 emoji、卡通元素
- 不使用橘色以外的红色（避免和 SPS 蓝/ADM 绿混淆）
- 质量对标 CVPR/NeurIPS 顶会论文配图
