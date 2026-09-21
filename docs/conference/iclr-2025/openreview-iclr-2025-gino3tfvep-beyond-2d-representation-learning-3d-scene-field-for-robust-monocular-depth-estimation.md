---
title: "Beyond 2D Representation: Learning 3D Scene Field for Robust Monocular Depth Estimation"
title_zh: 超越二维表示：学习三维场景场实现鲁棒单目深度估计
authors: "Haifeng Wu, Shuhang Gu, Lixin Duan, Wen Li"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=gINO3tfVEP"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于三维场景场表示的鲁棒单目深度估计
tldr: 单目深度估计在反射、阴影遮挡和低纹理等真实场景中仍不稳定，现有方法多依赖前视二维特征，容易产生不连续、不完整或前后不一致的深度图。本文提出基于三维场景场表示的自监督单目深度估计框架，用更强的三维表示来刻画复杂物理因素。实验表明该方法在困难场景下能获得更鲁棒、更一致的深度结果。该工作为移动端人像虚化和主体背景层次判断提供了更可靠的深度基础。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 现有单目深度估计依赖前视二维特征，难以应对反射、阴影遮挡和低纹理区域。
method: 提出基于三维场景场表示的自监督单目深度估计框架。
result: 在复杂真实场景下获得更鲁棒、更一致的深度图。
conclusion: 为移动端人像虚化等应用提供更可靠的深度估计基础。
---

## Abstract
Monocular depth estimation has been extensively studied over the past few decades, yet achieving robust depth estimation in real-world scenes remains a challenge, particularly in the presence of reflections, shadow occlusions, and low-texture regions. Existing methods typically rely on extracting front-view 2D features for depth estimation, which often fail to capture those complex physical factors present in real-world scenes, leading to discontinuous, incomplete, or inconsistent depth maps. To address these issues, we turn to learning a more powerful 3D representation for robust monocular depth estimation, and propose a novel self-supervised monocular depth estimation framework based on the Three-dimensional Scene Field  representation, or TSF-Depth for short. Specifically, we build our TSF-Depth framework upon an encoder-decoder architecture. The encoder extracts scene features from the input 2D image, and subsequently reshapes it as a tri-plane feature field by incorporating scene prior encoding. This tri-plane feature field is designed to implicitly model the structure and appearance of the continuous 3D scene. We then estimate a high-quality depth map from the tri-plane feature field by simulating the camera imaging process. To do this, we construct a 2D feature map with 3D geometry by sampling from the tri-plane feature field using the coordinates of points where the line of sight intersects with the scene. The aggregated multi-view geometric features are subsequently fed into the decoder for depth estimation. Extensive experiments on KITTI and NYUv2 datasets show that TSF-Depth achieves state-of-the-art performance. We also validate the generalization capability of our model on Make3D and ScanNet datasets.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于三维场景场表示的鲁棒单目深度估计。

### 2. 核心内容
单目深度估计在反射、阴影遮挡和低纹理等真实场景中仍不稳定，现有方法多依赖前视二维特征，容易产生不连续、不完整或前后不一致的深度图。本文提出基于三维场景场表示的自监督单目深度估计框架，用更强的三维表示来刻画复杂物理因素。实验表明该方法在困难场景下能获得更鲁棒、更一致的深度结果。该工作为移动端人像虚化和主体背景层次判断提供了更可靠的深度基础。

### 3. 对应检索需求
Papers central to 单目深度估计，用于人像虚化、主体背景层次、手持物和头戴物深度判断。, especially work that connects or combines: monocular depth estimation; relative depth prediction; metric depth estimation; zero-shot depth estimation; depth foundation model; Depth Anything model; monocular depth estimation for portrait bokeh and mobile photography; lightweight depth model for mobile devices; monocular depth estimation for thin structures transparent objects and handheld objects; depth foundation model for zero shot generalization in real world images.

### 4. 来源与原文
- Source：ICLR-2025-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=gINO3tfVEP](https://openreview.net/forum?id=gINO3tfVEP)
