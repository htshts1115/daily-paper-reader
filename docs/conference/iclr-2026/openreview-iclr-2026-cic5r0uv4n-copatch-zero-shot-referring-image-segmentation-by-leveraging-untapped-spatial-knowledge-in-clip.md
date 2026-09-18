---
title: "CoPatch: Zero-Shot Referring Image Segmentation by Leveraging Untapped Spatial Knowledge in CLIP"
title_zh: CoPatch：利用CLIP中未开发空间知识的零样本指代图像分割
authors: "Na Min An, Inha Kang, Minhyun Lee, Hyunjung Shim"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=cIC5r0uv4n"
tags: ["query:seg"]
score: 7.0
evidence: 利用CLIP空间知识的零样本指代图像分割
tldr: 指代图像分割需要空间定位能力，但现有CLIP等视觉语言模型虽擅长图文对齐，却难以理解空间关系，且文本与视觉特征对空间布局不敏感。为此提出零样本框架CoPatch，挖掘CLIP内部组件中未被利用的空间知识以增强空间定位。实验表明其在指代图像分割上取得提升。该工作说明无需额外训练即可从CLIP中获取空间先验，为零样本开放词汇分割提供新思路。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有视觉语言模型如CLIP擅长图文对齐，却难以理解空间关系，且文本流常忽略上下文词元，视觉特征对空间布局不敏感。
method: 提出零样本指代图像分割框架CoPatch，挖掘CLIP内部组件中未被利用的空间知识来增强空间定位能力。
result: 在零样本指代图像分割任务上取得提升，验证了利用CLIP内部空间知识的有效性。
conclusion: 表明无需额外训练即可从CLIP中提取空间先验，为零样本开放词汇分割提供新思路。
---

## Abstract
Spatial grounding is crucial for referring image segmentation (RIS), where the goal of the task is to localize an object described by language. Current foundational vision-language models (VLMs), such as CLIP, excel at aligning images and text but struggle with understanding spatial relationships. Within the language stream, most existing methods often focus on the primary noun phrase when extracting local text features, undermining contextual tokens. Within the vision stream, CLIP generates similar features for images with different spatial layouts, resulting in limited sensitivity to spatial structure. To address these limitations, we propose COPATCH, a zero-shot RIS framework that leverages internal model components to enhance spatial representations in both text and image modalities. For language, COPATCH constructs hybrid text features by incorporating context tokens carrying spatial cues. For vision, it extracts patch-level image features using our novel path discovered from intermediate layers, where spatial structure is better preserved. These enhanced features are fused into a clustered image–text similarity map, COMAP, enabling precise mask selection. As a result, COPATCH significantly improves spatial grounding in zero-shot RIS across RefCOCO, RefCOCO+, RefCOCOg, and PhraseCut (+ 2–7 mIoU) without requiring any additional training. Our findings underscore the importance of recovering and leveraging the untapped spatial knowledge inherently embedded in VLMs, thereby paving the way for opportunities in zero-shot RIS.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
利用CLIP空间知识的零样本指代图像分割。

### 2. 核心内容
指代图像分割需要空间定位能力，但现有CLIP等视觉语言模型虽擅长图文对齐，却难以理解空间关系，且文本与视觉特征对空间布局不敏感。为此提出零样本框架CoPatch，挖掘CLIP内部组件中未被利用的空间知识以增强空间定位。实验表明其在指代图像分割上取得提升。该工作说明无需额外训练即可从CLIP中获取空间先验，为零样本开放词汇分割提供新思路。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=cIC5r0uv4n](https://openreview.net/forum?id=cIC5r0uv4n)
