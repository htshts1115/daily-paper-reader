---
title: Multimodal Fusion of RGB and Complementary Modalities for Semantic Segmentation
title_zh: 融合RGB与互补模态的多模态语义分割
authors: "Hu Cao, Yifeng Cheng, Mu He, Mengyu Li, Yinlong Liu, Alois Knoll"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=wBD61QFEpm"
tags: ["query:seg"]
score: 6.0
evidence: RGB与辅助模态的多模态语义分割
tldr: 针对RGB+X多模态语义分割在恶劣光照和运动模糊下鲁棒性不足的问题，论文指出逐位置模态选择与跨模态语义对齐是两个关键瓶颈。为此提出逐token辅助模态选择机制，只激活最可靠的辅助流，并设计风格一致、极性感知的跨模态融合，将辅助外观统计迁移到RGB特征同时保留支持与矛盾证据。在热成像、事件、LiDAR、偏振和光场五种模态组合上实验，分割鲁棒性优于现有方法，为多模态融合分割提供了通用框架。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 多模态语义分割在恶劣光照与运动模糊下需要更鲁棒的模态选择与跨模态语义对齐，现有方法难以在逐位置可靠激活辅助模态。
method: 提出token级辅助模态选择机制，并采用风格一致、极性感知的跨模态融合，把辅助外观统计迁移到RGB特征，同时保留支持与矛盾证据。
result: 在热成像、事件、LiDAR、偏振、光场五种模态组合上验证，分割鲁棒性优于现有RGB+X方法。
conclusion: 表明逐token模态选择与极性感知融合能有效提升多模态语义分割的可靠性。
---

## Abstract
Multi-modal semantic segmentation augments RGB imagery with an auxiliary sensing stream X (RGB+X), e.g., thermal, event, LiDAR, polarization, or light field, to improve robustness under adverse illumination and motion blur. We target two coupled bottlenecks in RGB+X segmentation: selecting the most predictive modality at each location and aligning semantics across different modalities. The proposed framework performs token-wise auxiliary selection to activate a single, reliable auxiliary stream per token and applies style-consistent, polarity-aware cross-modality fusion that transfers auxiliary appearance statistics to RGB features while preserving both supportive and contradictory evidence. We evaluate across five modality pairings: RGB+Thermal, RGB+Event, RGB+LiDAR, RGB+Polarization, and RGB+Light Field and obtain new state of the art on each. Representative results include 76.89% mIoU on MFNet (RGB-Thermal) and 52.54% mIoU on MCubeS (RGB+A+D+N) and other combinations, surpassing recent fusion frameworks under comparable backbones and training protocols. Overall, this selective, alignment-aware fusion design provides a robust path to better RGB+X segmentation without sacrificing efficiency.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
RGB与辅助模态的多模态语义分割。

### 2. 核心内容
针对RGB+X多模态语义分割在恶劣光照和运动模糊下鲁棒性不足的问题，论文指出逐位置模态选择与跨模态语义对齐是两个关键瓶颈。为此提出逐token辅助模态选择机制，只激活最可靠的辅助流，并设计风格一致、极性感知的跨模态融合，将辅助外观统计迁移到RGB特征同时保留支持与矛盾证据。在热成像、事件、LiDAR、偏振和光场五种模态组合上实验，分割鲁棒性优于现有方法，为多模态融合分割提供了通用框架。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=wBD61QFEpm](https://openreview.net/forum?id=wBD61QFEpm)
