---
title: "MoGe-2: Accurate Monocular Geometry with Metric Scale and Sharp Details"
title_zh: MoGe-2：具备度量尺度与清晰细节的精确单目几何
authors: "Ruicheng Wang, Sicheng Xu, Yue Dong, Yu Deng, Jianfeng Xiang, Zelong Lv, Guangzhong Sun, Xin Tong, Jiaolong Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=16mDq7m2OK"
tags: ["query:mono-depth"]
score: 9.0
evidence: 单张图像恢复度量尺度几何
tldr: 现有单目几何估计多预测仿射不变的相对点图，尺度未知且细节模糊，难以用于度量级应用。MoGe-2在MoGe基础上探索将仿射不变点表示扩展为度量尺度预测的策略，在保持相对几何精度的同时恢复真实尺度。作者还提出数据精炼方法，用清晰合成标签过滤并补全真实数据，显著提升几何细节粒度，实现了单张图像的高精度度量尺度三维重建。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 现有单目几何估计仅给出尺度未知的仿射不变点图，且真实数据噪声导致细节缺失。
method: 在MoGe基础上扩展度量尺度预测，并用清晰合成标签精炼补全真实数据以恢复细节。
result: 方法在保持相对几何精度的同时输出度量尺度点图，几何细节显著增强。
conclusion: 该工作推进了开放域单目度量几何估计的实用化。
---

## Abstract
We propose MoGe-2, an advanced open-domain geometry estimation model that recovers a metric-scale 3D point map of a scene from a single image. Our method builds upon the recent monocular geometry estimation approach, MoGe, which predicts affine-invariant point maps with unknown scales. We explore effective strategies to extend MoGe for metric geometry prediction without compromising the relative geometry accuracy provided by the affine-invariant point representation. Additionally, we discover that noise and errors in real data diminish fine-grained detail in the predicted geometry. We address this by developing a data refinement approach that filters and completes real data using sharp synthetic labels, significantly enhancing the granularity of the reconstructed geometry while maintaining the overall accuracy. We train our model on a large corpus of mixed datasets and conducted comprehensive evaluations, demonstrating its superior performance in achieving accurate relative geometry, precise metric scale, and fine-grained detail recovery -- capabilities that no previous methods have simultaneously achieved.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
单张图像恢复度量尺度几何。

### 2. 核心内容
现有单目几何估计多预测仿射不变的相对点图，尺度未知且细节模糊，难以用于度量级应用。MoGe-2在MoGe基础上探索将仿射不变点表示扩展为度量尺度预测的策略，在保持相对几何精度的同时恢复真实尺度。作者还提出数据精炼方法，用清晰合成标签过滤并补全真实数据，显著提升几何细节粒度，实现了单张图像的高精度度量尺度三维重建。

### 3. 对应检索需求
metric depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=16mDq7m2OK](https://openreview.net/forum?id=16mDq7m2OK)
