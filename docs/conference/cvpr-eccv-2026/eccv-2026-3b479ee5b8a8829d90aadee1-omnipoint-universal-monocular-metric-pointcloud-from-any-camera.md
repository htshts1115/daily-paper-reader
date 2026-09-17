---
title: "OmniPoint: Universal Monocular Metric Pointcloud from Any Camera"
title_zh: OmniPoint：任意相机的通用单目度量点云
authors: "Botao Ye, Marc Pollefeys, Ming-Hsuan Yang, Abhijit Kundu"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11401.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 通用单目度量深度与点云重建
tldr: 从单目图像恢复度量三维几何是计算机视觉的基础任务，但现有方法被固定相机模型假设与僵化输入方案所割裂，难以适配鱼眼、等距柱状等传感器。本文提出统一框架OmniPoint，放弃传统平面深度回归，采用解耦的射线与距离表示及解耦训练目标，将相机投影模型与场景结构分离，并应对替代相机训练数据稀缺的问题。实验表明其可在多种相机上泛化度量重建。该工作推动了通用单目度量深度估计。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 611, \"height\": 395}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 739, \"height\": 415}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 758, \"height\": 379}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 462, \"height\": 379}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 689, \"height\": 343}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 758, \"height\": 379}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 614, \"height\": 379}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 376, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 378, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 683, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 759, \"height\": 379}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 420, \"height\": 339}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 757, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 573, \"height\": 274}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 579, \"height\": 410}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-016.webp\", \"caption\": \"\", \"page\": 1, \"index\": 16, \"width\": 527, \"height\": 395}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-017.webp\", \"caption\": \"\", \"page\": 1, \"index\": 17, \"width\": 527, \"height\": 395}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-018.webp\", \"caption\": \"\", \"page\": 1, \"index\": 18, \"width\": 611, \"height\": 396}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 541, \"height\": 278}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-020.webp\", \"caption\": \"\", \"page\": 11, \"index\": 20, \"width\": 415, \"height\": 309}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-021.webp\", \"caption\": \"\", \"page\": 11, \"index\": 21, \"width\": 414, \"height\": 308}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-022.webp\", \"caption\": \"\", \"page\": 11, \"index\": 22, \"width\": 414, \"height\": 308}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-023.webp\", \"caption\": \"\", \"page\": 11, \"index\": 23, \"width\": 412, \"height\": 412}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-024.webp\", \"caption\": \"\", \"page\": 11, \"index\": 24, \"width\": 424, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-025.webp\", \"caption\": \"\", \"page\": 11, \"index\": 25, \"width\": 449, \"height\": 271}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-026.webp\", \"caption\": \"\", \"page\": 11, \"index\": 26, \"width\": 407, \"height\": 322}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-027.webp\", \"caption\": \"\", \"page\": 11, \"index\": 27, \"width\": 416, \"height\": 333}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-028.webp\", \"caption\": \"\", \"page\": 11, \"index\": 28, \"width\": 413, \"height\": 332}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-029.webp\", \"caption\": \"\", \"page\": 11, \"index\": 29, \"width\": 489, \"height\": 274}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-030.webp\", \"caption\": \"\", \"page\": 11, \"index\": 30, \"width\": 499, \"height\": 284}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-031.webp\", \"caption\": \"\", \"page\": 11, \"index\": 31, \"width\": 468, \"height\": 275}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-032.webp\", \"caption\": \"\", \"page\": 11, \"index\": 32, \"width\": 551, \"height\": 250}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-033.webp\", \"caption\": \"\", \"page\": 11, \"index\": 33, \"width\": 412, \"height\": 412}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-034.webp\", \"caption\": \"\", \"page\": 11, \"index\": 34, \"width\": 412, \"height\": 412}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-035.webp\", \"caption\": \"\", \"page\": 11, \"index\": 35, \"width\": 412, \"height\": 412}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-036.webp\", \"caption\": \"\", \"page\": 11, \"index\": 36, \"width\": 412, \"height\": 412}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-037.webp\", \"caption\": \"\", \"page\": 11, \"index\": 37, \"width\": 413, \"height\": 414}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-038.webp\", \"caption\": \"\", \"page\": 11, \"index\": 38, \"width\": 418, \"height\": 410}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-039.webp\", \"caption\": \"\", \"page\": 11, \"index\": 39, \"width\": 415, \"height\": 417}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-040.webp\", \"caption\": \"\", \"page\": 11, \"index\": 40, \"width\": 432, \"height\": 432}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-041.webp\", \"caption\": \"\", \"page\": 11, \"index\": 41, \"width\": 413, \"height\": 307}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-042.webp\", \"caption\": \"\", \"page\": 13, \"index\": 42, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-043.webp\", \"caption\": \"\", \"page\": 13, \"index\": 43, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-044.webp\", \"caption\": \"\", \"page\": 13, \"index\": 44, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-045.webp\", \"caption\": \"\", \"page\": 13, \"index\": 45, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-046.webp\", \"caption\": \"\", \"page\": 13, \"index\": 46, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-047.webp\", \"caption\": \"\", \"page\": 13, \"index\": 47, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-048.webp\", \"caption\": \"\", \"page\": 13, \"index\": 48, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-049.webp\", \"caption\": \"\", \"page\": 13, \"index\": 49, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-050.webp\", \"caption\": \"\", \"page\": 13, \"index\": 50, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-051.webp\", \"caption\": \"\", \"page\": 13, \"index\": 51, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-052.webp\", \"caption\": \"\", \"page\": 13, \"index\": 52, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-053.webp\", \"caption\": \"\", \"page\": 13, \"index\": 53, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-054.webp\", \"caption\": \"\", \"page\": 13, \"index\": 54, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-055.webp\", \"caption\": \"\", \"page\": 13, \"index\": 55, \"width\": 510, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3b479ee5b8a8829d90aadee1/fig-056.webp\", \"caption\": \"\", \"page\": 13, \"index\": 56, \"width\": 510, \"height\": 255}]"
motivation: 现有单目度量三维重建方法受限于固定相机模型假设与不灵活的输入方式，难以泛化到多种成像传感器。
method: 提出统一框架OmniPoint，放弃平面深度回归，改用解耦的射线-距离表示与解耦训练目标，分离相机投影模型与场景结构。
result: 在针孔、鱼眼与等距柱状投影等多种相机上实现通用度量重建，缓解替代相机的训练数据稀缺问题。
conclusion: 为跨相机模型的单目度量深度与点云重建提供了统一且可泛化的方案。
---

## Abstract
Recovering metric 3D geometry from monocular images is a fundamental computer vision task, yet current methods remain heavily fragmented by fixed camera model assumptions and inflexible input schemes. We present OmniPoint, a unified framework designed to generalize metric reconstruction across diverse imaging sensors, including pinhole, fisheye, and equirectangular projections, while accommodating varying geometric priors. To overcome projection rigidity, OmniPoint abandons conventional planar depth regression. It instead adopts a decoupled ray and distance representation alongside a decoupled training objective, explicitly separating the camera projection model from the scene structure. To address the severe scarcity of training data for alternative cameras, we introduce a bidirectional augmentation strategy that explicitly bridges labeled perspective data and unlabeled omnidirectional domains in 3D space. Furthermore, to seamlessly integrate optional inputs like camera intrinsics or sparse depth without destabilizing the network through feature distribution shifts, we propose a robust information injection mechanism. This mechanism utilizes learnable input state embeddings to resolve architectural ambiguity and applies vectorized Gaussian smoothing to densify irregular measurements. Extensive experiments demonstrate that OmniPoint achieves state-of-the-art zeroshot performance across multiple benchmarks, establishing a robust new standard for unified monocular 3D reconstruction.

---

## 论文详细总结（自动生成）

# OmniPoint 论文深度总结

## 1. 核心问题与研究背景

- **研究动机**：从单目图像恢复度量三维几何是计算机视觉的基础任务，近年在大规模数据集与视觉基础模型推动下，零样本深度/点云估计已取得显著进展。
- **核心痛点**：现有方法高度**碎片化**，存在两大刚性约束：
  - **固定相机模型假设**：绝大多数方法面向针孔相机；全景、鱼眼方法各自专用，模型之间无法互通。
  - **僵化的输入方案**：无法动态融合可选几何先验（相机内参、稀疏深度），切换输入模态会导致特征分布漂移。
- **现实需求**：机器人、自动驾驶常配备异构传感器（前向针孔 + 环视鱼眼 + LiDAR），当前需维护多个孤立模型，内存开销大且传感器融合复杂。
- **整体含义**：论文提出 **OmniPoint**，首个在单一框架内统一**任意相机模型**（针孔/鱼眼/360°全景）、**任意输出表示**（仿射不变深度、仿射不变点、度量点）与**灵活几何先验**（内参、稀疏深度）的单目几何估计框架。

## 2. 方法论

### 2.1 核心思想：相机无关的射线-距离表示

- 放弃传统平面深度回归（依赖 `P = z·K⁻¹[u,v,1]ᵀ` 的线性反投影），因为该公式在宽视场/非针孔相机下失效，且 `z` 在 180° 处发散、无法表示相机后方点。
- 也放弃直接预测像素级 `(x,y,z)` 坐标，因为这会把投影模型与场景结构纠缠在一起，迫使网络记忆各相机高度非线性的映射 `F:(u,v)→(x,y,z)`，造成优化冲突。
- **采用分解表示**：每个像素预测单位射线方向 `r ∈ R³` 与径向距离 `d ∈ R⁺`，三维点为 `P = d · r`。
  - 射线 `r` 吸收任意镜头畸变与投影几何；
  - 距离 `d` 表示纯结构距离，对相机模型完全不变。
- 与 UniK3D 使用球谐函数参数化射线场不同，显式射线-距离配对避免了球谐带来的过度平滑伪影，能更好捕捉强畸变边缘的突变几何。

### 2.2 解耦点学习（Decoupled Point Learning）

- 朴素 L1 点损失 `L_naive = Σ‖d̂ᵢ·r̂ᵢ − dᵢ·rᵢ‖₁` 会纠缠射线与距离误差：当射线预测错误时，梯度会错误地惩罚原本准确的距离预测。
- 提出**解耦训练目标**：
  - `L_ray = Σ‖r̂ᵢ − rᵢ‖₁`：独立监督反投影几何；
  - `L_point = Σ‖s*·d̂ᵢ·rᵢ − dᵢ·rᵢ‖₁`：将预测距离沿**真实射线**投影构造代理点，纯粹隔离距离误差；
  - 其中 `s*` 为通过 ROE 对齐在线求得的最优尺度。
- 消融表明该解耦对高保真点云至关重要。

### 2.3 双向数据增强（Bidirectional Data Augmentation）

- 针对非针孔真值数据极度稀缺的问题，在 3D 空间显式桥接有标注透视数据与无标注全向数据。
- **Perspective-to-Any 合成**：将大规模针孔数据集（含 GT 深度）反投影为稠密 3D 点云，再定义虚拟相机模型（鱼眼径向畸变或等距柱状全景）重投影，并用二值有效性掩码剔除遮挡空洞，生成配对监督。
- **Any-to-Perspective 自训练**：从无标注鱼眼/全景图中采样一个虚拟针孔视角，用已训练好的透视模型生成伪真值深度，再反投影拼回原坐标系形成伪标签；每次训练只采样一个 patch，避免多 patch 预测不一致。

### 2.4 可选几何输入注入

- **输入状态嵌入**：引入可学习的 `e_intrinsic` 与 `e_depth`，作为布尔指示器加入 ViT token 序列，显式告知当前激活的输入配置，解决架构歧义、防止特征分布漂移。
- **鲁棒几何注入**：
  - 内参可用时，预计算逐像素 GT 射线图 `R_gt`，经轻量卷积编码器与图像特征融合；
  - 稀疏深度先按有效值均值归一化以稳定尺度；再采用**全向量化高斯溅射**生成稠密一致深度图：以每个有效点为中心，权重 `w(Δu,Δv)=exp(−(Δu²+Δv²)/(2σ²))`，`σ` 与深度幅值成比例；通过 scatter-add 并行累加得 `D_smooth`；
  - 构造二值掩码 `M` 与 `D_smooth` 拼接后卷积投影，与图像嵌入融合引导 ViT。

### 2.5 训练损失与流程

- 总损失：`L = L_point + λ_ray·L_ray + λ_metric·L_metric + λ_normal·L_normal + λ_local·L_local + λ_mask·L_mask`；
  - `L_metric = ‖log(ŝ) − stopgrad(log s*)‖₂²` 强制全局尺度一致；
  - 另含法向、局部一致性与天空掩码损失。
- **三阶段训练**：
  1. 大规模透视数据集预训练，建立强基线；
  2. 混合合成与真实鱼眼/全景数据微调，使用双向增强；
  3. 冻结骨干，仅用 SegFormer 伪标签训练掩码头。

## 3. 实验设计

### 3.1 数据集与基准

- **训练数据**：29 个标注数据集，涵盖 ARKitScenes、HOI4D、Matterport3D、ScanNet++、Waymo、3D Ken Burns、BEDLAM、BlendedMVS、HyperSim、TartanAir、VirtualKITTI2、KITTI360 等；另用无标注全景数据集 Diverse360、360+x 做 Any-to-Perspective 训练。
- **评估基准**：
  - **小视场（S.FoV）**：8 个针孔数据集 —— NYUv2、KITTI、ETH3D、iBims-1、GSO、Sintel、DIODE、HAMMER；
  - **大视场（L.FoV）**：鱼眼数据集 KITTI360；
  - **360° 全景**：Stanford2D3D-S、PanoSUNCG。
- **指标**：相对误差 `Rel ↓` 与鲁棒内点率 `δ1 ↑`（遵循 MoGe）。

### 3.2 对比方法

- 仿射不变深度估计：Depth Anything v1/v2、MoGe、VGGT；
- 度量深度估计：ZoeDepth、Metric3Dv2、UniDepth/UniDepth v2、Depth Pro、MoGe v2、Depth Anything 3、UniK3D；
- 全景深度估计：DA²。
- 为保证公平，所有基线在**统一输入格式与标准化度量计算流程**下重新评估。

## 4. 资源与算力

- **骨干网络**：DINOv2-ViT-Large，DPT 头预测 3D 点与掩码。
- **算力配置**：
  - 第一阶段：**72 张 A100 GPU**，每卡 batch size 8，训练 **10k 步**，约 **20 小时**；
  - 第二阶段：相同硬件，训练 **5k 步**；
  - 第三阶段：冻结骨干仅训练掩码头（未详述时长）。
- 论文明确给出了主要阶段的 GPU 型号、数量与时长，但第三阶段及数据增强/伪标签生成的额外开销未详细量化。

## 5. 实验数量与充分性

- **主要实验表格**：
  - Tab. 2：跨 S.FoV / L.FoV / 360° 的相对几何与深度对比；
  - Tab. 3：6 个基准的零样本度量深度 `δ1` 对比，并含 +K、+D 条件配置；
  - Tab. 4：不同输入配置（无条件、内参、稀疏深度、D+K）对比；
  - Tab. 5：输出表示消融（Ray+D vs XYZ）；
  - Tab. 6：点损失机制消融（P+GT Ray vs P vs D+Ray）；
  - Tab. 7：双向增强消融（P2A、A2P 及组合）；
  - Tab. 8：条件机制消融（去高斯平滑、去状态嵌入）。
- **定性对比**：图 4（全景/鱼眼/针孔三行对比）、图 5（全景与 DA²、UniK3D 对比）。
- **充分性评估**：
  - 覆盖三类相机、多种输入配置，消融维度较全面，且每个消融都对应明确的性能变化；
  - 对比方法均为近年 SOTA，且在统一评测流程下重新评估，**公平性较好**；
  - 但训练集规模庞大（29 个数据集），与部分基线训练数据不完全对齐，可能存在数据量优势；伪标签自训练引入的偏差也未做定量分析。

## 6. 主要结论与发现

- **统一框架可行**：OmniPoint 在针孔、鱼眼、全景三类相机上均达到 SOTA 或极具竞争力，验证了射线-距离表示的相机无关性。
- **非针孔场景优势显著**：
  - 鱼眼点云 Rel 从 UniK3D 的 11.5 降至 **6.66**；
  - 360° 深度 Rel 达 **5.79**，优于全景专用模型 DA²（6.65）。
- **透视场景不退化**：S.FoV 上 δ1 达 96.8，与针孔专用模型 MoGe V2 持平。
- **条件注入有效**：零样本度量深度 Mean δ1 达 83.5（SOTA）；加入内参升至 85.0；加入稀疏深度跃升至 **98.0**，具备高性能深度补全能力；D+K 联合进一步最优。
- **消融结论**：
  - Ray+D 表示优于直接 XYZ（三类相机一致）；
  - 解耦损失 P+GT Ray 优于朴素 P 与完全分离的 D+Ray；
  - P2A 与 A2P 各自独立有效，协同最优（8.45 → 5.79 Rel）；
  - 高斯平滑与状态嵌入均不可或缺。

## 7. 优点

- **表示创新**：显式解耦投影几何与场景结构，从根本上解决跨相机泛化的表示层障碍，比球谐参数化更稳定、更保细节。
- **损失设计精细**：用真实射线投影预测距离构造代理点，干净隔离距离误差，避免梯度交叉污染。
- **数据增强系统化**：P2A 与 A2P 在 3D 空间双向桥接，而非简单 2D 变换，有效缓解非针孔真值稀缺。
- **条件注入鲁棒**：状态嵌入 + 向量化高斯溅射，既解决架构歧义又避免不规则噪声梯度，使同一模型无缝切换零样本估计与深度补全。
- **评测严谨**：统一输入格式与度量流程重新评估所有基线，减少实现差异带来的不公平。
- **实验覆盖广**：三类相机、8+3 个基准、多组消融，验证充分。

## 8. 不足与局限

- **度量深度部分基准落后**：Tab. 3 中无条件下 NYUv2 仅 86.2、KITTI 88.0，明显低于 UniK3D（94.4/93.6）与 MoGe V2（96.1）；整体 Mean 优势主要来自 ETH3D、HAMMER 等基准，度量尺度估计的稳定性仍有提升空间。
- **算力门槛高**：72 张 A100 训练 15k 步，复现成本高；论文未报告推理速度、显存占用等部署指标。
- **训练数据规模庞大且不均衡**：29 个数据集混合训练，与基线数据量不完全对齐，SOTA 优势可能部分来自数据红利。
- **伪标签依赖风险**：A2P 自训练依赖透视模型的伪真值，若初始模型在特定域失败，误差会被固化放大；论文未给出伪标签质量的定量评估。
- **条件评估覆盖有限**：稀疏深度实验主要在部分基准上报告，未系统分析不同稀疏率、噪声水平下的鲁棒性。
- **失败案例与边界条件**：论文未讨论极端畸变、极近距离、动态场景或天空/透明物体等困难情形的表现。
- **第三阶段与增强流程细节不足**：掩码头训练时长、伪标签生成算力、数据增强的具体规模未量化。

（完）
