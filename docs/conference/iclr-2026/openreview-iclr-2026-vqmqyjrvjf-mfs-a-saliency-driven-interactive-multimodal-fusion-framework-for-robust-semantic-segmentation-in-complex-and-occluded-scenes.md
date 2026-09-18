---
title: "MFS: A Saliency Driven Interactive Multimodal Fusion Framework for Robust Semantic Segmentation in Complex and Occluded Scenes"
title_zh: MFS：面向复杂与遮挡场景鲁棒语义分割的显著性驱动交互式多模态融合框架
authors: Qiangxi Zhu
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=vQmqyjRVjf"
tags: ["query:seg"]
score: 6.0
evidence: 遮挡场景下的鲁棒语义分割
tldr: 针对复杂场景下语义分割难以检测远处弱小目标以及识别被遮挡物体的问题，本文提出一种基于频域动态路由与激活区域引导的交互式多模态语义分割框架。该框架包含边缘特征增强等三个核心模块，对多模态特征进行细粒度选择与融合，从而提升特征提取能力、融合鲁棒性和语义表征。实验表明该方法在复杂与遮挡场景下分割更稳健，为多模态分割提供了可迁移的融合思路。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 复杂场景中语义分割难以检测远处弱小目标并识别被遮挡物体，现有多模态融合鲁棒性不足。
method: 提出基于频域动态路由与激活区域引导的交互式多模态分割框架，含边缘特征增强等三个核心模块。
result: 该方法增强了特征提取与融合鲁棒性，在复杂和遮挡场景下取得更优的语义分割表现。
conclusion: 为多模态鲁棒语义分割提供了新的融合与增强范式，可迁移至遮挡场景分割任务。
---

## Abstract
In complex scenes, semantic segmentation often encounters challenges such as difficulty in detecting distant small or weak targets and recognizing occluded objects. Existing methods still suffer from limited robustness and suboptimal multimodal feature fusion. To address these issues, this paper proposes an interactive multimodal semantic segmentation framework based on frequency domain dynamic routing and activation region guidance, which effectively enhances the feature extraction capability, fusion robustness, and semantic representation of multimodal images. The proposed framework consists of three core modules: first, an edge feature enhancement module that performs fine-grained selection of key regions on the initial features to enhance weak targets and edge details; second, an activation region guided hybrid attention module that effectively fuses prominent region information from infrared and visible modalities; and finally, a deep semantic enhancement learning module that incorporates dynamic convolutional masks to improve the semantic consistency of fused features at both global and local levels. Experimental results on multiple public datasets demonstrate that the proposed method outperforms existing approaches in terms of image fusion quality, segmentation accuracy, and object detection performance, showing especially strong robustness and generalization ability in complex and occluded scenes.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
遮挡场景下的鲁棒语义分割。

### 2. 核心内容
针对复杂场景下语义分割难以检测远处弱小目标以及识别被遮挡物体的问题，本文提出一种基于频域动态路由与激活区域引导的交互式多模态语义分割框架。该框架包含边缘特征增强等三个核心模块，对多模态特征进行细粒度选择与融合，从而提升特征提取能力、融合鲁棒性和语义表征。实验表明该方法在复杂与遮挡场景下分割更稳健，为多模态分割提供了可迁移的融合思路。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=vQmqyjRVjf](https://openreview.net/forum?id=vQmqyjRVjf)
