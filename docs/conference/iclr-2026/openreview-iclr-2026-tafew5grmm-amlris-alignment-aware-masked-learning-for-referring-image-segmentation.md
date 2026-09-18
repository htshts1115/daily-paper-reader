---
title: "AMLRIS: Alignment-aware Masked Learning for Referring Image Segmentation"
title_zh: AMLRIS：面向指代图像分割的对齐感知掩码学习
authors: "Tongfei Chen, Shuo Yang, Yuguang Yang, Linlin Yang, Runtang Guo, Changbai Li, He Long, Chunyu Xie, Dawei Leng, Baochang Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=tAfew5gRmm"
tags: ["query:seg"]
score: 6.0
evidence: 指代图像分割的训练策略
tldr: 指代图像分割需根据自然语言表达式分割特定目标，但训练数据中存在难以对齐的实例特定信号，直接在错误像素上优化会注入误导梯度。本文提出对齐感知掩码学习AML，通过估计像素级视觉语言对齐度并过滤低对齐像素，让模型聚焦可靠线索。方法简单有效，可获得更可泛化的对齐特征，提升指代分割性能。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 指代分割训练中的难对齐像素会注入误导梯度，损害模型优化方向。
method: 提出对齐感知掩码学习，量化区域与指代的像素级对齐并过滤不可靠像素。
result: 模型能够聚焦可靠线索，学习到更可泛化的对齐特征。
conclusion: 为指代图像分割提供了简单有效的训练改进策略。
---

## Abstract
Referring Image Segmentation (RIS) aims to segment the object in an image uniquely referred to by a natural language expression. However, RIS training often contains hard-to-align and instance-specific visual signals; optimizing on such pixels injects misleading gradients and drives the model in the wrong direction. By explicitly estimating pixel-level vision–language alignment, the learner can suppress low-alignment regions, concentrate on reliable cues, and acquire more generalizable alignment features.
In this paper, we propose Alignment-Aware Masked Learning (AML), a simple yet effective training strategy that quantifies region–referent alignment (PMME) and filters out unreliable pixels during optimization (AFM). Specifically, each sample first computes a similarity map between visual and textual features, and then masks out pixels falling below an adaptive similarity threshold, thereby excluding poorly aligned regions from the training process. AML does not require architectural changes and incurs no inference overhead, directing attention to the areas aligned with the textual description. Experiments on the RefCOCO (vanilla/+/g) datasets show that AML achieves state-of-the-art results across all 8 splits, and beyond improving RIS performance, AML also enhances the model’s robustness to diverse descriptions and scenarios.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
指代图像分割的训练策略。

### 2. 核心内容
指代图像分割需根据自然语言表达式分割特定目标，但训练数据中存在难以对齐的实例特定信号，直接在错误像素上优化会注入误导梯度。本文提出对齐感知掩码学习AML，通过估计像素级视觉语言对齐度并过滤低对齐像素，让模型聚焦可靠线索。方法简单有效，可获得更可泛化的对齐特征，提升指代分割性能。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=tAfew5gRmm](https://openreview.net/forum?id=tAfew5gRmm)
