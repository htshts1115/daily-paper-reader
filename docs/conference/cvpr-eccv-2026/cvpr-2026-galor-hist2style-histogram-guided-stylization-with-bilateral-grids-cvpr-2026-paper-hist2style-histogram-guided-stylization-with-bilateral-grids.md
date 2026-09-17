---
title: "Hist2Style: Histogram-Guided Stylization with Bilateral Grids"
title_zh: Hist2Style：基于双边网格的直方图引导风格化
authors: "Galor, Dekel, Pikielny, Adam, Zhang, Zhoutong, Wang, Ke, Waller, Laura, Chen, Jiawen, Chugunov, Ilya"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Galor_Hist2Style_Histogram-Guided_Stylization_with_Bilateral_Grids_CVPR_2026_paper.pdf"
tags: ["query:cv-render"]
score: 6.0
evidence: 基于双边网格的快速边缘感知风格化，面向实时流程
tldr: 真实感风格迁移需在匹配颜色色调的同时保留内容细节，但大模型计算开销大且难控，不适合高分辨率实时流程。本文提出Hist2Style，基于双边网格将操作约束为局部仿射变换，实现快速边缘感知风格化，并将大模型蒸馏为轻量网络。实验表明其在高分辨率实时场景下保持视觉保真。该工作为高效的边缘感知图像滤波提供了思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 561, \"height\": 420}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 558, \"height\": 421}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 555, \"height\": 385}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 452, \"height\": 280}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 559, \"height\": 370}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 681, \"height\": 851}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 5, \"index\": 7, \"width\": 511, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 5, \"index\": 8, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 5, \"index\": 10, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 5, \"index\": 11, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 512, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 5, \"index\": 22, \"width\": 511, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 5, \"index\": 23, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 5, \"index\": 24, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 5, \"index\": 25, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 5, \"index\": 26, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 5, \"index\": 27, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 5, \"index\": 28, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 5, \"index\": 29, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 5, \"index\": 30, \"width\": 512, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 5, \"index\": 31, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 5, \"index\": 32, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 5, \"index\": 33, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 5, \"index\": 34, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 5, \"index\": 35, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 5, \"index\": 36, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 5, \"index\": 37, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 5, \"index\": 38, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 5, \"index\": 39, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 5, \"index\": 40, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 5, \"index\": 41, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 5, \"index\": 42, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 5, \"index\": 43, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 5, \"index\": 44, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 5, \"index\": 45, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 5, \"index\": 46, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 5, \"index\": 47, \"width\": 568, \"height\": 423}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 5, \"index\": 48, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 5, \"index\": 49, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 5, \"index\": 50, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 5, \"index\": 51, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 5, \"index\": 52, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 5, \"index\": 53, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 5, \"index\": 54, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 5, \"index\": 55, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-056.webp\", \"caption\": \"\", \"page\": 5, \"index\": 56, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-057.webp\", \"caption\": \"\", \"page\": 5, \"index\": 57, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-058.webp\", \"caption\": \"\", \"page\": 5, \"index\": 58, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-059.webp\", \"caption\": \"\", \"page\": 5, \"index\": 59, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-060.webp\", \"caption\": \"\", \"page\": 5, \"index\": 60, \"width\": 512, \"height\": 392}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-061.webp\", \"caption\": \"\", \"page\": 5, \"index\": 61, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-062.webp\", \"caption\": \"\", \"page\": 5, \"index\": 62, \"width\": 568, \"height\": 433}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-063.webp\", \"caption\": \"\", \"page\": 5, \"index\": 63, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-064.webp\", \"caption\": \"\", \"page\": 5, \"index\": 64, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-065.webp\", \"caption\": \"\", \"page\": 5, \"index\": 65, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-066.webp\", \"caption\": \"\", \"page\": 5, \"index\": 66, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-067.webp\", \"caption\": \"\", \"page\": 5, \"index\": 67, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-068.webp\", \"caption\": \"\", \"page\": 5, \"index\": 68, \"width\": 512, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-069.webp\", \"caption\": \"\", \"page\": 5, \"index\": 69, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-070.webp\", \"caption\": \"\", \"page\": 5, \"index\": 70, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-071.webp\", \"caption\": \"\", \"page\": 5, \"index\": 71, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-072.webp\", \"caption\": \"\", \"page\": 5, \"index\": 72, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-073.webp\", \"caption\": \"\", \"page\": 5, \"index\": 73, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-074.webp\", \"caption\": \"\", \"page\": 5, \"index\": 74, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-075.webp\", \"caption\": \"\", \"page\": 6, \"index\": 75, \"width\": 1991, \"height\": 552}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-076.webp\", \"caption\": \"\", \"page\": 8, \"index\": 76, \"width\": 470, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-077.webp\", \"caption\": \"\", \"page\": 8, \"index\": 77, \"width\": 470, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-078.webp\", \"caption\": \"\", \"page\": 8, \"index\": 78, \"width\": 470, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-079.webp\", \"caption\": \"\", \"page\": 8, \"index\": 79, \"width\": 393, \"height\": 452}]"
motivation: 现有大模型风格迁移计算开销大、可控性差，不适合高分辨率实时工作流。
method: 用双边网格将风格化约束为局部仿射变换，并把大模型蒸馏为轻量网络。
result: 在保持内容细节的同时实现了快速、边缘感知的高分辨率风格化。
conclusion: 双边网格为实时边缘感知图像处理提供了高效方案。
---

## Abstract
Photorealistic style transfer aims to match the color and tone of an input image to that of a style target while preserving the content and details of the original scene. Although existing large image models can facilitate these kinds of appearance edits, their high computational demands, potential for hallucinations, and limited user control make them unsuitable for high-resolution, real-time workflows. We introduce Hist2Style, a bilateral-grid formulation for fast, edge-aware stylization that preserves visual fidelity by constraining operations to locally affine transforms in bilateral space. Our model distills a large image editing model into a lightweight network by training on a large supervised corpus generated with language and vision-language models, targeting spatially varying color edits. The network conditions on a histogram-based embedding of the style target to provide an interpretable interface for adjusting the output style by modifying the target color distribution. Overall, Hist2Style maintains content structure by construction, avoids hallucinations, and supports real-time, high-resolution photorealistic stylization with interactive user-controllable color and tone adjustments. Our project page is available at \href https://dgalor.github.io/hist2style/ dgalor.github.io/hist2style/ .

---

## 论文详细总结（自动生成）

# Hist2Style 论文总结

## 1. 核心问题与整体含义

- **研究动机**：真实感风格迁移（photorealistic style transfer）的目标是将输入图像的颜色与色调匹配到风格参考图，同时保留原场景的内容与细节。
- **背景痛点**：
  - 经典颜色迁移方法（如 Reinhard、IDT）只做全局颜色统计对齐，缺乏空间/语义感知，易产生颗粒感等伪影。
  - 神经风格迁移（Gatys、WCT、PhotoWCT 等）虽表达力强，但多为艺术化、非真实感，或需要慢速逐图优化。
  - 大型图像编辑模型（Flux Kontext、Qwen Image Edit 等）虽灵活，但存在三大问题：**计算开销大**（高算力/显存/延迟）、**幻觉**（身份漂移、结构失真）、**可控性差**（难以用 prompt 精确表达细微色彩）。
- **整体含义**：本文提出 Hist2Style，通过“选择性蒸馏”把大型编辑模型的能力压缩为轻量、专用、可控的真实感风格化网络，使其适合高分辨率、实时、可交互的编辑工作流。

## 2. 方法论

### 2.1 核心思想
- **选择性蒸馏**：放弃生成能力，只保留“空间变化的颜色/色调编辑”这一子能力，从而兼顾表达力与真实感约束。
- **双边网格约束**：把编辑限制在双边空间中的局部仿射变换，从结构上保证内容与边缘不被破坏、避免幻觉。
- **直方图风格嵌入**：用风格图的边缘（per-channel）颜色直方图作为风格表示，天然可解释、可直接编辑。

### 2.2 关键技术与流程
- **数据合成**：用 LLM 生成多样化的真实感风格名称/描述（如 “Golden Hour”、“1950s Film Noir”），再用大型编辑模型对标准摄影数据集批量生成风格化版本，构成监督语料。
- **双边网格**：
  - 网格尺寸取 (8, 16, 16)，对应引导维、高、宽分辨率。
  - 每个网格单元预测一个仿射变换（3×4 = 12 个标量）+ 一个预乘的 α 不确定性值。
  - 引导维定义为 RGB 的**学习函数** g: R³ → R，相当于“亮度”维度，防止跨边缘平滑。
  - 通过三线性插值切片得到逐像素仿射变换，再作用于内容图，因此可扩展到任意分辨率。
- **损失函数**：
  - **空间损失**：输出与真值之间的 MSE（在 VGG 感知空间计算）。
  - **分布损失**：对每个通道排序像素后计算 1D Wasserstein-2 平方距离（即排序后 MSE，见论文 Algorithm 1），实现对边缘颜色分布的对齐。
- **模型架构（双分支）**：
  - 内容分支：ConvNeXt 风格块（7×7 深度卷积 + 倒瓶颈 + GELU + LayerNorm），下采样到 16×16。
  - 风格分支：把 1D 直方图当作序列，用 1D ConvNeXt 编码，得到全局风格 token。
  - 通过**交叉注意力**融合全局风格与局部内容特征，再由小卷积输出头预测仿射双边网格。
  - 应用仿射前后各加一个逐通道、单调平滑的非线性（LUT）。
- **交互式直方图操控**：在 Y'CbCr 空间提供曝光、对比度、U 偏移、V 偏移、平滑、强度等滑块，并支持直接拖拽直方图曲线；网络把全局意图转化为局部自适应编辑。

## 3. 实验设计

- **训练数据**：Unsplash Lite 数据集（25K 高质量图像），每张生成约 6–7 个合成风格变体，训练分辨率 256×256。
- **评测数据**：
  - 从 Unsplash 随机选 200 张未参与训练的内容图；
  - 人工筛选 136 张自然图像（剔除人工/编辑内容）；
  - 从 Unsplash 网站精选 19 张训练集外的风格图。
- **Benchmark 与对比方法**：SA-LUT、WCT2、Xia 等、IDT、D-LUT、PhotoWCT2、ReHistoGAN。
- **评估指标**：
  - **用户研究**：31 位摄影专家、3,000 次有效二选一试验。
  - **SQA**：本文新提出的基于 VLM 的风格化质量评估指标。
  - **循环一致性**（MSE）、**颜色匹配**（Wasserstein-2）、**FID**、**运行时间**、**内存**。
- **消融实验**：颜色空间损失（感知空间 vs. 原始颜色空间）、鲁棒训练（用同风格其他图直方图代替真值）。

## 4. 资源与算力

- 文中明确说明：**单张 A100 GPU** 上训练。
- 模型规模：**1.5M 参数**。
- 训练配置：**1127 个 epoch**，每个 epoch 含 **22.5K 图像**，batch size 为 **64**，训练分辨率 256×256。
- 优化器：Adam，学习率 3×10⁻⁴，β=(0.9, 0.99)，1 个 epoch 线性 warmup。
- 框架：PyTorch + PyTorch Lightning。

## 5. 实验数量与充分性

- **实验规模**：
  - 用户研究 3,000 次试验、31 位专家；SQA 评估 N=7000。
  - 运行时间对比覆盖 256² 到 4096² 共 5 档分辨率。
  - 定性对比两组数据集（用户研究集 + 独立非公开数据集）。
  - 消融实验至少 2 组（颜色空间损失、鲁棒训练），其余在补充材料。
- **充分性与公平性**：
  - 对比方法覆盖经典方法（IDT）、神经风格迁移（WCT2、PhotoWCT2）、双边网格方法（Xia 等）、LUT 方法（D-LUT、SA-LUT）、GAN 方法（ReHistoGAN），较全面。
  - 用户研究采用匿名、随机顺序、可标记平局，并使用模型默认输出以保证公平。
  - 论文指出 SA-LUT 因训练于 log 编码图像，在 RGB 上表现偏低，属于客观说明。
  - **局限**：消融数量偏少且核心消融放在补充材料；用户研究仅 31 人，样本规模有限。

## 6. 主要结论与发现

- **用户偏好**：Hist2Style 在所有对比中胜率均超过 61%，对 SA-LUT 胜率最高（82.57%），对 PhotoWCT2 为 61.62%。
- **效率**：512² 下仅需 0.003 s，16MP 下 0.1 s，是速度最快的方法之一；4MP 图像仅需 1 GB 显存，较 PhotoWCT2 有数量级提升。
- **SQA 指标**：与用户得分高度相关（相关系数 0.83），可作为可复现的自动评估替代。
- **循环一致性**：仅次于 IDT，表明局部仿射变换可被后续网格有效逆转，支持空间一致性主张。
- **颜色匹配**：介于 PhotoWCT2/WCT2（匹配最强）与真实感质量之间，形成良好折中。
- **消融发现**：感知空间损失优于原始颜色空间损失；用真值直方图训练比“鲁棒”训练颜色更丰富准确。

## 7. 优点

- **结构性保证真实感**：把变换限制在双边空间的局部仿射，从构造上避免结构扭曲与幻觉。
- **可解释、可交互**：以直方图作为风格表示，用户可直接编辑颜色分布，提供滑块与曲线拖拽两种直觉界面。
- **高效轻量**：1.5M 参数即可实现实时、高分辨率、低显存风格化。
- **蒸馏范式巧妙**：用 LLM + 大编辑模型自动生成大规模监督语料，规避人工标注成本。
- **提出 SQA 指标**：为高度主观的风格化任务提供与人类偏好高度相关的自动评估工具。
- **实验对比全面**：涵盖多类基线、多分辨率、用户研究与自动指标，结论相互印证。

## 8. 不足与局限

- **数据依赖与伪影风险**：训练依赖合成数据，其不完美（像素对齐误差）会传导至模型，论文亦将感知损失优势归因于此。
- **风格范围受限**：仅处理颜色/色调，无法加入胶片颗粒、散景、斑点等需要内容改动的效果。
- **高分辨率扩展性**：在超高分辨率下 Xia 等方法扩展更优（16MP 时 0.03 s vs. 0.1 s）；D-LUT 在风格已知时摊销后更快。
- **颜色匹配非最优**：PhotoWCT2、WCT2 的颜色分布匹配指标更优，本文为折中方案。
- **用户研究规模有限**：31 位专家、3,000 次试验，样本量和人群多样性有限，可能存在偏好偏差。
- **消融覆盖不足**：关键消融置于补充材料，主文消融组数偏少。
- **应用限制**：目前仅面向单图；多图层/对象级风格化、视频时序一致性、3D 辐射场集成均留作未来工作，尚待验证。

（完）
