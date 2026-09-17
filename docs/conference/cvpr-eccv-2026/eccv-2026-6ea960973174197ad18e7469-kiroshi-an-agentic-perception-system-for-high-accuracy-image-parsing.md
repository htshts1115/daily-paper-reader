---
title: "Kiroshi: An Agentic Perception System for High-Accuracy Image Parsing"
title_zh: Kiroshi：面向高精度图像解析的智能体感知系统
authors: "Haipeng ZHOU, Jinshan Liu, He Zhang, Xuequan Lu, Jun Ma, Lei Zhu"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2569.pdf"
tags: ["query:matting"]
score: 8.0
evidence: 用于高精度图像解析的自动抠图与分割智能体
tldr: 高精度抠图与分割比常规稠密预测更困难，需准确估计细粒度细节，而现有方法或缺乏语义感知，或依赖人工交互验证，难以实现全自动抠图。本文提出智能体感知系统 Kiroshi，训练带迭代精修的 Action Model，并从残差图中采样网格提示挖掘正负配对轨迹。该方法实现了全自动的高精度图像解析。这为免 trimap 抠图与细粒度前景分离提供了新的自动化范式。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-001.webp\", \"caption\": \"\", \"page\": 6, \"index\": 1, \"width\": 928, \"height\": 652}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 709, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 2747, \"height\": 1422}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-010.webp\", \"caption\": \"\", \"page\": 7, \"index\": 10, \"width\": 414, \"height\": 414}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-012.webp\", \"caption\": \"\", \"page\": 9, \"index\": 12, \"width\": 4418, \"height\": 3246}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-6ea960973174197ad18e7469/fig-013.webp\", \"caption\": \"\", \"page\": 9, \"index\": 13, \"width\": 4002, \"height\": 2784}]"
motivation: 高精度抠图与分割需细粒度细节，现有方法缺乏语义感知或依赖人工交互验证，难以全自动完成。
method: 提出智能体感知系统 Kiroshi，训练带迭代精修的 Action Model，并从残差图采样网格提示挖掘正负配对轨迹。
result: 实现全自动的高精度抠图与分割解析，减少人工验证与反复检查的负担。
conclusion: 为免 trimap 自动抠图与细粒度图像解析提供了智能体式新范式。
---

## Abstract
Parsing images with high precision for matting and segmentation is sig-nificantly more challenging than conventional dense prediction, as it requires accurateestimation of fine-grained details. Existing methods either lack semantic awareness orproduce suboptimal predictions; even interactive matting approaches rely on manualverification and repetitive checking, making fully automatic matting still unattainable.In this work, we propose Kiroshi , an agentic perception system for high-accuracyimage parsing. We train an Action Model with iterative refinement and mine pairedtrajectories by sampling grid prompts from residual maps, where each step yields apositive and a negative transition under the same intermediate prediction based onquantitative quality gains. These within-context preference pairs form a reliable su-pervision signal for post-training to align the MLLM policy toward more effectivegrid decisions. We also contribute a new High-Fidelity Referring Matting and Seg-mentation (HiFiRefMS ) benchmark to evaluate the performance of different mod-els. Experimental results demonstrate that our method surpasses state-of-the-art ap-proaches both quantitatively and qualitatively, and extensive ablation studies furthervalidate the effectiveness and superiority of our agentic design. Project will be releasedat https://github.com/haipengzhou856/Kiroshi.

---

## 论文详细总结（自动生成）

# Kiroshi：面向高精度图像解析的智能体感知系统——论文总结

## 1. 核心问题与整体含义

- **研究动机**：高精度图像解析（抠图与分割）比常规稠密预测困难得多，因为它需要准确估计细粒度细节（如毛发、透明效果、物体边界）。
- **现有方法的困境**：
  - **传统显著性抠图方法**：能保留细节（如绳索、毛发），但缺乏语义感知，在多实例场景中容易过度抠图或漏抠。
  - **交互式方法（如 ZIM、HQ-SAM）**：通过用户提示（点、框）可提取目标实例，但依赖频繁的人工干预与反复检查，无法实现全自动。
  - **MLLM 推理分割方法（如 LISA、SegAgent）**：语义对齐能力强，但受限于底层模型（如 SAM），预测掩码粗糙，无法恢复透明度和精细边界。
- **整体含义**：论文提出 Kiroshi，将高精度图像解析建模为**智能体感知问题**——系统不仅一次性输出结果，还能观察当前预测、判断不可靠区域、并迭代精修，从而在最小人工干预下实现全自动、语义感知的高精度掩码预测。

## 2. 方法论

### 2.1 核心思想

- 将任务建模为显式的**"规划-执行"马尔可夫决策过程（MDP）**，由两个协同组件构成：
  - **MLLM 策略生成器 P**：观察当前状态 $o_t = (I, X, s_t)$，输出区域级动作 $\tau_t$（可解码的文本网格图）：$\tau_t = \mathcal{P}(I, X, s_t)$。
  - **动作模型 A**：执行该动作，在像素级更新预测：$s_{t+1} = \mathcal{A}(I, s_t, \tau_t)$。
- 经 $T$ 步后输出最终结果 $\hat{s} = s_T$。MLLM 负责"**在哪精修、精修什么**"（语义可解释），动作模型负责"**如何精修**"（恢复高频细节与边界）。

### 2.2 网格感知动作模型（Grid-aware Action Model）

- **动机**：现有交互方法（ZIM、HQ-SAM）对负向提示不敏感，像素级点提示搜索空间大、冗余高、不稳定。
- **设计**：采用 **DINOv2 编码器 + Mask2Former 风格解码器**，将网格图作为注意力掩码 $M$ 引入 Transformer 解码器：
  - 注意力计算：$\mathbf{Z}_l = \mathrm{softmax}(M_{l-1} + \mathbf{Q}_l\mathbf{K}_l^\top)\mathbf{V}_l + \mathbf{Z}_{l-1}$
  - 掩码定义：网格内区域为 0，网格外为 $-\infty$。
- **优势**：将不稳定的像素级提示替换为一致的图块级交互；减少搜索空间；提供更丰富的语义与边界线索；天然契合智能体迭代精修框架。

### 2.3 轨迹挖掘策略（算法 1）

- 对每张图像执行 $K$ 次 rollout，每步采集一对网格轨迹 $(\tau_t^+, \tau_t^-)$：
  1. 计算误差图 $r_t = |Y - s_{t-1}|$；
  2. 对 $p \times p$ 网格块，若非零残差像素超过阈值 $\epsilon$（默认 40%），加入候选队列；
  3. 均匀采样 75% 的候选块构成轨迹 $\tau$；
  4. 转换为注意力掩码 $M$ 并输入动作模型，得到 $s_t^+$ 与 $s_t^-$；
  5. 用定量指标（如 MSE）比较质量增益 $\Delta_t^+ > 0 \land \Delta_t^- < 0$，分别标记为正/负样本。
- 产出**同状态下的正负偏好对** $(I, B, s_{t-1}, \tau^+, s^+)$ 与 $(I, B, s_{t-1}, \tau^-, s^-)$，为后续 DPO 提供干净监督信号。

### 2.4 赋能 MLLM 进行感知

- **将图像块视为可描述文本单元**：掩码被展平解析为 `<grid>` 特殊描述符，定义四种语义：
  - `<human>`（目标区域）、`<bg>`（背景）、`<unknown>`（需精修的不确定区域）、`<other>`（其他实例）。
- **行式游程编码（R-RLE）**：如一行含 64 个背景块表示为 `bg*64`（单 token），大幅压缩 token 长度，使微调高效轻量。
- `<unknown>` 区域通过标准腐蚀-膨胀三值图（trimap）推导得到。

### 2.5 后训练对齐（DPO）

- 采用 **直接偏好优化（DPO）**，避免依赖稀疏像素级奖励的强化学习：
  $$\mathcal{L}_{\mathrm{DPO}} = -\log \sigma\left(\beta\left[\log \mathcal{P}(\tau_+ \mid I, X) - \log \mathcal{P}(\tau_- \mid I, X)\right]\right)$$
- 每个精修步骤中，若 $\tau_t$ 带来提升则标为 preferred，否则为 rejected；并用 Qwen3-VL Plus 生成位置感知、语义接地的轨迹描述，组织为 VQA 式对话数据。

### 2.6 优化与推理

- 动作模型：$\ell_1$ 损失 + Laplacian 损失；MLLM：标准交叉熵损失。
- 推理：采用 **MLLM-as-Judge** 策略驱动多轮精修，默认 **3 轮**循环。

## 3. 实验设计

### 3.1 数据集与 Benchmark

- **新提出 HiFiRefMS 基准**（High-Fidelity Referring Matting and Segmentation）：
  - **抠图子集**：468 张图像 / 1187 个掩码（连续透明度值 0–1）。
  - **分割子集**：500 张图像 / 1366 个掩码（二值硬标签）。
  - 由公开数据集（P3M、AM-2K、AIM-500、DIS-5K、HIM-2K、MGMatting 等）重组、清洗、重新标注而成，重点覆盖**多实例场景**；透明物体从分割子集中剔除以避免标签不一致。
  - 文本描述由 Qwen3-VL Plus API 生成。
- **训练数据**：
  - SFT 阶段：RefCOCO 系列、RefMatte。
  - 动作模型：规模与 SmartMat 相当的公开抠图数据集 + DIS-5K + UHR-SOD。
  - DPO 阶段：约 40,000 对对话数据。

### 3.2 评估指标

- **抠图**：SAD、MSE、Grad（梯度失真）、Conn（连通性损失）。
- **分割**：maxFβ、Fβ、MAE、Sα、HCE（人工修正代价）。

### 3.3 对比方法（三大类）

- **显著性模型**：IS-Net、PGNet、HitNet、MVANet、DiffDIS。
- **交互式模型**：HQ-SAM、MAM、SmartMat、SDMatte、ZIM（除 MAM 外均提供 GT 框）。
- **MLLM 方法**：LISA、SAM4MLLM、Text4Seg、SegAgent。

## 4. 资源与算力

- 文中仅提及实验在 **NVIDIA A100（80GB）GPU** 上进行。
- **未明确说明**具体 GPU 数量、训练总时长、参数量规模等细节；论文表示更多细节见补充材料（Supplementary Material）。
- MLLM 主干为 **Ovis2.5-2B**（默认），动作模型编码器为 **DINOv2-Base**。

## 5. 实验数量与充分性

- **实验组数概览**：
  1. **主对比实验**（表 1）：与 14 个 SOTA 方法在分割与抠图两类指标上全面对比。
  2. **视觉对比**（图 7）：与 ZIM、DiffDIS、HQ-SAM、SegAgent 的定性比较。
  3. **MLLM 主干消融**（表 2）：4 种主干（Qwen2.5-VL-3B、InternVL3.5-2B、Qwen3-VL-2B、Ovis2.5-2B）。
  4. **策略配置消融**（表 3）：Vanilla box vs 1/3/5 轮精修。
  5. **网格尺寸消融**（表 4）：16×16、32×32、64×64。
  6. **跨数据集协议分析**（表 5）：HiFiRefMS 与合成数据集 RefMatte-Syn 上的 6 种配置对比，含推理时间测量。
  7. **交互有效性测试**（图 3）：ZIM 与 HQ-SAM 的人工干预效果对比。
- **充分性评估**：实验覆盖主对比、多维度消融、跨数据集泛化与效率分析，**较为充分**。
- **公平性**：交互式方法统一提供 GT 框（MAM 保留原始 referring 流程），MLLM 方法使用各自标准配置，对比相对客观。但需注意：不同类别方法获得的输入提示强度不同（GT 框 vs 文本），存在一定协议差异。

## 6. 主要结论与发现

- Kiroshi 在 HiFiRefMS 上取得**全面最优**：分割指标 maxFβ 0.875、Sα 0.866、HCE 1218；抠图指标 MSE 0.0263、SAD 26.34、Grad 23.71、Conn 13.48，均优于所有基线。
- **框驱动交互**提供强低层线索但存在框歧义（框内多个实例/背景泄漏）；**纯 referring 语义**可靠但精度不足。Kiroshi 结合区域级语义决策与迭代像素级精修，有效缓解二者缺陷。
- **网格图随迭代逐步移向边界与不确定区域**，验证智能体感知机制的必要性与有效性。
- 消融表明：3 轮精修、32×32 网格、Ovis2.5-2B 主干为最佳平衡配置；轮数过多收益递减，网格过细或过粗均降低性能。
- 跨数据集验证显示，智能体设计在真实与合成数据上均带来一致性提升，而外部拼装方案（如 Text4Seg + MGMatting）对迭代精修不敏感。

## 7. 优点

- **问题建模新颖**：将高精度解析从"单次稠密预测"转为"智能体感知闭环"，兼具语义可解释性与像素级精度。
- **网格级文本表示巧妙**：把图像块当作可描述 token，配合 R-RLE 压缩，将 MLLM 从低层像素感知中解放，专注区域级语义推理，显著降低 token 长度与对齐难度。
- **轨迹挖掘策略优雅**：在同一中间状态下自然生成正负偏好对，为 DPO 提供干净、可靠的监督信号，避免像素级奖励建模的困难。
- **实验体系完整**：主对比 + 多维消融 + 跨数据集 + 效率分析 + 视觉定性，论证链条完整。
- **新基准贡献**：HiFiRefMS 填补了真实场景多实例高保真 referring 抠图/分割评测的空白。
- **完全自动化**：仅需极简用户指令，无需重复人工验证。

## 8. 不足与局限

- **算力信息不透明**：未说明 GPU 数量、训练时长、总计算开销，难以评估复现成本与可扩展性。
- **基准规模有限**：HiFiRefMS 仅约 1000 张图像级别，覆盖场景多样性可能受限。
- **依赖外部组件**：文本描述生成依赖 Qwen3-VL Plus API；`<unknown>` 区域依赖 trimap 的腐蚀-膨胀，可能引入先验偏差。
- **推理效率**：3 轮精修耗时约 12.94 秒/图（表 5），高于单轮方案（7.42 秒），实时性受限。
- **超参敏感**：网格尺寸、精修轮数、残差阈值 $\epsilon$ 等

超参数需逐一调优（如 32×32 网格、3 轮精修、$\epsilon=40\%$），迁移到新数据集或新任务时可能需重新搜索，增加部署与复现成本。
- **依赖 MLLM 的语义先验**：轨迹生成完全由 MLLM 决策，若主干对复杂指代（如多实例中的细粒度属性、空间关系）理解错误，迭代精修可能收敛到错误区域，且缺乏显式纠错回退机制。
- **轨迹挖掘存在随机性**：算法 1 对候选块进行 75% 均匀采样，采样比例与阈值未做敏感性分析，正负样本质量可能受随机种子影响。
- **失败案例分析缺失**：论文未系统展示失败样例或误差归因，难以判断方法在极端场景（严重遮挡、透明叠加、多同类实例）下的边界。
- **实例混淆风险**：在多实例场景中，`<other>` 与 `<human>` 的区分依赖网格语义标注，若相邻实例边界在粗网格下落在同一块内，可能引入实例级混淆。
- **合成与真实域差异**：跨数据集协议虽验证了一致性提升，但 RefMatte-Syn 与 HiFiRefMS 的域间隙仍可能掩盖真实场景中的泛化问题。

## 9. 潜在改进方向与启示

- **效率优化**：可引入早停机制（如残差低于阈值即终止）或轻量化动作模型，以降低 3 轮精修的推理开销；也可探索并行化多区域精修。
- **监督信号增强**：当前 DPO 偏好对来自单步增益比较，未来可引入多步回报或过程奖励，进一步稳定长程精修轨迹。
- **网格自适应**：固定 $p \times p$ 网格可替换为内容自适应划分（如基于超像素或边缘密度），在细节密集区域使用更细粒度、平坦区域使用粗粒度。
- **基准扩展**：HiFiRefMS 可进一步扩大规模并增加视频、3D 或交互式编辑场景，以检验智能体感知框架的通用性。
- **组件解耦**：将 `<unknown>` 的 trimap 推导替换为可学习的不确定性估计，减少对腐蚀-膨胀先验的依赖。
- **与更强基座结合**：动作模型与 MLLM 主干均可替换为更大规模模型，验证性能上限与缩放规律。

## 10. 总体评价

Kiroshi 的核心贡献在于**范式转换**：将高精度图像解析从"单次稠密预测"重构为"语义规划 + 像素执行"的智能体闭环，并通过网格级文本动作空间、轨迹挖掘与 DPO 对齐，巧妙弥合了 MLLM 的语义能力与抠图/分割模型的高频细节恢复能力之间的鸿沟。其提出的 HiFiRefMS 基准与完整的消融体系为后续研究提供了可复现的评测基础。尽管在算力透明度、基准规模、推理效率与超参敏感性上仍有提升空间，但该方法在"全自动、语义感知、高保真"三者之间取得了目前较为均衡的折中，对 referring matting/segmentation 及更广泛的智能体视觉感知研究具有明确的启发意义。

（完）
