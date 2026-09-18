---
title: Dual-Structure Self-Distilled Learning for Enhancing Unsupervised Semantic Segmentation
title_zh: 双结构自蒸馏学习增强无监督语义分割
authors: "Jing Luo, Xiaoliu Luo, Mengzhu Wang, Zuotao Fu, Xu Wang, Taiping Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=sOkMcES3UQ"
tags: ["query:seg"]
score: 6.0
evidence: 无监督语义分割框架
tldr: 无监督语义分割旨在无需人工标注地为像素分配语义标签，但现有方法难以捕捉不同抽象层级的语义结构。本文提出双结构自蒸馏学习框架DSSDL，在单个网络内部完成自蒸馏，将标签空间学到的强表示传递给浅层，并整合亲和结构与聚类结构两种互补形式。其中反向方向挖掘策略用于保持细粒度局部一致性。该工作无需外部教师模型即可增强语义表示，为无监督语义分割提供新思路。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 无监督语义分割难以捕捉不同抽象层级的语义结构。
method: 提出DSSDL，在单网络内自蒸馏，结合亲和结构与聚类结构。
result: 通过反向方向挖掘保持细粒度局部一致性，提升分割表现。
conclusion: 无需外部教师即可增强无监督语义分割的语义表示能力。
---

## Abstract
Unsupervised semantic segmentation (USS) aims to assign semantic labels to pixels without human annotations, yet existing methods struggle to capture semantic structures across different abstraction levels. We propose Dual-Structure Self-Distilled Learning (DSSDL), a novel framework that performs self-distillation within a single network by transferring the stronger semantic representations learned in label space to guide shallower layer, without relying on external teachers. DSSDL integrates two complementary structures:(1) an affinity structure that performs binary pair classification over pairwise similarity scores and leverages a reversed directional mining strategy to preserve fine-grained local consistency.(2) a cluster structure that derives semantic codes from global prototypes and aligns per-pixel predictions via a swapped prediction loss to encourage consistent global grouping. By jointly modeling both structures, DSSDL enforces semantic consistency at both local and global levels, resulting in coherent and robust segmentations. Our method achieves substantial improvements over the strong baseline STEGO, with accuracy and mIoU gains of +16.7 and +3.3 on COCO-Stuff, +14.8 and +3.2 on Cityscapes, and +8.2 and +11.5 on Potsdam-3, respectively.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
无监督语义分割框架。

### 2. 核心内容
无监督语义分割旨在无需人工标注地为像素分配语义标签，但现有方法难以捕捉不同抽象层级的语义结构。本文提出双结构自蒸馏学习框架DSSDL，在单个网络内部完成自蒸馏，将标签空间学到的强表示传递给浅层，并整合亲和结构与聚类结构两种互补形式。其中反向方向挖掘策略用于保持细粒度局部一致性。该工作无需外部教师模型即可增强语义表示，为无监督语义分割提供新思路。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=sOkMcES3UQ](https://openreview.net/forum?id=sOkMcES3UQ)
