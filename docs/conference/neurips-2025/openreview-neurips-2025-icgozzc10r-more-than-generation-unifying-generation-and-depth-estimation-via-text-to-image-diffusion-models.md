---
title: "More Than Generation: Unifying Generation and Depth Estimation via Text-to-Image Diffusion Models"
title_zh: 不止于生成：用文生图扩散模型统一图像生成与深度估计
authors: "Hongkai Lin, Dingkang Liang, Mingyang Du, Xin Zhou, Xiang Bai"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ICgOzZc10r"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于文生图扩散的零样本深度估计
tldr: 生成式深度估计借助预训练文生图扩散模型的视觉先验获得强零样本能力，但训练中的参数更新会严重破坏原有图像生成能力。本文提出MERGE，从固定参数的文生图模型出发，通过即插即用框架在生成与深度估计模式间无缝切换。方法在保持图像生成质量的同时实现高效深度估计，为统一生成与深度任务提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 训练深度模型会破坏预训练文生图模型的图像生成能力。
method: 提出MERGE即插即用框架，从固定参数文生图模型统一生成与深度估计模式。
result: 在保持生成质量的同时实现高效零样本深度估计。
conclusion: 证明文生图扩散模型可同时胜任生成与深度估计任务。
---

## Abstract
Generative depth estimation methods leverage the rich visual priors stored in pretrained text-to-image diffusion models, demonstrating astonishing zero-shot capability. However, parameter updates during training lead to catastrophic degradation in the image generation capability of the pretrained model. We introduce MERGE, a unified model for image generation and depth estimation, starting from a fixed-parameters pretrained text-to-image model. MERGE demonstrates that the pretrained text-to-image model can do more than image generation but also expand to depth estimation effortlessly. Specifically, MERGE introduces a plug-and-play framework that enables seamless switching between image generation and depth estimation modes through simple and pluggable converters. Meanwhile, we propose a Group Reuse Mechanism to encourage parameter reuse and improve the utilization of the additional learnable parameter. MERGE unleashes the powerful depth estimation capability of the pretrained text-to-image model while preserving its original image generation ability. Compared to other unified models for image generation and depth estimation, MERGE achieves state-of-the-art performance across multiple depth estimation benchmarks. The code and model will be made available.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于文生图扩散的零样本深度估计。

### 2. 核心内容
生成式深度估计借助预训练文生图扩散模型的视觉先验获得强零样本能力，但训练中的参数更新会严重破坏原有图像生成能力。本文提出MERGE，从固定参数的文生图模型出发，通过即插即用框架在生成与深度估计模式间无缝切换。方法在保持图像生成质量的同时实现高效深度估计，为统一生成与深度任务提供了新思路。

### 3. 对应检索需求
zero-shot depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=ICgOzZc10r](https://openreview.net/forum?id=ICgOzZc10r)
