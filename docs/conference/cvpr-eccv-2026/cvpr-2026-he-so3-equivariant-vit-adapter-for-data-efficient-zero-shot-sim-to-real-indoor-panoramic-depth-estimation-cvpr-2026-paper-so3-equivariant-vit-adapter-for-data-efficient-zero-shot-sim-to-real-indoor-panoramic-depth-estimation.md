---
title: SO(3)-Equivariant ViT-Adapter for Data-Efficient Zero-Shot Sim-to-Real Indoor Panoramic Depth Estimation
title_zh: 面向数据高效零样本仿真到真实室内全景深度估计的SO(3)等变ViT适配器
authors: "He, Ziyan, Zhang, Qiudan, Ma, Lin, Wang, Xu"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/He_SO3-Equivariant_ViT-Adapter_for_Data-Efficient_Zero-Shot_Sim-to-Real_Indoor_Panoramic_Depth_Estimation_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 利用Depth Anything进行全景零样本深度估计
tldr: 全景深度估计在真实场景中泛化困难，Depth Anything等零样本模型因投影畸变与缺乏球面几何感知而性能骤降，且大规模全景RGB-D数据采集成本高昂。本文提出SO(3)等变ViT-Adapter，将透视图像预训练ViT的零样本能力迁移到全景深度估计，并显式建模球面几何。实验表明该方法在数据高效条件下显著提升仿真到真实的室内全景深度精度，为全景深度基础模型提供新思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-he-so3-equivariant-vit-adapter-for-data-efficient-zero-shot-sim-to-real-indoor-panoramic-depth-estimation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1372, \"height\": 750}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-he-so3-equivariant-vit-adapter-for-data-efficient-zero-shot-sim-to-real-indoor-panoramic-depth-estimation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 3860, \"height\": 1907}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-he-so3-equivariant-vit-adapter-for-data-efficient-zero-shot-sim-to-real-indoor-panoramic-depth-estimation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 3000, \"height\": 1233}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-he-so3-equivariant-vit-adapter-for-data-efficient-zero-shot-sim-to-real-indoor-panoramic-depth-estimation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 8, \"index\": 4, \"width\": 900, \"height\": 600}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-he-so3-equivariant-vit-adapter-for-data-efficient-zero-shot-sim-to-real-indoor-panoramic-depth-estimation-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 8, \"index\": 5, \"width\": 2158, \"height\": 879}]"
motivation: 全景深度估计在真实场景泛化差，Depth Anything在投影畸变下性能骤降，且全景RGB-D数据采集昂贵。
method: 提出SO(3)等变ViT-Adapter，把透视预训练ViT的零样本深度能力迁移到全景，并显式注入球面几何先验。
result: 在室内全景仿真到真实设定下以较少数据取得优于基线的零样本深度估计精度。
conclusion: 验证了等变适配器可高效复用透视深度基础模型，推动全景深度估计的实用化。
---

## Abstract
Panoramic depth estimation enables a complete 360^\circ understanding of 3D environments but faces significant challenges in generalizing to real-world scenes. While recent zero-shot depth models like Depth Anything achieve remarkable generalization on perspective images, their performance sharply degrades on panoramas due to projection distortions and the lack of spherical geometric awareness. Moreover, collecting large-scale panoramic RGB-D data is costly, hindering the large-scale training of panoramic foundation models. To address these issues, we propose an SO(3)-Equivariant ViT-Adapter, which transfers the powerful zero-shot capability of the perspective pre-trained ViT to panoramic depth estimation by explicitly incorporating a rotation-equivariant inductive bias. Our adapter introduces an SO(3) deformable cross-attention mechanism to effectively align SO(3)-equivariant features with perspective features, enhancing rotational consistency without modifying the ViT backbone. Trained solely on synthetic panoramas, our framework achieves robust zero-shot sim-to-real performance on real indoor benchmarks, including Matterport3D and Stanford2D3D, demonstrating both data efficiency and strong generalization for panoramic depth estimation.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：全景深度估计可提供 360° 的 3D 环境理解，对机器人、AR/VR、自主导航等很重要。但真实全景 RGB-D 数据采集成本高、标定复杂，导致大规模全景深度基础模型训练困难。
- **核心问题**：Depth Anything、Marigold 等透视图像零样本深度模型泛化能力强，但直接用于全景图时会因等距柱状投影畸变、缺乏球面几何感知而性能显著下降。
- **整体含义**：本文试图在**不修改、不微调透视预训练 ViT 主干**的前提下，通过适配器显式注入 SO(3) 旋转等变先验，把透视域预训练 ViT 的零样本深度能力迁移到全景深度估计，实现仅用合成全景数据训练、零样本仿真到真实（sim-to-real）的室内全景深度估计。

## 2. 方法论：核心思想与关键技术

- **核心思想**：在冻结的透视预训练 ViT 上增加可训练的 SO(3)-Equivariant ViT-Adapter，将球面/旋转群上的等变几何特征注入 ViT，使 ViT 在 ERP 全景图上的非等变特征获得旋转一致性。
- **整体架构**：
  - 输入包括 ERP 全景图 \(X_{ERP}\) 和 Driscoll-Healy 球面采样信号 \(X_{DH}\)。
  - ERP 图分块送入冻结 ViT，得到初始 ViT 特征 \(F^0_{vit}\)。
  - ESPM 从 \(X_{DH}\) 提取多尺度 SO(3)-等变特征 \(F^0_{esp}=\{F_1,F_2,F_3\}\)，并在第一个 adapter block 注入 ViT。
  - Transformer encoder 分为 \(N=4\) 个 block，每个 block 前后加入 SO(3) Feature Injector 和 Multi-Scale Feature Extractor，实现 \(S^2\)-SO(3) 双向特征交互。
  - 解码阶段，各 block 的 ViT 特征上采样为多分辨率，与投影到球面的 SO(3) 特征按尺度拼接，经 1×1 卷积调整通道后送入 DPT head，输出全景深度图。
- **Equivariant Spherical Prior Module, ESPM**：
  - 基于球面 CNN，使用 \(S^2\)Conv 将球面函数 \(f:S^2\to\mathbb{R}^{c_{in}}\) 提升为 SO(3) 上的函数 \(h:SO(3)\to\mathbb{R}^{c_{out}}\)。
  - 再用 \(SO(3)\)Conv 在旋转群上聚合旋转等变特征。
  - 实现上利用球谐变换和 Wigner-D 矩阵在谱域高效计算，并通过丢弃高频分量实现下采样。
  - 输出多尺度 SO(3) 等变特征，作为 ViT 的几何先验。
- **SO(3) Deformable Cross-Attention Module, SO(3)-DCAM**：
  - 将 2D 可变形注意力推广到球面和 SO(3) 群，解决球面非均匀采样导致的注意力权重失真。
  - **SO(3) Sparse Sampling**：以 ViT 特征为 query，在 SO(3) 上采样 key-value 特征；通过随机偏移旋转与 transport rotation 复合得到采样旋转，再转为 ZYZ 欧拉角从 \(F_{esp}\) 中取特征。
  - 初始化时用北极为中心的 SO(3) 网格偏置，并对不同尺度设置不同 \(\Delta\beta\) 范围，形成软局部约束。
  - **Spherical Contextual Relative Positional Encoding, SCRPE**：计算 query 与 key-value 之间的 SO(3) 旋转，经 log map 映射到李代数向量，再用可学习嵌入编码方向和幅值，生成球面相对位置编码。
  - 注意力形式
