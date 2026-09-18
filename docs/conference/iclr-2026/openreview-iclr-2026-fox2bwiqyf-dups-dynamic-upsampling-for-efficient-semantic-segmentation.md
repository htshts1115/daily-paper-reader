---
title: "DUPS: Dynamic upsampling for efficient semantic segmentation"
title_zh: DUPS：面向高效语义分割的动态上采样
authors: "David Hagerman, Roman Naeem, Erik Brorsson, Fredrik Kahl, Lennart Svensson"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=FOx2BWIQyF"
tags: ["query:seg"]
score: 5.0
evidence: 动态上采样的高效语义分割
tldr: 针对语义分割模型通常从高分辨率密集令牌开始、计算冗余且难以在复杂与均匀区域间高效分配算力的问题，本文提出DUPS由粗到细视觉Transformer。它从低分辨率开始，仅对预测含语义边界的区域动态上采样，并用混合分辨率注意力实现粗细令牌交互。实验在ADE20K、COCO-Stuff和Cityscapes上以显著更少FLOPs取得领先或相当精度，说明按语义边界分配计算可大幅降低分割开销。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 语义分割模型通常从高分辨率密集令牌开始，计算冗余，难以在语义复杂区域与均匀区域间高效分配算力。
method: 提出DUPS由粗到细的视觉Transformer，从低分辨率开始，仅对预测含语义边界的区域动态上采样，并采用混合分辨率注意力。
result: 在ADE20K、COCO-Stuff和Cityscapes上以显著更少FLOPs取得领先或相当精度。
conclusion: 表明按语义边界动态分配计算可在保持精度的同时大幅降低分割计算开销。
---

## Abstract
We present \textbf{DUPS}, a coarse-to-fine vision transformer for semantic segmentation. Unlike models that begin with dense high-resolution tokens, DUPS starts at low resolution and dynamically upsamples only regions predicted to contain semantic boundaries, following a “one-token-one-class” principle. Mixed-resolution attention enables interaction between coarse and fine tokens, allocating computation to semantically complex areas while avoiding redundant processing in homogeneous regions.  Experiments on ADE20K, COCO-Stuff, and Cityscapes demonstrate that DUPS achieves state-of-the-art results on ADE20K and COCO-Stuff with substantially fewer FLOPs, and delivers competitive accuracy on Cityscapes at markedly lower compute. For example, DUPS-Base attains \textbf{54.6 mIoU} on ADE20K in the $\sim$110M-parameter class while using fewer FLOPs than comparable backbones.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
动态上采样的高效语义分割。

### 2. 核心内容
针对语义分割模型通常从高分辨率密集令牌开始、计算冗余且难以在复杂与均匀区域间高效分配算力的问题，本文提出DUPS由粗到细视觉Transformer。它从低分辨率开始，仅对预测含语义边界的区域动态上采样，并用混合分辨率注意力实现粗细令牌交互。实验在ADE20K、COCO-Stuff和Cityscapes上以显著更少FLOPs取得领先或相当精度，说明按语义边界分配计算可大幅降低分割开销。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=FOx2BWIQyF](https://openreview.net/forum?id=FOx2BWIQyF)
