---
title: User-Instructed Disparity-aware Defocus Control
title_zh: 用户指令式视差感知虚化控制
authors: "Yudong Han, Yan Yang, Hao Yang, Liyuan Pan"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=j38Cb5LlaY"
tags: ["query:neural-bokeh"]
score: 7.0
evidence: 用户指令式虚化控制，模拟对焦与失焦区域
tldr: 全清晰照片往往无法表达创作者意图，但单镜头相机难以估计与深度相关的像差，使得景深控制十分困难。本文提出用户指令式景深控制框架UiD，允许用户以文本、框或点提示指定重新对焦区域，自动模拟画面中的清晰与虚化区域。该框架实现了可控的神经虚化渲染，为学习式景深编辑与前景背景层次控制提供了可行方案。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 全清晰图像难以传达创作意图，而单镜头相机因难以估计深度相关像差，景深虚化控制始终困难。
method: 提出UiD框架，允许用户以文本、框或点提示指定重新对焦区域，自动模拟清晰与失焦区域。
result: 该方法实现了用户可控的景深虚化模拟，可灵活调整画面清晰与模糊区域，提升创作表达与图像质量。
conclusion: 指令式视差感知虚化控制为单镜头相机上的学习式景深渲染提供了可行方案。
---

## Abstract
In photography, an All-in-Focus (AiF) image may not always effectively convey the creator’s intent. Professional photographers manipulate Depth of Field (DoF) to control which regions appear sharp or blurred, achieving compelling artistic effects. 
For general users, the ability to flexibly adjust DoF enhances creative expression and image quality. 
In this paper, we propose UiD, a User-Instructed DoF control framework, that allows users to specify refocusing regions using text, box, or point prompts, and our UiD automatically simulates in-focus and out-of-focus (OoF) regions in the given images.
However, controlling defocus blur in a single-lens camera remains challenging due to the difficulty in estimating depth-aware aberrations and the suboptimal quality of reconstructed AiF images. To address this, we leverage dual-pixel (DP) sensors, commonly found in DSLR-style and mobile cameras. DP sensors provide a small-baseline stereo pair in a single snapshot, enabling depth-aware aberration estimation. Our approach first establishes an invertible mapping between OoF and AiF images to learn spatially varying defocus kernels and the disparity features. These depth-aware kernels enable bidirectional image transformation—deblurring out-of-focus (OoF) images into all-in-focus (AiF) representations, and conversely reblurring AiF images into OoF outputs—by seamlessly switching between the kernel and its inverse form. These depth-aware kernels enable both deblurring of OoF images into AiF representations and reblurring AiF images into OoF representations by flexibly switching its original form to its inverse one. For user-guided refocusing, we first generate masks based on user prompts using SAM, which modulates disparity features in closed form, allowing dynamic kernel re-estimation for reblurring. This achieves user-controlled refocusing effects. Extensive experiments on both common datasets and the self-collected dataset demonstrate that UiD offers superior flexibility and quality in DoF manipulation imaging.

---

## 论文详细总结（自动生成）

### 1. 检索相关性
用户指令式虚化控制，模拟对焦与失焦区域。

### 2. 核心内容
全清晰照片往往无法表达创作者意图，但单镜头相机难以估计与深度相关的像差，使得景深控制十分困难。本文提出用户指令式景深控制框架UiD，允许用户以文本、框或点提示指定重新对焦区域，自动模拟画面中的清晰与虚化区域。该框架实现了可控的神经虚化渲染，为学习式景深编辑与前景背景层次控制提供了可行方案。

### 3. 对应检索需求
Papers central to 神经网络虚化、学习式景深渲染、人像散景渲染，重点关注 depth/matting/seg 联合使用。, especially work that connects or combines: depth-aware blur; learned defocus blur; neural network based bokeh rendering; learned depth of field rendering with neural networks; portrait bokeh rendering using depth and matting; bokeh synthesis with depth and segmentation; depth aware blur rendering with occlusion and boundary handling; learned defocus blur for realistic foreground background composition; neural bokeh rendering for portrait photography and mobile devices; deep learning based bokeh synthesis from single image.

### 4. 来源与原文
- Source：NeurIPS-2025-Accepted
- OpenReview：[https://openreview.net/forum?id=j38Cb5LlaY](https://openreview.net/forum?id=j38Cb5LlaY)
