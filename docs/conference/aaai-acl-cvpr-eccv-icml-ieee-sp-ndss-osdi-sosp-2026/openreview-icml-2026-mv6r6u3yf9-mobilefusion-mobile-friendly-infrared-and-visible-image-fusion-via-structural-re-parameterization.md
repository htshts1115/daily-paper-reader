---
title: "MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization"
title_zh: MobileFusion：基于结构重参数化的移动端红外与可见光图像融合
authors: "Yufa Duan, Jialing Huang, Yingying Wang, Weimin Cai, Xinghao Ding, Xiaotong Tu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/3caaad4a4dc7d5ad2ae45da6f51a9303cf901da4.pdf"
tags: ["query:cv-render"]
score: 6.0
evidence: 资源受限下的移动端友好图像融合
tldr: 现有红外与可见光图像融合网络设计冗余，难以在算力受限的移动设备上实时部署。本文提出 MobileFusion，用可重参数化多分支卷积在训练时促进跨模态交互、推理时折叠为单路算子，并加入轻量注意力增强上下文。该方法在严格资源约束下实现高质量融合，为移动端图像融合与实时部署提供了高效方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有红外可见光融合网络冗余，难以在算力受限的移动设备上实时部署。
method: 提出可重参数化多分支卷积，训练时跨模态交互、推理时折叠为单路算子，并加轻量注意力。
result: 在严格资源约束下实现高质量融合并支持快速推理。
conclusion: 为移动端图像融合与实时部署提供了高效可用的方案。
---

## Abstract
Deep neural networks have recently advanced infrared and visible image fusion (IVIF), but most existing methods rely on sophisticated yet redundant designs, which hinder real-time deployment on mobile devices with limited compute and memory. In this paper, we present MobileFusion, an extremely lightweight and effective convolutional framework that achieves high-quality fusion under strict resource constraints. MobileFusion leverages a novel re-parameterizable multi-branch convolution module to promote cross-modal interactions during training while collapsing into a single-path operator for fast inference. It further incorporates a lightweight attention module to enhance context awareness, together with a re-parameterized feed-forward network to improve feature expressiveness. Extensive experiments demonstrate that MobileFusion delivers a favorable trade-off between fusion quality and computational efficiency, enabling real-time and high-quality IVIF on resource-constrained platforms. The source code is available at https://github.com/sucessfullys/MobileFusion.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
资源受限下的移动端友好图像融合。

### 2. 核心内容
现有红外与可见光图像融合网络设计冗余，难以在算力受限的移动设备上实时部署。本文提出 MobileFusion，用可重参数化多分支卷积在训练时促进跨模态交互、推理时折叠为单路算子，并加入轻量注意力增强上下文。该方法在严格资源约束下实现高质量融合，为移动端图像融合与实时部署提供了高效方案。

### 3. 对应检索需求
image fusion for mobile photography。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=Mv6r6u3Yf9](https://openreview.net/forum?id=Mv6r6u3Yf9)
