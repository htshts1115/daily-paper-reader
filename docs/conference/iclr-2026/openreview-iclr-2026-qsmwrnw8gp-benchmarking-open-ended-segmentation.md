---
title: Benchmarking Open-ended Segmentation
title_zh: 开放式分割的基准评测
authors: "Cristina González, Santiago Rodriguez, Kevis-kokitsi Maninis, Jordi Pont-Tuset, Pablo Arbelaez"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=QSmwRnw8GP"
tags: ["query:seg"]
score: 5.0
evidence: 开放式分割的评测基准研究
tldr: 开放式分割要求模型能为未见概念和区域生成自由形式的描述，但现有评测协议难以反映生成描述的真实语义准确性。作者实证发现基于嵌入相似度的映射与人类判断存在明显偏差，于是提出一种考虑多种词汇关系的映射函数，使评分更贴近人类标注。该方法被整合进稳健的评测框架，并对先前最先进方法重新进行基准测试。该工作为开放式分割提供了更可靠的评测标准。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有开放式分割评测协议难以反映生成描述的真实语义准确性。
method: 引入考虑多重词汇关系的映射函数，构建更鲁棒评测框架并重新评测。
result: 实验表明新映射更贴近人类标注，并首次提出多任务基准。
conclusion: 为开放式分割提供更可靠的评测标准与方法论。
---

## Abstract
Open-ended segmentation requires models capable of generating free-form descriptions of previously unseen concepts and regions. Despite advancements in model development, current evaluation protocols for open-ended segmentation tasks fail to capture the true semantic accuracy of the generated descriptions. We empirically demonstrate that embedding‐based similarity score mappings diverge significantly from human judgments. To address this issue, we introduce a novel mapping function that considers multiple lexical relationships between free‐form outputs and test‐vocabulary labels, yielding much closer alignment with human annotations. We integrate this mapping into a robust evaluation framework and re‐benchmark previous state‐of‐the‐art methods. Additionally, we present the first Multi-modal Large‐Language Model trained with a contrastive objective to jointly align visual regions and textual descriptions, achieving new state‐of‐the‐art results in open‐ended panoptic segmentation.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
开放式分割的评测基准研究。

### 2. 核心内容
开放式分割要求模型能为未见概念和区域生成自由形式的描述，但现有评测协议难以反映生成描述的真实语义准确性。作者实证发现基于嵌入相似度的映射与人类判断存在明显偏差，于是提出一种考虑多种词汇关系的映射函数，使评分更贴近人类标注。该方法被整合进稳健的评测框架，并对先前最先进方法重新进行基准测试。该工作为开放式分割提供了更可靠的评测标准。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=QSmwRnw8GP](https://openreview.net/forum?id=QSmwRnw8GP)
