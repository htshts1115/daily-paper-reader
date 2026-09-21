---
title: Boosting Monocular Metric Depth Estimation via Bokeh Rendering
title_zh: 通过散景渲染提升单目度量深度估计
authors: "Hangwei Zhang, Armando Fortes, Tianyi Wei, Xingang Pan"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/1f3b6489c9d5cb56535cae56abc6d1845969cfc7.pdf"
tags: ["query:neural-bokeh"]
score: 9.0
evidence: 利用散景渲染提升单目深度估计
tldr: 现有散景管线依赖含噪深度图导致伪影，而单目深度模型在无纹理或远处区域易失效，扩散方法又缺乏一致的度量尺度。作者提出BokehDepth两阶段框架，将合成散焦视为无需监督的几何信号，先由物理约束生成模型从单图产生标定散景堆栈，再用于深度估计。实验表明该互惠机制能同时提升散景渲染质量与度量深度的准确性。该工作揭示了散焦与深度估计的光学互惠关系，为人像虚化与移动摄影提供新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有散景管线受噪声深度图拖累，单目深度模型在无纹理区域又缺乏几何线索，二者未充分利用散焦与深度的光学互惠。
method: 提出BokehDepth两阶段框架，用物理约束生成模型从单图合成标定散景堆栈，并将其作为无监督几何信号监督深度估计。
result: 实验证明该方法能同时改善散景渲染效果与度量深度的尺度一致性，在无纹理和远处区域表现更好。
conclusion: 该工作建立散焦渲染与深度估计的互惠桥梁，为人像虚化和移动端深度提供可复用范式。
---

## Abstract
Bokeh rendering and depth estimation share a fundamental optical connection, yet existing methods fail to fully exploit this reciprocity. Conventional bokeh pipelines rely heavily on noisy depth maps that inevitably introduce visual artifacts. Conversely, existing monocular depth models typically follow two flawed paradigms. Generative diffusion-based frameworks often lack consistent metric scale. Meanwhile, feed-forward metric depth models frequently fail in textureless or distant regions where defocus blur can provide geometric information. We propose BokehDepth, a two-stage framework that treats synthetic defocus as a supervision-free geometric signal. In the first stage, a physically grounded generative model produces calibrated bokeh stacks from a single sharp input without requiring prior depth input. Subsequently, a lightweight defocus-aware aggregation module integrates these stacks into the encoder of a depth estimation framework. This mechanism allows the model to extract consistent geometric features from the defocus dimension while keeping the decoder architecture unchanged. Experiments demonstrate that BokehDepth achieves superior visual bokeh fidelity compared to depth-dependent rendering baselines and consistently enhances the metric accuracy of state-of-the-art monocular depth models.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
利用散景渲染提升单目深度估计。

### 2. 核心内容
现有散景管线依赖含噪深度图导致伪影，而单目深度模型在无纹理或远处区域易失效，扩散方法又缺乏一致的度量尺度。作者提出BokehDepth两阶段框架，将合成散焦视为无需监督的几何信号，先由物理约束生成模型从单图产生标定散景堆栈，再用于深度估计。实验表明该互惠机制能同时提升散景渲染质量与度量深度的准确性。该工作揭示了散焦与深度估计的光学互惠关系，为人像虚化与移动摄影提供新思路。

### 3. 对应检索需求
depth-aware blur。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=B3YoryA3VD](https://openreview.net/forum?id=B3YoryA3VD)
