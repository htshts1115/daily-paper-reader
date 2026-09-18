---
title: Polysemous Language Gaussian Splatting via Matching-based Mask Lifting
title_zh: 基于匹配式掩码提升的多义语言高斯泼溅
authors: "Jiayu Ding, Xinpeng Liu, Zhiyi Pan, Shiqiang Long, Ge Li"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=K6AYxvp3jl"
tags: ["query:seg"]
score: 5.0
evidence: 开放词汇理解经二维掩码提升与前景概率
tldr: 将二维开放词汇理解提升到三维高斯场景是重要挑战，但主流方法依赖逐场景重训练、只能表示单一语义且易受跨视角不一致影响。论文提出免训练框架MUSplat，完全放弃特征优化，利用预训练二维分割模型生成并提升多粒度掩码，为每个高斯点估计前景概率。该方法实现即插即用的多义语义表示并缓解跨视角不一致。其掩码提升与前景概率估计思路对开放词汇分割与前景分离具有借鉴意义。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 将二维开放词汇理解提升到三维高斯场景的方法依赖逐场景重训练，且只能表示单一语义。
method: 提出免训练框架MUSplat，用预训练二维分割模型生成并提升多粒度掩码，估计每个高斯的前景概率。
result: 缓解跨视角语义不一致，实现即插即用的三维开放词汇多义语义表示。
conclusion: 表明免特征优化的掩码提升可支撑复杂多概念语义的三维场景理解。
---

## Abstract
Lifting 2D open-vocabulary understanding into 3D Gaussian Splatting (3DGS) scenes is a critical challenge. However, mainstream methods suffer from three key flaws:  (i) their reliance on costly per-scene retraining prevents plug-and-play application; (ii) their restrictive monosemous design fails to represent complex, multi-concept semantics; and (iii) their vulnerability to cross-view semantic inconsistencies corrupts the final semantic representation.
To overcome these limitations, we introduce MUSplat, a training-free framework that abandons feature optimization entirely. Leveraging a pre-trained 2D segmentation model, our pipeline generates and lifts multi-granularity 2D masks into 3D, where we estimate a foreground probability for each Gaussian point to form initial object groups. We then optimize the ambiguous boundaries of these initial groups using semantic entropy and geometric opacity. Subsequently, by interpreting the object's appearance across its most representative viewpoints, a Vision-Language Model (VLM) distills robust textual
features that reconciles visual inconsistencies, enabling open-vocabulary querying via semantic matching.
By eliminating the costly per-scene training process, MUSplat reduces scene adaptation time from hours to mere minutes.
On benchmark tasks for open-vocabulary 3D object selection and semantic segmentation, MUSplat outperforms established training-based frameworks while simultaneously addressing their monosemous limitations.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
开放词汇理解经二维掩码提升与前景概率。

### 2. 核心内容
将二维开放词汇理解提升到三维高斯场景是重要挑战，但主流方法依赖逐场景重训练、只能表示单一语义且易受跨视角不一致影响。论文提出免训练框架MUSplat，完全放弃特征优化，利用预训练二维分割模型生成并提升多粒度掩码，为每个高斯点估计前景概率。该方法实现即插即用的多义语义表示并缓解跨视角不一致。其掩码提升与前景概率估计思路对开放词汇分割与前景分离具有借鉴意义。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=K6AYxvp3jl](https://openreview.net/forum?id=K6AYxvp3jl)
