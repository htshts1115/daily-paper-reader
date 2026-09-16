---
title: "ST$^2$360D: Spatial-to-Temporal Consistency for Training-free 360 Monocular Depth Estimation"
title_zh: ST2-360D：面向免训练360度单目深度估计的空间到时序一致性
authors: "Zidong Cao, Jinjing Zhu, Hao Ai, Lutao Jiang, Yuanhuiyi Lyu, Hui Xiong"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=d0bm4upnQ8"
tags: ["query:mono-depth"]
score: 7.0
evidence: 免训练的360度单目深度估计
tldr: 360度单目深度估计因等距柱状投影畸变，常被切成独立透视块处理，导致块间尺度漂移与深度不一致。本文借鉴视频深度估计的时序一致性，将360度图像表示为透视帧序列，提出空间到时序一致性方法实现免训练深度估计。该方法在不需训练的情况下缓解尺度漂移，直接契合单目深度估计与免训练零样本需求。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 360度图像投影畸变使分块独立处理产生尺度漂移和深度不一致。
method: 将360度图像表示为透视帧序列，借鉴视频深度模型用空间到时序一致性估计深度。
result: 实现免训练的360度单目深度估计，缓解块间尺度漂移问题。
conclusion: 为360度单目深度估计提供免训练一致方案，契合单目与零样本深度需求。
---

## Abstract
360-degree monocular depth estimation plays a crucial role in scene understanding owing to its 180-degree by 360-degree field-of-view (FoV). To mitigate the distortions brought by equirectangular projection, existing methods typically divide 360-degree images into distortion-less perspective patches. However, since these patches are processed independently, depth inconsistencies are often introduced due to scale drift among patches. Recently, video depth estimation (VDE) models have leveraged temporal consistency for stable depth predictions across frames. Inspired by this, we propose to represent a 360-degree image as a sequence of perspective frames, mimicking the viewpoint adjustments users make when exploring a 360-degree scenario in virtual reality. Thus, the spatial consistency among perspective depth patches can be enhanced by exploiting the temporal consistency inherent in VDE models. To this end, we introduce a training-free pipeline for 360-degree monocular depth estimation, called ST²360D. Specifically, ST²360D transforms a 360-degree image into perspective video frames, predicts video depth maps using VDE models, and seamlessly merges these predictions into a complete 360-degree depth map. To generate sequenced perspective frames that align with VDE models, we propose two tailored strategies. First, a spherical-uniform sampling (SUS) strategy is proposed to facilitate uniform sampling of perspective views across the sphere, avoiding oversampling in polar regions typically with limited structural details. Second, a latitude-guided scanning (LGS) strategy is introduced to organize the frames into a coherent sequence, starting from the equator, prioritizing low-latitude slices, and progressively moving toward higher latitudes. Extensive experiments demonstrate that ST²360D achieves strong zero-shot capability on several datasets, supporting resolutions up to 4K.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
免训练的360度单目深度估计。

### 2. 核心内容
360度单目深度估计因等距柱状投影畸变，常被切成独立透视块处理，导致块间尺度漂移与深度不一致。本文借鉴视频深度估计的时序一致性，将360度图像表示为透视帧序列，提出空间到时序一致性方法实现免训练深度估计。该方法在不需训练的情况下缓解尺度漂移，直接契合单目深度估计与免训练零样本需求。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=d0bm4upnQ8](https://openreview.net/forum?id=d0bm4upnQ8)
