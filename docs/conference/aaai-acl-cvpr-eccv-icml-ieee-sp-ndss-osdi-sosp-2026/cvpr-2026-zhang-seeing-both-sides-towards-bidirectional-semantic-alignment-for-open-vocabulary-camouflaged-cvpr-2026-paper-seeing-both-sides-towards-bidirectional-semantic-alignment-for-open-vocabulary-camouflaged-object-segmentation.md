---
title: "Seeing Both Sides: Towards Bidirectional Semantic Alignment for Open-Vocabulary Camouflaged Object Segmentation"
title_zh: 双向视角：面向开放词汇伪装目标分割的双向语义对齐
authors: "Zhang, Guohui, Sun, Fuming, Zhao, Yu, Kong, Yuqiu, Sun, Jing, Wang, Fasheng"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Seeing_Both_Sides_Towards_Bidirectional_Semantic_Alignment_for_Open-Vocabulary_Camouflaged_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 8.0
evidence: 面向开放词汇分割的双向语义对齐
tldr: 论文针对开放词汇伪装目标分割中现有方法仅用文本单向引导视觉匹配、忽略图文双向交互，导致复杂伪装场景语义混乱的问题，提出双向语义对齐框架BaCLIP。其核心为互惠交互机制，使文本与视觉在图像级语义与像素级分割线索之间双向对齐。实验表明该方法有效缓解图文语义鸿沟，在未见类别的伪装目标分割上取得更精确结果。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 934, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 934, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 799, \"height\": 584}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 799, \"height\": 584}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 799, \"height\": 584}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 799, \"height\": 584}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 4, \"index\": 9, \"width\": 1024, \"height\": 615}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 1023, \"height\": 731}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 1023, \"height\": 731}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 1023, \"height\": 731}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 1023, \"height\": 731}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 6, \"index\": 17, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 6, \"index\": 18, \"width\": 1024, \"height\": 559}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 1024, \"height\": 559}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 6, \"index\": 22, \"width\": 1024, \"height\": 559}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 6, \"index\": 23, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 6, \"index\": 24, \"width\": 1024, \"height\": 559}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 6, \"index\": 25, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 6, \"index\": 26, \"width\": 722, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 6, \"index\": 27, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 6, \"index\": 28, \"width\": 722, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 6, \"index\": 29, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 6, \"index\": 30, \"width\": 722, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 6, \"index\": 31, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 6, \"index\": 32, \"width\": 722, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 6, \"index\": 33, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 8, \"index\": 34, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 8, \"index\": 35, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 8, \"index\": 36, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 8, \"index\": 37, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 8, \"index\": 38, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 8, \"index\": 39, \"width\": 1000, \"height\": 662}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 8, \"index\": 40, \"width\": 1024, \"height\": 683}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 8, \"index\": 41, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 8, \"index\": 42, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-seeing-both-sides-towards-bidirectional-semantic-alignment-for-open-vocabulary-camouflaged-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 8, \"index\": 43, \"width\": 1000, \"height\": 662}]"
motivation: 现有方法仅用文本单向引导视觉，忽略双向交互导致语义混乱。
method: 提出双向语义对齐框架BaCLIP，实现图文在语义与像素层面的互惠交互。
result: 缓解图文语义鸿沟，提升未见类别伪装目标分割精度。
conclusion: 为开放词汇分割提供双向对齐的新思路。
---

## Abstract
Open-Vocabulary Camouflaged Object Segmentation (OVCOS) aims to segment camouflaged objects from unseen categories under textual guidance precisely. However, existing methods often employ a unidirectional interaction strategy, where textual prompts guide the matching of visual features. Such a design neglects the bidirectional interaction between visual and language modalities, making the model vulnerable to the semantic gap between image-level textual semantics and pixel-level segmentation cues, which in turn leads to severe semantic confusion in complex camouflaged scenarios. To address this challenge, we propose BaCLIP, a novel bidirectional semantic alignment framework for OVCOS. At its core lies the Mutual Refinement and Enhancement Module (MREM), which establishes bidirectional cross-attention between visual and textual features, enabling mutual semantic calibration to resolve ambiguity and strengthen cross-modal alignment. Moreover, we introduce an Adaptive Prompt that transforms refined textual embeddings into semantic-aware prompts for Segment Anything Model (SAM), enabling direct textual guidance and improving mask precision. Experimental results on the OVCamo benchmark demonstrate that BaCLIP consistently achieves state-of-the-art performance with a compact architecture, effectively mitigating semantic confusion and advancing the understanding of cross-modal camouflage perception. Our code is released at https://github.com/okmaybach/BaCLIP-CVPR2026.

---

## 论文详细总结（自动生成）

# 论文总结：Seeing Both Sides: Towards Bidirectional Semantic Alignment for Open-Vocabulary Camouflaged Object Segmentation

---

## 1. 核心问题与整体含义（研究动机与背景）

- **任务背景**：开放词汇伪装目标分割（OV-COS）旨在依据文本提示，从**未见类别**中精确分割出与背景高度融合的伪装目标。该任务由 Pang 等人（ECCV 2024）正式提出，并配套发布了 OVCamo 基准和 CLIP 基线方法 OVCoser。
- **核心问题**：现有方法（如 OVCoser、SuCLIP）普遍采用**单向交互策略**，即仅由文本提示引导视觉特征匹配，忽略视觉与语言模态之间的双向反馈。
- **导致的后果**：
  - 图像级文本语义与像素级分割线索之间存在**语义鸿沟**；
  - 在复杂伪装场景中极易引发**语义混淆**，例如将背景中的“绿色叶子”误判为目标“绿色蠕虫”，或将“蜜蜂”误分类为“蚂蚁”、产生不完整分割掩码。
- **研究动机**：作者认为，必须建立视觉与语言之间的**双向引导机制**，让视觉线索反过来校准文本语义、文本语义增强视觉判别力，才能从根本上缓解语义混淆。
- **整体含义**：论文提出 BaCLIP 框架，为开放词汇伪装感知建立**双向跨模态对齐**的新范式。

---

## 2. 方法论：核心思想、关键技术细节与算法流程

### 2.1 整体框架

- **视觉通路**：CLIP 视觉编码器提取多尺度视觉特征 $f_v$。
- **文本通路**：类别描述经 CamoPrompts 后送入 CLIP 文本编码器，得到文本嵌入 $f_t$。
- **核心交互**：视觉与文本流在 **MREM**（Mutual Refinement and Enhancement Module）中进行双向交叉注意力。
- **视觉增强**：精炼后的视觉特征 $E_v$ 经 **CCE**（Camo Clue Extractor）中的级联 MFMSA 处理，输出伪装敏感特征 $E_v^*$。
- **文本提示**：MREM 增强后的文本特征投影为自适应提示嵌入 $E_t^*$，送入 SAM 的 Prompt Encoder。
- **掩码生成与分类**：$E_t^*$ 与 $E_v^*$ 共同输入 Mask Decoder 生成二值掩码，最终利用 CLIP 零样本能力预测类别。

### 2.2 MREM：双向交叉注意力

- 将视觉特征 $f_v \in \mathbb{R}^{H \times W \times C}$ 与文本嵌入 $f_t \in \mathbb{R}^{N \times C}$ 投影为 $h$ 组独立的 QKV 三元组：
  - 视觉侧：$Q_{v,i}, K_{v,i}, V_{v,i} = W^Q_{v,i} f_v, W^K_{v,i} f_v, W^V_{v,i} f_v$
  - 文本侧：$q_{t,i}, k_{t,i}, v_{t,i} = W^Q_{t,i} f_t, W^K_{t,i} f_t, W^V_{t,i} f_t$
- 单头双向交叉注意力：
  - 视觉被文本精炼：$F^{head}_{v,i} = \text{Softmax}\left(\frac{Q_{v,i} k_{t,i}^T}{\sqrt{d_k}}\right) v_{t,i}$
  - 文本被视觉精炼：$F^{head}_{t,i} = \text{Softmax}\left(\frac{q_{t,i} K_{v,i}^T}{\sqrt{d_k}}\right) V_{v,i}$
- 多头拼接后线性投影得到 $E_v$ 与 $E_t$：
  - $E_v = \text{Proj}(\text{Concat}(F^{head}_{v,1}, \dots, F^{head}_{v,h}) W^O_v)$
  - $E_t = \text{Concat}(F^{head}_{t,1}, \dots, F^{head}_{t,h}) W^O_t$
- **作用**：文本向视觉注入类别语义，视觉反向校准文本焦点，抑制与背景相关的语义混淆。

### 2.3 CCE：多频率多尺度注意力（MFMSA）

- **多尺度特征提取**：三路并行分支，分别以 Down2、Down4 下采样，生成 $E_1, E_2, E_3$。
- **MFCA（多频率通道注意力）**：利用 DCT Bias 将特征分解为多个频率分量，经并行 FC 层聚合生成通道注意力图，与原始特征相乘得到 $\chi_i$。
- **MSDA（多尺度差分注意力）**：引入可学习参数 $\alpha_i, \beta_i$ 控制前景/背景信息流：
  - $\lambda_i = \text{Conv}_3(\alpha_i(\chi_i \otimes F_i) \oplus \beta_i(\chi_i \otimes B_i))$
  - 其中 $F_i = \text{Sigmoid}(\text{Conv}_1(\chi_i))$ 为前景注意力图，$B_i = 1 - F_i$ 为背景注意力图。
- **多尺度聚合**：$\chi = \lambda_1 \oplus \text{Up}_2(\lambda_2) \oplus \text{Up}_4(\lambda_3)$，最终经残差连接：$E_v^* = E_v \oplus \chi$。

### 2.4 面向 SAM 的自适应文本提示

- 精炼文本嵌入 $E_t$ 先经 SelfAttention 捕获 token 间依赖：$P_t = \text{SelfAttention}(E_t)$。
- 再经投影层与冻结的 SAM Prompt Encoder：$E_t^* = \text{PromptEncoder}(\text{Proj}(P_t))$。
- 用自适应文本提示替代 SAM 原始的空间提示（点/框/掩码），使 SAM 具备开放词汇与语义引导能力。

### 2.5 损失函数

- 总损失：$\mathcal{L}_{seg} = \mathcal{L}_{BCE} + \mathcal{L}_{Dice}$，分别监督分割结果并缓解正负样本类别不平衡。

---

## 3. 实验设计

- **数据集 / 场景**：使用 **OVCamo** 基准，包含 14 个基础训练类别和 61 个新测试类别。
- **Benchmark**：OVCamo 上的开放词汇伪装目标分割评测。
- **对比方法**：
  - 通用开放词汇语义分割方法：SimSeg、OVSeg、ODISE、SAN、CAT-Seg、FC-CLIP；
  - 先进 OV-COS 方法：SuCLIP、OVCoser（基线）。
- **评测设置**：三种训练设定——(1) 在 COCO 上训练后直接在 OVCamo 测试；(2) 在 COCO 上训练后在 OVCamo 微调；(3) 直接在 OVCamo 上训练。
- **评价指标**：6 个指标——$cS_m$、$cF_{\omega\beta}$、$cMAE$、$cF_\beta$、$cE_m$、$cIoU$，同时考虑分割与分类性能。
- **额外分析**：
  - 困难类别分析（按基线 cIoU 排名后 25% 的 15 个类别）；
  - t-SNE 特征分布可视化（24 类）；
  - 定性对比与特征热力图可视化。

---

## 4. 资源与算力

- **GPU**：单张 NVIDIA GeForce RTX 4090（24 GB 显存）。
- **训练配置**：
  - 输入图像尺寸 384 × 384；
  - CLIP 参数冻结；
  - AdamW 优化器，batch size = 4，学习率 = 3 × 10⁻⁵，epochs = 30；
  - 余弦退火学习率调度；
  - 数据增强：随机翻转、旋转、颜色抖动。
- **未明确说明**：论文未报告具体训练时长、总 GPU 小时数或参数量统计。

---

## 5. 实验数量与充分性

- **主要实验组数**：
  - 表 1：与 7 种 OVSS 方法 + 2 种 OV-COS 方法在 3 种训练设定下的全面对比；
  - 表 2：困难类别（15 类）vs 全部类别（61 类）的针对性分析；
  - 表 3：组件逐步消融（baseline → +SAM → +CCE → +CCE+MREM，共 4 组）；
  - 表 4：骨干网络消融（ViT-B/16、ViT-L/14、ConvNeXt-L、ConvNeXt-XXL，共 4 组）；
  - 表 5：MREM 消融（w/o MREM、w/o visual、w/o text、w/o SA、完整模型，共 5 组）；
  - 表 6：CCE 消融（w/o CCE、MFMSA-2/3/4/5、w MSDA、w MFCA、完整模型，共 8 组）。
- **充分性与客观性**：
  - 消融实验覆盖了各核心模块及其子组件，设计较为系统；
  - 对比方法涵盖通用 OVSS 与专用 OV-COS 方法，且包含零样本、微调、直接训练三种设定，公平性较好；
  - 提供了困难类别的专项分析，增强了结论的说服力；
  - 但所有实验仅在 OVCamo 单一数据集上进行，跨数据集泛化验证不足。

---

## 6. 主要结论与发现

- **SOTA 性能**：BaCLIP 在 OVCamo 上全面超越 OVCoser：
  - $cS_m$ +1.0%、$cF_{\omega\beta}$ +5.0%、$cMAE$ +0.9%、$cF_\beta$ +3.9%、$cE_m$ +2.4%、$cIoU$ +4.5%。
- **困难类别提升更显著**：在 15 个最难类别上，$cIoU$ 提升 +6.3%、$cF_{\omega\beta}$ +7.1%、$cMAE$ 误差降低 +2.9%，远超全体类别平均增益，验证了方法对语义混淆的针对性缓解能力。
- **t-SNE 验证**：MREM 使 24 类特征分布从稀疏、重叠变为紧凑、边界清晰，证明双向语义精炼有效提升跨模态一致性与判别性。
- **消融结论**：
  - CCE 带来最大单模块增益（cIoU 从 0.332 提升至 0.428，+9.6%）；
  - MREM 在 CCE 基础上再提升 6.0% cIoU，验证双向交互的必要性；
  - 单向增强（仅视觉或仅文本）效果远不如双向；
  - ConvNeXt-L 骨干显著优于 ViT 系列，因其天然提供多尺度特征；
  - MFMSA 模块数取 3 为最佳，MFCA 与 MSDA 需联合使用效果最好。
- **效率优势**：方法无需额外视觉骨干（如 ResNet、Swin），用 CLIP 视觉编码器替换 SAM 原始骨干，显著降低参数量并提升效率。

---

## 7. 优点

- **范式创新**：首次从双向模态引导视角重新审视 OVCOS 任务，提出双向语义对齐框架，直击单向交互导致的语义混淆痛点。
- **模块设计精巧**：
  - MREM 通过双向交叉注意力实现图文互校准，结构清晰、即插即用；
  - CCE 结合频域（MFCA）与空域（MSDA）多尺度线索，针对性增强伪装特征提取；
  - 自适应文本提示无缝对接 SAM，无需手工空间提示。
- **实验扎实**：
  - 消融实验覆盖全面，逐步验证各组件贡献；
  - 困难类别专项分析直接呼应研究动机，逻辑闭环；
  - t-SNE 与热力图可视化提供直观解释性证据。
- **架构紧凑**：不依赖额外重型骨干，在保持高性能的同时控制参数量。
- **开源可复现**：代码已公开于 GitHub。

---

## 8. 不足与局限

- **数据集覆盖单一**：仅在 OVCamo 一个基准上评测，缺乏跨数据集（如 COD10K、CAMO 等）的泛化验证。
- **训练规模有限**：单卡 RTX 4090、batch size 仅 4、epochs 30，未报告训练时长与总计算量，难以评估实际训练成本。
- **分辨率限制**：输入固定为 384 × 384，对高分辨率伪装目标的细节保留可能不足。
- **骨干依赖**：性能受 CLIP 视觉编码器能力制约；虽测试了 ConvNeXt-XXL 更优，但未深入分析更大规模模型的效率-精度权衡。
- **困难类别定义依赖基线**：以 OVCoser 的 cIoU 排名划定“困难类别”，可能存在对基线性能的路径依赖偏差。
- **应用限制**：伪装场景本身标注困难，模型在极端低对比度或目标极小场景下的鲁棒性未充分讨论；推理延迟与实时性未涉及。
- **文本提示设计**：CamoPrompts 的具体构造方式在正文中描述较少，文本质量对结果的敏感性未做分析。

---

（完）
