---
title: Evaluating Robustness of Monocular Depth Estimation with Procedural Scene Perturbations
title_zh: 用程序化场景扰动评估单目深度估计的鲁棒性
authors: "John Nugent, Siyang Wu, Zeyu Ma, Beining Han, Meenal Parakh, Abhishek Joshi, Lingjie Mei, Alexander Raistrick, Xinyuan Li, Jia Deng"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=SLDYuNGwvU"
tags: ["query:mono-depth"]
score: 7.0
evidence: 评估单目深度估计鲁棒性的基准
tldr: 现有单目深度估计评测多关注标准基准上的精度，而忽略鲁棒性。本文提出PDE程序化深度评测基准，通过程序生成三维场景并施加物体、相机、材质与光照等受控扰动来系统测试深度模型。分析揭示了当前最先进深度模型在哪些扰动下最易失效，为更全面地评估深度估计提供了新工具。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有深度评测只衡量精度而忽略鲁棒性，评估不完整。
method: 提出PDE基准，用程序化生成三维场景并施加物体、相机、材质、光照扰动。
result: 揭示最先进深度模型在多种受控扰动下的失效模式。
conclusion: 为单目深度估计提供了系统的鲁棒性评测框架。
---

## Abstract
Recent years have witnessed substantial progress on monocular depth estimation, particularly as measured by the success of large models on standard benchmarks. However, performance on standard benchmarks does not offer a complete assessment, because most evaluate accuracy but not robustness. 
In this work, we introduce PDE (Procedural Depth Evaluation), a new benchmark which enables systematic evaluation of robustness to changes in 3D scene content.
PDE uses procedural generation to create 3D scenes that test robustness to various controlled perturbations, including object, camera, material and lighting changes. 
Our analysis yields interesting findings on what perturbations are challenging for state-of-the-art depth models, which we hope will inform further research. Code and data are available at https://github.com/princeton-vl/proc-depth-eval.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
评估单目深度估计鲁棒性的基准。

### 2. 核心内容
现有单目深度估计评测多关注标准基准上的精度，而忽略鲁棒性。本文提出PDE程序化深度评测基准，通过程序生成三维场景并施加物体、相机、材质与光照等受控扰动来系统测试深度模型。分析揭示了当前最先进深度模型在哪些扰动下最易失效，为更全面地评估深度估计提供了新工具。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=SLDYuNGwvU](https://openreview.net/forum?id=SLDYuNGwvU)
