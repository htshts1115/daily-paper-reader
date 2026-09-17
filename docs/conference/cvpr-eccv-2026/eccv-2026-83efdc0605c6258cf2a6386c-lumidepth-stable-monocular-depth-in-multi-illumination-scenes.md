---
title: "LumiDepth: Stable Monocular Depth in Multi-Illumination Scenes"
title_zh: LumiDepth：多光照场景下的稳定单目深度估计
authors: "Anqi Cheng, Zhiyuan Yang, Tianjiao Li, Haiyue Zhu, Kezhi Mao"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9908.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 多光照场景下的单目深度估计并适配深度基础模型
tldr: 多光照场景下的阴影、高光与曝光变化会严重破坏单目深度估计，现有深度基础模型在均匀光照数据上训练，遇到此类场景性能急剧下降。本文提出LumiDepth框架，从多光照RGB图像出发，设计分歧校准的概率伪监督来稳定训练，缓解真值深度稀缺与合成重光照几何失真的问题。实验表明该方法显著提升了多光照下的深度一致性与精度。该工作为真实复杂光照中的单目深度估计提供了鲁棒方案。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-001.webp\", \"caption\": \"\", \"page\": 7, \"index\": 1, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-002.webp\", \"caption\": \"\", \"page\": 7, \"index\": 2, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-003.webp\", \"caption\": \"\", \"page\": 7, \"index\": 3, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 433, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-010.webp\", \"caption\": \"\", \"page\": 9, \"index\": 10, \"width\": 635, \"height\": 310}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-83efdc0605c6258cf2a6386c/fig-011.webp\", \"caption\": \"\", \"page\": 9, \"index\": 11, \"width\": 504, \"height\": 284}]"
motivation: 多光照场景中的阴影、高光与曝光变化会破坏现有深度基础模型的局部外观线索，导致深度不一致甚至失败。
method: 提出LumiDepth框架，利用多光照RGB图像，通过分歧校准的概率伪监督学习稳定的单目深度。
result: 在多个多光照数据集上显著提升深度一致性与精度，缓解基础模型在非均匀光照下的退化。
conclusion: 表明面向多光照的伪监督学习可有效增强单目深度估计的鲁棒性。
---

## Abstract
Depth estimation in multi-illumination scenes with multi-ple, spatially varying light sources remains a crucial yet less-exploredproblem. Illumination changes introduce shadows, specular highlights,and exposure shifts that distort local appearance cues, causing severedepth inconsistency or even failure. Existing depth foundation models,trained predominantly on uniformly lit data, degrade sharply under suchconditions. However, direct adaptation is challenging because groundtruth depth is typically limited for multi-illumination datasets, whilesynthetic relighting often incurs geometric distortions. To address thesechallenges, we propose LumiDepth, a framework that learns from multi-illumination RGB images. First, a Disagreement-Calibrated ProbabilisticPseudo Supervision (DCPS) module constructs high-quality pseudo la-bels while preserving diversity. Second, a Frequency-aware Consistencyand Distillation (FaCD) module improves cross-illumination stabilitywithout over-smoothing by enforcing low-frequency geometric consis-tency and distilling high-frequency structural details bi-directionally. Toenable systematic evaluation, we introduce ReMID, a real-world multi-illumination RGB-D benchmark, together with stability metrics thatquantify average and worst-case depth variation. Experiments acrossdiverse datasets demonstrate that LumiDepth achieves state-of-the-artoverall performance, markedly improving both consistency and accuracyby reducing depth variation by 30.2% and absolute relative error by24.8%. We further show our target-domain label-free design remains ef-fective for depth under other appearance shifts such as weather and sen-⋆sor noise.

---

## 论文详细总结（自动生成）

# LumiDepth：多光照场景下的稳定单目深度估计 —— 论文总结

## 1. 核心问题与研究动机

- **问题定位**：多光照场景（multi-illumination scenes）中存在多个空间变化的光源，会带来阴影、镜面高光、曝光漂移等现象，扭曲局部外观线索，使单目深度估计（MDE）出现严重的深度不一致甚至完全失效。
- **现实需求**：此类场景广泛出现在机器人导航/操作（混合人工照明的工作空间）、夜间自动驾驶（车灯与路灯交替）等精度与安全关键任务中。
- **现有方法瓶颈**：
  - 深度基础模型（如 Marigold、Lotus、Depth Anything 系列）主要在均匀光照数据上训练，遇到多光照条件性能急剧下降，常把光照伪影误当作几何线索，导致表面扭曲、细节丢失。
  - **直接适配困难**：多光照 RGB-D 数据集稀缺（变光照下采集稠密深度真值本身很难）；合成重光照（如 LumiNet 类方法）面向外观编辑，缺乏物理与"光照—几何"一致性，会引入局部纹理伪影，破坏细粒度几何线索。
  - 传统鲁棒 MDE 依赖雨/噪声等合成扰动或"干净参考图+退化模拟"，但光照变化同时改变全局色调与局部结构，数据增强不足以弥合差距。
- **整体含义**：论文提出**无需目标域深度真值、也无需合成重光照**的训练范式，仅从"同一静态场景、不同光照"的 RGB 图像组中学习光照不变且几何准确的深度，并配套构建真实基准与稳定性度量。

## 2. 方法论

### 2.1 问题形式化
- 基于潜在扩散式 MDE（Stable Diffusion v2 + Lotus 的 x0-prediction 参数化）：RGB 图像 x 编码为条件潜变量 c，深度 d 经 VAE 编码为 z(0)，U-Net f_θ 用重建损失训练：`L_GT = E‖z(0) − f_θ(z(t), c, t)‖²₂`。
- 训练来源分两类：(i) 常规 RGB-D 对（用 L_GT）；(ii) 同场景多光照 RGB 组 `G = {x1,...,xN}`。
- 目标：`f(xi) ≈ f(xj) ≈ d_gt`，其中 d_gt 仅在评测时可用。

### 2.2 DCPS：分歧校准的概率伪监督
- **不确定性度量**：用预训练模型（即待适配模型自身）对组内每张图生成 N 个深度假设，第 i 个假设与其余假设的均方偏差 `v_i = 1/(N−1) Σ_{j≠i} ‖d_i − d_j‖²₂` 作为"分歧型"不确定性——跨光照越稳定则分歧越小。
- **分布自适应过滤**：阈值取 `τ = median({v_i})`，保留 `v_i ≤ τ` 的候选（保证至少 N/2 个样本非空，且对场景相关的分歧尺度稳健），避免脆弱的手工阈值。
- **置信度加权概率采样**：对保留的 K 个候选，用温度缩放 softmax 将不确定性转成权重 `ρ_k = exp(−u_k/T) / Σ_j exp(−u_j/T)`，再按 `k* ~ Categorical(ρ)` 采样一个候选作为伪标签 `d_pseudo = d_{k*}`。
- **动机**：均值/中位数聚合会混入不可靠假设、模糊结构；选单一"最优"候选则脆弱、易过拟合光照特异伪影。随机、置信度加权监督等价于在训练迭代中做可靠假设的隐式集成，避免偏差累积与边缘模糊。
- 伪监督以潜空间重建损失实现：`L_pseudo = E‖z(0),pseudo − f_θ(z(t),pseudo, E(x), t)‖²₂`。

### 2.3 FaCD：频率感知的一致性与蒸馏
- 直接对潜变量或解码深度施加一致性约束会**过正则化**，把光照导致的外观差异误当几何不一致，最终"一致但模糊"。
- 策略是**解耦低频与高频**：
  - **低频一致性**：先解码得到 `d̂1 = D(ẑ1), d̂2 = D(ẑ2)`，用低通算子 LPF（高斯滤波，核 11，σ=10）对齐全局形状：`L_LF = ‖LPF(d̂1) − LPF(d̂2)‖₁`，不约束局部不连续。
  - **高频蒸馏**：在深度域（而非图像域，以降低光照敏感性）计算梯度幅值 `g_i = ‖∇d̂i‖` 与边缘掩码 `M_i = 1(g_i > τ_d)`（τ_d=0.05），做**双向 stop-gradient** 蒸馏：`L_HF = ρ₂‖∇d̂1 − sg[∇d̂2]‖_{1,M2} + ρ₁‖∇d̂2 − sg[∇d̂1]‖_{1,M1}`。更可靠的预测提供更强教师信号，缓解某一光照下边缘损坏造成的错误强化。
- **总目标**：`L_total = L_GT + λ₁L_pseudo + λ₂L_LF + λ₃L_HF`，实验中 λ₁=0.5、λ₂=0.5、λ₃=0.1。

### 2.4 评测贡献
- **ReMID 基准**：真实世界多光照 RGB-D 数据集，100 个场景、1000 个样本，每个场景在多种光照（阳光、室内灯、手电筒等）下用 RealSense 采集稠密 RGB-D。
- **稳定性指标**：定义逐光照偏差 `v_i`（对齐真值后相对均值深度 ¯d 的归一化偏差），进而给出 **MeanDV**（平均稳定性）与 **MaxPIV**（最差光照/极端情况稳定性），二者均越低越好，替代不适用的视频时序一致性指标。

## 3. 实验设计

- **训练数据**：
  - RGB-D（仅用 Hypersim 54K、Virtual KITTI 20K，未超出基线设置）；
  - RGB-only 多光照数据：MIIW（10K）、LSMI（1K）、KITTI-C（3K）。
- **评测数据/场景**：
  - 多光照：自建 **ReMID**（1000 样本，Tabletop/Indoor）；
  - 夜间零样本：NuScenes-Night（500）、RobotCar-Night（186）；
  - 通用深度基准：NYUv2（654）、KITTI（697）、ETH3D、DIODE；
  - 非光照退化：RoboDepth（18 种腐蚀类型平均）；
  - 另有 MIIW、LSMI 的域内结果放在补充材料。
- **对比方法**：
  - 通用 MDE：Pixel-Perfect-Depth、DepthMaster、DAv2、DAv3、GenPercept、DistillAnyDepth、GeoWizard；
  - 鲁棒 MDE：Robust-Depth、WeatherDepth、D4RD、DA-AC；
  - 生成式基线：Marigold、Lotus，并额外构造**直接自训练（st）**变体（用 14K RGB-only 多光照数据但去掉 DCPS/FaCD），以隔离"单纯扩数据"与"一致性设计"的贡献。
- **消融与扩展实验**：
  - DCPS 选择策略对比（Mean / Median / Best / DCPS）；
  - FaCD 变体（潜空间一致、深度空间一致、仅 L_LF、仅 L_HF、完整 FaCD）；
  - 逐损失项移除（−L_GT、−L_pseudo、−(L_LF+L_HF)）；
  - **骨干无关插件验证**：将 DCPS/FaCD 接入判别式方法 DAv2；
  - RoboDepth 18 种腐蚀上的泛化验证（雨雪、噪声、模糊等）。

## 4. 资源与算力

- **GPU**：单张 NVIDIA RTX 4090（通过梯度累积达到等效 batch size 16）。
- **基础架构**：Stable Diffusion v2；多步与单步变体分别由 Marigold、Lotus 检查点初始化；训练时冻结 latent encoder、decoder 以及 U-Net 前两个下采样块。
- **未明确说明**：论文正文未给出训练总时长、迭代步数、训练能耗、随机种子数量或多次运行的方差；补充材料可能包含更多细节（正文未展开）。

## 5. 实验数量与充分性

- **规模**：约 5 张量化主表（多光照/夜间对比、通用基准、骨干插件、RoboDepth、3 张消融表）+ 多组定性对比（ReMID 极端曝光、夜间驾驶、通用基准、RoboDepth 腐蚀、点云可视化），覆盖 4 类任务场景与近 20 个对比方法，实验体量较充分。
- **客观性/公平性上的可取之处**：
  - 强调"不使用任何额外的目标域深度监督"，与依赖大量标注的鲁棒 MDE 方法在同等信息条件下比较；
  - 专门设置 st 自训练基线，剥离"数据扩充"带来的增益，归因较清晰；
  - 在通用均匀光照基准上验证不退化，说明增益并非以牺牲通用性为代价。
- **需注意之处**：
  - 未见随机种子/多次重复的统计显著性报告；
  - ReMID 规模（1000 样本、100 场景、单一 RealSense 采集）相对有限；
  - 部分超参（λ、τ_d、滤波核、冻结层选择）的敏感性分析被推迟到补充材料；
  - 与最接近的工作 [35]（合成多光照数据集）未做直接基准对比，作者以"公开版本仅两场景、无官方协议与检查点"为由说明，属合理但仍是覆盖缺口。

## 6. 主要结论与发现

- 在多光照 ReMID 上相对 Lotus：**MeanDV 0.043 → 0.030（−30.2%）**，**AbsRel 0.113 → 0.085（−24.8%）**，**δ1 0.850 → 0.914（+7.5%）**；平均排名从 6.7 提升到 2.0（改善 70.1%）。
- 夜间零样本（NuScenes-Night / RobotCar-Night）与通用基准（NYUv2/KITTI/ETH3D/DIODE）上同时保持或提升性能，δ1 与 AbsRel 大多为最优或次优。
- 消融显示：DCPS 的概率采样优于均值/中位数/最优单选；频率无关的一致性（潜空间或深度空间）虽提升稳定性却严重损害几何精度，验证 FaCD 解耦的必要性；移除 L_GT 会放大伪标签偏差，移除 L_pseudo 或频率项则同时损失精度与稳定性。
- 该"分组观测 + 无标签目标域"范式可迁移到天气、传感器噪声等其它外观变化场景（RoboDepth 上 MeanDV 0.051→0.038，AbsRel 0.135→0.115）。
- 模块是**骨干无关**的：接入 DAv2 后 MeanDV 0.051→0.036、AbsRel 0.119→0.102。

## 7. 优点

- **问题切入准确**：指出"光照变化同时改变全局色调与局部结构"，从数据合成/增强路线转向"利用同一场景多光照观测的一致性"，避开了重光照的几何失真风险。
- **无需目标域深度真值**：完全 label-free 的目标域适配，工程上可落地性强。
- **DCPS 设计精巧**：分歧型不确定性 + 中位数自适应阈值（保证非空候选集）+ 温度 softmax 概率采样，兼顾可靠性与监督多样性，避免均值模糊与单选脆弱两个极端。
- **FaCD 频率解耦**：低频对齐形状、高频双向 stop-gradient 蒸馏保边缘，并用可靠性权重（ρ）抑制错误强化，直击"一致但模糊"的通病。
- **评测贡献扎实**：ReMID 真实多光照 RGB-D 基准 + MeanDV/MaxPIV 平均与最差情形稳定性指标，填补了现有视频时序一致性指标不适用于静态多光照场景的空白。
- **验证维度广**：通用基准不退化、跨任务（夜间驾驶、腐蚀鲁棒）、跨骨干（DAv2 插件）三重验证，结论稳健性较好。

## 8. 不足与局限

- **训练数据前提较强**：方法假设训练时可获得"同一静态场景、不同光照"的成组 RGB 观测；在只有单张图或场景/相机发生运动的实际场景中难以直接应用。
- **依赖预训练假设质量**：DCPS 的伪标签来自模型自身假设，若所有光照条件下的预测一致地错误，分歧度量会失效并固化偏差；论文未给出这种失效模式的系统分析。
- **静态场景假设**：未讨论相机运动、动态物体或曝光/白平衡变化与几何变化耦合的情形，与视频深度一致性问题的边界虽已澄清，但也限制了适用面。
- **基准规模与代表性**：ReMID
