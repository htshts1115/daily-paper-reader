---
title: "Granular Computing-driven SAM: From Coarse-to-fine Guidance for Prompt-free Segmentation"
title_zh: 粒度计算驱动的SAM：面向免提示分割的由粗到细引导
authors: "Qiyang Yu, Yu Fang, Xuemei Cao, Yan Chen, Jianghao Li, Fan Min, Tianrui Li, Yi Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=ZMliZK1Wh9"
tags: ["query:seg"]
score: 6.0
evidence: 免提示分割与前景定位
tldr: 现有免提示分割模型如SAM仅在单一粒度生成提示，缺乏自主区域定位与高分辨率细粒度建模能力。论文提出粒度计算驱动的Grc-SAM，先以粗阶段自适应提取高响应区域完成前景定位，再以细阶段进行高分辨率精细掩码生成。实验表明该粗到细框架提升了分割精度并减少对外部提示的依赖。该工作为前景分割与细结构掩码提供了可迁移的无提示方案。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: SAM等模型仅在单一粒度生成提示，缺乏自主区域定位与高分辨率细粒度建模能力。
method: 提出粒度计算驱动的Grc-SAM，粗阶段自适应提取高响应区域定位前景，细阶段细化掩码。
result: 在免提示分割基准上提升掩码精度，并降低对外部提示的依赖。
conclusion: 表明粒度计算可有效支撑免提示分割，为前景定位与细粒度分割提供通用方案。
---

## Abstract
Prompt-free image segmentation aims to generate accurate masks without manual guidance. Typical pre-trained models, notably Segmentation Anything Model (SAM), generate prompts directly at a single granularity level. However, this approach has two limitations: (1) Localizability, lacking mechanisms for autonomous region localization; (2) Scalability, limited fine-grained modeling at high resolution. To address these challenges, we introduce Granular Computing-driven SAM (Grc-SAM), a coarse-to-fine framework motivated by Granular Computing (GrC). First, the coarse stage adaptively extracts high-response regions from features to achieve precise foreground localization and reduce reliance on external prompts. Second, the fine stage applies finer patch partitioning with sparse local swin-style attention to enhance detail modeling and enable high-resolution segmentation. Third, refined masks are encoded as latent prompt embeddings for the SAM decoder, replacing handcrafted prompts with an automated reasoning process. By integrating multi-granularity attention, Grc-SAM bridges granular computing with vision transformers. Extensive experimental results demonstrate Grc-SAM outperforms baseline methods in both accuracy and scalability. It offers a unique granular computational perspective for prompt-free segmentation.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
免提示分割与前景定位。

### 2. 核心内容
现有免提示分割模型如SAM仅在单一粒度生成提示，缺乏自主区域定位与高分辨率细粒度建模能力。论文提出粒度计算驱动的Grc-SAM，先以粗阶段自适应提取高响应区域完成前景定位，再以细阶段进行高分辨率精细掩码生成。实验表明该粗到细框架提升了分割精度并减少对外部提示的依赖。该工作为前景分割与细结构掩码提供了可迁移的无提示方案。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=ZMliZK1Wh9](https://openreview.net/forum?id=ZMliZK1Wh9)
