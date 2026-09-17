---
title: "AerialMetric: Benchmarking and Adapting UAV Monocular Metric Depth Estimation in the Real World"
title_zh: "AerialMetric:真实世界无人机单目度量深度估计的基准与适配"
authors: "Zhongqiang Song, Guanying Chen, Yuqi Zhang, Yin Zou, Chuanyu Fu, Zhiyuan Yuan, Chuan Huang, Shuguang Cui, Xiaochun Cao"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/4112.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 面向航拍影像的单目度量深度估计基准与适配
tldr: "单目度量深度估计在地面场景已取得进展,但主要在街景和室内数据上训练的模型应用于航拍视角时存在显著域差异。本文提出AerialMetric,一个用于评测和促进无人机航拍视角下单目度量深度估计适配的基准数据集。该数据集包含四个互补子集,覆盖真实摄影测量、受控航拍采集、逼真合成场景与野外数据。该工作揭示了域差异问题并推动航拍度量深度估计的适配研究。"
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-940a409b6548cd2db6106d19/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 3741, \"height\": 1401}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-940a409b6548cd2db6106d19/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 6693, \"height\": 5220}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-940a409b6548cd2db6106d19/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 5550, \"height\": 5207}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-940a409b6548cd2db6106d19/fig-004.webp\", \"caption\": \"\", \"page\": 11, \"index\": 4, \"width\": 4896, \"height\": 1710}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-940a409b6548cd2db6106d19/fig-005.webp\", \"caption\": \"\", \"page\": 12, \"index\": 5, \"width\": 5556, \"height\": 1902}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-940a409b6548cd2db6106d19/fig-006.webp\", \"caption\": \"\", \"page\": 14, \"index\": 6, \"width\": 4824, \"height\": 1805}]"
motivation: 针对地面训练的度量深度模型在无人机航拍视角下存在显著域差异、缺乏评测基准的问题。
method: "构建AerialMetric基准数据集,包含真实摄影测量、受控航拍、合成场景与野外四个互补子集,用于评测与适配。"
result: "揭示地面模型在航拍视角的域差异,并为单目度量深度估计的适配提供系统评测平台。"
conclusion: 推动无人机航拍场景下单目度量深度估计的域适配研究。
---

## Abstract
This paper addresses the problem of monocular metric depth estimation in aerial UAV imagery. Although recent data-driven methods have achieved remarkable progress in ground-level scenarios, models trained primarily on street-view and indoor datasets exhibit significant domain gaps when applied to aerial viewpoints. To tackle these challenges, we introduce AerialMetric, a benchmark dataset designed to evaluate and facilitate the adaptation of monocular metric depth estimation under UAV aerial viewpoints. The dataset consists of four complementary subsets collected from different sources, jointly covering real-world photogrammetry data, controlled aerial acquisition settings, photorealistic synthetic scenes, and in-the-wild Internet imagery. In total, AerialMetric provides 52K real-world and 16K synthetic image–depth pairs with reliable metric ground truth. Based on this dataset, we conduct systematic evaluations of existing state-of-the-art models under aerial settings and investigate the impact of viewpoint, altitude, and camera parameters on metric depth prediction. In addition, by fine-tuning representative metric depth model on our dataset, we establish a comprehensive aerial benchmark and achieve state-of-the-art performance across diverse aerial imagery. Our dataset, code, and model weight are publicly available at https://kuieless.github.io/AerialMetric-ECCV2026-page/.

---

## 论文详细总结（自动生成）

# AerialMetric 论文中文总结

## 1. 核心问题与整体含义
- **研究背景**：无人机在配送、巡检、环境监测、公共安全等场景中需要可靠的三维感知，单目度量深度估计可从单张图像恢复具有绝对尺度的场景几何。
- **核心问题**：现有数据驱动度量深度模型主要在街景、室内等地面视角数据上训练，直接迁移到无人机航拍视角时存在显著域差异；航拍图像具有俯视/斜视几何、高度变化大、视场角变化、深度范围广等特点，导致地面模型性能严重退化。
- **领域缺口**：缺少真实、多样、变量可控且带可靠度量深度真值的航拍数据集，也缺少系统评测航拍单目度量深度估计的基准。
- **整体含义**：论文提出 **AerialMetric** 基准数据集，包含真实摄影测量、受控航拍采集、逼真合成和野外互联网影像四类互补子集，用于评测并推动无人机航拍场景下的单目度量深度估计适配。

## 2. 方法论：核心思想与关键技术细节
- **核心思想**：通过多源、多视角、变量解耦的航拍数据构建统一基准，系统分析视角、高度、FOV 等成像因素对度量深度的影响，并基于该数据对代表性模型进行参数高效适配。
- **四个互补子集**：
  - **AerialMetric-Oblique**：聚合 UrbanBIS、GauU-SceneV2、UAVScenes、UrbanScene3D、ODM、ESRI 等六个公开城市级摄影测量数据集，覆盖 25 个子数据集，构建超过 47K 图像–深度对，场景包括城市、乡村、自然。
  - **AerialMetric-Decoupled**：自采受控数据，使用 DJI Matrice 300 RTK，配备 Zenmuse L1 与 P1。正交采样俯仰角 \(-90^\circ,-75^\circ,-60^\circ,-45^\circ\)、相对高度 80m/120m、FOV 83°/63°，覆盖 Building、Lawn、Farm、Factory 四类场景，约 4,600 对，仅用于测试。
  - **AerialMetric-Synthetic**：由 Google Earth Studio 与 Unreal Engine + AirSim + Cesium 生成，约 16K RGB-D 对，分辨率 3840×2160，覆盖极端视角、复杂
