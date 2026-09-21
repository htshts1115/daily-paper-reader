---
title: "LumiDepth: Stable Monocular Depth in Multi-Illumination Scenes"
title_zh: LumiDepth：多光照场景下的稳定单目深度估计
authors: "Anqi Cheng, Zhiyuan Yang, Tianjiao Li, Haiyue Zhu, Kezhi Mao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9908.pdf"
tags: ["query:mono-depth"]
score: 7.0
evidence: 多光照下稳定的单目深度估计
tldr: 多光源、空间变化光照场景下，阴影、高光与曝光变化会破坏外观线索，导致深度基础模型严重不一致甚至失效。本文提出LumiDepth，基于多光照RGB图像，采用不一致性校准的概率伪监督进行学习，以缓解标注缺失与合成重光照的几何畸变。实验显著提升了多光照场景下的深度稳定性与一致性。该工作为复杂光照下的单目深度估计提供稳健框架，可支撑后续人像虚化等应用。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-001.webp\", \"caption\": \"\", \"page\": 7, \"index\": 1, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-002.webp\", \"caption\": \"\", \"page\": 7, \"index\": 2, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-003.webp\", \"caption\": \"\", \"page\": 7, \"index\": 3, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-010.webp\", \"caption\": \"\", \"page\": 9, \"index\": 10, \"width\": 635, \"height\": 310}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-011.webp\", \"caption\": \"\", \"page\": 9, \"index\": 11, \"width\": 504, \"height\": 284}]"
motivation: 多光源空间变化光照下，阴影高光与曝光变化破坏外观线索，使深度基础模型失效。
method: 提出LumiDepth，基于多光照RGB图像，采用不一致性校准的概率伪监督进行学习。
result: 实验显著提升了多光照场景下深度估计的稳定性与一致性。
conclusion: 为复杂光照下的单目深度估计提供稳健框架，可支撑虚化等下游应用。
---

## Abstract
Depth estimation in multi-illumination scenes with multi-ple, spatially varying light sources remains a crucial yet less-exploredproblem. Illumination changes introduce shadows, specular highlights,and exposure shifts that distort local appearance cues, causing severedepth inconsistency or even failure. Existing depth foundation models,trained predominantly on uniformly lit data, degrade sharply under suchconditions. However, direct adaptation is challenging because groundtruth depth is typically limited for multi-illumination datasets, whilesynthetic relighting often incurs geometric distortions. To address thesechallenges, we propose LumiDepth, a framework that learns from multi-illumination RGB images. First, a Disagreement-Calibrated ProbabilisticPseudo Supervision (DCPS) module constructs high-quality pseudo la-bels while preserving diversity. Second, a Frequency-aware Consistencyand Distillation (FaCD) module improves cross-illumination stabilitywithout over-smoothing by enforcing low-frequency geometric consis-tency and distilling high-frequency structural details bi-directionally. Toenable systematic evaluation, we introduce ReMID, a real-world multi-illumination RGB-D benchmark, together with stability metrics thatquantify average and worst-case depth variation. Experiments acrossdiverse datasets demonstrate that LumiDepth achieves state-of-the-artoverall performance, markedly improving both consistency and accuracyby reducing depth variation by 30.2% and absolute relative error by24.8%. We further show our target-domain label-free design remains ef-fective for depth under other appearance shifts such as weather and sen-⋆sor noise.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：单目深度估计（MDE）在均匀光照下已取得显著进展，但真实场景常存在多光源、空间变化光照。阴影、镜面高光、曝光变化会改变物体外观，使深度基础模型将光照伪影误判为几何线索，导致深度不一致、结构缺失甚至失败。
- **关键挑战**：
  - 多光照 RGB-D 数据稀缺，目标域通常缺少深度真值。
  - 合成重光照方法主要面向外观编辑，可能引入局部纹理伪影，破坏精细几何线索。
  - 现有鲁棒 MDE 方法多依赖干净参考图或合成退化，难以直接迁移到“无标准光照”的多光照场景。
  - 视频深度一致性方法假设相机运动或动态物体，不适用于静态场景、变化光照设定。
- **整体含义**：论文提出 **LumiDepth**，目标是在仅有同一静态场景、不同光照的 RGB 图像组条件下，实现光照不变且几何准确的单目深度估计。同时构建真实多光照 RGB-D 基准 **ReMID** 与稳定性指标，推动该问题系统化评估。

## 2. 方法论

### 2.1 核心思想

- 基于潜空间扩散式 MDE 框架，利用多光照 RGB 图像组 `G={x1,...,xN}` 进行目标域无标签适配。
- 不依赖目标域深度真值，也不使用合成重光照；通过模型自身深度假设构建伪监督，并施加跨光照一致性约束。
- 两个核心模块：
  - **DCPS**：Disagreement-Calibrated Probabilistic Pseudo Supervision，不一致性校准的概率伪监督。
  - **FaCD**：Frequency-aware Consistency and Distillation，频率感知一致性与蒸馏。

### 2.2 DCPS：不一致性校准的概率伪监督

- 对同一场景的 N 张不同光照图像，先用预训练深度模型得到 N 个深度假设 `{d1,...,dN}`。
- 对每个假设 `di`，计算其与其他假设的平均 L2 距离作为不一致性/不确定性：
  - 距离越大，说明该预测在跨光照下越不稳定，可靠性越低。
- 采用分布自适应阈值过滤：
  - 阈值取所有不确定性分数的中位数 `median({vi})`。
  - 保留 `vi ≤ τ` 的候选，保证至少保留约一半样本，避免脆弱的手工阈值。
- 将保留候选的 uncertainty 转为归一化置信度权重：
  - 使用温度缩放 softmax，不确定性越小，采样概率越高。
- 从候选集中按置信度概率采样一个深度作为伪标签，而非直接均值/中位数或单一“最佳”预测：
  - 均值/中位数会混入不可靠假设，导致结构模糊。
  - 单一最佳候选可能过拟合光照特定伪影。
  - 概率采样保留多样性，形成隐式集成，减少偏差累积。
- 伪监督损失：将伪标签编码到潜空间，与扩散模型预测做重建损失。

### 2.3 FaCD：频率感知一致性与蒸馏

- 直接跨光照一致性约束容易过度正则化，把光照变化误当几何差异，导致深度过平滑、边缘丢失。
- FaCD 将一致性分解为低频和高频两部分：
  - **低频一致性 `LLF`**：对解码后的深度图施加低通滤波，约束不同光照下全局形状一致。
  - **高频蒸馏 `LHF`**：基于深度梯度定义边缘幅值和边缘掩码，进行双向 stop-gradient 蒸馏。
- 高频蒸馏细节：
  - 使用深度梯度而非图像梯度，减少光照敏感性。
  - 更可靠的预测作为 teacher，提供更强监督信号。
  - 双向 stop-gradient 避免两个光照分支耦合坍塌，并缓解某一光照边缘损坏导致的错误强化。
- 与 latent 空间一致性或直接 depth 空间一致性相比，FaCD 在保持稳定性的同时保留边缘和薄结构。

### 2.4 总损失与实现

- 总损失：
  - `Ltotal = LGT + λ1 Lpseudo + λ2 LLF + λ3 LHF`
  - 实验设置：`λ1=0.5`，`λ2=0.5`，`λ3=0.1`。
- 训练同时使用：
  - 有深度真值的 RGB-D 对，提供标准扩散重建损失 `LGT`。
  - 无深度真值的多光照 RGB 组，提供 DCPS 伪监督和 FaCD 一致性。
- 实现细节：
  - 基于 Stable Diffusion v2 架构。
  - 多步和单步变体分别从 Marigold 和 Lotus 初始化。
  - 冻结 latent encoder、decoder 以及 U-Net 前两个下采样块。
  - 低通滤波使用高斯滤波，kernel size 11，σ=10。
  - 边缘掩码阈值 `τd=0.05`。

## 3. 实验设计

### 3.1 数据集与场景

- **训练数据**：
  - 有深度真值：Hypersim、Virtual KITTI。
  - 多光照 RGB-only：MIIW、LSMI、KITTI-C。
- **评估数据**：
  - **ReMID**：论文新建真实多光照 RGB-D 基准，100 个场景、1000 个样本，包含 sunlight、room light、torchlight 等光照变体，使用 RealSense 采集密集 RGB-D。
  - 夜间零样本：NuScenes-Night、RobotCar-Night。
  - 标准深度基准：NYUv2、KITTI、ETH3D、DIODE。
  - 其他退化：RoboDepth，18 种 corruption，包括噪声、模糊、天气等。
  - 补充材料中还报告 MIIW、LSMI 的 in-domain 结果。

### 3.2 评估指标

- 精度指标：`AbsRel ↓`、`δ1 ↑`。
- 多光照稳定性指标：
  - **MeanDV**：平均深度变化，衡量平均稳定性。
  - **MaxPIV**：最大单图变化，衡量最差光照条件下的稳定性。
  - 两者越低越好。
- 指标在深度对齐到真值后计算，用于量化外观变化但几何固定时的深度一致性。

### 3.3 对比方法

- 通用 MDE：Pixel-Perfect-Depth、DepthMaster、DAv2、DAv3、GenPercept、DistillAnyDepth、GeoWizard 等。
- 鲁棒 MDE：Robust-Depth、WeatherDepth、D4RD、DA-AC。
- 深度基础模型：Marigold、Lotus。
- 额外基线：Marigold/Lotus 的直接自训练变体 `(st)`，使用 14K RGB-only 多光照数据但不含 DCPS 和 FaCD，用于隔离模块贡献。
- 插件验证：将 DCPS、FaCD 接入 DAv2。

## 4. 资源与算力

- 文中明确提到：使用 **单张 NVIDIA RTX 4090 GPU** 训练。
- batch size 为 **16**，并使用梯度累积。
- 未明确说明：
  - 总训练时长、训练迭代次数、总 GPU 小时数。
  - 是否使用多卡或分布式训练。
  - 随机种子、重复实验次数、误差棒或统计显著性检验。
- 因此，算力信息只部分公开，训练成本与可复现性细节不足。

## 5. 实验数量与充分性

- **主实验数量较多**：
  - 表 1：ReMID、NuScenes-Night、RobotCar-Night 上零样本对比，涵盖通用、鲁棒、生成式 MDE 及自训练基线。
  - 表 3：NYUv2、KITTI、ETH3D、DIODE 标准深度基准。
  - 表 4：在 DAv2 上验证 DCPS/FaCD 插件效果。
  - 表 5：RoboDepth 18 种 corruption 平均结果。
  - 表 6：
