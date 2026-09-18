---
title: "Looking Locally: Object-Centric Vision Transformers as Foundation Models for Efficient Segmentation"
title_zh: 局部观察：作为高效分割基础模型的对象中心视觉Transformer
authors: "Manuel Traub, Martin V. Butz"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=uM3VAbVs9j"
tags: ["query:seg"]
score: 7.0
evidence: 高效目标分割基础模型
tldr: 现有分割模型需先编码整幅图像再聚焦目标，在高分辨率场景中分割小物体时浪费大量算力。本文提出FLIP，一种仿生中央凹的输入切块方法，通过自上而下注意力选择性采样以目标为中心的多分辨率图像块，将高分辨率处理分配给物体中心、粗粒度上下文留给周边。该尺度不变设计在高效分割上超越SAM、SAM2等模型，为资源受限场景提供了新选择。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有分割模型需编码整图再聚焦目标，高分辨率小目标场景下计算浪费严重。
method: 提出FLIP，仿中央凹地采样以目标为中心的多分辨率图像块进行分割。
result: 在高效分割上超越SAM、SAM2等模型，兼顾精度与算力。
conclusion: 为高效目标分割提供了参数高效的对象中心视觉基础模型。
---

## Abstract
Current state-of-the-art segmentation models encode entire images before focusing on specific objects. As a result, they waste computational resources - particularly when small objects are to be segmented in high-resolution scenes. We introduce FLIP (Fovea-Like Input Patching), a parameter-efficient vision model that realizes object segmentation through biologically-inspired top-down attention. FLIP selectively samples multi-resolution patches centered on objects of interest from the input. As a result, it allocates high-resolution processing to object centers while maintaining coarser peripheral context. This off-grid, scale-invariant design enables FLIP to outperform META's Segment Anything models (SAM, SAM2 and fast variants) by large margins: With more than 440$\times$ fewer parameters, FLIP-Tiny (0.51M parameters) reaches a mean IoU of 79.90\% while SAM2-L reaches 75.87\% IoU (224.45M parameters). FLIP-Large even achieves 83.26\% mean IoU (96.6M parameters), still running about $2    \times$ faster than SAM2-L. We evaluate on six benchmarks in total. 
In five established benchmarks (Hypersim, KITTI-360, OpenImages, COCO, LVIS) FLIP consistently outperforms SAM and various variants of it. In our novel ObjaScale dataset, which stress-tests scale invariance with objects ranging from 0.0001\% up to 25\% of the image area, we show that FLIP segments even very small objects accurately, where existing models fail severely. FLIP opens new possibilities for real-time, object-centric vision applications and offers much higher energy efficiency. We believe that FLIP can act as a powerful foundation model, as it is very well-suited to track objects over time, for example, when being integrated into slot-based scene segmentation architectures.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
高效目标分割基础模型。

### 2. 核心内容
现有分割模型需先编码整幅图像再聚焦目标，在高分辨率场景中分割小物体时浪费大量算力。本文提出FLIP，一种仿生中央凹的输入切块方法，通过自上而下注意力选择性采样以目标为中心的多分辨率图像块，将高分辨率处理分配给物体中心、粗粒度上下文留给周边。该尺度不变设计在高效分割上超越SAM、SAM2等模型，为资源受限场景提供了新选择。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=uM3VAbVs9j](https://openreview.net/forum?id=uM3VAbVs9j)
