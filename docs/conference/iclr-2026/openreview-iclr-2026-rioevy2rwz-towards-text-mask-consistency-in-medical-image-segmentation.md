---
title: Towards Text-Mask Consistency in Medical Image Segmentation
title_zh: 面向医学图像分割的文本-掩码一致性
authors: "Jie Gui, HangTu, Wen Sha, Xiuquan Du"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=riOevy2RwZ"
tags: ["query:seg"]
score: 4.0
evidence: 文本-掩码一致性的图像分割
tldr: 视觉语言模型在医学图像分割中常产生与文本描述冲突的掩码，尤其在多部位多病灶描述下。作者将失败归因于模板化临床语言导致的假负样本以及单向视觉驱动交叉注意力缺乏语言主导的空间通路。为此提出一致性增强的两阶段分割框架C2Seg，采用聚类感知对比学习与语言主导的空间通路。实验提升了文本与掩码的一致性。该工作属语义分割范畴，但面向医学领域，与用户人像/前景分割需求仅为方法层面弱相关。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 医学视觉语言分割模型常输出与文本不符的掩码，多部位多病灶描述下对齐困难。
method: 提出一致性增强两阶段分割C2Seg，用聚类感知对比学习并引入语言主导的空间感知通路。
result: 缓解了文本与掩码冲突问题，提升跨多站点描述的分割一致性。
conclusion: 该工作聚焦医学语义分割的跨模态对齐，属分割方向的领域特定方法参考。
---

## Abstract
Vision-language models for medical image segmentation often produce masks that conflict with the accompanying text, especially under multi-site/multi-lesion descriptions. We trace this failure to two factors: (i) highly templated and repetitive clinical language causes one-to-one hard contrastive learning to yield numerous false negatives, weakening cross-modal alignment; and (ii) predominantly vision-driven, one-way cross-attention lacks a language-dominant, spatially aware pathway, hindering effective injection of textual semantics into the spatial visual domain. To this end, we propose Consistency-enhanced Two-stage Segmentation (C2Seg). In the pretraining stage, Cluster-aware Contrastive Learning uses a frozen strong baseline to construct an intra-batch text similarity matrix as soft labels, thereby alleviating false negative conflicts and producing more discriminative visual representations. In the fusion stage, we introduce a Bidirectional Complementary Attention Module, where each modality dominates attention along its own path, fostering deep interaction and structural consistency between visual and textual representations. In order to enhance the expressive power of multimodal features, we further adopt KAN-based Attention Gating. Without updating the language encoder, our approach significantly improves text-mask consistency and segmentation accuracy on four public medical imaging datasets.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
文本-掩码一致性的图像分割。

### 2. 核心内容
视觉语言模型在医学图像分割中常产生与文本描述冲突的掩码，尤其在多部位多病灶描述下。作者将失败归因于模板化临床语言导致的假负样本以及单向视觉驱动交叉注意力缺乏语言主导的空间通路。为此提出一致性增强的两阶段分割框架C2Seg，采用聚类感知对比学习与语言主导的空间通路。实验提升了文本与掩码的一致性。该工作属语义分割范畴，但面向医学领域，与用户人像/前景分割需求仅为方法层面弱相关。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=riOevy2RwZ](https://openreview.net/forum?id=riOevy2RwZ)
