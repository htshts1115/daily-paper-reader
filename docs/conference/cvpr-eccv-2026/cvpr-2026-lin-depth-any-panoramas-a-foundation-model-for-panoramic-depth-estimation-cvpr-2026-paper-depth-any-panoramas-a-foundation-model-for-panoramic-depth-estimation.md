---
title: "Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation"
title_zh: Depth Any Panoramas：全景深度估计基础模型
authors: "Lin, Xin, Song, Meixi, Zhang, Dizhe, Lu, Wenxuan, Li, Haodong, Du, Bo, Yang, Ming-Hsuan, Nguyen, Truong, Qi, Lu"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Lin_Depth_Any_Panoramas_A_Foundation_Model_for_Panoramic_Depth_Estimation_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 具备强泛化能力的全景度量深度基础模型
tldr: 全景度量深度估计缺乏大规模数据，难以像透视图像那样训练泛化性强的深度基础模型。本文采用数据闭环范式，融合公开数据集、UE5合成数据、文生图数据与网络真实全景图，并用三阶段伪标签清洗缩小域差距，同时以DINOv3-Large为骨干引入范围掩码头与锐度优化。实验表明该模型能在多样场景距离下稳定泛化，成为全景度量深度基础模型。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 1440, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 3, \"index\": 15, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 512, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 720, \"height\": 360}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 720, \"height\": 360}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 604, \"height\": 304}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 512, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 5, \"index\": 22, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 6, \"index\": 23, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 6, \"index\": 24, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 6, \"index\": 25, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 6, \"index\": 26, \"width\": 1068, \"height\": 226}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 6, \"index\": 27, \"width\": 1068, \"height\": 226}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 6, \"index\": 28, \"width\": 1068, \"height\": 226}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 6, \"index\": 29, \"width\": 1068, \"height\": 226}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 6, \"index\": 30, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 6, \"index\": 31, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 6, \"index\": 32, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 6, \"index\": 33, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 6, \"index\": 34, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 6, \"index\": 35, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 6, \"index\": 36, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 6, \"index\": 37, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 6, \"index\": 38, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 6, \"index\": 39, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 6, \"index\": 40, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 6, \"index\": 41, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 6, \"index\": 42, \"width\": 1026, \"height\": 3950}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 6, \"index\": 43, \"width\": 899, \"height\": 3950}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 6, \"index\": 44, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 7, \"index\": 45, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 7, \"index\": 46, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 7, \"index\": 47, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 7, \"index\": 48, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 7, \"index\": 49, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 7, \"index\": 50, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 7, \"index\": 51, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 7, \"index\": 52, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 7, \"index\": 53, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-lin-depth-any-panoramas-a-foundation-model-for-panoramic-depth-estimation-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 7, \"index\": 54, \"width\": 1024, \"height\": 512}]"
motivation: 全景度量深度缺少大规模标注数据，跨室内外与合成真实域差距大，难以训练泛化性强的模型。
method: 构建多源全景数据集并设计三阶段伪标签清洗，以DINOv3-Large为骨干加入范围掩码头与锐度优化。
result: 在多样场景距离下实现稳定的度量深度泛化，优于既有全景深度方法。
conclusion: 提出全景度量深度基础模型，为全景场景的通用深度估计奠定数据与框架基础。
---

## Abstract
In this work, we present a panoramic metric depth foundation model that generalizes across diverse scene distances. We explore a data-in-the-loop paradigm from the view of both data construction and framework design. We collect a large-scale dataset by combining public datasets, high-quality synthetic data from our UE5 simulator and text-to-image models, and real panoramic images from the web. To reduce domain gaps between indoor/outdoor and synthetic/real data, we introduce a three-stage pseudo-label curation pipeline to generate reliable ground truth for unlabeled images. For the model, we adopt DINOv3-Large as the backbone for its strong pre-trained generalization, and introduce a plug-and-play range mask head, sharpness-centric optimization, and geometry-centric optimization to improve robustness to varying distances and enforce geometric consistency across views. Experiments on multiple benchmarks (e.g., Stanford2D3D, Matterport3D, and Deep360) demonstrate strong performance and zero-shot generalization, with particularly robust and stable metric predictions in diverse real-world scenes. The project page can be found at: https://insta360-research-team.github.io/DAP_website/

---

## 论文详细总结（自动生成）

# Depth Any Panoramas (DAP) 论文总结

## 1. 核心问题与研究背景

- **任务定位**：全景（360°×180°）单目**度量深度估计**，服务于空间智能与机器人应用（如全向避障导航）。
- **核心痛点**：
  - 全景深度估计明显落后于透视图像深度估计。
  - 已有的全景专用相对/尺度不变方法（PanDA、Depth Anywhere、DA²）与统一度量深度框架（DAC、Unik3D）**难以泛化到多样真实场景，尤其室外**。
  - 根因是**数据规模与多样性受限**：全景数据采集与标注成本极高，室内/室外、合成/真实之间存在显著域差距。
- **研究动机**：借鉴透视深度基础模型（Depth Anything 系列）的数据规模化经验，探索**数据闭环（data-in-the-loop）范式**——既要把数据规模做上去并保证真值可靠，又要让模型架构能有效消化这种规模。
- **整体含义**：提出 **DAP（Depth Any Panoramas）**，一个统一室内外、跨任意距离的**全景度量深度基础模型**，无需微调即可零样本泛化。

## 2. 方法论

### 2.1 数据引擎（Data Engine，约 2M 全景样本）

| 数据来源 | 类型 | 规模 |
|---|---|---|
| Structured3D | 合成室内，有标注 | 18,298 |
| DAP-2M-Labeled（AirSim360 / UE5） | 合成室外，有标注 | 90K（5 个场景：New York City、SF City、Downtown West、City Park、Rome，>26,600 条完整全景序列，无人机中低空轨迹） |
| 网络采集 | 真实无标注 | 1.7M（由 250K 全景视频抽帧、筛选地平线异常样本得到，Qwen2-VL 自动分类为约 250K 室内 + 1.45M 室外） |
| DiT360 生成 | 生成式室内 | 200K |
| **合计** | | **约 2M（约 500K 室内 + 1.5M 室外；300K 合成 + 1.7M 真实）** |

- 对比此前工作（PanDA 122k、DA² 606k、Unik3D 694k、DAC 800k），DAP 在**规模与域覆盖（室内/室外 × 合成/真实）上均为最大最全**。

### 2.2 三阶段伪标签清洗与训练流程

- **Stage 1 — Scene-Invariant Labeler**：在 20K 合成室内 + 90K 合成室外（几何与光照多样）上训练打标器，避免过拟合单一场景布局，获得跨域一致的物理深度先验；权重由 UniK3D 初始化。
- **Stage 2 — Realism-Invariant Labeler**：
  - 先预训练一个**深度质量判别器**（PatchGAN）：合成 GT 深度为"真"，Labeler 输出为"假"，学到场景无关的质量先验。
  - 用 Stage-1 Labeler 对全部 1.9M 无标注真实图像生成伪标签，按判别器打分挑选**室内/室外各 top 300K** 高置信样本。
  - 与 Stage-1 合成数据合并，训练 Realism-Invariant Labeler，使其对真实域外观变化鲁棒。
- **Stage 3 — DAP 训练**：在全部标注数据 + 1.9M 精炼伪标签上联合训练最终模型，实现大规模半监督学习。

### 2.3 模型设计

- **骨干**：DINOv3-Large（强预训练泛化能力）+ 畸变感知深度解码器。
- **双头结构**：
  - **度量深度头**输出稠密深度图 $D$；
  - **即插即用范围掩码头**输出二值掩码 $M$，提供 10 m / 20 m / 50 m / 100 m 四档距离阈值，损失为加权 BCE + Dice：
    $\mathcal{L}_{mask}=\|M-M_{gt}\|^2+0.5\,\mathcal{L}_{Dice}(M,M_{gt})$。
  - 最终深度为逐元素相乘 $M \odot D$，保证不同尺度下的物理有效性与度量一致性。

- **锐度导向优化（Sharpness-centric）**：
  - $\mathcal{L}_{DF}$（稠密保真）：将深度图按二十面体 12 个顶点处的虚拟相机分解为 12 个透视 patch，避开极点拉伸，对每个视图做有效掩码、归一化后计算预测与 GT 深度 Gram 矩阵之差的 Frobenius 范数并取平均。
  - $\mathcal{L}_{grad}$：在 ERP 域用 Sobel 求梯度幅值并阈值化得边缘掩码 $M_E$，仅在边缘区域施加 SILog 损失，补偿 $\mathcal{L}_{DF}$ 在 ERP 域的不足，锐化物体边界。

- **几何导向优化（Geometry-centric）**：
  - $\mathcal{L}_{normal}$：预测与 GT 表面法向场的 L1 距离；
  - $\mathcal{L}_{pts}$：将深度投影到球坐标得 3D 点云，计算逐点 L1 距离。

- **总目标**：以畸变图 $M_{distort}$ 对各项加权求和，补偿等距柱状投影中极区像素过表征问题：
  $\mathcal{L}_{total}=M_{distort}\odot(\lambda_1\mathcal{L}_{SILog}+\lambda_2\mathcal{L}_{DF}+\lambda_3\mathcal{L}_{grad}+\lambda_4\mathcal{L}_{normal}+\lambda_5\mathcal{L}_{pts}+\lambda_6\mathcal{L}_{mask})$。

## 3. 实验设计

- **评估基准（全部零样本）**：
  - 室内：**Stanford2D3D**、**Matterport3D**；
  - 室外：**Deep360**；
  - 自建新基准 **DAP-Test**：1,343 张带精确深度标注的高质量室外全景图（对本模型属 in-domain，用于验证数据规模化与训练策略有效性）。
- **评价指标**：AbsRel、RMSE、$\delta_1$。
- **对比方法**：
  - 尺度不变类（仅作参考，需用 GT 对齐尺度）：MoGe、VGGT、DepthAnythingV2、PanDA、DA²；
  - 度量类：Unik3D、DAC。
- **训练配置**：分辨率 512×1024；Adam 优化器；骨干 lr = 5e-6，解码器 lr = 5e-5；损失权重 $\lambda_{1..6}$ = 1.0 / 0.4 / 5.0 / 2.0 / 2.0 / 2.0；数据增强含颜色抖动、水平平移、翻转。

## 4. 资源与算力

- 论文仅说明"**所有实验在 H20 GPU 上进行**"。
- **未明确给出**：GPU 具体数量、训练总时长、训练步数/epoch、模型参数量与推理速度。
- 亦未报告总计算量（FLOPs）或碳排放等估算。因此算力开销**无法从论文正文准确复现**，属于信息披露不足。

## 5. 实验数量与充分性

- **定量实验组数（约 4 个主表）**：
  1. 表 3：3 个 benchmark × 3 指标，对比 8 种方法（含尺度不变方法作参考）；
  2. 表 4：DAP-Test 上对比 DAC、Unik3D 两种度量方法；
  3. 表 5：消融——畸变图 / 几何损失 / 锐度损失三项逐级叠加，2 个数据集；
  4. 表 6：范围掩码阈值消融（10/20/50/100 m 与"无掩码"共 5 种设置），2 个数据集。
- **定性实验**：图 4（真实室内外多样场景 vs DAC、Unik3D）、图 5（Stanford2D3D vs GT）。
- **充分性评价**：
  - **优点**：消融覆盖了畸变补偿、几何一致性、锐度、范围掩码四类关键设计，且逐项叠加验证，逻辑清晰；零样本设定下跨室内外三个公开基准 + 自建基准，覆盖面较广。
  - **不足**：
    - 消融仅在 DINOv3-Large 单一骨干下进行，**未做骨干替换或数据规模缩放（scaling law）实验**，无法直接印证"数据规模化"的边际收益。
    - 表 3 中 DA²、PanDA 等室外结果为"—"，**缺少同口径的室外对比**。
    - 尺度不变方法在评估时需借助 GT 获取尺度，与直接输出绝对度量的 DAP **并非完全对等**（论文已明确声明只作参考，态度客观）。
    - **未报告方差/多次运行结果**，也未给出失败案例分析。

## 6. 主要结论与发现

- **零样本度量深度全面领先**：
  - Stanford2D3D：AbsRel 0.0921、$\delta_1$ 0.9135（DAC 为 0.1366 / 0.8393）；
  - Matterport3D：AbsRel 0.1186、$\delta_1$ 0.8518（DAC 为 0.1803 / 0.7203）；
  - Deep360：AbsRel 0.0659、RMSE 5.224、$\delta_1$ 0.9525（DAC 为 0.2611 / 8.371 / 0.6311）。
- **DAP-Test 上大幅提升**：AbsRel 从 Unik3D 的 0.2517 降至 0.0781，RMSE 从 10.56 降至 6.804，$\delta_1$ 从 0.6086 升至 0.9370。
- **消融结论**：畸变图提升优化稳定性；几何损失（法向 + 点云）增强结构一致性；锐度损失（$\mathcal{L}_{DF}$ + $\mathcal{L}_{grad}$）进一步最优（AbsRel 0.1084/0.0862，$\delta_1$ 0.8576/0.8719）。
- **范围掩码结论**：小阈值（10/20 m）侧近距几何，100 m 档整体最优（AbsRel 0.0793/0.0862，$\delta_1$ 0.9353/0.8719）；**移除掩码显著掉点**，说明其能过滤不可靠远距预测、稳定训练。
- **定性结论**：DAP 在复杂布局、深度不连续处边界更锐利、全局几何更连贯，远景与天空区域不塌陷；单模型统一室内外度量深度，无需任何微调。

## 7. 优点

- **数据侧**：构建了目前规模最大（~2M）、域覆盖最广（室内/室外 × 合成/真实）的全景深度数据引擎，并明确给出与前作的数据构成对照表，可复现性强。
- **训练范式**：三阶段渐进式伪标签清洗（场景不变打标器 → 判别器筛选高质量伪标签 → 真实性不变打标器精炼 → 全量半监督训练）设计巧妙，**同时弥合合成–真实与室内–室外两类域差距**，且判别器用合成 GT 作"真"样本的思路简洁有效。
- **模型设计**：
  - 范围掩码头为**即插即用**模块，让单一模型自适应从室内近距到室外远距的多尺度场景，$M \odot D$ 保证输出物理有效；
  - 用二十面体 12 视图的 Gram 相似度避开 ERP 极点畸变，配合 ERP 域的梯度损失，**锐度与几何一致性互补**；
  - 畸变图加权损失显式处理极区像素过表征。
- **结果强度**：直接输出绝对度量尺度、无需任何后处理对齐，仍在三个公开基准上全面最优；视觉一致性与尺度感知在远景、天空等困难区域表现突出。
- **贡献互补**：数据、训练流程、模型与损失三方面协同，而非单点改进。

## 8. 不足与局限

- **算力信息缺失**：仅提及 H20 GPU，未给出数量、训练时长、参数量与推理效率，**可复现性与成本评估受限**。
- **自建基准的偏差风险**：DAP-Test 由作者构建且对 DAP 属 in-domain，虽有助于验证数据缩放效果，但**存在选择性偏差**，不能替代真正的跨域零样本评估。
- **对比公平性**：室外场景下

- **对比公平性**：室外场景下 DA²、PanDA 等全景专用方法的结果在表 3 中为"—"，缺少同口径对比；而尺度不变方法需要借助 GT 对齐尺度后才能比较，与 DAP 直接输出绝对度量的设定并不完全等价，因此"全面领先"的结论在跨类别比较上仍需谨慎解读。
- **消融维度单一**：消融实验只覆盖损失与掩码设计，未对骨干网络（如换成 ViT 系列其他规模、Swin、或更小的 DINOv3 变体）做替换测试，也未做数据规模的 scaling 曲线，因而无法回答"性能提升中数据引擎与模型设计各占多少"这一关键归因问题。
- **缺少鲁棒性与不确定性分析**：未报告多随机种子下的均值/方差，未做失败案例（如强反光、无纹理墙面、极近遮挡、动态物体）分析，也未提供深度不确定性估计或置信度校准，实际部署时的可靠性边界不清晰。
- **泛化边界未探明**：评估集以室内（Stanford2D3D、Matterport3D）与室外（Deep360、DAP-Test）静态场景为主，对鱼眼/多相机拼接、手持晃动、夜间、雨雾、水下等极端条件没有覆盖；网络采集的 1.7M 数据虽带来多样性，但也可能引入标注噪声与地理/风格偏置。
- **伪标签闭环的潜在风险**：三阶段流程依赖 Stage-1 Labeler 与判别器，若打标器在某一域（如超远距或极端室内）系统性偏差，伪标签筛选只能过滤"看起来不像 GT"的样本，难以纠正一致性错误，存在误差累积与自我强化的可能。
- **评测指标与协议细节**：仅用 AbsRel、RMSE、$\delta_1$，未报告对数域指标（如 $\log_{10}$ 误差）或边界精度指标；评测时的深度截断范围、天空/无效像素处理方式若在不同方法间不一致，会影响可比性。
- **开源与可复现性**：论文未明确说明数据引擎、DAP-2M-Labeled 合成数据、DAP-Test 基准与模型权重是否公开，这直接影响社区能否复现其数据规模化结论。

## 9. 可借鉴点与启示

- **"数据闭环"思路**：先用小规模、几何多样的合成数据训练出场景无关的打标器，再用判别器筛选高质量伪标签，最后在全量数据上训练——这一"先立标尺、再扩数据、后统一训练"的范式可迁移到其他缺乏真值的稠密预测任务（如全景法向、光流、语义）。
- **用合成 GT 当"真样本"训练质量判别器**：无需人工标注即可获得域无关的伪标签质量评分，是低成本提升伪标签可靠性的实用技巧。
- **畸变感知的损失设计**：以二十面体顶点虚拟相机分解代替直接在 ERP 域计算损失、并配合畸变图对像素加权，是处理球面等距柱状投影极区过表征的通用方案，可复用于全景分割、全景生成等任务。
- **即插即用的范围掩码头**：用少量阈值档位让单模型适配室内近距到室外远距的多尺度需求，且输出可保证物理有效，工程上易部署。
- **模型无关性**：数据引擎与训练流程与具体骨干解耦，理论上可替换任意强预训练视觉编码器，便于后续迭代。

## 10. 总体评价

DAP 是一篇**工程完整度高、数据贡献突出**的全景度量深度工作。其最大价值在于：首次把透视深度基础模型的"数据规模化 + 半监督伪标签"范式系统性地搬到全景域，构建了约 2M 规模、覆盖室内外与合成真实四象限的数据引擎，并通过三阶段清洗流程与畸变/几何/锐度三类损失设计，让单一模型在零样本条件下同时刷新室内与室外全景深度基准，且直接输出绝对度量尺度。方法层面的掩码头、二十面体 Gram 损失、畸变加权均为清晰可复用的设计。

主要短板在于**归因证据与披露透明度**：缺少骨干替换、数据规模缩放、多随机种子与失败案例分析，算力与训练细节报告不足，自建基准 DAP-Test 存在 in-domain 偏置，室外跨方法对比不完整。因此其"数据规模化带来增益"的核心论点虽方向可信，但尚未被严格的控制变量实验所证实。

总体而言，论文在**数据与系统层面贡献显著、结果领先幅度大**，适合作为全景深度方向的强基线；若后续补足归因消融、鲁棒性评估与开源发布，其影响力与可复现性将进一步提升。

（完）
