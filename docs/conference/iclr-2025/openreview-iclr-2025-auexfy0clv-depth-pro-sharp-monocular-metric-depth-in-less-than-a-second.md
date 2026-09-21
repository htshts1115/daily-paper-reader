---
title: "Depth Pro: Sharp Monocular Metric Depth in Less Than a Second"
title_zh: Depth Pro：亚秒级锐利单目度量深度估计
authors: "Alexey Bochkovskiy, Amaël Delaunoy, Hugo Germain, Marcel Santos, Yichao Zhou, Stephan Richter, Vladlen Koltun"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=aueXfY0Clv"
tags: ["query:mono-depth"]
score: 9.0
evidence: 零样本度量单目深度基础模型
tldr: 单目深度估计长期面临尺度模糊与边界不锐利的问题，且依赖相机内参等元数据。本文提出Depth Pro，一个零样本度量单目深度基础模型，采用高效多尺度视觉Transformer与真实合成混合训练策略，可在0.3秒内生成225万像素、边界锐利的度量深度图，无需相机内参。该工作为高质量、快速、可泛化的深度估计提供了新基准。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 现有单目深度估计存在尺度模糊、边界不锐利且依赖相机内参等问题，难以快速获得度量深度。
method: 提出Depth Pro基础模型，采用高效多尺度视觉Transformer与真实合成混合训练协议，实现零样本度量深度估计。
result: 可在0.3秒内生成225万像素、边界锐利的度量深度图，且无需相机内参。
conclusion: 为快速、可泛化、高精度的单目度量深度估计树立新基准。
---

## Abstract
We present a foundation model for zero-shot metric monocular depth estimation. Our model, Depth Pro, synthesizes high-resolution depth maps with unparalleled sharpness and high-frequency details. The predictions are metric, with absolute scale, without relying on the availability of metadata such as camera intrinsics. And the model is fast, producing a 2.25-megapixel depth map in 0.3 seconds on a standard GPU. These characteristics are enabled by a number of technical contributions, including an efficient multi-scale vision transformer for dense prediction, a training protocol that combines real and synthetic datasets to achieve high metric accuracy alongside fine boundary tracing, dedicated evaluation metrics for boundary accuracy in estimated depth maps, and state-of-the-art focal length estimation from a single image. Extensive experiments analyze specific design choices and demonstrate that Depth Pro outperforms prior work along multiple dimensions. We release code & weights at https://github.com/apple/ml-depth-pro

---

## 论文详细总结（自动生成）

### 1. 检索相关性
零样本度量单目深度基础模型。

### 2. 核心内容
单目深度估计长期面临尺度模糊与边界不锐利的问题，且依赖相机内参等元数据。本文提出Depth Pro，一个零样本度量单目深度基础模型，采用高效多尺度视觉Transformer与真实合成混合训练策略，可在0.3秒内生成225万像素、边界锐利的度量深度图，无需相机内参。该工作为高质量、快速、可泛化的深度估计提供了新基准。

### 3. 对应检索需求
Papers central to 单目深度估计，用于人像虚化、主体背景层次、手持物和头戴物深度判断。, especially work that connects or combines: monocular depth estimation; relative depth prediction; metric depth estimation; zero-shot depth estimation; depth foundation model; Depth Anything model; monocular depth estimation for portrait bokeh and mobile photography; lightweight depth model for mobile devices; monocular depth estimation for thin structures transparent objects and handheld objects; depth foundation model for zero shot generalization in real world images.

### 4. 来源与原文
- Source：ICLR-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=aueXfY0Clv](https://openreview.net/forum?id=aueXfY0Clv)
