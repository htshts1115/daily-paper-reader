---
title: "SeeGroup: Multi-Layer Depth Estimation of Transparent Surfaces via Self-Determined Grouping"
title_zh: SeeGroup：基于自确定分组透明表面的多层深度估计
authors: "Wen, Hongyu, Deng, Jia"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wen_SeeGroup_Multi-Layer_Depth_Estimation_of_Transparent_Surfaces_via_Self-Determined_Grouping_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 透明表面的多层深度估计
tldr: 透明物体在日常生活中常见，理解其多层深度（透明表面与后方物体）对交互应用至关重要，但现有深度方法只输出单张深度图，对透明表面存在固有歧义。本文提出SeeGroup，设计循环分解模块与基于强度的多层深度表达，实现多层深度估计。实验在LayeredDepth基准上显著超越现有方法，提升四元组相对深度精度。该工作推动了透明物体深度感知的发展。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 3, \"index\": 6, \"width\": 1140, \"height\": 1140}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 3, \"index\": 7, \"width\": 1140, \"height\": 1140}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 3, \"index\": 8, \"width\": 1140, \"height\": 1140}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 3, \"index\": 9, \"width\": 1140, \"height\": 1140}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 3390, \"height\": 1245}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 3390, \"height\": 1245}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 3390, \"height\": 1245}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 6, \"index\": 17, \"width\": 3390, \"height\": 1245}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 6, \"index\": 18, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 8, \"index\": 23, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 8, \"index\": 25, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 3390, \"height\": 810}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wen-seegroup-multi-layer-depth-estimation-of-transparent-surfaces-via-self-determined-grouping-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 3390, \"height\": 810}]"
motivation: 透明物体普遍存在，但现有深度方法只输出单层深度图，对透明表面本质上是模糊的。
method: 提出多层深度估计方法SeeGroup，设计循环分解模块与基于强度的多层深度公式。
result: 在LayeredDepth基准上显著提升多层深度估计性能，四元组相对深度精度达到新最优。
conclusion: 为透明表面及其后方物体的多层深度理解提供了有效方案。
---

## Abstract
Transparent objects are common in daily life, and understanding their multi-layer depth information, including both the transparent surface and the objects behind it, is crucial for real-world applications that interact with transparent materials.However, existing depth methods produce only a single depth map, which is inherently ambiguous for transparent surfaces.In this work, We propose a multi-layer depth estimation method, SeeGroup, consisting of novel recurrent decomposition module design and an intensity-based formulation for multi-layer depth. Experiments demonstrate that our method significantly improves the state of the art of multi-layer depth estimation, improving quadruplet relative depth accuracy on LayeredDepth benchmark from 61.34% to 70.09%.

---

## 论文详细总结（自动生成）

# SeeGroup 论文中文总结

## 1. 核心问题与整体含义

- **研究动机**：透明物体在日常生活和机器人、自动驾驶、3D 重建、抓取等场景中非常常见。透明表面会使同一像素对应的相机射线穿过多个表面，因此一个像素可能对应多个深度值，单张深度图对透明区域存在本质歧义。
- **现有方法局限**：
  - 一类方法把透明物体当作不透明物体，只预测第一层深度，即透明表面本身。
  - 另一类方法忽略透明表面，只预测后方背景几何。
  - 两者都无法同时表达“透明表面”和“其后方物体”，难以满足机器人既要避障又要感知容器/玻璃后方目标的需求。
- **任务定义**：论文研究多层深度估计。给定单张 RGB 图像，对每个像素预测一个深度递增序列，序列长度可随像素和场景变化；每个深度对应沿相机光轴方向的一个可见表面层。
- **关键问题**：如何把逐像素的多个深度值分组为多张深度图。传统“按深度排序分组”在复杂场景中可能把不同物体拼到同一层，导致几何和语义不连贯；更合理的方式可能是“物体中心分组”，但最佳分组高度依赖场景，甚至依赖图像区域。
- **整体含义**：论文提出 SeeGroup，让模型在推理时自行决定多层深度的分组顺序，而非预设固定排序，从而更灵活地表达透明物体及其后方结构。

## 2. 方法论

- **核心思想**：
  - 不直接回归固定顺序的多层深度，而是把每像素多层几何建模为“深度轴上的强度函数”。
  - 通过循环分解模块从图像特征中迭代分离出多个特征组件，每个组件对应一组深度层。
  - 每个组件映射为 Laplace 分布参数，整体强度函数为多个 Laplace 分量的最大值混合。
  - 训练损失对深度顺序置换不变，使模型可以自确定分组。

- **整体流程**：
  1. 使用 backbone encoder 提取特征图 \(F_0\)。
  2. 循环分解模块迭代生成 \(n\) 个组件特征 \(C_1, C_2, \dots, C_n\)。
  3. 每个 \(C_i\) 经预测器映射为 Laplace 参数：中心 \(d_i\) 和尺度 \(b_i\)。
  4. 构建逐像素深度强度函数 \(\Lambda(x)\)。
  5. 推理时在深度轴上检测峰值，得到多层深度，并排序为递增序列。

- **循环分解模块**：
  - 分解器 \(D\)：从当前残差特征 \(F_{i-1}\) 中提取组件 \(C_i = D(F_{i-1})\)，每个组件对应当前特征中最主导的一组深度层。
  - 重映射器 \(R\)：将组件 \(C_i\) 映射回特征空间，得到 \(R(C_i)\)。
  - 更新残差：\(F_i = F_{i-1} - \eta_i \cdot R(C_i)\)，其中 \(\eta_i\) 用于保持尺度一致。
  - 该过程逐步移除已被解释的信息，使后续组件关注剩余深度层。

- **强度函数参数化**：
  - 每个组件对应一个 Laplace 贡献：
    \[
    L_i(x)=\frac{1}{2b_i}\exp\left(-\frac{|x-d_i|}{b_i}\right)
    \]
  - 整体强度定义为最大混合：
    \[
    \Lambda(x)=\max_{i=1}^{n} L_i(x)
    \]
  - 相比加权混合，最大值混合会局部抑制次要分量，鼓励不同分量专注于不同深度范围，减少塌缩为单一宽峰。
  - \(\Lambda(x)\) 表示在深度 \(x\) 观察到表面的似然；峰值对应深度层，低谷表示不确定或无表面。

- **置换不变损失**：
  - 给定像素的真实深度集合 \(\{d_1,\dots,d_m\}\)，其似然近似正比于：
    \[
    \prod_{i=1}^{m}\Lambda(d_i)
    \]
  - 取负对数得到强度损失：
    \[
    L_{\text{int}}=-\sum_{i=1}^{m}\log \Lambda(d_i)
    =-\sum_{i=1}^{m}\log \max_{j=1}^{n} L_j(d_i)
    \]
  - 由于乘法可交换，该损失对深度顺序不敏感，允许模型自定顺序和分组。
  - 为防止过度预测额外分量，引入覆盖损失：
    \[
    L_{\text{cov}}=-\sum_{j=1}^{n}\log \max_{i=1}^{m} L_j(d_i)
    \]
  - 覆盖损失要求每个预测分量至少匹配一个真实深度，否则受到惩罚。
  - 总损失：
    \[
    L=\lambda_{\text{int}}L_{\text{int}}+\lambda_{\text{cov}}L_{\text{cov}}+\lambda_{\text{gm}}L_{\text{gm}}
    \]
    其中 \(L_{\text{gm}}\) 为梯度匹配损失，用于提升细节。训练时 \(\lambda_{\text{int}}=1.0,\lambda_{\text
