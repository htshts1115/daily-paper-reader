---
title: "ICDepth: Taming Video Diffusion Models for Video Depth Estimation via In-Context Conditioning"
title_zh: ICDepth：通过上下文条件化驾驭视频扩散模型的视频深度估计
authors: "Xuanhua He, JIAXIN XIE, Mingzhe Zheng, Qifeng Chen"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/4043.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于扩散Transformer的单目视频深度估计
tldr: 单目视频深度估计需同时满足时间一致性、几何精度与跨场景泛化，但现有方法难以兼顾：判别式模型逐帧精确却受限于上下文导致时间漂移，生成式模型一致性与泛化更好但需海量数据且缺乏几何精度。本文提出ICDepth，通过上下文条件化将预训练文生视频扩散Transformer适配到视频深度估计，利用其丰富时空先验。实验表明该方法在时间一致性、几何精度与泛化间取得更好平衡。该工作拓展了扩散先验在视频深度任务中的应用。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-013.webp\", \"caption\": \"\", \"page\": 2, \"index\": 13, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-014.webp\", \"caption\": \"\", \"page\": 2, \"index\": 14, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-015.webp\", \"caption\": \"\", \"page\": 2, \"index\": 15, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-016.webp\", \"caption\": \"\", \"page\": 2, \"index\": 16, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-017.webp\", \"caption\": \"\", \"page\": 2, \"index\": 17, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-018.webp\", \"caption\": \"\", \"page\": 2, \"index\": 18, \"width\": 1080, \"height\": 2048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-019.webp\", \"caption\": \"\", \"page\": 2, \"index\": 19, \"width\": 1080, \"height\": 2048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-020.webp\", \"caption\": \"\", \"page\": 2, \"index\": 20, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-021.webp\", \"caption\": \"\", \"page\": 2, \"index\": 21, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-022.webp\", \"caption\": \"\", \"page\": 2, \"index\": 22, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-023.webp\", \"caption\": \"\", \"page\": 2, \"index\": 23, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-024.webp\", \"caption\": \"\", \"page\": 2, \"index\": 24, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-025.webp\", \"caption\": \"\", \"page\": 2, \"index\": 25, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-026.webp\", \"caption\": \"\", \"page\": 2, \"index\": 26, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-027.webp\", \"caption\": \"\", \"page\": 2, \"index\": 27, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-028.webp\", \"caption\": \"\", \"page\": 2, \"index\": 28, \"width\": 672, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-029.webp\", \"caption\": \"\", \"page\": 5, \"index\": 29, \"width\": 2600, \"height\": 1614}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-030.webp\", \"caption\": \"\", \"page\": 12, \"index\": 30, \"width\": 3648, \"height\": 2240}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-031.webp\", \"caption\": \"\", \"page\": 12, \"index\": 31, \"width\": 1224, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-032.webp\", \"caption\": \"\", \"page\": 12, \"index\": 32, \"width\": 1224, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-033.webp\", \"caption\": \"\", \"page\": 12, \"index\": 33, \"width\": 3648, \"height\": 2240}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-034.webp\", \"caption\": \"\", \"page\": 12, \"index\": 34, \"width\": 1224, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-035.webp\", \"caption\": \"\", \"page\": 12, \"index\": 35, \"width\": 1224, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-036.webp\", \"caption\": \"\", \"page\": 12, \"index\": 36, \"width\": 1224, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d689ddbaf272a4bbaa4fd9c0/fig-037.webp\", \"caption\": \"\", \"page\": 13, \"index\": 37, \"width\": 2982, \"height\": 1099}]"
motivation: 现有方法难以同时兼顾视频深度估计的时间一致性、几何精度与跨场景泛化。
method: 提出ICDepth，通过上下文条件化将预训练文生视频扩散Transformer适配到视频深度估计。
result: 利用视频扩散的时空先验，在一致性、几何精度与泛化之间取得更好平衡。
conclusion: 拓展了扩散先验在单目视频深度估计中的应用。
---

## Abstract
Monocular video depth estimation requires temporal con-sistency, geometric accuracy, and generalization across diverse scenar-ios—yet existing methods struggle to achieve all three simultaneously.Discriminative models excel at per-frame accuracy but suffer from tem-poral drift due to limited context windows, while generative methodsimprove consistency and generalization at the cost of extensive train-ing data (10M+ samples) and lack of geometric precision. In responseto these issues, we introduce ICDepth, a framework that adapts pre-trained text-to-video diffusion transformers for video depth estimationvia In-Context Conditioning (ICC), leveraging their rich spatial-temporalpriors. To address key challenges in transferring ICC from generationto dense prediction, we propose: (1) SAND-Attention, which ensuresprecise spatial-temporal alignment via shared RoPE and enforces uni-directional attention to prevent noise contamination; (2) SRFM, whichinjects DINOv2 semantic and resolution priors to enhance geometric pre-cision. ICDepth achieves state-of-the-art results on multiple benchmarkswith remarkable data efficiency, trained on only 0.8M frames (6–13×less than competing generative methods), while demonstrating strongzero-shot generalization to diverse domains.

---

## 论文详细总结（自动生成）

# ICDepth 论文深度总结

## 一、核心问题与研究动机

- **任务背景**：单目视频深度估计是 3D 视觉的基础任务，广泛应用于 AR/VR、自动驾驶与三维重建。它要求模型同时满足三个核心需求：
  - **时间一致性**：深度图跨帧稳定、无闪烁；
  - **几何精度**：能利用相邻帧时序信息提升当前帧的准确性与鲁棒性；
  - **泛化能力**：适应多样场景，尤其是长视频与复杂运动。

- **现有方法的两难困境**：
  - **判别式模型**（如 Video Depth Anything）：逐帧精度高，但依赖狭窄的局部时间窗口，难以建模长程依赖，导致长视频中的**一致性漂移**；且结果过于平滑、缺乏细节，泛化受限。
  - **生成式模型**（如 DepthCrafter、Depth Any Video）：基于 Stable Video Diffusion 等预训练视频扩散模型，一致性与泛化更好，但基础 SVD 是 U-Net 架构、先验较弱，且采用因式分解的时空建模（3D 卷积 + 1D 时间注意力），需要侵入式改动与**超 10M 样本**的大规模训练，几何精度仍不足。

- **核心追问**：能否用有限数据训练一个同时满足三项要求的模型？
  - 论文的答案是：利用**原生 3D 注意力的文生视频扩散 Transformer（VDiT，如 Wan 2.1）**，其时空先验更丰富，通过**上下文条件化（In-Context Conditioning, ICC）**将其迁移到深度估计任务。

---

## 二、方法论

### 1. 核心思想

- 摒弃传统的**通道维度拼接**（需修改输入投影层、跨模态交互弱），改用 **ICC**：将 RGB 条件与深度隐变量视为统一 token 序列
  - $s_t = [z_t;\, c] \in \mathbb{R}^{2n \times c}$
  - 由 VDiT 原生注意力直接建模两者关系，**非侵入式**且交互丰富。

### 2. 两大挑战与对应设计

#### 挑战一：噪声污染与时空错位 → **SAND-Attention**

传统 ICC 全注意力存在三个问题：(1) RoPE 在深度-RGB 对齐 token 间制造了虚假的顺序关系；(2) 双向注意力让带噪的 $z$ 污染干净的 $c$；(3) 统一的时间步嵌入 $e_t$ 给稳定的 RGB 特征注入不必要方差。

SAND-Attention（时空对齐、噪声解耦注意力）的做法：

- **分离 Q/K/V**：将序列的 Q、K、V 分别拆为深度部分与条件部分；
- **共享 RoPE 对齐**：对深度与条件 token 使用**相同的位置索引 $P$** 施加 RoPE，确保对应的 $(x, y, t)$ 坐标拥有相同的时空位置编码；
- **噪声解耦注意力**：
  - 干净条件 token 内部做自注意力：$O_c = \text{softmax}(Q'_c K'^T_c) V_c$
  - 带噪深度 token **单向**查询干净条件（同时保留自身）：$O_z = \text{softmax}(Q'_z [K'_z; K'_c]^T)[V_z; V_c]$
  - 反向注意力被系统性阻断，保证信息单向流动；
- **时间步嵌入置零**：对条件 token 的 $e_t$ 置零，使干净条件信号免受扩散噪声干扰；
- 保持与 Flash Attention 的兼容性。

#### 挑战二：几何模糊与分辨率失配 → **SRFM**

T2V 模型的表征并非为感知任务优化，且深度图与分辨率/宽高比强相关，固定分辨率推理会掉点。SRFM（语义-分辨率感知特征调制块）：

- **语义先验**：提取 DINOv2 特征 $f_d$，池化重塑为语义嵌入 $e_d$；
- **分辨率先验**：将空间尺寸 $(h, w)$ 经正弦位置编码与 MLP 得到分辨率嵌入 $e_r$；
- **调制注入**：将 $e_d, e_r$ 经两个 MLP 投影并通道翻倍，拆分为 scale/shift 参数，对 VDiT 块中 MLP 后的深度特征依次施加调制：
  - $z^l_d = z^l \cdot (1 + e^{\text{scale}}_d) + e^{\text{shift}}_d$
  - $z^l_r = z^l_d \cdot (1 + e^{\text{scale}}_r) + e^{\text{shift}}_r$
  - $s^{l+1} = [z^l_r;\, c^l]$

### 3. 训练流程

- **骨干**：Wan 2.1 1.3B T2V 模型；采用 **Flow Matching** 目标，预测速度场 $v_t$：
  - $\mathcal{L} = \mathbb{E}_{t, z_0, z_1, c, e_r, e_d}\left[M \odot \|u_\Theta(z_t, t, c, e_r, e_d) - v_t\|^2\right]$
- **数据处理**：将深度 $V_D$ 转为视差并按视频做 min-max 归一化到 $[-1, 1]$；通过阈值 $D_{\max}$ 构造二值有效掩码 $M$，损失**仅在有效区域计算**；
- **推理**：从高斯噪声出发，条件于 RGB 视频及其语义/分辨率特征，求解 ODE 得到深度序列，采样步数设为 5。

---

## 三、实验设计

- **训练数据集**（约 0.8M 帧）：
  - VKITTI、TartanAir 与 TartanGround 的子集（仅用单向相机）、OmniWorld 的合成子集。

- **评测 Benchmark**：
  - **Sintel**（高度动态场景与复杂运动）、**KITTI**、**ScanNet**、**Bonn**；
  - 额外：500 帧 **ScanNet++** 长序列、自建**低光 Sintel** 变体（分布偏移鲁棒性测试）；
  - 定性对比：3D 游戏、2D 卡通、水下、室内、驾驶、夜间等场景。

- **对比方法**：
  - 判别式：Depth Anything V2、Video Depth Anything；
  - 生成式：ChronoDepth、DepthCrafter、Depth Any Video。

- **评价指标**：RMSE、阈值精度 $\delta_1$、绝对相对误差 AbsRel；长序列另用时间对齐误差 TAE。

- **公平性处理**：所有基线均重新推理，并使用 DepthCrafter 官方评测脚本统一评估，因此报告的基线指标可能与原论文不同。

---

## 四、资源与算力

- **明确说明的部分**：
  - GPU：**4 张 H800**；
  - 训练：**8 个 epoch**，每卡 batch size 为 1，学习率 $2 \times 10^{-4}$，梯度累积 32 步；
  - 训练分辨率策略：多分辨率训练，保持原始宽高比、空间维度可被 32 整除；token 预算基准为 $672 \times 384 \times 77$，时间长度在 21–77 帧间随分辨率反向调整；
  - 推理采样步数：5 步。
- **未明确说明的部分**：论文**未给出具体训练总时长/墙钟时间**，也未报告总 GPU 小时数，仅能从 4×H800、8 epoch、梯度累积 32 等配置间接估计。

---

## 五、实验数量与充分性

- **主要实验组**：
  1. 表 1：4 个数据集（Sintel / ScanNet / KITTI / Bonn）的零样本视频深度定量对比；
  2. 表 2：Sintel 上的**逐帧**深度精度（含逐帧 scale-shift 对齐）；
  3. 表 3：500 帧 ScanNet++ 上的**时间一致性与长序列**评测（TAE）；
  4. 表 4：未见**低光**分布偏移下的鲁棒性；
  5. 表 5：**消融实验**，围绕三个问题（Q1 ICC vs 通道拼接；Q2 SAND-Attention 的三种变体：全注意力 / 无 RoPE 对齐 / 无解耦注意力；Q3 SRFM 的三种变体：整体移除 / 去 DINOv2 / 去分辨率嵌入）；
  6. 表 6：效率对比（时间、FPS、显存）；
  7. 表 7：不同采样步数（3/5/10/20）的精度-效率权衡；
  8. 图 3、图 4：多域与夜间场景的定性对比。
- **充分性评价**：
  - 覆盖面较广，从精度、一致性、鲁棒性、效率到消融均有涉及，**实验设计较为完整**；
  - 消融实验针对性明确，能清晰归因各模块贡献（如 RoPE 对齐缺失导致 AbsRel 从 0.250 恶化到 0.410，验证其关键性）；
  - **客观性较好**：统一使用 DepthCrafter 官方评测脚本、重新推理全部基线，避免了不同论文评测协议不一致带来的偏差；
  - **潜在不足**：训练数据规模远小于对手，虽被宣传为“数据高效”，但也意味着训练集分布较窄（以合成数据为主），可能对真实域泛化的验证还不够充分；部分定性对比缺乏量化支撑。

---

## 六、主要结论与发现

- **SOTA 性能**：在 Sintel、KITTI、Bonn 上取得最佳 AbsRel 与 $\delta_1$；Sintel 上 AbsRel 提升 16.0%、$\delta_1$ 提升 10.1%；ScanNet 上以显著更少数据取得接近最优的第二名。
- **极高数据效率**：仅用 **0.8M 帧**训练，比同类生成式方法（6M–10.5M）少 **6–13×**。
- **逐帧精度更优**：表 2 显示其逐帧精度超过其他视频深度模型，甚至超过 Depth Anything V2，说明视频上下文带来了额外增益。
- **长序列一致性最佳**：500 帧 ScanNet++ 上 TAE 最低（2.61），AbsRel 最低（0.131）。
- **鲁棒性最强**：低光 Sintel 上 $\delta_1$ 相对退化仅 **4.0%**，远低于 DepthCrafter（8.4%）与其他方法（13.2%）。
- **消融结论**：
  - ICC 显著优于通道拼接（AbsRel 0.250 vs 0.367）；
  - SAND-Attention 中 RoPE 对齐最关键，缺失会导致严重失败；解耦注意力缺失造成中等但显著的退化；
  - SRFM 整体移除的损失大于任一子组件单独移除，说明 DINOv2 语义先验与分辨率嵌入存在**协同效应**。
- **效率**：与 Depth Any Video 推理速度相当（11.85s vs 11.19s），但显存仅 **11.0 GB vs 33.0 GB**；仅需 3–5 步采样即可保持较强精度。

---

## 七、优点

- **范式创新**：首次将 ICC 范式系统性地从生成任务迁移到视频深度估计这一密集预测任务，并给出针对性的适配方案（SAND-Attention + SRFM），而非简单套用。
- **非侵入式适配**：不改动 VDiT 的输入投影层，充分利用预训练注意力的跨模态建模能力，避免通道拼接的信息损失。
- **数据效率突出**：在 0.8M 帧上即达 SOTA，显著降低训练成本，对实际落地有吸引力。
- **显存友好**：相比同类生成式方法显存降低约 3 倍，且保持相当推理速度。
- **实验严谨性**：统一评测脚本重跑所有基线，主动说明指标差异来源，消融实验设计层次清晰、归因明确。
- **泛化能力强**：在雾天、夜间、水下、2D/3D 动画等多域场景及 1080p 非标准宽高比下均表现稳健。

---

## 八、不足与局限

- **推理速度仍受限于生成式范式**：11.85s / 4.5 FPS，远慢于判别式的 Video Depth Anything（1.82s / 29.1 FPS），难以满足实时应用需求。
- **训练数据规模与多样性有限**：仅 0.8M 帧且以合成数据（VKITTI、TartanAir、OmniWorld）为主，真实域覆盖不足；论文虽强调零样本泛化，但缺乏对真实采集视频的大规模系统性验证。
- **训练成本未完全披露**：未报告总训练时长或 GPU 小时数，难以横向比较实际训练开销。
- **部分指标非最优**：ScanNet 上仅列第二，说明在室内静态场景下仍有提升空间。
- **掩码与归一化依赖**：训练依赖最大深度阈值构造的有效掩码，以及逐视频 min-max 归一化，对深度范围异常或缺失的视频可能敏感。
- **消融维度有限**：SRFM 中 scale/shift 调制顺序、DINOv2 特征池化方式等细节未做进一步敏感性分析；采样步数增加反而精度波动（表 7 中 10/20 步结果与 3/5 步不一致），其稳定性机制未深入解释。
- **应用限制**：生成式扩散推理的随机性与多步采样特性，可能在高安全要求的自动驾驶等场景中带来可复现性与延迟上的顾虑。

（完）
