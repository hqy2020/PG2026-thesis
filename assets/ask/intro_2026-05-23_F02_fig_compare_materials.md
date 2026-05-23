## 需求描述

为论文 Introduction 首图（Figure 1）提供真实实验素材，用于制作 sparse-view input、Gaussian allocation、rendering/error 对比图。所有素材必须来自真实 CT/X-ray projection 实验输出，不能使用概念示意图、生成式占位图或手绘 placeholder。

## 输入

- Dataset：选择视觉效果最有代表性的 1 个 case，优先 Chest；若 Chest 视觉证据不足，可改用 Head 并说明原因。
- View count：优先 2-view setting；若 Gaussian allocation 在 2-view 下不可解释，可补充 3-view 作为备选，但必须标注。
- 对比方法：R2-Gaussian 与 XRA-GS。
- 目标用途：`assets/fig/intro_fig_compare.png` 的真实素材来源。

## 期望输出

请将真实素材放入 `assets/data/intro_f02_compare_materials/`，并返回一个 answer 说明文件到 `assets/answer/intro_2026-05-23_F02_fig_compare_materials.md`。

### 图像素材

- `assets/data/intro_f02_compare_materials/sparse_input_proj1.png`：2-view 中第 1 张输入 X-ray projection，grayscale。
- `assets/data/intro_f02_compare_materials/sparse_input_proj2.png`：2-view 中第 2 张输入 X-ray projection，grayscale。
- `assets/data/intro_f02_compare_materials/fdk_coarse.png`：FDK coarse reconstruction 的 representative slice 或 projection，grayscale。
- `assets/data/intro_f02_compare_materials/gaussian_alloc_r2_gaussian.png`：R2-Gaussian 收敛后 Gaussian centers 在同一 2D slice 上的分布。
- `assets/data/intro_f02_compare_materials/gaussian_alloc_xra_gs.png`：XRA-GS 收敛后 Gaussian centers 在同一 2D slice 上的分布。
- `assets/data/intro_f02_compare_materials/render_r2_gaussian.png`：R2-Gaussian novel-view rendering，grayscale。
- `assets/data/intro_f02_compare_materials/render_xra_gs.png`：XRA-GS novel-view rendering，grayscale。
- `assets/data/intro_f02_compare_materials/gt.png`：对应 novel view 的 ground truth projection，grayscale。
- `assets/data/intro_f02_compare_materials/errormap_r2_gaussian.png`：`|render - GT|` error map，inferno colormap。
- `assets/data/intro_f02_compare_materials/errormap_xra_gs.png`：`|render - GT|` error map，inferno colormap。
- `assets/data/intro_f02_compare_materials/vmax.txt`：两个 error map 共用的 vmax。

### 追溯信息

在 answer 文件中列出：

- organ / case ID / view angles / novel view angle。
- 每个 PNG 的来源路径或生成命令。
- R2-Gaussian 与 XRA-GS 的 checkpoint 路径、config、commit hash。
- PSNR2D / SSIM2D（如果可用）。
- Gaussian counts（如果可用）。
- 若某个素材无法导出，说明原因并给出可替代素材。

## 优先级

P0（阻塞 Introduction 首图最终定稿）。

## 截止时间

尽快；首图需要在正文排版和 caption 定稿前完成。
