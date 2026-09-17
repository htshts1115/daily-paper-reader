---
title: "From Inpainting to Layer Decomposition: Repurposing Generative Inpainting Models for Image Layer Decomposition"
title_zh: 从修补到图层分解：改造生成式修补模型用于图像图层分解
authors: "Chen, Jingxi, Zhang, Yixiao, Qian, Xiaoye, Li, Zongxia, Fermuller, Cornelia, Chen, Caren, Aloimonos, Yiannis"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Chen_From_Inpainting_to_Layer_Decomposition_Repurposing_Generative_Inpainting_Models_for_CVPR_2026_paper.pdf"
tags: ["query:matting"]
score: 6.0
evidence: 前景背景图层分解与遮挡处理
tldr: 图像可视为前景物体叠加在背景之上的分层组合，但将单张图像分解为图层的方法与数据仍然有限。该工作观察到图层分解与修补外扩任务之间存在强联系，于是通过轻量微调把基于扩散的修补模型改造成图层分解模型，并提出线性复杂度的多模态上下文融合模块以在隐空间保留细节。实验验证了该方案在图层分解与遮挡处理上的有效性，为图像编辑中的独立元素操控提供了实用途径。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 3, \"index\": 13, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 3, \"index\": 14, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 3, \"index\": 15, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 3, \"index\": 19, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 4, \"index\": 20, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 4, \"index\": 21, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 4, \"index\": 22, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 4, \"index\": 23, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 4, \"index\": 24, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 4, \"index\": 25, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 4, \"index\": 26, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 4, \"index\": 27, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 4, \"index\": 28, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 4, \"index\": 29, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 4, \"index\": 30, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 4, \"index\": 31, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 4, \"index\": 32, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 5, \"index\": 33, \"width\": 1494, \"height\": 1302}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 7, \"index\": 34, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 7, \"index\": 35, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 7, \"index\": 36, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 7, \"index\": 37, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 7, \"index\": 38, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 7, \"index\": 39, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 7, \"index\": 40, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 7, \"index\": 41, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 7, \"index\": 42, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 7, \"index\": 43, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 7, \"index\": 44, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 7, \"index\": 45, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 7, \"index\": 46, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 7, \"index\": 47, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 7, \"index\": 48, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 7, \"index\": 49, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 7, \"index\": 50, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 7, \"index\": 51, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 7, \"index\": 52, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 7, \"index\": 53, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 7, \"index\": 54, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 7, \"index\": 55, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-056.webp\", \"caption\": \"\", \"page\": 7, \"index\": 56, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-057.webp\", \"caption\": \"\", \"page\": 7, \"index\": 57, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-058.webp\", \"caption\": \"\", \"page\": 7, \"index\": 58, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-059.webp\", \"caption\": \"\", \"page\": 7, \"index\": 59, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-060.webp\", \"caption\": \"\", \"page\": 7, \"index\": 60, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-061.webp\", \"caption\": \"\", \"page\": 7, \"index\": 61, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-062.webp\", \"caption\": \"\", \"page\": 7, \"index\": 62, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-063.webp\", \"caption\": \"\", \"page\": 7, \"index\": 63, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-064.webp\", \"caption\": \"\", \"page\": 7, \"index\": 64, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-065.webp\", \"caption\": \"\", \"page\": 7, \"index\": 65, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-066.webp\", \"caption\": \"\", \"page\": 7, \"index\": 66, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-067.webp\", \"caption\": \"\", \"page\": 7, \"index\": 67, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-068.webp\", \"caption\": \"\", \"page\": 7, \"index\": 68, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-069.webp\", \"caption\": \"\", \"page\": 7, \"index\": 69, \"width\": 1024, \"height\": 800}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-070.webp\", \"caption\": \"\", \"page\": 7, \"index\": 70, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-071.webp\", \"caption\": \"\", \"page\": 7, \"index\": 71, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-072.webp\", \"caption\": \"\", \"page\": 7, \"index\": 72, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-073.webp\", \"caption\": \"\", \"page\": 7, \"index\": 73, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-074.webp\", \"caption\": \"\", \"page\": 7, \"index\": 74, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-075.webp\", \"caption\": \"\", \"page\": 7, \"index\": 75, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-076.webp\", \"caption\": \"\", \"page\": 8, \"index\": 76, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-077.webp\", \"caption\": \"\", \"page\": 8, \"index\": 77, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-078.webp\", \"caption\": \"\", \"page\": 8, \"index\": 78, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-079.webp\", \"caption\": \"\", \"page\": 8, \"index\": 79, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-080.webp\", \"caption\": \"\", \"page\": 8, \"index\": 80, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-081.webp\", \"caption\": \"\", \"page\": 8, \"index\": 81, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-082.webp\", \"caption\": \"\", \"page\": 8, \"index\": 82, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-083.webp\", \"caption\": \"\", \"page\": 8, \"index\": 83, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-084.webp\", \"caption\": \"\", \"page\": 8, \"index\": 84, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-085.webp\", \"caption\": \"\", \"page\": 8, \"index\": 85, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-086.webp\", \"caption\": \"\", \"page\": 8, \"index\": 86, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-087.webp\", \"caption\": \"\", \"page\": 8, \"index\": 87, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-088.webp\", \"caption\": \"\", \"page\": 8, \"index\": 88, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-089.webp\", \"caption\": \"\", \"page\": 8, \"index\": 89, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-090.webp\", \"caption\": \"\", \"page\": 8, \"index\": 90, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chen-from-inpainting-to-layer-decomposition-repurposing-generative-inpainting-models-for-cvpr-2026-paper/fig-091.webp\", \"caption\": \"\", \"page\": 8, \"index\": 91, \"width\": 1024, \"height\": 1024}]"
motivation: 单张图像分解为前景与背景图层的方法和数据有限，限制了内容创作中的独立元素编辑。
method: 将图层分解与修补外扩任务建立联系，通过轻量微调改造扩散修补模型，并加入线性复杂度多模态上下文融合。
result: 在保持隐空间细节的同时实现有效图层分解与遮挡处理。
conclusion: 为图像分层编辑提供了可复用的生成式方案。
---

## Abstract
Images can be viewed as layered compositions, foreground objects over background, with potential occlusions. This layered representation enables independent editing of elements, offering greater flexibility for content creation. Despite the progress in large generative models, decomposing a single image into layers remains challenging due to limited methods and data. We observe a strong connection between layer decomposition and in/outpainting tasks, and propose adapting a diffusion-based inpainting model for layer decomposition using lightweight finetuning. To further preserve detail in the latent space, we introduce a novel multi-modality context fusion module with linear attention complexity. Our model is trained purely on a synthetic dataset constructed from open-source assets and achieves superior performance in object removal and occlusion recovery, unlocking new possibilities in downstream editing and creative applications.

---

## 论文详细总结（自动生成）

# 论文总结：《从修补到图层分解：改造生成式修补模型用于图像图层分解》

## 1. 核心问题与研究动机

- **研究背景**：图像可视为“前景物体叠加在背景之上”的分层组合，且前景常带有遮挡关系。这种图层化表示允许对元素进行独立编辑（如重新合成、分层艺术创作、组件化检索），比单层图像具备更高的创作灵活性。
- **核心问题**：尽管扩散模型在图像生成与编辑上进展显著，**将单张图像分解为前景层与背景层**（同时完成前景提取、遮挡恢复与背景去除）仍是一个探索不足的任务，主要瓶颈在于**可用方法与高质量图层标注数据都极为稀缺**。
- **现有方案痛点**：近期工作 LAYERDECOMP 通过**全量微调闭源文生图模型**并在大规模精选数据上训练来实现该任务，但计算与数据成本极高，普通研究者与开发者难以复现。
- **关键洞察**：作者观察到图层分解与**修补（inpainting）/外扩（outpainting）**存在结构性统一关系——
  - 背景层 ≈ 对掩码区域做修补填充；
  - 前景层 ≈ 对未掩码区域做外扩并附加 alpha 通道，掩码外 alpha 强制为零。
- **整体含义**：若能把已开源的修补模型以**参数与数据高效**的方式改造为图层分解模型，就能实现“即插即用”的能力复用，并随未来修补模型进步而受益。

## 2. 方法论：Outpaint-and-Remove

### 2.1 核心思想
- 不从头训练，而是把图层分解**重新表述为修补 + 外扩的组合**，基于预训练修补 DiT 做轻量适配，同时输出：① 带遮挡恢复的 RGBA 前景；② 已去除物体的干净背景。

### 2.2 关键技术细节

- **基座模型**：FLUX.1-Fill-dev（扩散 Transformer，DiT），权重冻结。
- **多模态上下文 Tokenization**：
  - 从输入图像生成 **边缘图（Canny）、分割图（SegFormer）、深度图（Depth-Anything-V2）**；
  - 利用预训练 DiT 的 VAE 编码器将这些图像类输入统一 token 化。
- **多模态隐空间融合（Multi-Modal Latent Fusion）**：
  - 直接拼接多模态 token 会带来计算爆炸（标准注意力为 O(K²)）；
  - 采用**线性注意力**思路，用少量常数个（N ≪ K）**隐 token 作为 query**，把复杂度降到约 **O(KN)**，与输入 token 数呈线性关系。
- **图像–掩码上下文设计（核心创新之一）**：
  - 标准修补模型仅使用背景上下文 `c^b_{I−M}`；
  - 本文额外引入**前景图像–掩码上下文** `c^f_{I−M}`，作为控制信号，帮助模型在“保留已有信息”与“生成新内容”之间取得平衡，抑制前景区域幻觉。
  - 最终输入按通道拼接：
    - 前景：`concat(z^f_t, c^f_{I−M}, c_MM)`
    - 背景：`concat(z^b_t, c^b_{I−M}, c_MM)`
  - DiT 接收两条各 N 个 token 的序列（前景/背景各一条）。
- **参数高效微调（PEFT）**：
  - 微调**输入投影层**以容纳新增通道；
  - 在 DiT 的**每个注意力层与前馈层插入 LoRA**；基座权重冻结。
  - LoRA rank 是关键超参（见消融）。
- **解码**：
  - 背景为 RGB，直接复用预训练 VAE 编解码器；
  - 前景为 RGBA，**单独微调一个 RGBA 编码器/解码器**。
- **训练目标**：标准 flow matching 损失。

### 2.3 训练数据构造（全公开资源）
- 三个来源：
  1. **真实前景**（MULAN）：细节丰富但形状不完整、遮挡/背景纠缠；
  2. **合成前景**（LayerDiffuse，由 ChatGPT-4o 生成的前景提示词引导）：形状完整但纹理过平滑；
  3. **背景**（OpenImages），与缩放后的前景叠加合成逼真场景。
- 每张训练图含 **1–3 个前景物体**并可能带遮挡；**故意使用不完美掩码**，让模型学会推断准确边界。
- 总计 **10 万组“图像–前景–背景”三元组**。

## 3. 实验设计

### 3.1 数据集与评测场景
- **定量评测**：MULAN 测试集 **526 张图像**（作者称其为该领域唯一标准数据集）。
- **前景层评测**：自收集 **40 张多样化高质量真实图像**。
- **用户研究**：**18 位独立研究者**参与，评估前景提取质量。

### 3.2 评价指标
- PSNR ↑、SSIM ↑、LPIPS ↓、FID ↓，另加**用户偏好率**。

### 3.3 对比方法
- **背景去除（物体移除）对比**：SD-XL Inpainting、PowerPaint、BrushNet、OmniEraser、GeoRemover、Qwen-Image-Edit，以及基座模型 FLUX.1-Fill-dev。
- **前景提取对比**：由于无开源图层分解方法，改用两个抠图方法 MattingAnything、DiffMatte 作为代理基线。

### 3.4 主要结果
- **背景去除**：Ours 在所有指标上最优（PSNR 27.30、SSIM 0.93、LPIPS 0.08、FID 25.97）；相对基座 FLUX.1-Fill-dev **PSNR 提升 1.71 dB、FID 降低 9.99**。
- **前景提取**：Ours 在 PSNR/SSIM/LPIPS 上略逊于 DiffMatte（28.38 vs 29.69 等），但**用户偏好率最高（59.51% vs 32.34% / 8.15%）**，说明客观指标与人眼偏好存在差距。

## 4. 资源与算力

- 文中明确给出的训练配置：
  - **输入分辨率 1024×1024**；
  - **batch size 8**；
  - **学习率 5e−5**；
  - **训练 7200 次迭代**；
  - 默认 **LoRA rank 256**；
  - 使用标准 flow matching 损失。
- **未明确说明的部分**：论文**未披露 GPU 型号、GPU 数量、总训练时长或显存占用**等硬件与算力细节。虽然作者强调方法“数据与参数高效”，但缺少具体算力开销数据，无法直接核算其实际训练成本。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 1 组背景去除主实验（7 个基线 + 本方法，4 项指标）；
  - 1 组前景提取对比（2 个抠图基线 + 本方法，4 项指标 + 用户研究）；
  - 1 组完整消融（**10 行**）：LoRA rank（128 / 256 / 1024）、去掉前景上下文 `c^f_{I−M}`、去掉多模态上下文 `c_MM`、去掉合成前景数据、替换基座为 Kontext、分别去掉 edge/seg/depth；
  - 若干定性对比（真实图像、编辑示例）与失败案例分析。
- **充分性与公平性评估**：
  - **优点**：消融维度覆盖较全，涵盖骨干选择、数据来源、上下文设计、各模态贡献、LoRA rank，且对“为何选择修补模型而非通用图生图模型”做了对照验证。
  - **待商榷之处**：
    - 定量评测**主要依赖 MULAN 单一数据集**，且该数据集标注本身由现成模型生成、质量无保证；
    - 前景层评测仅 40 张自采图像，用户研究仅 18 人，样本规模偏小；
    - 前景提取对比使用抠图方法作为代理基线，并非同一任务的直接竞争者，比较的公平性有限；
    - 缺少训练数据规模、算力开销等可复现性细节。

## 6. 主要结论与发现

- 图层分解与修补/外扩存在**内在结构统一性**，可以把图层分解视为“背景修补 + 前景外扩（带透明度约束）”的组合。
- **修补模型比通用图生图模型更适合作为该任务的适配基座**：换成 FLUX.1-Kontext-dev 后性能明显下降。
- 仅用**公开数据 + 轻量 LoRA 适配**即可在图层分解与物体移除上达到 SOTA，显著降低数据与算力门槛。
- **双上下文设计（前景 + 背景图像–掩码上下文）是抑制幻觉、忠实保留前景内容的关键**；去掉后 PSNR 下降 0.26 dB，且前景开始被篡改/幻觉。
- **多模态上下文（深度/分割/边缘）提升背景修补质量**，帮助模型理解待填充区域的语义。
- **LoRA rank 存在权衡**：128 不足以学会新任务，1024 会覆盖预训练先验导致幻觉，256 为最佳平衡。
- **合成前景数据有效**：混合“细节丰富但形状不完整的真实前景”与“形状完整但纹理欠佳的合成前景”，能提升训练效果。

## 7. 优点

- **视角新颖**：首次系统性地把预训练修补模型改造用于图像图层分解，并给出修补/外扩与图层分解的结构性统一论证。
- **参数与数据高效**：LoRA + 输入层微调，仅 7200 步训练；训练数据全部来自开源资源，可复现、易推广，无需商业级数据集。
- **模块设计有针对性与理论依据**：
  - 线性注意力的多模态隐融合（O(KN)）在保留细节的同时控制计算开销；
  - 双图像–掩码上下文显式区分“需生成区”与“需保留区”，直接针对扩散模型的幻觉问题。
- **数据策略巧妙**：用真实前景与合成前景互补，并**故意使用不完美掩码**以增强模型对掩码误差的鲁棒性。
- **评测维度较完整**：客观指标 + 用户研究 + 定性对比 + 失败案例分析，且消融设计清晰成体系。
- **下游应用价值明确**：图层分解可直接支撑分层编辑、创意重合成等实际场景。

## 8. 不足与局限

- **失败场景**：在**杂乱物体、大范围遮挡、手指捏持的小物体**等复杂图像上失败；作者归因于合成训练数据缺乏此类精细样本。
- **数据依赖风险**：
  - 训练数据完全依赖 MULAN、LayerDiffuse、OpenImages 等公开资源，其中 MULAN 的 RGBA 图层由现成模型生成，**质量无保证**，可能引入偏差；
  - LayerDiffuse 合成前景纹理过平滑，可能限制细节上限。
- **评测覆盖有限**：
  - 定量评测集中于 MULAN 单数据集，泛化性证据不足；
  - 前景层评测样本仅 40 张，用户研究仅 18 人，统计效力有限；
  - 缺乏与真正图层分解方法（如 LAYERDECOMP）的定量直接对比（受限于其闭源/大算力特性）。
- **指标与人眼偏好不一致**：前景提取上客观指标落后于 DiffMatte，却赢得用户偏好，说明现有指标对该任务可能不够适配。
- **算力信息缺失**：未报告 GPU 型号、数量、训练时长，削弱了“高效”主张的可验证性。
- **技术限制**：掩码质量仍强烈影响结果（不完整掩码会导致前景区域被幻觉或篡改），实际使用中对输入掩码有一定依赖。
- **应用限制**：基座模型为非商业许可（FLUX.1-Fill-dev），实际商业落地存在授权约束。

（完）
