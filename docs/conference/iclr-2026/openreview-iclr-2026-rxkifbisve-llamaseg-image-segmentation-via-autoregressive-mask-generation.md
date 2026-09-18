---
title: "LlamaSeg: Image Segmentation via Autoregressive Mask Generation"
title_zh: LlamaSeg：通过自回归掩码生成的图像分割
authors: "Jiru Deng, Tengjin Weng, Tianyu Yang, Wenhan Luo, Zhiheng Li, Wenhao Jiang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=RXkiFbiSvE"
tags: ["query:seg"]
score: 8.0
evidence: 以开放词汇文本提示统一多种分割任务
tldr: 针对多种图像分割任务难以统一的问题，LlamaSeg将分割重构为视觉生成任务，把掩码编码为视觉token，用LLaMA式Transformer直接进行下一token预测，使分割自然融入自回归架构。作者还构建了含200万掩码、5800多个开放词汇标签的SA-OVRS数据集支撑大规模训练。模型能够依据文本提示定位目标并生成细粒度掩码，统一了多类分割任务。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有分割方法各自独立，难以用统一框架处理开放词汇等多样任务。
method: 把掩码编码为视觉token，用LLaMA式Transformer自回归预测，并构建大规模开放词汇分割数据集。
result: 模型可根据文本提示定位目标并生成细粒度掩码，统一多种分割任务。
conclusion: 为语言指令驱动的通用分割提供了自回归生成式新范式。
---

## Abstract
We present LlamaSeg, a visual autoregressive framework that unifies multiple image segmentation tasks via natural language instructions. By reformulating segmentation as visual generation, LlamaSeg encodes masks as visual tokens and uses a LLaMA-style Transformer for direct next-token prediction, naturally fitting segmentation into autoregressive architectures. To support large-scale training, we introduce a data annotation pipeline and construct the SA-OVRS dataset, which contains 2M segmentation masks annotated with over 5,800 open-vocabulary labels or diverse textual descriptions, spanning diverse real-world scenarios. This enables our model to localize objects in images based on text prompts and to generate fine-grained masks. We further introduce the composite metric average Hausdorff Distance ($d_{\mathrm{AHD}}$) to evaluate mask contour fidelity for generative models better. Experiments show that LlamaSeg consistently outperforms existing generative approaches on multiple segmentation benchmarks and delivers finer, more accurate segmentation masks.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
以开放词汇文本提示统一多种分割任务。

### 2. 核心内容
针对多种图像分割任务难以统一的问题，LlamaSeg将分割重构为视觉生成任务，把掩码编码为视觉token，用LLaMA式Transformer直接进行下一token预测，使分割自然融入自回归架构。作者还构建了含200万掩码、5800多个开放词汇标签的SA-OVRS数据集支撑大规模训练。模型能够依据文本提示定位目标并生成细粒度掩码，统一了多类分割任务。

### 3. 对应检索需求
open-vocabulary segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Rejected-Public
- OpenReview：[https://openreview.net/forum?id=RXkiFbiSvE](https://openreview.net/forum?id=RXkiFbiSvE)
