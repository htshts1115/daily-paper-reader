---
title: Open-Set Domain Generalization for Semantic Segmentation
title_zh: 面向语义分割的开放集域泛化
authors: "Seun-An Choe, Keonhee Park, Jinwoo Choi, Gyeong-Moon Park"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=gNgyV2dPAK"
tags: ["query:seg"]
score: 6.0
evidence: 面向语义分割的开放集域泛化
tldr: 开放集域泛化语义分割要求在训练中完全未见的域里既分割已知类又识别未知类，而现有域泛化方法在开放集下常把未知物体误判为已知类。论文提出统一框架显式建模未知，先用Stable Diffusion生成逼真的未知物体插入源图像提供监督，再通过分割头扩展学习未知感知表示，并提升对语义与视觉域偏移的鲁棒性。实验表明该方法在开放集设置下能更好识别未知类并保持已知类分割性能。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 开放集域泛化语义分割需在未见目标域中分割已知类并识别未知类，现有域泛化方法在开放集下易把未知误判为已知。
method: 提出统一框架，用Stable Diffusion生成逼真未知物体插入源图，通过分割头扩展学习未知感知表示，提升语义与视觉域偏移鲁棒性。
result: 在开放集域泛化设置下，该方法能更好地识别未知类别并保持已知类分割性能。
conclusion: 表明显式建模未知并扩充分割头可有效提升开放集域泛化语义分割的鲁棒性。
---

## Abstract
Open-Set domain generalization for semantic segmentation (OSDG-SS) aims to segment known classes and identify unknown categories in target domains that are entirely unseen during training. While recent domain generalization methods perform well under the closed-set assumption, they struggle in open-set settings by misclassifying unknown objects as one of the known classes. To address this challenge, we propose a unified framework that explicitly models unknowns and improves robustness to both semantic and visual domain shifts. First, to provide supervision for unknown regions, we generate realistic unknown objects using Stable Diffusion and insert them into source images, allowing the model to learn unknown-aware representations via segmentation head expansion. However, since synthetic unknowns may not reflect the true distribution of unknowns in target domains, we introduce a meta-learning strategy that partitions the unknown set into meta-train and meta-test subsets, guiding the model to generalize across unseen unknown categories through entropy-based rejection and subdomain shifts. Finally, to reduce confusion between unknowns and visually similar known classes, we optimize the decision boundaries in feature space by enforcing compactness for known classes and expanding the unknown using Mixup-based hard negative synthesis. Extensive experiments across multiple benchmarks demonstrate that our framework significantly improves in the OSDG-SS setting.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向语义分割的开放集域泛化。

### 2. 核心内容
开放集域泛化语义分割要求在训练中完全未见的域里既分割已知类又识别未知类，而现有域泛化方法在开放集下常把未知物体误判为已知类。论文提出统一框架显式建模未知，先用Stable Diffusion生成逼真的未知物体插入源图像提供监督，再通过分割头扩展学习未知感知表示，并提升对语义与视觉域偏移的鲁棒性。实验表明该方法在开放集设置下能更好识别未知类并保持已知类分割性能。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=gNgyV2dPAK](https://openreview.net/forum?id=gNgyV2dPAK)
