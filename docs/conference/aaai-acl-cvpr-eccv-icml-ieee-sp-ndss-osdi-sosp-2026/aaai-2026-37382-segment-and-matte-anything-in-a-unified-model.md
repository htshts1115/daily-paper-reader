---
title: Segment and Matte Anything in a Unified Model
title_zh: 在统一模型中分割并抠取任意目标
authors: "Zezhong Fan, Xiaohan Li, Topojoy Biswas, Kaushiki Nag, Kannan Achan"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37382/41344"
tags: ["query:matting"]
score: 9.0
evidence: 统一分割与交互式图像抠图
tldr: 针对SAM掩码精度难以满足实际应用、且交互式图像抠图尚未在SAM框架中实现的问题，本文提出统一模型，将分割与抠图任务联合建模，在单一框架内实现高精度目标勾画与由多样用户提示引导的精细alpha抠图。实验表明该方法在分割与抠图任务上同时提升精度，验证了两者强相关性，为精细边界抠图提供统一方案。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37382/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1819, \"height\": 775}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37382/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 883, \"height\": 657}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37382/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 872, \"height\": 823}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37382/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 874, \"height\": 826}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37382/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1274, \"height\": 829}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37382/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1482, \"height\": 272}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37382/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 755, \"height\": 269}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37382/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 698, \"height\": 274}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37382/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 874, \"height\": 245}]"
motivation: SAM虽具强零样本分割能力，但掩码精度不足，且交互式图像抠图尚未在其框架中探索。
method: 提出统一模型，将分割与抠图关联建模，在单一框架内生成由用户提示引导的精细alpha抠图。
result: 在分割与抠图任务上同时提升精度，验证分割与抠图联合建模的可行性。
conclusion: 表明统一的分割与抠图框架可提升SAM的精细边界能力，推动交互式抠图应用。
---

## Abstract
Segment Anything (SAM) has recently pushed the boundaries of segmentation by demonstrating remarkable zero-shot generalization and flexible prompting after training on over one billion masks. Despite this, its mask prediction accuracy often falls short of the precision required in real-world applications. While several refinement modules have been proposed to boost SAM’s segmentation quality, achieving highly accurate object delineation within a single, unified framework remains an open challenge. Furthermore, interactive image matting—which aims to generate fine-grained alpha mattes guided by diverse user hints—has not yet been explored in the context of SAM. Insights from recent studies highlight strong correlations between segmentation and matting, suggesting the feasibility of a unified model capable of both tasks.

In this paper, we introduce Segment And Matte Anything (SAMA), a lightweight extension of SAM that delivers high-quality interactive image segmentation and matting with minimal extra parameters or computational cost. Our Multi-View Localization Encoder (MVLE) captures detailed features from local views, while the Localization Adapter (Local-Adapter) refines mask outputs by recovering subtle boundary details. We also incorporate two prediction heads for each task into the architecture to generate segmentation and matting tasks, simultaneously. Trained on a diverse dataset aggregated from publicly available sources, SAMA achieves state-of-the-art performance across multiple segmentation and matting benchmarks, showcasing its adaptability and effectiveness in a wide range of downstream tasks.

---

## 论文详细总结（自动生成）

# 论文总结：Segment and Matte Anything in a Unified Model（SAMA）

## 1. 核心问题与整体含义
- **研究背景**：SAM 在超过 10 亿掩码上训练后具备强零样本分割能力和灵活提示方式，但其掩码预测精度常常不足，边界不够紧致、亚像素精度和细节保持有限，难以满足真实应用需求。
- **现有问题**：HQ-SAM、DIS-SAM、SAMRefiner、Pi-SAM 等改进方法通常需要额外后处理模型、额外人工交互或级联模块，增加复杂度并降低实用性。
- **未探索方向**：交互式图像抠图——在点、框、scribble、trimap 等稀疏提示下生成精细 alpha matte——尚未在 SAM 框架中充分探索。
- **核心动机**：分割提供全局对象线索，抠图提供局部边界精度，两者具有强互补性。论文希望用一个统一、轻量框架同时完成高质量交互式分割与抠图，并保留 SAM 的零样本泛化和提示灵活性。
- **整体含义**：提出 SAMA（Segment And Matte Anything），作为 SAM 的轻量扩展，首次在 SAM 基础上联合进行交互式分割与交互式抠图，新增参数仅约 1.8%。

## 2. 方法论
- **总体思想**：冻结 SAM 全部参数，仅训练新增模块；通过多视图局部编码、局部适配器和双任务预测头，将全局语义与局部细节结合，同时输出分割 mask 和 alpha matte。
- **多视图输入**：将原图作为全局视图，同时均匀裁剪为 4 个非重叠局部 patch，上采样回原分辨率后送入同一图像编码器，得到局部特征，与全局特征进行多尺度池化和区域对应交叉注意力融合。
- **Multi-View Localization Encoder（MVLE）**：
  - 对全局特征做多感受野平均池化，得到多尺度上下文表示。
  - 将池化后的全局特征按空间位置划分为 4 个区域，与对应局部特征做多头交叉注意力。
  - 局部特征作为 query，池化全局特征作为 key/value，输出更新后的局部特征，用于增强细粒度定位。
- **Localization Adapter（Local-Adapter）**：
  - 插入 SAM 解码器层之间，将高分辨率局部特征注入解码过程。
  - 用 decoder 输出作为 query，将 MVLE 局部特征与编码器早期特征残差融合后作为 key/value，进行第一次交叉注意力。
  - 第二次交叉注意力交换 query/key/value 角色，实现 global-local 与 local-global 双向交互。
  - 用 1×1 卷积和 sigmoid 生成置信图，与第一次交叉注意力输出逐元素相乘，再加回 decoder 全局特征，以平衡细节精度与 SAM 零样本泛化，降低过拟合和灾难性遗忘风险。
- **SAMA Token 与预测头**：
  - 用两个可学习 SAMA token 分别对应分割和抠图任务，替换/扩展 SAM 输出 token；prompt token 和 SAM token 冻结，仅 SAMA token 可训练。
  - 两个轻量任务特定预测头，通过插值上采样、卷积、BN 和 GELU，分别生成分割 mask 和 alpha matte。
- **训练方式**：
  - 端到端多任务损失：\(L = L_{seg} + L_{matting}\)。
  - 分割损失：\(L_{seg} = L_{BCE} + L_{IoU} + L_{SSIM}\)，分别提供像素级、区域级和
