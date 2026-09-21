---
title: "InstantPortrait: One-Step Portrait Editing via Diffusion Multi-Objective Distillation"
title_zh: InstantPortrait：基于扩散多目标蒸馏的单步人像编辑
authors: "Zhixin Lai, Keqiang Sun, Fu-Yun Wang, Dhritiman Sagar, Erli Ding"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=ZkFMe3OPfw"
tags: ["query:cv-render"]
score: 4.0
evidence: 面向滤镜与AR的实时人像编辑
tldr: 针对实时人像编辑中身份保持、指令一致与推理速度三者难以兼顾的问题，论文提出InstantPortrait网络，通过扩散多目标蒸馏实现单步人像编辑。该方法在滤镜、增强现实与视频通信等场景下兼顾编辑保真度与身份一致性，并大幅提升推理速度。虽不直接做散景渲染，但其实时人像滤镜思路与移动端人像处理相关。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 实时人像编辑需同时兼顾身份保持、指令保真与快速推理，现有扩散方法缺乏专门设计。
method: 提出InstantPortrait网络IPNet，通过扩散多目标蒸馏实现单步人像图像编辑。
result: 在滤镜、AR与视频通信等场景实现实时人像编辑并保持身份与指令一致性。
conclusion: 为实时人像编辑提供了高效方案，对移动端人像处理具有参考价值。
---

## Abstract
Real-time instruction-based portrait image editing is crucial in various applications, including filters, augmented reality, and video communications, etc. However, real-time portrait editing presents three significant challenges: identity preservation, fidelity to editing instructions, and fast model inference. Given that these aspects often present a trade-off, concurrently addressing them poses an even greater challenge. While diffusion-based image editing methods have shown promising capabilities in personalized image editing in recent years, they lack a dedicated focus on portrait editing and thus suffer from the aforementioned problems as well. To address the gap, this paper introduces an Instant-Portrait Network (IPNet), the first one-step diffusion-based model for portrait editing. We train the network in two stages. We first employ an annealing identity loss to train an Identity Enhancement Network (IDE-Net), to ensure robust identity preservation. We then train the IPNet using a novel diffusion Multi-Objective Distillation approach that integrates adversarial loss, identity distillation loss, and a novel Facial-Style Enhancing loss. The Diffusion Multi-Objective Distillation approach efficiently reduces inference steps, ensures identity consistency, and enhances the precision of instruction-based editing. Extensive comparison with prior models demonstrates IPNet as a superior model in terms of identity preservation, text fidelity, and inference speed.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
面向滤镜与AR的实时人像编辑。

### 2. 核心内容
针对实时人像编辑中身份保持、指令一致与推理速度三者难以兼顾的问题，论文提出InstantPortrait网络，通过扩散多目标蒸馏实现单步人像编辑。该方法在滤镜、增强现实与视频通信等场景下兼顾编辑保真度与身份一致性，并大幅提升推理速度。虽不直接做散景渲染，但其实时人像滤镜思路与移动端人像处理相关。

### 3. 对应检索需求
digital filter effects for portrait photography including pro mist glow diffusion and cinematic rendering。

### 4. 来源与原文
- Source：ICLR-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=ZkFMe3OPfw](https://openreview.net/forum?id=ZkFMe3OPfw)
