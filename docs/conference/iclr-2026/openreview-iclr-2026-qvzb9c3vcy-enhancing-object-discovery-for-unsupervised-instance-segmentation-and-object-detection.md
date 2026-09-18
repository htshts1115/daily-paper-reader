---
title: Enhancing Object Discovery for Unsupervised Instance Segmentation and Object Detection
title_zh: 增强无监督实例分割与目标检测的对象发现
authors: "Xingyu Feng, Hebei Gao, Hong Li"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=QVzb9c3VCy"
tags: ["query:seg"]
score: 6.0
evidence: 无监督实例分割与目标检测
tldr: 无监督实例分割与目标检测长期受制于不可靠的伪标签和繁琐的掩码后处理，难以在无专门损失的情况下稳定发现对象。论文提出COLER框架，先用CutOnce仅执行一次归一化割即可在一张图中生成多个对象掩码，再让检测器从这些粗掩码中学习，并设计简洁模块充分利用自监督模型的对象发现能力。训练无需专门伪标签损失，实验显示其在无监督实例分割与检测上具有竞争力。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 无监督实例分割与目标检测缺乏可靠的伪标签与后处理，难以在不依赖复杂损失的情况下发现对象。
method: 提出COLER，用CutOnce仅执行一次归一化割生成多对象伪标签，并设计简洁模块让自监督模型充分发挥对象发现能力，摆脱掩码后处理。
result: 训练无需专门伪标签损失，COLER在无监督实例分割和目标检测上取得有竞争力的性能。
conclusion: 表明单次归一化割与简洁设计即可有效实现无监督对象发现与分割。
---

## Abstract
We propose Cut-Once-and-LEaRn (COLER), a simple approach for unsupervised instance segmentation and object detection. COLER first uses our developed CutOnce to generate coarse pseudo labels, then enables the detector to learn
from these masks. CutOnce applies Normalized Cut only
once and does not rely on any clustering methods, but it
can generate multiple object masks in an image. We have
designed several novel yet simple modules that not only allow CutOnce to fully leverage the object discovery capabilities of self-supervised models, but also free it from reliance
on mask post-processing. During training, COLER achieves
strong performance without requiring specially designed loss
functions for pseudo labels, and its performance is further improved through self-training. COLER is a zero-shot unsupervised model that outperforms previous state-of-the-art methods on multiple benchmarks. We believe our method can help
advance the field of unsupervised object localization.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
无监督实例分割与目标检测。

### 2. 核心内容
无监督实例分割与目标检测长期受制于不可靠的伪标签和繁琐的掩码后处理，难以在无专门损失的情况下稳定发现对象。论文提出COLER框架，先用CutOnce仅执行一次归一化割即可在一张图中生成多个对象掩码，再让检测器从这些粗掩码中学习，并设计简洁模块充分利用自监督模型的对象发现能力。训练无需专门伪标签损失，实验显示其在无监督实例分割与检测上具有竞争力。

### 3. 对应检索需求
instance segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=QVzb9c3VCy](https://openreview.net/forum?id=QVzb9c3VCy)
