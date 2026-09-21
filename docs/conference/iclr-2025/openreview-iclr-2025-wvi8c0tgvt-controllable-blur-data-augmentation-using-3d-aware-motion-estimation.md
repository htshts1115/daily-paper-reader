---
title: Controllable Blur Data Augmentation Using 3D-Aware Motion Estimation
title_zh: 基于3D感知运动估计的可控模糊数据增强
authors: "Insoo Kim, Hana Lee, Hyong-Euk Lee, Jinwoo Shin"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=Wvi8c0tgvt"
tags: ["query:cv-render"]
score: 6.0
evidence: 3D感知模糊合成与数据增强
tldr: 针对真实模糊数据集场景和模糊模式不足、扩展数据耗时的问题，该文提出3D感知模糊合成器，从3D空间估计相机和物体运动以生成多样且真实的模糊图像。相比2D非均匀核方法，其模糊模式更符合物理成像。实验表明该方法能有效增强模糊数据多样性。其可控模糊合成可服务于计算摄影模糊管线，但主要针对运动模糊而非景深散景。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 解决真实模糊数据集多样不足且扩展成本高的问题。
method: 提出3D感知模糊合成器，从3D运动估计生成可控模糊图像。
result: 生成更真实多样的模糊图像用于数据增强。
conclusion: 为模糊合成和增强提供3D感知方案，可迁移到模糊管线。
---

## Abstract
Existing realistic blur datasets provide insufficient variety in scenes and blur patterns to be trained, while expanding data diversity demands considerable time and effort due to complex dual-camera systems. To address the challenge, data augmentation can be an effective way to artificially increase data diversity. However, existing methods on this line are typically designed to estimate motions from a 2D perspective, e.g., estimating 2D non-uniform kernels disregarding 3D aspects of blur modeling, which leads to unrealistic motion patterns due to the fact that camera and object motions inherently arise in 3D space. In this paper, we propose a 3D-aware blur synthesizer capable of generating diverse and realistic blur images for blur data augmentation. Specifically, we estimate 3D camera positions within the motion blur interval, generate the corresponding scene images, and aggregate them to synthesize a realistic blur image. Since the 3D camera positions projected onto the 2D image plane inherently lie in 2D space, we can represent the 3D transformation as a combination of 2D transformation and projected 3D residual component. This allows for 3D transformation without requiring explicit depth measurements, as the 3D residual component is directly estimated via a neural network. Furthermore, our blur synthesizer allows for controllable blur data augmentation by modifying blur magnitude, direction, and scenes, resulting in diverse blur images. As a result, our method significantly improves deblurring performance, making it more practical for real-world scenarios.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
3D感知模糊合成与数据增强。

### 2. 核心内容
针对真实模糊数据集场景和模糊模式不足、扩展数据耗时的问题，该文提出3D感知模糊合成器，从3D空间估计相机和物体运动以生成多样且真实的模糊图像。相比2D非均匀核方法，其模糊模式更符合物理成像。实验表明该方法能有效增强模糊数据多样性。其可控模糊合成可服务于计算摄影模糊管线，但主要针对运动模糊而非景深散景。

### 3. 对应检索需求
point spread function synthesis for blur。

### 4. 来源与原文
- Source：ICLR-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=Wvi8c0tgvt](https://openreview.net/forum?id=Wvi8c0tgvt)
