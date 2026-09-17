---
title: "$\\alpha$Matte4K & $\\mu$Matting: Dataset and Model for Ultra-Micro Precision Alpha Video Matting"
title_zh: αMatte4K 与 μMatting：面向超微精度 Alpha 视频抠图的数据集与模型
authors: "Chen, Xinyi, Dong, Hang, Jiang, Baowei, Xu, Shenkun, Guan, Youqi, Shi, Kanle, Gai, Kun, Song, Haichuan"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_alphaMatte4K__muMatting_Dataset_and_Model_for_Ultra-Micro_Precision_Alpha_CVPR_2026_paper.pdf"
tags: ["query:matting"]
score: 9.0
evidence: 高分辨率人体视频抠图与时序一致性
tldr: 高分辨率人体视频抠图需在半透明区域预测精确 alpha 并保持时序一致，但现有方法在主体稳定性、时序建模与计算成本上难以兼顾质量与效率。本文提出分辨率无关的两阶段框架 μMatting：先用人物感知掩码自编码器定位粗抠图，再用稀疏三维卷积精修关键区域，并引入时序调制器注入全局时空线索。实验在 αMatte4K 数据集上取得更优的质量—效率平衡。该工作推动了高精度实时视频抠图与发丝级细节处理。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 3328, \"height\": 2733}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 3899, \"height\": 2915}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 3, \"index\": 3, \"width\": 1417, \"height\": 965}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 4343, \"height\": 2279}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 5, \"index\": 5, \"width\": 2737, \"height\": 1076}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 4256, \"height\": 1862}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 6963, \"height\": 4040}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 8, \"index\": 8, \"width\": 908, \"height\": 714}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-alphamatte4k-mumatting-dataset-and-model-for-ultra-micro-precision-alpha-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 8, \"index\": 9, \"width\": 2643, \"height\": 1023}]"
motivation: 高分辨率人体视频抠图在主体稳定性、时序一致性与计算成本上难以兼顾质量与效率。
method: 提出分辨率无关的两阶段框架：人物感知掩码自编码器粗定位，稀疏三维卷积精修，并加时序调制器注入时空线索。
result: 在自建的 αMatte4K 数据集上取得更优的质量与效率平衡，半透明区域与时序稳定性均有提升。
conclusion: 为高分辨率实时视频抠图与发丝级细节处理提供了数据集与模型范式。
---

## Abstract
High-resolution human video matting aims to predict accurate alpha mattes for semi-transparent regions while ensuring temporal consistency across frames. Despite notable progress, current methods still fail to achieve a satisfactory trade-off between quality and efficiency, with limitations in subject stability, temporal modeling, and computational cost. In this paper, we introduce \muMatting, an innovative resolution-agnostic two-stage framework for video matting: (1) coarse matte localization using a portrait-aware masked autoencoder; (2) refinement of critical regions via sparse 3D convolution, augmented by a temporal modulator that injects global spatio-temporal cues for enhanced consistency and contextual awareness. From data perspective, existing research remains limited by the insufficient quality of datasets, including (1) inaccurate alpha fractional values resulting from imperfect annotation, and (2) visual inconsistencies arising from arbitrary foreground-background compositions that lack natural coherence. To address this, we introduce \alphaMatte4K, a large-scale 4K-resolution human video matting dataset, which achieves accurate annotations and physical consistency through physically based rendering (PBR). Extensive experiments show that \muMatting surpasses state-of-the-art methods in accuracy and spatio-temporal consistency, while \alphaMatte4K boosts baseline performance, driving applications in real-world scenarios. The project is open-sourced at https://github.com/kadatec/mu-Matting.

---

## 论文详细总结（自动生成）

# αMatte4K & μMatting 论文总结

## 1. 核心问题与整体含义

- **研究背景**：4K 分辨率人体视频内容在虚拟会议、短视频、直播和 AIGC 中快速普及，视频抠图需要同时满足三点：空间细节准确、时序一致无闪烁、可扩展到 4K+ 且不明显退化。
- **现有瓶颈**：
  - 时序建模方法分为逐帧方法（如 RVM、AdaM）和块级方法（如 VMFormer）。前者时序建模有限，后者在高分辨率下多帧自注意力计算和显存开销极大。
  - 为降低计算量，许多方法采用“降采样—上采样”，导致半透明区域、发丝和边缘 alpha 模糊。
  - SparseMat 等稀疏推理方法虽高效，但偏图像抠图，依赖简单帧差，缺少时序连续性。
  - 部分方法依赖 SAM2 等外部初始掩码，增加系统复杂度和运行开销，且外部误差会传播到抠图结果。
- **数据层面问题**：现有数据集如 VideoMatte240K、HHM50K 多通过人工标注、抠图算法或色键构建，存在 alpha 不精确、噪声大；部分数据集只提供前景和 alpha，需与外部背景拼接，造成前景—背景光照、几何和运动不一致。
- **整体含义**：论文同时从数据和模型两端入手，提出 4K 人体视频抠图数据集 **αMatte4K** 与分辨率无关两阶段框架 **μMatting**，目标是在高分辨率下实现更精确的 alpha、更好的时序一致性和可接受的计算效率。

## 2. 方法论

### 2.1 核心观察与总体思想

- 作者分析 2 秒视频片段发现：仅有约 **13.7%** 像素的 alpha 随时间显著变化，且主要集中在边界和细节区域，大部分前景基本静态。
- 因此 μMatting 采用两阶段设计：
  1. **粗抠图定位**：先获得稳定的主体粗 alpha。
  2. **关键区域精修**：只对变化大、半透明、边缘等关键区域做稀疏时空精修。

### 2.2 数据集 αMatte4K 构建

- 采用 **PBR（基于物理的渲染）** 四阶段流水线：
  1. 从 MetaHuman 选取 30 个高质量数字人模型，使用 Mixamo 骨骼动作驱动，覆盖行走、跳舞、交互等。
  2. 在 Unreal Engine 中构建 22 个大型城市和自然 3D 场景，采样 900 个位置放置人物。
  3. 设计多样相机轨迹，约每 130 帧改变视角和动作，增加时序变化。
  4. 以 9:16 竖屏人像配置渲染，匹配短视频和直播常见格式。
- 数据集规模：**900 个视频、超过 115K 帧、4K 分辨率（2160×3840）**，提供像素级精确 alpha，尤其保留发丝、睫毛、运动模糊等难标注区域。
- 多样性覆盖：角色资产、运动类型、环境光照、相机设置；包含室内外、自然光/人工光、静态/推拉摇移等。

### 2.3 模型 μMatting

- 输入视频片段 \(I \in \mathbb{R}^{T \times H \times W \times 3}\)，实验中 \(T=4\)，先下采样到 512×512 以降低计算量。

#### 第一阶段：Coarse Alpha Predictor, CAP

- 使用 **Sapiens-0.3B**，一个在 3 亿以上人体图像上预训练的掩码自编码器，引入强人体先验。
- 编码器产生 patch token 和全局 [CLS] token，解码得到粗 alpha \(A_c^\downarrow\)。
- 对粗 alpha 中 \(\alpha \in (0,1)\) 的非二值区域做形态学腐蚀和膨胀，得到关键区域掩码 \(K^\downarrow\)，再与粗 alpha 一起上采样回原分辨率。
- 第一阶段损失：像素级 L1 损失 + 5 层 Laplacian 金字塔损失，兼顾像素精度和多尺度结构一致性。

#### 第二阶段：Fractional Alpha Refiner, FAR

- 将原始视频 \(I\) 与上采样粗 alpha \(A_c\) 拼接为 4 通道输入 \(I'\)。
- 根据关键区域 \(K\) 提取需要优化的像素，形成稀疏表示 \(S_{in} \in \mathbb{R}^{N_k \times 4}\)。
- 通过 **3D 稀疏卷积编码器—解码器** 聚合邻帧时空特征，输出稀疏精修 alpha \(S_{out}\)，再映射回全分辨率得到 \(A_d\)。只有关键区域像素被更新。
- 引入 **Temporal Sparse Context Modulator, TSCM**：用 CAP 编码器的 [CLS] token，经投影到 256 维、GRU 建模跨帧依赖、全连接和 sigmoid，再与稀疏编码特征逐元素相乘，注入全局时空上下文。TSCM 仅增加约 **0.79M** 参数，占总参数约 **0.21%**。
- 第二阶段损失：
  - **区域损失**：在关键区域 \(K\) 内计算 L1 和 Laplacian 损失。
  - **时序一致性损失**：在相邻帧关键区域交集 \(K_\cap\) 上，约束预测 alpha 差与真实 alpha 差一致。
  - **全局监督损失**：对最终融合 alpha 计算 L1。
  - 总损失为 \(L_{stage2} = 1 \cdot L_{region} + 0.5 \cdot L_{entire} + 0.5 \cdot L_{temporal}\)。
- 最终融合：\(A = K \times A_d + (1-K) \times A_c\)，非关键区域保留稳定粗预测，关键区域使用精修结果。

## 3. 实验设计

- **训练数据**：
  - HHM50K：主要增强 CAP 的前景定位能力。
  - VideoMatte240K 的 HD 划分（VM-HD）与 DVM 背景合成。
  - 本文提出的 αMatte4K。
- **评估 benchmark**：
  - **CRGNN**：真实世界视频，评估泛化性和鲁棒性。
  - **VM 1920×1080**：RVM 经典拼接测试集。
  - **VM-4K**：作者新构建，50 个视频、每视频 100 帧、3840×2160，用于高分辨率评测。
- **评价指标**：MAD、MSE、Grad、dtSSD；MAD/MSE 缩放 \(10^3\)，Grad 缩放 \(10^{-3}\)，dtSSD 缩放 \(10^2\)。
- **对比方法**：MODNet、R
