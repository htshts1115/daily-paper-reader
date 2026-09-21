---
title: "MP-Mat: A 3D-and-Instance-Aware Human Matting and Editing Framework with Multiplane Representation"
title_zh: MP-Mat：基于多平面表示的三维与实例感知人体抠图与编辑框架
authors: "Siyi Jiao, Wenzheng Zeng, Yerong Li, Huayu Zhang, Changxin Gao, Nong Sang, Mike Zheng Shou"
date: 2025
publication_date: 2025
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=Xw0fCEMFss"
tags: ["query:matting"]
score: 7.0
evidence: 基于深度多层表示的人体实例抠图
tldr: 针对人体实例抠图在毛发与细薄边界处难以分离混合像素的问题，本文提出MP-Mat，一个融合三维与实例感知的多平面抠图框架。方法从场景几何与实例两个层面构建特征级多平面表示，依据深度差异将场景拆分为多个平面，使表示具备三维感知能力。实验表明该框架能有效处理多实例交织与细薄结构边界，提升抠图质量。其利用深度差异分离前景的思路对人像虚化与抠图流水线有重要参考价值。
source: ICLR-2025-Accepted
selection_source: conference_retrieval
motivation: 人体实例抠图在毛发与细薄边界及多实例混合像素处容易失败。
method: 构建特征级多平面表示，按深度差异将场景拆分为多个平面以获得三维与实例感知。
result: 实验表明该框架能有效分离多实例交织像素并处理细薄边界结构。
conclusion: 为利用深度信息进行人像抠图提供了新思路，可支撑人像虚化流水线。
---

## Abstract
Human instance matting aims to estimate an alpha matte for each human instance in an image, which is challenging as it easily fails in complex cases requiring disentangling mingled pixels belonging to multiple instances along hairy and thin boundary structures. In this work, we address this by introducing MP-Mat, a novel 3D-and-instance-aware matting framework with multiplane representation, where the multiplane concept is designed from two different perspectives: scene geometry level and instance level. Specifically, we first build feature-level multiplane representations to split the scene into multiple planes based on depth differences. This approach makes the scene representation 3D-aware, and can serve as an effective clue for splitting instances in different 3D positions, thereby improving interpretability and boundary handling ability especially in occlusion areas. Then, we introduce another multiplane representation that splits the scene in an instance-level perspective, and represents each instance with both matte and color. We also treat background as a special instance, which is often overlooked by existing methods. Such an instance-level representation facilitates both foreground and background content awareness, and is useful for other down-stream tasks like image editing. Once built, the representation can be reused to realize controllable instance-level image editing with high efficiency. Extensive experiments validate the clear advantage of MP-Mat in matting task. We also demonstrate its superiority in image editing tasks, an area under-explored by existing matting-focused methods, where our approach under zero-shot inference even outperforms trained specialized image editing techniques by large margins. Code is open-sourced at https://github.com/JiaoSiyi/MPMat.git.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
基于深度多层表示的人体实例抠图。

### 2. 核心内容
针对人体实例抠图在毛发与细薄边界处难以分离混合像素的问题，本文提出MP-Mat，一个融合三维与实例感知的多平面抠图框架。方法从场景几何与实例两个层面构建特征级多平面表示，依据深度差异将场景拆分为多个平面，使表示具备三维感知能力。实验表明该框架能有效处理多实例交织与细薄结构边界，提升抠图质量。其利用深度差异分离前景的思路对人像虚化与抠图流水线有重要参考价值。

### 3. 对应检索需求
Papers central to 人像抠图、人体抠图、视频抠图，重点关注发丝、透明物、前景完整性和边界自然度。, especially work that connects or combines: trimap-free matting; portrait matting; human segmentation for matting; natural image matting; video matting without trimap; fine hair detail matting; trimap free matting for robust foreground background separation in real world images; human matting for hair details transparent objects and thin structures; High quality portrait matting with hair detail; Real time video matting for human subjects.

### 4. 来源与原文
- Source：ICLR-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=Xw0fCEMFss](https://openreview.net/forum?id=Xw0fCEMFss)
