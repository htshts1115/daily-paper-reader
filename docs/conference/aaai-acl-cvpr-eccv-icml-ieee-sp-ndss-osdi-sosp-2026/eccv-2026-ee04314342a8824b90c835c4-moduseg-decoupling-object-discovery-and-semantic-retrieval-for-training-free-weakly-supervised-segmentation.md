---
title: "ModuSeg: Decoupling Object Discovery and Semantic Retrieval for Training-Free Weakly Supervised Segmentation"
title_zh: ModuSeg：解耦目标发现与语义检索的免训练弱监督分割
authors: "Qingze He, Fagui Liu, Dengke Zhang, Qingmao Wei, Quan Tang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/4632.pdf"
tags: ["query:seg"]
score: 4.0
evidence: 弱监督语义分割，解耦目标发现与语义检索
tldr: 弱监督语义分割仅使用图像级标签，现有方法常将语义识别与目标定位耦合，导致伪标签噪声大且需多阶段重训。本文提出ModuSeg，一个免训练框架，显式解耦目标发现与语义检索，借助基础模型能力降低伪标签噪声。该方法无需耗时的多阶段训练或不稳定的端到端联合优化，即可获得像素级语义分割预测，为弱监督分割提供了简洁有效的新思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ee04314342a8824b90c835c4/fig-001.webp\", \"caption\": \"\", \"page\": 11, \"index\": 1, \"width\": 2024, \"height\": 933}]"
motivation: 现有弱监督语义分割将语义识别与目标定位耦合，易聚焦稀疏判别区域，伪标签噪声大且依赖多阶段重训。
method: 提出免训练的ModuSeg框架，显式解耦目标发现与语义检索两个环节，借助基础模型抑制伪标签噪声。
result: 在弱监督语义分割基准上，该方法无需多阶段训练即可获得像素级预测并降低伪标签噪声。
conclusion: 解耦式免训练设计为弱监督语义分割提供了更稳定高效的范式。
---

## Abstract
Weakly supervised semantic segmentation aims to achievepixel-level predictions using image-level labels. Existing methods typi-cally entangle semantic recognition and object localization, which oftenleads models to focus exclusively on sparse discriminative regions. Al-though foundation models show immense potential, many approachesstill follow the tightly coupled optimization paradigm, struggling to ef-fectively alleviate pseudo-label noise and often relying on time-consumingmulti-stage retraining or unstable end-to-end joint optimization. To ad-dress the above challenges, we present ModuSeg, a training-free weaklysupervised semantic segmentation framework centered on explicitly de-coupling object discovery and semantic assignment. Specifically, we in-tegrate a general mask proposer to extract geometric proposals withreliable boundaries, while leveraging semantic foundation models to con-struct an offline feature bank, transforming segmentation into a non-parametric feature retrieval process. Furthermore, we propose seman-tic boundary purification and soft-masked feature aggregation strate-gies to effectively mitigate boundary ambiguity and quantization errors,thereby extracting high-quality category prototypes. Extensive experi-ments demonstrate that the proposed decoupled architecture better pre-serves fine boundaries without parameter fine-tuning and achieves highlycompetitive performance on standard benchmark datasets. Code is avail-able at https://github.com/Autumnair007/ModuSeg.

---

## 论文详细总结（自动生成）

# ModuSeg 论文总结

## 1. 核心问题与整体含义
- **研究背景**：弱监督语义分割（WSSS）仅使用图像级标签实现像素级预测，以降低密集标注成本。
- **核心问题**：现有主流方法通常将“语义识别”和“目标定位”耦合在单一分类目标中，导致类激活图（CAM）只覆盖稀疏、最具判别性的局部区域，伪标签噪声大。
- **现有范式局限**：为修补不完整区域，传统方法常依赖多阶段重训练、迭代细化或端到端联合优化，训练复杂、耗时且不稳定；即使引入基础模型，许多方法仍沿用耦合优化或微调/蒸馏，未充分利用基础模型的几何与语义先验。
- **论文含义**：ModuSeg 提出一种**免训练** WSSS 框架，显式解耦“目标发现”和“语义检索/分配”，将分割转化为“几何
