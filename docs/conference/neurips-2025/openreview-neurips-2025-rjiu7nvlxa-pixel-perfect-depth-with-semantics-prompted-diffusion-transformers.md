---
title: Pixel-Perfect Depth with Semantics-Prompted Diffusion Transformers
title_zh: 像素级完美深度：基于语义提示扩散Transformer的深度估计
authors: "Gangwei Xu, Haotong Lin, Hongcheng Luo, Xianqi Wang, Jingfeng Yao, Lianghui Zhu, Yuechuan Pu, Cheng Chi_, Haiyang Sun, BING WANG, Guang Chen, Hangjun Ye, Sida Peng, Xin Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=rJiu7nvLxA"
tags: ["query:mono-depth"]
score: 9.0
evidence: 单目深度估计，像素空间扩散，无飞点深度
tldr: 现有生成式深度估计模型微调Stable Diffusion，但需用VAE将深度图压缩到隐空间，从而在边缘和细节处引入飞点伪影。本文提出Pixel-Perfect Depth，直接在像素空间进行扩散生成，并设计语义提示扩散Transformer（SP-DiT）以应对像素空间生成的高复杂度。方法可输出高质量、无飞点的深度图与点云。该工作提升了单目深度估计在边缘与细节处的保真度，对高质量深度重建具有实用价值。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有生成式深度估计依赖VAE压缩深度图，会在边缘与细节处产生飞点伪影，影响点云质量。
method: 提出在像素空间直接进行扩散生成的单目深度估计模型，并设计语义提示扩散Transformer（SP-DiT）降低像素空间生成复杂度。
result: 方法可生成无飞点、边缘清晰的高质量深度图与点云，性能优于基于隐空间的生成式深度模型。
conclusion: 直接在像素空间做扩散生成可有效消除VAE伪影，为高质量单目深度估计提供了新思路。
---

## Abstract
This paper presents **Pixel-Perfect Depth**, a monocular depth estimation model based on pixel-space diffusion generation that produces high-quality, flying-pixel-free point clouds from estimated depth maps. Current generative depth estimation models fine-tune Stable Diffusion and achieve impressive performance. However, they require a VAE to compress depth maps into the latent space, which inevitably introduces flying pixels at edges and details. Our model addresses this challenge by directly performing diffusion generation in the pixel space, avoiding VAE-induced artifacts. To overcome the high complexity associated with pixel-space generation, we introduce two novel designs: 1) **Semantics-Prompted Diffusion Transformers** (**SP-DiT**), which incorporate semantic representations from vision foundation models into DiT to prompt the diffusion process, thereby preserving global semantic consistency while enhancing fine-grained visual details; and 2) **Cascade DiT Design** that progressively increases the number of tokens to further enhance efficiency and accuracy. Our model achieves the best performance among all published generative models across five benchmarks, and significantly outperforms all other models in edge-aware point cloud evaluation. Project page: https://pixel-perfect-depth.github.io/.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
单目深度估计，像素空间扩散，无飞点深度。

### 2. 核心内容
现有生成式深度估计模型微调Stable Diffusion，但需用VAE将深度图压缩到隐空间，从而在边缘和细节处引入飞点伪影。本文提出Pixel-Perfect Depth，直接在像素空间进行扩散生成，并设计语义提示扩散Transformer（SP-DiT）以应对像素空间生成的高复杂度。方法可输出高质量、无飞点的深度图与点云。该工作提升了单目深度估计在边缘与细节处的保真度，对高质量深度重建具有实用价值。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=rJiu7nvLxA](https://openreview.net/forum?id=rJiu7nvLxA)
