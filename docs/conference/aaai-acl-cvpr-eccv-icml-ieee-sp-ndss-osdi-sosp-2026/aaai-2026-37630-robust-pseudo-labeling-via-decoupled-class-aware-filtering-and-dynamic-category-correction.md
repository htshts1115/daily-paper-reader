---
title: Robust Pseudo-Labeling via Decoupled Class-Aware Filtering and Dynamic Category Correction
title_zh: 基于解耦类别感知筛选与动态类别校正的鲁棒伪标签方法
authors: "Jianghang Lin, Yilin Lu, Chaoyang Zhu, Yunhang Shen, Shengchuan Zhang, Liujuan Cao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37630/41592"
tags: ["query:seg"]
score: 6.0
evidence: 解耦伪标签筛选的半监督实例分割
tldr: 半监督实例分割需在少量标注与大量无标注数据下分类并分组像素，其核心难题是伪标签噪声，尤其当类别与掩码质量耦合为单一置信度时，语义精度与空间精度难以兼顾。本文提出伪标签解耦与校正框架PL-DC，在实例级引入自适应类别感知阈值的解耦筛选，并进行动态类别校正。实验表明该框架改善了伪标签选择质量，提升了半监督实例分割性能。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37630/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 10243, \"height\": 2611}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37630/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 2660, \"height\": 2647}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37630/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 2855, \"height\": 1025}]"
motivation: 半监督实例分割中伪标签噪声大，类别与掩码质量耦合导致筛选次优。
method: 提出PL-DC框架，在实例级用自适应类别感知阈值解耦筛选伪标签并做动态类别校正。
result: 实验表明该框架提升了伪标签选择质量与半监督实例分割的整体性能。
conclusion: 该工作为实例分割的伪标签噪声问题提供了有效解耦方案。
---

## Abstract
Semi-Supervised Instance Segmentation (SSIS) involves classifying and grouping image pixels into distinct object instances using limited labeled data alongside large-scale unlabeled data. A major challenge in SSIS lies in the inherent noise of pseudo-labels, particularly when class and mask qualities are coupled into a single confidence score for filtering. Such coupling often results in sub-optimal trade-offs between semantic accuracy and spatial precision. To address this, we propose a novel Pseudo-Label Decoupling and Correction (PL-DC) framework, which explicitly decouples and enhances the pseudo-label selection process for SSIS. At the instance level, we introduce a Decoupled Filtering with Adaptive Class-Aware Thresholds mechanism, which independently evaluates class and mask qualities using category-specific thresholds updated via exponential moving averages. At the category level, we design a Dynamic Instance Category Correction module that reassigns ambiguous class pseudo-label by leveraging semantic prototypes and consistency alignment. At the pixel level, a Pixel-Level Mask Uncertainty-Aware mechanism is applied to suppress the influence of unreliable pixels during mask supervision, further improving the robustness against pixel-wise noise. Extensive experiments on COCO and Cityscapes datasets demonstrate that the proposed PL-DC achieves significant performance improvements, setting new state-of-the-art results. Notably, PL-DC achieves gains of +11.7 mAP with just 1% labeled COCO data and +16.4 mAP with 5% Cityscapes labels, showing its effectiveness under extremely low-label regimes.

---

## 论文详细总结（自动生成）

# 论文中文总结：Robust Pseudo-Labeling via Decoupled Class-Aware Filtering and Dynamic Category Correction

## 1. 核心问题与整体含义
- **研究背景**：半监督实例分割（SSIS）希望利用少量标注图像和大量无标注图像，同时完成像素级分类、实例区分和掩码预测，以降低对昂贵像素级标注的依赖。
- **核心问题**：SSIS 中伪标签噪声严重。现有方法常把类别置信度与掩码质量耦合为单一置信度进行筛选，导致语义准确性与空间精度之间出现次优折中。
- **论文识别的三类挑战**：
  - **实例级筛选偏差**：单一耦合分数与真实实例质量相关性弱，可能保留语义错误但掩码质量高、或空间粗糙但类别正确的伪标签。
  - **类别级混淆**：视觉相似或共现频繁的类别易混淆，如 Bears vs. Dogs、Hot Dogs vs. Sandwiches，稀疏监督下更严重。
  - **像素级噪声累积**：掩码伪标签数量远多于实例类别伪标签，噪声像素容易主导训练信号。
- **整体含义**：论文提出 **PL-DC（Pseudo-Label Decoupling and Correction）** 框架，从实例、类别、像素三个层级解耦并校正伪标签，提升半监督实例分割在极低标注条件下的鲁棒性与性能。

## 2. 方法论
- **总体框架**：采用教师-学生结构，教师和学生均为 Mask2Former。教师生成伪标签，学生同时用标注数据和伪标签训练；教师参数通过 EMA 从学生更新。
- **总体损失**：  
  \(L = L_{sup} + \lambda L_{unsup}\)，其中 \(L_{sup}=L_{cls}+L_{mask}\)。学生用 SGD/优化器更新，教师梯度冻结。

### 2.1 实例级：Decoupled Filtering with Adaptive Class-Aware Thresholds（DF-ACAT）
- **核心思想**：不再使用 \(s_k=c_k \cdot m_k\) 单一耦合分数，而是将类别质量 \(c_k\) 和掩码质量 \(m_k\) 解耦，分别设置阈值筛选。
- **类别质量**：由分类 logits 的 softmax 最大类别概率得到。
- **掩码质量**：由预测掩码中前景像素比例或相关置信统计得到。
- **自适应类别阈值**：
  - 初始阈值按类别频率设置：常见类更严格，稀有类更宽松。  
    \(T_c^{(k,0)}=T_c^{min}+(T_c^{max}-T_c^{min})\cdot n_k/N\)，掩码阈值类似。
  - 训练中用 EMA 根据每类伪标签分数动态更新：  
    \(T_c^{(k)}(e)=\alpha T_c^{(k)}(e-1)+(1-\alpha)\hat T_c^{(k)}(e)\)。
- **三级筛选策略**：
  - 同时超过类别阈值和掩码阈值：高质量，直接保留。
  - 远低于阈值：丢弃。
  - 处于中间：送入 DICC 进一步校正。

### 2.2 类别级：Dynamic Instance Category Correction（DICC）
- **目的**：缓解类别混淆和类别不平衡导致的错误伪标签。
- **实现**：
  - 使用 CLIP 等视觉-语言模型进行零样本类别校正。
  - 对弱增强无标注图像提取全局视觉特征，并对所有掩码做池化得到掩码嵌入。
  - 用大语言模型（如 GPT-4o）为每个类别生成多组多样化文本描述，增强文本表示。
  - 计算掩码嵌入与增强文本嵌入的相似度，得到 CLIP 类别概率 \(p_i^{clip}\)。
- **动态融合**：
  - 将教师预测 \(\hat p_i\) 与 CLIP 预测 \(p_i^{clip}\) 融合：  
    \(w=0.25(\cos(e/E_{max}\pi)+1)\)，  
    \(p_i^f=w p_i^{clip}+(1-w)\hat p_i\)。
  - 权重 \(w\) 从约 0.5 随训练衰减到 0，表示早期更依赖 VLM，后期更信任教师模型。
  - 最终取 \(p_i^f\) 最大类别作为校正后的类别伪标签。

### 2.3 像素级：Pixel-Level Mask Uncertainty-Aware（PMUA）
- **核心思想**：对掩码伪标签中不确定像素降权，减少噪声像素对训练的影响。
- **不确定性定义**：  
  \(u_{ik}=1-2|\sigma(q_{ik})-0.5|\)，其中 \(\sigma(q_{ik})\) 是教师模型对第 k 个实例第 i 个像素的前景概率。
- **损失加权**：在无监督掩码二元交叉熵中乘以 \((1-u)\)，使高不确定性像素贡献更小。  
  结合匈牙利匹配后，形成像素级不确定性感知的掩码损失。
- **理论说明**：扩展版推导表明，不确定性越高，该像素伪标签对学生参数更新的影响越小。

## 3. 实验设计
- **数据集与场景**：
  - **COCO**：80 类，118k train2017、5k val2017、123k unlabel2017。采样 1%、2%、5%、10% 作为标注数据；另用 100% train2017 加 unlabel2017。
  - **Cityscapes**：2,975 张训练图、500 张验证图，1024×2048，8 个实例类别。采样 5%、10%、20%、30% 作为标注数据。
- **评价指标**：标准 COCO mAP，在 COCO val2017 和 Cityscapes validation 上评估。
- **基础网络**：Mask2Former + ResNet-50，Detectron2 实现，冻结 backbone。
- **对比方法**：
  - COCO：Mask R-CNN、Mask2Former 全监督、DD、Noisy Boundaries、Polite Teacher、PAIS、GuidedDistillation 等。
  - Cityscapes：Mask R
