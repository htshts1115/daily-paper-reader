---
title: Parallax Portrait Matting
title_zh: 视差人像抠图
authors: "Xin Cai, Jiawen Chen, Lars Jebe, Tianfan Xue, Zhoutong Zhang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/5777.pdf"
tags: ["query:matting"]
score: 9.0
evidence: 人像抠图与视差前景背景分离
tldr: 单图抠图在前景与背景均富纹理时高度病态，现有方法常依赖绿幕、偏振光或干净背景等专用采集条件。本文提出视差人像抠图，利用连拍中轻微视角变化产生的视差，估计三分图与前景背景运动并构建互补观测。实验表明该方法在挑战性纹理场景下取得更优抠图结果，且无需专用采集设备。该工作为自然场景下的人像抠图提供了实用且易获取的两帧解决方案。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 598, \"height\": 478}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 613, \"height\": 490}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1224, \"height\": 980}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 778, \"height\": 648}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 902, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 1723, \"height\": 1357}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 901, \"height\": 787}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 1226, \"height\": 980}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 932, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 908, \"height\": 807}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 903, \"height\": 807}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 480, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-013.webp\", \"caption\": \"\", \"page\": 2, \"index\": 13, \"width\": 919, \"height\": 826}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-014.webp\", \"caption\": \"\", \"page\": 7, \"index\": 14, \"width\": 591, \"height\": 438}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-015.webp\", \"caption\": \"\", \"page\": 7, \"index\": 15, \"width\": 497, \"height\": 367}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-016.webp\", \"caption\": \"\", \"page\": 7, \"index\": 16, \"width\": 537, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-017.webp\", \"caption\": \"\", \"page\": 7, \"index\": 17, \"width\": 590, \"height\": 433}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-018.webp\", \"caption\": \"\", \"page\": 7, \"index\": 18, \"width\": 588, \"height\": 436}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-019.webp\", \"caption\": \"\", \"page\": 7, \"index\": 19, \"width\": 587, \"height\": 435}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 859, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-021.webp\", \"caption\": \"\", \"page\": 7, \"index\": 21, \"width\": 350, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 376, \"height\": 374}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 410, \"height\": 410}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 859, \"height\": 861}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 857, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-026.webp\", \"caption\": \"\", \"page\": 7, \"index\": 26, \"width\": 528, \"height\": 528}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-027.webp\", \"caption\": \"\", \"page\": 7, \"index\": 27, \"width\": 444, \"height\": 444}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 925, \"height\": 931}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 860, \"height\": 867}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 924, \"height\": 923}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-032.webp\", \"caption\": \"\", \"page\": 8, \"index\": 32, \"width\": 540, \"height\": 540}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-033.webp\", \"caption\": \"\", \"page\": 8, \"index\": 33, \"width\": 917, \"height\": 923}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-034.webp\", \"caption\": \"\", \"page\": 8, \"index\": 34, \"width\": 852, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-035.webp\", \"caption\": \"\", \"page\": 8, \"index\": 35, \"width\": 924, \"height\": 932}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-036.webp\", \"caption\": \"\", \"page\": 8, \"index\": 36, \"width\": 859, \"height\": 868}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-037.webp\", \"caption\": \"\", \"page\": 8, \"index\": 37, \"width\": 916, \"height\": 923}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-038.webp\", \"caption\": \"\", \"page\": 8, \"index\": 38, \"width\": 851, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-039.webp\", \"caption\": \"\", \"page\": 8, \"index\": 39, \"width\": 922, \"height\": 923}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-040.webp\", \"caption\": \"\", \"page\": 8, \"index\": 40, \"width\": 857, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-041.webp\", \"caption\": \"\", \"page\": 8, \"index\": 41, \"width\": 925, \"height\": 917}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-042.webp\", \"caption\": \"\", \"page\": 8, \"index\": 42, \"width\": 860, \"height\": 853}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-043.webp\", \"caption\": \"\", \"page\": 8, \"index\": 43, \"width\": 925, \"height\": 923}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-044.webp\", \"caption\": \"\", \"page\": 8, \"index\": 44, \"width\": 860, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-045.webp\", \"caption\": \"\", \"page\": 8, \"index\": 45, \"width\": 925, \"height\": 926}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-046.webp\", \"caption\": \"\", \"page\": 8, \"index\": 46, \"width\": 860, \"height\": 862}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-047.webp\", \"caption\": \"\", \"page\": 12, \"index\": 47, \"width\": 650, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-048.webp\", \"caption\": \"\", \"page\": 12, \"index\": 48, \"width\": 647, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-049.webp\", \"caption\": \"\", \"page\": 12, \"index\": 49, \"width\": 651, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-050.webp\", \"caption\": \"\", \"page\": 12, \"index\": 50, \"width\": 646, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-051.webp\", \"caption\": \"\", \"page\": 12, \"index\": 51, \"width\": 651, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-052.webp\", \"caption\": \"\", \"page\": 12, \"index\": 52, \"width\": 648, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-053.webp\", \"caption\": \"\", \"page\": 12, \"index\": 53, \"width\": 648, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-054.webp\", \"caption\": \"\", \"page\": 12, \"index\": 54, \"width\": 650, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-055.webp\", \"caption\": \"\", \"page\": 12, \"index\": 55, \"width\": 626, \"height\": 622}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-056.webp\", \"caption\": \"\", \"page\": 12, \"index\": 56, \"width\": 650, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-057.webp\", \"caption\": \"\", \"page\": 12, \"index\": 57, \"width\": 647, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-058.webp\", \"caption\": \"\", \"page\": 12, \"index\": 58, \"width\": 651, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-059.webp\", \"caption\": \"\", \"page\": 12, \"index\": 59, \"width\": 646, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-060.webp\", \"caption\": \"\", \"page\": 12, \"index\": 60, \"width\": 651, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-061.webp\", \"caption\": \"\", \"page\": 12, \"index\": 61, \"width\": 648, \"height\": 649}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-062.webp\", \"caption\": \"\", \"page\": 12, \"index\": 62, \"width\": 648, \"height\": 649}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-063.webp\", \"caption\": \"\", \"page\": 12, \"index\": 63, \"width\": 650, \"height\": 651}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-064.webp\", \"caption\": \"\", \"page\": 12, \"index\": 64, \"width\": 622, \"height\": 622}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-065.webp\", \"caption\": \"\", \"page\": 12, \"index\": 65, \"width\": 649, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-066.webp\", \"caption\": \"\", \"page\": 12, \"index\": 66, \"width\": 648, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-067.webp\", \"caption\": \"\", \"page\": 13, \"index\": 67, \"width\": 1691, \"height\": 1732}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-068.webp\", \"caption\": \"\", \"page\": 13, \"index\": 68, \"width\": 1691, \"height\": 1732}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-069.webp\", \"caption\": \"\", \"page\": 13, \"index\": 69, \"width\": 886, \"height\": 908}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-070.webp\", \"caption\": \"\", \"page\": 13, \"index\": 70, \"width\": 1691, \"height\": 1732}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-071.webp\", \"caption\": \"\", \"page\": 13, \"index\": 71, \"width\": 500, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-072.webp\", \"caption\": \"\", \"page\": 13, \"index\": 72, \"width\": 500, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-073.webp\", \"caption\": \"\", \"page\": 13, \"index\": 73, \"width\": 500, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-074.webp\", \"caption\": \"\", \"page\": 13, \"index\": 74, \"width\": 500, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-075.webp\", \"caption\": \"\", \"page\": 13, \"index\": 75, \"width\": 816, \"height\": 836}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-076.webp\", \"caption\": \"\", \"page\": 13, \"index\": 76, \"width\": 432, \"height\": 346}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-077.webp\", \"caption\": \"\", \"page\": 13, \"index\": 77, \"width\": 1152, \"height\": 920}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-078.webp\", \"caption\": \"\", \"page\": 13, \"index\": 78, \"width\": 1186, \"height\": 950}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-079.webp\", \"caption\": \"\", \"page\": 13, \"index\": 79, \"width\": 1186, \"height\": 950}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-080.webp\", \"caption\": \"\", \"page\": 13, \"index\": 80, \"width\": 1186, \"height\": 950}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-081.webp\", \"caption\": \"\", \"page\": 13, \"index\": 81, \"width\": 1186, \"height\": 950}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-082.webp\", \"caption\": \"\", \"page\": 13, \"index\": 82, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-083.webp\", \"caption\": \"\", \"page\": 13, \"index\": 83, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-084.webp\", \"caption\": \"\", \"page\": 13, \"index\": 84, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-085.webp\", \"caption\": \"\", \"page\": 13, \"index\": 85, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-086.webp\", \"caption\": \"\", \"page\": 13, \"index\": 86, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-087.webp\", \"caption\": \"\", \"page\": 13, \"index\": 87, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-088.webp\", \"caption\": \"\", \"page\": 13, \"index\": 88, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-089.webp\", \"caption\": \"\", \"page\": 13, \"index\": 89, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-090.webp\", \"caption\": \"\", \"page\": 13, \"index\": 90, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-091.webp\", \"caption\": \"\", \"page\": 13, \"index\": 91, \"width\": 408, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-092.webp\", \"caption\": \"\", \"page\": 14, \"index\": 92, \"width\": 778, \"height\": 650}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-093.webp\", \"caption\": \"\", \"page\": 14, \"index\": 93, \"width\": 1186, \"height\": 989}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-094.webp\", \"caption\": \"\", \"page\": 14, \"index\": 94, \"width\": 1186, \"height\": 989}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-095.webp\", \"caption\": \"\", \"page\": 14, \"index\": 95, \"width\": 1186, \"height\": 989}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-096.webp\", \"caption\": \"\", \"page\": 14, \"index\": 96, \"width\": 1190, \"height\": 992}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-097.webp\", \"caption\": \"\", \"page\": 14, \"index\": 97, \"width\": 353, \"height\": 353}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-098.webp\", \"caption\": \"\", \"page\": 14, \"index\": 98, \"width\": 968, \"height\": 968}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-099.webp\", \"caption\": \"\", \"page\": 15, \"index\": 99, \"width\": 501, \"height\": 406}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-100.webp\", \"caption\": \"\", \"page\": 15, \"index\": 100, \"width\": 640, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-101.webp\", \"caption\": \"\", \"page\": 15, \"index\": 101, \"width\": 502, \"height\": 406}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9694c7d027e4ecf339bda15f/fig-102.webp\", \"caption\": \"\", \"page\": 15, \"index\": 102, \"width\": 1057, \"height\": 846}]"
motivation: 单图抠图在前景背景均富纹理时病态，现有方法依赖绿幕、偏振光或干净背景等专用采集条件。
method: 提出视差人像抠图，利用连拍中轻微视角变化产生的视差，估计三分图与前景背景运动并构建互补观测。
result: 在挑战性纹理场景下取得更优抠图结果，且无需专用采集设备。
conclusion: 为自然场景人像抠图提供实用且易获取的两帧解决方案。
---

## Abstract
Image matting is highly ill-posed, especially when both theforeground and background are richly textured. While single-image mat-ting methods learn strong priors from data, they often struggle on thesechallenging cases. Existing approaches improve results by requiring ad-ditional signals such as green screens, polarized lighting, or clean back-ground images, but these typically rely on specialized capture setups.We present Parallax Portrait Matting, a practical two-frame mattingmethod that uses a second image captured with slight viewpoint change.Such a setting arises naturally in burst photography, where small cameramotion induces foreground-background parallax and provides comple-mentary observations for matting. Our pipeline estimates trimaps andforeground/background motion, then constructs aligned views for pre-diction. To handle imperfect motion estimation, the network uses thebackground-aligned pair for direct fusion and the foreground-aligned cuethrough cross-attention for error compensation. Experiments show thatour method recovers finer details and more accurate foreground colorsthan strong single-image matting baselines on challenging portrait cases.

---

## 论文详细总结（自动生成）

# 《Parallax Portrait Matting（视差人像抠图）》论文总结

## 1. 核心问题与整体含义

- **研究背景**：图像抠图（image matting）旨在将图像分解为前景 F、背景 B 与透明度 α，满足线性合成公式 I = αF + (1−α)B。该问题本质上是高度病态的（ill-posed）：单张图像只有 1 个（灰度）或 3 个（彩色）约束，却需求解 3 或 7 个未知量，解空间无穷大。
- **核心痛点**：当**前景与背景都纹理丰富**时，单图抠图方法（无论基于数据先验还是生成模型先验）往往难以区分前景细节与背景，尤其是发丝、半透明边界等区域。
- **现有替代方案的局限**：已有工作通过引入额外信号（绿幕、偏振光、相机阵列、焦点堆栈、干净背景图等）来缓解病态性，但均需**专用硬件或受控采集流程**，难以在日常摄影中普及。
- **本文主张**：提出 **Parallax Portrait Matting（视差人像抠图）**，利用**连拍（burst）中轻微相机移动带来的前景/背景视差**作为额外观测。由于人像主体通常离相机更近，前后景呈现不同的表观运动，视差自然提供了分离细结构的补充约束，且**无需任何专用设备**。

---

## 2. 方法论

### 2.1 核心思想

- 给定基础帧 I₁ 与另一帧 I₀（轻微视角变化），定义前景运动场 M^F_{1→0} 与背景运动场 M^B_{1→0}，则两帧抠图方程通过运动场关联：

  I₀ = M^F_{1→0}(α₁F₁) + (1 − M^F_{1→0}(α₁))·M^B_{1→0}(B₁)

- **关键洞察**：视差约束只有在 M^F ≠ M^B 时才有用；当两层运动相同时方程线性相关，因此方法自然要求“存在视差 + 场景基本静止 + 两帧曝光/白平衡一致”的操作域。
- **运动可靠性不对称**：背景通常更远、运动更平滑、对齐更可靠；前景（尤其发丝）存在非刚性运动与残留光流误差。因此设计上**保守使用运动线索**：背景对齐用于像素级直接融合，前景对齐仅作为特征级噪声辅助线索。

### 2.2 技术流程

- **Trimap 估计**：用 BiRefNet 生成二值前景掩码，腐蚀/膨胀各 100 像素，得到 200 像素宽的不确定带（足以覆盖现代分割模型误差）。
- **运动估计**：
  - 用 GMFlow 估计两帧光流；
  - 对遮挡/不确定区域，采用“局部平滑”假设，将不确定区域运动替换为最近邻的确定区域运动值（前景、背景分别 inpaint）。
  - 背景对齐图 I^B_{0→1} = M^B_{0→1}(I₀) 仅在重叠区与 I₁ 有差异，可揭示被遮挡背景；前景对齐图 I^F_{0→1} = M^F_{0→1}(I₀) 则让前景静止、背景移动，直接提示前景对象。
- **网络架构（双分支、对称结构、非对称功能）**：
  - **主分支（背景对齐）**：输入 I₁、I^B_{0→1}、Trimap Tr₁，直接像素级融合，预测基础帧的 α₁ 与 F₁。
  - **辅助分支（前景对齐）**：输入 I^F_{0→1}、伴随帧 M^F_{0→1}(M^B_{1→0}(I₁))、扭曲 Trimap M^F_{0→1}(Tr₀)，预测前景对齐视角的 α 与 F。
  - **交互方式**：两分支通过 **cross-attention（交叉注意力）** 在特征空间建立软对应，而非直接像素拼接，从而在对应可靠处借用信息、在运动误差处抑制不可靠证据。
  - 两分支**共享权重**，鼓励统一表征，使网络能同时受益于单图抠图数据与多帧视差线索。
  - 编码器/解码器使用 ViT-Small，MatteHead 来自 ViTMatte，总参数 38.6M；用 CroCo 跨视角预训练权重初始化（初始化选择而非必需组件）。
- **训练损失**：
  - Alpha 损失：将像素分为“软像素”（0<α<1，集合 S）与“硬像素”（α=0 或 1，集合 H）分别归一化加权 L1，记为 L_sep；另加 Laplacian 损失 L_laplacian 与梯度惩罚 L_grad。
  - 前景颜色损失：预测预乘前景 αF，用合成损失监督：L_composition = ‖Iᵢ − (αᵢFᵢ + (1−αᵍᵗᵢ)Bᵍᵗᵢ)‖。
  - 总损失：L_total = L_sep + L_laplacian + L_grad + L_composition。
- **Patch 训练/推理**：以 Trimap Tr₁ 提取 448×448 patch（覆盖所有不确定区域），相邻 patch 重叠 224 像素，融合时用高斯窗口加权，实现高分辨率无缝拼接。

---

## 3. 实验设计

- **训练数据（仅合成）**：
  - 前景来自 P3M-10K（9,421 张）与 HHM-2K（2,000 张），用 layer-diffusion 生成伪前景颜色标注；
  - 背景来自 BG-20K（15,000 张）；
  - 对 α 做随机 gamma 变换增强；对 50% 前景做直方图均衡以缩小合成—真实差距；对前景与背景分别施加随机仿射变换模拟运动，并加入约 10 像素随机噪声防止完美对齐；训练 trimap 由 GT alpha 二值化后随机膨胀/腐蚀（60–120 次迭代）生成。
- **测试数据**：
  - 合成测试：P3M-500-NP、PPM-100、RWP-636 作为前景，BG-20K 测试集作为背景。
  - 真实数据：自采集 RAW 图像对（固定相机参数，Adobe Lightroom 一致渲染），场景含轻微视差。
- **评价指标**：SAD、MSE、Connectivity（Conn）、Grad（均按惯例放大 10³）；前景颜色用预乘前景 MSE(αF) 衡量。不预测前景色的方法按 [23] 协议用输入×预测 α 替代。
- **对比方法**：
  - Trimap-free 单图：MODNet、ViTAE-S；
  - Trimap-based 单图：MG-Matting、MatteFormer；
  - 视频抠图：MaGGIe、MatAnyone（视为相邻帧参考）；
  - 商业闭源方案：Adobe Photoshop、Remove.bg（真实图定性对比）。
  - 所有 trimap-based 方法统一使用同一 BiRefNet trimap，避免 trimap 质量带来的不公平。

---

## 4. 资源与算力

- 论文明确说明：训练使用 **8 张 NVIDIA RTX 4090 GPU**，每 GPU batch size 为 2，AdamW 优化器，学习率 5×10⁻⁵，训练 **50 个 epoch**，每 epoch 含 **100K 合成 patch 对**。
- 网络本身约 38.6M 参数（与 MatteFormer 44.7M、MatAnyone 35.2M 相当或更少）。
- 完整流程还额外使用 BiRefNet（约 200M）做 trimap 估计、GMFlow（7.4M）做运动估计，二者均为现成组件、可替换。
- **未提及**：具体训练总时长（小时/天）、单次推理耗时、显存占用等细节。

---

## 5. 实验数量与充分性

- **定量实验**：在 3 个合成测试集（PPM-100、P3M-NP-500、RWP-636）上与 6 个方法全面比较，覆盖 alpha 4 项指标 + 前景颜色 1 项指标。
- **定性实验**：合成测试集定性对比（Fig. 5）；真实场景对比（Fig. 6）；与商业方案（Adobe Photoshop、Remove.bg）对比（Fig. 7）；补充材料含更多真实示例。
- **消融实验**（Tab. 2，PPM-100）：共 5 个变体——
  1. 去掉背景对齐帧；
  2. 去掉前景对齐帧；
  3. 单分支（单图版本）；
  4. 两分支输入同一帧（无视差退化情形）；
  5. 推理时加入运动噪声。
- **充分性评价**：
  - **优点**：消融覆盖了各组件贡献与退化情形，验证了“双线索互补且不可互换”以及“对视差缺失/对齐误差的优雅退化”；统一 trimap 保证了公平性；同时与闭源商业方案对比，增强了说服力。
  - **可改进处**：真实数据为作者自采集，规模与多样性未量化；视频基线并非为两帧视差设计，比较只能作为参考；训练完全依赖合成数据，伪前景颜色标注的质量上限未被独立评估。

---

## 6. 主要结论与发现

- 在合成测试集上，本方法在**所有指标上一致优于**所有单图与视频抠图基线；前景颜色精度（MSE of αF）相对最佳基线**降低 35–45%**，这对下游合成任务尤为关键。
- 真实场景中，即使仅用合成数据训练，本方法也能产生更干净的 alpha、更准确的前景颜色与更细的发丝结构，细节优于 Adobe Photoshop 与 Remove.bg。
- 消融表明：去掉背景对齐主要损失细细节；去掉前景对齐主要造成前后景混淆；输入同一帧时性能退化至接近单分支，证明收益来自**视差本身**而非“多一帧”。
- 加入运动噪声后仍优于单图基线，验证了“前景对齐作为特征级噪声线索”的设计有效性。

---

## 7. 优点

- **问题定位实用**：仅需一张轻微视角变化的额外图像，天然契合手机连拍场景，无需绿幕/偏振/相机阵列等专用设备。
- **设计洞察清晰**：明确区分前景/背景运动可靠性的不对称性，并以“背景直接融合 + 前景 cross-attention 补偿”的非对称架构优雅应对，具有可解释性。
- **鲁棒性设计**：共享权重、特征级软对应、运动噪声增强训练，使模型在视差弱或对齐差时平滑退化为强单图预测，而非灾难性失败。
- **兼顾前景颜色**：不仅预测 alpha，还通过预乘前景与合成损失显著提升前景色精度，直击下游合成的实际需求。
- **公平对比**：统一 trimap 来源，并与闭源商业方案同台定性比较，结论可信度较高。

---

## 8. 不足与局限

- **运动估计与训练解耦**：光流（GMFlow）为现成模块，不能与抠图网络联合优化，误差无法端到端修正。
- **运动幅度受限**：帧间运动较大或更复杂时性能可能下降；论文假设场景基本静止，风力、头发飘动、主体移动会引入残差运动。
- **极端模糊场景仍失效**：低光照、或整个 burst 中主体与背景始终难以区分时，视差不足以提供有效约束。
- **真实数据规模有限**：真实评估为作者自采集的少量场景，缺乏大规模、多设备、多光照的系统性真实基准；模型完全依赖合成数据训练，存在合成—真实域差距风险。
- **算力与效率未充分报告**：未给出训练总时长、推理速度与显存需求；完整流程还需额外 200M 参数的 BiRefNet，部署成本需进一步评估。
- **场景覆盖偏窄**：方法定位为人像抠图，对非人像主体、透明物体、剧烈形变等场景的适用性未做验证。

（完）
