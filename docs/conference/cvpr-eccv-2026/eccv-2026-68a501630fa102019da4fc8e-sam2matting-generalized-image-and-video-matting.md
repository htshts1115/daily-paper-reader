---
title: "SAM2Matting: Generalized Image and Video Matting"
title_zh: SAM2Matting：通用图像与视频抠图
authors: "Ruiqi Shen, Guangquan Jie, Chang Liu, Henghui Ding"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/8235.pdf"
tags: ["query:matting"]
score: 9.0
evidence: 通用图像与视频抠图，解耦跟踪与抠图
tldr: 视频抠图因高层跟踪需逐帧理解、低层抠图关注极细粒度细节而存在鸿沟，现有方法依赖昂贵领域数据，泛化受限。本文提出SAM2Matting，通过区域提议桥和专用抠图头增强SAM2跟踪器，将跟踪与抠图解耦。该方法在图像与视频抠图任务上实现了良好的泛化性能。该工作为无需trimap的通用抠图提供了新范式。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 1823, \"height\": 2384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1824, \"height\": 2384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 670, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 672, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 670, \"height\": 1102}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 672, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1247, \"height\": 1451}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 1246, \"height\": 1451}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 672, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-013.webp\", \"caption\": \"\", \"page\": 2, \"index\": 13, \"width\": 1246, \"height\": 1450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-014.webp\", \"caption\": \"\", \"page\": 2, \"index\": 14, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-015.webp\", \"caption\": \"\", \"page\": 2, \"index\": 15, \"width\": 2109, \"height\": 2693}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-016.webp\", \"caption\": \"\", \"page\": 2, \"index\": 16, \"width\": 1819, \"height\": 2397}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-017.webp\", \"caption\": \"\", \"page\": 2, \"index\": 17, \"width\": 2887, \"height\": 2697}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-018.webp\", \"caption\": \"\", \"page\": 2, \"index\": 18, \"width\": 2589, \"height\": 2401}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-019.webp\", \"caption\": \"\", \"page\": 2, \"index\": 19, \"width\": 1929, \"height\": 2688}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-020.webp\", \"caption\": \"\", \"page\": 2, \"index\": 20, \"width\": 1640, \"height\": 2392}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-021.webp\", \"caption\": \"\", \"page\": 2, \"index\": 21, \"width\": 2346, \"height\": 2780}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-022.webp\", \"caption\": \"\", \"page\": 2, \"index\": 22, \"width\": 2053, \"height\": 2484}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-023.webp\", \"caption\": \"\", \"page\": 2, \"index\": 23, \"width\": 2345, \"height\": 2780}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-024.webp\", \"caption\": \"\", \"page\": 2, \"index\": 24, \"width\": 2053, \"height\": 2484}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-025.webp\", \"caption\": \"\", \"page\": 2, \"index\": 25, \"width\": 670, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-026.webp\", \"caption\": \"\", \"page\": 2, \"index\": 26, \"width\": 670, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-027.webp\", \"caption\": \"\", \"page\": 2, \"index\": 27, \"width\": 670, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-028.webp\", \"caption\": \"\", \"page\": 2, \"index\": 28, \"width\": 670, \"height\": 1100}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-029.webp\", \"caption\": \"\", \"page\": 4, \"index\": 29, \"width\": 300, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-030.webp\", \"caption\": \"\", \"page\": 4, \"index\": 30, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-031.webp\", \"caption\": \"\", \"page\": 4, \"index\": 31, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-032.webp\", \"caption\": \"\", \"page\": 4, \"index\": 32, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-033.webp\", \"caption\": \"\", \"page\": 4, \"index\": 33, \"width\": 1024, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-034.webp\", \"caption\": \"\", \"page\": 4, \"index\": 34, \"width\": 720, \"height\": 1280}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-035.webp\", \"caption\": \"\", \"page\": 4, \"index\": 35, \"width\": 834, \"height\": 592}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-036.webp\", \"caption\": \"\", \"page\": 9, \"index\": 36, \"width\": 1080, \"height\": 1618}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-037.webp\", \"caption\": \"\", \"page\": 9, \"index\": 37, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-038.webp\", \"caption\": \"\", \"page\": 9, \"index\": 38, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-039.webp\", \"caption\": \"\", \"page\": 9, \"index\": 39, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-040.webp\", \"caption\": \"\", \"page\": 9, \"index\": 40, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-041.webp\", \"caption\": \"\", \"page\": 9, \"index\": 41, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-042.webp\", \"caption\": \"\", \"page\": 9, \"index\": 42, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-043.webp\", \"caption\": \"\", \"page\": 9, \"index\": 43, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-044.webp\", \"caption\": \"\", \"page\": 9, \"index\": 44, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-045.webp\", \"caption\": \"\", \"page\": 9, \"index\": 45, \"width\": 722, \"height\": 962}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-046.webp\", \"caption\": \"\", \"page\": 9, \"index\": 46, \"width\": 1080, \"height\": 1618}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-047.webp\", \"caption\": \"\", \"page\": 9, \"index\": 47, \"width\": 976, \"height\": 1300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-048.webp\", \"caption\": \"\", \"page\": 9, \"index\": 48, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-049.webp\", \"caption\": \"\", \"page\": 9, \"index\": 49, \"width\": 976, \"height\": 1300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-050.webp\", \"caption\": \"\", \"page\": 9, \"index\": 50, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-051.webp\", \"caption\": \"\", \"page\": 9, \"index\": 51, \"width\": 720, \"height\": 960}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-052.webp\", \"caption\": \"\", \"page\": 9, \"index\": 52, \"width\": 1080, \"height\": 1618}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-053.webp\", \"caption\": \"\", \"page\": 9, \"index\": 53, \"width\": 1080, \"height\": 1618}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-054.webp\", \"caption\": \"\", \"page\": 9, \"index\": 54, \"width\": 1080, \"height\": 1618}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-055.webp\", \"caption\": \"\", \"page\": 9, \"index\": 55, \"width\": 1080, \"height\": 1440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-056.webp\", \"caption\": \"\", \"page\": 9, \"index\": 56, \"width\": 1080, \"height\": 1440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-057.webp\", \"caption\": \"\", \"page\": 9, \"index\": 57, \"width\": 1080, \"height\": 1440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-058.webp\", \"caption\": \"\", \"page\": 9, \"index\": 58, \"width\": 1080, \"height\": 1440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-059.webp\", \"caption\": \"\", \"page\": 9, \"index\": 59, \"width\": 1080, \"height\": 1440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-060.webp\", \"caption\": \"\", \"page\": 10, \"index\": 60, \"width\": 649, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-061.webp\", \"caption\": \"\", \"page\": 10, \"index\": 61, \"width\": 647, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-062.webp\", \"caption\": \"\", \"page\": 10, \"index\": 62, \"width\": 649, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-063.webp\", \"caption\": \"\", \"page\": 10, \"index\": 63, \"width\": 648, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-064.webp\", \"caption\": \"\", \"page\": 10, \"index\": 64, \"width\": 647, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-065.webp\", \"caption\": \"\", \"page\": 10, \"index\": 65, \"width\": 651, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-066.webp\", \"caption\": \"\", \"page\": 10, \"index\": 66, \"width\": 652, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-067.webp\", \"caption\": \"\", \"page\": 10, \"index\": 67, \"width\": 647, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-068.webp\", \"caption\": \"\", \"page\": 10, \"index\": 68, \"width\": 651, \"height\": 849}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-069.webp\", \"caption\": \"\", \"page\": 10, \"index\": 69, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-070.webp\", \"caption\": \"\", \"page\": 10, \"index\": 70, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-071.webp\", \"caption\": \"\", \"page\": 10, \"index\": 71, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-072.webp\", \"caption\": \"\", \"page\": 10, \"index\": 72, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-073.webp\", \"caption\": \"\", \"page\": 10, \"index\": 73, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-074.webp\", \"caption\": \"\", \"page\": 10, \"index\": 74, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-075.webp\", \"caption\": \"\", \"page\": 10, \"index\": 75, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-076.webp\", \"caption\": \"\", \"page\": 10, \"index\": 76, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-077.webp\", \"caption\": \"\", \"page\": 10, \"index\": 77, \"width\": 360, \"height\": 577}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-078.webp\", \"caption\": \"\", \"page\": 10, \"index\": 78, \"width\": 432, \"height\": 613}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-079.webp\", \"caption\": \"\", \"page\": 10, \"index\": 79, \"width\": 432, \"height\": 613}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-080.webp\", \"caption\": \"\", \"page\": 10, \"index\": 80, \"width\": 432, \"height\": 613}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-081.webp\", \"caption\": \"\", \"page\": 10, \"index\": 81, \"width\": 434, \"height\": 614}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-082.webp\", \"caption\": \"\", \"page\": 10, \"index\": 82, \"width\": 433, \"height\": 618}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-083.webp\", \"caption\": \"\", \"page\": 10, \"index\": 83, \"width\": 432, \"height\": 613}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-084.webp\", \"caption\": \"\", \"page\": 10, \"index\": 84, \"width\": 521, \"height\": 689}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-085.webp\", \"caption\": \"\", \"page\": 10, \"index\": 85, \"width\": 521, \"height\": 689}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-086.webp\", \"caption\": \"\", \"page\": 10, \"index\": 86, \"width\": 521, \"height\": 689}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-087.webp\", \"caption\": \"\", \"page\": 10, \"index\": 87, \"width\": 521, \"height\": 667}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-088.webp\", \"caption\": \"\", \"page\": 10, \"index\": 88, \"width\": 518, \"height\": 664}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-089.webp\", \"caption\": \"\", \"page\": 10, \"index\": 89, \"width\": 518, \"height\": 662}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-090.webp\", \"caption\": \"\", \"page\": 10, \"index\": 90, \"width\": 493, \"height\": 699}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-091.webp\", \"caption\": \"\", \"page\": 10, \"index\": 91, \"width\": 493, \"height\": 699}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-092.webp\", \"caption\": \"\", \"page\": 10, \"index\": 92, \"width\": 493, \"height\": 699}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-093.webp\", \"caption\": \"\", \"page\": 10, \"index\": 93, \"width\": 493, \"height\": 699}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-094.webp\", \"caption\": \"\", \"page\": 10, \"index\": 94, \"width\": 493, \"height\": 699}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-095.webp\", \"caption\": \"\", \"page\": 10, \"index\": 95, \"width\": 493, \"height\": 699}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-096.webp\", \"caption\": \"\", \"page\": 10, \"index\": 96, \"width\": 670, \"height\": 510}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-097.webp\", \"caption\": \"\", \"page\": 10, \"index\": 97, \"width\": 670, \"height\": 510}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-098.webp\", \"caption\": \"\", \"page\": 10, \"index\": 98, \"width\": 670, \"height\": 510}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-099.webp\", \"caption\": \"\", \"page\": 10, \"index\": 99, \"width\": 360, \"height\": 595}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-100.webp\", \"caption\": \"\", \"page\": 10, \"index\": 100, \"width\": 360, \"height\": 587}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-101.webp\", \"caption\": \"\", \"page\": 10, \"index\": 101, \"width\": 360, \"height\": 587}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-102.webp\", \"caption\": \"\", \"page\": 10, \"index\": 102, \"width\": 358, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-103.webp\", \"caption\": \"\", \"page\": 10, \"index\": 103, \"width\": 358, \"height\": 460}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-104.webp\", \"caption\": \"\", \"page\": 10, \"index\": 104, \"width\": 358, \"height\": 477}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-105.webp\", \"caption\": \"\", \"page\": 10, \"index\": 105, \"width\": 358, \"height\": 469}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-106.webp\", \"caption\": \"\", \"page\": 10, \"index\": 106, \"width\": 358, \"height\": 474}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-107.webp\", \"caption\": \"\", \"page\": 10, \"index\": 107, \"width\": 358, \"height\": 473}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-108.webp\", \"caption\": \"\", \"page\": 10, \"index\": 108, \"width\": 358, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-109.webp\", \"caption\": \"\", \"page\": 10, \"index\": 109, \"width\": 358, \"height\": 447}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-110.webp\", \"caption\": \"\", \"page\": 10, \"index\": 110, \"width\": 358, \"height\": 468}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-111.webp\", \"caption\": \"\", \"page\": 10, \"index\": 111, \"width\": 358, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-112.webp\", \"caption\": \"\", \"page\": 10, \"index\": 112, \"width\": 358, \"height\": 452}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-113.webp\", \"caption\": \"\", \"page\": 11, \"index\": 113, \"width\": 297, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-114.webp\", \"caption\": \"\", \"page\": 11, \"index\": 114, \"width\": 297, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-115.webp\", \"caption\": \"\", \"page\": 11, \"index\": 115, \"width\": 298, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-116.webp\", \"caption\": \"\", \"page\": 11, \"index\": 116, \"width\": 297, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-117.webp\", \"caption\": \"\", \"page\": 11, \"index\": 117, \"width\": 314, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-118.webp\", \"caption\": \"\", \"page\": 11, \"index\": 118, \"width\": 313, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-119.webp\", \"caption\": \"\", \"page\": 11, \"index\": 119, \"width\": 314, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-120.webp\", \"caption\": \"\", \"page\": 11, \"index\": 120, \"width\": 314, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-121.webp\", \"caption\": \"\", \"page\": 12, \"index\": 121, \"width\": 422, \"height\": 757}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-122.webp\", \"caption\": \"\", \"page\": 12, \"index\": 122, \"width\": 422, \"height\": 757}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-123.webp\", \"caption\": \"\", \"page\": 12, \"index\": 123, \"width\": 422, \"height\": 757}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-124.webp\", \"caption\": \"\", \"page\": 12, \"index\": 124, \"width\": 720, \"height\": 1063}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-125.webp\", \"caption\": \"\", \"page\": 12, \"index\": 125, \"width\": 720, \"height\": 1063}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-126.webp\", \"caption\": \"\", \"page\": 12, \"index\": 126, \"width\": 720, \"height\": 1063}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-127.webp\", \"caption\": \"\", \"page\": 12, \"index\": 127, \"width\": 526, \"height\": 807}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-128.webp\", \"caption\": \"\", \"page\": 12, \"index\": 128, \"width\": 526, \"height\": 807}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-129.webp\", \"caption\": \"\", \"page\": 12, \"index\": 129, \"width\": 526, \"height\": 806}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-130.webp\", \"caption\": \"\", \"page\": 12, \"index\": 130, \"width\": 720, \"height\": 1112}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-131.webp\", \"caption\": \"\", \"page\": 12, \"index\": 131, \"width\": 720, \"height\": 1138}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-132.webp\", \"caption\": \"\", \"page\": 12, \"index\": 132, \"width\": 720, \"height\": 1112}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-133.webp\", \"caption\": \"\", \"page\": 12, \"index\": 133, \"width\": 411, \"height\": 743}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-134.webp\", \"caption\": \"\", \"page\": 12, \"index\": 134, \"width\": 720, \"height\": 1063}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-135.webp\", \"caption\": \"\", \"page\": 12, \"index\": 135, \"width\": 657, \"height\": 1039}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-136.webp\", \"caption\": \"\", \"page\": 12, \"index\": 136, \"width\": 493, \"height\": 778}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-137.webp\", \"caption\": \"\", \"page\": 14, \"index\": 137, \"width\": 513, \"height\": 288}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-138.webp\", \"caption\": \"\", \"page\": 14, \"index\": 138, \"width\": 514, \"height\": 288}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-68a501630fa102019da4fc8e/fig-139.webp\", \"caption\": \"\", \"page\": 14, \"index\": 139, \"width\": 513, \"height\": 288}]"
motivation: 视频抠图中高层跟踪与低层细节抠图存在鸿沟，且依赖领域数据导致泛化不足。
method: 用区域提议桥和专用抠图头增强SAM2跟踪器，将跟踪与细粒度抠图解耦。
result: 在图像与视频抠图上实现了较强的泛化能力和稳定的跟踪鲁棒性。
conclusion: 解耦跟踪与抠图可获得通用的高质量抠图框架。
---

## Abstract
Despite impressive advances in image matting, video mattingremains challenging due to the inherent gap between high-level tracking,which requires frame-wise understanding, and low-level matting, whichfocuses on extremely fine-grained details. Existing methods attempt thisusing costly domain-specific video matting datasets, which may limittheir out-of-domain generalization and leave tracking robustness vulner-able. We rethink this paradigm with SAM2Matting, a novel frameworkthat decouples the task by enhancing the foundational tracker of SAM2with a region-proposal bridge and dedicated matting heads. This en-ables uncompromised SAM2 to handle tracking while the matting com-ponents focus exclusively on resolving fine-grained intricate details. No-tably, despite being trained only on images, SAM2Matting establishesnew state-of-the-art performance on video matting, with robust general-ization across both human-centric and in-the-wild matting scenarios.

---

## 论文详细总结（自动生成）

# SAM2Matting：通用图像与视频抠图 —— 论文深度总结

## 1. 核心问题与整体含义

**研究背景与动机**
- **抠图（Matting）** 是低层视觉的基础任务，目标是通过预测像素级 alpha matte 将前景目标与背景分离，公式为 $I = \alpha F + (1-\alpha)B$。
- 当扩展到**视频抠图**时，通常需要用户提供初始帧掩码以指定目标，并保证跨帧一致跟踪。
- 由此产生**根本性矛盾**：视频抠图同时要求
  - **高层语义理解**（如 VOS 中的鲁棒目标跟踪，需要逐帧理解）；
  - **低层细粒度感知**（如单图抠图中对发丝、半透明等极细节的建模）。
- **现有范式的问题**：主流方法依赖昂贵、领域特定的视频抠图数据集（多为人体中心），导致
  - 数据规模与多样性受限，**域外泛化能力弱**；
  - 从零训练难以获得鲁棒跟踪，微调预训练 VOS 模型又会**破坏原有跟踪鲁棒性**。

**核心问题（论文提出的关键设问）**
> 是否必须依赖这些标注成本极高、且覆盖面仍然狭窄的视频抠图数据集？

**整体含义**
- 论文主张：视频抠图可**解耦**为「已被大规模 VOS 数据解决的高层跟踪」+「已被丰富图像抠图数据覆盖的低层 alpha 估计」两个子任务。
- 提出 **SAM2Matting**：冻结 SAM2 跟踪器，仅训练专用抠图组件，**仅用图像数据训练**即在视频抠图上取得零样本 SOTA，并在人体中心与野外场景下均具备强泛化性。

---

## 2. 方法论

### 2.1 核心思想
- **解耦设计**：保持 SAM2 的完整跟踪能力（backbone 冻结），把细粒度 alpha 估计交给专门的抠图头。
- **统一流水线**：多源先验引导 → 识别抠图关键区域（ROI）→ 在 ROI 内生成并逐级精化 alpha。
- 三个模块：**ROI Detector（区域提议桥）**、**Pseudo-Trimap Generation**、**Progressive Alpha Predictor**。

### 2.2 ROI Detector（感兴趣区域检测器）
- 动机：传统做法要么用**规则化形态学操作**（膨胀/腐蚀）生成 trimap，隐含"边界重要性均匀"假设；要么**直接用原始掩码**作为 ROI。二者都会漏掉复杂结构内的细节，或把确定前景也纳入抠图。
- 做法：将 ROI 检测**重构为像素级二分类任务**（正样本 = 需要抠图的区域，即细粒度或半透明区域）。
- 输入：SAM2 掩码 $M$、当前帧 $I$、多尺度图像特征 $F$。
- 公式流程：
  - 每个尺度 $i$ 用卷积头预测 ROI logit 图：$L_{t,i} = f_{R}(I_{t,i}, M_{t,i}, F_{t,i})$
  - 多尺度聚合（上采样 + 拼接后经层次卷积网络）：$L_t = f_\varphi([U(L_{t,1}), \dots, U(L_{t,n})])$
  - 经 sigmoid 与阈值 $\theta$ 得到二值 ROI：$\mathcal{R}_t = \mathbb{1}[\sigma(L_t) \geq \theta]$

### 2.3 Pseudo-Trimap 生成
- 用 SAM2 掩码 $M_t$ 指定**确定前景/背景**，ROI $\mathcal{R}_t$ 指定**未知区域**：
  - $\mathcal{T}_t(h,w) = M_t(h,w)$，若 $\mathcal{R}_t(h,w)=0$；否则为 $0.5$。
- 作用：既保持结构完整性，又提供显式的前背景分离先验。

### 2.4 Progressive Alpha Predictor（渐进式 alpha 预测器）
- 与 ROI 的并行处理不同，alpha 估计被建模为**由粗到细的串行精化**过程，中间尺度结果作为下一尺度的引导。
- 复合输入：
  - $i=1$：$X_{t,1} = [F_{t,1}, \mathcal{T}_{t,1}, I_{t,1}]$
  - $i \geq 2$：$X_{t,i} = [F_{t,i}, \mathcal{T}_{t,i}, I_{t,i}, U(\mathcal{A}_{t,i-1})]$（含上一尺度上采样 matte）
- 每个尺度：投影层 $g_{\mathcal{A},i}$ 映射到固定维度，再经抠图头 $f_{\mathcal{A},i}$ 与 sigmoid 得到 $\mathcal{A}_{t,i}$；最细尺度的结果上采样到原分辨率作为最终 matte。

### 2.5 优化策略
- **训练设计**：冻结 SAM2 backbone 以保持跟踪能力，仅训练抠图组件；**仅在静态图像抠图数据上训练**。
- **ROI 监督**：对 GT alpha 在 $[\alpha,\beta]$ 内阈值化后做膨胀减腐蚀得到 GT ROI；损失为 focal loss + smooth-L1 loss（抑制 ROI 边界锯齿）。
- **Alpha 监督**：$L_1$ loss + Laplacian loss，并在所有尺度做**深度监督**。
- **Matte-Mask 一致性约束** $\mathcal{L}_{con}$：将预测 matte 以 $\gamma$ 阈值化得二值掩码，锚定到 SAM2 掩码，用 focal + dice 的联合分割损失，防止前景内部出现空洞。
- 总损失：$\mathcal{L} = \mathcal{L}_{\mathcal{R}} + \mathcal{L}_{\mathcal{A}}$，其中 $\mathcal{L}_{\mathcal{A}} = \mathcal{L}_{L_1} + \mathcal{L}_{lap} + \mathcal{L}_{con}$。

---

## 3. 实验设计

### 3.1 训练数据
- 使用 **8 个图像抠图数据集**：I-HIM50K、P3M-10k、CelebAHairMask-HQ、AIM-500、Distinctions-646、AM-2K、UHRIM、RefMatte。
- 为公平对比基线，另训练了与基线相同数据集的变体（*、† 标记）。
- **未使用任何视频抠图数据训练**（视频结果为严格零样本）。

### 3.2 评测基准与场景
- **图像抠图**：P3M-500-NP、AM-2K test、PPM-100。
- **视频抠图**：V-HIM60（Easy/Medium/Hard）、VideoMatte-SD。
- **指标**：MAD、MSE、Grad、Conn（越低越好）；视频额外用 **dtSSD**。
- 额外引入**基于光流的时序抖动指标** $F_{warp}$（用 RAFT Large 计算光流后做反向 warp 的 MSE）。

### 3.3 对比方法
- 图像：P3M、GFM、E2E-HIM、MAM、Matte Anything。
- 视频：OTVM、FTP-VM、InstMatt、SparseMat、MaGGIe、MatAnyone、RVM、以及原始 SAM2 分割。
- 骨干替换实验：Cutie-base、SAM2.1-Tiny、SAM2.1Long-B+、SAM3。

### 3.4 消融与附加实验
- ROI 策略消融（形态学 / 全掩码 / ROI Detector）。
- 架构与监督设计消融（渐进多尺度、一致性损失、平滑损失）。
- 视频数据微调对比（V-HIM2K5 微调 vs 不微调）。
- 效率对比（FPS / VRAM，多分辨率）。
- 跟踪不准确性鲁棒性、抖动效应、失败案例。

---

## 4. 资源与算力

- 论文明确说明：
  - **4 张 NVIDIA A6000 GPU**；
  - **训练 5 个 epoch**；
  - 优化器 **AdamW**，batch size **32**，学习率 **5 × 10⁻³**；
  - 骨干为 **SAM2.1 Hiera-B+**，且保持冻结。
- **未明确说明**的部分：单次训练的总时长（小时/天）、总 GPU 小时数、推理阶段具体硬件（除 A6000 外）、数据增强与网格搜索的额外算力开销。

---

## 5. 实验数量与充分性

**实验组数概览（约 10+ 组）**
1. 图像抠图对比（3 个 benchmark，含 2 个同数据变体 + Full 模型）；
2. 视频抠图零样本对比（4 个子集/数据集，多指标）；
3. 定性对比：人体抠图、野外视频、附件与背景干扰；
4. ROI 策略消融（3 种设置）；
5. 架构与监督消融（4 种组合）；
6. 视频数据微调影响（域内 vs 域外）；
7. FPS / VRAM 效率对比（多分辨率）；
8. 跟踪不准确性鲁棒性可视化；
9. 抖动效应定量 + 定性（4 个数据集）；
10. 骨干替换实验（5 种 tracker）；
11. 跟踪稳定性对比（真实视频）；
12. 失败案例分析。

**充分性与公平性评价**
- **优点**：
  - 覆盖图像 + 视频、人体 + 野外、定量 + 定性、精度 + 效率 + 时序一致性，维度全面；
  - 为公平比较，专门训练了与 MAM / Matte Anything 同数据集的变体，控制了数据变量；
  - 消融逐项验证了 ROI、渐进多尺度、一致性损失、平滑损失各自的贡献。
- **可改进之处**：
  - 消融主要在 V-HIM60-Hard 单一数据集上报告，跨数据集消融较少；
  - 部分基线（如 MaGGIe、RVM）在某些指标上"未报告"（表中为 –），比较存在不完整；
  - 图像抠图对比的基线数量相对有限，未与最新扩散类抠图方法对比；
  - 视频基准仍以人体中心为主（V-HIM60、VideoMatte），野外评测以定性为主，缺乏大规模野外定量基准。

---

## 6. 主要结论与发现

- **零样本视频抠图 SOTA**：仅用图像数据训练，在 V-HIM60 与 VideoMatte-SD 上多数指标超越全监督基线；V-HIM60-Hard 上 MAD 比 MatAnyone 降低 **11.89**，dtSSD 最低，时序一致性最佳。
- **图像抠图同样领先**：P3M-500-NP 上 MAD 比 MAM 低 **11.35**；AM-2K 上 MSE 比 Matte Anything 低 **24.8%**。
- **ROI Detector 有效**：优于形态学 trimap 与原始掩码，能捕获飞发、叶片、肢体间隙等细节（Hard 上 MAD 18.20 vs 20.07 vs 29.82）。
- **渐进多尺度 + 两类监督损失均有增益**：一致性损失填补前景空洞，平滑损失减少锯齿。
- **视频数据微调是双刃剑**：域内（V-HIM60-Hard）提升，但域外（AM-2K 动物数据）退化，说明视频抠图数据域窄、易过拟合。
- **实时高效**：任意分辨率下稳定 >27 FPS，VRAM 约 3.38 GB；MatAnyone 在 2160p 直接 OOM，1440p 仅 2.92 FPS。
- **框架骨干无关**：替换 Cutie、SAM2.1-T、SAM2.1Long、SAM3 均能取得强结果，SAM3 最佳。
- **对跟踪误差有鲁棒性**：多源融合使 ROI Detector 能补回 SAM2 漏掉的滑雪杖、剔除误纳的桌子。
- **跟踪稳定性强**：得益于强基础跟踪器，无需显式时序建模即可保持时序一致，优于 MatAnyone。

---

## 7. 优点（方法 / 实验设计亮点）

- **范式创新**：明确提出"解耦高层跟踪与低层抠图"，从"必须依赖视频抠图数据"的惯性中跳出，用图像数据解决视频任务，显著降低标注依赖。
- **架构即插即用**：框架对跟踪骨干不敏感，可换 Cutie / SAM2 各尺寸 / SAM3，工程实用性强。
- **ROI 学习化**：用可学习检测器替代形态学规则，将 ROI 检测显式建模为像素二分类，配合 focal + smooth 损失，精准定位"真正需要抠图"的区域。
- **伪 trimap 设计巧妙**：以 SAM2 掩码为确定区、ROI 为未知区，兼顾结构完整与前景背景分离。
- **多尺度深度监督 + 一致性约束**：既逐步恢复细结构，又防止前景空洞，损失设计有针对性且被消融验证。
- **实验设计考虑公平性**：设置同数据变体、控制变量；并主动讨论"微调视频数据是否有益"这一反直觉问题，结论有说服力。
- **效率与精度兼顾**：任意分辨率下稳定实时，具备落地潜力。
- **分析全面**：额外做了抖动指标、跟踪鲁棒性、失败案例，态度客观。

---

## 8. 不足与局限

**方法层面**
- 依赖 SAM2 的初始帧掩码输入，仍属**半交互式**设定，非全自动；掩码质量差时可能受影响。
- ROI 阈值 $\theta$、trimap 阈值 $\alpha,\beta,\gamma$ 依赖**网格搜索**，超参敏感性与自适应性问题未充分讨论。
- 冻结 backbone 意味着**无法从视频时序信息中学习**，时序一致性完全依赖跟踪器质量；对弱跟踪器（如 SAM2.1-T）性能下降。
- 论文指出极端过曝等**视觉线索本身丢失**的场景会失败（GT 亦不可定义），但未给出改进方向。

**实验覆盖与偏差风险**
- 视频定量基准仍以**人体中心**为主，野外场景主要靠定性展示，缺乏大规模野外定量评测，泛化结论的统计强度有限。
- 部分基线指标缺失（表中"–"），横向比较不完全对等。
- 消融集中于单一数据集（V-HIM60-Hard），跨数据集/跨骨干的消融不足。
- 抖动指标 $F_{warp}$ 依赖 RAFT 光流质量，光流本身误差可能污染评测结果。
- 训练数据虽为 8 个图像数据集，但以人像/自然图像为主，对特殊材质（烟、玻璃、毛发极细结构）的覆盖度未知。

**应用限制**
- 需要初始帧掩码，交互成本仍存在；长视频、目标频繁进出画面时的稳定性未系统评估。
- 单卡 A6000 上约 3.38 GB 显存、>27 FPS，但未报告端到端（含 SAM2 编码/记忆库）在超长视频上的内存增长情况。

---

（完）
