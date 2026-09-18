---
title: "DiSa: Saliency-Aware Foreground-Background Disentangled Framework for Open-Vocabulary Semantic Segmentation"
title_zh: DiSa：面向开放词汇语义分割的显著性感知前景背景解耦框架
authors: "Zhen Yao, Xin Li, TAOTAO JING, shuai zhang, Mooi Choo Chuah"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=BLfcuMF4vi"
tags: ["query:seg"]
score: 7.0
evidence: 开放词汇语义分割与前景背景解耦
tldr: 开放词汇语义分割需依据文本标签为每个像素分配类别，现有方法多用CLIP等视觉语言模型做稠密预测，但存在前景偏置和空间定位不足两大缺陷，导致忽略背景、边界模糊。本文提出DiSa，一个显著性感知的前景背景解耦框架，显式引入显著性线索来分离前景与背景。方法缓解了前景偏置并锐化物体边界，提升了开放词汇分割质量。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 基于CLIP的分割方法存在前景偏置和空间定位不足，忽略背景且边界模糊。
method: 提出显著性感知的前景背景解耦框架，显式引入显著性线索分离前景与背景。
result: 缓解了前景偏置并改善物体边界的空间定位。
conclusion: 为开放词汇语义分割提供了前景背景解耦的有效方案。
---

## Abstract
Open-vocabulary semantic segmentation aims to assign labels to every pixel in an image based on text labels. State-of-the-art approaches typically utilize vision-language models (VLMs), such as CLIP, for dense prediction. However, VLMs, pre-trained on image-text pairs, are biased toward salient, object-centric regions and exhibit two critical limitations when adapted to semantic segmentation: (i) Foreground Bias, which tends to ignore background regions, and (ii) Limited Spatial Localization, resulting in blurred object boundaries. To address these limitations, we introduce DiSa, a novel saliency-aware foreground-background disentangled framework. By explicitly incorporating saliency cues in our designed Saliency-aware Disentanglement Module (SDM), DiSa separately models foreground and background ensemble features in a divide-and-conquer manner. Additionally, we propose a Hierarchical Refinement Module (HRM) that leverages pixel-wise spatial contexts and enables channel-wise feature refinement through multi-level updates. Extensive experiments on six benchmark open-vocabulary semantic segmentation datasets demonstrate that DiSa consistently outperforms current state-of-the-art methods.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
开放词汇语义分割与前景背景解耦。

### 2. 核心内容
开放词汇语义分割需依据文本标签为每个像素分配类别，现有方法多用CLIP等视觉语言模型做稠密预测，但存在前景偏置和空间定位不足两大缺陷，导致忽略背景、边界模糊。本文提出DiSa，一个显著性感知的前景背景解耦框架，显式引入显著性线索来分离前景与背景。方法缓解了前景偏置并锐化物体边界，提升了开放词汇分割质量。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=BLfcuMF4vi](https://openreview.net/forum?id=BLfcuMF4vi)
