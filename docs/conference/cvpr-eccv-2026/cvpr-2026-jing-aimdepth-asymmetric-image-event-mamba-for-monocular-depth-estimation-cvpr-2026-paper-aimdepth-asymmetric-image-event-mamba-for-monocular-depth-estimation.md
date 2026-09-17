---
title: "AIMDepth: Asymmetric Image-Event Mamba for Monocular Depth Estimation"
title_zh: AIMDepth：面向单目深度估计的非对称图像-事件Mamba
authors: "Jing, Luoxi, Shi, Dianxi, Cao, Yushe, Wang, Yuanze, Zhang, Junze, Cui, Yuning, Wang, Mengzhu"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Jing_AIMDepth_Asymmetric_Image-Event_Mamba_for_Monocular_Depth_Estimation_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于图像-事件融合的单目深度估计
tldr: 单目深度估计对机器人等应用至关重要，图像与事件模态互补，但现有融合方法受限于卷积或注意力的长程建模能力与高计算成本，且忽视事件与图像间的域差异，易产生语义偏差。本文提出AIMDepth，采用非对称图像-事件Mamba架构，在融合特征时缓解模态表示差异，适配长序列深度估计。实验显示其在精度与效率上均优于现有方法。该工作为多模态鲁棒深度估计提供了新思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1248, \"height\": 489}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 422, \"height\": 319}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 8, \"index\": 6, \"width\": 2461, \"height\": 1240}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-aimdepth-asymmetric-image-event-mamba-for-monocular-depth-estimation-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 11, \"index\": 7, \"width\": 985, \"height\": 551}]"
motivation: 现有图像-事件融合深度方法受限于卷积或注意力架构的长程建模能力与高计算成本，且未处理模态域差异导致语义偏差。
method: 提出AIMDepth，采用非对称图像-事件Mamba架构，在融合中显式缓解事件与图像的表示差异与域间隙。
result: 在深度估计任务上取得优于现有融合方法的精度，同时降低长序列建模的计算开销。
conclusion: 验证了Mamba式非对称融合在鲁棒单目深度估计中的有效性。
---

## Abstract
Monocular depth estimation is essential for applications such as robotics. The complementary characteristics of event and image modalities have inspired fusion-based methods for robust depth estimation. However, existing methods rely on convolutional or attention-based architectures, which either have limited capacity for long-range modeling or incur high computational cost, making them less suitable for depth estimation over long sequences. Moreover, effective image-event fusion remains challenging, since most methods directly fuse features without addressing the domain gap and representational differences between raw events and images, resulting in semantic bias and degraded performance. In this work, we propose AIMDepth, an Asymmetric Image-Event Mamba framework for monocular depth estimation, built on state space models for linear complexity and accurate prediction. To alleviate input-domain misalignment, we introduce a Spectral Cross-modal Prior Guidance (SCPG) for bidirectional prior injection at the input level. To reduce the imbalance between sparse events and dense images, we design an asymmetric modal-aware Encoder (AME) with separate encoding paths and feature-level alignment. We further develop a Modality-interactive Local Refinement (ModiLocal) to enable hierarchical interaction and fine-grained alignment. Experiments on public datasets show that AIMDepth achieves state-of-the-art performance in complex environments.

---

## 论文详细总结（自动生成）

# AIMDepth：面向单目深度估计的非对称图像-事件 Mamba —— 论文深度总结

## 1. 核心问题与研究背景

- **任务重要性**：单目深度估计是自动驾驶、机器人、增强现实等应用的基础任务。
- **单一模态的瓶颈**：
  - 纯图像方法能提供稠密空间细节，但在运动模糊、极端光照（如夜间）下性能显著退化。
  - 事件相机异步捕捉逐像素亮度变化，具有高时间分辨率与高动态范围，在高速运动/低光场景中鲁棒；但事件数据本质稀疏、以边缘驱动，单独使用时结构表征不完整。
- **融合动机**：图像与事件在信息密度与语义结构上互补，融合可提升跨场景鲁棒深度估计。
- **现有融合方法的不足**：
  - 基于 CNN 的方法（RAMNet、SRFNet）感受野有限，全局上下文建模能力弱；
  - 基于 Transformer 的方法（ER-F2D、UniCT Depth、HMNet）自注意力为二次复杂度，难以扩展到长序列深度估计；
  - 融合范式分为**隐式**（编码器内部融合）与**显式**（对称编码器 + 专用融合模块），二者**均忽略事件（稀疏、动态）与图像（稠密、静态）之间的域差异与表示错位**，直接融合会引入语义偏差，导致表征次优、深度精度下降。
- **本文定位**：提出 **AIMDepth**，据作者所述是**首个将状态空间模型（Mamba/SSM）用于图像-事件融合单目深度估计**的工作，同时追求线性计算复杂度、显式的跨模态对齐与高精度预测。

## 2. 方法论

### 2.1 整体框架

- 采用 U-Net 式结构，由四个关键组件构成：**SCPG**（输入级对齐）→ **AME**（特征级对齐）→ **ModiLocal**（渐进融合与细粒度精修）→ **基于 Mamba 的解码器**（空间重建与深度输出）。
- 输入处理：原始事件体素栅格 `E_raw` 经双线性插值转为类图像表示 `E ∈ R^{K×H×W}`（K 为时间 bin 数），与图像 `I ∈ R^{C×H×W}` 同步；SCPG 输出对齐后的 `Ẽ` 与 `Ĩ`。
- 核心设计思路是**分层对齐策略**：先在输入级缩小模态分布差异，再在特征级进行非对称对齐，最后做多语义层级的交互融合。

### 2.2 SCPG：频谱跨模态先验引导（输入级对齐）

- 核心思想：在**频域**做双向先验注入，利用两模态互补的频谱特性，天然可解释且与 Mamba 架构契合。
- **EAT（Event-targeted Amplitude Transfer，事件导向幅度迁移）**：
  - 对事件体素 `E` 与图像 `I` 分别做二维 DFT，分解为幅度谱 `F_A(·)` 与相位谱 `F_P(·)`。
  - 构造中心低频方形二值掩码 `M_β(h,w)=1` 当 `|h| ≤ βH` 且 `|w| ≤ βW`，否则为 0（β 为预设比例，实验中取 0.01）。
  - 逐事件通道用图像低频幅度替换事件低频幅度：`F'_A(E_c) = M_β·F_A(I) + (1−M_β)·F_A(E_c)`。
  - 再以**原事件相位**做逆傅里叶变换重建 `Ẽ_c = F^{-1}(F'_A(E_c)·e^{jF_P(E_c)})`，从而引入图像全局轮廓/空间布局先验，同时保留事件的高频时序动态。
- **IPE（Image-targeted Phase Enhancement，图像
