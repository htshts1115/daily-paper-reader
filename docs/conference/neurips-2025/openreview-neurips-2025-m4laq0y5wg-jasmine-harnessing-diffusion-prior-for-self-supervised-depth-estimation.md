---
title: "Jasmine: Harnessing Diffusion Prior for Self-supervised Depth Estimation"
title_zh: Jasmine：利用扩散先验的自监督深度估计
authors: "JiYuan Wang, Chunyu Lin, cheng guan, Lang Nie, Jing He, Haodong Li, Kang Liao, Yao Zhao"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=M4Laq0Y5WG"
tags: ["query:mono-depth"]
score: 9.0
evidence: 基于扩散先验的自监督单目深度估计
tldr: 现有基于扩散模型的稠密预测方法多依赖高精度监督，而自监督重投影又受遮挡、无纹理和光照变化困扰，导致预测模糊。本文提出 Jasmine，首个基于稳定扩散的自监督单目深度估计框架，通过混合批次图像重建代理任务充分利用扩散视觉先验。无需额外监督即可提升预测清晰度与泛化能力。该工作推动了深度基础模型在真实图像上的零样本泛化。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有扩散方法需高精度监督，自监督重投影又受遮挡和无纹理影响导致预测模糊。
method: 构建混合批次图像重建代理任务，让稳定扩散视觉先验服务于自监督单目深度估计。
result: 在无额外监督下提升了单目深度预测的清晰度与泛化性能。
conclusion: 为扩散先验驱动的自监督深度估计提供了新范式。
---

## Abstract
In this paper, we propose \textbf{Jasmine}, the first Stable Diffusion (SD)-based self-supervised framework for monocular depth estimation, which effectively harnesses SD’s visual priors to enhance the sharpness and generalization of unsupervised prediction. Previous SD-based methods are all supervised since adapting diffusion models for dense prediction requires high-precision supervision. In contrast, self-supervised reprojection suffers from inherent challenges (\textit{e.g.}, occlusions, texture-less regions, illumination variance), and the predictions exhibit blurs and artifacts that severely compromise SD's latent priors. To resolve this, we construct a novel surrogate task of mix-batch image reconstruction. Without any additional supervision, it preserves the detail priors of SD models by reconstructing the images themselves while preventing depth estimation from degradation. Furthermore, to address the inherent misalignment between SD's scale and shift invariant estimation and self-supervised scale-invariant depth estimation, we build the Scale-Shift GRU. It not only bridges this distribution gap but also isolates the fine-grained texture of SD output against the interference of reprojection loss. Extensive experiments demonstrate that Jasmine achieves SoTA performance on the KITTI benchmark and exhibits superior zero-shot generalization across multiple datasets.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于扩散先验的自监督单目深度估计。

### 2. 核心内容
现有基于扩散模型的稠密预测方法多依赖高精度监督，而自监督重投影又受遮挡、无纹理和光照变化困扰，导致预测模糊。本文提出 Jasmine，首个基于稳定扩散的自监督单目深度估计框架，通过混合批次图像重建代理任务充分利用扩散视觉先验。无需额外监督即可提升预测清晰度与泛化能力。该工作推动了深度基础模型在真实图像上的零样本泛化。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=M4Laq0Y5WG](https://openreview.net/forum?id=M4Laq0Y5WG)
