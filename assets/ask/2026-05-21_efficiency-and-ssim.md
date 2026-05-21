## 需求描述
补填论文中 efficiency 表和 SSIM2D 表缺失的实验数据。

## 输入
- 设定：3-view setting, five organs (Chest, Head, Abdomen, Foot, Pancreas)
- 对比方法：X-Gaussian, R2-Gaussian, XRA-GS
- 数据集：X-Gaussian 官方仓库发布的处理后的数据

## 期望输出

### Output 1: Efficiency 数据（P0）
文件：`assets/data/tab_efficiency_3view.csv`
格式：
```
method,organ,training_time_min,final_gaussian_count_k,peak_gpu_memory_gb
X-Gaussian,Chest,...,...,...
X-Gaussian,Head,...,...,...
...
R2-Gaussian,Chest,...,...,...
...
XRA-GS,Chest,...,...,...
...
```
同时提供 five-organ average 行。

### Output 2: Per-organ SSIM2D 数据（P1）
文件：`assets/data/tab_ssim2d_per_organ.csv`
格式：
```
method,Chest_2v,Chest_3v,Chest_4v,Head_2v,...,Pancreas_4v,Avg_2v,Avg_3v,Avg_4v
R2-Gaussian,...,...,...
X-Field,...,...,...
XRA-GS,...,...,...
```
注意：如果 DNGaussian / CoR-GS / FSGS / X-Gaussian 的同协议 SSIM2D 也能获取，一并提供。

### Output 3: Single-module ablation 数据（P1）
文件：`assets/data/tab_ablation_single_module.csv`
格式：
```
config,2v_avg,3v_avg,4v_avg
+SPS only,...,...
+GAP only,...,...
+ADM only,...,...
```
用于 supplementary material。

## 优先级
P0（Output 1 阻塞论文投稿，Output 2/3 为 P1）

## 截止时间
尽快
