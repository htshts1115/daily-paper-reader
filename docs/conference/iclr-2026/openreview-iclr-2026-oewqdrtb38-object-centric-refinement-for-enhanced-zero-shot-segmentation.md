---
title: Object-Centric Refinement for Enhanced Zero-Shot Segmentation
title_zh: 面向增强零样本分割的对象中心精炼
authors: "Srinivasa Rao Nandam, Sara Atito, Zhenhua Feng, Josef Kittler, Muhammad Awais"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=oeWqDrTb38"
tags: ["query:seg"]
score: 6.0
evidence: 基于CLIP的零样本开放词汇语义分割
tldr: 针对零样本语义分割依赖CLIP等视觉语言模型、但其图像块表示缺乏对象中心结构、难以定位未见类别连贯语义区域的问题，本文提出对象中心零样本分割OC-ZSS。方法引入自监督引导的对象提示，利用注意力掩码提取对象级特征以精炼图像块表示。实验表明对象级信息精炼显著提升分割解码器对未见类别的分割效果，为开放词汇分割提供了有效思路。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 零样本语义分割依赖CLIP等视觉语言模型，但其图像块表示缺乏对象中心结构，难以定位连贯语义区域，尤其在未见类别上表现受限。
method: 提出OC-ZSS，引入自监督引导的对象提示，利用注意力掩码提取对象级特征以精炼图像块表示，增强对象中心结构。
result: 对象级信息精炼后的图像块表示显著改善分割解码器对未见类别的定位与分割效果。
conclusion: 说明引入对象中心结构能有效提升零样本语义分割性能。
---

## Abstract
Zero-shot semantic segmentation aims to recognize, pixel-wise, unseen categories without annotated masks, typically by leveraging vision-language models such as CLIP. However, the patch representations obtained by the CLIP's vision encoder lack object-centric structure, making it difficult to localize coherent semantic regions.
This hinders the performance of the segmentation decoder, especially for unseen categories. To mitigate this issue, we propose object-centric zero-shot segmentation (OC-ZSS) that enhances patch representations using object-level information. 
To extract object features for patch refinement, we introduce self-supervision-guided object prompts into the encoder. These prompts attend to coarse object regions using attention masks derived from unsupervised clustering of features from a pretrained self-supervised~(SSL) model. Although these prompts offer a structured initialization of the object-level context, the extracted features remain coarse due to the unsupervised nature of clustering. To further refine the object features and effectively enrich patch representations, we develop a dual-stage Object Refinement Attention (ORA) module that iteratively updates both object and patch features through cross-attention. Last, to make the refinement more robust and sensitive to objects of varying spatial scales, we incorporate a lightweight granular attention mechanism that operates over multiple receptive fields. OC-ZSS achieves state-of-the-art performance on standard zero-shot segmentation benchmarks across inductive, transductive, and cross-domain settings.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于CLIP的零样本开放词汇语义分割。

### 2. 核心内容
针对零样本语义分割依赖CLIP等视觉语言模型、但其图像块表示缺乏对象中心结构、难以定位未见类别连贯语义区域的问题，本文提出对象中心零样本分割OC-ZSS。方法引入自监督引导的对象提示，利用注意力掩码提取对象级特征以精炼图像块表示。实验表明对象级信息精炼显著提升分割解码器对未见类别的分割效果，为开放词汇分割提供了有效思路。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=oeWqDrTb38](https://openreview.net/forum?id=oeWqDrTb38)
