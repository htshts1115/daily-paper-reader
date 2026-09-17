---
title: Zero-Shot Novel Depth Synthesis Using Foundation Models Scene Representations
title_zh: 利用基础模型场景表示的零样本新视角深度合成
authors: "Denis Akola, David Fouhey"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/10966.pdf"
tags: ["query:mono-depth"]
score: 7.0
evidence: 利用3D基础模型场景表示的零样本新视角深度合成
tldr: 以VGGT为代表的3D基础模型通过前馈Transformer预测丰富的统一表示，在多种3D任务上表现优异。本文研究能否利用其内部表示从新视角推断场景3D，假设求解3D重建需要模型学习包含大量场景常识的表示。作者先证明可从3DFM内部表示解码隐藏表面，进而提出Z3D，在3DFM表示上进行潜在扩散以估计未见视角的点图。实验表明该方法可实现零样本新视角深度合成，凸显3D基础模型表示的通用价值。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-001.webp\", \"caption\": \"\", \"page\": 4, \"index\": 1, \"width\": 450, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-002.webp\", \"caption\": \"\", \"page\": 11, \"index\": 2, \"width\": 525, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-003.webp\", \"caption\": \"\", \"page\": 11, \"index\": 3, \"width\": 547, \"height\": 547}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-004.webp\", \"caption\": \"\", \"page\": 11, \"index\": 4, \"width\": 547, \"height\": 550}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-005.webp\", \"caption\": \"\", \"page\": 11, \"index\": 5, \"width\": 608, \"height\": 846}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-006.webp\", \"caption\": \"\", \"page\": 11, \"index\": 6, \"width\": 517, \"height\": 517}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-007.webp\", \"caption\": \"\", \"page\": 11, \"index\": 7, \"width\": 517, \"height\": 517}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-008.webp\", \"caption\": \"\", \"page\": 11, \"index\": 8, \"width\": 518, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-009.webp\", \"caption\": \"\", \"page\": 11, \"index\": 9, \"width\": 518, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-010.webp\", \"caption\": \"\", \"page\": 11, \"index\": 10, \"width\": 518, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-011.webp\", \"caption\": \"\", \"page\": 11, \"index\": 11, \"width\": 414, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-012.webp\", \"caption\": \"\", \"page\": 11, \"index\": 12, \"width\": 414, \"height\": 370}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-013.webp\", \"caption\": \"\", \"page\": 11, \"index\": 13, \"width\": 388, \"height\": 348}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-014.webp\", \"caption\": \"\", \"page\": 11, \"index\": 14, \"width\": 388, \"height\": 348}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-015.webp\", \"caption\": \"\", \"page\": 11, \"index\": 15, \"width\": 390, \"height\": 348}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-016.webp\", \"caption\": \"\", \"page\": 12, \"index\": 16, \"width\": 638, \"height\": 701}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-017.webp\", \"caption\": \"\", \"page\": 12, \"index\": 17, \"width\": 504, \"height\": 474}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-018.webp\", \"caption\": \"\", \"page\": 12, \"index\": 18, \"width\": 504, \"height\": 474}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-019.webp\", \"caption\": \"\", \"page\": 15, \"index\": 19, \"width\": 432, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6665f343bacae5db153e977f/fig-020.webp\", \"caption\": \"\", \"page\": 15, \"index\": 20, \"width\": 438, \"height\": 474}]"
motivation: 3D基础模型已能预测统一表示，但其内部表示能否用于新视角3D推断尚待研究。
method: 提出Z3D，在3D基础模型的内部表示上进行潜在扩散，估计未见视角的点图。
result: 证明可从3DFM内部表示解码隐藏表面，并实现新视角深度合成。
conclusion: 揭示3D基础模型蕴含丰富场景知识，可支持零样本新视角深度推断。
---

## Abstract
3D Foundation Models (3DFMs) such as VGGT have re-cently pushed the boundaries of 3D vision by predicting rich unifiedrepresentations with feed-foward transformers. The scene representationslearned by these models enable strong performance on multiple 3D visiontasks. In this paper, we investigate using their internal representationsto infer 3D in the scene from new views. Our hypothesis is that in or-der to solve the task of 3D reconstruction, these models need to learn arepresentation that includes a large amount of general knowledge about3D scenes. After showing that it is possible to decode hidden surfacesfrom internal 3DFM representations, we propose a method, Z3D, thatestimates pointmaps in unseen views by doing latent diffusion on 3DFMrepresentation. We show that Z3D can predict realistic depthmaps fornew views across multiple datasets.

---

## 论文详细总结（自动生成）

# 论文总结：Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations（Z3D）

## 1. 核心问题与研究背景

- **任务定义**：**新视角深度合成（Novel Depth Synthesis）**——给定一幅或少量输入视角图像，以及目标相机的位姿，预测未见视角下合理且几何一致的深度图，**尤其包括被前景遮挡、完全未观测到的几何结构**。
- **应用动机**：机器人导航、AR/VR、自动驾驶等场景中往往只能观测到场景的部分表面，但系统必须对被遮挡区域做几何推理，以支持物理交互、规划与空间推理。
- **现有方法局限**：
  - NeRF、3D Gaussian Splatting 等神经表示擅长**观测视角之间的插值**，但需要稠密输入与逐场景优化，**并非为遮挡后几何的"幻想"（hallucination）而设计**，稀疏视角下几何不完整。
  - 联合学习视角与深度预测的早期工作泛化能力有限。
  - 基于扩散模型的深度预测多在 **2D 图像空间**进行，缺乏强 3D 一致性先验，跨视角几何不连贯。
- **核心洞察/假设**：3D 基础模型（3DFMs，如 VGGT、WorldMirror）为完成 3D 重建任务，其内部表示必然**隐含大量关于 3D 场景的通用知识**，包括不可见表面；因此可将其内部表示与扩散模型结合，把新视角深度合成建模为**场景几何上的条件生成任务**。

## 2. 方法论

### 2.1 核心思想
- **解耦表示学习与生成补全**：表示学习交由预训练 3DFM（冻结），生成式补全交由扩散模型。
- 直接把 3DFM 的 patch token 空间当作**潜空间**做 latent diffusion：条件信号来自 3DFM 中间层特征与目标视角相对位姿，扩散采样出的 token 再交给原 3DFM 的 DPT 深度头解码为深度图。
- 最终形式：`d̂ = D(x₀)`，其中 `x₀` 为扩散模型恢复出的目标视角干净 token。

### 2.2 前置验证：3DFM 是否编码隐藏结构？
- 采用**线性探针**思路，以**分层深度图像（LDI, Layered Depth Images）**为目标：LDI 在每像素处表示光线穿过的前 k 个表面，准确预测第 2 层及以后表面必须理解遮挡区域。
- 做法一：扩展 VGGT 的 DPT 头，使其输出 4 层深度与置信度图，其余层冻结训练；结果显示能产生合理的分层深度，**超出首个可见表面**。
- 做法二：在 3DFM 特征上做线性探针预测 LDI，定量结果（Table 1）：
  - 数据集平均基线：AbsRel 0.319 / δ<1.25 0.564
  - VGGT-LDI：0.197 / 0.717
  - WM-LDI：0.167 / 0.789
  - 结论：即便弱线性模型也能把误差减半，说明隐藏/未观测信息**确实内嵌在 3DFM 表示中**。

### 2.3 Z3D 网络架构
四个组件：**冻结 3DFM 骨干 φ + 位姿编码器 pθ + 条件扩散模型 fθ（DiT）+ DPT 头 D**。

- **3DFM 骨干 φ（冻结）**：
  - 每张图像切 patch 成 token，经帧内注意力与跨帧全局注意力交替处理，拼接为场景表示。
  - 关键设计：仅使用**第 17 层**token 作为扩散的目标/噪声空间（据类似文献分析，该层对深度预测贡献显著高于其他三个聚合层），以控制计算量；**源视角则使用全部四层聚合输出作为条件**，补偿信息损失。token 维度约 2048。
- **位姿编码器 pθ**：
  - 目标视角相对位姿表示为每视角 12 维向量，Fourier 编码后经 MLP 映射到与 patch token 同维；所有位姿**相对源集合第一帧**表示。
- **扩散模型 fθ（DiT 架构）**：
  - 定义 `x₀ = fₜ = φ(Iₜ)`（目标），`zₛ = fₛ = φ(Iₛ)`（源），`p = pθ(Pₜ)`。
  - 仅对目标 token 加噪，源 token 保持干净仅作条件。
  - 前向扩散：`xₜ = √αₜ·x₀ + √(1−αₜ)·ε`，`αₜ = Π(1−βₛ)`。
  - 去噪器预测**速度（velocity）**：`v̂ₜ = fθ(xₜ, t, zₛ, p)`。
  - 条件注入方式：每个 DiTBlock 插入**交叉注意力**以关注源视角多尺度特征；位姿嵌入**直接加到时间步嵌入**上（类似 DiT 的 adaLN 做法）。
  - **噪声调度器的时间步偏移（timestep shift）**：标准调度器面向低维潜空间（≲1024），直接用于高维 3DFM token 空间（≥1024）不稳定，故采用维度相关的缩放规则 `α = √(m/n)`，基准维度 n=4096，m 取 3DFM 表示的有效数据维度。
- **DPT 头 D**：类比 VAE 解码器，将采样 token 解码为深度图，训练与推理中均**冻结**。

### 2.4 训练与实现细节
- 框架：PyTorch + 改造版 DiT；采用 **flow-matching** 噪声调度与速度预测目标（遵循 Stable Diffusion v3 形式）。
- 训练：FlowMatchEulerDiscreteScheduler，**1000 步时间步**；推理仅采样 **50 步**。
- **两阶段训练**（因 Stage 2 从零训练不稳定、收敛慢）：
  - Stage 1：1 源 → 1 目标视角，有效 batch size 128，**98k 步**。
  - Stage 2：2 源 → 4 目标视角，有效 batch size 32，**156k 步**，从 Stage 1 权重初始化。
- 优化器：AdamW，β₁=0.9、β₂=0.95，无权重衰减，学习率 2×10⁻⁴，前 10% 线性 warmup，30% 训练进度后线性衰减至 0。
- **训练数据**：由 5 个真实+合成数据集聚合而成——MegaDepth、Hypersim、Taskonomy、Replica、Habitat HM3D；样本通过**成对相机视锥重叠度**挖掘，每序列约 2–6 张重叠视角。

## 3. 实验设计

- **评测数据集**：
  - 域外：DTU、NRGBD、7-Scenes。
  - 域内：训练数据集测试划分的子集。
  - 户外单独报告：MegaDepth（Table 6）。
- **评测设定**：`1 源 → 1 目标` 与 `2 源 → 4 目标` 两种，评估跨域泛化能力。
- **指标**：
  - 深度：仿射不变深度评测协议（最小二乘/Weiszfeld 对齐后）计算 **AbsRel** 与 **δ<1.25**。
  - 多视角 3D 重建：将深度投影为点云，报告 **Accuracy（Acc.）** 与 **Completion（Comp.）**，均含均值与中位数。
- **对比方法（基线）**：
  - **LVSM + 3DFM**：用 SOTA 场景无关新视角合成模型 LVSM 生成新视角 RGB，再用 VGGT / WorldMirror 估计深度（记为 LVSM+VGGT、LVSM+WM）。
  - **Depth Diffusion (DD)**：使用与 Z3D 相同架构，但扩散直接在 3DFM 输出的**深度图像素空间**上进行（VGGT-DD、WM-DD），用于剥离"潜空间 vs 像素空间"的影响。
  - MVGD（最相关的工作）因**代码不可得而未做直接比较**。
  - 消融性质对比：Z3D-VGGT、Z3D-WM（不同 3DFM 骨干）。
- **额外泛化实验**：在更新的 3DFM **VGGT-Ω** 上按 1→1 设定重训 Z3D-VGGT-Ω（Tables 7、8），无算法改动。
- **定性分析**：深度图对比（Fig.3）、**深度梯度分析**（Fig.4，展示 DD 基线有明显梯度尖峰）、单源点云对比（Fig.5）、

- **定性分析（续）**：
  - 多视角点云拼接对比（Fig.6），验证跨视角几何一致性；
  - 户外场景定性结果（Fig.7），展示在 MegaDepth 等大尺度、远距离场景下的深度预测表现。
- **消融实验**：针对关键设计选择设置消融，包括（1）扩散作用空间：3DFM token 潜空间 vs. 深度图像素空间（对应 DD 基线）；（2）条件注入方式：交叉注意力 + 位姿嵌入 vs. 简单拼接/仅时间步条件；（3）位姿编码：相对位姿 vs. 绝对位姿或无位姿；（4）3DFM 层选择：仅第 17 层 vs. 多层聚合；（5）噪声调度器：维度自适应偏移 vs. 标准调度器。
- **评测关注点**：在稀疏输入与遮挡区域的深度合理性、跨数据集域泛化、多视角几何一致性，以及扩散是否真正"补全"而非简单回归可见表面。

## 4. 主要结果与发现

- **潜空间 vs. 像素空间**：Z3D 在所有评测数据集上稳定优于 DD 基线（VGGT-DD、WM-DD），说明将扩散放在 3DFM 潜空间比直接在深度图像空间做扩散更能保持 3D 一致性。DD 基线的深度梯度分析（Fig.4）显示其在物体边界处出现明显梯度尖峰，反映像素空间扩散难以建模跨视角几何约束。
- **跨域泛化**：在 DTU、NRGBD、7-Scenes 等域外数据集上，Z3D-VGGT 与 Z3D-WM 的 AbsRel 与 δ<1.25 均优于 LVSM+VGGT / LVSM+WM，表明 Z3D 不依赖测试场景的逐场景优化，具备零样本泛化能力。
- **遮挡区域补全**：定性结果（Fig.3、Fig.5、Fig.6）显示 Z3D 能对前景遮挡后的几何结构给出合理预测，点云在遮挡边界处无明显断裂或"空洞"，而基线方法在遮挡区域往往出现深度塌陷或几何不连续。
- **多视角 3D 重建**：投影点云的 Accuracy 与 Completion 指标（含均值与中位数）表明 Z3D 在 2→4 设定下重建完整度更高，且中位数误差较低，说明其误差分布更集中、少有大偏差离群点。
- **户外场景**：MegaDepth 上的单独报告（Table 6）验证方法在大尺度、纹理稀疏、远距离场景下仍保持稳定，未出现明显域偏移退化。
- **3DFM 骨干影响**：Z3D-WM 与 Z3D-VGGT 结果相近且各有优势，说明框架对骨干具有一定通用性；使用 VGGT-Ω 重训的 Z3D-VGGT-Ω（Tables 7、8）在 1→1 设定下进一步提升，验证方法可随 3DFM 升级而受益，且无需算法改动。
- **线性探针结论的意义**：Table 1 的 LDI 探针结果从机制上支撑了 Z3D 的合理性——3DFM 表示中确实编码了未观测表面信息，扩散模型的作用是"解锁/解码"这些信息，而非凭空生成。

## 5. 贡献与创新点

- **问题新定义**：明确提出**新视角深度合成（Novel Depth Synthesis）**任务，强调对遮挡后未观测几何的推理，区别于传统新视角合成与单目/多视角深度估计。
- **表示与生成解耦**：提出将预训练 3DFM 的 patch token 空间直接作为扩散潜空间，冻结表示学习、仅训练条件扩散补全，避免了端到端训练对 3D 先验的破坏。
- **机制性验证**：通过 LDI 线性探针与扩展 DPT 头实验，实证 3DFM 内部表示隐含隐藏结构信息，为方法提供可解释依据。
- **工程细节贡献**：针对高维 token 潜空间的噪声调度器维度偏移规则、仅对目标 token 加噪、源 token 全层聚合作条件、位姿嵌入加至时间步嵌入等设计，均为该范式下可复用的实践方案。
- **零样本与可升级性**：无需逐场景优化即可跨域泛化，并可随更强 3DFM（如 VGGT-Ω）直接受益，具备良好的可扩展性。

## 6. 局限性与未来方向

- **计算成本**：高维 token 潜空间扩散推理仍需 50 步采样，且 3DFM 骨干与 DPT 头推理开销较大，实时性受限。
- **数据依赖**：训练依赖成对相机视锥重叠度挖掘的样本，对极稀疏或无重叠输入场景的适用性未充分讨论。
- **未直接对比 MVGD**：因代码不可得而未做直接比较，与最相关工作的方法论差异缺少定量对照。
- **评测协议**：深度采用仿射不变协议，虽利于跨方法比较，但可能弱化绝对尺度一致性的评估；点云指标对对齐方式较敏感。
- **潜在方向**：减少采样步数（如一致性模型、蒸馏）、扩展到视频/动态场景、结合显式 3D 表示（如 3DGS）做联合优化、以及将位姿不确定性纳入条件建模。

## 7. 总体评价

Z3D 的核心价值在于提出并验证了一个清晰的技术假设：**3D 基础模型的内部表示已隐含场景的隐藏几何，生成式模型的作用是在该表示空间上做条件补全**。论文以 LDI 探针提供机制证据，以潜空间扩散架构实现方法，并通过跨域、遮挡、多视角一致性等多维度实验加以验证，逻辑链条完整。其"冻结 3DFM + 潜空间条件扩散"的范式对后续新视角深度、场景补全与 3D 生成任务具有较好的参考与迁移价值；主要不足在于计算开销、与最相关工作的直接对比缺失，以及评测协议对绝对尺度的弱化。

（完）
