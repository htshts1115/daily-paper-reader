---
title: "NOCTIS: Novel Object Cyclic Threshold based Instance Segmentation"
title_zh: NOCTIS：基于循环阈值的新物体实例分割
authors: "Max Gandyra, Alessandro Santonicola, Michael Beetz"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=H8UFAU9gJ2"
tags: ["query:seg"]
score: 7.0
evidence: 基于Grounded-SAM与DINOv2的免训练实例分割
tldr: 针对新类别物体实例分割难以泛化、需反复训练的问题，本文提出免训练框架NOCTIS。方法集成Grounded-SAM 2生成带精确框与掩码的候选，并利用DINOv2的零样本能力提供类别与patch嵌入，通过循环阈值匹配分数完成候选与目标匹配。实验表明该方法无需再训练即可适应多种新物体，为开放场景实例分割提供了通用方案。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有实例分割模型难以在无需重训练的情况下泛化到各种新物体类别。
method: 集成Grounded-SAM 2生成候选框与掩码，结合DINOv2零样本嵌入并用循环阈值相似度完成目标匹配。
result: 无需任何再训练即可对新物体实现精确的实例分割与定位。
conclusion: 提出免训练的通用实例分割框架，验证了基础模型组合在开放场景中的有效性。
---

## Abstract
Instance segmentation of novel objects instances in RGB images, given some example images for each object, is a well known problem in computer vision.
Designing a model general enough to be employed for all kinds of novel objects without (re-) training has proven to be a difficult task.
To handle this, we present a new training-free framework, called: Novel Object Cyclic Threshold based Instance Segmentation (NOCTIS).
NOCTIS integrates two pre-trained models: Grounded-SAM 2 for object proposals with precise bounding boxes and corresponding segmentation masks; and DINOv2 for robust class and patch embeddings, due to its zero-shot capabilities.
Internally, the proposal-object matching is realized by determining an object matching score based on the similarity of the class embeddings and the average maximum similarity of the patch embeddings with a new cyclic thresholding (CT) mechanism that mitigates unstable matches caused by repetitive textures or visually similar patterns.
Beyond CT, NOCTIS introduces: (i) an appearance score that is unaffected by object selection bias; (ii) the usage of the average confidence of the proposals’ bounding box and mask as a scoring component; and (iii) an RGB-only pipeline that performs even better than RGB-D ones.
We empirically show that NOCTIS, without further training/fine tuning, attains state-of-the-art results regarding the mean AP score, w.r.t. the best RGB and RGB-D methods on the seven core datasets of the BOP 2023 challenge for the ''Model-based 2D segmentation of unseen objects'' task.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于Grounded-SAM与DINOv2的免训练实例分割。

### 2. 核心内容
针对新类别物体实例分割难以泛化、需反复训练的问题，本文提出免训练框架NOCTIS。方法集成Grounded-SAM 2生成带精确框与掩码的候选，并利用DINOv2的零样本能力提供类别与patch嵌入，通过循环阈值匹配分数完成候选与目标匹配。实验表明该方法无需再训练即可适应多种新物体，为开放场景实例分割提供了通用方案。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=H8UFAU9gJ2](https://openreview.net/forum?id=H8UFAU9gJ2)
