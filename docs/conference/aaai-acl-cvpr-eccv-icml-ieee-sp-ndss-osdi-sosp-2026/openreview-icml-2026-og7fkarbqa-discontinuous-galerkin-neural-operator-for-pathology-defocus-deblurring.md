---
title: Discontinuous Galerkin Neural Operator for Pathology Defocus Deblurring
title_zh: 用于病理散焦去模糊的间断伽辽金神经算子
authors: "Shaoqing Duan, Haofei Song, Xintian Mao, Qingli Li, Yan Wang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/17cf2c6f128fc8ffee74194777d258c19dc2bed6.pdf"
tags: ["query:cv-render"]
score: 4.0
evidence: 将散焦建模为空间可变积分算子
tldr: 病理显微图像中的散焦去模糊面临由位置相关积分成像带来的空间可变且局部不连续模糊。现有深度学习方法受平移不变假设限制，难以建模此类异质模糊。作者提出间断伽辽金神经算子，将散焦形成直接建模为积分算子，克服全局核的平滑与平稳假设。该算子视角对散焦模糊建模与点扩散函数合成具有方法层面的借鉴价值。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 病理显微散焦模糊具有空间可变和局部不连续特性，现有深度学习方法受平移不变假设限制，难以刻画异质模糊。
method: 提出间断伽辽金神经算子，将散焦形成直接建模为积分算子，突破全局参数化核的平滑与平稳性假设。
result: 该算子能够更有效地建模非平稳、异质且局部不连续的散焦模式，提升去模糊表现。
conclusion: 工作为散焦模糊的算子化建模提供新视角，对散焦核与点扩散函数相关任务具方法论启示。
---

## Abstract
Defocus deblurring in pathological microscopy remains challenging due to the spatially varying and locally discontinuous nature of optical blur induced by a position-dependent integral imaging process.
  Existing deep learning methods, constrained by shift-invariance assumptions and limited interpretability, are not well suited to such heterogeneous blur patterns.
  Neural operators provide a principled alternative by modeling defocus formation directly as an integral operator, offering a new perspective on defocus deblurring.
  However, most existing neural operator architectures for low-level vision rely on globally parameterized kernels that assume smoothness and stationarity, limiting their ability to model heterogeneous and locally discontinuous blur patterns.
  To address this limitation, we propose the Discontinuous Galerkin Neural Operator (DGNO), which parameterizes the integral kernel using a discontinuous Galerkin formulation with element-local volume operators and interface numerical fluxes.
  DGNO provides a principled combination of locality,
  heterogeneity modeling, and global coherence while preserving the underlying physics
  of optical image formation. 
  Extensive experiments demonstrate that DGNO surpasses state-of-the-art methods, delivering sharper reconstructions, robust handling of spatially varying blur, and scalable high-resolution performance.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
将散焦建模为空间可变积分算子。

### 2. 核心内容
病理显微图像中的散焦去模糊面临由位置相关积分成像带来的空间可变且局部不连续模糊。现有深度学习方法受平移不变假设限制，难以建模此类异质模糊。作者提出间断伽辽金神经算子，将散焦形成直接建模为积分算子，克服全局核的平滑与平稳假设。该算子视角对散焦模糊建模与点扩散函数合成具有方法层面的借鉴价值。

### 3. 对应检索需求
point spread function synthesis for blur。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=Og7FKaRBQA](https://openreview.net/forum?id=Og7FKaRBQA)
