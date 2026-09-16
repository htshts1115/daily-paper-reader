---
title: "Distil-E2D: Distilling Image-to-Depth Priors for Event-Based Monocular Depth Estimation"
title_zh: Distil-E2D：为事件相机单目深度估计蒸馏图像到深度先验
authors: "Jie Long Lee, Gim Hee Lee"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=yFerzf9v1b"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于事件相机的单目深度估计，蒸馏图像深度先验
tldr: 事件相机适合在极端光照下做单目深度估计，但其监督信号依赖LiDAR标签，存在稀疏、空间不完整和伪影问题，不利于从稀疏事件学习稠密深度。本文提出Distil-E2D框架，利用同录的APS或RGB图像生成稠密合成伪标签，将图像域的深度先验蒸馏到事件域。该方法缓解了稀疏监督的缺陷，提升了事件域稠密深度估计质量。其意义在于为事件相机单目深度估计提供了更有效的监督范式。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 事件相机单目深度估计受限于LiDAR监督标签稀疏且不完整，难以从稀疏事件中学习稠密深度。
method: 提出Distil-E2D框架，利用同录APS或RGB图像生成稠密合成伪标签，将图像域深度先验蒸馏至事件域。
result: 通过稠密伪标签蒸馏，方法在挑战性光照下获得更完整、更准确的事件域稠密深度估计。
conclusion: 跨域深度先验蒸馏为事件相机稠密深度估计提供了更有效的监督方式。
---

## Abstract
Event cameras are neuromorphic vision sensors that asynchronously capture pixel-level intensity changes with high temporal resolution and dynamic range. These make them well suited for monocular depth estimation under challenging lighting conditions. However, progress in event-based monocular depth estimation remains constrained by the quality of supervision: LiDAR-based depth labels are inherently sparse, spatially incomplete, and prone to artifacts. Consequently, these signals are suboptimal for learning dense depth from sparse events. To address this problem, we propose Distil-E2D, a framework that distills depth priors from the image domain into the event domain by generating dense synthetic pseudolabels from co-recorded APS or RGB frames using foundational depth models. These pseudolabels complement sparse LiDAR depths with dense semantically rich supervision informed by large-scale image-depth datasets. To reconcile discrepancies between synthetic and real depths, we introduce a Confidence-Guided Calibrated Depth Loss that learns nonlinear depth alignment and adaptively weights supervision by alignment confidence. Additionally, our architecture integrates past predictions via a Context Transformer and employs a Dual-Decoder Training scheme that enhances encoder representations by jointly learning metric and relative depth abstractions. Experiments on benchmark datasets show that Distil-E2D achieves state-of-the-art performance in event-based monocular depth estimation across both event-only and event+APS settings.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于事件相机的单目深度估计，蒸馏图像深度先验。

### 2. 核心内容
事件相机适合在极端光照下做单目深度估计，但其监督信号依赖LiDAR标签，存在稀疏、空间不完整和伪影问题，不利于从稀疏事件学习稠密深度。本文提出Distil-E2D框架，利用同录的APS或RGB图像生成稠密合成伪标签，将图像域的深度先验蒸馏到事件域。该方法缓解了稀疏监督的缺陷，提升了事件域稠密深度估计质量。其意义在于为事件相机单目深度估计提供了更有效的监督范式。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=yFerzf9v1b](https://openreview.net/forum?id=yFerzf9v1b)
