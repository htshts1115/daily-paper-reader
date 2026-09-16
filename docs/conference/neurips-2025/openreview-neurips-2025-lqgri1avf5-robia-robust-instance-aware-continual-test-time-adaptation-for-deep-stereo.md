---
title: "RobIA: Robust Instance-aware Continual Test-time Adaptation for Deep Stereo"
title_zh: RobIA：面向深度双目估计的稳健实例感知持续测试时自适应
authors: "Jueun Ko, Hyewon Park, Hyesong Choi, Dongbo Min"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=LqgRi1avf5"
tags: ["query:stereo-depth"]
score: 7.0
evidence: 面向双目深度估计的持续测试时自适应
tldr: 真实环境中的双目深度估计面临动态域偏移、监督稀疏与标注昂贵等挑战。本文提出RobIA，一种面向双目深度估计的稳健实例感知持续测试时自适应框架，通过专家混合模块动态路由输入到冻结专家并进行轻量自适应。方法在持续变化的场景下提升双目深度估计的适应性与稳定性，为真实场景双目深度提供了鲁棒方案。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 真实场景双目深度估计面临动态域偏移和昂贵标注的挑战。
method: 提出实例感知持续测试时自适应框架，用专家混合动态路由进行轻量适配。
result: 在持续域偏移下提升双目深度估计的适应性与稳健性。
conclusion: 为真实环境双目深度估计提供了高效自适应方案。
---

## Abstract
Stereo Depth Estimation in real-world environments poses significant challenges due to dynamic domain shifts, sparse or unreliable supervision, and the high cost of acquiring dense ground-truth labels. While recent Test-Time Adaptation (TTA) methods offer promising solutions, most rely on static target domain assumptions and input-invariant adaptation strategies, limiting their effectiveness under continual shifts. In this paper, we propose RobIA, a novel Robust, Instance-Aware framework for Continual Test-Time Adaptation (CTTA) in stereo depth estimation. RobIA integrates two key components: (1) Attend-and-Excite Mixture-of-Experts (AttEx-MoE), a parameter-efficient module that dynamically routes input to frozen experts via lightweight self-attention mechanism tailored to epipolar geometry, and (2) Robust AdaptBN Teacher, a PEFT-based teacher model that provides dense pseudo-supervision by complementing sparse handcrafted labels. 
This strategy enables input-specific flexibility, broad supervision coverage, improving generalization under domain shift. Extensive experiments demonstrate that RobIA achieves superior adaptation performance across dynamic target domains while maintaining computational efficiency.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向双目深度估计的持续测试时自适应。

### 2. 核心内容
真实环境中的双目深度估计面临动态域偏移、监督稀疏与标注昂贵等挑战。本文提出RobIA，一种面向双目深度估计的稳健实例感知持续测试时自适应框架，通过专家混合模块动态路由输入到冻结专家并进行轻量自适应。方法在持续变化的场景下提升双目深度估计的适应性与稳定性，为真实场景双目深度提供了鲁棒方案。

### 3. 对应检索需求
Papers central to 双目深度估计，重点关注手机双摄、小基线、校正误差和非严格校正双目。, especially work that connects or combines: dual-camera depth; rectification-free stereo; binocular depth estimation for mobile dual cameras; dual camera stereo matching small baseline; uncalibrated stereo depth estimation dual camera; mobile stereo depth estimation smartphone dual camera; stereo depth estimation for occlusion weak texture and portrait bokeh scenes; stereo depth estimation for mobile dual camera and small baseline systems; unrectified stereo matching robust to calibration and rectification errors; lightweight stereo matching for real time depth estimation on mobile devices.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=LqgRi1avf5](https://openreview.net/forum?id=LqgRi1avf5)
