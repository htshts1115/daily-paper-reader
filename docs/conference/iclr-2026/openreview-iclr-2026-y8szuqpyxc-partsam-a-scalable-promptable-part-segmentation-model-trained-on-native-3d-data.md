---
title: "PartSAM: A Scalable Promptable Part Segmentation Model Trained on Native 3D Data"
title_zh: PartSAM：基于原生三维数据训练的可扩展可提示部件分割模型
authors: "Zhe Zhu, Le Wan, Rui Xu, Yiheng Zhang, Honghua Chen, Zhiyang Dou, Cheng Lin, Yuan Liu, Mingqiang Wei"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=y8sZUQPYXC"
tags: ["query:seg"]
score: 5.0
evidence: 遵循SAM设计的可提示部件分割模型
tldr: 将三维物体分割成部件是长期挑战，现有开放世界方法多借助SAM等二维基础模型，把多视图掩码提升到三维，但这种间接范式无法捕捉内在几何，导致理解仅停留在表面、分解不可控且泛化受限。本文提出PartSAM，首个在大规模三维数据上原生训练的可提示部件分割模型，沿用SAM的编码器-解码器思路，采用基于三平面的双分支编码器。该工作提升了部件分割对未见物体的泛化能力，为三维部件分割提供可扩展的新范式。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有开放世界部件分割依赖二维基础模型提升监督，几何理解不足。
method: 提出首个原生三维训练的可提示部件分割模型，采用三平面双分支编码器。
result: 克服表面化理解与分解失控问题，提升对未见物体的泛化能力。
conclusion: 为三维部件分割提供可扩展的原生三维建模范式。
---

## Abstract
Segmenting 3D objects into parts is a long-standing challenge in computer vision. To overcome taxonomy constraints and generalize to unseen 3D objects, recent works turn to open-world part segmentation. These approaches typically transfer supervision from 2D foundation models, such as SAM, by lifting multi-view masks into 3D. However, this indirect paradigm fails to capture intrinsic geometry, leading to surface-only understanding, uncontrolled decomposition, and limited generalization. We present PartSAM, the first promptable part segmentation model trained natively on large-scale 3D data. Following the design philosophy of SAM, PartSAM employs an encoder–decoder architecture in which a triplane-based dual-branch encoder produces spatially structured tokens for scalable part-aware representation learning. To enable large-scale supervision, we further introduce a model-in-the-loop annotation pipeline that curates over five million 3D shape–part pairs from online assets, providing diverse and fine-grained labels. This combination of scalable architecture and diverse 3D data yields emergent open-world capabilities: with a single prompt, PartSAM achieves highly accurate part identification, and in a “Segment-Every-Part” mode, it automatically decomposes shapes into both surface and internal structures. Extensive experiments show that PartSAM outperforms state-of-the-art methods by large margins across multiple benchmarks, marking a decisive step toward foundation models for 3D part understanding.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
遵循SAM设计的可提示部件分割模型。

### 2. 核心内容
将三维物体分割成部件是长期挑战，现有开放世界方法多借助SAM等二维基础模型，把多视图掩码提升到三维，但这种间接范式无法捕捉内在几何，导致理解仅停留在表面、分解不可控且泛化受限。本文提出PartSAM，首个在大规模三维数据上原生训练的可提示部件分割模型，沿用SAM的编码器-解码器思路，采用基于三平面的双分支编码器。该工作提升了部件分割对未见物体的泛化能力，为三维部件分割提供可扩展的新范式。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=y8sZUQPYXC](https://openreview.net/forum?id=y8sZUQPYXC)
