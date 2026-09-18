---
title: "TENet: A Text-Enhanced Network for Few-Shot Semantic Segmentation with Background-Aware Query Refinement"
title_zh: TENet：背景感知查询细化的文本增强小样本语义分割网络
authors: "Jingshan Hong, Haigen Hu, Huihuang Zhang, Qianwei Zhou, Kangkang Ai, Xiaoqin Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=zeBKTZEiCv"
tags: ["query:seg"]
score: 6.0
evidence: 背景感知细化的少样本语义分割
tldr: 小样本语义分割受标注数据稀缺与支持-查询域差异困扰，现有多模态方法多只利用视觉特征与前景文本，忽视背景语义。论文提出文本增强网络TENet，同时使用前景与背景文本生成高质量激活图，并自适应细化查询特征。实验表明背景语义与前景的关联能提升目标区分能力与分割精度。该工作说明背景上下文对语义分割推理具有重要增益。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 小样本语义分割受标注稀缺与域差异困扰，现有多模态方法忽视背景语义的价值。
method: 提出TENet，同时利用前景与背景文本生成高质量激活图，并自适应细化查询特征。
result: 借助背景语义与前景的关联提升目标区分能力，改善小样本分割精度。
conclusion: 表明背景文本信息对小样本语义分割推理具有重要增益。
---

## Abstract
Existing few-shot semantic segmentation (FSS) methods suffer from limited annotation data and domain gaps between support and query images. Although recent multi-modal approaches incorporate textual information to mitigate this gap, they primarily focus on visual features and foreground text, ignoring the value of background semantics.
However, the background context plays a crucial role in reasoning. Its semantic association with the foreground helps the model to better distinguish the target.
Motivated by this, we propose a Text Enhancement Network, called TENet, which is a novel FSS framework that uses both foreground and background text to generate high-quality activation maps for query features. The TENet adaptively generates background text from the foreground semantics by integrating a DeepSeek-based activation generation module. The background text is encoded using a CLIP encoder and fused with visual features to generate activation maps. To further improve alignment precision, we propose a joint optimization strategy by combining dynamic and fixed refinement methods.
Extensive experiments on PASCAL-5$^i$ and COCO-20$^i$ show that the TENet consistently outperforms state-of-the-art methods, validating the effectiveness of incorporating background text information and refined activation mechanisms in FSS.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
背景感知细化的少样本语义分割。

### 2. 核心内容
小样本语义分割受标注数据稀缺与支持-查询域差异困扰，现有多模态方法多只利用视觉特征与前景文本，忽视背景语义。论文提出文本增强网络TENet，同时使用前景与背景文本生成高质量激活图，并自适应细化查询特征。实验表明背景语义与前景的关联能提升目标区分能力与分割精度。该工作说明背景上下文对语义分割推理具有重要增益。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=zeBKTZEiCv](https://openreview.net/forum?id=zeBKTZEiCv)
