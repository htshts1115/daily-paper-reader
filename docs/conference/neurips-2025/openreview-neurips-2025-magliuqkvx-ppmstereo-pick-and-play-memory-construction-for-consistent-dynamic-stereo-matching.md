---
title: "PPMStereo: Pick-and-Play Memory Construction for Consistent Dynamic Stereo Matching"
title_zh: PPMStereo：面向一致动态立体匹配的即插即用记忆构建
authors: "Yun Wang, Junjie Hu, Qiaole Dong, Yongjian Zhang, Yanwei Fu, Tin Lun Lam, Dapeng Wu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=MaglIUQKVX"
tags: ["query:stereo-depth"]
score: 6.0
evidence: 双目视频时序一致深度估计
tldr: 针对立体视频中深度估计时序不一致、破坏增强现实沉浸感的问题，现有方法在长程时序建模与计算开销之间存在难以调和的矛盾。本文提出PPMStereo，引入可即插即用的记忆缓冲区，在保持计算高效的同时建模长程时空一致性。实验表明该方法在动态立体匹配上取得一致且高效的结果，为立体视频深度估计提供了新的时序建模思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 立体视频深度估计时序不一致会破坏AR沉浸感，而长程时序建模与计算效率难以兼顾。
method: 提出即插即用的记忆缓冲区，用于高效建模长程时空一致性以提升动态立体匹配。
result: 在动态立体匹配任务上实现时序一致且计算高效的深度估计结果。
conclusion: 为立体视频时序一致的深度估计提供了一种可插拔的高效记忆建模方案。
---

## Abstract
Temporally consistent depth estimation from stereo video is critical for real-world applications such as augmented reality, where inconsistent depth estimation disrupts the immersion of users.
Despite its importance, this task remains challenging due to the difficulty in modeling long-term temporal consistency in a computationally efficient manner.
Previous methods attempt to address this by aggregating spatio-temporal information but face a fundamental trade-off: limited temporal modeling provides only modest gains, whereas capturing long-range dependencies significantly increases computational cost.
To address this limitation, we introduce a memory buffer for modeling long-range spatio-temporal consistency while achieving efficient dynamic stereo matching.
Inspired by the two-stage decision-making process in humans, we propose a Pick-and-Play Memory (PPM) construction module for dynamic Stereo matching, dubbed as PPMStereo. PPM consists of a pick process that identifies the most relevant frames and a play process that weights the selected frames adaptively for spatio-temporal aggregation.
This two-stage collaborative process maintains a compact yet highly informative memory buffer while achieving temporally consistent information aggregation.
Extensive experiments validate the effectiveness of PPMStereo, demonstrating state-of-the-art performance in both accuracy and temporal consistency.Codes are available at \textcolor{blue}{https://github.com/cocowy1/PPMStereo}.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
双目视频时序一致深度估计。

### 2. 核心内容
针对立体视频中深度估计时序不一致、破坏增强现实沉浸感的问题，现有方法在长程时序建模与计算开销之间存在难以调和的矛盾。本文提出PPMStereo，引入可即插即用的记忆缓冲区，在保持计算高效的同时建模长程时空一致性。实验表明该方法在动态立体匹配上取得一致且高效的结果，为立体视频深度估计提供了新的时序建模思路。

### 3. 对应检索需求
Papers central to 双目深度估计，重点关注手机双摄、小基线、校正误差和非严格校正双目。, especially work that connects or combines: dual-camera depth; rectification-free stereo; binocular depth estimation for mobile dual cameras; dual camera stereo matching small baseline; uncalibrated stereo depth estimation dual camera; mobile stereo depth estimation smartphone dual camera; stereo depth estimation for occlusion weak texture and portrait bokeh scenes; stereo depth estimation for mobile dual camera and small baseline systems; unrectified stereo matching robust to calibration and rectification errors; lightweight stereo matching for real time depth estimation on mobile devices.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=MaglIUQKVX](https://openreview.net/forum?id=MaglIUQKVX)
