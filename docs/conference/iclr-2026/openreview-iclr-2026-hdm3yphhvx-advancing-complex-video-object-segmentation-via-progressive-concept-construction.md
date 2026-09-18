---
title: Advancing Complex Video Object Segmentation via Progressive Concept Construction
title_zh: 通过渐进式概念构建推进复杂视频目标分割
authors: "Zhixiong Zhang, Shuangrui Ding, Xiaoyi Dong, Songxin He, Jianfan Lin, Junsong Tang, Yuhang Zang, Yuhang Cao, Dahua Lin, Jiaqi Wang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=hDM3YphhVx"
tags: ["query:seg"]
score: 4.0
evidence: 概念驱动的视频目标分割
tldr: 针对视频目标分割在需要高层语义推理时鲁棒性不足的问题，本文提出Segment Concept框架，用大视觉语言模型跨帧构建以物体为中心的概念先验，仅在场景切换时调用模型以兼顾语义推理与开销。作者还构建了面向复杂语义场景的SeCVOS基准。实验显示该概念驱动方式在复杂场景下分割更稳健，为视频目标分割提供了新思路。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 视频目标分割在需要高层概念推理和语义理解时鲁棒性不足，特征匹配范式受限。
method: 提出概念驱动的SeC框架，用大视觉语言模型跨帧构建物体中心概念先验，仅在场景切换时调用。
result: 构建SeCVOS复杂场景基准，实验表明概念驱动方法在复杂语义场景下分割更稳健。
conclusion: 将高层概念表示引入视频目标分割，为复杂场景分割提供了新的建模范式。
---

## Abstract
We propose Segment Concept (SeC), a concept-driven video object segmentation (VOS) framework that shifts from conventional feature matching to the progressive construction and utilization of high-level, object-centric representations. SeC employs Large Vision-Language Models (LVLMs) to integrate visual cues across diverse frames, constructing robust conceptual priors. To balance semantic reasoning with computational overhead, SeC forwards the LVLMs only when a new scene appears, injecting concept-level features at those points.
To rigorously assess VOS methods in scenarios demanding high-level conceptual reasoning and robust semantic understanding, we introduce the Semantic Complex Scenarios Video Object Segmentation benchmark (SeCVOS). SeCVOS comprises 160 manually annotated multi-scenario videos designed to challenge models with substantial appearance variations and dynamic scene transformations. Empirical evaluations demonstrate that SeC substantially outperforms state-of-the-art approaches, including SAM 2 and its advanced variants, on both SeCVOS and standard VOS benchmarks. In particular, SeC achieves an 11.8-point improvement over SAM 2.1 on SeCVOS, establishing a new state-of-the-art in concept-aware VOS.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
概念驱动的视频目标分割。

### 2. 核心内容
针对视频目标分割在需要高层语义推理时鲁棒性不足的问题，本文提出Segment Concept框架，用大视觉语言模型跨帧构建以物体为中心的概念先验，仅在场景切换时调用模型以兼顾语义推理与开销。作者还构建了面向复杂语义场景的SeCVOS基准。实验显示该概念驱动方式在复杂场景下分割更稳健，为视频目标分割提供了新思路。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=hDM3YphhVx](https://openreview.net/forum?id=hDM3YphhVx)
