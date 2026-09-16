---
title: "RaySt3R: Predicting Novel Depth Maps for Zero-Shot Object Completion"
title_zh: RaySt3R：预测新视角深度图实现零样本物体补全
authors: "Bardienus Pieter Duisterhof, Jan Oberst, Bowen Wen, Stan Birchfield, Deva Ramanan, Jeffrey Ichnowski"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=NpRbTTgRBG"
tags: ["query:mono-depth"]
score: 4.0
evidence: 预测新视角深度图实现零样本物体补全
tldr: 现有三维形状补全方法缺乏三维一致性、计算昂贵且难以刻画锐利边界。本文提出RaySt3R，将三维补全重新表述为新视角合成问题，用前馈Transformer为查询射线预测深度图、物体掩码和逐像素置信度，并跨多个查询视图融合结果。方法在保持边界锐利的同时重建完整三维形状，为深度预测与三维补全提供了统一思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有三维形状补全缺乏三维一致性且边界不锐利。
method: 把补全重构为新视角合成，用前馈Transformer预测深度图、掩码与置信度并融合。
result: 跨查询视图融合可重建完整且边界锐利的三维形状。
conclusion: 为深度预测驱动的三维形状补全提供了统一框架。
---

## Abstract
3D shape completion has broad applications in robotics, digital twin reconstruction, and extended reality (XR). Although recent advances in 3D object and scene completion have achieved impressive results, existing methods lack 3D consistency, are computationally expensive, and struggle to capture sharp object boundaries. 
Our work (RaySt3R) addresses these limitations by recasting 3D shape completion as a novel view synthesis problem. 
Specifically, given a single RGB-D image, 
and a novel viewpoint (encoded as a collection of query rays),
we train a feedforward transformer to predict depth maps, object masks, and per-pixel confidence scores for those query rays. 
RaySt3R fuses these predictions across multiple query views 
to reconstruct complete 3D shapes. 
We evaluate RaySt3R on synthetic and real-world datasets, and observe it achieves state-of-the-art performance,
outperforming the baselines on all datasets by up to 44% in 3D chamfer distance.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
预测新视角深度图实现零样本物体补全。

### 2. 核心内容
现有三维形状补全方法缺乏三维一致性、计算昂贵且难以刻画锐利边界。本文提出RaySt3R，将三维补全重新表述为新视角合成问题，用前馈Transformer为查询射线预测深度图、物体掩码和逐像素置信度，并跨多个查询视图融合结果。方法在保持边界锐利的同时重建完整三维形状，为深度预测与三维补全提供了统一思路。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=NpRbTTgRBG](https://openreview.net/forum?id=NpRbTTgRBG)
