---
title: "DualFocus: Depth from Focus with Spatio-Focal Dual Variational Constraints"
title_zh: DualFocus：基于空间-焦距双变分约束的深度对焦估计
authors: "Sungmin Woo, Sangyoun Lee"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=OZUl49U6p6"
tags: ["query:mono-depth"]
score: 5.0
evidence: 基于对焦堆栈变分约束的深度估计
tldr: 基于对焦的深度估计通过分析不同焦距图像的聚焦线索来获取深度，但现有学习方法在细纹理或深度突变场景中易受歧义聚焦线索误导。本文提出DualFocus框架，利用焦栈中随焦距变化的梯度模式，在空间与焦距两个维度联合建模，并引入双重变分约束以区分真实深度边缘与纹理伪影。该方法在复杂场景下提升了深度估计精度，为对焦线索的可靠利用提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有基于对焦的深度估计在细纹理或深度突变场景中，聚焦线索模糊易导致估计错误。
method: 提出DualFocus框架，利用焦栈梯度模式在空间与焦距维度联合建模，并引入双重变分约束。
result: 该方法能区分真实深度边缘与纹理伪影，在复杂场景中提升了深度估计的精度与鲁棒性。
conclusion: 空间与焦距双约束的对焦深度估计为复杂场景下的可靠深度获取提供了新方案。
---

## Abstract
Depth-from-Focus (DFF) enables precise depth estimation by analyzing focus cues across a stack of images captured at varying focal lengths. While recent learning-based approaches have advanced this field, they often struggle in complex scenes with fine textures or abrupt depth changes, where focus cues may become ambiguous or misleading. We present DualFocus, a novel DFF framework that leverages the focal stack’s unique gradient patterns induced by focus variation, jointly modeling focus changes over spatial and focal dimensions. Our approach introduces a variational formulation with dual constraints tailored to DFF: spatial constraints exploit gradient pattern changes across focus levels to distinguish true depth edges from texture artifacts, while focal constraints enforce unimodal, monotonic focus probabilities aligned with physical focus behavior. These inductive biases improve robustness and accuracy in challenging regions. Comprehensive experiments on four public datasets demonstrate that DualFocus consistently outperforms state-of-the-art methods in both depth accuracy and perceptual quality.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于对焦堆栈变分约束的深度估计。

### 2. 核心内容
基于对焦的深度估计通过分析不同焦距图像的聚焦线索来获取深度，但现有学习方法在细纹理或深度突变场景中易受歧义聚焦线索误导。本文提出DualFocus框架，利用焦栈中随焦距变化的梯度模式，在空间与焦距两个维度联合建模，并引入双重变分约束以区分真实深度边缘与纹理伪影。该方法在复杂场景下提升了深度估计精度，为对焦线索的可靠利用提供了新思路。

### 3. 对应检索需求
metric depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=OZUl49U6p6](https://openreview.net/forum?id=OZUl49U6p6)
