---
title: Training-Free Open-Vocabulary Camouflaged Object Segmentation via Fine-Grained Object Binding and Adaptive Hybrid Prompt
title_zh: 通过细粒度目标绑定与自适应混合提示实现免训练开放词汇伪装目标分割
authors: "Ren, Peng, Jiang, Cheng, Yang, Chuande, Sun, Fuming, Bai, Tian"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ren_Training-Free_Open-Vocabulary_Camouflaged_Object_Segmentation_via_Fine-Grained_Object_Binding_and_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 7.0
evidence: 免训练开放词汇伪装目标分割
tldr: 针对开放词汇伪装目标分割中现有方法依赖掩码标注、且稀疏文本提示导致目标绑定不足的问题，本文提出免训练框架，结合细粒度目标绑定与自适应混合提示，并借助多模态大语言模型增强视觉块间的类别关联。实验表明该方法无需任何掩码监督即可在伪装场景下取得优于现有免训练方法的精度，为快速泛化到未见类别提供了可行方案。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ren-training-free-open-vocabulary-camouflaged-object-segmentation-via-fine-grained-object-binding-and-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 8, \"index\": 1, \"width\": 5712, \"height\": 4787}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ren-training-free-open-vocabulary-camouflaged-object-segmentation-via-fine-grained-object-binding-and-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 8, \"index\": 2, \"width\": 5712, \"height\": 4787}]"
motivation: 现有免训练开放词汇伪装目标分割依赖稀疏文本提示且忽略视觉块间类别相似性，目标绑定能力不足。
method: 提出细粒度目标绑定与自适应混合提示框架，利用多模态大语言模型增强视觉块与类别的绑定。
result: 在伪装目标分割基准上无需掩码标注即取得优于现有免训练方法的精度。
conclusion: 表明免训练范式可快速泛化到未见类别，为开放词汇分割提供新思路。
---

## Abstract
Vision-Language models (e.g., CLIP) facilitate the development of open-vocabulary camouflaged object segmentation (OVCOS), but existing methods still rely on mask annotations for fully-supervised training. In contrast, the training-free paradigm can rapidly process unseen data, representing a highly promising solution. However, in camouflage scenarios, existing training-free methods utilize sparse textual prompts and ignore the category similarity between visual patches, leading to inadequate object binding capability. To alleviate these issues, we propose a fine-grained object binding and adaptive hybrid prompt framework for training-free OVCOS. The framework first employs multimodal large language models (MLLMs) to explicitly model fine-grained textual descriptions of camouflaged objects and background. Building on this, we construct a semantic probe to decouple object and background features and explicitly model category similarity between visual patches via semantic consistency ranking, thereby achieving accurate object binding. Subsequently, we propose an entropy-guided text embedding adjustment strategy to adjust textual embeddings, aiming to further enhance fine-grained object binding. Finally, we utilize an adaptive hybrid prompt generation strategy to generate hybrid prompts, assisting SAM in accurately segmenting camouflaged objects. Experimental results on the OVCamo benchmark demonstrate that our method achieves excellent performance, significantly surpassing the advanced training-free ResCLIP.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：开放词汇伪装目标分割（OVCOS）要求模型根据文本提示分割未见过的伪装类别。传统 COS 多依赖闭集监督；已有 OVCOS 方法虽支持开放词汇，但通常需要掩码标注进行全监督训练，容易过拟合已见类别，泛化到新伪装类别时受限。
- **核心问题**：现有免训练开放词汇语义分割方法直接迁移到伪装场景时，存在两个关键缺陷：
  - **文本语义稀疏**：多使用 “a photo of a <class>” 等模板，缺少对伪装目标属性与背景语义的细粒度描述，易受背景语义干扰。
  - **忽略视觉块间类别相似性**：直接使用 patch-text 相似度图分割，未显式建模同一伪装目标不同 patch 之间的类别相关性，导致“目标绑定”能力不足。
- **整体含义**：论文提出一种免训练 OVCOS 框架，利用多模态大语言模型、语义探针、熵引导文本嵌入调整和自适应混合提示，在无需掩码监督训练的情况下，实现更精确的伪装目标绑定与分割，提升对未见伪装类别的泛化能力。

## 2. 方法论：核心思想与关键技术

- **总体框架**：冻结 CLIP、SAM、LLaVA 等基础模型，采用免训练范式。核心模块包括：
  - 多模态大语言模型生成细粒度目标描述与背景描述；
  - 语义探针（Semantic Probe）解耦目标/背景并建模 patch 间类别相似性；
  - 熵引导文本嵌入调整（EGTEA）抑制背景语义偏差；
  - 自适应混合提示生成（AHPG）辅助 SAM 分割。

- **CLIP 视觉特征处理**：
  - 遵循 ResCLIP 思路，移除 CLIP ViT 最后一层的残差连接与前馈网络；
  - 使用中间层注意力特征精炼最终视觉层，以保留更多局部细节；
  - 对图像 \(I\) 和文本 \(T\)，提取视觉特征 \(F_v=\{F_{patch},F_{cls}\}\) 和文本特征 \(F_t\)；
  - 类别预测基于 \([CLS]\) 与文本嵌入的余弦相似度，经 softmax 得到 \(P(c)\)；
  - patch-text 相似度图定义为 \(S=\cos(F_{patch},F_t)\)。

- **语义探针（Semantic Probe）**：
  - 使用 LLaVA-1.5 为每张图生成：
    - **目标描述
