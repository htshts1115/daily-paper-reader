---
title: "RefChess: Training-Free Contextual Search for Zero-Shot Referring Image Segmentation"
title_zh: RefChess：面向零样本指代图像分割的免训练上下文搜索
authors: "Shiyan Tong, Jinxia Zhang, Zhiyuan Wang, Hao Tian, YingYing Wang, Kanjian Zhang, Haikun Wei"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf/cbd019c058cec1cf79139cd5c3c0080ef8f86fe4.pdf"
tags: ["query:seg"]
score: 4.0
evidence: 零样本指代图像分割提案选择
tldr: 零样本指代图像分割中，现有方法独立打分候选提案，易被部分满足表达的相似候选干扰而选错掩码。本文提出RefChess，一种免训练上下文搜索框架，在采样的干扰上下文中评估候选掩码，并以蒙特卡洛树搜索作为预算内的选择策略。实验表明该方法提升提案选择鲁棒性，但任务聚焦语言指代分割，与通用语义或实例分割需求关联中等。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有零样本指代图像分割方法独立评估候选提案，易受视觉相似候选干扰而选错目标掩码。
method: 提出免训练的RefChess框架，在采样干扰上下文中评估候选掩码并用蒙特卡洛树搜索进行预算化选择。
result: 实验表明该上下文搜索策略提升了指代图像分割中提案选择的鲁棒性与准确度。
conclusion: 该工作为零样本指代图像分割提供了免训练且抗干扰的提案选择新方法。
---

## Abstract
Recent advances in zero-shot referring image segmentation (RIS), driven by foundation models such as SAM and CLIP, have improved cross-modal alignment between visual regions and natural language expressions. Nevertheless, selecting the correct segmentation proposal remains challenging, as existing methods typically score proposals independently and can be distracted by visually similar candidates that partially satisfy the expression. To address this limitation, we propose RefChess, a training-free contextual search framework for robust proposal selection. Instead of treating proposal selection as a single-step ranking problem, RefChess evaluates candidate masks under sampled distractor contexts and uses Monte-Carlo Tree Search as a budgeted mechanism to explore the combinatorial space of contextual perturbations. The search is guided by a stability-aware reward that integrates language decomposition, vision--language similarity, object-centric cues, and spatial guidance signals. Experiments on standard RIS benchmarks show that RefChess consistently improves robustness and referring segmentation performance without task-specific training. Code is available at \url{https://github.com/Tongshiyan/RefChess}.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
零样本指代图像分割提案选择。

### 2. 核心内容
零样本指代图像分割中，现有方法独立打分候选提案，易被部分满足表达的相似候选干扰而选错掩码。本文提出RefChess，一种免训练上下文搜索框架，在采样的干扰上下文中评估候选掩码，并以蒙特卡洛树搜索作为预算内的选择策略。实验表明该方法提升提案选择鲁棒性，但任务聚焦语言指代分割，与通用语义或实例分割需求关联中等。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICML-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=RESRoG7nvd](https://openreview.net/forum?id=RESRoG7nvd)
