---
title: Learning Explicit Semantic-Spatial Synergy for Weakly Supervised Referring Image Segmentation
title_zh: 学习显式语义-空间协同的弱监督指代图像分割
authors: "Tianrui ZHANG, Zilin Guo, Lian Xu, Mohammed Bennamoun, Farid Boussaid, Hamid Laga, Dan Xu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=DiyoGdNId7"
tags: ["query:seg"]
score: 5.0
evidence: 结合深度空间线索的指代图像分割
tldr: 针对弱监督指代图像分割缺乏显式空间理解、与全监督方法差距较大的问题，本文提出ES³Net框架，通过显式空间增强模块将由深度获得的对象级三维坐标与掩码语义特征融合，从多个角度显式学习语义-空间协同。在弱监督设定下引入空间信息后分割性能明显提升，验证了语义与空间协同建模的有效性。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有弱监督指代图像分割缺乏显式空间理解机制，难以实现语义与空间协同，与全监督方法仍有较大差距。
method: 提出ES³Net框架，通过显式空间增强模块将掩码语义特征与由深度获得的对象级三维坐标融合，从三个角度显式学习语义-空间协同。
result: 在弱监督设定下显式引入空间信息后，分割性能明显提升，缩小了与全监督方法的差距。
conclusion: 表明显式建模语义与空间协同是提升弱监督指代分割的有效途径。
---

## Abstract
Weakly Supervised Referring Image Segmentation (WSRIS) aims to segment target objects specified by natural language expressions using only image-text pairs. While recent advances have improved semantic grounding, existing methods still lack explicit mechanisms to incorporate spatial understanding, preventing them from achieving semantic–spatial synergy and leaving a large gap to fully supervised approaches. To address this limitation, we propose ES³Net, a novel framework that Explicitly learns Semantic-Spatial Synergy from the following three perspectives: First, we propose an Explicit Spatial Enhancement Module that integrates mask-grounded semantic features with object-centric 3D coordinates derived from readily obtained depth. This produces embeddings where spatial geometry is semantically anchored, enabling accurate localization of position-sensitive expressions. Second, a Language Consistency Module is proposed to enforce consistent alignment across diverse expressions referring to the same instance, improving robustness to linguistic variations. Finally, we introduce a Confidence-Aware Dense Distillation strategy that transforms high-confidence grounding predictions into pseudo labels, allowing a lightweight student–teacher RIS model to be trained for stable learning and efficient inference. Extensive experiments on RefCOCO, RefCOCO+, and RefCOCOg demonstrate that ES³Net establishes new state-of-the-art performance, underscoring the importance of explicit semantic–spatial synergy in advancing WSRIS.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
结合深度空间线索的指代图像分割。

### 2. 核心内容
针对弱监督指代图像分割缺乏显式空间理解、与全监督方法差距较大的问题，本文提出ES³Net框架，通过显式空间增强模块将由深度获得的对象级三维坐标与掩码语义特征融合，从多个角度显式学习语义-空间协同。在弱监督设定下引入空间信息后分割性能明显提升，验证了语义与空间协同建模的有效性。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=DiyoGdNId7](https://openreview.net/forum?id=DiyoGdNId7)
