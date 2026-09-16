---
title: Native Segmentation Vision Transformers
title_zh: 原生分割视觉Transformer
authors: "Guillem Braso, Aljosa Osep, Laura Leal-Taixé"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=V7RRnsAlbY"
tags: ["query:seg"]
score: 4.0
evidence: 骨干网络中原生涌现的层次化分割
tldr: 现有视觉骨干多采用均匀下采样降低空间分辨率，忽视图像内容与边界结构。本文提出原生分割视觉Transformer，用内容感知的空间分组层按图像边界与语义动态分配令牌。堆叠该分组层可在特征提取中原生涌现层次化分割掩码，无需额外分割头，为骨干级分割提供了新范式，对主体前景分割有借鉴意义。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 均匀下采样忽略图像内容与边界，分割通常依赖额外专用头。
method: 提出内容感知空间分组层，按边界与语义分配令牌，堆叠形成原生层次化分割。
result: 无需分割专用头即可从分组层涌现强分割掩码。
conclusion: 开创了骨干网络原生分割的新范式，对前景主体分割有参考价值。
---

## Abstract
Uniform downsampling remains the de facto standard for reducing spatial resolution in vision backbones. In this work, we propose an alternative design built around a content-aware spatial grouping layer that dynamically assigns tokens to a reduced set based on image boundaries and their semantic content. Stacking our grouping layer across consecutive backbone stages results in hierarchical segmentation that arises *natively* in the feature extraction process, resulting in our coined Native Segmentation Vision Transformer.
We show that a careful design of our architecture enables the emergence of strong segmentation masks solely from grouping layers, that is, without additional segmentation-specific heads. This sets the foundation for a new paradigm of *native*, backbone-level segmentation, which enables strong zero-shot results without mask supervision, as well as a minimal and efficient standalone model design for downstream segmentation tasks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
骨干网络中原生涌现的层次化分割。

### 2. 核心内容
现有视觉骨干多采用均匀下采样降低空间分辨率，忽视图像内容与边界结构。本文提出原生分割视觉Transformer，用内容感知的空间分组层按图像边界与语义动态分配令牌。堆叠该分组层可在特征提取中原生涌现层次化分割掩码，无需额外分割头，为骨干级分割提供了新范式，对主体前景分割有借鉴意义。

### 3. 对应检索需求
Papers central to 人像分割、人体分割、前景分割，重点关注虚化场景中的主体完整性和手持物归属。, especially work that connects or combines: open-vocabulary segmentation; instance segmentation; semantic segmentation; Portrait segmentation for subject integrity in blur; Human segmentation algorithm with handheld object detection; Foreground segmentation in defocused images; foreground segmentation for handheld objects accessories and portrait scenes; segmentation model for thin structures hair boundaries and occlusions.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=V7RRnsAlbY](https://openreview.net/forum?id=V7RRnsAlbY)
