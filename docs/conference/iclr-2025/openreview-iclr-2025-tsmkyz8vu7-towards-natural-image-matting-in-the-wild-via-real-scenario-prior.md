---
title: Towards Natural Image Matting in the Wild via Real-Scenario Prior
title_zh: 面向真实场景先验的自然图像抠图
authors: "Ruihao Xia, Yu Liang, Peng-Tao Jiang, Hao Zhang, Qianru Sun, Yang Tang, Bo Li, Pan Zhou"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=tSmkYZ8vU7"
tags: ["query:matting"]
score: 9.0
evidence: 真实场景先验的自然图像抠图与配件融合
tldr: 现有抠图方法多在合成数据上微调，面对复杂遮挡的真实场景泛化能力不足。本文构建基于COCO的真实场景抠图数据集COCO-Matting，通过配件融合与掩码转matte生成38251个人像实例alpha matte，并据此改进SAM式抠图模型。实验表明该方法在复杂自然场景下显著提升抠图质量，推动真实场景人像抠图发展。
source: ICLR-2025-Public
selection_source: conference_retrieval
motivation: 合成数据训练的抠图模型难以泛化到复杂遮挡的真实场景，制约了实际应用效果。
method: 构建基于COCO的COCO-Matting数据集，包含配件融合与mask-to-matte流程，并据此改进SAM式交互抠图模型。
result: 数据集含38251个人像实例级alpha matte，模型在复杂自然场景下抠图质量显著提升。
conclusion: 为真实场景人像抠图提供了高质量数据与更强泛化方法。
---

## Abstract
Recent approaches attempt to adapt powerful interactive segmentation models, such as SAM, to interactive matting and fine-tune the models based on synthetic matting datasets. However, models trained on synthetic data fail to generalize to complex and occlusion scenes. We address this challenge by proposing a new matting dataset based on the COCO dataset, namely COCO-Matting. Specifically, the construction of our COCO-Matting includes accessory fusion and mask-to-matte, which selects real-world complex images from COCO and converts semantic segmentation masks to matting labels. The built COCO-Matting comprises an extensive collection of 38,251 human instance-level alpha mattes in complex natural scenarios. Furthermore, existing SAM-based matting methods extract intermediate features and masks from a frozen SAM and only train a lightweight matting decoder by end-to-end matting losses, which do not fully exploit the potential of the pre-trained SAM. Thus, we propose SEMat which revamps the network architecture and training objectives. For network architecture, the proposed feature-aligned transformer learns to extract fine-grained edge and transparency features. The proposed matte-aligned decoder aims to segment matting-specific objects and convert coarse masks into high-precision mattes. For training objectives, the proposed regularization and trimap loss aim to retain the prior from the pre-trained model and push the matting logits extracted from the mask decoder to contain trimap-based semantic information. Extensive experiments across seven diverse datasets demonstrate the superior performance of our method, proving its efficacy in interactive natural image matting. Code is available in the supplementary file.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
真实场景先验的自然图像抠图与配件融合。

### 2. 核心内容
现有抠图方法多在合成数据上微调，面对复杂遮挡的真实场景泛化能力不足。本文构建基于COCO的真实场景抠图数据集COCO-Matting，通过配件融合与掩码转matte生成38251个人像实例alpha matte，并据此改进SAM式抠图模型。实验表明该方法在复杂自然场景下显著提升抠图质量，推动真实场景人像抠图发展。

### 3. 对应检索需求
Papers central to 人像抠图、人体抠图、视频抠图，重点关注发丝、透明物、前景完整性和边界自然度。, especially work that connects or combines: trimap-free matting; portrait matting; human segmentation for matting; natural image matting; video matting without trimap; fine hair detail matting; trimap free matting for robust foreground background separation in real world images; human matting for hair details transparent objects and thin structures; High quality portrait matting with hair detail; Real time video matting for human subjects.

### 4. 来源与原文
- Source：ICLR-2025-Public
- OpenReview：[https://openreview.net/forum?id=tSmkYZ8vU7](https://openreview.net/forum?id=tSmkYZ8vU7)
