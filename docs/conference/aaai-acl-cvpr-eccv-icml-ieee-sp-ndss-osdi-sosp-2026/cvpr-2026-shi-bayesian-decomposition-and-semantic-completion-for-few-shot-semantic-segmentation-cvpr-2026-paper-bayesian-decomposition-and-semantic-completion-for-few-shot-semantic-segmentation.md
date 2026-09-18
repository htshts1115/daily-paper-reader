---
title: Bayesian Decomposition and Semantic Completion for Few-shot Semantic Segmentation
title_zh: 面向少样本语义分割的贝叶斯分解与语义补全
authors: "Shi, Guangchen, Wu, Yirui, Zhu, Wei, Wang, Tao, Zhang, Hao, Li, Bo, Lu, Tong"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Bayesian_Decomposition_and_Semantic_Completion_for_Few-shot_Semantic_Segmentation_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 6.0
evidence: 基于贝叶斯概率网络的少样本语义分割
tldr: 少样本语义分割需要在极少标注下分割新类别，现有方法依赖复杂的类别特定建模，计算成本高且泛化差。本文提出贝叶斯概率网络BPNet，将任务分解为先验、似然与类别一致性三项可解释组件，用SAM生成碎片先验、用轻量类别无关定位模型估计似然与一致性。实验表明该框架在低数据条件下提升泛化并降低计算开销，为语义分割提供通用建模思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-bayesian-decomposition-and-semantic-completion-for-few-shot-semantic-segmentation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 4, \"index\": 1, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-bayesian-decomposition-and-semantic-completion-for-few-shot-semantic-segmentation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-bayesian-decomposition-and-semantic-completion-for-few-shot-semantic-segmentation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-bayesian-decomposition-and-semantic-completion-for-few-shot-semantic-segmentation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 400, \"height\": 400}]"
motivation: 少样本语义分割现有方法依赖复杂类别特定建模，成本高且低数据下泛化受限。
method: 提出贝叶斯概率网络BPNet，用SAM生成先验并结合轻量类别无关定位模型估计似然与一致性。
result: 实验表明该方法在低数据条件下提升泛化能力并显著降低计算开销。
conclusion: 该工作为少样本语义分割提供了可解释且高效的通用建模框架。
---

## Abstract
Few-shot Semantic Segmentation (FSS) aims to segment objects of novel categories given only a handful of labeled examples. However, existing methods often rely on complex category-specific modeling, resulting in high computational cost and limited generalization under low-data regimes. To address these challenges, we propose a Bayesian Probabilistic Network (BPNet) that reformulates FSS as a composition of three interpretable components: a prior, a likelihood, and a class-consistency term. Specifically, an efficient Segment Anything Model (SAM) is employed to generate fragmented prior regions for the query image, while both the likelihood and the consistency terms are estimated by a lightweight Class-Agnostic Localization Model (CALM). CALM simultaneously predicts the class consistency between support-query pairs through a binary classification head and estimates the likelihood by localizing the target region in the support image. By evaluating SAM-generated regions in parallel, CALM can efficiently identify the core region, thereby transforming the segmentation problem into a simple binary classification task. Furthermore, to mitigate the semantic incompleteness of SAM proposals, we introduce an attention-based Semantic Completion Module (SCM), which leverages local and global context cues to integrate fragmented regions into semantically complete masks. Extensive experiments demonstrate that BPNet achieves state-of-the-art performance while maintaining high efficiency.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：少样本语义分割（FSS）目标是在仅有少量标注样本的条件下分割新类别。现有方法多依赖类别原型建模、复杂类别特定模块或大型多模态模型，存在计算成本高、低数据条件下泛化受限等问题。
- **核心问题**：如何在避免直接建模类别原型、降低计算开销的同时，提升 FSS 对新类别和复杂场景的泛化能力。
- **整体含义**：论文提出 **BPNet（Bayesian Probabilistic Network）**，将 FSS 重新表述为贝叶斯概率分解问题，由先验、似然和类别一致性三个可解释、轻量组件构成，为 FSS 提供了一种高效、可解释的建模框架。

## 2. 方法论

### 2.1 核心思想：贝叶斯分解

- 将 FSS 目标 \(p(y|x,s,m)\) 分解为：
  \[
  p(y|x,s,m) \propto p(y|x)\cdot p(m|s,x,y)\cdot p(s|x,y)
  \]
  其中：
  - \(p(y|x)\)：基于查询图像结构的先验区域；
  - \(p(m|s,x,y)\)：给定查询假设时观测到支持掩码的似然；
  - \(p(s|x,y)\)：支持图像与查询区域之间的类别一致性。
- 该分解避免直接建模类别原型，将复杂分割问题转化为轻量概率组件组合。

### 2.2 关键技术细节

- **先验生成**：使用轻量 EfficientSAM-S 对查询图像生成碎片化区域提议 \(\{R_i\}_{i=1}^N\)，提供结构准确但语义不完整的候选区域。
- **类别无关定位模块 CALM**：
  - 使用预训练轻量 ResNet-18 提取查询和支持图像特征。
  - 对每个查询区域 \(R_i\)，将其掩码与查询特征逐元素相乘，全局平均池化后与支持图像特征拼接，输入 MLP + Sigmoid，得到类别一致性概率 \(P^c_i\)。
  - 以 \(P^c_i\) 为监督信号反传，按 LayerCAM 生成支持图像 CAM，二值化后与支持掩码计算 IoU，作为似然概率 \(P^l_i\)。
  - 选择联合概率最高的区域作为核心区域：
    \[
    R_{core}=\arg\max_{R_i}(P^l_i\cdot P^c_i)
    \]
  - k-shot 时对多个支持样本的概率取平均。
- **语义补全模块 SCM**：
  - 对每个区域提取特征向量 \(V_i\)，与核心区域 \(V_{core}\) 计算余弦相似度，得到局部相似性。
  - 通过 cross-attention 计算查询全局特征与候选区域的语义上下文，再与核心区域比较，得到全局相似性，并乘以 \(P^c_i\cdot P^l_i\) 加权。
  - 最终相似性为：
    \[
    sim_i=\alpha sim^{global}_i+(1-\alpha)sim^{local}_i
    \]
    若 \(sim_i>0.5\)，则将该区域纳入最终预测掩码。
- **训练方式**：CALM 只需二分类标签，不需要精确分割掩码；训练中 SAM 结果几乎不变，因此可预计算 SAM 查询分割结果以节省显存并加速训练。

## 3. 实验设计

- **数据集 / Benchmark**：
  - **PASCAL-5i**：来自 PASCAL VOC 2012，含 20 类，四折交叉验证，每折 5 类测试、15 类训练。
  - **COCO-20i**：来自 MS COCO，含 80 类，四折，每折 20 类测试、60 类训练。
- **评价指标**：mIoU，重复 10 次不同支持图像选择并报告平均值。
- **设置**：1-shot 与 5-shot。
- **对比方法**：HDMNet、SCCAN、ABCB、DiffSeg、AlignDiff、LLaFS、PAHNet、VRP-SAM 等，涵盖 ResNet、Diffusion、LLM、SAM 等不同骨干或预训练范式。
- **定性实验**：展示 SCM 将碎片区域扩展为完整掩码、不同区域激活不同支持区域、不同支持图像引导不同核心区域选择，并给出失败案例。
- **消融实验**：
  - 网络设计：验证先验、似然 \(P^l\)、一致性 \(P^c\)、SCM 的作用，并比较 SAM 与聚类提议生成器。
  - CALM 设计：比较 ResNet-18、ResNet-101、DenseNet-121 骨干，以及分类任务与分割任务头，并报告 FPS。
  - SCM 设计：比较局部相似性、全局相似性、加权融合与 cross-attention 融合。

## 4. 资源与算力

- 文中明确提到：使用 **PyTorch**，在 **RTX 3090 GPU** 上训练 **200 epochs**。
- 为节省 GPU 显存和加速训练，作者预计算了 SAM 对所有查询图像的分割结果并存储。
- 表 3 报告了不同配置下的 FPS，如约 1.2、5.5、2.8、1.6，可用于粗略反映推理效率。
- **未明确说明**：GPU 数量、总训练时长、显存占用、模型参数量、训练总计算量等。因此算力信息不完整。

## 5. 实验数量与充分性

- 实验覆盖两个主流 FSS benchmark，均包含 1-shot 和 5-shot、四个 split，并重复 10 次，统计较规范。
- 消融实验较系统：
  - 表 2 验证 \(P^l\)、\(P^c\)、SCM 和 SAM 提议质量；
  - 表 3 验证不同骨干和任务头；
  - 表 4 验证 SCM 中局部/全局相似性与融合方式。
- 另有定性结果和失败案例分析。
- **充分性评价**：整体较充分，能支撑主要结论。但实验仍集中在两个标准数据集上，缺少跨域、开放集、更多 shot 数、复杂现实场景等验证。
- **公平性评价**：对比方法在相同 benchmark 上报告 mIoU，较客观；但不同方法使用不同预训练资源、骨干和范式，例如 LLaFS 使用 LLM、DiffSeg/AlignDiff 使用 Diffusion、BPNet 使用 SAM，严格公平性受资源差异影响。PAHNet 报告的是集成到 SCCAN 后的最佳性能，也需注意比较口径。

## 6. 主要结论与发现

- BPNet 在 PASCAL-5i 和 COCO-20i 上均取得 SOTA 或极具竞争力的结果：
  - PASCAL-5i：1-shot mean **75.7**，5-shot mean **77.1**；
  - COCO-20i：1-shot mean **54.2**，5-shot mean **61.6**。
- CALM 和 SCM 均为关键组件：
  - 去掉 \(P^l\)、\(P^c\) 或 SCM 都会显著下降；
  - 其中类别一致性 \(P^c\) 和 SCM 对最终性能尤其重要。
- SAM 提议质量明显优于简单聚类提议生成器。
- 不同骨干（ResNet-18/101、DenseNet-121）和分类/分割任务头带来的性能波动较小，说明方法鲁棒性较强。
- SCM 中局部相似性与全局相似性互补，cross-attention 融合优于简单加权平均。
- 方法能有效将 SAM 碎片区域补全为语义完整掩码，但在区域同时包含前景和背景时可能失败。

## 7. 优点

- **可解释性强**：将 FSS 显式分解为先验、似然和类别一致性，避免黑箱式类别原型建模。
- **轻量高效**：CALM 以单二分类网络联合估计似然与一致性，训练成本低；SAM 结果可预计算，加速训练。
- **无需精确分割监督**：CALM 只需二分类标签，降低对像素级标注的依赖。
- **语义补全设计合理**：SCM 同时利用局部特征相似性和全局上下文，能合并碎片区域，处理 SAM 提议语义不完整问题。
- **泛化与鲁棒性较好**：在两个 benchmark 上表现稳定，且对骨干变化不敏感。
- **易于扩展 k-shot**：通过平均多个支持样本的概率即可扩展到 5-shot。

## 8. 不足与局限

- **依赖 SAM 提议质量**：先验区域由 EfficientSAM 生成，若提议混合前景和背景，SCM 只能补全、不能分离，导致失败。
- **数据集覆盖有限**：仅评估 PASCAL-5i 和 COCO-20i，未验证跨域、开放集、视频、医学等更广泛场景。
- **算力报告不完整**：未说明 GPU 数量、训练时长、显存、参数量等，复现和效率比较信息不足。
- **公平性风险**：与使用 LLM、Diffusion、SAM 等不同资源的方法比较时，预训练知识和计算预算不完全一致。
- **超参数与阈值分析不足**：SCM 中可学习参数 \(\alpha\) 和判定阈值 0.5 的影响未充分消融。
- **应用限制**：需要额外 SAM 预计算或推理开销；对混合区域、背景干扰和类别边界模糊场景仍可能敏感。
- **k-shot 设置有限**：主要验证 1-shot 与 5-shot，未探索更多样本数或极端低资源情况。

（完）
