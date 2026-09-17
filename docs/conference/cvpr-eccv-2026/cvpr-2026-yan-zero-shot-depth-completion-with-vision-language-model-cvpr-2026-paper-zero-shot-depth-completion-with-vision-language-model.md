---
title: Zero-Shot Depth Completion with Vision-Language Model
title_zh: 基于视觉语言模型的零样本深度补全
authors: "Yan, Zhiqiang, Wu, Yuan, Lee, Gim Hee"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Yan_Zero-Shot_Depth_Completion_with_Vision-Language_Model_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于视觉语言模型的零样本深度补全
tldr: 视觉语言模型在语言引导的语义理解任务上表现优异，但其几何感知潜力仍未被充分探索。本文提出首个基于VLM的深度补全框架，在几乎不修改架构的前提下引入稀疏深度注入机制，从视觉标记化、文本提示与文本监督三方面扩展模型的3D感知能力：稀疏深度被标记化以提供绝对尺度并缓解尺度与相机歧义，由稀疏深度导出的二值掩码作为提示引导模型。实验表明该框架实现零样本深度补全，拓展了VLM在几何任务中的应用。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 472, \"height\": 354}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 473, \"height\": 355}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 472, \"height\": 354}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 472, \"height\": 354}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 473, \"height\": 354}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 7, \"index\": 10, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 7, \"index\": 12, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 7, \"index\": 13, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 7, \"index\": 14, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 7, \"index\": 15, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 7, \"index\": 16, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 8, \"index\": 17, \"width\": 934, \"height\": 701}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 8, \"index\": 18, \"width\": 934, \"height\": 701}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 8, \"index\": 19, \"width\": 719, \"height\": 539}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 8, \"index\": 20, \"width\": 719, \"height\": 539}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 8, \"index\": 21, \"width\": 502, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yan-zero-shot-depth-completion-with-vision-language-model-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 502, \"height\": 352}]"
motivation: 视觉语言模型在语义理解上成功，但几何感知潜力尚未被充分挖掘。
method: 提出首个基于VLM的深度补全框架，通过稀疏深度注入机制扩展VLM的3D感知能力。
result: 稀疏深度被视觉标记化以提供绝对尺度，文本提示与监督引导模型，实现零样本深度补全。
conclusion: 几乎无需改动架构即可将VLM拓展至几何感知任务。
---

## Abstract
Vision language models (VLMs) have achieved remarkable success in semantic understanding tasks under language guidance, yet their potential for geometric perception remains largely underexplored. This paper introduces the first VLM-based depth completion framework. With almost no architectural modifications, we propose a sparse depth injection mechanism that extends the capability of VLM toward 3D perception through three key aspects: visual tokenization, textual prompt, and textual supervision. At the visual input side, sparse depth is tokenized to provide absolute scale and accurate geometric cues, alleviating the scale and camera ambiguities of RGB-only inputs. At the textual input side, a binary mask derived from sparse depth serves as a prompt, instructing the model where to complete and where to preserve. At the supervision side, the model is fine-tuned using text labels generated from sparse depth, requiring no ground-truth depth. Benefiting from the strong semantic priors and cross-modal expressiveness of VLM, our framework achieves superior zero-shot performance across diverse sensors, sparsity levels, and scenes.

---

## 论文详细总结（自动生成）

# 论文总结：Zero-Shot Depth Completion with Vision-Language Model

## 1. 核心问题与研究动机
- **任务背景**：深度补全旨在从稀疏深度图恢复稠密深度，通常辅以 RGB 图像。该任务对自动驾驶、3D 重建、具身智能等至关重要。
- **现有方法不足**：
  - 早期方法依赖任务专用架构、空间传播网络或 RGB-D 融合，跨域泛化有限。
  - 近期零样本方法借助深度基础模型或扩散模型，但仍主要是把稀疏深度“嵌入”网络，并未真正显式区分“哪里需要预测、哪里需要保留”。
  - 视觉语言模型（VLM）在语义理解与指令跟随上表现突出，但其几何感知潜力尚未被充分挖掘。
- **论文目标**：提出首个基于 VLM 的深度补全框架，通过稀疏深度注入机制，让 VLM 同时利用视觉、几何和文本线索，实现跨传感器、跨稀疏度、跨场景的零样本深度补全。

## 2. 方法论
- **核心思想**：在几乎不修改 VLM 架构的前提下，将稀疏深度以三种方式注入 VLM：视觉标记化、文本提示、文本监督，统称为稀疏深度注入机制（SDIM）。
- **视觉标记化**：
  - 输入 RGB 图像 \(I\) 和稀疏深度 \(S\)。
  - 稀疏深度经 32 通道零初始化卷积、BN、LeakyReLU 编码；RGB 经类似操作编码。
  - RGB-D 特征拼接后，经高维/低维投影，再由零初始化卷积输出 \(O\)。
  - \(O\) 经 3D 卷积嵌入后，与 RGB 图像 token 相加，送入 VLM 视觉编码器。
  - 该设计属于“软融合”，相比直接拼接 RGB-D 的“硬融合”，能更平滑地注入深度先验，并保持与预训练图像 token 分布接近。
- **文本提示**：
  - 从稀疏深度生成二值 mask：0 表示缺失深度，1 表示有效深度。
  - 将 mask 转为固定模板文本：
