---
title: "No time to train! Training-Free Reference-Based Instance Segmentation"
title_zh: 无需训练！基于参考的免训练实例分割
authors: "Miguel Espinosa, Chenhongyi Yang, Linus Ericsson, Steven McDonagh, Elliot J. Crowley"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=fEZ6DqfwTR"
tags: ["query:seg"]
score: 7.0
evidence: 利用基础模型先验的免训练参考式实例分割
tldr: 针对SAM仍需人工提示或复杂提示生成规则的问题，本文研究仅给定少量参考图像时的目标分割任务。核心思想是利用基础模型学到的强语义先验，在参考图与目标图之间建立对应关系，从而自动生成分割提示。实验证明该免训练方法能有效完成参考式实例分割，减轻了新图像处理时的提示负担。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: SAM仍需人工视觉提示或复杂的域相关提示生成规则，处理新图像负担较重。
method: 利用基础模型的强语义先验，在参考图与目标图间建立区域对应以自动生成分割结果。
result: 在仅有少量参考图像的条件下实现了有效的免训练目标实例分割。
conclusion: 证明语义对应关系可替代人工提示，推动参考式分割的免训练化。
---

## Abstract
The performance of image segmentation models has historically been constrained by the high cost of collecting large-scale annnotated data. The Segment Anything Model (SAM) alleviates this original problem through a promptable, semantics-agnostic, segmentation paradigm and yet still requires manual visual-prompts or complex domain-dependent prompt-generation rules to process a new image. Towards reducing this new burden, our work investigates the task of object segmentation when provided with, alternatively, only a small set of reference images. Our key insight is to leverage strong semantic priors, as learned by foundation models, to identify corresponding regions between a reference and a target image. We find that correspondences enable automatic generation of instance-level segmentation masks for downstream tasks and instantiate our ideas via a multi-stage, training-free method incorporating (1) memory bank construction; (2) representation aggregation and (3) semantic-aware feature matching. Our experiments show significant improvements on segmentation metrics, leading to state-of-the-art performance on COCO FSOD (36.8% nAP), PASCAL VOC Few-Shot (71.2% nAP50) and outperforming existing training-free approaches on the Cross-Domain FSOD benchmark (22.4% nAP).

---

## 论文详细总结（自动生成）

### 1. 检索相关性
利用基础模型先验的免训练参考式实例分割。

### 2. 核心内容
针对SAM仍需人工提示或复杂提示生成规则的问题，本文研究仅给定少量参考图像时的目标分割任务。核心思想是利用基础模型学到的强语义先验，在参考图与目标图之间建立对应关系，从而自动生成分割提示。实验证明该免训练方法能有效完成参考式实例分割，减轻了新图像处理时的提示负担。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=fEZ6DqfwTR](https://openreview.net/forum?id=fEZ6DqfwTR)
