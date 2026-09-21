---
title: Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention
title_zh: 基于线性注意力像素空间扩散的高效高质深度估计
authors: "Bingde Liu, Wu Ran, Jinglei Zhang, Huanhuan Yuan, Chao Ma"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1498.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于像素空间扩散的高效高质量单目深度估计
tldr: 针对生成式单目深度估计虽细节保真好，但标准注意力O(N^2)复杂度和多步去噪在高分辨率下代价过高的问题，论文提出Lapis线性注意力像素空间生成框架，实现一步扩散的高效高保真深度估计。它通过由粗到细的层级结构与补丁级一致性模块，缓解直接使用线性注意力与一步预测带来的结构不一致、细节丢失与噪声。实验表明该方法在效率与精度上兼顾，适合移动端深度模型。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1008, \"height\": 1520}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 1008, \"height\": 1520}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1008, \"height\": 1512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 1008, \"height\": 1512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 3428, \"height\": 5135}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1980, \"height\": 2475}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1664, \"height\": 2224}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 1666, \"height\": 2212}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 1664, \"height\": 2224}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 1666, \"height\": 2212}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 490, \"height\": 616}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 496, \"height\": 624}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 496, \"height\": 624}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 490, \"height\": 616}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 3200, \"height\": 3999}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 784, \"height\": 1168}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 1168, \"height\": 1760}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 1568, \"height\": 2352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-019.webp\", \"caption\": \"\", \"page\": 3, \"index\": 19, \"width\": 659, \"height\": 988}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-020.webp\", \"caption\": \"\", \"page\": 3, \"index\": 20, \"width\": 448, \"height\": 672}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-021.webp\", \"caption\": \"\", \"page\": 3, \"index\": 21, \"width\": 784, \"height\": 1168}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-022.webp\", \"caption\": \"\", \"page\": 3, \"index\": 22, \"width\": 1168, \"height\": 1760}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-023.webp\", \"caption\": \"\", \"page\": 3, \"index\": 23, \"width\": 1568, \"height\": 2352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-024.webp\", \"caption\": \"\", \"page\": 3, \"index\": 24, \"width\": 292, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-025.webp\", \"caption\": \"\", \"page\": 3, \"index\": 25, \"width\": 448, \"height\": 672}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-032.webp\", \"caption\": \"\", \"page\": 8, \"index\": 32, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-033.webp\", \"caption\": \"\", \"page\": 8, \"index\": 33, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-034.webp\", \"caption\": \"\", \"page\": 8, \"index\": 34, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-035.webp\", \"caption\": \"\", \"page\": 8, \"index\": 35, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-036.webp\", \"caption\": \"\", \"page\": 8, \"index\": 36, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-037.webp\", \"caption\": \"\", \"page\": 8, \"index\": 37, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-038.webp\", \"caption\": \"\", \"page\": 8, \"index\": 38, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-039.webp\", \"caption\": \"\", \"page\": 8, \"index\": 39, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-040.webp\", \"caption\": \"\", \"page\": 8, \"index\": 40, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-041.webp\", \"caption\": \"\", \"page\": 8, \"index\": 41, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-042.webp\", \"caption\": \"\", \"page\": 10, \"index\": 42, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-043.webp\", \"caption\": \"\", \"page\": 10, \"index\": 43, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-044.webp\", \"caption\": \"\", \"page\": 10, \"index\": 44, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-045.webp\", \"caption\": \"\", \"page\": 10, \"index\": 45, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-046.webp\", \"caption\": \"\", \"page\": 10, \"index\": 46, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-047.webp\", \"caption\": \"\", \"page\": 10, \"index\": 47, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-048.webp\", \"caption\": \"\", \"page\": 10, \"index\": 48, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-049.webp\", \"caption\": \"\", \"page\": 10, \"index\": 49, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-050.webp\", \"caption\": \"\", \"page\": 10, \"index\": 50, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-051.webp\", \"caption\": \"\", \"page\": 10, \"index\": 51, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-052.webp\", \"caption\": \"\", \"page\": 10, \"index\": 52, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-053.webp\", \"caption\": \"\", \"page\": 10, \"index\": 53, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-054.webp\", \"caption\": \"\", \"page\": 10, \"index\": 54, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-055.webp\", \"caption\": \"\", \"page\": 10, \"index\": 55, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-056.webp\", \"caption\": \"\", \"page\": 10, \"index\": 56, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-057.webp\", \"caption\": \"\", \"page\": 10, \"index\": 57, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-058.webp\", \"caption\": \"\", \"page\": 10, \"index\": 58, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-059.webp\", \"caption\": \"\", \"page\": 10, \"index\": 59, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-060.webp\", \"caption\": \"\", \"page\": 10, \"index\": 60, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-061.webp\", \"caption\": \"\", \"page\": 10, \"index\": 61, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-062.webp\", \"caption\": \"\", \"page\": 10, \"index\": 62, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-063.webp\", \"caption\": \"\", \"page\": 10, \"index\": 63, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-064.webp\", \"caption\": \"\", \"page\": 10, \"index\": 64, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-065.webp\", \"caption\": \"\", \"page\": 10, \"index\": 65, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-066.webp\", \"caption\": \"\", \"page\": 10, \"index\": 66, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-067.webp\", \"caption\": \"\", \"page\": 10, \"index\": 67, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-068.webp\", \"caption\": \"\", \"page\": 10, \"index\": 68, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-069.webp\", \"caption\": \"\", \"page\": 10, \"index\": 69, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-070.webp\", \"caption\": \"\", \"page\": 10, \"index\": 70, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-071.webp\", \"caption\": \"\", \"page\": 10, \"index\": 71, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-072.webp\", \"caption\": \"\", \"page\": 10, \"index\": 72, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-073.webp\", \"caption\": \"\", \"page\": 10, \"index\": 73, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-074.webp\", \"caption\": \"\", \"page\": 10, \"index\": 74, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-075.webp\", \"caption\": \"\", \"page\": 10, \"index\": 75, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-076.webp\", \"caption\": \"\", \"page\": 10, \"index\": 76, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-077.webp\", \"caption\": \"\", \"page\": 10, \"index\": 77, \"width\": 1242, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-078.webp\", \"caption\": \"\", \"page\": 10, \"index\": 78, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-079.webp\", \"caption\": \"\", \"page\": 10, \"index\": 79, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-080.webp\", \"caption\": \"\", \"page\": 10, \"index\": 80, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-081.webp\", \"caption\": \"\", \"page\": 10, \"index\": 81, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-082.webp\", \"caption\": \"\", \"page\": 10, \"index\": 82, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-083.webp\", \"caption\": \"\", \"page\": 10, \"index\": 83, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-084.webp\", \"caption\": \"\", \"page\": 10, \"index\": 84, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-085.webp\", \"caption\": \"\", \"page\": 10, \"index\": 85, \"width\": 2473, \"height\": 1649}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-086.webp\", \"caption\": \"\", \"page\": 14, \"index\": 86, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-087.webp\", \"caption\": \"\", \"page\": 14, \"index\": 87, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-088.webp\", \"caption\": \"\", \"page\": 14, \"index\": 88, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-089.webp\", \"caption\": \"\", \"page\": 14, \"index\": 89, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-090.webp\", \"caption\": \"\", \"page\": 14, \"index\": 90, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-091.webp\", \"caption\": \"\", \"page\": 14, \"index\": 91, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-092.webp\", \"caption\": \"\", \"page\": 14, \"index\": 92, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-093.webp\", \"caption\": \"\", \"page\": 14, \"index\": 93, \"width\": 2048, \"height\": 1360}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-48368ce368a1c6b74d35eb8b/fig-094.webp\", \"caption\": \"\", \"page\": 14, \"index\": 94, \"width\": 2473, \"height\": 1649}]"
motivation: 生成式单目深度估计细节保真好，但标准注意力复杂度高、多步去噪代价大，难扩展到高分辨率。
method: 提出Lapis线性注意力像素空间生成框架，以由粗到细层级和补丁级一致性模块实现一步扩散深度估计。
result: 实验表明该方法在保持高保真深度细节的同时显著降低计算开销。
conclusion: 为移动端高效单目深度估计提供了可行方案。
---

## Abstract
This work presents Lapis, a linear-attention-based pixel-space generative framework that achieves efficient and high-fidelity depthestimation with one-step diffusion. While generative frameworks havesignificantly advanced monocular depth estimation with superior detailfidelity, the O(N 2 ) complexity of standard attention and the multi-stepdenoising process introduce prohibitive computational costs when scal-ing them to high-resolution image applications. Although linear atten-tion and one-step prediction are intuitively viable, directly applying themleads to poor structural consistency, detail loss, and noise. Lapis recti-fies these limitations through a coarse-to-fine hierarchy. Specifically, aPatch-level Consistency Module restores structural coherence by inte-grating semantic and spatial priors. Subsequently, a Pixel-level Refine-ment Module recovers sharp geometric boundaries via skip-connection-based pixel correspondence. Furthermore, to mitigate sampling noise in-herent in one-step diffusion, we leverage the manifold assumption andadopt a direct x-prediction strategy to target the clean data manifold.Extensive evaluations on multiple benchmarks demonstrate that Lapisconsistently achieves state-of-the-art (SOTA) accuracy and boundarysharpness across various resolutions, reducing inference latency by upto 7.6× at 1080P and 10.9× at 1440P resolution compared to previousSOTA generative models.

---

## 论文详细总结（自动生成）

# 论文总结：基于线性注意力像素空间扩散的高效高质深度估计（Lapis）

## 1. 核心问题与整体含义

- **研究背景**：单目深度估计（MDE）是3D/4D感知与重建的基础任务。近年来该领域从判别式回归转向生成式框架，生成式方法在细节保真度上显著优于判别式方法。
- **核心矛盾**：当应用要求高分辨率以捕捉像素级几何时，现有生成式框架面临**保真度与效率的根本权衡**：
  - **隐空间U-Net路线**：继承预训练图像生成器的隐空间架构，但受VAE瓶颈的不可逆信息损失限制，且难以捕捉高分辨率下的长程依赖。
  - **像素空间DiT路线**：消除隐空间瓶颈、保持长程一致性，但标准注意力O(N²)复杂度在高分辨率下计算不可行，且多步迭代采样进一步放大开销。
- **直观方案的困境**：直接采用线性注意力 + 一步采样虽在直觉上可行，但会导致**结构一致性差、细节丢失和噪声污染**。作者将其归因于两个尺度的问题：补丁级结构错位（破坏全局一致性）与像素级保真度损失（阻碍细粒度几何恢复）；同时v-prediction在单次前向传播下在像素空间极不稳定。
- **整体含义**：本文提出Lapis，**首个基于线性注意力的像素空间生成框架**，在单次前向传播中实现一致、高保真的深度重建，同时保持O(N)计算复杂度，试图弥合生成式质量与判别式速度之间的鸿沟。

## 2. 方法论

### 2.1 核心思想
- 在像素空间直接进行**一步扩散**，以拼接的噪声深度图与条件图像为输入，直接预测干净深度图，无需VAE隐自编码器。
- 用线性注意力替换DiT中所有标准多头自注意力（MSA），将复杂度降至O(N)。
- 通过**由粗到细层级结构**（PCM + PRM）弥补线性化带来的表征保真度差距，并通过**直接x-prediction**抑制一步采样噪声。

### 2.2 关键技术细节

**（1）一步像素空间扩散**
- 遵循流匹配范式，线性调度：`x_t = (1-t)·x_0 + t·ε`，其中ε~N(0,1)，t~[τ,1]（τ≈0.05）。
- 模型直接预测：`x̂_0 = x_θ(x_t, t, c)`。
- 速度目标：`v_t = ε - x_0`，预测速度`v̂_t = (x_t - x̂_0)/t`。

**（2）训练损失**
- 速度损失：预测速度与真实速度的MSE。
- 多尺度梯度匹配损失：在x空间对多分辨率尺度S上的空间梯度进行L1匹配，增强边界锐度。
- 总损失：`L_total = L_velocity + λ_grad · L_grad`（λ_grad = 1.5）。

**（3）线性注意力公式**
- 用非负核函数φ(·)近似softmax相似度，利用矩阵乘法结合律，预先计算全局上下文项`Σφ(K_j)^T V_j ∈ R^{d×d}`和归一化因子，避免显式构建N×N注意力矩阵，复杂度从O(N²d)降至O(Nd²)。
- 核函数实现为`φ(x) = elu(x) + 1`。

**（4）Patch-level Consistency Module (PCM)**
- **全局关系一致性**：用冻结的DINOv2编码器提取语义描述子z，经门控机制精炼后与时间步嵌入融合，通过扩展的AdaLN-Zero机制调制线性注意力层和FFN层，将特征流锚定在一致的全局几何布局中。
- **局部空间连续性**：在FFN中引入残差3×3深度可分离卷积（DWC），构成ConvFFN，强制相邻token间的空间相关性，抑制网格伪影。

**（5）Pixel-level Refinement Module (PRM)**
- 通过长程跳跃连接重新整合像素级输入线索，恢复锐利几何边界。
- 输入y与可学习补丁位置编码拼接后经MLP得到PRM输入。
- 最终DiT块的token先reshape为空间网格，经MLP投影和PixelShuffle上采样至目标像素分辨率。
- PRM由M=3个Pixel Refiner块组成，每块使用AdaLN-Zero调制的ConvFFN解码像素级潜变量，最后用线性预测头输出高保真深度图。

**（6）深度归一化**
- 对原始深度取对数后按2/98百分位归一化至[-0.5, 0.5]，再重缩放至单位方差以保证训练稳定。

## 3. 实验设计

### 3.1 数据集与场景
- **训练数据**：约122K样本，来自5个合成数据集——Hypersim（53.8K）、TartanAir（28.2K）、VKITTI2（21.3K）、UrbanSyn（7.5K）、MatrixCity（11.6K），统一缩放至1024×768分辨率，简单拼接无加权采样。
- **零样本原生分辨率评估**：NYUv2（室内）、KITTI（室外）、ETH3D（多样）、ScanNet（室内）、DIODE（多样），共5个真实数据集。
- **1080P/1440P测试时分辨率缩放评估**：Middlebury（室内）、Booster（室内）、Cityscapes（室外）、DrivingStereo（室外）、ETH3D（多样），共5个高分辨率标注数据集。
- **边界锐度评估**：Hypersim（室内）、Sintel（多样）、Spring（室外），共3个高分辨率合成基准。

### 3.2 Benchmark与指标
- **精度指标**：AbsRel（绝对相对误差，↓）和δ1准确率（↑）。
- **边界锐度指标**：F1-score（↑），在480P/720P/1080P/1440P四种分辨率下评估。
- **运行时指标**：延迟（ms）、吞吐量（Hz）、峰值GPU内存（GB），覆盖480P/720P/1080P/1440P。

### 3.3 对比方法
- **判别式方法**：MiDaS、LeRes、Omnidata、DPT、HDN、Lotus-D、Depth Anything、Depth Anything V2、Depth Anything 3、MoGe、MoGe-2。
- **生成式方法**：GeoWizard、GenPercept、Diffusion-E2E-FT、Lotus-G、Marigold v1.0/v1.1、Lotus-2、Pixel-Perfect Depth。
- 共覆盖**12个benchmark**，涉及不同分辨率、不同场景类型。

## 4. 资源与算力

- **模型规模**：520M参数，保持DiT-Large配置的隐藏维度和块数，转为全线性化骨干。
- **GPU配置**：4块NVIDIA RTX Pro 6000 Blackwell GPU。
- **训练时长**：400K steps，每GPU batch size为8。
- **优化器**：AdamW，恒定学习率1×10⁻⁴，无权重衰减。
- **其他**：EMA衰减率0.9999（评估使用EMA权重）；训练和推理均使用bfloat16混合精度。
- **消融实验**：采用DiT-Base轻量配置，PRM简化为M=2块、D_pixel=16，以提升分析效率。
- **说明**：论文对算力信息描述较为完整，但未提及具体训练总时长（小时/天）。

## 5. 实验数量与充分性

### 实验组数概览
- **主实验1**（表1）：原生分辨率零样本评估，5个数据集 × 2个指标，对比约15种方法。
- **主实验2**（表2）：1080P/1440P分辨率缩放评估，5个数据集 × 2个分辨率 × 2个指标，对比6种方法。
- **主实验3**（表3）：边界锐度评估，3个数据集 × 4个分辨率 × F1-score，对比6种方法。
- **主实验4**（表4）：运行时分析，4个分辨率 × 3个指标，对比6种方法。
- **消融实验1**（表5）：组件消融（Full / w/o Global PCM / w/o Local PCM / w/o PRM），5个数据集 × 2个指标。
- **消融实验2**（图6）：预测目标（x-prediction vs v-prediction）× 采样步数（1/2/4/8）对比。
- **定性实验**（图4、图5）：架构组件消融可视化和多模型定性对比。

### 充分性与公平性评价
- **充分性**：实验覆盖多分辨率（480P–1440P）、多场景（室内/室外/多样）、多指标（精度/边界/效率），消融实验完整验证了每个组件的必要性，整体较为充分。
- **客观公平性**：作者对部分基线用Marigold评估协议重新评估（以*标记），并统一了评估指标和测试分辨率；对比方法涵盖了判别式和生成式两大阵营的代表性工作。
- **潜在偏差**：训练仅使用合成数据，测试涉及真实数据集，属于零样本评估，方法本身较为严格；但消融实验使用轻量配置，与完整模型性能存在差距，可能影响结论的直接迁移性。

## 6. 主要结论与发现

- **精度SOTA**：原生分辨率下，Lapis取得平均AbsRel 4.1%、δ1 98.2%，超越所有判别式和生成式基线（如Pixel-Perfect Depth的4.2%/98.0%、MoGe-2的4.8%/97.1%）。
- **高分辨率鲁棒性**：1080P下平均AbsRel 5.1，1440P下5.2，分别比最强竞争者相对提升约10%和19%。
- **边界锐度领先**：在所有测试分辨率下F1-score均优于所有基线，且随分辨率提升呈近单调改善。
- **效率显著提升**：相比之前SOTA生成模型，1080P延迟降低7.6×，1440P降低10.9×；吞吐量接近判别式模型（如1080P下8.4 Hz vs Depth Anything V2的12.4 Hz）。
- **一步x-prediction最优**：x-prediction与v-prediction均在一步采样时达到峰值，x-prediction在AbsRel和像素级连续性上略优，且与干净数据流形对齐更好。
- **组件必要性**：Global PCM对全局一致性至关重要（去除后AbsRel从4.8骤升至19.8）；Local PCM保证补丁间连续性；PRM对精度指标影响边际，但对恢复高频细节不可或缺。

## 7. 优点

- **架构创新性**：首次将线性注意力引入单目深度估计的像素空间扩散框架，实现O(N)复杂度的一步生成，兼具生成式质量与判别式速度。
- **问题诊断精准**：清晰识别线性化+一步采样带来的双重退化（补丁级结构错位、像素级细节丢失）及v-prediction的不稳定性，并针对性设计PCM、PRM和x-prediction。
- **方法设计优雅**：粗到细的双级精修（PCM负责全局/局部结构，PRM负责像素细节）分工明确；基于流形假设的x-prediction策略理论依据清晰。
- **实验全面**：覆盖12个benchmark、多分辨率、多场景，既有定量指标也有定性可视化，消融实验完整。
- **效率优势突出**：在高分辨率下相对生成式基线的延迟优势达7.6×–10.9×，同时内存占用远低于Lotus-2等重型生成模型。
- **代码开源**：提供了GitHub仓库链接，便于复现和后续研究。

## 8. 不足与局限

- **训练数据局限**：仅使用约122K合成数据训练，规模远小于Depth Anything系列（62.6M），可能限制零样本泛化上限；未使用真实数据，存在合成到真实的域差距风险。
- **任务范围限制

- **任务范围限制**：仅针对单目深度估计这一单一任务进行验证，未探索该线性注意力像素空间扩散框架在法线估计、光流、表面重建等其他密集预测任务上的可迁移性，方法的通用性边界尚未明确。
- **一步采样的多样性代价**：尽管一步x-prediction在精度上达到峰值，但扩散模型多步迭代所具备的生成多样性（对歧义区域的多模态建模）被完全放弃；论文未讨论在透明、反光、遮挡等固有歧义区域是否会出现过度平滑或模式坍塌。
- **合成到真实的域差距**：训练集全部为合成数据，虽以零样本方式在真实基准上验证，但缺少在真实数据上微调后的对比实验，无法判断性能上限是否受合成域偏置约束。
- **消融与完整模型不一致**：消融实验统一采用DiT-Base轻量配置（PRM简化为M=2、D_pixel=16），与完整520M模型的容量和感受野差异显著，组件贡献度的定量结论向完整模型迁移时需谨慎解读。
- **超参数敏感性未充分揭示**：调度下界τ、梯度匹配损失权重λ_grad、PRM块数M、像素潜变量维度D_pixel等关键超参数仅给出取值，缺少敏感性曲线或选取依据的消融，复现与调参成本较高。
- **失败案例与错误分析缺失**：论文以成功案例的定性对比为主，未系统呈现方法在极端场景（如纹理缺失、强反射、远距离薄结构）下的失败模式，方法边界刻画不够完整。
- **运行时对比的公平性细节**：延迟与吞吐量对比未完全说明各基线是否在同一硬件、同一精度（bfloat16/fp16）、同一批大小下测量，跨方法效率结论可能受实现差异影响。
- **长程依赖的实际收益未量化**：论文强调像素空间DiT保持长程一致性，但未通过专门实验（如超大分辨率或超长序列的注意力图可视化）直接验证线性注意力在深度估计中对长程几何一致性的具体贡献。

## 9. 总结性评价与启示

- **定位**：Lapis处于生成式深度估计与高效判别式方法之间的"第三条路径"——以像素空间扩散保留生成式保真度，以线性注意力和一步采样换取判别式级速度，是对"保真度-效率"权衡的一次系统性工程化解构。
- **方法论价值**：其核心贡献不在于单个模块，而在于**问题诊断驱动的协同设计**：先识别线性化+一步采样导致的两级退化（补丁级结构错位、像素级细节丢失），再以PCM（全局DINOv2语义锚定+局部卷积连续性）和PRM（像素级跳跃精修）分别对应，配合x-prediction稳定单步流形对齐，形成闭环的问题-方案映射，这种"诊断-对症"范式对其他高效生成模型设计具有借鉴意义。
- **对领域的启示**：
  - 线性注意力在密集预测任务中的可行性被首次在像素空间扩散框架下验证，为高分辨率生成式感知提供了O(N)复杂度的可行范式；
  - "一步生成 + 显式结构先验"可能是替代多步迭代采样的有效折中，尤其适用于对延迟敏感的下游应用；
  - 粗到细的层级精修（结构一致性 → 像素保真度）分工思路，可迁移至其他需要同时保证全局布局与局部细节的密集预测任务。
- **适用场景判断**：适合高分辨率、低延迟、单帧确定性输出的深度估计需求（如自动驾驶感知、AR/VR实时建图）；不适合需要多模态深度分布采样或对歧义区域进行不确定性建模的场景。
- **开放问题**：如何在保持一步效率的同时恢复生成多样性；如何将合成训练的泛化上限提升至Depth Anything级别的数据规模；线性注意力核函数的选择（ELU+1之外）是否对深度几何恢复有系统性影响——这些均值得后续工作深入。

（完）
