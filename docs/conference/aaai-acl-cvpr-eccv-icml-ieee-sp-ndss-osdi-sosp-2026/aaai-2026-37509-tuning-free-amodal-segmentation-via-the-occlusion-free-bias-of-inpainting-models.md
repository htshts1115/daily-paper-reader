---
title: Tuning-Free Amodal Segmentation via the Occlusion-Free Bias of Inpainting Models
title_zh: 利用修复模型遮挡无偏性的免调优非模态分割
authors: "Jae Joong Lee, Bedrich Benes, Raymond A. Yeh"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37509/41471"
tags: ["query:seg"]
score: 6.0
evidence: 处理遮挡目标部分的非模态分割
tldr: 针对现有非模态分割依赖标注掩码或合成数据、泛化能力受限的问题，本文提出免调优方法，利用扩散修复基础模型固有的遮挡无偏性来推断目标被遮挡部分的掩码。实验表明该方法无需非模态标注即可在多个数据集上获得更稳健的遮挡区域分割效果，为通用遮挡感知分割提供了新的零样本思路。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 871, \"height\": 459}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1791, \"height\": 859}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1822, \"height\": 242}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 849, \"height\": 496}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 845, \"height\": 505}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1812, \"height\": 746}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 874, \"height\": 565}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37509/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 877, \"height\": 440}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37509/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 882, \"height\": 379}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37509/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 878, \"height\": 229}]"
motivation: 现有非模态分割依赖带标注掩码或合成数据，数据集多样性不足限制泛化能力。
method: 提出免调优方法，利用扩散修复基础模型的遮挡无偏性预测目标可见与遮挡部分的掩码。
result: 在无需非模态标注的情况下实现跨数据集更稳健的遮挡区域分割。
conclusion: 表明复用修复模型的遮挡先验可提升非模态分割泛化性。
---

## Abstract
Amodal segmentation is an image-based algorithm that aims to predict masks for both visible and occluded parts of objects. Existing methods typically rely on supervised learning with annotated amodal masks or synthetic data. The effectiveness of these methods relies heavily on the quality of the datasets. This dependence can unintentionally restrict their generalization capabilities due to insufficient diversity and size. Although existing zero-shot methods perform well on their reported datasets, their performance does not necessarily transfer to other datasets. We propose a tuning-free approach that re-purposes diffusion-based inpainting foundation models for amodal segmentation. Our approach is motivated by the “occlusion-free bias” of inpainting models, i.e., the inpainted objects tend to be complete and without occlusions. We reconstruct the occluded regions of an object via inpainting and then apply segmentation, all without additional training or fine-tuning. Experiments on five datasets, three previously unreported, demonstrate the generalizability of our approach. On average, our approach achieves 5.3% more accurate masks in mIoU compared to the publicly available state-of-the-art, pix2gestalt.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究问题**：非模态分割（amodal segmentation）要求同时预测目标可见部分与被遮挡部分的完整掩码。现有方法多依赖带非模态标注的数据集或合成数据，性能高度受限于数据质量、规模与多样性。
- **研究动机**：人工标注被遮挡区域困难且不一致，合成数据又存在与真实数据的分布差距，因此已有监督方法及部分零样本方法的泛化能力有限。
- **整体含义**：本文提出一种**免调优、零样本**的非模态分割框架，复用预训练扩散修复基础模型，不训练、不微调、不需要非模态标注，也不限制预定义类别。核心观察是扩散修复模型存在“**遮挡无偏性**”（occlusion-free bias）：给定合理修复区域，模型倾向于生成完整目标而非遮挡物。

## 2. 方法论

- **核心思想**：对可见掩码进行扩展修复，让扩散修复模型补全被遮挡区域；随后在修复后的无遮挡目标上使用分割模型（如 SAM）提取非模态掩码。
- **整体流程**：
  - 输入 RGB 图像 \(I\) 与可见掩码 \(V\)。
  - 构造条件图像 \(x\)：对象区域来自加噪后的可见对象，背景区域来自颜色分布匹配的合成背景。
  - 构造软修复区域 \(M\)：由可见掩码轮廓的并集凸包生成。
  - 使用扩散修复模型进行“软修复”，得到修复图像 \(\hat{x}_0\)。
  - 用 SAM 从 \(V\) 中均匀采样 9 个点，提取最终非模态掩码 \(\hat{A}\)。
- **关键组件**：
  - **泄漏条件（leakage conditioning）**：不严格保持非掩码区域不变，而是将原图信息“泄漏”到扩散采样中：
    \[
    \hat{x}_t = s\cdot(M\odot\tilde
