---
title: "Beyond Appearance: Camouflaged Object Detection via Geometric Structure"
title_zh: 超越外观：基于几何结构的伪装目标检测
authors: "Han, Jinyu, Wu, Changguang, Sun, Fuming, Tang, Jinhui"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Han_Beyond_Appearance_Camouflaged_Object_Detection_via_Geometric_Structure_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 4.0
evidence: 利用单目深度估计先验进行伪装目标检测
tldr: 深度先验能提供显著几何结构以辅助伪装目标检测，但直接使用单目深度估计会带来任务错配而仍难以识别伪装目标。本文提出DepthSAM，一种适配单目深度估计的方法，包含稀疏专家适配器与几何语义融合模块，将几何线索与高层语义高效整合。实验表明该方法在伪装环境中兼具鲁棒语义理解与几何感知能力。该工作说明深度先验需经任务适配才能更好服务于下游检测任务。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
motivation: 直接使用单目深度估计先验进行伪装目标检测存在任务错配，仍难以识别目标。
method: 提出DepthSAM，含稀疏专家适配器与几何语义融合模块，将深度几何线索与高层语义结合。
result: 在伪装环境下实现鲁棒语义理解与几何感知，提升伪装目标检测效果。
conclusion: 表明深度先验需经任务适配才能有效服务下游任务。
---

## Abstract
Depth priors provide salient geometric structure that benefits camouflaged object detection (COD), but directly using Monocular Depth Estimation (MDE) causes a task misalignment that still fails to identify camouflaged objects.To address this issue, we propose the Depth Segment Anything Model (DepthSAM), a MDE-adapted method specifically designed to mitigate this misalignment.DepthSAM incorporates two core innovations: (1) a Sparse Mixture-of-Experts Adapter (SMEA) that enables MDE to learn semantic information unique to camouflaged scenes, and (2) a Geometric-Semantic Fusion Module (GSFM) that efficiently integrates geometric cues with high-level semantics. With these components, DepthSAM achieves both robust semantic understanding in camouflaged environments and accurate segmentation of camouflaged objects.Extensive experiments show that DepthSAM achieves new SOTA performance on three major benchmarks. For example, on COD10K, its S_ \alpha and F_ b ^ \omega metrics surpass the best competing methods by 3.0% and 4.3%, respectively.

---

## 论文详细总结（自动生成）

# 论文总结：Beyond Appearance: Camouflaged Object Detection via Geometric Structure

## 1. 核心问题与整体含义
- **研究背景**：伪装目标检测（COD）旨在识别与周围环境高度融合的目标，广泛用于医学图像分析、军事侦察、灾害评估等。现有方法多依赖 RGB 图像中的颜色、纹理等**弱外观线索**，从 CNN、Transformer 到 SAM 等基础模型，本质仍是“从外观中挖掘差异”。
- **核心问题**：极端伪装会使外观线索缺失或具有欺骗性，导致现有方法性能受限。单目深度估计（MDE）可提供更鲁棒的几何结构先验，但**直接使用 MDE 存在任务错配**：MDE 目标是场景级几何重建，而 COD 目标是目标级分割；当目标几何与背景深度交织时，MDE 会不加区分地重建二者，仍无法突出伪装目标。
- **整体含义**：论文提出 **DepthSAM**，首次将 MDE 基础模型适配到 COD，通过调制 MDE 内部特征并融合几何与语义，解决“场景级重建 vs. 目标级分割”的错配，在多个基准上取得 SOTA。

## 2. 方法论
- **总体架构**：基于预训练 MDE 模型 **Depth Anything v2（DAv2）**，包含 DINOv2 编码器与 DPT 解码器。编码器与解码器保持冻结，在编码器 Transformer Block 前注入 **SMEA**，再用 **GSFM** 融合解码器多尺度输出，最后由轻量卷积预测头输出掩码。
- **Sparse Mixture-of-Experts Adapter（SMEA）**：
  - 目的：让冻结的 MDE 编码器特征从“通用场景几何”转向“伪装目标几何”。
  - 结构：由 N 个轻量专家和一个门控网络组成，门控仅激活 Top-K（默认 K=2）专家。
  - 公式：\(x_m = x + (\sum_{i=1}^{N} g_i E_i(x)) / \sum_{i=1}^{N} g_i\)，其中 \(g_i \in \text{Top-K}(G(x))\)。残差连接保证稳定训练。
  - 作用：SMEA 在特征进入冻结 DINOv2 块前进行调制，进而影响冻结 DPT 解码器，使其多尺度输出 \(\{F_1,F_2,F_3,F_4\}\) 偏向伪装目标结构。辅助损失用于保证专家稀疏性。
- **Geometric-Semantic Fusion Module（GSFM）**：
  - 目的：融合浅层几何细节与深层语义信息。
  - 结构：采用渐进融合，按浅到深级联 **Spatial-Frequency Refinement Module（SFRM）**：\(F_o = \text{SFRM}(\text{SFRM}(\text{SFRM}(F_4,F_3),F_2),F_1)\)。
  - SFRM 核心：双域设计，空间流捕捉局部几何，频率流（FFT）捕捉全局语义；通过四路并行 MHSA 交互：空间自注意力、频率自注意力、几何引导语义、语义引导几何。
  - 最终 \(F_o\) 经两个卷积层映射为单通道预测掩码 \(P\)。
- **损失函数**：\(L = L_{BCE} + L_{IO
