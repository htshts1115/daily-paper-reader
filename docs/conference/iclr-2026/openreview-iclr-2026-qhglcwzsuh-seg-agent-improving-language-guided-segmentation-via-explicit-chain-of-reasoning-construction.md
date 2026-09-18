---
title: "Seg-Agent: Improving Language-Guided Segmentation via Explicit Chain-of-Reasoning Construction"
title_zh: Seg-Agent：通过显式思维链构建改进语言引导分割
authors: "Chao Hao, Jun Xu, Ji Du, shuo Ye, Yong Xu, Ziyue Qiao, Xiaodong Cun, Guangcong Wang, Xubin Zheng, Zitong YU"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=qhglCWZsuh"
tags: ["query:seg"]
score: 6.0
evidence: 语言引导分割，免训练
tldr: 语言引导分割突破了传统语义分割的范围限制，可根据用户指令分割任意目标，但现有两阶段方法依赖大规模训练来弥补基础模型空间定位能力不足。本文提出Seg-Agent，通过显式构建思维链来增强多模态大模型的空间推理，无需训练即可引导SAM等模型生成高质量掩码。该方法在语言引导分割任务上提升了精度，为免训练的通用分割提供了新思路。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有语言引导分割两阶段框架空间定位弱，需大规模训练才能提升精度。
method: 提出Seg-Agent，通过显式思维链构建增强空间推理，免训练引导分割模型。
result: 无需训练即可根据指令分割任意目标，提升语言引导分割精度。
conclusion: 为免训练的语言引导通用分割提供了新范式。
---

## Abstract
Language-guided segmentation breaks through the scope limitations of traditional semantic segmentation, enabling models to segment any target region in an image based on user instructions. Existing methods are typically two-stage frameworks: they first employ multimodal large language models (MLLMs) to understand the textual instruction and generate visual prompts from the image, and then use foundational segmentation models such as SAM to produce high-quality masks. However, due to the limited spatial grounding capability of the base models, they usually require training on large-scale datasets to achieve improved segmentation accuracy. In this paper, we propose Seg-Agent, a completely training-free language-guided segmentation method. By constructing an explicit reasoning chain: generation, selection, and refinement, Seg-Agent achieves performance comparable to training-based approaches. Additionally, to evaluate the generalization ability of Seg-Agent, we collect a diverse dataset covering various language-guided segmentation scenarios, named Various-LangSeg. Extensive experiments demonstrate the effectiveness of our proposed method. The code and dataset will be made publicly available.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
语言引导分割，免训练。

### 2. 核心内容
语言引导分割突破了传统语义分割的范围限制，可根据用户指令分割任意目标，但现有两阶段方法依赖大规模训练来弥补基础模型空间定位能力不足。本文提出Seg-Agent，通过显式构建思维链来增强多模态大模型的空间推理，无需训练即可引导SAM等模型生成高质量掩码。该方法在语言引导分割任务上提升了精度，为免训练的通用分割提供了新思路。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Public
- OpenReview：[https://openreview.net/forum?id=qhglCWZsuh](https://openreview.net/forum?id=qhglCWZsuh)
