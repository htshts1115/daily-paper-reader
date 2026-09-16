---
title: Dense Metric Depth Estimation via Event-based Differential Focus Volume Prompting
title_zh: 基于事件对焦差分体积提示的稠密度量深度估计
authors: "Boyu Li, Peiqi Duan, Zhaojun Huang, Xinyu Zhou, Yifei Xia, Boxin Shi"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=cPO8dUCJOc"
tags: ["query:mono-depth"]
score: 7.0
evidence: 融合事件与图像基础模型的稠密度量深度估计
tldr: 单图像深度估计在真实场景中常受尺度歧义与视觉错觉困扰，传统基于对焦的方法又受限于低采样率。本文提出基于事件的对焦差分体积，通过焦点扫描触发事件构建稀疏度量深度，并借助提示机制将其注入图像基础模型。该方法实现了稠密度量深度估计，在复杂真实场景中缓解了尺度不确定性，为融合事件与基础模型的度量深度提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 单图像深度估计存在尺度歧义与视觉错觉，传统对焦方法又受限于低采样率，真实场景稠密度量深度仍难获取。
method: 利用焦点扫描触发事件构建事件对焦差分体积，转化为稀疏度量深度，并以提示方式融合进图像基础模型。
result: 该方法实现了稠密度量深度估计，在复杂真实场景中缓解尺度歧义，验证了事件与基础模型融合的有效性。
conclusion: 融合事件与图像基础模型的提示式方案为真实场景稠密度量深度估计提供了新路径。
---

## Abstract
Dense metric depth estimation has witnessed great developments in recent years. While single-image-based methods have demonstrated commendable performance in certain circumstances, they may encounter challenges regarding scale ambiguities and visual illusions in real world. Traditional depth-from-focus methods are constrained by low sampling rates during data acquisition. In this paper, we introduce a novel approach to enhance dense metric depth estimation by fusing events with image foundation models via a prompting approach. Specifically, we build Event-based Differential Focus Volumes (EDFV) using events triggered through focus sweeping, which are subsequently transformed into sparse metric depth maps. These maps are then utilized for prompting dense depth estimation via our proposed Event-based Depth Prompting Network. We further construct synthetic and real-captured datasets to facilitate the training and evaluation of both frame-based and event-based methods. Quantitative and qualitative results, including both in-domain and zero-shot experiments, demonstrate the superior performance of our method compared to existing approaches. Code and data will be available at https://github.com/liboyu02/EDFV/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
融合事件与图像基础模型的稠密度量深度估计。

### 2. 核心内容
单图像深度估计在真实场景中常受尺度歧义与视觉错觉困扰，传统基于对焦的方法又受限于低采样率。本文提出基于事件的对焦差分体积，通过焦点扫描触发事件构建稀疏度量深度，并借助提示机制将其注入图像基础模型。该方法实现了稠密度量深度估计，在复杂真实场景中缓解了尺度不确定性，为融合事件与基础模型的度量深度提供了新思路。

### 3. 对应检索需求
metric depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=cPO8dUCJOc](https://openreview.net/forum?id=cPO8dUCJOc)
