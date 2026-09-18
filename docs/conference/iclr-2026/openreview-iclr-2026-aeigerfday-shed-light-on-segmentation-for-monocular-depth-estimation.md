---
title: SHED Light on Segmentation for Monocular Depth Estimation
title_zh: SHED：让分割为单目深度估计带来启示
authors: "Seung Hyun Lee, Sangwoo Mo, Stella X. Yu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=AeIGeRFDAy"
tags: ["query:mono-depth"]
score: 6.0
evidence: 引入分割先验的单目深度估计
tldr: 现有单目深度基础模型虽规模庞大，却把深度预测当作独立逐像素回归，导致深度图中物体形状模糊等结构不一致。为此提出SHED编解码架构，将分割结果融入深度估计，从空间布局显式施加几何先验。实验显示该方法提升了深度图结构一致性，缓解形状歧义。其意义在于说明分割先验可帮助深度模型理解场景结构，为深度估计提供新方向。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有深度基础模型将深度估计视为独立逐像素回归，忽略场景结构，导致深度图中物体形状模糊等结构不一致问题。
method: 提出SHED编解码架构，通过将分割结果引入深度估计，从空间布局中显式施加几何先验约束。
result: 实验表明该方法能提升深度图的结构一致性，缓解物体形状模糊等结构性误差。
conclusion: 表明引入分割先验有助于深度基础模型真正理解场景结构，为深度估计提供新思路。
---

## Abstract
Monocular depth estimation is a dense prediction task that infers per-pixel depth from a single image, fundamental to 3D perception and robotics. There are extensively strong depth foundation models, supported by a backbone pre-trained with a massive scale of data. However, do these depth foundation models really understand the structure? Although real-world scenes exhibit strong structure, these methods treat it as an independent pixel-wise regression problem, often resulting in structural inconsistencies in depth maps, such as ambiguous object shapes. We propose SHED, a novel encoder-decoder architecture that enforces geometric prior explicitly from spatio-layout by incorporating segmentation into depth estimation. Inspired by the bidirectional hierarchical reasoning in human perception, SHED redesigns the vision transformer by replacing fixed patch tokens with segment tokens, which are hierarchically pooled in the encoder and unpooled in the decoder to reverse the hierarchy. The model is supervised only at the final output, and the intermediate segment hierarchy emerges naturally without explicit supervision. SHED offers three key advantages. First, it improves depth boundaries and segment coherence, and demonstrates robust cross-domain generalization. Second, it enables features and segments to better capture global scene layout. Third, it enhances 3D reconstruction and reveals part structures that conventional pixel-wise methods fail to capture.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
引入分割先验的单目深度估计。

### 2. 核心内容
现有单目深度基础模型虽规模庞大，却把深度预测当作独立逐像素回归，导致深度图中物体形状模糊等结构不一致。为此提出SHED编解码架构，将分割结果融入深度估计，从空间布局显式施加几何先验。实验显示该方法提升了深度图结构一致性，缓解形状歧义。其意义在于说明分割先验可帮助深度模型理解场景结构，为深度估计提供新方向。

### 3. 对应检索需求
Papers central to 单目深度估计，用于人像虚化、主体背景层次、手持物和头戴物深度判断。, especially work that connects or combines: monocular depth estimation; relative depth prediction; metric depth estimation; zero-shot depth estimation; depth foundation model; Depth Anything model; monocular depth estimation for portrait bokeh and mobile photography; lightweight depth model for mobile devices; monocular depth estimation for thin structures transparent objects and handheld objects; depth foundation model for zero shot generalization in real world images.

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=AeIGeRFDAy](https://openreview.net/forum?id=AeIGeRFDAy)
