---
title: "QSCA: Quantization with Self-Compensating Auxiliary for Monocular Depth Estimation"
title_zh: QSCA：面向单目深度估计的自补偿辅助量化
authors: "Jincheol Yang, Jaemin Choi, Matti Alexander Zinke, Suk-Ju Kang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=CGReBdzOdP"
tags: ["query:mono-depth"]
score: 9.0
evidence: 面向资源受限设备的单目深度模型4比特训练后量化
tldr: 以Depth Anything为代表的单目深度基础模型泛化能力强，但计算与内存开销大，难以部署到资源受限设备。本文提出QSCA框架，针对单目深度模型进行4比特训练后量化，并引入自补偿辅助机制，在无需大量标注重训练的情况下平衡效率与精度。该方法为移动端轻量化深度模型的落地提供了可行方案，推动了深度基础模型在端侧的实用化。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 深度基础模型如Depth Anything泛化强但计算内存开销大，难以部署于资源受限设备。
method: 提出QSCA框架，对单目深度估计模型进行4比特训练后量化，并引入自补偿辅助机制。
result: 该方法在无需大量标注重训练的前提下平衡了效率与精度，实现了深度模型的轻量化部署。
conclusion: 自补偿量化方案为单目深度基础模型在移动端等资源受限设备上的落地提供了有效途径。
---

## Abstract
Monocular depth estimation has advanced significantly with foundation models like Depth Anything, leveraging large-scale transformer architectures for the superior generalization. 
However, the deployment on resource-constrained devices remains challenging due to the high computation and memory requirement. 
Existing quantization methods, such as post-training quantization and quantization-aware training, often face trade-offs between efficiency and accuracy, or require extensive labeled data for retraining.
To address these limitations, we propose Quantization with Self-Compensating Auxiliary for Monocular Depth Estimation (QSCA), a novel framework for 4-bit post-training quantization of Monocular depth estimation models. 
Our method integrates a lightweight Self-Compensating Auxiliary (SCA) module into both transformer encoder and decoder blocks, enabling the quantized model to recover from performance degradation without requiring ground truth.
This design enables fast adaptation while preserving structural and spatial consistency in predicted depth maps.
To our knowledge, this is the first framework to successfully apply 4-bit quantization across all layers of large-scale monocular depth estimation models.
Experimental results demonstrate that QSCA significantly improves quantized depth estimation performance. On the NYUv2 dataset, it achieves an 11\% improvement in $\delta_1$ accuracy over existing post-training quantization methods.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向资源受限设备的单目深度模型4比特训练后量化。

### 2. 核心内容
以Depth Anything为代表的单目深度基础模型泛化能力强，但计算与内存开销大，难以部署到资源受限设备。本文提出QSCA框架，针对单目深度模型进行4比特训练后量化，并引入自补偿辅助机制，在无需大量标注重训练的情况下平衡效率与精度。该方法为移动端轻量化深度模型的落地提供了可行方案，推动了深度基础模型在端侧的实用化。

### 3. 对应检索需求
lightweight depth model for mobile devices。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=CGReBdzOdP](https://openreview.net/forum?id=CGReBdzOdP)
