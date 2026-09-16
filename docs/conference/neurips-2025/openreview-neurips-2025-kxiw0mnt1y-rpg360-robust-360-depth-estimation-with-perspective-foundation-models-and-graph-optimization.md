---
title: "RPG360: Robust 360 Depth Estimation with Perspective Foundation Models and Graph Optimization"
title_zh: RPG360：结合透视基础模型与图优化的稳健全景深度估计
authors: "Dongki Jung, Jaehoon Choi, Yonghan Lee, Dinesh Manocha"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=kxiw0Mnt1y"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于透视基础模型的免训练全景单目深度
tldr: 全景图像单目深度估计长期受限于大规模标注数据稀缺。本文提出RPG360，将360度图像转换为六面立方体贴图，借助透视基础模型估计深度与表面法向，并用图优化对齐各面之间的尺度不一致。方法无需训练即可获得稳健的全景深度结果，为全景深度估计提供了免标注的实用方案。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 全景深度估计缺乏大规模标注数据，现有方法难以稳健应用。
method: 将360度图像转为六面立方体贴图，用透视基础模型估计深度和法向并做图优化尺度对齐。
result: 无需训练即可稳健估计全景深度，缓解各面深度尺度不一致问题。
conclusion: 为全景单目深度估计提供了免训练且可泛化的实用范式。
---

## Abstract
The increasing use of 360$^\circ$ images across various domains has emphasized the need for robust depth estimation techniques tailored for omnidirectional images. However, obtaining large-scale labeled datasets for 360$^\circ$ depth estimation remains a significant challenge. In this paper, we propose RPG360, a training-free robust 360$^\circ$ monocular depth estimation method that leverages perspective foundation models and graph optimization. Our approach converts 360$^\circ$ images into six- face cubemap representations, where a perspective foundation model is employed to estimate depth and surface normals. To address depth scale inconsistencies across different faces of the cubemap, we introduce a novel depth scale alignment technique using graph-based optimization, which parameterizes the predicted depth and normal maps while incorporating an additional per-face scale parameter. This optimization ensures depth scale consistency across the six-face cubemap while preserving 3D structural integrity. Furthermore, as foundation models exhibit inherent robustness in zero-shot settings, our method achieves superior performance across diverse datasets, including Matterport3D, Stanford2D3D, and 360Loc. We also demonstrate the versatility of our depth estimation approach by validating its benefits in downstream tasks such as feature matching 3.2 ∼ 5.4% and Structure from Motion 0.2 ∼ 9.7% in AUC@5$^\circ$.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于透视基础模型的免训练全景单目深度。

### 2. 核心内容
全景图像单目深度估计长期受限于大规模标注数据稀缺。本文提出RPG360，将360度图像转换为六面立方体贴图，借助透视基础模型估计深度与表面法向，并用图优化对齐各面之间的尺度不一致。方法无需训练即可获得稳健的全景深度结果，为全景深度估计提供了免标注的实用方案。

### 3. 对应检索需求
depth foundation model。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=kxiw0Mnt1y](https://openreview.net/forum?id=kxiw0Mnt1y)
