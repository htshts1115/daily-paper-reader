---
title: Learning Accurate Segmentation Purely from Self-Supervision
title_zh: 纯自监督学习准确分割
authors: "Zuyao You, Zuxuan Wu, Yu-Gang Jiang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/3472.pdf"
tags: ["query:seg"]
score: 6.0
evidence: 从原始图像自监督地进行前景背景分离
tldr: 无标注地准确分割目标一直是计算机视觉的难题。本文提出Selfment自监督框架，从原始图像出发，先用自监督特征构建块级亲和图并应用NCut得到粗略前景背景分离，再通过迭代块优化逐步增强空间一致性与语义一致性，最后用精炼掩码作为监督训练轻量分割器。该工作无需人工标注或预训练分割模型，即可实现前景分割，对前景提取类任务具有参考价值。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 2570, \"height\": 842}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 999, \"height\": 745}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 1072, \"height\": 603}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 1072, \"height\": 603}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 1028, \"height\": 808}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-006.webp\", \"caption\": \"\", \"page\": 4, \"index\": 6, \"width\": 1072, \"height\": 603}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-007.webp\", \"caption\": \"\", \"page\": 4, \"index\": 7, \"width\": 1094, \"height\": 887}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-008.webp\", \"caption\": \"\", \"page\": 4, \"index\": 8, \"width\": 1099, \"height\": 891}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-009.webp\", \"caption\": \"\", \"page\": 4, \"index\": 9, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-010.webp\", \"caption\": \"\", \"page\": 8, \"index\": 10, \"width\": 2836, \"height\": 1545}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-011.webp\", \"caption\": \"\", \"page\": 9, \"index\": 11, \"width\": 2249, \"height\": 1570}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-012.webp\", \"caption\": \"\", \"page\": 11, \"index\": 12, \"width\": 1830, \"height\": 1168}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-013.webp\", \"caption\": \"\", \"page\": 12, \"index\": 13, \"width\": 2134, \"height\": 1445}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-dd5ad9d745665ec0050e75b4/fig-014.webp\", \"caption\": \"\", \"page\": 13, \"index\": 14, \"width\": 2296, \"height\": 1488}]"
motivation: 在无任何人工标注下准确分割目标仍是计算机视觉的核心难题。
method: 提出Selfment框架，用块级亲和图与NCut初始化前景背景分离，再以迭代块优化精炼掩码训练轻量分割器。
result: 方法无需标注或预训练分割模型即可完成前景分割，并保持空间与语义一致性。
conclusion: 该工作展示了纯自监督前景分割的可行性，可为前景提取任务提供通用思路。
---

## Abstract
Accurately segmenting objects without any manual anno-tations remains one of the core challenges in computer vision. In thiswork, we introduce Selfment, a fully self-supervised framework that seg-ments foreground objects directly from raw images without human labels,pretrained segmentation models, or any post-processing. Selfment firstconstructs patch-level affinity graphs from self-supervised features and ap-plies NCut to obtain an initial coarse foreground-background separation.We then introduce Iterative Patch Optimization (IPO), a feature-space refinement procedure that progressively enforces spatial coherenceand semantic consistency through iterative patch clustering. The refinedmasks are subsequently used as supervisory signals to train a lightweightsegmentation head with contrastive and region-consistency objectives,allowing the model to learn stable and transferable object representations.Despite its simplicity and complete absence of manual supervision, Self-ment sets new state-of-the-art (SoTA) results across multiple benchmarks.It achieves substantial improvements on Fmax over previous unsupervisedsaliency detection methods on ECSSD (+4.0\%), HKUIS (+4.6\%), andPASCAL-S (+5.7\%). Moreover, without any additional fine-tuning, Self-ment demonstrates remarkable zero-shot generalization to camouflagedobject detection tasks (e.g., .910 S m on CHAMELEON and .792 \protect \mathcal {F} { x0008 eta }^{\omega }on CAMO), outperforming all existing unsupervised approaches andeven rivaling the SoTA fully supervised methods. Codes and weights areavailable at: https://geshang777.github.io/Selfment/.

---

## 论文详细总结（自动生成）

# Selfment 论文中文总结

## 1. 核心问题与研究动机

- **核心问题**：能否在**完全没有人工标注、没有预训练分割模型、没有后处理**的条件下，直接从无标注图像中学习准确的目标分割？
- **背景痛点**：
  - 传统分割依赖密集人工掩码标注，成本高、耗时长、受人类归纳偏置影响。
  - 弱监督方法（点、涂鸦、运动轨迹）虽降低标注量，但仍依赖人工信号。
  - 近期方法常依赖 SAM 等现成分割模型做伪标签或提示适配，引入外部先验，削弱了"真自监督"程度。
  - 已有基于自监督特征的方法（如 TokenCut）虽能用 NCut 发现物体，但二分结果不稳定、掩码粗糙，通常需 CRF、双边求解器或形态学等重后处理。
- **整体含义**：论文提出 **Selfment**，一个完全自监督的前景分割框架，借助 DINOv3 等自监督基础模型的密集语义特征，把"特征相似性"转化为可靠的前景/背景分割，证明高质量目标分割可完全由自监督实现。

## 2. 方法论

### 核心思想
将自监督 ViT 的 patch 特征视为图节点，先用 NCut 得到粗略前景/背景二分，再用 **迭代块优化（IPO）** 在特征空间中逐步细化掩码，最后以细化掩码为伪标签训练一个轻量分割头。

### 关键技术细节

- **（1）构图与 NCut 初始二分**
  - 对 patch 特征 $f_i$ 构建无向加权图，亲和度：
    - 若内积 $\langle f_i, f_j\rangle > \tau$（$\tau=0.2$）取该内积，否则取小常数 $\epsilon$ 保证连通。
  - NCut 目标最小化组间相似度、保持组内高亲和，等价于求解广义特征值问题 $(D-A)x = \lambda D x$。
  - 取**第二小特征向量（Fiedler 向量）** $x_2$ 定义最优二分；以 $x_2$ 的均值为阈值得到二值掩码。
  - 取包含"种子 patch"（$x_2$ 绝对值最大处）的连通分量作为主目标掩码。

- **（2）迭代块优化（IPO）**
  - 对所有 patch 嵌入做 L2 归一化。
  - 由 NCut 结果计算前景/背景初始质心 $\mu_f^{(0)},\mu_b^{(0)}$。
  - 每次迭代：按 patch 与两质心的相似度大小重新分配标签（更接近前景质心则标为前景），随后重算质心；重复固定 $T=20$ 次。
  - **方向一致性约束**：保留参考向量 $r=\mu_f^{(0)}-\mu_b^{(0)}$，若新质心差与 $r$ 内积为负则反转标签，避免标签翻转与退化解。
  - 该步骤仅依赖特征相似性，无外部先验，显著提升空间一致性与语义一致性。

- **（3）自监督训练轻量分割头**
  - 结构：两层投影头（含 ReLU）将 patch 特征映射到嵌入空间，再接二分类器输出前景/背景 logits。
  - 损失由三部分加权组合：
    - **对比损失（InfoNCE）**：拉近同区域 patch 嵌入、推远异区域 patch 嵌入。
    - **软 Dice 损失**：促进分割空间紧凑与边界完整。
    - **BCE 损失**：每个 patch 预测其伪标签。
  - 总损失 $\mathcal{L}_{total}=\lambda_{con}\mathcal{L}_{con}+\lambda_{Dice}\mathcal{L}_{Dice}+\lambda_{BCE}\mathcal{L}_{BCE}$，权重分别为 0.1、1.0、1.0。

## 3. 实验设计

- **任务与数据集**：
  - **无监督显著性检测**：ECSSD、DUTS、HKUIS、PASCAL-S，指标 Fmax、IoU、像素精度 Acc。
  - **伪装目标检测（COD，零样本）**：CHAMELEON、CAMO、COD10K、NC4K，指标 S-Measure（Sm）、Weighted F-Measure（Fωβ）、E-Measure（Eξ）、MAE。
- **对比方法**：
  - 显著性：HS、wCtr、WSC、DeepUSPS、BigBiGAN、E-BigBiGAN、LOST、TokenCut、SelfMask、FOUND（均无后处理，统一推理分辨率 768×768 与 1280×1280）。
  - COD：全监督（BGNet、SINetv2、ZoomNet、FSPNet、BiRefNet）、半监督（CamoTeacher、SCOD-ND）、无监督（BigBiGAN、TokenCut、SelfMask、UCOS-DA、UCOD-DPL）。
- **实现设置**：DINOv3-7B 冻结；从 DUTS 训练集随机采样 1,000 张作自监督语料；图像缩放至 768×768；Adam，lr=1e-3，训练 3 epoch；缓存 backbone 特征加速。

## 4. 资源与算力

- **GPU**：8× NVIDIA A100（80G），使用 PyTorch DistributedDataParallel 分布式训练。
- **训练时长**：3 个 epoch 仅需 **27.6 分钟**。
- **可训练参数**：分割头仅 **0.54M** 参数，单次前向 **1.08M FLOPs**；backbone 全程冻结。
- **推理效率**：单张 A100 处理 768×768 图像，缓存特征时 0.029s，不缓存时 1.915s（对比 TokenCut+DINOv3-7B 为 5.087s）。
- 论文对算力描述较为明确。

## 5. 实验数量与充分性

- **主要实验**：表 1（4 个显著性数据集 × 3 指标，含两种分辨率）、表 2（4 个 COD 数据集 × 4 指标，跨全监督/半监督/无监督多类方法）。
- **消融实验**：
  - 主流程逐步累加（NCut → +IPO → +自监督训练 → +Dice → +对比损失），见表 3。
  - Backbone 对比（DINO-Base、DINOv3-Huge+、DINOv3-7B，跨 4 个数据集，图 5）。
  - 输入分辨率影响（768/1536/2560，图 8）。
  - 初始二分方法对比（<CLS> token、K-means、NCut，表 4）。
  - 泛化到非 DINO backbone（PE-Spacial、TIPSv2，表 5）。
  - 计算效率对比（表 6）。
- **充分性评价**：实验覆盖面较广，包含多任务、多数据集、多 backbone、多分辨率及组件消融，论证较充分。
- **公平性**：强调所有方法**均无后处理**、在相同 backbone 与相同推理分辨率下比较、消融固定采样种子并严格控制变量，公平性较好。部分消融（如表 3）使用 ECSSD 与 500 张 DUTS 子集，属于"敏捷迭代"设定，但与主实验配方保持一致。

## 6. 主要结论与发现

- Selfment 在无监督显著性检测上全面超越已有方法，Fmax 提升：**ECSSD +4.0%、DUTS +7.0%、HKUIS +4.6%、PASCAL-S +5.7%**。
- 零样本 COD 表现突出：Sm 达 **.910（CHAMELEON）、.869（CAMO）、.873（COD10K）、.902（NC4K）**，超越所有无监督方法，部分指标甚至超过全监督方法（如 CAMO 上 Sm .869 超过 FSPNet）。
- **随推理分辨率升高性能持续提升**（如 1280×1280 优于 768×768），而 TokenCut 等在高分辨率下因 NCut 不稳定而退化；Selfment 虽仅在 768×768 训练，却能自然泛化到 2048×2048/2560×2560。
- IPO 贡献显著：Fmax +4.8%、IoU +9.3%、Acc +1.6%，约 10 次迭代即收敛。
- 自监督训练（仅 BCE）即把 Fmax 从 79.5% 提升至 88.3%，加入对比与 Dice 损失进一步提升。
- 除 Selfment 外，其他方法（TokenCut、SelfMask、FOUND）**未能从模型规模扩大中获益**，FOUND 用 DINOv3-7B 甚至训练失败；Selfment 在不同 backbone 下均稳定有效。
- NCut 是优于 K-means 和 <CLS> token 的初始二分方法。

## 7. 优点

- **完全自监督**：无需人工标注、无 SAM 等外部分割先验、无任何后处理，真正实现端到端无监督分割。
- **方法简洁有效**：IPO 仅基于特征相似性的迭代聚类，思路简单但收益显著，且易于跨 backbone 迁移（DINO、DINOv3、PE、TIPSv2 均有效）。
- **分辨率可扩展**：突破 NCut 单次二分在高分辨率下的不稳定性，随输入分辨率提升质量持续改善。
- **强零样本泛化**：无任务微调即可在伪装目标检测这一困难任务上媲美全监督方法。
- **高计算效率**：仅训练 0.54M 参数的轻量头，3 epoch / 27.6 分钟完成训练，特征缓存后推理 0.029s/图。
- **实验公平性**：统一分辨率、统一无后处理、严格控制变量，backbone 对比充分。

## 8. 不足与局限

- **论文未设专门的 Limitations 章节**，以下部分为基于正文证据的推断：
  - **依赖大型强 backbone**：核心效果建立在 DINOv3-7B 等大模型特征之上；对特征质量较弱的 backbone（如 TIPSv2 B/14）提升后 Fmax 仅 88.7%，仍受 backbone 表征能力制约。
  - **仅做二分类前景/背景**：方法针对显著/前景目标，未涉及多类语义分割或实例级区分，泛化到通用多类分割的能力未验证。
  - **COD 上并非全面最优**：在 MAE、Eξ 等指标上仍落后部分全监督方法（如 CHAMELEON MAE .025 vs BiRefNet .016），Fωβ 亦逊于全监督 SoTA，说明边界精度仍有差距。
  - **训练语料规模小且单一**：仅用 1,000 张 DUTS 图像，可能带来数据集偏置（偏向显著性场景），对分布外场景的鲁棒性未充分讨论。
  - **高分辨率成本**：NCut 涉及特征值求解，高分辨率亲和图的计算与内存开销随 patch 数增长，论文未详述极端分辨率下的复杂度与失败案例。
  - **缺乏失败案例分析**：未系统报告在复杂多目标、重叠物体或非显著物体场景下的表现，偏差风险与适用边界尚不清晰。

（完）
