---
title: Repurposing Marigold for Zero-Shot Metric Depth Estimation via Defocus Blur Cues
title_zh: 利用散焦模糊线索将Marigold改造为零样本度量深度估计器
authors: "Chinmay Talegaonkar, Nikhil Gandudi Suresh, Zachary Novack, Yash Belhe, Priyanka Nagasamudra, Nicholas Antipa"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=imO353Gyrl"
tags: ["query:mono-depth"]
score: 9.0
evidence: 利用散焦模糊线索的零样本度量深度估计
tldr: 现有单目度量深度估计方法在零样本泛化上虽有进展，但在分布外数据上性能明显下降。本文提出在推理阶段向预训练的Marigold扩散模型注入散焦模糊线索，用同视角不同光圈的两张图像，通过梯度优化度量尺度参数与噪声隐变量，免训练地将其转为度量深度预测器。实验表明该方法提升了分布外数据上的零样本度量深度估计精度，为结合光学线索的深度基础模型提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有单目度量深度估计在分布外数据集上泛化性能显著下降，缺乏可靠的度量尺度。
method: 在推理阶段向预训练Marigold扩散模型注入散焦模糊线索，用双光圈图像优化度量尺度参数与噪声隐变量。
result: 免训练地将尺度不变的Marigold转为度量深度预测器，在分布外数据上提升零样本度量深度估计表现。
conclusion: 证明结合散焦等光学线索可增强深度基础模型的零样本度量深度能力。
---

## Abstract
Recent monocular metric depth estimation (MMDE) methods have made notable progress towards zero-shot generalization. However, they still exhibit a significant performance drop on out-of-distribution datasets. We address this limitation by injecting defocus blur cues at inference time into Marigold, a \textit{pre-trained} diffusion model for zero-shot, scale-invariant monocular depth estimation (MDE). Our method effectively turns Marigold into a metric depth predictor in a training-free manner. To incorporate defocus cues, we capture two images with a small and a large aperture from the same viewpoint. To recover metric depth, we then optimize the metric depth scaling parameters and the noise latents of Marigold at inference time using gradients from a loss function based on the defocus-blur image formation model. We compare our method against existing state-of-the-art zero-shot MMDE methods on a self-collected real dataset, showing quantitative and qualitative improvements.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
利用散焦模糊线索的零样本度量深度估计。

### 2. 核心内容
现有单目度量深度估计方法在零样本泛化上虽有进展，但在分布外数据上性能明显下降。本文提出在推理阶段向预训练的Marigold扩散模型注入散焦模糊线索，用同视角不同光圈的两张图像，通过梯度优化度量尺度参数与噪声隐变量，免训练地将其转为度量深度预测器。实验表明该方法提升了分布外数据上的零样本度量深度估计精度，为结合光学线索的深度基础模型提供了新思路。

### 3. 对应检索需求
metric depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=imO353Gyrl](https://openreview.net/forum?id=imO353Gyrl)
