---
title: "One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models"
title_zh: 一景两深：探究单目基础模型中的几何歧义
authors: "Xiaohao Xu, Feng Xue, Xiang Li, Haowei Li, Shusheng Yang, Tianyi Zhang, Matthew Johnson-Roberson, Xiaonan Huang"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/118.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 透明多层场景下的单目深度歧义
tldr: 单目深度估计将一条光线上的多层可见表面压缩为每像素单一标量，透明场景使这一歧义可被度量。本文提出MultiDepth-3k稀疏双层序数基准，衡量深度层偏好与多层空间关系精度。实验揭示主流单目基础模型的深度层选择源于标注与训练约定而非场景内在真值，为理解与改进单目深度模型提供新视角。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 526, \"height\": 982}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1098, \"height\": 523}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 619, \"height\": 469}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 597, \"height\": 709}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 365, \"height\": 712}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 614, \"height\": 469}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1221, \"height\": 701}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-008.webp\", \"caption\": \"\", \"page\": 3, \"index\": 8, \"width\": 2576, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-009.webp\", \"caption\": \"\", \"page\": 3, \"index\": 9, \"width\": 2072, \"height\": 644}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-010.webp\", \"caption\": \"\", \"page\": 3, \"index\": 10, \"width\": 2072, \"height\": 644}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-011.webp\", \"caption\": \"\", \"page\": 3, \"index\": 11, \"width\": 2576, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-012.webp\", \"caption\": \"\", \"page\": 3, \"index\": 12, \"width\": 1536, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-013.webp\", \"caption\": \"\", \"page\": 3, \"index\": 13, \"width\": 1536, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-014.webp\", \"caption\": \"\", \"page\": 3, \"index\": 14, \"width\": 1536, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-015.webp\", \"caption\": \"\", \"page\": 3, \"index\": 15, \"width\": 2304, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 2304, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 2304, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 2576, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-019.webp\", \"caption\": \"\", \"page\": 3, \"index\": 19, \"width\": 638, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-020.webp\", \"caption\": \"\", \"page\": 3, \"index\": 20, \"width\": 383, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-021.webp\", \"caption\": \"\", \"page\": 3, \"index\": 21, \"width\": 574, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-022.webp\", \"caption\": \"\", \"page\": 3, \"index\": 22, \"width\": 2576, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 3700, \"height\": 742}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 3700, \"height\": 742}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 3700, \"height\": 742}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-026.webp\", \"caption\": \"\", \"page\": 7, \"index\": 26, \"width\": 3700, \"height\": 742}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-027.webp\", \"caption\": \"\", \"page\": 7, \"index\": 27, \"width\": 1512, \"height\": 902}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-028.webp\", \"caption\": \"\", \"page\": 7, \"index\": 28, \"width\": 1004, \"height\": 992}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 500, \"height\": 430}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 500, \"height\": 430}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-031.webp\", \"caption\": \"\", \"page\": 12, \"index\": 31, \"width\": 324, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-032.webp\", \"caption\": \"\", \"page\": 12, \"index\": 32, \"width\": 324, \"height\": 404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-033.webp\", \"caption\": \"\", \"page\": 12, \"index\": 33, \"width\": 330, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-034.webp\", \"caption\": \"\", \"page\": 12, \"index\": 34, \"width\": 330, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-035.webp\", \"caption\": \"\", \"page\": 12, \"index\": 35, \"width\": 330, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-036.webp\", \"caption\": \"\", \"page\": 12, \"index\": 36, \"width\": 324, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-037.webp\", \"caption\": \"\", \"page\": 12, \"index\": 37, \"width\": 324, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-038.webp\", \"caption\": \"\", \"page\": 12, \"index\": 38, \"width\": 324, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-039.webp\", \"caption\": \"\", \"page\": 12, \"index\": 39, \"width\": 334, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-040.webp\", \"caption\": \"\", \"page\": 12, \"index\": 40, \"width\": 323, \"height\": 409}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-041.webp\", \"caption\": \"\", \"page\": 12, \"index\": 41, \"width\": 334, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-042.webp\", \"caption\": \"\", \"page\": 12, \"index\": 42, \"width\": 334, \"height\": 404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-043.webp\", \"caption\": \"\", \"page\": 15, \"index\": 43, \"width\": 643, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-044.webp\", \"caption\": \"\", \"page\": 15, \"index\": 44, \"width\": 1287, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-045.webp\", \"caption\": \"\", \"page\": 15, \"index\": 45, \"width\": 1287, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-046.webp\", \"caption\": \"\", \"page\": 15, \"index\": 46, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-047.webp\", \"caption\": \"\", \"page\": 15, \"index\": 47, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-048.webp\", \"caption\": \"\", \"page\": 15, \"index\": 48, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-049.webp\", \"caption\": \"\", \"page\": 15, \"index\": 49, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-050.webp\", \"caption\": \"\", \"page\": 15, \"index\": 50, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-051.webp\", \"caption\": \"\", \"page\": 15, \"index\": 51, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-052.webp\", \"caption\": \"\", \"page\": 15, \"index\": 52, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-053.webp\", \"caption\": \"\", \"page\": 15, \"index\": 53, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-054.webp\", \"caption\": \"\", \"page\": 15, \"index\": 54, \"width\": 622, \"height\": 358}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-055.webp\", \"caption\": \"\", \"page\": 15, \"index\": 55, \"width\": 643, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-056.webp\", \"caption\": \"\", \"page\": 15, \"index\": 56, \"width\": 1287, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-057.webp\", \"caption\": \"\", \"page\": 15, \"index\": 57, \"width\": 1287, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-058.webp\", \"caption\": \"\", \"page\": 15, \"index\": 58, \"width\": 500, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-059.webp\", \"caption\": \"\", \"page\": 15, \"index\": 59, \"width\": 812, \"height\": 538}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-060.webp\", \"caption\": \"\", \"page\": 15, \"index\": 60, \"width\": 812, \"height\": 538}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-061.webp\", \"caption\": \"\", \"page\": 15, \"index\": 61, \"width\": 500, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-062.webp\", \"caption\": \"\", \"page\": 15, \"index\": 62, \"width\": 1350, \"height\": 820}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-063.webp\", \"caption\": \"\", \"page\": 15, \"index\": 63, \"width\": 972, \"height\": 590}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-064.webp\", \"caption\": \"\", \"page\": 15, \"index\": 64, \"width\": 972, \"height\": 590}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-065.webp\", \"caption\": \"\", \"page\": 15, \"index\": 65, \"width\": 972, \"height\": 590}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-066.webp\", \"caption\": \"\", \"page\": 15, \"index\": 66, \"width\": 490, \"height\": 487}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-067.webp\", \"caption\": \"\", \"page\": 15, \"index\": 67, \"width\": 490, \"height\": 487}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-068.webp\", \"caption\": \"\", \"page\": 15, \"index\": 68, \"width\": 490, \"height\": 487}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-069.webp\", \"caption\": \"\", \"page\": 15, \"index\": 69, \"width\": 490, \"height\": 487}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-070.webp\", \"caption\": \"\", \"page\": 15, \"index\": 70, \"width\": 800, \"height\": 622}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-071.webp\", \"caption\": \"\", \"page\": 15, \"index\": 71, \"width\": 800, \"height\": 622}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-072.webp\", \"caption\": \"\", \"page\": 15, \"index\": 72, \"width\": 800, \"height\": 622}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-073.webp\", \"caption\": \"\", \"page\": 15, \"index\": 73, \"width\": 800, \"height\": 622}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-074.webp\", \"caption\": \"\", \"page\": 15, \"index\": 74, \"width\": 500, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-075.webp\", \"caption\": \"\", \"page\": 15, \"index\": 75, \"width\": 500, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-076.webp\", \"caption\": \"\", \"page\": 15, \"index\": 76, \"width\": 1207, \"height\": 800}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-a3860a3c8480c7679496abef/fig-077.webp\", \"caption\": \"\", \"page\": 15, \"index\": 77, \"width\": 812, \"height\": 538}]"
motivation: 单目深度估计把多层可见几何压缩为每像素单一标量，透明场景暴露其监督约定问题。
method: 构建MultiDepth-3k稀疏双层序数基准，度量深度层偏好与多层空间关系精度。
result: 实验显示主流单目基础模型的深度层选择反映标注与训练约定而非场景真值。
conclusion: 为理解并改进单目基础模型的几何歧义提供诊断基准与视角。
---

## Abstract
A faithful 3D world representation should account for layeredgeometry, where a single camera ray may contain multiple visible and ge-ometrically valid surfaces. Monocular depth estimation, however, reducesthis structure to one scalar depth per pixel. Transparent scenes makethis ambiguity measurable: the same ray can pass through foregroundglass and observe the background, turning the supervised target into aconvention of annotation, data, and training rather than a scene-intrinsictruth. A learned predictor exposes this convention as its depth-layerpreference. We introduce MultiDepth-3k (MD-3k), a sparse two-layer or-dinal benchmark for measuring depth-layer preference and multi-layerspatial relationship accuracy (ML-SRA). On MD-3k, leading depth foun-dation models exhibit diverse layer preferences under standard RGBinput, showing that the same layered geometry can be resolved differentlyacross models. We further find that Laplacian Visual Prompting (LVP),a training-free spectral input transformation, can substantially changethe reported layer for certain frozen models. The strongest RGB/LVPpair, DAv2-L, reaches 75.5% ML-SRA. These results suggest that depthfoundation models may express complementary geometric hypotheses thatstandard RGB inference leaves unexpressed. We invite the community torethink depth supervision and evaluation through an ambiguity-awarelens, where multiple valid 3D interpretations are treated as geometricstructure to be measured, preserved, and expressed.

---

## 论文详细总结（自动生成）

# 论文总结：One Scene, Two Depths: Probing Geometric Ambiguity in Monocular Foundation Models

## 1. 核心问题与整体含义

- **核心问题**：单目深度估计通常将图像映射为“每像素一个深度值”，但真实场景中一条相机光线可能穿过透明前景并看到背景，因此同一像素对应多个几何上有效的可见表面。论文研究这种**多层几何歧义**下，深度基础模型实际表达的是哪一层深度，以及这种选择能否被输入变换调制。
- **研究动机**：透明场景把歧义显式化。监督标签不再是场景内在唯一真值，而是受标注约定、传感器差异、合成渲染规则和单深度训练目标共同塑造的“层约定”。例如超声可能返回近处玻璃，LiDAR 可能穿透或错过透明表面，合成数据依赖 alpha 合成与射线终止策略。
- **整体含义**：论文主张应把多个有效 3D 解释视为需要测量、保留和表达的几何结构，而不是噪声。标准 RGB 推理可能只暴露了模型几何后验中的一个切片。

## 2. 方法论

- **核心思想**：将透明场景视为受控的两层歧义案例，定义前景透明层 \(D^{(1)}\) 与可见背景层 \(D^{(2)}\)，满足 \(D^{(1)} \le D^{(2)}\)。用稀疏序数标签而非稠密度量深度，测量冻结单输出模型的“深度层偏好”，并测试 Laplacian Visual Prompting 是否能改变该偏好。
- **稀疏序数表示**：
  - 对每张图采样稀疏点对 \(P=\{(u_m,v_m)\}\)，人工标注两层各自的相对深度顺序：
    \[
    y_m^{(k)}=\mathrm{sign}(D^{(k)}(u_m)-D^{(k)}(v_m))
    \]
  - 预测深度 \(\hat D\) 若满足 \(\mathrm{sign}(\hat D(u_m)-\hat D(v_m))=y_m^{(k)}\)，则认为其在该点对上符合第 \(k\) 层。
- **深度层偏好 \(\alpha\)**：
  \[
  \alpha(f_\theta)=\mathbb E_m[I(\hat D\equiv y_m^{(2)})-I(\hat D\equiv y_m^{(1)})]
  \]
  - \(\alpha>0\)：偏好背景层；\(\alpha<0\)：偏好前景层；\(|\alpha|\) 表示偏好强度。
- **配对假设互补性**：
  - 将两个深度输出 \(\{\hat D_A,\hat D_B\}\) 视为候选对，寻找一个数据集级全局排列 \(\pi^\star\)，最大化同时满足两层序数约束的点对数量。
  - 对应指标为 ML-SRA，即两层相对顺序都被正确预测的比例。
- **Laplacian Visual Prompting (LVP)**：
  - 对输入 RGB 图像逐通道做浮点卷积，使用离散 Laplacian 核：
    \[
    K_L=\begin{bmatrix}0&1&0\\1&-4&1\\0&1&0\end{bmatrix}
    \]
  - 得到有符号高频残差后，按通道做 min–max 归一化，映射回模型输入值范围，例如 uint8 的 [0,255]。
  - 将变换后的图像送入同一冻结模型，得到 LVP 条件深度假设 \(D_{\text{LVP}}=f_\theta(L(I))\)。
  - RGB 与 LVP 输出组成无序候选对，通过 benchmark 标签选择一个全局层分配 \(\pi^\star\)，不进行逐图 oracle 选择。

## 3. 实验设计

- **数据集 / 场景**：
  - 提出 **MultiDepth-3k (MD-3k)**：来自 GDD 数据集的 3,161 张真实透明场景 RGB 图像，每图一对稀疏点，标注两层序数关系。
  - 子集划分：
    - **Same 子集**：1,783 对，两层相对顺序一致。
    - **Reverse 子集**：1,378 对，两层相对顺序冲突。单输出模型若复制同一深度图，无法同时满足两层。
  - 使用 **DA-2K** 作为非歧义参考基准。
- **评价指标**：
  - **SRA(1)/SRA(2)**：分别对前景层、背景层的空间关系准确率。
  - **\(\alpha\)**：深度层偏好方向与强度。
  - **ML-SRA**：两层序数关系同时正确的比例。
  - 定义 **Ideal Collapsed Baseline**：完美预测单层并复制为两层，在 Same 上 100%，Reverse 上 0%，加权总体为 56.4%。
- **对比方法**：
  - 判别式模型：DPT、ZoeDepth。
  - 生成式模型：Marigold、GeoWizard。
  - 度量估计模型：Depth Pro、UniK3D-L、UniDepth-v2-L。
  - Depth Anything 系列：DAv1-S/B/L、DAv2-S/B/L、DAv2-Indoor-S/B/L、DAv2-Outdoor-S/B/L。
- **主要实验类型**：
  - RGB 输入下的单层偏好与 per-layer SRA。
  - RGB/LVP 候选对的 ML-SRA。
  - 缩放效应分析：模型规模对互补性与稳定性的影响。
  - Prompt 消融：Laplacian vs Gaussian、Sobel、Fourier、Wavelet。
  - LVP 变体：8 邻域核、符号翻转、灰度输入。
  - 语义先验对比：mask interpolation 与 LVP。
  - 下游定性应用：ControlNet 条件生成、视频逐帧 RGB/LVP 深度流。
  - 泛化与失败案例：曲面玻璃、半透明表面。

## 4. 资源与算力

- 论文明确说明所有评估均为**严格训练免费**，冻结预训练模型权重，只做推理与输入变换。
- 文中未给出具体 GPU 型号、数量、训练时长或推理总算力。
- 仅在致谢中提到 **Modal Labs** 提供部分学术计算资助。
- 因此，本文自身的计算资源细节不透明；基础模型的预训练算力也未在本文范围内说明。

## 5. 实验数量与充分性

- **实验规模**：
  - 主表覆盖约 20 个模型在 MD-3k Overall/Reverse/Same 及 DA-2K 上的 RGB 与 LVP 结果。
  - ML-SRA 表覆盖约 19 个模型的 RGB/LVP 候选对。
  - 消融包括：16 个模型的 Laplacian vs Gaussian；3 个 DAv2 模型上的 Sobel/Fourier/Wavelet；LVP 核变体、符号、灰度；缩放分析；语义先验对比；下游定性案例。
- **充分性**：
  - 模型覆盖较广，涵盖生成式、判别式、度量式、域专用与通用深度基础模型。
  - 子集划分清晰，Reverse 子集专门检验单图无法同时满足冲突序数的情况。
  - 消融较系统，支持“高频强调”而非某一特定核函数是主要因素。
- **公平性与客观性**：
  - 所有模型冻结、训练免费，评测协议一致，具有较好可比性。
  - 但 ML-SRA 使用 benchmark 标签选择全局排列 \(\pi^\star\)，属于数据集级校准，不是自动逐实例层选择；实际部署仍需外部选择器或校准标签。
  - 语义先验对比中，LVP 使用 DAv2-L，而 mask interpolation 使用 DAv1-L，骨干不同，比较并非完全同条件。
  - MD-3k 每图仅一对点，稀疏序数标签统计噪声较大，且全部来自 GDD，域覆盖有限。

## 6. 主要结论与发现

- **深度层偏好是模型内在且异质的**：
  - 标准 RGB 输入下，不同深度基础模型对同一透明场景报告不同层。
  - DAv2 通用版和 Indoor 版更偏向前景透明层；DAv1、DAv2-Outdoor 及部分生成式模型更偏向背景层。
  - 这与训练数据混合、域偏差和监督约定有关，而非场景唯一真值。
- **LVP 可调制某些冻结模型的层偏好**：
  - LVP 对 DPT、Depth Pro、ZoeDepth、多个 DAv2 模型影响显著；对 DAv1、Marigold、GeoWizard 等影响较弱。
  - 典型例子：DAv2-L 在 Reverse 子集上从前景偏好转为背景偏好，SRA(1) 从 65.3% 降至 15.9%，SRA(2) 从 34.7% 升至 84.1%。
- **RGB/LVP 配对可提供互补几何假设**：
  - DAv2-L 的 RGB/LVP 对达到 **75.5% Overall ML
