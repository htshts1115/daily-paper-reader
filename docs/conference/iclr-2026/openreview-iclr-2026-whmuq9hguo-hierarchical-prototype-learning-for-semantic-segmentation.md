---
title: Hierarchical Prototype Learning for Semantic Segmentation
title_zh: 面向语义分割的层次化原型学习
authors: "Seoha Lim, Jinmyeong Kim, Jieun Kim, Sung-Bae Cho"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=wHMuQ9HgUo"
tags: ["query:seg"]
score: 6.0
evidence: 面向语义分割的层次化原型学习
tldr: 传统语义分割方法因缺少部件级与物体级语义的关联，难以区分同一物体内部的细粒度部件。论文提出层次化原型分割HiPoSeg，构建同时刻画抽象物体级表征与细节部件级特征的结构化原型空间，并采用层次对比学习对齐不同层级语义。实验表明该方法增强了类内判别与部件级区分能力。该工作为细粒度分割提供了层次化表征的通用思路。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 传统语义分割因缺少部件级与物体级语义的关联，难以区分同一物体内的细粒度部件。
method: 提出HiPoSeg，构建结构化原型空间并采用层次对比学习对齐物体级与部件级表征。
result: 提升类内判别与部件级区分能力，改善细粒度语义分割效果。
conclusion: 表明层次化原型可有效连接部件与整体语义，为细粒度分割提供通用思路。
---

## Abstract
Conventional semantic segmentation methods often fail to distinguish fine-grained parts within the same object because of missing links between part-level cues and object-level semantics.
Inspired by how humans recognize objects, which involves first identifying them as a whole and then distinguishing their parts, we propose a hierarchical prototype-based segmentation method called Hierarchical Prototype Segmentation (HiPoSeg). This builds a structured prototype space that captures both abstract object-level representations and detailed part-level features, enabling consistent alignment between levels. HiPoSeg leverages a hierarchical contrastive learning strategy to structure semantic representations across levels, encouraging both intra-level discrimination and cross-level consistency.
Experiments on standard benchmarks such as Cityscapes, ADE20K, Mapillary Vistas 2.0, and PASCAL-Part-108 demonstrate that HiPoSeg produces consistent performance improvement with an average gain of +3.07\%p mIoU without any additional inference cost.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向语义分割的层次化原型学习。

### 2. 核心内容
传统语义分割方法因缺少部件级与物体级语义的关联，难以区分同一物体内部的细粒度部件。论文提出层次化原型分割HiPoSeg，构建同时刻画抽象物体级表征与细节部件级特征的结构化原型空间，并采用层次对比学习对齐不同层级语义。实验表明该方法增强了类内判别与部件级区分能力。该工作为细粒度分割提供了层次化表征的通用思路。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=wHMuQ9HgUo](https://openreview.net/forum?id=wHMuQ9HgUo)
