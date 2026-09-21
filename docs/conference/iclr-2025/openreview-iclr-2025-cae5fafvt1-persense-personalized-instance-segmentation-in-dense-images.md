---
title: "PerSense: Personalized Instance Segmentation in Dense Images"
title_zh: PerSense：稠密图像中的个性化实例分割
authors: "Muhammad Ibraheem Siddiqui, Muhammad Umer Sheikh, Hassan Abid, Muhammad Haris Khan"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=caE5faFVT1"
tags: ["query:seg"]
score: 4.0
evidence: 稠密图像中的个性化实例分割
tldr: 现有分割模型在严重遮挡、尺度变化和背景杂乱的稠密拥挤场景中，难以自动分割出目标物体的个性化实例。作者提出端到端、免训练、模型无关的一次性框架PerSense，并构建可自动生成目标的基线方法用于个性化实例分割。实验表明PerSense能在密集场景中更准确地勾画目标实例，缓解遮挡与尺度带来的困难。该框架对实例与前景分割具有方法借鉴意义，但未专门针对人像前景或虚化场景。
source: ICLR-2025-Rejected-Public
selection_source: conference_retrieval
motivation: 现有分割模型在严重遮挡、尺度变化和背景杂乱的稠密场景中难以自动分割个性化实例。
method: 作者提出端到端、免训练、模型无关的一次性框架PerSense，并构建自动生成目标的基线。
result: 实验表明PerSense能在密集场景中更准确地勾画目标实例，缓解遮挡与尺度挑战。
conclusion: 该框架对实例与前景分割有方法借鉴意义，但未专门针对人像或虚化场景。
---

## Abstract
Leveraging large-scale pre-training, vision foundational models showcase notable performance benefits. Recent segmentation algorithms for natural scenes have advanced significantly. However, existing models still struggle to automatically segment personalized instances in dense and crowded scenarios, where severe occlusions, scale variations, and background clutter pose a challenge to accurately delineate densely packed instances of the target object. To address this, we propose **PerSense**, an end-to-end, training-free, and model-agnostic one-shot framework for **Per**sonalized instance **S**egmentation in d**ense** images. Towards developing this framework, we make the following core contributions. **(a)** We develop a new baseline capable of automatically generating instance-level point prompts via proposing a novel Instance Detection Module (IDM) that leverages density maps, encapsulating spatial distribution of objects in an image. **(b)** To mitigate false positives within generated point prompts, we design Point Prompt Selection Module (PPSM). Both IDM and PPSM transform density maps into personalized precise point prompts for instance-level segmentation and offer a seamless integration in our model-agnostic framework. **(c)** We introduce a feedback mechanism which enables PerSense to improve the accuracy of density maps by automating the exemplar selection process for density map generation. **(d)** To promote algorithmic advances and effective tools for this relatively underexplored task, we introduce PerSense-D, a diverse dataset exclusive to personalized instance segmentation in dense images. Our extensive experiments establish PerSense superiority in dense scenarios by achieving an mIoU of **71.61%** on PerSense-D, outperforming recent SOTA models by significant margins of **+47.16%**, **+42.27%**, **+8.83%**, and **+5.69%**. Additionally, our qualitative findings demonstrate the adaptability of our framework to images captured in-the-wild.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
稠密图像中的个性化实例分割。

### 2. 核心内容
现有分割模型在严重遮挡、尺度变化和背景杂乱的稠密拥挤场景中，难以自动分割出目标物体的个性化实例。作者提出端到端、免训练、模型无关的一次性框架PerSense，并构建可自动生成目标的基线方法用于个性化实例分割。实验表明PerSense能在密集场景中更准确地勾画目标实例，缓解遮挡与尺度带来的困难。该框架对实例与前景分割具有方法借鉴意义，但未专门针对人像前景或虚化场景。

### 3. 对应检索需求
Papers central to 人像分割、人体分割、前景分割，重点关注虚化场景中的主体完整性和手持物归属。, especially work that connects or combines: open-vocabulary segmentation; instance segmentation; semantic segmentation; Portrait segmentation for subject integrity in blur; Human segmentation algorithm with handheld object detection; Foreground segmentation in defocused images; foreground segmentation for handheld objects accessories and portrait scenes; segmentation model for thin structures hair boundaries and occlusions.

### 4. 来源与原文
- Source：ICLR-2025-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=caE5faFVT1](https://openreview.net/forum?id=caE5faFVT1)
