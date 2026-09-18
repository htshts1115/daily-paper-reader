---
title: "LiFR-Seg: Anytime High-Frame-Rate Segmentation via Event-Guided Propagation"
title_zh: LiFR-Seg：基于事件引导传播的任意时刻高帧率分割
authors: "Xiaoshan Wu, Xiaoyang Lyu, Yifei Yu, Bo Wang, Zhongrui Wang, Xiaojuan Qi"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=9oS7DHIg7f"
tags: ["query:seg"]
score: 6.0
evidence: 事件引导传播的稠密语义分割
tldr: 标准相机帧率低，动态环境中帧间存在严重感知空缺，难以获得稠密连续的语义分割。论文提出任意时刻帧间语义分割新任务，并设计LiFR-Seg框架，仅用单帧历史RGB与异步事件流，通过事件导出的运动场稳健传播深层语义特征。实验表明该方法在高度动态场景中抑制特征退化，实现任意时刻的高帧率分割。该工作为事件相机辅助的稠密语义分割提供了新任务设定与有效框架。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 标准相机帧率低，动态场景帧间存在感知空缺，难以获得稠密连续的语义分割。
method: 提出任意时刻帧间语义分割任务，并设计LiFR-Seg，用单帧RGB与异步事件流传播语义特征。
result: 借助事件运动场在高度动态场景中稳健传播语义，实现任意时刻高帧率分割。
conclusion: 为事件相机辅助的稠密语义分割提供了新任务定义与有效框架。
---

## Abstract
Dense semantic segmentation in dynamic environments is fundamentally limited by the low-frame-rate (LFR) nature of standard cameras, which creates critical perceptual gaps between frames.
To solve this, we introduce *Anytime Interframe Semantic Segmentation*: a new task for predicting segmentation at any arbitrary time using only a single past RGB frame and a stream of asynchronous event data.
This task presents a core challenge: how to robustly propagate dense semantic features using a motion field derived from sparse and often noisy event data, all while mitigating feature degradation in highly dynamic scenes.
We propose LiFR-Seg, a novel framework that directly addresses these challenges by propagating deep semantic features through time. The core of our method is an *uncertainty-aware warping process*, guided by an event-driven motion field and its learned, explicit confidence. A *temporal memory attention* module further ensures coherence in dynamic scenarios.
We validate our method on the DSEC dataset and a new high-frequency synthetic benchmark (SHF-DSEC) we contribute. Remarkably, our LFR system achieves performance (73.82\% mIoU on DSEC) that is statistically indistinguishable from an HFR upper-bound (within 0.09\%) that has full access to the target frame.
% We further demonstrate superior robustness in *highly dynamic* (M3ED-Drone \& Quadruped) and *low-light* (DSEC-Night) scenarios, where our method can even surpass the HFR baseline.
We further demonstrate superior robustness across extreme scenarios: in highly dynamic (M3ED) tests, our method closely matches the HFR baseline's performance, while in the low-light (DSEC-Night) evaluation, it even surpasses it.
This work presents a new, efficient paradigm for achieving robust, high-frame-rate perception with low-frame-rate hardware.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
事件引导传播的稠密语义分割。

### 2. 核心内容
标准相机帧率低，动态环境中帧间存在严重感知空缺，难以获得稠密连续的语义分割。论文提出任意时刻帧间语义分割新任务，并设计LiFR-Seg框架，仅用单帧历史RGB与异步事件流，通过事件导出的运动场稳健传播深层语义特征。实验表明该方法在高度动态场景中抑制特征退化，实现任意时刻的高帧率分割。该工作为事件相机辅助的稠密语义分割提供了新任务设定与有效框架。

### 3. 对应检索需求
semantic segmentation。

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=9oS7DHIg7f](https://openreview.net/forum?id=9oS7DHIg7f)
