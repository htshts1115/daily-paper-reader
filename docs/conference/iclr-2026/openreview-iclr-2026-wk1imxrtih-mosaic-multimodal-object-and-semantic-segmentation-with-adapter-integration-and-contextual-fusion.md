---
title: "MOSAIC: Multimodal Object and Semantic Segmentation with Adapter Integration and Contextual Fusion"
title_zh: MOSAIC：融合适配器与上下文的多模态目标与语义分割
authors: "Alan Chi-Man Lee, Wing-Sun Cheng, Calvin Chun-Kit Chan"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=WK1iMXRTiH"
tags: ["query:seg"]
score: 6.0
evidence: 多模态语义分割框架
tldr: RGB-IR多模态感知中，可见光与红外特征难以有效对齐融合，制约检测与分割性能。本文提出MOSAIC框架，基于视觉Transformer引入可变形特征采样、特征注意力融合块与上下文特征增强器，动态对齐并整合跨模态多尺度信息。在FLIR、LLVIP、MFNet及VT系列基准上取得领先结果，显著提升鲁棒性与精度。该工作属于语义分割与目标检测范畴，与用户关注的分割需求在方法上相关，但不针对人像或虚化场景。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: RGB-IR多模态感知中跨模态特征难以对齐融合，影响目标检测与语义分割的鲁棒性。
method: 基于视觉Transformer构建MOSAIC，采用可变形特征采样、特征注意力融合块与上下文特征增强器动态整合多尺度RGB-IR特征。
result: 在FLIR、LLVIP、MFNet与VT系列基准上取得领先性能，提升检测与分割精度。
conclusion: 该框架验证了多模态融合对分割任务的价值，属语义分割方向的通用方法参考。
---

## Abstract
We introduce MOSAIC, a novel framework for enhancing multimodal RGB-IR object detection and semantic segmentation. MOSAIC utilizes Vision Transformers and introduces modules like the Deformable Feature Sampling, Feature Attention Fusion Block, and Contextual Feature Enhancer. These components dynamically align and integrate RGB-IR features, capturing multi-scale contextual information to enhance object detection and segmentation tasks. Extensive evaluations demonstrate that MOSAIC achieves state-of-the-art results on FLIR, LLVIP, MFNet and VT-series benchmark datasets, significantly improving robustness and accuracy in RGB-IR downstream tasks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
多模态语义分割框架。

### 2. 核心内容
RGB-IR多模态感知中，可见光与红外特征难以有效对齐融合，制约检测与分割性能。本文提出MOSAIC框架，基于视觉Transformer引入可变形特征采样、特征注意力融合块与上下文特征增强器，动态对齐并整合跨模态多尺度信息。在FLIR、LLVIP、MFNet及VT系列基准上取得领先结果，显著提升鲁棒性与精度。该工作属于语义分割与目标检测范畴，与用户关注的分割需求在方法上相关，但不针对人像或虚化场景。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=WK1iMXRTiH](https://openreview.net/forum?id=WK1iMXRTiH)
