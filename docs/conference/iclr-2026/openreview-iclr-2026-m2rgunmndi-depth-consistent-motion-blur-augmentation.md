---
title: Depth-consistent Motion Blur Augmentation
title_zh: 深度一致的运动模糊数据增强
authors: "Aakanksha, Rajagopalan N Ambasamduram"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=m2rgUNmnDI"
tags: ["query:cv-render"]
score: 5.0
evidence: 深度一致的空间可变模糊建模
tldr: 运动模糊常见于轻量手持相机，现有鲁棒性建模多将其视为与其他退化相同，忽略了运动模糊因场景动态而具有的空间可变性以及对场景几何与深度的依赖。已有工作虽引入场景动态导致的空间可变模糊，却仍用空间不变模糊建模相机自运动，存在不足。本文提出一种高效方法生成空间可变且深度一致的运动模糊来建模相机自运动。该工作更真实地反映手持相机退化特性，为模糊增强与场景理解鲁棒性研究提供新思路。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有运动模糊建模忽略空间可变性与场景深度依赖，不够完善。
method: 提出高效方法生成空间可变且深度一致的运动模糊以模拟相机自运动。
result: 相比空间不变模糊建模，更真实地反映手持相机退化特性。
conclusion: 为含深度依赖的模糊增强与场景理解鲁棒性提供新思路。
---

## Abstract
Motion blur is a ubiquitous phenomenon commonly encountered in lightweight, handheld cameras. Addressing this degradation is essential for preserving visual fidelity and ensuring the robustness of vision models for scene understanding tasks. In the literature, robustness to motion blur has been generally treated like other degradations; this despite the complex space-variant nature of motion blur due to scene dynamics and its inherent dependence on scene geometry and depth. While some recent works addressing this issue have introduced space-variant blur due to scene dynamics, they fall back on space-invariant blurring to model camera egomotion which is imperfect. This work proposes an efficient methodology to generate space-variant depth-consistent blur to model camera egomotion by leveraging depth foundation models. We refer to our approach as Depth-consistent Motion Blur Augmentation (DMBA). To demonstrate the effectiveness of DMBA in improving robustness to realistic motion blur, we provide experiments for the tasks of semantic segmentation and self-supervised monocular depth estimation. We include results for standard networks on the Cityscapes dataset for semantic segmentation and the KITTI dataset for monocular depth estimation. We also illustrate the improved generalizability of our method to complex real-world scenes by evaluating on commonly used datasets GoPro and REDS that contain real motion blur.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
深度一致的空间可变模糊建模。

### 2. 核心内容
运动模糊常见于轻量手持相机，现有鲁棒性建模多将其视为与其他退化相同，忽略了运动模糊因场景动态而具有的空间可变性以及对场景几何与深度的依赖。已有工作虽引入场景动态导致的空间可变模糊，却仍用空间不变模糊建模相机自运动，存在不足。本文提出一种高效方法生成空间可变且深度一致的运动模糊来建模相机自运动。该工作更真实地反映手持相机退化特性，为模糊增强与场景理解鲁棒性研究提供新思路。

### 3. 对应检索需求
Papers central to 服务于手机虚化 pipeline 的计算摄影和渲染算法，包括高性能模糊、空间可变卷积、点扩散函数合成、特殊滤镜、边缘优化、图像融合和实时渲染。, especially work that connects or combines: efficient image filtering; computational photography for mobile blur pipeline; point spread function synthesis for blur; edge optimization in blur rendering; image fusion for mobile photography; real time rendering for blur effects; digital filter effects for portrait photography including pro mist glow diffusion and cinematic rendering; efficient defocus blur and bokeh rendering for mobile computational photography; spatially varying convolution and point spread function synthesis for realistic bokeh effects; edge optimization in computational photography.

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=m2rgUNmnDI](https://openreview.net/forum?id=m2rgUNmnDI)
