---
title: "DERD-Net: Learning Depth from Event-based Ray Densities"
title_zh: DERD-Net：基于事件射线密度的深度估计网络
authors: "Diego de Oliveira Hitzges, Suman Ghosh, Guillermo Gallego"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=0KnZasL9nA"
tags: ["query:mono-depth"]
score: 5.0
evidence: 单目与双目像素级深度估计
tldr: 事件相机数据异步且呈流式，面向离散图像设计的传统深度网络难以适配。该文提出DERD-Net，将事件按已知位姿反投影到空间生成视差空间图像，用其编码三维场景结构以实现像素级深度估计。方法在单目与双目设置下均适用，具备可扩展与灵活适配特性，为事件相机深度估计与SLAM提供了新框架。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 事件数据异步流式的特性使面向离散图像的传统深度网络难以直接用于深度估计。
method: 将事件按位姿反投影为视差空间图像，编码三维射线密度并用神经网络回归像素级深度。
result: 框架在单目与双目设置下均可实现可扩展的像素级深度估计。
conclusion: 为事件相机的深度估计与多视图立体、SLAM提供了通用适配框架。
---

## Abstract
Event cameras offer a promising avenue for multi-view stereo depth estimation and Simultaneous Localization And Mapping (SLAM) due to their ability to detect blur-free 3D edges at high-speed and over broad illumination conditions. However, traditional deep learning frameworks designed for conventional cameras struggle with the asynchronous, stream-like nature of event data, as their architectures are optimized for discrete, image-like inputs. We propose a scalable, flexible and adaptable framework for pixel-wise depth estimation with event cameras in both monocular and stereo setups. The 3D scene structure is encoded into disparity space images (DSIs), representing spatial densities of rays obtained by back-projecting events into space via known camera poses. Our neural network processes local subregions of the DSIs combining 3D convolutions and a recurrent structure to recognize valuable patterns for depth prediction. Local processing enables fast inference with full parallelization and ensures constant ultra-low model complexity and memory costs, regardless of camera resolution. Experiments on standard benchmarks (MVSEC and DSEC datasets) demonstrate unprecedented effectiveness:
(i) using purely monocular data, our method achieves comparable results to existing stereo methods; (ii) when applied to stereo data, it strongly outperforms all state-of-the-art (SOTA) approaches, reducing the mean absolute error by at least 42\%; (iii) our method also allows for increases in depth completeness by more than 3-fold while still yielding a reduction in median absolute error of at least 30\%. Given its remarkable performance and effective processing of event-data, our framework holds strong potential to become a standard approach for using deep learning for event-based depth estimation and SLAM.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
单目与双目像素级深度估计。

### 2. 核心内容
事件相机数据异步且呈流式，面向离散图像设计的传统深度网络难以适配。该文提出DERD-Net，将事件按已知位姿反投影到空间生成视差空间图像，用其编码三维场景结构以实现像素级深度估计。方法在单目与双目设置下均适用，具备可扩展与灵活适配特性，为事件相机深度估计与SLAM提供了新框架。

### 3. 对应检索需求
monocular depth estimation。

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=0KnZasL9nA](https://openreview.net/forum?id=0KnZasL9nA)
