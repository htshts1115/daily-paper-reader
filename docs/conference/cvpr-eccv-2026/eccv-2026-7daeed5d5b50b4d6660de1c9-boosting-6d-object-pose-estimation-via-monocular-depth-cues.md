---
title: Boosting 6D Object Pose Estimation via Monocular Depth Cues
title_zh: 利用单目深度线索提升6D物体位姿估计
authors: "Fengda Hao, Rui Song, Qingyuan Wang, Jiaojiao Li, Zhiyong Hu, David Ferstl, Yinlin Hu"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/12811.pdf"
tags: ["query:mono-depth"]
score: 6.0
evidence: 利用单目深度线索
tldr: 针对单目深度尺度模糊、局部不可靠而难以用于度量位姿优化的问题，本文提出仅用RGB的6D物体位姿估计方法，将深度校正与位姿优化构成迭代闭环，利用位姿诱导的几何一致性对深度进行校准与滤波，并设计动态深度离群点剔除模块。实验表明该方法能从单目图像获得稳定的度量位姿更新，提升位姿估计精度，为单目深度在度量几何任务中的应用提供了新思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 441, \"height\": 430}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 386, \"height\": 374}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 486, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 471, \"height\": 445}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 1024, \"height\": 976}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 455, \"height\": 361}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-7daeed5d5b50b4d6660de1c9/fig-007.webp\", \"caption\": \"\", \"page\": 13, \"index\": 7, \"width\": 2400, \"height\": 2400}]"
motivation: 单目深度估计虽有进展，但尺度模糊且局部不可靠，难以直接用于度量位姿优化。
method: 提出仅用RGB的方法，将深度校正与位姿优化闭环迭代，用位姿诱导的几何一致性校准并过滤深度，并设计动态深度离群点剔除模块。
result: 通过循环优化实现稳定的度量位姿更新，在单目输入下提升6D位姿估计精度。
conclusion: 表明单目深度可作为可迭代校准的几何约束，服务于度量位姿估计。
---

## Abstract
We present an RGB-only method for 6D object pose esti-mation that leverages monocular depth cues from a single image. Al-though monocular depth estimation has advanced substantially, its pre-dictions remain scale-ambiguous and locally unreliable, limiting theiruse in metric pose refinement. We address this gap by closing the loopbetween depth correction and pose refinement: monocular depth is notonly a regularizer but is iteratively calibrated and filtered using pose-induced geometric consistency, enabling stable metric pose updates fromRGB alone. We propose a dynamic depth outlier removal module basedon metric consistency and infer object pose from dense 2D correspon-dences. Both components are embedded into a recurrent optimizationloop, enabling iterative depth correction and pose refinement. Experi-ments on seven BOP datasets demonstrate state-of-the-art performanceamong RGB-only methods, without requiring real depth input.

---

## 论文详细总结（自动生成）

# 论文总结：Boosting 6D Object Pose Estimation via Monocular Depth Cues

## 1. 核心问题与整体含义
- **研究任务**：仅使用单张 RGB 图像进行 6D 物体位姿估计与位姿细化，不依赖真实深度输入。
- **核心问题**：单目观测天然存在尺度歧义与几何不确定性；现有多数 RGB 位姿细化方法依赖光度一致性或光流一致性，在无纹理、遮挡、反光、光照变化等场景下容易失效。与此同时，单目深度估计虽发展迅速，但预测结果仍存在尺度模糊、局部噪声和离群区域，难以直接用于度量位姿优化。
- **整体含义**：论文将单目深度从“固定辅助先验”转变为“可迭代校准、可滤波的几何中间表示”，通过深度校正与位姿优化的闭环，实现仅 RGB 输入下的稳定度量位姿更新。其意义在于为低成本、无深度传感器的 6D 位姿估计提供新思路。

## 2. 方法论
- **总体框架 MDC-Net**：
  - 输入：单张 RGB 图像、初始位姿 \(P_{k-1}\)、相机内参、目标 CAD 模型。
  - 使用预训练单目深度估计器生成深度图；每轮迭代根据当前位姿渲染物体，获得渲染 RGB、深度、掩码和可见表面点。
  - 构建 4D cost volume，使用基于 GRU 的循环位姿回归器预测残差位姿 \(\Delta P_k\)，更新得到 \(P_k\)。
  - 核心闭环：位姿诱导几何一致性用于校正深度，校正后的深度再用于下一轮位姿细化。
- **Scale Refinement Module，SRM**：
  - 目标：将相对单目深度转换为具有度量一致性的绝对深度代理。
  - 公式：\(D_{abs}(x,y)=S(x,y)\cdot
