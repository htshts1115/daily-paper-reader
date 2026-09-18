---
title: "Hist2Style: Histogram-Guided Stylization with Bilateral Grids"
title_zh: Hist2Style：基于双边网格的直方图引导风格化
authors: "Galor, Dekel, Pikielny, Adam, Zhang, Zhoutong, Wang, Ke, Waller, Laura, Chen, Jiawen, Chugunov, Ilya"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Galor_Hist2Style_Histogram-Guided_Stylization_with_Bilateral_Grids_CVPR_2026_paper.pdf"
tags: ["query:cv-render"]
score: 5.0
evidence: 双边网格边缘感知快速风格化
tldr: 高分辨率实时风格化面临大模型计算开销高、易产生幻觉且用户控制有限的问题。本文提出Hist2Style，基于双边网格将操作约束为双边空间中的局部仿射变换，实现快速且边缘感知的风格化，并通过蒸馏大图像编辑模型得到轻量网络。实验显示该方法在保持视觉保真度的同时支持实时工作流，为高效图像滤波与移动端渲染管线提供了可复用思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 561, \"height\": 420}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 558, \"height\": 421}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 555, \"height\": 385}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 452, \"height\": 280}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 559, \"height\": 370}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 681, \"height\": 851}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 5, \"index\": 7, \"width\": 511, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 5, \"index\": 8, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 5, \"index\": 10, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 5, \"index\": 11, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 512, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 5, \"index\": 22, \"width\": 511, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 5, \"index\": 23, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 5, \"index\": 24, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 5, \"index\": 25, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 5, \"index\": 26, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 5, \"index\": 27, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 5, \"index\": 28, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 5, \"index\": 29, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 5, \"index\": 30, \"width\": 512, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 5, \"index\": 31, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 5, \"index\": 32, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 5, \"index\": 33, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 5, \"index\": 34, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 5, \"index\": 35, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 5, \"index\": 36, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 5, \"index\": 37, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 5, \"index\": 38, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 5, \"index\": 39, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 5, \"index\": 40, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 5, \"index\": 41, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 5, \"index\": 42, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 5, \"index\": 43, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 5, \"index\": 44, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 5, \"index\": 45, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 5, \"index\": 46, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 5, \"index\": 47, \"width\": 568, \"height\": 423}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 5, \"index\": 48, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 5, \"index\": 49, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 5, \"index\": 50, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 5, \"index\": 51, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 5, \"index\": 52, \"width\": 512, \"height\": 384}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 5, \"index\": 53, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 5, \"index\": 54, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 5, \"index\": 55, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-056.webp\", \"caption\": \"\", \"page\": 5, \"index\": 56, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-057.webp\", \"caption\": \"\", \"page\": 5, \"index\": 57, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-058.webp\", \"caption\": \"\", \"page\": 5, \"index\": 58, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-059.webp\", \"caption\": \"\", \"page\": 5, \"index\": 59, \"width\": 568, \"height\": 426}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-060.webp\", \"caption\": \"\", \"page\": 5, \"index\": 60, \"width\": 512, \"height\": 392}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-061.webp\", \"caption\": \"\", \"page\": 5, \"index\": 61, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-062.webp\", \"caption\": \"\", \"page\": 5, \"index\": 62, \"width\": 568, \"height\": 433}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-063.webp\", \"caption\": \"\", \"page\": 5, \"index\": 63, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-064.webp\", \"caption\": \"\", \"page\": 5, \"index\": 64, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-065.webp\", \"caption\": \"\", \"page\": 5, \"index\": 65, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-066.webp\", \"caption\": \"\", \"page\": 5, \"index\": 66, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-067.webp\", \"caption\": \"\", \"page\": 5, \"index\": 67, \"width\": 568, \"height\": 436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-068.webp\", \"caption\": \"\", \"page\": 5, \"index\": 68, \"width\": 512, \"height\": 341}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-069.webp\", \"caption\": \"\", \"page\": 5, \"index\": 69, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-070.webp\", \"caption\": \"\", \"page\": 5, \"index\": 70, \"width\": 568, \"height\": 378}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-071.webp\", \"caption\": \"\", \"page\": 5, \"index\": 71, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-072.webp\", \"caption\": \"\", \"page\": 5, \"index\": 72, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-073.webp\", \"caption\": \"\", \"page\": 5, \"index\": 73, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-074.webp\", \"caption\": \"\", \"page\": 5, \"index\": 74, \"width\": 568, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-075.webp\", \"caption\": \"\", \"page\": 6, \"index\": 75, \"width\": 1991, \"height\": 552}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-076.webp\", \"caption\": \"\", \"page\": 8, \"index\": 76, \"width\": 470, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-077.webp\", \"caption\": \"\", \"page\": 8, \"index\": 77, \"width\": 470, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-078.webp\", \"caption\": \"\", \"page\": 8, \"index\": 78, \"width\": 470, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-galor-hist2style-histogram-guided-stylization-with-bilateral-grids-cvpr-2026-paper/fig-079.webp\", \"caption\": \"\", \"page\": 8, \"index\": 79, \"width\": 393, \"height\": 452}]"
motivation: 大图像模型计算开销高、易产生幻觉且控制有限，不适合高分辨率实时风格化工作流。
method: 提出基于双边网格的公式，将操作约束为双边空间局部仿射变换，并蒸馏大编辑模型为轻量网络。
result: 实现快速边缘感知的风格化，在保持视觉保真度的同时支持高分辨率实时处理。
conclusion: 为高效、可控的实时图像风格化与边缘感知滤波提供了轻量化方案。
---

## Abstract
Photorealistic style transfer aims to match the color and tone of an input image to that of a style target while preserving the content and details of the original scene. Although existing large image models can facilitate these kinds of appearance edits, their high computational demands, potential for hallucinations, and limited user control make them unsuitable for high-resolution, real-time workflows. We introduce Hist2Style, a bilateral-grid formulation for fast, edge-aware stylization that preserves visual fidelity by constraining operations to locally affine transforms in bilateral space. Our model distills a large image editing model into a lightweight network by training on a large supervised corpus generated with language and vision-language models, targeting spatially varying color edits. The network conditions on a histogram-based embedding of the style target to provide an interpretable interface for adjusting the output style by modifying the target color distribution. Overall, Hist2Style maintains content structure by construction, avoids hallucinations, and supports real-time, high-resolution photorealistic stylization with interactive user-controllable color and tone adjustments. Our project page is available at \href https://dgalor.github.io/hist2style/ dgalor.github.io/hist2style/ .

---

## 论文详细总结（自动生成）

# Hist2Style：基于双边网格的直方图引导风格化 —— 论文深度总结

## 1. 核心问题与研究背景

- **任务定位**：照片级真实（photorealistic）风格迁移，即在**不改变内容结构**的前提下，把输入图像的颜色与影调匹配到风格参考图。论文明确采用"风格 = 颜色与影调，内容 = 结构与边缘"的约定。
- **现有痛点（三类）**：
  - **大图像编辑模型（如 Flux Kontext、Qwen Image Edit）**：表达力强但计算/显存开销大、推理慢，不适合高分辨率实时流程；
  - **幻觉（hallucination）**：易引入身份漂移、结构扭曲等破坏真实感的伪影；
  - **可控性差**：文本/图像提示难以精确表达细微的颜色与影调意图，用户对输出缺乏可解释的控制手段。
- **本文主张**：牺牲通用性、换回照片级约束与效率——**选择性蒸馏**一个大编辑模型到轻量专用网络，并用**直方图嵌入**作为可解释、可交互的风格接口。
- **整体含义**：为高分辨率、实时、可控的调色/风格化提供一条"经典颜色迁移 + 现代语义先验"的融合路线，对移动端与边缘设备的渲染管线有直接参考价值。

## 2. 方法论

### 2.1 核心思想
- 将风格化建模为**双边空间中的局部仿射变换**（双边网格），从构造上保证边缘感知与内容保真；风格由**风格图的逐通道边缘直方图**编码，因而可被人为直接编辑。

### 2.2 选择性蒸馏流程
- 用大语言模型（Gemini）自动生成多样化的照片级风格描述（如 "Golden Hour"、"1950s Film Noir"、"Dark Stormy Night"）。
- 以标准摄影数据集（Unsplash Lite，25K 图）为内容，用大图像编辑模型（Flux Kontext）按提示生成风格化版本作为**合成监督真值**，风格在跨内容上保持一致。
- 学生网络回归教师的风格化结果，从而只继承"空间变化的颜色编辑"这一子能力（不含内容生成）。
- 为压制教师带来的幻觉，除自动数据过滤外，进一步把照片级约束**内建进模型结构**（双边网格）。

### 2.3 双边网格表示
- 引导维度取为 RGB 的**可学习函数** g: R³→R（近似亮度维度），防止跨边缘平滑。
- 网格尺寸 (G_g, G_h, G_w) = (8, 16, 16)；每个网格单元预测 **3×4 = 12 个仿射参数**，另预测一个**预乘不确定性通道 α**（softplus 保证稳定）。
- 推理时用内容图对网格做**三线性插值切片**，得到逐像素仿射变换（系数除以切片后的 α 再应用）；网格分辨率与图像分辨率解耦，因此可扩展到任意高分辨率。
- 仿射变换前后各施加一个**逐通道可学习单调非线性（LUT）**，类似色调曲线。

### 2.4 风格条件与损失
- 风格嵌入 = 风格图的**边缘（逐通道）直方图**；1D 直方图按"每通道一条序列"送入 1D ConvNeXt 得到全局风格 token。
- **空间损失**：输出与真值的 MSE。
- **分布损失**：对每个通道在空间上排序后计算 MSE，等价于**一维 Wasserstein-2 距离的平方**（算法 1：排序→逐通道平方距离→求均值）。
- 两项损失均施加在 **VGG 感知空间**而非原始颜色空间，作者归因于合成数据存在像素级不对齐。

### 2.5 网络结构
- **双分支设计**：内容分支为 ConvNeXt 风格卷积编码器（7×7 深度可分离大核 + 倒残差 + GELU + LayerNorm），下采样到 16×16 以匹配网格尺寸；风格分支为 1D ConvNeXt。
- 二者通过**交叉注意力**融合，拼接后由小型卷积输出头预测仿射双边网格。

### 2.6 交互式直方图操控
- 在 **Y'CbCr** 空间提供滑杆：曝光 E、对比度 C（在亮度峰值 delta 与原始直方图间插值）、Cb 位移 U、Cr 位移 V、平滑 S，以及作用于输出变换的强度 A（恒等↔预测变换插值）。
- 另支持**直接拖拽直方图**增删某亮度/色度 bin 的质量，由模型保证变换仍符合照片统计规律——把"全局意图"翻译为"局部自适应编辑"。

## 3. 实验设计

- **数据**：
  - 训练：Unsplash Lite（25K 高清图），每图平均生成 **6–7 个合成风格变体**，训练分辨率 256×256。
  - 评估：从 Unsplash 中抽取 **200 张未参与训练的内容图**，人工筛选出 **136 张自然图像**（剔除人工/编辑内容），并另选 **19 张风格图**。
  - 另有一个独立收集的**非公开数据集**用于定性比较（覆盖白天、夜晚、鲜艳、单色等场景）。
- **Benchmark / 对比方法**：SA-LUT、WCT²、Xia et al.、IDT、D-LUT、PhotoWCT²、ReHistoGAN（含 ReHistoGAN 部分指标）。
- **用户研究**：二选一匿名偏好测试，**31 位摄影专家、3000 次有效试验**，指示语要求"在保持内容结构与细节的同时匹配风格调色板/影调/整体美学且不引入伪影"，允许判平局。所有对比均使用 Hist2Style 默认输出（不启用用户控制）。
- **量化指标**：用户得分（对 H2S 的胜率 + ½ 平局率）、新提出的 **SQA（VLM 风格化质量评估）**、循环一致性（A→B→A 的 MSE）、颜色匹配（算法 1 的分布距离，Y'/Cb/Cr）、FID，以及跨分辨率的**运行时间与显存**。
- **消融**：① "Color Space Loss"（损失施加于原始颜色空间而非感知空间）；② "Robust" 训练（不使用目标图真直方图，而用同风格另一张图的直方图）。

## 4. 资源与算力

- 论文明确给出：**单张 A100 GPU**；模型规模 **1.5M 参数**；Adam 优化器，学习率 3×10⁻⁴，(β₁, β₂) = (0.9, 0.99)，1 个 epoch 线性 warm-up；训练 **1127 个 epoch**，每 epoch 22.5K 图像，batch size 64。
- **未明确说明**：总训练时长（小时/天）、GPU 显存占用、合成数据生成（教师模型推理）所消耗的算力与时间成本。
- 推理侧给出较完整数据：256²/512²/1024²/2048²/4096² 分辨率下分别为 0.001 / 0.003 / 0.009 / 0.04 / 0.1 秒；处理 4MP 图像仅需约 **1 GB 显存**。

## 5. 实验数量与充分性

- **规模概览**：
  - 1 组大规模用户研究（3000 trials，31 位专家）；
  - SQA 评估 N=7000；
  - 运行时间覆盖 5 个分辨率档、8 种方法；
  - 循环一致性、颜色匹配（3 通道）、FID 等多项量化对比；
  - 2 组主要消融 + 补充材料中的额外消融；
  - 两个数据集上的定性对比（公开评估集 + 独立非公开集）。
- **充分性评价**：
  - **优点**：用户研究规模与专家背景较扎实；同时报告感知质量、分布匹配、循环一致性、效率与显存，维度较全面；提出 SQA 以缓解主观评估难复现的问题。
  - **可质疑之处**：
    - 消融数量偏少（正文仅两项），架构组件（交叉注意力、α 通道、LUT 非线性、网格尺寸等）的贡献拆解被推到补充材料；
    - 评估数据来自 Unsplash 且含人工筛选，存在**选择偏差**风险，作者也承认训练数据"合成且存在像素不对齐"；
    - 用户研究仅 31 人，且未报告置信区间或显著性检验；
    - 部分基线（如 SA-LUT）作者指出其训练于 log 编码图像，可能未在其最优设定下比较，公平性存在一定瑕疵。

## 6. 主要结论与发现

- Hist2Style 在用户研究中取得**最高总体偏好**，对任一单一基线**胜率均超过 61%**（对 SA-LUT 82.57%、WCT² 72.58%、Xia et al. 73.24%、IDT 73.75%、D-LUT 70.59%、PhotoWCT² 61.62%）。
- **速度与资源**：与 Xia et al. 同为最快方法，512² 下均为 0.003 s；低分辨率下 Hist2Style 更快，高分辨率（16MP）下 Xia et al. 更优（0.03 s vs 0.1 s）；相对 PhotoWCT² 有数量级的运行时与峰值显存改善。
- **权衡关系**：Hist2Style 在颜色分布匹配上不及 PhotoWCT²/WCT²（后者风格化更强但感知质量与用户得分更低），但在"全局颜色统计匹配"与"感知质量"之间取得了更好的折中；循环一致性仅次于 IDT，支持其空间一致性的主张。
- **SQA 有效性**：VLM 驱动的 SQA 与用户得分高度相关（约 0.83），明显优于运行时间、循环一致性、FID 等指标与人类偏好的相关性。
- **消融结论**：感知空间损失优于颜色空间损失（归因于合成数据的像素不对齐）；"Robust" 训练会损害颜色匹配精度。

## 7. 优点

- **结构性保证**：把照片级约束写进表示本身（双边网格上的局部仿射变换），从构造上避免内容形变与幻觉，而非依赖后处理或正则项。
- **分辨率解耦**：变换在低分辨率网格上计算、逐像素切片应用，天然支持任意高分辨率，效率高、显存低。
- **可解释且可交互的风格接口**：用边缘直方图代替深度特征或语言嵌入，既可直接编辑（滑杆 + 直接拖拽），也贴合传统调色/色调曲线工作流。
- **务实的蒸馏范式**：用 LLM 生成风格提示、用大编辑模型生成监督数据，将"通用生成能力"裁剪为"专用编辑能力"，兼顾语义先验与效率。
- **评估贡献**：提出与人类偏好高度一致的 SQA 指标，并给出可直接复用的分布匹配损失（排序后 MSE ≈ 1D Wasserstein-2），可迁移至其他颜色迁移任务。
- **交互与自动化的统一**：同一模型既支持全自动风格化，也支持用户实时调参，且不牺牲实时性。

## 8. 不足与局限

- **风格表达受限**：仅建模颜色与影调，无法加入胶片颗粒、散斑、景深/散景等效果；对"非颜色类风格"无能为力。
- **空间控制缺失**：风格条件为全局边缘直方图，无法对不同物体施加不同风格（作者将其列为未来工作，需联合分割掩码）。
- **数据依赖与偏差**：完全依赖合成监督，教师模型的偏差与幻觉可能被部分继承；训练分辨率仅 256²，高分辨率下的行为主要依赖网格解耦而非直接监督；评估集来自单一图库并经过人工筛选。
- **对比公平性**：SA-LUT 等基线可能未在最优配置下评测；部分指标（如 ReHistoGAN）在表中数值异常，说明指标口径或方法适配存在不确定性。
- **效率非全面领先**：高分辨率下推理速度不及 Xia et al.（0.1 s vs 0.03 s @16MP），D-LUT 在风格已知时摊销后更快（0.001 s）。
- **评估严谨性**：用户研究样本（31 人）与统计显著性报告有限；正文消融较少，关键设计选择的独立贡献需依赖补充材料。
- **应用边界**：视频与 3D/辐射场场景尚未验证，长视频的时序一致性未处理。

（完）
