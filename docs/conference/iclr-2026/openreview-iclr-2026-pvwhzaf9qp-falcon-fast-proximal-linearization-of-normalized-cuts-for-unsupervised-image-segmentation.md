---
title: "Falcon: Fast Proximal Linearization of Normalized Cuts for Unsupervised Image Segmentation"
title_zh: Falcon：用于无监督图像分割的归一化割快速近端线性化
authors: "Xiao Zhang, Xiangyu Han, Xiwen Lai, Yao Sun, Pei Zhang, Xia Liu, Konrad Kording"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=PvWHzAf9qp"
tags: ["query:seg"]
score: 4.0
evidence: 基于归一化割的无监督图像分割
tldr: 针对基于归一化割的零样本无监督分割依赖递归二分与重复特征分解、计算昂贵且缺乏K路分割收敛保证的问题，本文提出Falcon近端梯度求解器，直接优化离散K路归一化割目标而无需谱松弛，并证明其线性收敛。实验表明该方法能快速稳定地产生K路分割，减少近似误差，为可扩展无监督图像分割提供了有理论保证的高效优化方案。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 基于归一化割的零样本无监督分割依赖递归二分与重复特征分解，计算昂贵且缺乏K路分割的收敛保证。
method: 提出Falcon近端梯度求解器，直接优化离散K路归一化割目标而无需谱松弛，并证明线性收敛。
result: 在多个分割基准上实现快速稳定的K路分割，避免谱松弛近似误差并具备收敛性保证。
conclusion: 为可扩展的无监督图像分割提供了更高效且有理论保证的优化方案。
---

## Abstract
Current zero-shot unsupervised segmentation methods based on normalized cuts (NCut) face three key limitations. First, they rely on recursive bipartitions with repeated eigen-decompositions, making them prohibitively expensive at scale. Second, each split requires spectral relaxation followed by rounding, introducing layers of approximation where the final partition may diverge from the true NCut objective. Third, recursive bipartitioning offers no principled assurance of producing a stable $K$-way segmentation, and existing heuristics lack convergence guarantees. We propose \textbf{Falcon}, a proximal-gradient solver that directly optimizes the discrete $K$-way NCut objective without spectral relaxation. We prove linear convergence under the \textit{Kurdyka--\L{}ojasiewicz} (KL) property. Falcon computes closed-form gradient scores weighted by cluster volumes and performs row-wise one-hot proximal updates stabilized by inertia. A monotone backtracking scheme adaptively tunes the proximal parameter, ensuring non-decreasing NCut values. This design preserves discrete feasibility, removes repeated eigen-decomposition, and guarantees convergence. Across six benchmarks, Falcon outperforms the strongest official baseline (DiffCut) by wide margins, e.g., +13.2 mIoU on VOC, +27.7 on COCO-Object, and +3.1 on Cityscapes, while remaining competitive on Pascal Context. It also runs up to an order of magnitude faster than recursive NCut and scales more favorably in memory at high resolution, making it practical for larger token grids. By pairing pretrained foundation models with a principled NCut solver, Falcon sets a new state of the art across six benchmarks and achieves the best performance on 17 of 18 benchmark--encoder pairs, underscoring both its robustness and its generality in bridging the gap between unsupervised and supervised segmentation.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于归一化割的无监督图像分割。

### 2. 核心内容
针对基于归一化割的零样本无监督分割依赖递归二分与重复特征分解、计算昂贵且缺乏K路分割收敛保证的问题，本文提出Falcon近端梯度求解器，直接优化离散K路归一化割目标而无需谱松弛，并证明其线性收敛。实验表明该方法能快速稳定地产生K路分割，减少近似误差，为可扩展无监督图像分割提供了有理论保证的高效优化方案。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=PvWHzAf9qp](https://openreview.net/forum?id=PvWHzAf9qp)
