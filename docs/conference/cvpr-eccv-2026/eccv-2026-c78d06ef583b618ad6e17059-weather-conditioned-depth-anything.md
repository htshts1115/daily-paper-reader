---
title: Weather-Conditioned Depth Anything
title_zh: 天气条件化的Depth Anything
authors: "Zhaoming Xu, Chan-Wei Hu, Kuan-Ru Huang, Zihao Zhu, Renjie Li, Yang Zhou, Zhengzhong Tu"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11783.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 改进Depth Anything基础模型的恶劣天气鲁棒性
tldr: 以Depth Anything系列为代表的单目深度估计基础模型在雾、雨、雪、夜间等恶劣天气下会出现严重失效。本文提出天气条件化的Depth Anything（DA-W）框架，通过风格过滤提取与内容无关的退化感知天气嵌入，并用零初始化适配器以参数高效的方式注入Depth Anything骨干。该轻量调制使单一统一模型能适应多种天气。实验表明其在恶劣天气下显著提升深度估计鲁棒性，扩展了深度基础模型的适用范围。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-016.webp\", \"caption\": \"\", \"page\": 1, \"index\": 16, \"width\": 576, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 1200, \"height\": 589}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 1146, \"height\": 562}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 484, \"height\": 428}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 385, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 391, \"height\": 392}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-022.webp\", \"caption\": \"\", \"page\": 6, \"index\": 22, \"width\": 385, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-023.webp\", \"caption\": \"\", \"page\": 6, \"index\": 23, \"width\": 385, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-024.webp\", \"caption\": \"\", \"page\": 6, \"index\": 24, \"width\": 385, \"height\": 388}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-025.webp\", \"caption\": \"\", \"page\": 6, \"index\": 25, \"width\": 1402, \"height\": 685}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-026.webp\", \"caption\": \"\", \"page\": 6, \"index\": 26, \"width\": 961, \"height\": 546}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-027.webp\", \"caption\": \"\", \"page\": 10, \"index\": 27, \"width\": 784, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-028.webp\", \"caption\": \"\", \"page\": 10, \"index\": 28, \"width\": 784, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-029.webp\", \"caption\": \"\", \"page\": 10, \"index\": 29, \"width\": 784, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-030.webp\", \"caption\": \"\", \"page\": 10, \"index\": 30, \"width\": 784, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-031.webp\", \"caption\": \"\", \"page\": 10, \"index\": 31, \"width\": 784, \"height\": 588}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-032.webp\", \"caption\": \"\", \"page\": 10, \"index\": 32, \"width\": 784, \"height\": 588}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-033.webp\", \"caption\": \"\", \"page\": 10, \"index\": 33, \"width\": 784, \"height\": 588}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-034.webp\", \"caption\": \"\", \"page\": 10, \"index\": 34, \"width\": 784, \"height\": 588}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-035.webp\", \"caption\": \"\", \"page\": 14, \"index\": 35, \"width\": 1682, \"height\": 1396}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-036.webp\", \"caption\": \"\", \"page\": 14, \"index\": 36, \"width\": 1682, \"height\": 1404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-037.webp\", \"caption\": \"\", \"page\": 14, \"index\": 37, \"width\": 1682, \"height\": 1404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-038.webp\", \"caption\": \"\", \"page\": 14, \"index\": 38, \"width\": 1682, \"height\": 1354}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-039.webp\", \"caption\": \"\", \"page\": 14, \"index\": 39, \"width\": 1680, \"height\": 1402}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-040.webp\", \"caption\": \"\", \"page\": 14, \"index\": 40, \"width\": 1680, \"height\": 1400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-041.webp\", \"caption\": \"\", \"page\": 14, \"index\": 41, \"width\": 1680, \"height\": 1408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-042.webp\", \"caption\": \"\", \"page\": 14, \"index\": 42, \"width\": 1682, \"height\": 1406}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-043.webp\", \"caption\": \"\", \"page\": 14, \"index\": 43, \"width\": 1682, \"height\": 1404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-044.webp\", \"caption\": \"\", \"page\": 14, \"index\": 44, \"width\": 1682, \"height\": 1404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-045.webp\", \"caption\": \"\", \"page\": 15, \"index\": 45, \"width\": 4144, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c78d06ef583b618ad6e17059/fig-046.webp\", \"caption\": \"\", \"page\": 15, \"index\": 46, \"width\": 6888, \"height\": 518}]"
motivation: Depth Anything等深度基础模型在雾雨雪夜间等恶劣天气下会出现严重失效。
method: 提出DA-W框架，用风格过滤提取退化感知天气嵌入，并通过零初始化适配器注入Depth Anything骨干。
result: 单一统一模型可适应多种天气，在恶劣条件下显著提升深度估计鲁棒性。
conclusion: 以轻量调制扩展了深度基础模型在真实复杂天气下的适用性。
---

## Abstract
Monocular depth estimation foundation models, such as the Depth Anything series, have achieved remarkable performance across diverse domains. However, they still suffer from critical failures under adverse weather conditions, such as fog, rain, snow, or at night. To address this, we present Weather-Conditioned Depth Anything (DA-W), a framework that explicitly disentangles style from content for weatherrobust depth estimation. Specifically, we introduce a Style Filter trained on a curated mix of real and synthetic degradation datasets to extract content-independent, degradation-aware weather embeddings. This style embedding is then injected into the Depth Anything backbone using a parameter-efficient, zero-initialized adapter. Such a lightweight modulation allows a single unified model to robustly adapt to diverse conditions—including fog, rain, snow, and low-light—while avoiding catastrophic forgetting of its core generalization abilities in normal conditions. We train the adapter using a pseudo-label distillation and alignment strategy. Our comprehensive experiments demonstrate that our proposed DA-W achieves state-of-the-art robust depth estimation, improving AbsRel by an average of 3.7% on our curated weather benchmarks, while matching or slightly outperforming performance on standard clean benchmarks.

---

## 论文详细总结（自动生成）

# Weather-Conditioned Depth Anything（DA-W）论文总结

## 1. 核心问题与整体含义

- **研究动机**：单目深度估计（MDE）基础模型（如 Depth Anything 系列）在多样场景下表现优异，但在雾、雨、雪、夜间等恶劣天气下会出现严重失效。原因是大气散射、遮挡、镜面伪影和低光噪声从根本上改变了图像外观。
- **现有方法的两类局限**：
  - **两阶段预处理**：先用扩散/统一复原模型去天气，再估计深度；但复原目标偏向感知质量而非几何精度，常破坏关键深度线索，且易过拟合特定下游模型。
  - **天气感知训练**：将鲁棒性直接纳入深度模型（如 WeatherDepth、md4all、DepthAnything-AC）；但真实恶劣天气下的标注深度数据极难获取，主流做法依赖合成退化数据，存在合成到真实的泛化鸿沟。
- **关键洞察（论文核心诊断）**：作者提取 Depth Anything v2 编码器的 [CLS] token 并做 t-SNE 可视化，发现不同天气（雾、雨、雪）的特征严重混杂、无法分离。模型将天气风格与场景几何纠缠在单一表示中，无法区分“外观变化源于天气还是场景本身”，这正是鲁棒性脆弱的根因。
- **整体含义**：论文主张显式解耦“风格（天气）”与“内容（场景几何）”，用天气条件化调制来提升深度估计的鲁棒性，同时不牺牲干净场景的泛化能力。

## 2. 方法论

- **核心思想**：设计一个风格过滤器（Style Filter）提取与内容无关、退化感知的天气嵌入，再通过参数高效、零初始化的 AdaLN-Zero 适配器将嵌入注入冻结的 Depth Anything 骨干（仅作用于 DPT 解码器），实现单一统一模型适应多种天气。
- **关键技术细节**：
  - **天气嵌入**：给定图像 $I$，风格过滤器 $F_\theta$ 输出紧凑天气嵌入 $w \in \mathbb{R}^{64}$，要求其既具天气判别性（同天气不同场景嵌入相近、同场景不同天气嵌入相异），又具域对齐性（同一天气的真实与合成样本落在潜空间同一区域）。
  - **风格过滤器设计**：基于多尺度 Gram 矩阵提取风格统计，通过对比损失训练。
    - 对比损失形式：对批次内所有图像对，同类天气的嵌入余弦相似度需超过正间隔 $m$，异类则被推远；损失为 $\sum_{(a,b)}[\mathbb{I}_{ab}[m-d_{ab}]_+ + (1-\mathbb{I}_{ab})d_{ab}]$。
    - **跨域对齐**：将“同一天气的真实-合成对”也视为正样本，不同于 MWFormer 只考虑域内配对，从而学到统一的天气嵌入空间。
    - **负面尝试**：作者也试过 CLIP 风格的 prompt-driven 与 image-image 对齐变体，但因 CLIP 特征偏语义、对物理驱动的低层线索不敏感，真实与合成同天气样本仍可分离，故未采用。
  - **天气条件化注入**：64 维天气嵌入 $w$ 在 4 个多尺度特征图（各降至 64 通道）和最终融合特征前共 5 个位置注入。轻量 MLP 将 $w$ 映射为逐通道的 shift $\beta_i$、scale $\gamma_i$ 和 gate $g_i$，按 AdaLN-Zero 方式更新特征：$F_i \leftarrow F_i + g_i(w)(\mathrm{LN}(F_i)\odot(1+\gamma_i(w)) + \beta_i(w))$。所有调制头零初始化，保证初始输出与基座模型一致。
  - **参数高效训练**：从预训练 Depth Anything 初始化，仅更新 DPT 解码器头和少量调制头，冻结编码器，防止表征漂移与灾难性遗忘。
- **损失函数（仿射不变损失 $\ell$ 定义在视差图上）**：
  - **蒸馏损失 $\mathcal{L}_{dist}$**：学生（ViT-S）对齐冻结教师（ViT-L）的伪标签；对合成天气图像，以对应干净图像的教师预测为目标。
  - **配对对齐损失 $\mathcal{L}_{pair}$**：对共享几何的干净-合成对，约束学生两次预测一致。
  - **增强一致性损失 $\mathcal{L}_{aug}$**：对无干净配对真实天气图像，施加保几何的外观变换（ColorJitter），约束一致性。
  - **总目标**：$\mathcal{L} = \mathcal{L}_{dist} + \mathcal{L}_{pair} + \mathcal{L}_{aug}$。
- **训练流程（两阶段）**：Stage I 在真实+合成混合数据上训练风格过滤器；Stage II 优化 DPT 解码器头与 AdaLN-Zero 调制层，训练 20 epoch，AdamW，学习率 5e-6，权重衰减 0.01，batch size 16。

## 3. 实验设计

- **数据集/场景**：
  - **风格过滤器训练数据**：7 个真实恶劣天气数据集（ACDC、RTTS、Snow100K、Muses、RID、RIS、NightCity），约 15K 图像，覆盖雾/雨/雪/低光；4 个干净数据集（COCO、MegaDepth、SA-1B、HRWSI），约 200K 图像（Stage I 均匀下采样 20K 平衡）。
  - **合成退化**：参照 RobustSAM 配方，对干净图像生成配对合成天气视图。
  - **深度监督**：使用数据集提供的有效性掩码，否则用 Lang-SAM 生成天空掩码排除。
- **Benchmark**：
  - **真实恶劣天气**：NuScenes-night、RobotCar-night、DrivingStereo-rain/cloud/fog。
  - **合成天气损坏**：KITTI-C（Dark、Snow、Fog、Motion）。
  - **混合天气**：在 KITTI Eigen split 上用 RoboDepth 组合 11 种多天气组合（5 个严重等级），另有 Boreas 夜间+雪的真实定性评估。
  - **干净域**：KITTI、NYU-Depth v2、Sintel、ETH3D、DIODE。
- **评价指标**：AbsRel（越低越好）、δ1（越高越好），遵循 DepthAnything-AC 协议。
- **对比方法**：DynaDepth、EC-Depth、STEPS、robustdepth、weather-depth、Syn2Real、DepthPro、DepthAnything v1/v2/v3、DepthAnything-AC、MWFormer+DA v2、DarkIR+DA v2。
- **消融实验**：微调策略（全量 vs 仅解码器）、数据组成（是否含真实退化）、天气注入（是否启用 AdaLN）、损失项（$\mathcal{L}_{dist}$/$\mathcal{L}_{pair}$/$\mathcal{L}_{aug}$）、RGB 复原基线、全量微调对比。

## 4. 资源与算力

- 论文明确说明：**所有实验在单张 NVIDIA A100 GPU 上完成**。
- 训练配置：20 epochs，AdamW，学习率 5e-6，权重衰减 0.01，batch size 16。
- 致谢提到 GPU 硬件由 Texas A&M University 通过 **NVIDIA Academia Grant Program** 提供。
- 未提及具体训练时长、GPU 显存占用或多卡扩展性等信息。

## 5. 实验数量与充分性

- **实验组数**：包含 6 张主要表格（Table 1–6）和多张定性图（Fig. 1–7），覆盖真实恶劣天气（5 个数据集）、合成损坏（4 类）、混合天气（11 种组合）、干净域（5 个数据集）以及多组消融。
- **充分性**：
  - 覆盖真实与合成、单一天气与混合天气、恶劣与干净场景，维度较全面。
  - 消融较系统：分别验证了微调策略、真实数据引入、天气注入、各损失项贡献、RGB 复原对照。
  - 与多种强基线（含 DA 系列、复原式两阶段管线、专用天气方法）对比，并给出平均排名（Avg. rank）以减少单指标偏差。
- **客观与公平性**：
  - 采用统一评价协议（DepthAnything-AC），指标标准化（Fig. 2 基线归一化）。
  - 消融表 6 明确说明所有行使用相同数据子集、种子与评价协议。
  - 部分数据（如 MWFormer 在 NuScenes-night、RobotCar-night）标注为“–”（不可得），处理较诚实。
- **潜在不足**：混合天气的真实子集（Boreas 夜间+雪）仅为定性评估，缺乏定量指标；RobotCar-night 上未达最优，说明覆盖面仍有空白。

## 6. 主要结论与发现

- DA-W 在真实恶劣天气基准（NuScenes-night、DS-rain）上取得 DepthAnything 家族内最佳鲁棒性，AbsRel 与 δ1 均优于 DA v2 和 DA-AC。
- 在合成 KITTI-C 上，Dark、Snow、Motion 取得最优，Fog 具有竞争力；相较 DA v2 在所有设置上均有提升，Snow 增益最大。
- 在干净域基准上保持甚至小幅超越基座模型（KITTI、Sintel 有增益，ETH3D 持平），证明零初始化 AdaLN 解码器侧调制能避免灾难性遗忘。
- 混合天气组合（如雨夜、雪夜、雾+雨+雪+夜）上，DA-W 在大多数轨道上一致提升 δ1 与 AbsRel。
- 损失消融显示：移除 $\mathcal{L}_{dist}$ 导致最大退化（Global AbsRel 从 0.117 升至 0.352），说明教师蒸馏是几何锚定的关键；$\mathcal{L}_{pair}$ 有小幅稳定增益；$\mathcal{L}_{aug}$ 无独立可测增益，更宜视为真实天气一致性正则。
- 特征调制分析表明：夜间暗区、雾天纹理丰富区的调制差异更强，说明天气条件化能自适应聚焦于退化最严重区域，且无需显式空间监督。

## 7. 优点

- **问题诊断深入**：用 t-SNE 实证揭示 DA v2 [CLS] token 的天气-内容纠缠问题，为方法设计提供了清晰动机。
- **解耦思路明确**：显式分离风格（天气）与内容（几何），风格过滤器同时追求天气判别性与真实-合成域对齐，切中合成到真实迁移的核心痛点。
- **参数高效且安全**：仅训练解码器头与少量 AdaLN 调制头，编码器冻结，零初始化保证初始等价于基座模型，有效防止灾难性遗忘。
- **无需推理时预处理**：相比两阶段复原管线，避免额外预处理与误差累积，推理更简洁高效。
- **实验维度全面**：真实/合成、单一/混合天气、干净域全覆盖，并引入平均排名指标，结论较有说服力。
- **诚实的负面结果报告**：报告了 CLIP 变体失败、DS-fog 增益有限、RobotCar-night 不占优等，增强可信度。

## 8. 不足与局限

- **模型规模覆盖有限**：受控适应实验仅基于 DA-v2-S（ViT-S），向更大 Depth Anything 变体及其他深度基础模型扩展需匹配的适配头与优化设置，尚未验证。
- **真实夜间场景仍具挑战**：RobotCar-night 上 DA v3、DepthPro 表现明显更好，说明相机响应、曝光动态、运动模糊和场景分布偏移等非天气因素未被建模，是当前天气条件化调制的盲区。
- **部分天气增益不均衡**：DS-cloud、DS-fog 未达最优；合成 Fog 上增益较小；消融显示 DS-fog 在启用天气注入后略有下降，说明并非所有退化都同等受益。
- **真实混合天气缺乏定量评估**：Boreas 夜间+雪仅提供定性结果，混合天气真实子集的定量覆盖不足。
- **损失项冗余**：$\mathcal{L}_{aug}$ 在消融中无独立可测增益，其必要性存疑。
- **风格过滤器依赖数据混合**：需要精心构建的真实+合成混合数据集与退化算子，跨数据集偏差风险存在；对未见天气类型（如沙尘、冰雹）的泛化未讨论。
- **算力信息不完整**：仅提及单张 A100，未报告训练时长、显存与可复现性细节。

（完）
