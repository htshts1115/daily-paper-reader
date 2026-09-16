---
title: Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation
title_zh: 利用深度与语言实现开放词汇域泛化语义分割
authors: "Siyu Chen, Ting Han, Chengzheng Fu, Changshe Zhang, Chaolei Wang, Jinhe Su, Guorong Cai, Meiliu Wu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=KWNabnuuct"
tags: ["query:seg"]
score: 7.0
evidence: 结合深度基础模型的开放词汇语义分割
tldr: 该文指出开放词汇分割与域泛化分割存在互补性，提出统一任务OV-DGSS以对未见类别生成像素掩膜并跨域保持鲁棒。方法Vireo构建于冻结的视觉基础模型之上，引入深度基础模型提取域不变的结构特征，并弥合语义与几何表征的鸿沟。实验表明其能同时提升新类别与跨域场景的分割表现，对真实世界分割与前景主体理解具有推动作用。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 开放词汇分割与域泛化分割互补，需同时对未见类别和未见域保持鲁棒。
method: 提出单阶段框架Vireo，基于冻结视觉基础模型并引入深度基础模型提取域不变结构特征。
result: 方法在未见类别与跨域场景上均取得更好的分割性能，兼顾开放词汇与泛化能力。
conclusion: 该工作统一了两类分割任务，为真实世界分割与前景主体理解提供了新范式。
---

## Abstract
Open-Vocabulary semantic segmentation (OVSS) and domain generalization in semantic segmentation (DGSS) highlight a subtle complementarity that motivates Open-Vocabulary Domain-Generalized Semantic Segmentation (OV-DGSS). OV-DGSS aims to generate pixel-level masks for unseen categories while maintaining robustness across unseen domains, a critical capability for real-world scenarios such as autonomous driving in adverse conditions. We introduce Vireo, a novel single-stage framework for OV-DGSS that unifies the strengths of OVSS and DGSS for the first time. Vireo builds upon the frozen Visual Foundation Models (VFMs) and incorporates scene geometry via Depth VFMs to extract domain-invariant structural features. To bridge the gap between visual and textual modalities under domain shift, we propose three key components: (1) GeoText Query, which align geometric features with language cues and progressively refine VFM encoder representations; (2) Coarse Mask Prior Embedding (CMPE) for enhancing gradient flow for faster convergence and stronger textual influence; and (3) the Domain-Open-Vocabulary Vector Embedding Head (DOV-VEH), which fuses refined structural and semantic features for robust prediction. Comprehensive evaluation on these components demonstrates the effectiveness of our designs. Our proposed Vireo achieves the state-of-the-art performance and surpasses existing methods by a large margin in both domain generalization and open-vocabulary recognition, offering a unified and scalable solution for robust visual understanding in diverse and dynamic environments. Code is available at https://github.com/SY-Ch/Vireo.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
结合深度基础模型的开放词汇语义分割。

### 2. 核心内容
该文指出开放词汇分割与域泛化分割存在互补性，提出统一任务OV-DGSS以对未见类别生成像素掩膜并跨域保持鲁棒。方法Vireo构建于冻结的视觉基础模型之上，引入深度基础模型提取域不变的结构特征，并弥合语义与几何表征的鸿沟。实验表明其能同时提升新类别与跨域场景的分割表现，对真实世界分割与前景主体理解具有推动作用。

### 3. 对应检索需求
Papers central to 人像分割、人体分割、前景分割，重点关注虚化场景中的主体完整性和手持物归属。, especially work that connects or combines: open-vocabulary segmentation; instance segmentation; semantic segmentation; Portrait segmentation for subject integrity in blur; Human segmentation algorithm with handheld object detection; Foreground segmentation in defocused images; foreground segmentation for handheld objects accessories and portrait scenes; segmentation model for thin structures hair boundaries and occlusions.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=KWNabnuuct](https://openreview.net/forum?id=KWNabnuuct)
