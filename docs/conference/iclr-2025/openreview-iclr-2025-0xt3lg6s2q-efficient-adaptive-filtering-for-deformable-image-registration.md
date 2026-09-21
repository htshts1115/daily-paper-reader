---
title: Efficient Adaptive Filtering for Deformable Image registration
title_zh: 面向可变形图像配准的高效自适应滤波
authors: "Renjiu Hu, Xiang Chen, Jiacheng Wang, Gaolei Li, Noel C Codella, Hang Zhang"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=0XT3Lg6S2Q"
tags: ["query:cv-render"]
score: 5.0
evidence: 可微双边网格实现高效保边滤波
tldr: 针对学习式医学配准计算量大的问题，论文提出AdaWarp模块，利用可微双边网格对形变场进行保边低频近似，以低分辨率数据结构逼近全分辨率结果。该模块包含编码器、引导图生成器与双边网格，在保持精度的同时显著降低计算复杂度。其高效保边滤波思想可迁移到计算摄影中的快速图像滤波与模糊渲染。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 学习式配准计算代价高，低分辨率数据结构的物理先验尚未被充分利用。
method: 提出AdaWarp模块，由编码器、引导图生成器和可微双边网格组成，实现保边低频形变近似。
result: 在保持配准精度的同时显著降低计算复杂度，减少低分辨率近似误差。
conclusion: 验证了可微双边网格在高效保边滤波上的价值，可迁移至图像滤波任务。
---

## Abstract
In medical image registration, where targets exhibit piecewise smooth structures, a carefully designed low-resolution data structure can effectively approximate full-resolution deformation fields with minimal accuracy loss. 
Although this physical prior has proven effective in traditional registration algorithms, it remains underexplored in current learning-based registration literature.
In this paper, we propose AdaWarp, a novel neural network module that leverages this prior for efficient and accurate medical image registration. 
AdaWarp comprises an encoder, a guidance map generator, and a differentiable bilateral grid, enabling an edge-preserving low-frequency approximation of the deformation field. 
This design reduces computational complexity with low-resolution feature maps while increasing the effective receptive field, achieving a balanced trade-off between registration accuracy and efficiency.
Experiments on two registration datasets covering different modalities and input constraints demonstrate that AdaWarp outperforms existing methods in accuracy-efficiency and accuracy-smoothness tradeoffs.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
可微双边网格实现高效保边滤波。

### 2. 核心内容
针对学习式医学配准计算量大的问题，论文提出AdaWarp模块，利用可微双边网格对形变场进行保边低频近似，以低分辨率数据结构逼近全分辨率结果。该模块包含编码器、引导图生成器与双边网格，在保持精度的同时显著降低计算复杂度。其高效保边滤波思想可迁移到计算摄影中的快速图像滤波与模糊渲染。

### 3. 对应检索需求
efficient image filtering。

### 4. 来源与原文
- Source：ICLR-2025-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=0XT3Lg6S2Q](https://openreview.net/forum?id=0XT3Lg6S2Q)
