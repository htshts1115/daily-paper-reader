---
title: "Looking Locally: Object-Centric Vision Transformers as Foundation Models for Efficient Segmentation"
title_zh: 局部观察：面向高效分割的目标中心视觉Transformer基础模型
authors: "Manuel Traub, Martin V. Butz"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/9782584a78e97e0051f5bd6db32593b4ad8a479b.pdf"
tags: ["query:seg"]
score: 5.0
evidence: 高效目标分割基础模型
tldr: 当前最先进的分割模型需先编码整幅图像再聚焦具体目标，浪费大量计算资源。本文提出FLIP，一种类中央凹输入切块的参数高效视觉模型，通过生物学启发的自顶向下注意力，围绕感兴趣目标选择性采样多分辨率图像块，把高分辨率处理集中在目标中心并保留粗粒度周边上下文。该离网格、尺度不变设计使FLIP-Tiny以仅0.51M参数、比SAM系列少440倍以上参数即大幅超越其分割性能。工作为高效分割基础模型提供新思路，与分割类需求相关。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有分割模型需编码整幅图像再聚焦目标，浪费大量计算资源。
method: 提出FLIP，以类中央凹的自顶向下注意力选择性采样多分辨率目标块。
result: 参数减少440倍以上仍大幅超越SAM系列分割模型。
conclusion: 为高效目标分割提供了参数极省的注意力范式。
---

## Abstract
Current state-of-the-art segmentation models encode entire images before focusing on specific objects. This wastes computational resources. We introduce FLIP (Fovea-Like Input Patching), a parameter-efficient vision model that realizes object segmentation through biologically-inspired top-down attention. FLIP selectively samples multi-resolution patches centered on objects of interest from the input. As a result, it allocates high-resolution processing to object centers while maintaining coarser peripheral context. This off-grid, scale-invariant design enables FLIP to outperform META's Segment Anything models (SAM, SAM2 and fast variants) by large margins: With more than 440 $ \times$ fewer parameters, FLIP-Tiny (0.51M parameters) reaches a mean IoU of 79.90\% while SAM2-L reaches 75.87\% IoU (224.45M parameters). FLIP-Large even achieves 83.26\% mean IoU (96.6M parameters), still running about $2 \times$ faster than SAM2-L. We evaluate on six benchmarks in total. In five established benchmarks (Hypersim, KITTI-360, OpenImages, COCO, LVIS) FLIP consistently outperforms SAM and various variants of it. In our novel ObjaScale dataset, which stress-tests scale invariance with objects ranging from 0.0001\% up to 25\% of the image area, we show that FLIP segments even very small objects accurately, where existing models fail severely. FLIP opens new possibilities for real-time, object-centric vision and offers much higher energy efficiency. We believe that FLIP can act as a powerful foundation model, as it is very well-suited to track objects over time, for example, when being integrated into slot-based scene segmentation architectures.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
高效目标分割基础模型。

### 2. 核心内容
当前最先进的分割模型需先编码整幅图像再聚焦具体目标，浪费大量计算资源。本文提出FLIP，一种类中央凹输入切块的参数高效视觉模型，通过生物学启发的自顶向下注意力，围绕感兴趣目标选择性采样多分辨率图像块，把高分辨率处理集中在目标中心并保留粗粒度周边上下文。该离网格、尺度不变设计使FLIP-Tiny以仅0.51M参数、比SAM系列少440倍以上参数即大幅超越其分割性能。工作为高效分割基础模型提供新思路，与分割类需求相关。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=nIJOtyIQsZ](https://openreview.net/forum?id=nIJOtyIQsZ)
