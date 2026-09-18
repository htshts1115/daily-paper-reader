---
title: Post-Training Quantization for Video Matting
title_zh: 面向视频抠图的训练后量化
authors: "Tianrui Zhu, Houyuan Chen, Ruihao Gong, Michele Magno, Haotong Qin, Kai Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=XAXT7A8EWh"
tags: ["query:matting"]
score: 8.0
evidence: 面向视频抠图高效部署的训练后量化
tldr: 视频抠图在影视和VR中很关键，但其模型计算量大，难以部署到资源受限设备，而训练后量化在该领域仍处起步阶段，精度与时序一致性难以保持。论文提出首个面向视频抠图的通用PTQ框架，采用两阶段策略，结合块重建优化实现快速稳定的量化，并针对时序一致性加以约束。实验显示该框架在压缩加速模型的同时维持精度与时间一致性，为视频抠图模型的端侧部署提供了系统性方案。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 视频抠图模型计算量大，难以部署到资源受限设备，而训练后量化在该领域仍处起步阶段，精度与时间一致性难以保持。
method: 提出首个面向视频抠图的通用PTQ框架，采用两阶段策略，结合块重建优化实现快速稳定的量化，并兼顾时序一致性。
result: 实验表明该框架在压缩加速视频抠图模型的同时保持精度与时序一致性，优于朴素量化方案。
conclusion: 为视频抠图模型的端侧高效部署提供了首个系统性的训练后量化方案。
---

## Abstract
Video matting is crucial for applications such as film production and virtual reality, yet deploying its computationally intensive models on resource-constrained devices presents challenges. Quantization is a key technique for model compression and acceleration. As an efficient approach, Post-Training Quantization (PTQ) is still in its nascent stages for video matting, facing significant hurdles in maintaining accuracy and temporal coherence. To address these challenges, this paper proposes a novel and general PTQ framework specifically designed for video matting models, marking, to the best of our knowledge, the first systematic attempt in this domain. Our contributions include: (1) A two-stage PTQ strategy that combines block reconstruction-based optimization for fast, stable initial quantization and local dependency capture, followed by a global calibration of quantization parameters to minimize accuracy loss. (2) A Statistically-Driven Global Affine Calibration (GAC) method that enables the network to compensate for cumulative statistical distortions arising from factors such as neglected BN layer effects, even reducing the error of existing PTQ methods on video matting tasks up to 20%. (3) An Optical Flow Assistance (OFA) component that leverages temporal and semantic priors from frames to guide the PTQ process, enhancing the model’s ability to distinguish moving foregrounds in complex scenes and ultimately achieving near full-precision performance even under ultra-low-bit quantization. Comprehensive quantitative and visual results show that our PTQ4VM achieves the state-of-the-art accuracy performance across different bit-widths compared to the existing quantization methods. We highlight that the 4-bit PTQ4VM even achieves performance close to the full-precision counterpart while enjoying 8× FLOP savings.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向视频抠图高效部署的训练后量化。

### 2. 核心内容
视频抠图在影视和VR中很关键，但其模型计算量大，难以部署到资源受限设备，而训练后量化在该领域仍处起步阶段，精度与时序一致性难以保持。论文提出首个面向视频抠图的通用PTQ框架，采用两阶段策略，结合块重建优化实现快速稳定的量化，并针对时序一致性加以约束。实验显示该框架在压缩加速模型的同时维持精度与时间一致性，为视频抠图模型的端侧部署提供了系统性方案。

### 3. 对应检索需求
Real time video matting for human subjects。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=XAXT7A8EWh](https://openreview.net/forum?id=XAXT7A8EWh)
