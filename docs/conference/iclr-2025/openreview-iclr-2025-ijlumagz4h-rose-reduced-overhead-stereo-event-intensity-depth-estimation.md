---
title: "ROSE: Reduced Overhead Stereo Event-Intensity Depth Estimation"
title_zh: ROSE：降低开销的立体事件强度深度估计
authors: "Sankarshana Venugopal, Seokjun Moon, Mohammad Mostafavi, Jonghyun Choi"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=IjLumaGZ4h"
tags: ["query:stereo-depth"]
score: 6.0
evidence: 轻量实时双目深度估计
tldr: 针对事件相机立体深度估计计算开销大、难以实时的问题，该文提出ROSE框架，结合轻量级事件表示网络与优化立体匹配来降低模型规模和计算量。方法在事件和强度图像上实现实时深度估计，同时保持精度。其高效双目匹配思路可迁移到手机双摄小基线深度估计。
source: ICLR-2025-Public
selection_source: conference_retrieval
motivation: 解决事件相机立体深度估计计算开销大、实时性差的问题。
method: 采用轻量事件表示网络并优化立体匹配流程以降低计算量。
result: 在事件与强度图像上实现实时深度估计且保持精度。
conclusion: 为高效双目深度估计提供方案，可启发手机双摄小基线场景。
---

## Abstract
Stereo depth estimation using event cameras is a promising approach for real-time vision tasks, offering low-latency, high-speed data capture. However, existing methods often suffer from high computational overhead, limiting their real-time applicability. To address these challenges, we introduce ROSE (Reduced Overhead Stereo Event and Intensity) a Real-Time framework for efficient depth estimation from events and intensity images. Current approaches rely on dense networks that fail to scale with increasing data complexity, constraining both accuracy and speed. In contrast, ROSE incorporates lightweight event representation networks and optimizes the stereo matching process to reduce model size and computational load without compromising accuracy.
We replace conventional network components with efficient spatio-temporal representations and streamline adaptive aggregation modules, reducing computational complexity by 1000× compared to previous methods. Furthermore, we adapt event grouping strategies to better align with intensity images, improving the quality of depth estimation under various lighting and motion conditions. Extensive experiments on the DSEC and MVSEC benchmarks demonstrate that ROSE achieves real-time performance, boosting frame rates to 32.2 FPS on DSEC and 66.9 FPS on MVSEC while maintaining competitive depth accuracy. This marks a significant improvement over prior work in terms of speed and scalability, making ROSE a viable solution for real-time stereo depth estimation in resource-constrained environments. Our code and models will be released to support further advancements in the field.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
轻量实时双目深度估计。

### 2. 核心内容
针对事件相机立体深度估计计算开销大、难以实时的问题，该文提出ROSE框架，结合轻量级事件表示网络与优化立体匹配来降低模型规模和计算量。方法在事件和强度图像上实现实时深度估计，同时保持精度。其高效双目匹配思路可迁移到手机双摄小基线深度估计。

### 3. 对应检索需求
Papers central to 双目深度估计，重点关注手机双摄、小基线、校正误差和非严格校正双目。, especially work that connects or combines: dual-camera depth; rectification-free stereo; binocular depth estimation for mobile dual cameras; dual camera stereo matching small baseline; uncalibrated stereo depth estimation dual camera; mobile stereo depth estimation smartphone dual camera; stereo depth estimation for occlusion weak texture and portrait bokeh scenes; stereo depth estimation for mobile dual camera and small baseline systems; unrectified stereo matching robust to calibration and rectification errors; lightweight stereo matching for real time depth estimation on mobile devices.

### 4. 来源与原文
- Source：ICLR-2025-Public
- OpenReview：[https://openreview.net/forum?id=IjLumaGZ4h](https://openreview.net/forum?id=IjLumaGZ4h)
