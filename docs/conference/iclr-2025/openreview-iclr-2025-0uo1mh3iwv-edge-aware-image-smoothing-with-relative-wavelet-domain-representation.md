---
title: Edge-aware Image Smoothing with Relative Wavelet Domain Representation
title_zh: 基于相对小波域表示的边缘感知图像平滑
authors: "Huiqing QI, Xiaoliu Luo, Tingting Li, Fang Li"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=0UO1mH3Iwv"
tags: ["query:cv-render"]
score: 4.0
evidence: 边缘感知图像平滑属于基础图像滤波
tldr: 图像平滑旨在去除纹理同时保留主要结构，但现有方法常出现梯度反转与光晕伪影，且深度模型一旦训练完成便无法调节平滑强度。本文提出基于相对小波域表示的边缘感知平滑方法，在小波域中建模相对关系以兼顾平滑强度与边缘保持。实验表明该方法能有效抑制伪影并支持强度可调。其贡献在于为图像滤波与边缘优化提供了通用且可调节的技术手段，对虚化渲染前的图像处理具有参考价值。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 现有图像平滑方法易产生梯度反转与光晕伪影，且深度学习模型的平滑强度无法按纹理复杂度调节。
method: 提出相对小波域表示，在小波域中对边缘与纹理进行建模，实现强度可调的边缘保持平滑。
result: 方法在去除纹理的同时较好保持主要结构，缓解了伪影并支持平滑强度灵活调整。
conclusion: 为图像滤波与边缘优化提供了通用可调的技术方案，可服务于虚化等下游渲染任务。
---

## Abstract
Image smoothing is a fundamental technique in image processing, designed to eliminate perturbations and textures while preserving dominant structures. It plays a pivotal role in numerous high-level computer vision tasks. More recently, both traditional and deep learning-based smoothing methods have been developed. However, existing algorithms frequently encounter issues such as gradient reversals and halo artifacts. Furthermore, the smoothing strength of deep learning-based models, once trained, cannot be adjusted for adapting different complexity levels of textures.  These limitations stem from the inability of previous approaches to achieve an optimal balance between smoothing intensity and edge preservation. Consequently, image smoothing while maintaining edge integrity remains a significant challenge. To address these challenges, we propose a novel edge-aware smoothing model that leverages a relative wavelet domain representation. Specifically, by employing wavelet transformation, we introduce a new measure, termed Relative Wavelet Domain Representation (RWDR), which effectively distinguishes between textures and structures. Additionally, we present an innovative edge-aware scale map that is incorporated into the adaptive bilateral filter, facilitating mutual guidance in the smoothing process. This paper provides complete theoretical derivations for solving the proposed non-convex optimization model. Extensive experiments substantiate that our method has a competitive superiority with previous algorithms in edge-preserving and artifact removal. Visual and numerical comparisons further validate the effectiveness and efficiency of our approach in several applications of image smoothing.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
边缘感知图像平滑属于基础图像滤波。

### 2. 核心内容
图像平滑旨在去除纹理同时保留主要结构，但现有方法常出现梯度反转与光晕伪影，且深度模型一旦训练完成便无法调节平滑强度。本文提出基于相对小波域表示的边缘感知平滑方法，在小波域中建模相对关系以兼顾平滑强度与边缘保持。实验表明该方法能有效抑制伪影并支持强度可调。其贡献在于为图像滤波与边缘优化提供了通用且可调节的技术手段，对虚化渲染前的图像处理具有参考价值。

### 3. 对应检索需求
efficient image filtering。

### 4. 来源与原文
- Source：ICLR-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=0UO1mH3Iwv](https://openreview.net/forum?id=0UO1mH3Iwv)
