---
title: Enhancing Object Discovery for Unsupervised Instance Segmentation and Object Detection
title_zh: 增强无监督实例分割与目标检测中的目标发现
authors: "Xingyu Feng, Hebei Gao, Hong Li"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/4033fe196ac0c2dde702875edc72bbdcae3b30be.pdf"
tags: ["query:seg"]
score: 5.0
evidence: 无监督实例分割与目标检测
tldr: 现有无监督实例分割常依赖聚类与掩码后处理，流程复杂且难以一次生成多目标掩码。本文提出COLER，先用CutOnce做一次归一化割生成粗伪标签，再让检测器从这些掩码中学习，无需K-Means等聚类。训练中该方法取得强性能，并摆脱掩码后处理依赖。工作为归一化割在多目标分割中的应用开辟新方向，对通用实例分割方法有借鉴价值。
source: ICML-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有无监督实例分割依赖聚类与后处理，流程复杂且难以一次生成多目标掩码。
method: 提出CutOnce一次归一化割生成粗伪标签，再让检测器从掩码中学习。
result: 训练中取得强性能，无需掩码后处理即可完成多目标分割。
conclusion: 为归一化割在多目标分割中的应用开辟新方向。
---

## Abstract
We propose Cut-Once-and-LEaRn (COLER), a simple approach for unsupervised instance segmentation and object detection. COLER first uses our developed CutOnce to generate coarse pseudo labels, then enables the detector to learn from these masks. CutOnce applies Normalized Cut (NCut) only once and does not rely on any clustering methods (e.g., K-Means), but it can generate multiple object masks in an image. Our work opens a new direction for NCut algorithm in multi-object segmentation. We have designed several novel yet simple modules that not only allow CutOnce to fully leverage the object discovery capabilities of self-supervised model, but also free it from reliance on mask post-processing. During training, COLER achieves strong performance without requiring specially designed loss functions for pseudo labels, and its performance is further improved through self-training. COLER is a zero-shot unsupervised model that outperforms previous state-of-the-art methods on multiple benchmarks. We believe our method can help advance the field of unsupervised object localization.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
无监督实例分割与目标检测。

### 2. 核心内容
现有无监督实例分割常依赖聚类与掩码后处理，流程复杂且难以一次生成多目标掩码。本文提出COLER，先用CutOnce做一次归一化割生成粗伪标签，再让检测器从这些掩码中学习，无需K-Means等聚类。训练中该方法取得强性能，并摆脱掩码后处理依赖。工作为归一化割在多目标分割中的应用开辟新方向，对通用实例分割方法有借鉴价值。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICML-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=i2790nxluz](https://openreview.net/forum?id=i2790nxluz)
