---
title: Online 3D Instance Segmentation at task-oriented granularity with Unposed Monocular Video
title_zh: 基于无位姿单目视频的任务导向在线三维实例分割
authors: "Dong Wu, Baicheng Li, Yingdian Cao, Shunkai Zhou, Yiwen Lu, Hongbin Zha"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=4wJjkGE90n"
tags: ["query:seg"]
score: 6.0
evidence: 结合开放词汇检测器的在线三维实例分割
tldr: 现有三维实例分割多采用自底向上先分割后识别的范式，难以适应开放世界中具身智能体的任务需求。本文提出面向无位姿单目视频的实时任务导向三维实例分割框架，用开放词汇检测器与提示式二维分割模型解耦每帧物体，同时借助稠密SLAM重建场景几何。以SLAM位姿图引导多视图掩码关联并复用稠密对应关系。该工作实现了任务自适应的开放世界感知与交互，为具身智能提供新范式。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有自底向上分割先分割后识别，难适应开放世界任务需求。
method: 结合开放词汇检测器与提示式二维分割，并用SLAM关联多视图掩码。
result: 实现实时任务导向三维实例分割，可自适应感知开放场景物体。
conclusion: 为具身智能体的开放世界感知与交互提供新范式。
---

## Abstract
We present a real-time, task-oriented 3D instance segmentation framework for unposed monocular video, enabling embodied agents to task-adaptively perceive and interact with objects in open-world scenes. Unlike most previous bottom-up segmentation paradigm that segment before recognition, we adopt a task-oriented segmentation approach. Specifically, objects are decoupled within each frame using an open-vocabulary detector combined with a prompt-based 2D segmentation model, while the 3D underlying geometry of the scene is simultaneously being reconstructed using a modern dense SLAM system. Guided by the SLAM-derived pose graph, we selectively associate multi-view masks and reuse the dense correspondences provided by the SLAM system, incrementally converting them into geometric association scores with minimal additional computation. By incorporating semantic similarity and mutual exclusivity metrics, we design a priority-ordered mask clustering algorithm for efficient online multi-view mask matching and merging. Evaluations on open-vocabulary 3D instance segmentation benchmarks show that our method effectively mitigates the performance degradation of existing approaches when using dense SLAM reconstructions instead of depth-sensor point clouds. On the Replica dataset, using only unposed images, it even achieves results comparable to methods leveraging ground-truth depth and poses. Codes will be released upon acceptance of the paper.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
结合开放词汇检测器的在线三维实例分割。

### 2. 核心内容
现有三维实例分割多采用自底向上先分割后识别的范式，难以适应开放世界中具身智能体的任务需求。本文提出面向无位姿单目视频的实时任务导向三维实例分割框架，用开放词汇检测器与提示式二维分割模型解耦每帧物体，同时借助稠密SLAM重建场景几何。以SLAM位姿图引导多视图掩码关联并复用稠密对应关系。该工作实现了任务自适应的开放世界感知与交互，为具身智能提供新范式。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=4wJjkGE90n](https://openreview.net/forum?id=4wJjkGE90n)
