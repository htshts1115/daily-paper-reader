---
title: "From Diffusion to Rectified Flow: Rethinking Text-Based Segmentation"
title_zh: 从扩散到整流流：重思文本驱动分割
authors: "Zishen Qu, Xuesong Li, Hongwei Kang, HaiJian Gu, Quan Meng, Tianrui Niu, Yangxin, Ruidong Pan"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=r5I3AnVAjE"
tags: ["query:seg"]
score: 6.0
evidence: 基于整流流的文本驱动图像分割
tldr: 针对文本驱动图像分割中扩散模型虽具丰富多模态语义特征却因生成特性不利于判别式分割的问题，本文提出RLFSeg框架，利用整流流在潜空间中学习从图像到分割掩码的直接映射。该模型摆脱了扩散噪声过程的干扰，从而更适配判别式分割任务。实验表明其在文本驱动的灵活分割上表现更优，为开放词汇分割提供了新的建模范式。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有方法用扩散模型做分割特征提取，但其生成特性不利于判别式分割任务。
method: 提出RLFSeg，用整流流在潜空间学习从图像到分割掩码的直接映射，摆脱噪声过程。
result: 实验表明该方法在文本驱动分割上表现更优，灵活性和适用范围更广。
conclusion: 以整流流替代扩散特征，为开放词汇文本分割提供了更契合判别任务的范式。
---

## Abstract
Text-based image segmentation aims to delineate object boundaries within an image from text prompts, offering higher flexibility and broader application scope compared to traditional fixed-category segmentation tasks. 
Recent studies have shown that diffusion models (e.g., Stable Diffusion) can provide rich multimodal semantic features, leading to studies of using diffusion models as feature extractors for segmentation tasks. Such methods, however, inherit the generative natures of diffusion models that are harmful to discriminative segmentation tasks. In response, we propose RLFSeg, a novel framework that leverages Rectified Flow to learn direct mapping from the image to the segmentation mask within the latent space. The model is thus freed from the noise-denoise process and the need to optimize the time step of diffusion models, resulting in substantially better performance than previous diffusion-based methods, especially on zero-shot scenarios. By introducing label refinement and an Adaptive One-Step Sampling strategy, the model achieves higher accuracy even on a single inference step. The framework redirects a pretrained generative model to the discriminative segmentation task with zero modification to model structure, thus reveals promising application potential and significant research value.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于整流流的文本驱动图像分割。

### 2. 核心内容
针对文本驱动图像分割中扩散模型虽具丰富多模态语义特征却因生成特性不利于判别式分割的问题，本文提出RLFSeg框架，利用整流流在潜空间中学习从图像到分割掩码的直接映射。该模型摆脱了扩散噪声过程的干扰，从而更适配判别式分割任务。实验表明其在文本驱动的灵活分割上表现更优，为开放词汇分割提供了新的建模范式。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=r5I3AnVAjE](https://openreview.net/forum?id=r5I3AnVAjE)
