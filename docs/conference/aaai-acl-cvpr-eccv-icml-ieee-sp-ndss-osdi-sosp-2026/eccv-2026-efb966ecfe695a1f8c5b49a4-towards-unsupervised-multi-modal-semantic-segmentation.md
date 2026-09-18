---
title: Towards Unsupervised Multi-modal Semantic Segmentation
title_zh: 面向无监督多模态语义分割
authors: "Haitian Zhang, Thai Nguyen, Xiangyuan Wang, Mohan Liu, Addison Wang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2669.pdf"
tags: ["query:seg"]
score: 4.0
evidence: 无监督多模态语义分割
tldr: 多模态语义分割对复杂环境鲁棒感知很重要，但人工标注成本高昂制约其发展。将单模态无监督分割直接扩展到多模态会遭遇融合退化，因为无显式监督时框架难以协调不同传感器的异构结构模式。本文首次提出无监督多模态语义分割问题，设计方法有效利用互补传感器信息，为降低标注依赖的多模态分割开辟新方向。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-efb966ecfe695a1f8c5b49a4/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 2226, \"height\": 1172}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-efb966ecfe695a1f8c5b49a4/fig-002.webp\", \"caption\": \"\", \"page\": 8, \"index\": 2, \"width\": 1016, \"height\": 492}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-efb966ecfe695a1f8c5b49a4/fig-003.webp\", \"caption\": \"\", \"page\": 8, \"index\": 3, \"width\": 470, \"height\": 462}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-efb966ecfe695a1f8c5b49a4/fig-004.webp\", \"caption\": \"\", \"page\": 8, \"index\": 4, \"width\": 456, \"height\": 473}]"
motivation: 多模态语义分割受限于高昂标注成本，而无监督方法直接扩展到多模态会遭遇融合退化。
method: 首次提出无监督多模态语义分割问题，设计框架在无监督下有效利用互补传感器信息。
result: 缓解异构结构模式的融合退化，提升无监督多模态分割的表现。
conclusion: 为无监督多模态语义分割开辟新方向，降低对人工标注的依赖。
---

## Abstract
Multi-modal semantic segmentation (MSS) is essential forrobust perception in complex environments, yet its potential remainslargely untapped due to the prohibitive cost of human annotations. Whileunsupervised semantic segmentation (USS) has seen success on single RGBmodality, its naive extension to multi-modal data is hamperedby fusion degradation. This is because, in the absence of explicitsupervision, existing frameworks struggle to reconcile the heterogeneousstructural patterns captured by different sensors, failing to effectivelyexploit their complementary information. In this paper, we make thefirst attempt to address the novel problem of Unsupervised Multi-modal Semantic Segmentation (UMSS), aiming to effectively exploitcomplementary sensor information in a fully label-free setting. To thisend, we propose UniM2 (Unified Multi-Modal), a novel frameworkbuilt upon DINOv3 that transforms conventional fusion methods intoconsistent performance gains. Our key idea is to learn a unified latentspace driven by Cross-modal Correspondence Synergy (CMCS) toextract intrinsic shared semantic cues, bypassing the need for label-guidedadaptive fusion. To mitigate inherent inter-modal conflicts, we introducea Cross-modal Harmonizer (CMH) that designates RGB as a stablereference, effectively suppressing inconsistent relational supervision whileguiding the model to exploit complementary structural features. Extensiveexperimental results on NYU-Depth-v2 and MFNet show that UniM2improves mIoU by 6.4% and 9.8%, respectively, demonstrating clearadvantages over existing frameworks in UMSS task.

---

## 论文详细总结（自动生成）

# UMSS: 面向无监督多模态语义分割（UniM2）论文总结

## 1. 核心问题与整体含义

- **研究动机**：多模态语义分割（MSS）对自动驾驶、机器人导航、具身智能等安全关键应用至关重要，但严重依赖昂贵的像素级人工标注，且受限于预定义语义类别，难以利用海量无标注多模态数据。
- **关键痛点**：单模态无监督语义分割（USS）在 RGB 上已成功，但直接扩展到多模态会出现"**融合退化**"——在没有显式监督时，现有框架无法协调不同传感器捕获的异构结构模式，反而导致性能下降（如图 1 所示，CBAM、StitchFusion 等先进融合策略在无监督设定下均不如单 RGB 基线）。
- **根本原因**：监督学习中有真值标注隐式仲裁模态间不一致，而无监督设定下缺乏这种标签驱动的仲裁，导致潜在空间混乱、聚类质量下降。
- **整体含义**：本文**首次定义无监督多模态语义分割（UMSS）任务**，目标是在完全无标签设定下有效利用互补传感器信息。

## 2. 方法论（UniM2 框架）

- **核心思想**：学习一个由**跨模态对应协同（CMCS）**驱动的统一潜在空间，将跨模态对应一致性作为内在监督信号；并用**跨模态协调器（CMH）**以 RGB 为稳定参考，抑制不一致的关系监督。
- **任务定义**：给定配对数据集 $D=\{(I_i,\{X_i^{(m)}\}_{m=1}^M)\}_{i=1}^N$，学习联合表示 $\Phi(f_{rgb},\{f_X^{(m)}\}) \to s$，无任何人工标注。
- **关键技术细节**：
  - **训练输入扩展**：将 STEGO 的 Self/KNN/Random 配对策略扩展到多模态组，每个配对组 $G_1=\{I_1,X_1\}$、$G_2=\{I_2,X_2\}$，产生四个主干特征图但仅输出两个分割嵌入 $s_1,s_2$。
  - **模态融合**：$f_{fus}=\Psi(\text{MSN}(f_{rgb}),\text{MSN}(f_X))$，采用可学习 Conv Fusion，先经 Modality-Specific Networks（MSN）精炼。
  - **CMCS 损失**：对 RGB 和辅助模态分别计算对应关系 $F^{rgb}$、$F^X$（像素级余弦相似度），并约束统一空间对应 $S$；总损失 $L_{cmcs}=L_{rgb}+\lambda L_X$，其中各项形如 $L=-\sum (F-b)\odot\max(0,S)$，$b$ 为条件于配对类型的偏置。
  - **CMH 机制**：不直接刚性对齐统一嵌入 $s$ 与辅助特征 $f_X$，而是通过轻量可学习缓冲 $s_X=\text{CMH}(s)$（两层卷积实现），使辅助监督与主语义流形解耦；协调后的对应为 $S^X_{hwij}=\cos(s^X_{1,hw},s^X_{2,ij})$。
  - **可扩展性**：为每个辅助模态分配独立 CMH 分支，总损失泛化为 $L_{cmcs}=L_{rgb}+\sum_{n=1}^N \lambda_n L_{X_n}$，防止梯度干扰。

## 3. 实验设计

- **数据集 / 场景**：
  - **NYU-Depth-v2**：室内 RGB-D 分割，1,449 对对齐图像，13 类评估协议。
  - **MFNet**：城市 RGB-热红外分割，1,569 对图像（白天/夜晚），8 类评估。
  - **MCubeS**：四模态材料分割（RGB、NIR、DoLP、AoLP），20 类，验证多于两模态的融合。
- **Benchmark / 评价指标**：mIoU 与 Pixel Accuracy（Acc.）。
- **对比方法**：
  - USS 扩展：STEGO、EAGLE 及其多模态变体；直接 K-means 聚类 DINO 特征。
  - 图像级融合：SwinFusion、Mask-DiFuser。
  - RGB-to-X 蒸馏：CORAL、MMD、Cosine。
- **实现细节**：DINOv3 冻结主干，5-crop 预处理，分割头为两层卷积；消融用 DINOv3-Small/16，主对比含 Small 与 Base/16。

## 4. 资源与算力

- **GPU**：单张 **NVIDIA GeForce RTX 5090**。
- **训练时长**：受益于冻结主干，**每个模型训练时间少于 2 小时**。
- **超参搜索**：每个对比方法均分配 **200 次贝叶斯超参数优化**迭代，保证公平。
- **优化器**：Adam，学习率 $5\times10^{-4}$，batch size 32。
- 论文未提及多卡并行或更大规模算力集群的使用。

## 5. 实验数量与充分性

- **实验规模**：覆盖 3 个数据集（双模态 ×2 + 四模态 ×1），包含主对比、逐类分析、可视化对比、特征可视化。
- **消融实验**：
  - 组件有效性（CMCS、MSN、CMH 逐步加入：25.0% → 31.3% → 34.2% → 36.9%）。
  - CMH 锚点位置（Both / Depth only / RGB only / No anchors）。
  - 融合策略（Max / Mean / Sum / Conv）。
- **公平性**：所有对比方法使用相同的超参数搜索预算，避免统一配置带来的偏差；指出 USS 对超参敏感并非 UniM2 独有。
- **充分性评价**：实验较为充分，涵盖多数据集、多模态数量、逐类与可视化分析；但消融主要在 NYU-Depth-v2 + DINOv3-Small/16 上完成，跨数据集/跨主干的消融覆盖略有限。

## 6. 主要结论与发现

- **核心成果**：UniM2 将传统融合方法的"性能退化"转化为稳定增益——在 DINOv3-Base/16 下，NYU-Depth-v2 上比 RGB-only STEGO 提升 **6.4 mIoU**，MFNet 上提升 **9.8 mIoU**（Table 1 中代表值分别为 36.9 和 45.7）。
- **反直觉发现**：直接引入辅助模态到现有 USS 基线（STEGO、EAGLE）常导致 mIoU 明显下降，说明无监督下异构模态带来结构性冲突。
- **逐类分析**：朴素深度融合提升 Sofa 等几何敏感类，但严重损害 Floor、Wall 等外观主导类；UniM2 在 Sofa、Table、TV 上最佳，同时保持 Floor、Wall 的强表现，实现更好平衡。
- **多模态扩展**：在 MCubeS 上加入信息量大的模态（如 NIR、DoLP）可获一致提升；AoLP 等弱/噪声模态仍可能限制性能。
- **锚点选择**：RGB 作为唯一锚点（36.9%）显著优于 Depth 锚点（27.6%）；无锚点则崩溃至 19.8%，说明 RGB 提供更可靠的语义结构。

## 7. 优点

- **任务开创性**：首次形式化定义 UMSS 任务，填补无监督学习与多模态感知之间的空白。
- **方法设计巧妙**：
  - CMCS 用跨模态对应一致性作为内在监督，避免对标签的依赖，强调"多源共识"而非单向模仿。
  - CMH 以轻量可学习缓冲实现软对齐，既吸收互补线索又隔离模态冲突，设计简洁且理论上有解释空间。
  - 模块化设计天然支持 N 个辅助模态扩展，无需复杂平衡策略。
- **实验严谨**：
  - 为所有对比方法统一分配 200 次贝叶斯超参搜索，公平性强。
  - 提供逐类分析、特征可视化、锚点消融、融合策略消融等多角度验证。
- **实用性强**：冻结主干使训练高效（单卡 <2 小时），易于复现与推广。

## 8. 不足与局限

- **模态质量依赖**：MCubeS 上 AoLP 等弱/噪声模态仍会拖累性能，说明方法对传感器可靠性敏感，未提出显式的模态质量评估或噪声鲁棒机制。
- **消融覆盖有限**：主要消融集中在 NYU-Depth-v2 + DINOv3-Small/16，未在 MFNet、MCubeS 或 Base 主干上系统验证各组件贡献。
- **对主干的依赖**：整体框架建立在 DINOv3 冻结特征之上，其性能可能受限于 DINOv3 的预训练质量与域泛化能力，未探索其他自监督主干。
- **超参敏感性**：$\lambda$、$b$ 等超参需按配对类型与数据集调节，虽用贝叶斯优化缓解，但仍是潜在偏差风险来源。
- **应用限制**：目前主要验证室内/城市驾驶/材料分割场景，对传感器标定、模态缺失、模态损坏等实际部署问题的鲁棒性未做深入探讨。
- **理论分析**：CMH 的深入理论分析放在补充材料，正文对其"为何能抑制冲突"的机理解释偏定性。

（完）
