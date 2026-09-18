---
title: "CAST: Contrastive Adaptation and Distillation for Semi-Supervised Instance Segmentation"
title_zh: CAST：面向半监督实例分割的对比自适应与蒸馏
authors: "Pardis Taghavi, Tian Liu, Renjie Li, Reza Langari, Zhengzhong Tu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=jqLqBG6d2q"
tags: ["query:seg"]
score: 6.0
evidence: 基于知识蒸馏的半监督实例分割
tldr: 实例分割需要昂贵的逐像素标注和庞大模型，限制了实际部署。论文提出CAST半监督知识蒸馏框架，分三阶段：先用对比校准自训练对视觉基础模型做域自适应，再通过统一多目标损失进行知识迁移，最后精炼学生模型以缓解伪标签偏差，核心是融合掩码与类别分数的实例感知像素级对比损失。实验表明CAST能把基础模型压缩为紧凑专家，在有限标注下优于现有方法。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 实例分割依赖昂贵的逐像素标注和算力巨大的模型，难以在有限标注下高效部署紧凑模型。
method: 提出三阶段半监督知识蒸馏框架CAST，先将视觉基础模型自训练做域自适应，再通过统一多目标损失迁移知识，最后精炼学生模型，并用实例感知像素级对比损失。
result: 在有限标注与大量无标注数据下，CAST把基础模型压缩为紧凑专家，性能优于现有半监督分割方法。
conclusion: 表明对比校准与多目标蒸馏可有效提升半监督实例分割的精度与效率。
---

## Abstract
Instance segmentation demands costly per-pixel annotations and computationally expensive models. We introduce CAST, a semi-supervised knowledge distillation (SSKD) framework that compresses pre-trained vision foundation models (VFM) into compact experts using limited labeled and abundant unlabeled data. CAST unfolds in three stages: (1) domain adaptation of the VFM(s) via self-training with contrastive calibration, (2) knowledge transfer through a unified multi-objective loss, and (3) student refinement to mitigate residual pseudo-label bias. Central to CAST is an \emph{instance-aware pixel-wise contrastive loss} that fuses mask and class scores to extract informative negatives and enforce clear inter-instance margins. By maintaining this contrastive signal across both adaptation and distillation, we align teacher and student embeddings and fully leverage unlabeled images. On Cityscapes and ADE20K, our 11X smaller student improves over its zero-shot VFM teacher(s) by +8.5 and +7.1 AP, surpasses adapted teacher(s) by +3.4 and +1.5 AP, and further outperforms state-of-the-art SSKD methods on both benchmarks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于知识蒸馏的半监督实例分割。

### 2. 核心内容
实例分割需要昂贵的逐像素标注和庞大模型，限制了实际部署。论文提出CAST半监督知识蒸馏框架，分三阶段：先用对比校准自训练对视觉基础模型做域自适应，再通过统一多目标损失进行知识迁移，最后精炼学生模型以缓解伪标签偏差，核心是融合掩码与类别分数的实例感知像素级对比损失。实验表明CAST能把基础模型压缩为紧凑专家，在有限标注下优于现有方法。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=jqLqBG6d2q](https://openreview.net/forum?id=jqLqBG6d2q)
