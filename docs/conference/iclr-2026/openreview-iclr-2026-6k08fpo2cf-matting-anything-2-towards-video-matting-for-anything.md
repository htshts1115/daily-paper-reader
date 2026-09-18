---
title: "Matting Anything 2:  Towards Video Matting for Anything"
title_zh: Matting Anything 2：迈向任意对象的视频抠图
authors: "Chenyi Zhang, Yiheng Lin, Yunchao Wei, Hongsong Wang, Caifeng Shan, Fang Zhao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openreview.net/pdf?id=6K08FPo2cf"
tags: ["query:matting"]
score: 9.0
evidence: 可提示的视频抠图，兼顾透明与精细物体
tldr: 现有视频抠图方法大多局限于人像等特定域，且依赖难以获取的首帧掩码，对火焰、烟雾等透明或精细物体表现不佳。论文提出通用鲁棒的可提示视频抠图模型MAM2，其可提示双模解码器同时预测分割掩码和高质量trimap，利用trimap引导提升泛化能力，并缓解透明物体的预测不稳定。用户可用点、框或掩码灵活提示，实验表明MAM2能稳定处理多样对象，推动任意对象视频抠图。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有视频抠图方法多局限于人像等特定域，且依赖难以获取的首帧掩码，对火焰、烟雾等透明或精细物体效果差。
method: 提出可提示的视频抠图模型MAM2，通过可提示双模解码器同时预测分割掩码与高质量trimap，并以trimap引导提升泛化。
result: 借助点、框或掩码等灵活提示，MAM2能稳定处理多种透明与精细对象，显著优于域特定方法。
conclusion: 为通用、鲁棒的任意对象视频抠图提供了可提示的统一方案。
---

## Abstract
Video matting is a crucial task for many applications, but existing methods face significant limitations. They are often domain-specific, focusing primarily on human portraits, and rely on the mask of first frame that is challenging to acquire for transparent or intricate objects like fire or smoke. To address these challenges, we introduce Matting Anything 2 (MAM2), a versatile and robust video matting model that handles diverse objects using flexible user prompts such as points, boxes, or masks. We first propose Promptable Dual-mode Decoder (PDD), an effective structure that simultaneously predicts a segmentation mask and a corresponding high-quality trimap, leveraging trimap-based guidance to improve generalization. To tackle prediction instability for transparent objects across video frames, we further propose a Memory-Separable Siamese (MSS) mechanism. MSS employs a recurrent approach that isolates trimap prediction from potentially interfering mask memory, significantly enhancing temporal consistency. To validate our method's performance on diverse objects, we introduce the Natural Object Video Matting dataset, a new benchmark with substantially greater diversity. Extensive experiments show that MAM2 possesses exceptional matting accuracy and generalization capabilities. We believe MAM2 demonstrates a significant leap forward in creating a video matting method for anything.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
可提示的视频抠图，兼顾透明与精细物体。

### 2. 核心内容
现有视频抠图方法大多局限于人像等特定域，且依赖难以获取的首帧掩码，对火焰、烟雾等透明或精细物体表现不佳。论文提出通用鲁棒的可提示视频抠图模型MAM2，其可提示双模解码器同时预测分割掩码和高质量trimap，利用trimap引导提升泛化能力，并缓解透明物体的预测不稳定。用户可用点、框或掩码灵活提示，实验表明MAM2能稳定处理多样对象，推动任意对象视频抠图。

### 3. 对应检索需求
Papers central to 人像抠图、人体抠图、视频抠图，重点关注发丝、透明物、前景完整性和边界自然度。, especially work that connects or combines: trimap-free matting; portrait matting; human segmentation for matting; natural image matting; video matting without trimap; fine hair detail matting; trimap free matting for robust foreground background separation in real world images; human matting for hair details transparent objects and thin structures; High quality portrait matting with hair detail; Real time video matting for human subjects.

### 4. 来源与原文
- Source：ICLR-2026-Accepted
- OpenReview：[https://openreview.net/forum?id=6K08FPo2cf](https://openreview.net/forum?id=6K08FPo2cf)
