---
title: "Iris: Integrating Language into Diffusion-based Monocular Depth Estimation"
title_zh: "Iris:将语言融入基于扩散模型的单目深度估计"
authors: "Zeng, Ziyao, Ni, Jingcheng, Wang, Daniel, Rim, Patrick, Chung, Younjoon, Yang, Fengyu, Hong, Byung-Woo, Wong, Alex"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Zeng_Iris_Integrating_Language_into_Diffusion-based_Monocular_Depth_Estimation_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: "基于扩散模型的单目深度估计,引入语言条件"
tldr: "传统单目深度估计器常受视觉歧义与干扰影响,难以准确推断场景结构。本文提出Iris,将文本描述作为条件引入基于扩散模型的单目深度估计,利用文本到图像预训练中学到的形状与空间关系先验来缩小解空间。实验表明,融合语言信息能有效提升深度估计的保真度与鲁棒性。该工作为语言引导的单目深度基础模型提供了新思路。"
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 565, \"height\": 427}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 565, \"height\": 427}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1792, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1600, \"height\": 1215}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 1600, \"height\": 1215}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 832, \"height\": 624}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 1201, \"height\": 1236}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 1096, \"height\": 1223}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 1215, \"height\": 1168}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 4, \"index\": 13, \"width\": 268, \"height\": 580}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 4, \"index\": 14, \"width\": 1244, \"height\": 193}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 4, \"index\": 15, \"width\": 624, \"height\": 1023}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 4, \"index\": 16, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 4, \"index\": 17, \"width\": 602, \"height\": 657}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 4, \"index\": 18, \"width\": 268, \"height\": 580}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 4, \"index\": 19, \"width\": 491, \"height\": 508}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 4, \"index\": 20, \"width\": 273, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 4, \"index\": 21, \"width\": 1298, \"height\": 329}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 4, \"index\": 22, \"width\": 486, \"height\": 513}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 4, \"index\": 23, \"width\": 1292, \"height\": 309}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 4, \"index\": 24, \"width\": 1649, \"height\": 427}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 5, \"index\": 25, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 5, \"index\": 26, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 5, \"index\": 27, \"width\": 565, \"height\": 427}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 5, \"index\": 28, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 5, \"index\": 29, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 5, \"index\": 30, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 5, \"index\": 31, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 5, \"index\": 32, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 5, \"index\": 33, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 5, \"index\": 34, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 5, \"index\": 35, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 5, \"index\": 36, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 5, \"index\": 37, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 5, \"index\": 38, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 5, \"index\": 39, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 5, \"index\": 40, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 5, \"index\": 41, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 5, \"index\": 42, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 5, \"index\": 43, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 5, \"index\": 44, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 5, \"index\": 45, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 5, \"index\": 46, \"width\": 1226, \"height\": 370}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 5, \"index\": 47, \"width\": 1226, \"height\": 370}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 5, \"index\": 48, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 5, \"index\": 49, \"width\": 1242, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 5, \"index\": 50, \"width\": 1242, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 5, \"index\": 51, \"width\": 1241, \"height\": 376}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 5, \"index\": 52, \"width\": 1241, \"height\": 376}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 7, \"index\": 53, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 7, \"index\": 54, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 7, \"index\": 55, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-056.webp\", \"caption\": \"\", \"page\": 7, \"index\": 56, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-057.webp\", \"caption\": \"\", \"page\": 8, \"index\": 57, \"width\": 1200, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-058.webp\", \"caption\": \"\", \"page\": 8, \"index\": 58, \"width\": 1256, \"height\": 907}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-059.webp\", \"caption\": \"\", \"page\": 8, \"index\": 59, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-060.webp\", \"caption\": \"\", \"page\": 8, \"index\": 60, \"width\": 435, \"height\": 328}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-061.webp\", \"caption\": \"\", \"page\": 8, \"index\": 61, \"width\": 565, \"height\": 427}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zeng-iris-integrating-language-into-diffusion-based-monocular-depth-estimation-cvpr-2026-paper/fig-062.webp\", \"caption\": \"\", \"page\": 8, \"index\": 62, \"width\": 565, \"height\": 427}]"
motivation: "针对传统单目深度估计器受视觉歧义和干扰影响、估计保真度受限的问题,探索语言信息能否提供额外约束。"
method: "将文本描述作为条件注入基于扩散模型的单目深度估计器,利用文本到图像预训练隐式编码的物体形状与空间关系来约束深度解空间。"
result: "实验表明,在训练和推理中融合文本描述能降低解空间、提升深度估计的保真度与鲁棒性。"
conclusion: "语言条件为单目深度估计提供了有效先验,推动了语言引导深度基础模型的发展。"
---

## Abstract
Conventional monocular depth estimators suffer from visual ambiguities and nuisances. We demonstrate that language can improve the fidelity of estimates by providing additional information through text as a condition, thereby reducing the solution space for depth estimates. This conditional distribution is learned during text-to-image pre-training of diffusion models. To generate images under various viewpoints and layouts that reflect textual descriptions, the model implicitly encodes object shapes and their spatial relationships, comprising the 3-dimensional (3D) scene structure. We investigate the benefits of integrating text descriptions into the training and inference of the diffusion-based monocular depth estimators (MDE). We experiment with three different diffusion-based MDEs, namely Marigold, Lotus, and E2E-FT, and their variants. By training on HyperSim and Virtual KITTI, and evaluating on NYUv2, KITTI, ETH3D, ScanNet, and DIODE, we find that our strategy of integrating text into MDEs improves the overall accuracy of depth estimates, especially in small areas. The effect is also targeted in that improvements are more pronounced in specific regions described in the text. Naturally, this lends to iterative refinement of the depth estimate by providing additional descriptions of the 3D scene. Separately, we find that incorporating text can accelerate convergence of training and the inference diffusion trajectory.

---

## 论文详细总结（自动生成）

# Iris：将语言融入基于扩散模型的单目深度估计——论文深度总结

## 1. 核心问题与整体含义（研究动机与背景）

- **单目深度估计的根本困难**：从单张 RGB 图像恢复 3D 结构在几何上是病态（ill-posed）问题，存在尺度、遮挡、视角、光照、外观、纹理等多重歧义与干扰。
- **扩散模型的进展与局限**：以 Marigold、Lotus、E2E-FT 为代表的扩散式 MDE 通过逐步去噪潜在表示，能捕捉复杂结构与细节，但在以下区域仍易出错：
  - 无纹理或重复纹理区域；
  - 均匀表面；
  - 占据像素很少的物体（本身尺寸小或距离远）。
- **核心假设**：文本到图像预训练过程中，扩散模型隐式编码了物体形状、尺寸、空间关系与 3D 场景结构。若将语言描述作为额外条件引入 MDE，可**缩小与输入图像兼容的 3D 场景解空间**，从而缓解视觉歧义。
- **研究定位**：现有扩散式 MDE 仅以图像为条件，语言信息被丢弃。本文（Iris）首次系统验证将文本描述作为附加模态注入扩散式 MDE 的训练与推理，能否提升深度估计的保真度、局部精度与效率。

## 2. 方法论

### 2.1 核心思想
- 在扩散式 MDE 的条件中去噪过程中，同时以**输入图像 x** 和**文本描述 c** 为条件，预测每一步要移除的噪声，最终将高斯噪声逐步精炼为与图像和语言均对齐的深度图。
- 利用现有文本到图像扩散模型（Stable Diffusion v2）的预训练先验，避免从零训练的高昂成本。

### 2.2 关键技术细节
- **数据形式**：监督数据集 \( \mathcal{D} = \{x^{(m)}, c^{(m)}, y^{*(m)}\} \)，其中 \(y^*\) 为真值深度图，\(c\) 为对应文本描述。
- **潜在空间**：真值深度图 \(y^*\) 经冻结 VAE 编码器 \(E\) 得到潜在表示 \(z_y = E(y^*)\)；最终去噪潜在 \(z_0\) 经冻结 VAE 解码器 \(D\) 还原为深度预测 \(\hat{y} = D(z_0)\)。
- **文本编码**：文本 \(c\) 经冻结的 CLIP 文本编码器编码后输入扩散模型。
- **图像条件**：图像 \(x\) 经同一 VAE 编码器 \(E(x)\) 编码，与深度潜在 \(z_t\) 拼接后输入扩散模型。
- **骨干网络**：以 Stable Diffusion v2 的去噪 U-Net 初始化。

### 2.3 公式与算法流程（文字说明）
- **前向扩散**：逐步向潜在深度特征加入高斯噪声，\(q(z_t|z_{t-1}) = \mathcal{N}(z_t; \sqrt{1-\beta_t}\,z_{t-1}, \beta_t I)\)，其中 \(\beta_t\) 控制每步噪声方差。
- **反向扩散**：以 \(p_\theta(z_{0:T}|x,c) = p(z_T)\prod_{t=1}^{T} p_\theta(z_{t-1}|z_t,x,c)\) 定义，\(z_T\) 为标准高斯先验；每步去噪分布参数化为 \(\mathcal{N}(z_{t-1}; \mu_\theta(z_t,t,x,c), \Sigma_\theta(z_t,t,x,c))\)。
- **训练目标**：预测加入的噪声，损失为
  \[
  \mathcal{L}(\theta) = \mathbb{E}_{y,\epsilon,t}\left[\|\epsilon - \epsilon_\theta(z_t,t,x,c)\|^2\right]
  \]
  其中 \(z_t = \sqrt{\bar\alpha_t}\,z_y + \sqrt{1-\bar\alpha_t}\,\epsilon\)，\(\epsilon\sim\mathcal{N}(0,I)\)，\(\bar\alpha_t=\prod_{s=1}^{t}(1-\beta_s)\)。
- **推理**：从 \(z_T\sim\mathcal{N}(0,I)\) 出发，按 \(z_{t-1} = \frac{1}{\sqrt{\alpha_t}}\left(z_t - \frac{1-\alpha_t}{\sqrt{1-\bar\alpha_t}}\epsilon_\theta(z_t,t,x,c)\right)\) 逐步去噪至 \(t=0\)，再由冻结 VAE 解码器得到 \(\hat{y}=D(z_0)\)。
- **默认设置**：除非特别说明，“整合文本”指训练与推理阶段均使用文本条件。

### 2.4 文本描述获取
- 由于标准基准不含人工文本，使用现成视觉语言模型模拟人工标注：
  - Marigold 使用 **LLaVA v1.6**；
  - Lotus 与 E2E-FT 使用 **InternVL3-8B**；
  - 每张训练/测试图像生成一条文本描述。

## 3. 实验设计

### 3.1 数据集与场景
- **训练集**（均为合成数据，覆盖室内与室外）：
  - **HyperSim**：461 个室内场景的逼真合成数据，Marigold/E2E-FT 约 54,000 样本，Lotus 约 39,000 样本。
  - **Virtual KITTI 2**：合成街景，5 种不同天气与相机视角设置，选取 4 个场景，约 20,000 样本。
- **评估集**（5 个真实世界数据集，零样本评估，均未参与训练）：
  - NYUv2（室内）、KITTI（室外驾驶）、ETH3D、ScanNet、DIODE。

### 3.2 Benchmark 与指标
- 采用**仿射不变深度评估协议**（affine-invariant depth evaluation）。
- 指标：
  - **δ1↑**：一阶阈值精度；
  - **AbsRel↓**：平均绝对相对误差。

### 3.3 对比方法
- **非扩散/基础模型**：GeoWizard、DPT、Omnidata、Depth Anything、Depth Anything v2。
- **扩散式 MDE 基线及变体**：
  - Marigold 及其 +Text 的三种设置（Train Only、Infer Only、Train & Infer）；
  - Lotus-D、Lotus-G 及对应 +Text 设置；
  - E2E-FT (Stable Diffusion) 及 +Text 设置。
- 带 * 的为作者用开源代码重新训练与评估的结果；因计算开销，所有模型评估均不使用 ensemble。

### 3.4 额外实验维度
- **局部区域分析**：用 MaskDINO 获取 NYUv2 全景分割掩码，评估占图面积 <5%、<10%、<20% 的小区域性能。
- **迭代细化**：在原始描述后逐步追加新句子，重复推理，观察指定区域是否持续改善。
- **去噪步数分析**：比较不同推理步数下的收敛表现。
- **错误文本实验**：用错误描述替换正确描述，观察模型是否被误导。
- **训练收敛速度**：比较加入文本前后的训练收敛曲线。

## 4. 资源与算力

- **论文未明确说明**所使用的 GPU 型号、数量、训练时长或具体算力开销。
- 文中仅间接提及计算负担：
  - “Due to computational overhead, all models are evaluated without ensembling”（因计算开销，所有模型评估不使用 ensemble）；
  - “Due to computation overhead, following the same configuration of Marigold, we use a subset of KITTI and NYUv2 for training-time evaluation”（因计算开销，训练时评估仅使用 KITTI 与 NYUv2 的子集）。
- 因此，无法从本文判断其训练与推理的实际资源需求，这在一定程度上影响了可复现性与效率对比的透明度。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 3 个基础扩散式 MDE（Marigold、Lotus-D、Lotus-G、E2E-FT，实为 4 个变体）× 3 种文本整合方式（Train Only / Infer Only / Train & Infer）；
  - 5 个评估数据集上的零样本定量对比；
  - 与 5 个非扩散/基础模型的横向对比；
  - 小区域（<5%、<10%、<20%）定量分析；
  - 迭代细化定性实验；
  - 去噪步数收敛实验；
  - 错误文本误导实验；
  - 训练收敛速度对比。
- **充分性评价**：
  - 覆盖了多种基础模型、多个数据集、多种文本注入时机，实验维度较全面；
  - 同时包含定量指标与定性可视化，论证较为立体；
  - 消融实验（Train Only / Infer Only / Train & Infer）有效分离了训练与推理阶段文本条件的作用。
- **公平性与客观性**：
  - 统一采用仿射不变评估协议与 δ1/AbsRel 指标，便于横向比较；
  - 对部分基线使用官方开源代码重训重评（带 *），并明确标注不可复现的结果为灰色；
  - 但所有评估均未使用 ensemble，可能使部分基线（如 Marigold 原论文使用 ensemble）结果偏低，需注意对比口径差异；
  - 文本描述由 VLM 自动生成而非人工标注，可能影响“语言条件”质量的上限，也使得不同基础模型使用了不同 VLM，存在一定变量混淆。

## 6. 主要结论与发现

- **Finding 1（整体精度提升）**：整合文本后，扩散式 MDE 的整体深度估计精度普遍提升，归因于文本条件缩小了与输入图像兼容的 3D 场景解空间。
- **Finding 2（局部针对性改善）**：文本描述所涉及的区域深度估计明显改善，对占据像素很少的小物体尤为显著（如“皂液器”“黑色圆形底座台灯”等）。
- **Finding 3（迭代细化可行）**：通过逐步追加更详细的文本描述，可对指定区域或物体进行迭代式深度精修，可用于纠正模型的错误模式。
- **Finding 4（效率提升）**：加入语言条件可加速训练收敛，并为推理扩散轨迹提供良好初始化；整合文本仅需约 10 步去噪即可收敛，而基线需约 25 步。
- **小区域优势**：在占图 <5%、<10%、<20% 的小区域上，+Text 相比 Marigold 基线均有更明显提升（如 <5% 区域 δ1 从 91.7 提升至 92.8，AbsRel 从 9.0 降至 8.3）。
- **错误文本的负面影响**：用错误描述（如把“带玻璃的书架”替换为“带窗帘的窗户”）会误导模型，导致结构感知失败，说明方法对文本准确性敏感。

## 7. 优点

- **方法简洁且通用**：仅需在现有扩散式 MDE 中引入文本编码器与文本条件，无需重新设计网络架构，可即插即用地应用于 Marigold、Lotus、E2E-FT 等多种模型。
- **充分利用预训练先验**：借助文本到图像扩散模型已学到的物体形状与空间关系，避免从零训练的高成本。
- **多维度验证**：从整体精度、局部小区域、迭代细化、收敛速度、错误文本敏感性等多个角度系统验证语言的作用。
- **发现“效率红利”**：文本条件不仅提升精度，还加速训练收敛并减少推理去噪步数（10 步 vs 25 步），具有实际部署价值。
- **可解释性与可控性**：语言作为条件使模型行为更具针对性和可解释性，用户可通过文本描述有意识地强调易错区域。
- **实验对比相对规范**：采用统一的仿射不变评估协议，标注重训结果与不可复现结果，增强了透明度。

## 8. 不足与局限

- **对文本描述质量的强依赖**：错误、模糊或不完整的文本会直接导致深度估计性能下降，缺乏语言鲁棒性模块（如不确定性估计或一致性过滤）。
- **自动生成文本的局限**：使用 LLaVA v1.6 与 InternVL3-8B 模拟人工标注，但自动描述可能遗漏关键物体或包含噪声，未必等同于高质量人工标注；且不同基础模型使用不同 VLM，引入额外变量。
- **算力信息缺失**：未报告 GPU 型号、数量、训练时长等，难以评估方法的实际资源需求与可复现性。
- **评估口径差异**：所有模型均未使用 ensemble，而部分基线原论文使用 ensemble，可能导致对比结果不完全对等。
- **仅限仿射不变深度**：未涉及度量尺度（metric scale）深度估计，应用场景受限（如自动驾驶、机器人导航需要绝对尺度）。
- **局部评估范围有限**：小区域分析仅在 NYUv2 上进行，未在 KITTI、ETH3D、ScanNet、DIODE 等其他数据集上系统验证。
- **部分结果不可复现**：论文中灰色标注了无法用发布代码与模型复现的结果，说明部分基线对比存在不确定性。
- **文本注入方式较简单**：仅将 CLIP 文本嵌入作为条件，未探索更精细的文本-区域对齐机制（如 region-level 文本提示或 grounding）。

（完）
