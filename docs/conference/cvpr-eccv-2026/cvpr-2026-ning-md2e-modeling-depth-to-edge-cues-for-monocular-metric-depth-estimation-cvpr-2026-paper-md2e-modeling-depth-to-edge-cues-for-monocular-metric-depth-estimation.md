---
title: "MD2E: Modeling Depth-to-Edge Cues for Monocular Metric Depth Estimation"
title_zh: MD2E：面向单目度量深度估计的深度到边缘线索建模
authors: "Ning, Chao, Shen, Minghe, Yokoya, Naoto"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ning_MD2E_Modeling_Depth-to-Edge_Cues_for_Monocular_Metric_Depth_Estimation_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 无相机内参的单目度量深度估计
tldr: 单目度量深度估计在无相机内参时尤为困难，因为焦距与场景深度共同变化使深度变化难以从图像直接感知。本文观察到边缘频率统计随度量尺度呈现系统性偏移，提出MD2E，设计频谱分位估计器SQE从预测边缘图的傅里叶谱输出度量尺度代理，并用边缘预测正则化深度边界。实验在多种相机上验证了无内参度量深度估计的有效性。该工作为度量深度提供了新线索。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 786, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 786, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 786, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 786, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 786, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 786, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 4, \"index\": 7, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 4, \"index\": 8, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 4, \"index\": 9, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 4, \"index\": 10, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 4, \"index\": 11, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 4, \"index\": 12, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 4, \"index\": 13, \"width\": 1028, \"height\": 930}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 4, \"index\": 14, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 4, \"index\": 15, \"width\": 1089, \"height\": 492}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 7, \"index\": 16, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 7, \"index\": 17, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 7, \"index\": 18, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 7, \"index\": 19, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 7, \"index\": 21, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 7, \"index\": 26, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 7, \"index\": 27, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 7, \"index\": 28, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 7, \"index\": 29, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 7, \"index\": 30, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 7, \"index\": 31, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 7, \"index\": 32, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 7, \"index\": 33, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 7, \"index\": 34, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 7, \"index\": 35, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 7, \"index\": 36, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 7, \"index\": 37, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 7, \"index\": 38, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 7, \"index\": 39, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 7, \"index\": 40, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 7, \"index\": 41, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 7, \"index\": 42, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 7, \"index\": 43, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 7, \"index\": 44, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 7, \"index\": 45, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 7, \"index\": 46, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 7, \"index\": 47, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 7, \"index\": 48, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 7, \"index\": 49, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 7, \"index\": 50, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 7, \"index\": 51, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 7, \"index\": 52, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 7, \"index\": 53, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 7, \"index\": 54, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ning-md2e-modeling-depth-to-edge-cues-for-monocular-metric-depth-estimation-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 7, \"index\": 55, \"width\": 640, \"height\": 480}]"
motivation: 在无相机内参的单目度量深度估计中，焦距与场景深度共同变化时，深度变化难以从图像感知。
method: 提出MD2E，利用边缘频率统计的尺度相关性，设计频谱分位估计器SQE作为度量尺度代理，并用边缘预测正则化深度边界。
result: 在多种相机设置下实现无内参的单目度量深度估计，提升度量精度与边界质量。
conclusion: 表明深度到边缘线索可为无内参度量深度估计提供有效的尺度校准。
---

## Abstract
We study monocular metric depth estimation (MMDE) without camera intrinsics at training or inference. When focal length and scene depth vary together, depth changes are difficult to perceive in the image, yet the edge-frequency statistics exhibit systematic, scale-correlated shifts. Building on this observation, we introduce a spectral quantile estimator (SQE) that analyzes the Fourier spectrum of a predicted edge map and outputs a single score used as a proxy for metric scale. Consequently, we propose MD2E, a method that models depth-to-edge cues by deriving edge targets from depth annotations, calibrating metric scale using the spectral score, and using edge predictions to regularize depth boundaries while producing metric depth. Across diverse cameras and datasets, MD2E achieves state-of-the-art performance in MMDE in both zero-shot and fine-tuning settings. The project page is available at https://2j472no.github.io/MD2E/.

---

## 论文详细总结（自动生成）

# MD2E 论文结构化总结

## 1. 核心问题与研究动机

- **研究任务**：单目度量深度估计（Monocular Metric Depth Estimation, MMDE），即在**训练与推理阶段均不使用相机内参**的条件下，从单张 RGB 图像预测具有绝对物理尺度的稠密深度图。
- **背景痛点**：
  - 传统相对深度方法（MiDaS、DPT、Depth Anything 等）采用尺度/平移不变损失，只能恢复相对深度，无法满足 3D 目标检测、数字孪生重建、机器人抓取等需要度量尺度的任务。
  - Metric3D / Metric3D v2 通过规范化相机模型恢复绝对尺度，但**依赖标定好的相机内参**；UniDepth / Depth Pro 尝试去除内参依赖，但仍需学习相机表示或焦距预测模块。
- **关键观察**：当焦距与场景深度**耦合变化**时，RGB 图像外观几乎不变（例如同一把椅子在不同焦距与距离下拍摄），深度变化难以从图像直接感知；然而**预测边缘图的频率统计会呈现与尺度系统相关的偏移**（如边缘粗细、能量在空间频率上的分布变化）。
- **整体意义**：论文提出利用"深度到边缘"（depth-to-edge）线索替代相机内参，作为度量尺度的隐式代理，为无内参 MMDE 提供了一条新路径。

## 2. 方法论

### 2.1 核心思想
将稠密深度标注转换为边缘监督信号 → 训练网络同时输出边缘图与初始深度图 → 用**频谱分位估计器（SQE）**从边缘图傅里叶谱中提取一个标量尺度代理 \(t_{pred}\) → 用该分数校准深度 logits，得到度量深度；同时用边缘预测正则化深度边界以提升锐度。

### 2.2 关键技术细节

- **深度到边缘变换（Depth-to-Edge）**：
  1. 将深度转为**逆深度**，突出近处几何不连续性；
  2. 沿水平、垂直及 ±45° 方向计算**对称有限差分**并聚合，得到方向显著性 \(S(x)\)；
  3. 在 3×3 邻域做**局部 softmax** 得到概率化对比度 \(P_x(y)\)；
  4. 边缘强度定义为中心权重减去邻域最小值：\(E(x) = P_x(x) - \min_{y} P_x(y)\)；
  5. 训练时对 GT 边缘做 **0.9 全局分位二值化**；对预测深度附加一个轻量 1×1 卷积头以对齐二值标签，且与深度回归器解耦。

- **频谱分位估计器（SQE）**：
  1. 对边缘图加**可学习窗函数**（平坦窗与 Hann 窗的凸组合）并去均值，计算功率谱 \(\Phi(f)\)；
  2. 施加**平滑径向高通** \(\Phi_h(f) = \Phi(f)\left[1-\exp(-(r(f)/r_0)^2)\right]\)，其中 \(r_0\) 可学习；
  3. 用**高斯软分配**将频谱聚合为 \(K\) 个径向 bin，得到 \(R_k\)；
  4. 归一化并累加得到累积径向能量 \(C_k\)；
  5. 在可学习分位水平 \(p\) 下用**软分位**公式提取位置 \(f_p\)；
  6. 通过平滑下界反比映射将 \(f_p\) 转为无量纲分数 \(t\)：**边缘越细锐（高频集中）→ \(t\) 越小**；边缘越粗宽（低频主导）→ \(t\) 越大。

- **尺度校准与监督**：
  - 用 \(t_{pred}\) 校准深度 logits：\(D_{pred} = \bar{d}_{max} / (1+\exp(-Z/t_{pred}))\)；
  - 损失项：类别平衡交叉熵 \(L_{edge}\) + SQE 分数一致性 \(L_1 = |t_{pred} - t_{GT}|\) + 度量深度损失 \(L_{depth}\)（log 空间对齐）+ 边缘一致性 \(L_{MSE}\)（预测边缘与预测深度导出边缘的一致性）；
  - 总损失：\(L = 0.1 L_{edge} + L_1 + 100 L_{depth} + L_{MSE}\)。

- **主干**：以 Metric3D v2 为 MDE 模型，**移除其联合深度-法向优化模块**，替换为两个卷积预测器（初始深度 + 边缘图）。

## 3. 实验设计

### 3.1 数据集
- **训练集**：从 Metric3D v2 的数据源中选取子集，包括 DDAD、DIML、Cityscapes、Mapillary Planet-Scale Depth、Virtual KITTI、Matterport3D、Taskonomy、DSEC、Hypersim，**总量上限 4M RGB-D 对**。
- **边缘监督专用集**：仅使用 Virtual KITTI 与 Hypersim（因稠密可靠深度才能生成稳健的深度导出边缘）。
- **零样本评测**：NYUv2、KITTI、DIODE、iBIMS-1、ETH3D（共 6 个基准，涵盖室内/室外）。
- **微调（in-domain）评测**：NYUv2、KITTI。

### 3.2 对比方法
Adabins、NewCRFs、ZoeDepth、UniDepthV2、Depth Pro、Metric3D v2、IEBins、Depth Anything V2 等 SOTA 方法，主干统一为 DINOv2-L 或 Swin-L / BEiT-L。

### 3.3 评测指标
A.Rel↓、RMS↓、Log10↓、RMS log↓、δ1/δ2/δ3↑。

## 4. 资源与算力

- **GPU**：8× NVIDIA A100。
- **训练时长**：完整训练在 **4 天内**完成。
- **优化设置**：AdamW，batch size 16，基础学习率 1e-4（编码器乘 0.01），多项式学习率衰减至 0，**1e6 次迭代**。
- **预训练**：ViT-L 编码器来自 Metric3D v2，DPT 解码器重新初始化。
- **消融实验**：在 1M 样本、1e5 次迭代、batch size 16 的缩小设定下进行，以控制成本。

## 5. 实验数量与充分性

- **组数概览**：
  - 零样本评测：6 个未见基准 × 多方法对比（表 1）；
  - 域内微调：NYUv2 + KITTI 两个数据集（表 2）；
  - 消融实验：4 组变体（w/o SQE、w/o Ledge & LMSE、w/o L1、w/o LMSE）（表 3）；
  - 尺度相关性分析：约 30 张/相机设置、约 10⁶ 样本的幂律回归与 Pearson 相关性分析（图 4）；
  - 定性对比：4 个数据集上的可视化（图 3）。
- **充分性与公平性**：
  - 对比方法覆盖了零样本 MMDE、相对深度、单数据集 SOTA 等主流路线，主干对齐（DINOv2-L），比较基本公平。
  - 为公平对比 Metric3D v2，**仅使用其子训练集且不使用相机参数与表面法向标注**，条件更为苛刻。
  - 消融实验揭示了各模块贡献，但对 SQE 内部超参（K、p、λ、α、β 等）的敏感性分析未展开，可进一步补充。

## 6. 主要结论与发现

- **零样本性能 SOTA**：在 iBIMS-1 上 A.Rel 降低 **53.0%**、RMS 降低 **41.9%**；ETH3D 与 KITTI 上 RMS 分别降低 **49.3%** 与 **28.3%**。
- **域内微调 SOTA**：相比 IEBins，NYUv2 A.Rel 降低 49.4%、KITTI 降低 30.0%；相比 Depth Anything V2，NYUv2 A.Rel 降低 21.4%、KITTI 降低 22.2%；δ1 在两个数据集上均取得最佳。
- **尺度线索有效性**：边缘分数 \(t_{pred}\) 与归一化焦距 \(f_x/W\) 及场景最大深度 \(d_{max}\) 呈强线性相关（Pearson ≈ 0.698），说明其能同时捕捉**相机设置与场景尺度**两类因素。
- **消融结论**：去除 SQE 导致零样本泛化崩溃（δ1 从 0.604 降至 0.251，A.Rel 上升 126%）；去除边缘监督也显著退化；\(L_1\) 与 \(L_{MSE}\) 带来边际但一致的提升。
- **定性结论**：相比 Metric3D v2 更锐利、相比 Depth Pro 全局一致性更好、相比 UniDepthV2 在细薄结构上更完整。

## 7. 优点

- **新线索**：首次将**深度导出边缘的频谱分位**作为零样本 MMDE 的尺度代理，避免了对相机内参或焦距预测模块的依赖。
- **物理可解释性**：SQE 设计有明确物理动机——焦距变化改变边缘粗细与频率能量分布，可微分、可端到端学习。
- **监督信号干净**：使用**深度导出边缘**（而非 RGB 边缘）作为监督，避免高频纹理噪声，并缓解深度标签在边缘处缺失/不完整带来的伪影。
- **一举两得**：边缘预测既用于度量尺度校准，又用于边界锐化，训练目标设计紧凑。
- **公平且严格**：在 Metric3D v2 子集上训练、不使用相机参数与法向标注，仍取得 SOTA，说服力较强。

## 8. 不足与局限

- **训练数据依赖**：边缘监督仅使用 Virtual KITTI 与 Hypersim 两个**合成数据集**，向真实数据的迁移能力与分布偏差值得进一步验证。
- **对深度标签质量敏感**：深度到边缘变换要求稠密可靠深度，稀疏 LiDAR 或噪声标注下边缘目标可能不可靠。
- **场景覆盖限制**：训练池限制为 4M 对，未验证在更大规模或极端场景（如透明物体、反光面、夜间）下的表现。
- **个别指标非最优**：在 ETH3D 上 A.Rel 略逊于 UniDepthV2（0.277 vs 0.256）；在 DIODE 室内 RMS 略高于 Metric3D v2（0.400 vs 0.389），说明并非全面占优。
- **推理开销未充分讨论**：SQE 需要在频域计算，论文未报告推理延迟、显存占用与实时性对比。
- **超参敏感性未系统研究**：SQE 中 \(K, p, \lambda, \alpha, \beta, r_0\) 等超参的影响未做深入分析。
- **失败案例缺失**：论文未给出明确的失败模式分析，例如极端尺度变化或纹理稀疏场景下的表现。

（完）
