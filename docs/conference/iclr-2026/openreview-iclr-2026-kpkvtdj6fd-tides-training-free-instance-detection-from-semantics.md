---
title: "TIDES: Training-free Instance Detection from Semantics"
title_zh: TIDES：从语义出发的免训练实例检测
authors: "Jaejun Lee, Shin Nishimura, Sahar Ghavidel, Allen Tao, Dibyendu Mukherjee"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=KpKvtdJ6Fd"
tags: ["query:seg"]
score: 7.0
evidence: 基于语义的免训练开放词汇与实例分割
tldr: 针对免训练开放词汇实例分割难以区分个体的空白，本文提出TIDES流水线。方法系统评估SAM等可提示分割模型作为实例划分来源的适用性，并设计实例导向评分，利用patch级语义将任意TF-OVSS与可提示模型组合以生成实例分割。实验表明该免训练方案可有效完成开放词汇实例分割，拓展了基础模型在密集预测中的复用能力。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 免训练开放词汇语义分割已有进展，但实例分割因双编码器无法区分个体而仍待探索。
method: 复用TF-OVSS与可提示分割模型，并提出实例导向评分利用patch级语义划分实例。
result: 无需训练即可将语义分割能力转化为开放词汇实例分割，取得有效分割结果。
conclusion: 证明基础模型组合可支撑免训练开放词汇实例分割，扩展密集预测任务边界。
---

## Abstract
Efforts to leverage the coarse semantic understanding of vision-language dual encoder models, such as CLIP, for dense prediction tasks without training have shown promise, particularly in training-free open-vocabulary semantic segmentation (TF-OVSS). However, instance segmentation (TF-OVIS) remains largely unexplored because dual encoder models cannot distinguish individual instances on their own. We systematically evaluate the suitability of promptable segmentation models (PSMs), such as SAM, as sources of accurate instance delineation and present TIDES (Training-free Instance Detector from Semantics), a pipeline that repurposes any pair of TF-OVSS and PSM for instance segmentation. At its core is our instance-oriented (IO) scoring, which leverages patch-level semantic alignments from TF-OVSS to re-evaluate PSM-generated masks, accurately identifying individual object instances without training, instance-level labels, or external detectors. Extensive evaluation on the MS COCO-based OVIS benchmark across multiple TF-OVSS and PSM combinations demonstrates TIDES’ flexibility and effectiveness: it surpasses the previous best TF-OVIS method by 9.2 AP and naive baselines with the original scoring by 2.7 AP.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于语义的免训练开放词汇与实例分割。

### 2. 核心内容
针对免训练开放词汇实例分割难以区分个体的空白，本文提出TIDES流水线。方法系统评估SAM等可提示分割模型作为实例划分来源的适用性，并设计实例导向评分，利用patch级语义将任意TF-OVSS与可提示模型组合以生成实例分割。实验表明该免训练方案可有效完成开放词汇实例分割，拓展了基础模型在密集预测中的复用能力。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=KpKvtdJ6Fd](https://openreview.net/forum?id=KpKvtdJ6Fd)
