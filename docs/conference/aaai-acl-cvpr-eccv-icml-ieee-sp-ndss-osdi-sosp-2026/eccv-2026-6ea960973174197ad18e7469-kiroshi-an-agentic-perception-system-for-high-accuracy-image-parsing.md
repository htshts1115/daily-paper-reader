---
title: "Kiroshi: An Agentic Perception System for High-Accuracy Image Parsing"
title_zh: Kiroshi：用于高精度图像解析的智能体感知系统
authors: "Haipeng ZHOU, Jinshan Liu, He Zhang, Xuequan Lu, Jun Ma, Lei Zhu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2569.pdf"
tags: ["query:matting"]
score: 8.0
evidence: 全自动高精度抠图与分割
tldr: 高精度图像解析中的抠图与分割比常规稠密预测更难，需要精细细节估计，而现有方法要么缺乏语义感知，要么依赖人工反复核验，使全自动抠图难以实现。本文提出Kiroshi智能体感知系统，训练带迭代细化的动作模型，并从残差图采样网格提示、挖掘配对轨迹，基于量化质量进行正负样本学习。该方法推动了全自动高精度抠图与分割，减少对人工验证的依赖，对前景背景精细分离具有直接价值。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-001.webp\", \"caption\": \"\", \"page\": 6, \"index\": 1, \"width\": 928, \"height\": 652}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 2747, \"height\": 1422}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-010.webp\", \"caption\": \"\", \"page\": 7, \"index\": 10, \"width\": 414, \"height\": 414}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-012.webp\", \"caption\": \"\", \"page\": 9, \"index\": 12, \"width\": 4418, \"height\": 3246}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-013.webp\", \"caption\": \"\", \"page\": 9, \"index\": 13, \"width\": 4002, \"height\": 2784}]"
motivation: 高精度抠图与分割需精细细节估计，现有方法缺乏语义感知或依赖人工反复核验，全自动抠图仍难实现。
method: 提出Kiroshi智能体感知系统，训练带迭代细化的动作模型，并从残差图采样网格提示挖掘配对轨迹。
result: 实现全自动的高精度抠图与分割，减少对人工验证和重复检查的依赖。
conclusion: 推动全自动抠图走向可行，为精细图像解析提供智能体式新范式。
---

## Abstract
Parsing images with high precision for matting and segmentation is sig-nificantly more challenging than conventional dense prediction, as it requires accurateestimation of fine-grained details. Existing methods either lack semantic awareness orproduce suboptimal predictions; even interactive matting approaches rely on manualverification and repetitive checking, making fully automatic matting still unattainable.In this work, we propose Kiroshi , an agentic perception system for high-accuracyimage parsing. We train an Action Model with iterative refinement and mine pairedtrajectories by sampling grid prompts from residual maps, where each step yields apositive and a negative transition under the same intermediate prediction based onquantitative quality gains. These within-context preference pairs form a reliable su-pervision signal for post-training to align the MLLM policy toward more effectivegrid decisions. We also contribute a new High-Fidelity Referring Matting and Seg-mentation (HiFiRefMS ) benchmark to evaluate the performance of different mod-els. Experimental results demonstrate that our method surpasses state-of-the-art ap-proaches both quantitatively and qualitatively, and extensive ablation studies furthervalidate the effectiveness and superiority of our agentic design. Project will be releasedat https://github.com/haipengzhou856/Kiroshi.

---

## 论文详细总结（自动生成）

# Kiroshi：用于高精度图像解析的智能体感知系统 — 论文总结

## 1. 核心问题与研究背景

- **问题定位**：高精度图像解析（抠图 matting + 分割 segmentation）比常规稠密预测更难，因为它不仅要求语义正确，还要求对**精细结构**（发丝、透明区域、孔洞、细边缘）进行准确估计。
- **现有方法的三类缺陷**：
  - **显著目标类方法**（IS-Net、MVANet、DiffDIS 等）：能保留细细节（如绳索），但**缺乏语义感知**，在多实例场景下极易过度抠图或漏抠。
  - **交互式方法**（HQ-SAM、ZIM、SmartMatte、SDMatte 等）：通过点/框提示可提升边界精度，但**依赖人工反复检查与修正**，无法全自动；且 ZIM 对负向提示不敏感，HQ-SAM 语义稳定但边界保真度不足。
  - **MLLM 推理分割方法**（LISA、SAM4MLLM、Text4Seg、SegAgent 等）：语义对齐好，但受底层模型（如 SAM）限制，**掩码粗糙**，无法恢复透明度与细边界；且把像素级轨迹（点）作为优化目标时搜索空间巨大、冗余严重。
- **核心洞察**：现有数据集（DIS-5K、RefCOCO、RefMatte 等）要么只提供二值标注不区分实例，要么依赖合成贴图数据导致真实场景泛化差，缺乏"指代 + 高保真"的统一评测。
- **总体含义**：作者把高精度解析重构为**智能体感知问题（agentic perception）**——系统不应只做一次性输出，而应观察当前预测、判断哪里不可靠、并迭代精修，从而实现**全自动、语义感知、高保真**的掩码预测。

## 2. 方法论

### 2.1 总体框架（Plan-and-Act MDP）

- 系统由两个协作组件构成：**MLLM 策略生成器 𝒫** 与 **动作模型 𝒜**。
- 在精修步 $t$，策略观测状态 $o_t = (I, X, s_t)$（图像、文本指令、当前中间结果），输出**区域级动作** τ_t，即一段可解码的**文本网格图（textual grid map）**：
  - $\tau_t = \mathcal{P}(o_t) = \mathcal{P}(I, X, s_t)$
- 动作模型在像素级执行该动作并更新预测：
  - $s_{t+1} = \mathcal{A}(I, s_t, \tau_t),\quad t = 0,\dots,T-1$
- 最终输出 $\hat{s} = s_T$。设计哲学：**MLLM 决定"在哪里精修、修什么"（语义可解释），动作模型决定"如何精修"（恢复高频细节与边界）**。

### 2.2 网格感知动作模型（Grid-aware Action Model）

- 骨干：**DINOv2-Base 编码器 + Mask2Former 风格解码器**。
- 核心机制：把网格图转换为 **attention mask** 注入 Transformer 解码器，作为结构化提示信号：
  - $\mathbf{Z}_l = \mathrm{softmax}(M_{l-1} + \mathbf{Q}_l\mathbf{K}_l^{\top})\mathbf{V}_l + \mathbf{Z}_{l-1}$
  - $M^{b}(s) = 0$（若 patch 属于网格），否则 $-\infty$（屏蔽）。
- 设计收益：(i) 用一致的 patch 级交互替代不稳定的像素级点提示，缩小搜索空间；(ii) 提供更丰富的语义与边界线索；(iii) 天然适配 MLLM 智能体框架。

### 2.3 轨迹挖掘（Trajectory Mining，Alg. 1）

- 对每张图执行 K 次 rollout；每步从**残差图** $r_t = |Y - s_{t-1}|$ 中采样网格提示。
- **候选 patch 判定**：p×p 的 patch 中若超过 ε（默认 **40%**）的像素残差非零，则进入候选队列（零残差代表模型已确信）。
- 从候选中**均匀采样 75%** 的 patch 组成轨迹 τ，构建 attention mask 后送入动作模型。
- **同一状态下采两条轨迹**（τ⁺ 与 τ⁻），用 MSE 等定量指标比较 $Q(s_t^{+}) - Q(s_{t-1})$ 与 $Q(s_t^{-}) - Q(s_{t-1})$，直到出现"正增益 + 负增益"配对，分别放入正/负样本池 $D^{+}$、$D^{-}$。
- 关键点：随着动作模型收敛，预测整体变好，但随机采样仍能持续产生**信息量充足的负样本**，从而在同一状态 $(I, B, s_{t-1})$ 下形成**干净的上下文内偏好信号（within-context preference pairs）**。

### 2.4 赋予 MLLM 感知能力（文本化网格）

- 将掩码展平解析为特殊的文本描述符 `<grid>`，每个 patch 作为一个语义单元，共四类语义：
  - `<target>`（如 `<human>`）、`<bg>`、`<unknown>`（需精修的不确定区）、`<other>`（其他实例）。
- 采用 **Row-wise Run-Length Encoding（R-RLE）** 压缩 token 长度，例如一行 64 个背景 patch 记为 `bg*64`（单 token）。理论上 32×32 网格最多 1024 token，但由于掩码空间连续性，实际序列远短于上界。
- `<unknown>` 区域由 trimap 经标准腐蚀–膨胀过程导出；该阶段同时做视觉定位（visual grounding），为后续精修提供良好初始化。
- SFT 阶段使用标准交叉熵损失，监督信号纯文本。

### 2.5 后训练对齐（DPO）

- 动机：抠图涉及极细结构与稀疏像素级奖励，DPO 比依赖稠密奖励的 RL 更稳定高效。
- DPO 数据来自动作模型 rollout：τ_t 使预测变好则为 chosen，否则为 rejected；并用 **Qwen3-VL Plus** 生成位置感知、语义落地的轨迹描述，组织成 VQA 风格对话数据。
- 损失：$\mathcal{L}_{\mathrm{DPO}} = -\log\sigma\big(\beta[\log\mathcal{P}(\tau_+|I,X) - \log\mathcal{P}(\tau_-|I,X)]\big)$
- 动作模型损失：**ℓ1 损失 + Laplacian 损失**组合。

### 2.6 推理流程

- 采用 **MLLM-as-Judge + Prompt Rolling** 驱动多轮精修；网格图中仅 `<target>` 与 `<unknown>` 区域视为有效并转换为 attention mask；默认 **3 轮精修**。

## 3. 实验设计

### 3.1 数据集与 Benchmark

- **新提出 HiFiRefMS（High-Fidelity Referring Matting and Segmentation）基准**：
  - **抠图子集**：468 张图 / 1187 个掩码（连续透明度 0–1）。
  - **分割子集**：500 张图 / 1366 个掩码（二值 0/1）。
  - 由公开数据集（PPM-100、AIM、[35]、DIS-5K、HIM、MGMatting 等）重组、清洗、重标注而成，强调**多实例场景**；对遮挡/视觉复杂样本进行人工重标注；分割子集剔除透明物体以避免标签不一致（如玻璃桌）。
  - 文本指代表达由 **Qwen3-VL Plus** API 流水线生成。
- **跨数据集验证**：额外在合成数据集 **RefMatte-Syn** 上做交叉验证。

### 3.2 对比方法与指标

- **对比三类共 15 个方法**：
  - 显著类：IS-Net、PGNet、HitNet、MVANet、DiffDIS。
  - 交互类：HQ-SAM、MAM、SmartMatte、SDMatte、ZIM。
  - MLLM 类：LISA、SAM4MLLM、Text4Seg、SegAgent。
- **指标**：
  - 抠图：SAD、MSE、Grad、Conn。
  - 分割：maxFβ、Fβ、MAE、Sα、HCE。
- **公平性设置**：交互式方法按 [17] 惯例提供 **GT 导出的框**（即精确框、无文本指代），唯 MAM 保留其原 pipeline（GroundingDINO → SAM → matting）。

## 4. 资源与算力

- 论文仅说明："所有实验在 **NVIDIA A100（80GB）GPU** 上完成"。
- **未明确给出 GPU 数量、训练总时长、显存占用或训练步数**等细节；作者称更多细节放在补充材料中（本次提供的正文未包含）。
- 模型规模信息：动作模型使用 **DINOv2-Base**，MLLM 使用 **Ovis2.5-2B**（消融中另比较 Qwen2.5-VL-3B、InternVL3.5-2B、Qwen3-VL-2B）。
- 数据规模：DPO 数据约 **40,000 对对话**；SFT 用 RefCOCO 系列 + RefMatte；动作模型用与 SmartMat 同量级的公开抠图数据 + DIS-5K + UHR-SOD。

## 5. 实验数量与充分性

- **主要定量对比（Tab. 1）**：15 个基线方法 × 9 项指标，覆盖三大类范式。
- **消融实验（4 组）**：
  - Tab. 2：**MLLM 骨干**对比（4 种：Qwen2.5-VL-3B、InternVL3.5-2B、Qwen3-VL-2B、Ovis2.5-2B）。
  - Tab. 3：**策略配置**（Vanilla box、1 轮、3 轮、5 轮）。
  - Tab. 4：**网格粒度**（16×16、32×32、64×64）。
  - Tab. 5：**跨数据集协议对比**（8 种配置，含 GT-box+ZIM、GroundDINO-box+ZIM、Text4Seg 变体、SegAgent 变体、Ours×1/×3），并统计每图耗时。
- **定性对比**：Fig. 7 给出与 ZIM、DiffDIS、HQ-SAM、SegAgent 的视觉对比（发丝、透明、多实例）。
- **充分性评价**：
  - 优点：覆盖三类范式、跨真实/合成数据集、多维度消融（骨干/轮数/网格粒度/协议）、并报告时间成本，实验设计较为系统。
  - 可商榷点：仅有一个（自建）主 benchmark 承担全部主结果，缺少在既有权威基准（如 DIS-5K、RefCOCO 官方测试集）上的完整主表；消融规模较小（每项 3–4 个配置）；未报告多次运行的方差或显著性检验；跨数据集对比中部分基线的配置由作者自行搭建（如 Text4Seg-mask+MGMatting、SegAgent-mask+MGMatting），可能不完全等价于其原始设定。

## 6. 主要结论与发现

- **定量**：Kiroshi 在 HiFiRefMS 上取得全面最优——分割 maxFβ **0.875**、Fβ 0.820、MAE 0.033、Sα 0.866、HCE **1218**；抠图 MSE **0.0263**、SAD 26.34、Grad 23.71、Conn 13.48，均为最低误差。
- **定性**：相比框驱动交互方法（框内易泄漏其他 stuff/实例）与纯指代 MLLM 方法（掩码粗糙、丢失发丝与透明），本方法能保留细结构并实现更干净的实例分离。
- **机制性发现**：
  - 框提供强低级线索但存在"框歧义"；纯指代语义可靠但精度不足；**区域级语义决策 + 迭代像素级精修**可同时缓解两者。
  - 精修轮数存在权衡：3 轮为最佳平衡点，过少欠精修，过多收益递减。
  - 网格粒度存在权衡：16×16 细节更多但轨迹噪声大，64×64 更稳定但分辨率不足，**32×32 最优**。
  - 轨迹是**动态且由预测质量驱动**的，网格图会逐步移向边界与不确定区域，这是相对固定策略基线的核心优势。
- **总评**：本方法为稠密预测提供了一种可解释、有效且富有洞察的奖励设计，指向"推理驱动引导 + 高精度解析"统一的方向。

## 7. 优点与亮点

- **范式创新**：将高精度抠图/分割重构为闭环智能体感知（plan-and-act MDP），实现**全自动、无需人工反复核验**，直接针对"全自动抠图不可达"这一痛点。
- **区域级而非像素级推理**：用 patch 级网格提示替代不稳定点提示，显著缩小 MLLM 的搜索空间，避免 14×14 局部区域内多点冗余、语义信号不足的问题。
- **自监督式的偏好数据

生成**：偏好对来自动作模型的同状态双轨迹 rollout（τ⁺/τ⁻），天然构成 within-context preference pairs，无需人工标注或额外奖励模型即可完成 DPO 对齐。
- **多模态骨干的合理选型**：消融显示较小规模 MLLM（2B 级）即可胜任区域级决策，说明任务被成功"降维"到语义规划层，而非依赖超大模型暴力拟合。
- **文本化网格与 R-RLE 压缩**：把掩码解析为 `<target>/<bg>/<unknown>/<other>` 四类语义 token 并用行式游程编码压缩，使 MLLM 能以极短序列"看见"当前预测，兼顾了 token 效率与空间结构可读性。
- **训练目标与任务匹配**：动作模型采用 ℓ1 + Laplacian 损失，贴合抠图的透明度与高频边缘需求；策略侧用 DPO 而非稠密奖励 RL，规避了稀疏像素奖励下的训练不稳定。
- **评测贡献**：提出的 HiFiRefMS 同时覆盖"指代 + 抠图/分割 + 多实例"，并刻意剔除透明物体导致的标签歧义样本，为后续研究提供了更清晰的统一评测入口。
- **可解释性**：MLLM 输出的文本网格图本身就是人类可读的决策轨迹，能直接观察系统"认为哪里不确定、要修哪里"，优于端到端黑箱模型。

## 8. 不足与局限

- **算力与复现细节缺失**：正文仅提及 A100（80GB），未给出 GPU 数量、训练时长、显存占用、批大小与迭代步数，独立复现存在门槛；关键超参（如 ε=40%、采样 75%、β 等）的敏感性分析未充分展开。
- **主基准为自建**：核心结果全部落在作者新提出的 HiFiRefMS 上，缺少在 DIS-5K、RefCOCO/+/g、RefMatte 等既有权威基准上的完整主表，横向可比性受限，且自建基准的构建偏好可能无意中有利于本方法。
- **基线配置的等价性存疑**：跨数据集对比中，Text4Seg-mask+MGMatting、SegAgent-mask+MGMatting 等组合由作者自行搭建，未必等价于原论文设定；交互式方法使用 GT 框（强先验）而本方法使用文本指代，虽作者以协议对比（Tab. 5）回应，但不同先验条件下的公平性仍是可讨论点。
- **统计严谨性不足**：未见多次随机种子的方差报告、置信区间或显著性检验，单次结果的领先幅度（如 maxFβ 0.875）稳健性无法判断。
- **消融粒度有限**：骨干、轮数、网格粒度各自仅 3–4 个配置，缺少对 `<unknown>` 区域导出阈值、候选 patch 判定阈值 ε、rollout 次数 K、R-RLE 压缩策略等关键设计的选择依据与敏感性曲线。
- **推理成本**：多轮精修（默认 3 轮）叠加 MLLM 推理，单图耗时高于一次性前馈方法；论文虽在 Tab. 5 报告时间，但未系统讨论精度–延迟权衡与可部署性。
- **泛化边界未探明**：仅补充了合成数据集 RefMatte-Syn 的交叉验证，对视频、3D、极端透明/反光材质、超多实例密集场景的适用性缺乏证据。
- **对底层动作模型的依赖**：最终边界保真度仍受 DINOv2-Base + Mask2Former 解码器的能力上限约束；若动作模型本身对某类细结构（如极细网格纱、半透明烟雾）建模不足，策略层再优也难以补救。

## 9. 总体评价与启示

- **定位**：Kiroshi 的核心贡献不在于单点网络结构创新，而在于**问题重构**——把高精度抠图/分割从"一次性稠密预测"改写为"语义规划 + 像素执行"的闭环智能体感知，并用文本化网格打通了 MLLM 与像素级精修之间的接口。
- **方法学价值**：区域级（patch 级）动作表示是一个值得迁移的设计，它同时解决了 MLLM 输出像素轨迹的搜索空间爆炸问题与点提示语义贫弱的矛盾；其"同状态双轨迹 → 偏好对"的自监督式 DPO 数据构造思路，对其它细粒度稠密预测任务（如深度补全、缺陷检测、医学分割）具有借鉴意义。
- **实证强度**：在自建基准上对 15 个跨范式基线取得全面领先，且通过骨干/轮数/网格粒度/协议四组消融支撑了主要设计选择的合理性，实验框架较为完整；但受限于单主基准、缺少方差与显著性报告、部分基线配置自建，结论的普适性仍需外部独立复现验证。
- **适用边界**：更适合对**边界保真度与实例语义同时敏感**、且可接受多轮推理开销的场景（离线精修、专业修图辅助、数据集标注清洗），而非严格实时或超低功耗端侧部署。
- **未来方向**：(1) 在既有权威基准上补全主表并报告多次运行统计；(2) 探索更细/自适应网格与层次化动作空间；(3) 引入显式不确定性建模以自适应决定精修轮数，降低平均推理成本；(4) 扩展到视频时序一致性与 3D 一致性的高保真解析。
- **一句话总结**：Kiroshi 用"让 MLLM 决定在哪修、让动作模型决定怎么修"的分工，把全自动高保真图像解析推向可解释的闭环智能体范式，方向清晰、机制新颖，但证据的广度与统计严谨性仍有提升空间。

（完）
