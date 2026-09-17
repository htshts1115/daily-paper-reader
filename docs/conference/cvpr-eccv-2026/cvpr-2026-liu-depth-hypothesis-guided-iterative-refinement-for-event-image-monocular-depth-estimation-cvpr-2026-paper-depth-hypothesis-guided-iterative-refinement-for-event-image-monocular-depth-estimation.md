---
title: Depth Hypothesis Guided Iterative Refinement for Event-Image Monocular Depth Estimation
title_zh: 面向事件图像单目深度估计的深度假设引导迭代精化
authors: "Liu, Daikun, Wang, Teng, Sun, Changyin"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Depth_Hypothesis_Guided_Iterative_Refinement_for_Event-Image_Monocular_Depth_Estimation_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 事件图像单目深度估计，深度假设引导迭代精化
tldr: 事件相机具备优异动态特性，但现有单目深度估计方法多依赖上下文特征优化，仍难以应对直接全深度回归的病态与非线性问题。本文提出HypoDepth，首次构建事件图像单目深度迭代精化框架：通过离散深度假设体将回归转化为受约束的深度搜索，并利用三维代价体与多尺度相关搜索引导稳定的残差优化。该轻量代价体带来稳定的精度提升，为事件图像深度估计提供了新的求解思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-depth-hypothesis-guided-iterative-refinement-for-event-image-monocular-depth-estimation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 737, \"height\": 565}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-depth-hypothesis-guided-iterative-refinement-for-event-image-monocular-depth-estimation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 454, \"height\": 344}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-depth-hypothesis-guided-iterative-refinement-for-event-image-monocular-depth-estimation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 515, \"height\": 268}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-depth-hypothesis-guided-iterative-refinement-for-event-image-monocular-depth-estimation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 641, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-depth-hypothesis-guided-iterative-refinement-for-event-image-monocular-depth-estimation-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 640, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-depth-hypothesis-guided-iterative-refinement-for-event-image-monocular-depth-estimation-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 640, \"height\": 320}]"
motivation: 事件相机用于单目深度估计时，直接全深度回归存在病态与非线性难题。
method: 提出HypoDepth，构建离散深度假设体，将回归转为约束深度搜索，用多尺度相关搜索引导残差优化。
result: 作为首个事件图像单目深度迭代精化框架，在深度估计精度上取得稳定提升。
conclusion: 以轻量代价体实现稳定深度优化，为事件单目深度估计提供新范式。
---

## Abstract
Event cameras hold excellent dynamic properties, showing great potential for monocular depth estimation (MDE). However, existing methods mainly improve performance by optimizing contextual features, but still struggle with the ill-posed and nonlinear nature of direct full-depth regression. In this paper, we propose HypoDepth, the first event-image monocular depth iterative refinement framework. By introducing a discrete Depth Hypothesis Volume (DHV), we transform the depth regression problem into a constrained depth search task. Specifically, we construct a 3D cost volume between the DHV features and contextual features and perform a multi-scale correlation search to guide stable residual optimization. This lightweight cost volume enables efficient global-to-local refinement across multi-resolution. Our method outperforms existing approaches on DSEC and MVSEC with state-of-the-art results and strong zero-shot generalization. Meanwhile, our tiny model achieves an excellent balance between accuracy and efficiency, enabling real-time performance on resource-limited devices.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：单目深度估计（MDE）是三维场景理解的基础任务，但纯图像方法在高速运动、低光照等条件下容易失效。事件相机具有高时间分辨率和高动态范围，适合捕捉动态场景变化，但在静态区域缺乏视觉信息，难以单独恢复静态结构。
- **现有方法局限**：已有事件–图像融合方法主要致力于跨模态对齐、融合和上下文特征优化，例如 RAMNet、UniCT、SRFNet、PCDepth 等，但大多仍采用直接全深度回归。由于单目深度估计本身病态且高度非线性，直接回归完整深度分布难以稳定收敛。
- **论文整体含义**：本文提出 **HypoDepth**，被作者称为首个事件–图像单目深度迭代精化框架。其核心是把病态的深度回归问题转化为受约束的深度搜索任务：通过离散 **Depth Hypothesis Volume（DHV）** 约束解空间，再借助三维代价体和多尺度相关搜索引导残差优化，从而提升精度、泛化性和效率。

## 2. 方法论

### 2.1 核心思想

- 受 RAFT 在光流估计中“代价体 + 迭代残差”范式启发，Hyp
