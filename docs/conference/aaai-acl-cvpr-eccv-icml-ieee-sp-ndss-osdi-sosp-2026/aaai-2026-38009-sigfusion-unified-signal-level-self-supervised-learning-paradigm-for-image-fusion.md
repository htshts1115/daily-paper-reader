---
title: "SigFusion: Unified Signal-Level Self-Supervised Learning Paradigm for Image Fusion"
title_zh: SigFusion：面向图像融合的统一信号级自监督学习范式
authors: "Zeyu Wang, Jiawei Feng, Jiayu Wang, Pengjie Wang, Haiyu Song"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38009/41971"
tags: ["query:cv-render"]
score: 4.0
evidence: 图像融合自监督范式
tldr: 图像融合领域长期受限于缺乏大规模真实训练数据，现有方法多依赖小规模或合成数据。为此提出SigFusion统一信号级自监督学习范式，利用伪标签生成网络从海量无标注自然图像自动合成训练集与伪标签，核心包含可学习一维信号调制器与SigFormer。实验验证该范式可推广至多种图像融合任务。其价值在于为融合类任务提供通用可迁移的自监督训练框架。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-001.webp\", \"caption\": \"\", \"page\": 5, \"index\": 1, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-002.webp\", \"caption\": \"\", \"page\": 5, \"index\": 2, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-003.webp\", \"caption\": \"\", \"page\": 5, \"index\": 3, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-004.webp\", \"caption\": \"\", \"page\": 5, \"index\": 4, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-005.webp\", \"caption\": \"\", \"page\": 5, \"index\": 5, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-006.webp\", \"caption\": \"\", \"page\": 5, \"index\": 6, \"width\": 537, \"height\": 302}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-007.webp\", \"caption\": \"\", \"page\": 5, \"index\": 7, \"width\": 516, \"height\": 408}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-008.webp\", \"caption\": \"\", \"page\": 5, \"index\": 8, \"width\": 546, \"height\": 404}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 545, \"height\": 294}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-010.webp\", \"caption\": \"\", \"page\": 5, \"index\": 10, \"width\": 516, \"height\": 374}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-011.webp\", \"caption\": \"\", \"page\": 5, \"index\": 11, \"width\": 535, \"height\": 357}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 553, \"height\": 301}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 416, \"height\": 320}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 535, \"height\": 311}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 443, \"height\": 393}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 479, \"height\": 369}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-022.webp\", \"caption\": \"\", \"page\": 5, \"index\": 22, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-023.webp\", \"caption\": \"\", \"page\": 5, \"index\": 23, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-024.webp\", \"caption\": \"\", \"page\": 5, \"index\": 24, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-025.webp\", \"caption\": \"\", \"page\": 5, \"index\": 25, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-026.webp\", \"caption\": \"\", \"page\": 5, \"index\": 26, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-027.webp\", \"caption\": \"\", \"page\": 5, \"index\": 27, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-028.webp\", \"caption\": \"\", \"page\": 5, \"index\": 28, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-029.webp\", \"caption\": \"\", \"page\": 5, \"index\": 29, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-030.webp\", \"caption\": \"\", \"page\": 5, \"index\": 30, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-031.webp\", \"caption\": \"\", \"page\": 5, \"index\": 31, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-032.webp\", \"caption\": \"\", \"page\": 5, \"index\": 32, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-033.webp\", \"caption\": \"\", \"page\": 5, \"index\": 33, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-034.webp\", \"caption\": \"\", \"page\": 5, \"index\": 34, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-035.webp\", \"caption\": \"\", \"page\": 5, \"index\": 35, \"width\": 520, \"height\": 520}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-036.webp\", \"caption\": \"\", \"page\": 5, \"index\": 36, \"width\": 448, \"height\": 389}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-037.webp\", \"caption\": \"\", \"page\": 5, \"index\": 37, \"width\": 443, \"height\": 393}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-038.webp\", \"caption\": \"\", \"page\": 5, \"index\": 38, \"width\": 443, \"height\": 380}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-039.webp\", \"caption\": \"\", \"page\": 5, \"index\": 39, \"width\": 443, \"height\": 380}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-040.webp\", \"caption\": \"\", \"page\": 5, \"index\": 40, \"width\": 443, \"height\": 380}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-041.webp\", \"caption\": \"\", \"page\": 5, \"index\": 41, \"width\": 443, \"height\": 380}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-042.webp\", \"caption\": \"\", \"page\": 5, \"index\": 42, \"width\": 449, \"height\": 380}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-043.webp\", \"caption\": \"\", \"page\": 5, \"index\": 43, \"width\": 443, \"height\": 408}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-044.webp\", \"caption\": \"\", \"page\": 5, \"index\": 44, \"width\": 443, \"height\": 393}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-045.webp\", \"caption\": \"\", \"page\": 5, \"index\": 45, \"width\": 443, \"height\": 393}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-046.webp\", \"caption\": \"\", \"page\": 5, \"index\": 46, \"width\": 417, \"height\": 393}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-047.webp\", \"caption\": \"\", \"page\": 5, \"index\": 47, \"width\": 443, \"height\": 388}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-048.webp\", \"caption\": \"\", \"page\": 5, \"index\": 48, \"width\": 443, \"height\": 408}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-049.webp\", \"caption\": \"\", \"page\": 5, \"index\": 49, \"width\": 443, \"height\": 408}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-050.webp\", \"caption\": \"\", \"page\": 5, \"index\": 50, \"width\": 444, \"height\": 388}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-051.webp\", \"caption\": \"\", \"page\": 5, \"index\": 51, \"width\": 443, \"height\": 393}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-052.webp\", \"caption\": \"\", \"page\": 5, \"index\": 52, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-053.webp\", \"caption\": \"\", \"page\": 5, \"index\": 53, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-054.webp\", \"caption\": \"\", \"page\": 5, \"index\": 54, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-055.webp\", \"caption\": \"\", \"page\": 5, \"index\": 55, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-056.webp\", \"caption\": \"\", \"page\": 5, \"index\": 56, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-057.webp\", \"caption\": \"\", \"page\": 5, \"index\": 57, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-058.webp\", \"caption\": \"\", \"page\": 5, \"index\": 58, \"width\": 508, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-059.webp\", \"caption\": \"\", \"page\": 5, \"index\": 59, \"width\": 512, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-060.webp\", \"caption\": \"\", \"page\": 5, \"index\": 60, \"width\": 518, \"height\": 416}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-061.webp\", \"caption\": \"\", \"page\": 5, \"index\": 61, \"width\": 542, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-062.webp\", \"caption\": \"\", \"page\": 5, \"index\": 62, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-063.webp\", \"caption\": \"\", \"page\": 5, \"index\": 63, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-064.webp\", \"caption\": \"\", \"page\": 5, \"index\": 64, \"width\": 535, \"height\": 306}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-065.webp\", \"caption\": \"\", \"page\": 7, \"index\": 65, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-066.webp\", \"caption\": \"\", \"page\": 7, \"index\": 66, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-067.webp\", \"caption\": \"\", \"page\": 7, \"index\": 67, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-068.webp\", \"caption\": \"\", \"page\": 7, \"index\": 68, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-069.webp\", \"caption\": \"\", \"page\": 7, \"index\": 69, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-070.webp\", \"caption\": \"\", \"page\": 7, \"index\": 70, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-071.webp\", \"caption\": \"\", \"page\": 7, \"index\": 71, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-072.webp\", \"caption\": \"\", \"page\": 7, \"index\": 72, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-073.webp\", \"caption\": \"\", \"page\": 7, \"index\": 73, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-074.webp\", \"caption\": \"\", \"page\": 7, \"index\": 74, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-075.webp\", \"caption\": \"\", \"page\": 7, \"index\": 75, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-076.webp\", \"caption\": \"\", \"page\": 7, \"index\": 76, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-077.webp\", \"caption\": \"\", \"page\": 7, \"index\": 77, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-078.webp\", \"caption\": \"\", \"page\": 7, \"index\": 78, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-079.webp\", \"caption\": \"\", \"page\": 7, \"index\": 79, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-080.webp\", \"caption\": \"\", \"page\": 7, \"index\": 80, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-081.webp\", \"caption\": \"\", \"page\": 7, \"index\": 81, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-082.webp\", \"caption\": \"\", \"page\": 7, \"index\": 82, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-083.webp\", \"caption\": \"\", \"page\": 7, \"index\": 83, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-084.webp\", \"caption\": \"\", \"page\": 7, \"index\": 84, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-085.webp\", \"caption\": \"\", \"page\": 7, \"index\": 85, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-086.webp\", \"caption\": \"\", \"page\": 7, \"index\": 86, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-087.webp\", \"caption\": \"\", \"page\": 7, \"index\": 87, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-088.webp\", \"caption\": \"\", \"page\": 7, \"index\": 88, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-089.webp\", \"caption\": \"\", \"page\": 7, \"index\": 89, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-090.webp\", \"caption\": \"\", \"page\": 7, \"index\": 90, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-091.webp\", \"caption\": \"\", \"page\": 7, \"index\": 91, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-092.webp\", \"caption\": \"\", \"page\": 7, \"index\": 92, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-093.webp\", \"caption\": \"\", \"page\": 7, \"index\": 93, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-094.webp\", \"caption\": \"\", \"page\": 7, \"index\": 94, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-095.webp\", \"caption\": \"\", \"page\": 7, \"index\": 95, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-096.webp\", \"caption\": \"\", \"page\": 7, \"index\": 96, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-097.webp\", \"caption\": \"\", \"page\": 7, \"index\": 97, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-098.webp\", \"caption\": \"\", \"page\": 7, \"index\": 98, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-099.webp\", \"caption\": \"\", \"page\": 7, \"index\": 99, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-100.webp\", \"caption\": \"\", \"page\": 7, \"index\": 100, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-101.webp\", \"caption\": \"\", \"page\": 7, \"index\": 101, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-102.webp\", \"caption\": \"\", \"page\": 7, \"index\": 102, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-103.webp\", \"caption\": \"\", \"page\": 7, \"index\": 103, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-104.webp\", \"caption\": \"\", \"page\": 7, \"index\": 104, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-105.webp\", \"caption\": \"\", \"page\": 7, \"index\": 105, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-106.webp\", \"caption\": \"\", \"page\": 7, \"index\": 106, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-107.webp\", \"caption\": \"\", \"page\": 7, \"index\": 107, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-108.webp\", \"caption\": \"\", \"page\": 7, \"index\": 108, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-109.webp\", \"caption\": \"\", \"page\": 7, \"index\": 109, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-110.webp\", \"caption\": \"\", \"page\": 7, \"index\": 110, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-111.webp\", \"caption\": \"\", \"page\": 7, \"index\": 111, \"width\": 875, \"height\": 656}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38009/fig-112.webp\", \"caption\": \"\", \"page\": 7, \"index\": 112, \"width\": 875, \"height\": 656}]"
motivation: 图像融合缺乏大规模真实训练数据，现有模型多依赖小规模或合成数据，限制泛化能力。
method: 提出统一信号级自监督范式，用伪标签生成网络从无标注自然图像合成训练集，含一维信号调制器与SigFormer。
result: 该范式可适用于多种图像融合任务，缓解了真实数据匮乏问题并提升训练可行性。
conclusion: 工作为图像融合提供了通用可迁移的自监督训练框架，对移动摄影融合管线具参考价值。
---

## Abstract
Image Fusion (IF) aims to integrate complementary features from multiple source images into a single image. However, a key challenge in this field is the lack of large-scale real-world training datasets. Existing models typically rely on either small datasets or synthetic, less realistic datasets. To address this, we propose SigFusion, a unified signal-level self-supervised learning paradigm for various IF tasks.The core idea is to use signal-level Pseudo-Label Generation Networks (PLGN) to automatically synthesize training sets and pseudo labels with real multi-source signal characteristics from vast unlabeled natural images.PLGN includes two critical components: learnable 1D Signal Modulators (SM) and SigFormer. SM learns implicit 1D signal patterns across various source images and embeds them into natural images, reducing the domain gap between synthetic and real datasets. SigFormer integrates Transformer with signal processing methods, establishing an appropriate signal representation space for SM. Its cascaded, multi-level design allows hierarchical feature learning from coarse to fine detail. Moreover, SigFormer can serve as a flexible backbone for IF, as its design adheres to the classic decomposition-reconstruction paradigm. Experimental results demonstrate that SigFusion achieves state-of-the-art performance across multiple IF tasks, including medical image fusion, infrared-visible image fusion, multi-focus image fusion, and multi-exposure image fusion.

---

## 论文详细总结（自动生成）

# SigFusion 论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **领域痛点**：图像融合（Image Fusion, IF）旨在把多源图像的互补信息整合到单张图像中，但该领域长期缺乏大规模真实训练数据，原因包括医学影像的患者隐私、遥感的保密要求、以及严格的预注册流程等。
- **现有两条技术路线的局限**：
  - **MMIF（多模态融合，如红外-可见光）**：多采用在小规模真实数据上的无监督学习，虽有精巧架构与损失函数，但受数据量限制易过拟合到有限场景分布，存在性能天花板。
  - **DPIF（数字摄影融合，如多聚焦、多曝光）**：依赖合成数据（亮度调整、局部模糊等），虽能规模化，但合成数据与真实数据间存在显著域差距，且任务特异性强。
- **核心研究问题**：能否构建一个**统一的数据集合成范式**，在多种 IF 任务上最大程度缩小合成数据与真实多源图像之间的域差距？
- **整体含义**：论文提出 **SigFusion**，宣称是首个面向图像融合的**统一信号级自监督学习（SSL）范式**，把"数据集合成"与"融合任务"统一到一个框架中，覆盖医学融合（MIF）、红外-可见光融合（VIF）、多聚焦融合（MFIF）、多曝光融合（MEF）四类任务。

## 2. 方法论

### 2.1 核心思想

- 采用经典两阶段 SSL 范式：
  - **Stage I（pretext 预训练）**：用伪标签生成网络 PLGN 从海量无标注自然图像合成"多源图像对 + 伪标签"，构建大规模融合训练集，预训练融合网络。
  - **Stage II（下游微调）**：在真实多源图像对上微调，完成域适应。
- 关键创新是**信号级**（而非像素级/特征级）建模：把图像视为由幅度、频率、相位刻画的简化 1D 信号，从而跨越模态、分辨率、动态范围差异。

### 2.2 关键技术组件

- **PLGN（Pseudo-Label Generation Network）**：由 **SM（Signal Modulator）** 与 **SigFormer** 组成。
- **SM（可学习 1D 信号调制器）**：
  - 从真实多源图像中学习隐式信号模式，注入自然图像，使其逼近目标模态（IR/VIS/CT/MRI/PET/多聚焦/多曝光）。
  - 低频信号用 **Transformer**（捕获长程依赖、广域上下文），高频信号用 **MLP**（高效调制稀疏高频子带）。
  - 不同模态对应独立 SM 模块（如 SM_IR,H、SM_VIS,L 等）。
- **SigFormer**：
  - 高度对称的**分解器（SF-Dec）+ 重构器（SF-Rec）**结构，遵循"分解-重构"经典范式。
  - 每个子模块：MHSA 建立全局依赖 → 2D 转 1D（下采样 + 1×1 卷积 + flatten）→ **EWT（经验小波变换）** 分解出低频 L 与两个高频 H¹、H² → 1D 转 2D 回融 → MLP 映射。
  - 级联多级设计实现从粗到细的层次化特征学习，逐级只分解低频、保留高频。
  - 重构器把 EWT 分解替换为 EWT 重构，逐级恢复信号。
  - **双重用途**：带 SM 时作 PLGN；不带 SM 时直接作为 IF 融合骨干。

### 2.3 算法流程与公式要点

- **Pretext 目标（Eq.1）**：对无标注图像 Xᵢ，用 G₁(Xᵢ)、G₂(Xᵢ) 生成两个伪标签，既作融合网络输入又作监督信号，最小化 L(FN_θ(G₁(Xᵢ),G₂(Xᵢ)), G₁(Xᵢ), G₂(Xᵢ))。
- **融合网络**：用 SigFormer 分解器把 G₁、G₂ 转成频率子带集合，通道拼接后由重构器输出融合图。
- **损失函数**：
  - MMIF：`L_MMIF = α₁L_mse + β₁L_ssim + γ₁(L_MaxL1 + L_GradL1)`（空间像素最大值域与梯度域的 L1）。
  - DPIF：`L_DPIF = α₂L_ssim + β₂(L_MaxL1 + L_GradL1)`。
- **PLGN 训练策略（Eq.4–7）**：以**多个融合模型输出的融合图像为输入**，以**真实源图像为 GT**，即让网络学习"从融合图反向恢复源图"，增强对源特征的敏感性。SM 将融合图信号映射到 GT 信号（Eq.5），再由重构器生成输出 S（Eq.6）；损失同时约束信号级（低频 L_GT、高频 H_GT 的 MSE）与像素级（MSE）。
- **SigFormer 自预训练（Eq.15）**：在大规模自然图像上以自重建方式无监督预训练，保证分解-重构鲁棒性。
- **Stage II 微调（Eq.16）**：在真实多源图像对上用相同损失微调，继承 SigFormer 权重。
- **训练规模放大机制**：M 组源图像对 × N 个融合模型 × Z 个频带 → 共 **2M×N×Z** 组 1D 信号对，构成 PLGN 训练集。

## 3. 实验设计

- **任务与数据集**：
  - **VIF**：MSRS 训练；M³FD、TNO 测试。
  - **MIF**：Harvard 医学网站 334 对（300/34 划分）；测试 21 对 MRI-CT、42 对 MRI-PET。
  - **MFIF**：RealMFF（710 对）训练；LYTRO、MFFW 测试。
  - **MEF**：SICE 训练集训练；SICE 测试集与 MEFB 测试。
  - **Pretext 阶段**：Flickr25k（25,000 张），每图合成 4 个变体，共 4×25,000 张，形成 4 个基准集。
- **评价指标**：QG、QM、QP、MI、SD、VIFF。除无参考的 SD 外，其余均以两张源图像为监督（沿用 IF 主流做法）。
- **对比方法（20+ 个）**：
  - VIF/MIF：U2Fusion、DeFusion、CDDFuse、LRRNet、MURF、EMMA、Text-DiFuse、FILM、C2RF、GIF-Net、DCEvo、OminiFuse、MTG-Fusion。
  - MFIF：CU-Net、U2Fusion、IFCNN、SDNet、DeFusion、DIFNet、FusionDiff、MGDN、ZMFF、DeepM²CDL、FILM、GIF-Net。
  - MEF：CU-Net、U2Fusion、IFCNN、MEF-GAN、SDNet、SwinFusion、DeFusion、DIFNet、MGDN、HoLoCo、FILM、GIF-Net。
- **消融实验设计**：
  - **SM 消融**：全部移除 / 仅移除高频 SM / 仅移除低频 SM / 保留全部。
  - **SigFormer 消融**：仅 Transformer（无 EWT）/ Transformer 换 CNN / EWT 换 DWT / 默认设计。
  - **Pretext 消融**：无 PT / 有 PT 但无 PLGN（直接自然图）/ 默认。
  - **PLGN 泛化实验**：用合成数据集预训练其他 IF 模型，再在其原始数据集上微调（结果放补充材料）。
  - **合成数据可视化**：Fig.5、Fig.6 对比真实源图、自然图与调制后信号。

## 4. 资源与算力

- 文中明确提到的硬件环境：**Intel i9-14900k CPU + RTX 4090 GPU + 128 GB RAM**，PyTorch + CUDA 12.1。
- 训练超参：Adam 优化器，学习率 1×10⁻⁴，**100 epochs**，batch size 16；EWT 分解器用 2 个子带（两个子模块）。
- **未明确说明的部分**：GPU 的具体数量（仅写 "RTX 4090 GPU"，未标注张数）、总训练时长、模型参数量、推理时延与显存占用等均未给出，因此算力成本无法精确评估。

## 5. 实验数量与充分性

- **实验规模**：
  - 4 大融合任务 × 多个测试集（M³FD、TNO、MRI-CT、MRI-PET、LYTRO、MFFW、MEFB、SICE），合计约 8 个测试场景。
  - 每场景对比 12–13 个 SOTA 方法，共涉及 20 余个基线。
  - 主结果表 1 张（含 4 类任务的 8 个子表）；消融表 2 张（VIF 与 MFIF 各 7 个变体）；定性对比图多组。
- **充分性评价**：
  - **优点**：任务覆盖面广、指标数量多、基线新颖（含 2025 年 CVPR/IJCV 工作）、消融维度较系统（SM / SigFormer / PT 三条主线）。
  - **局限**：消融结果仅在 VIF 与 MFIF 上呈现，其余任务结果置于补充材料，正文证据链不完整；PLGN 泛化实验同样只在补充材料。
- **客观性与公平性**：
  - 对比方法引用年份新、来源广，指标选取遵循主流实践。
  - 但**未详述各基线的训练设置、数据划分与复现细节**，无法完全排除训练数据/调参差异带来的不公平。
  - 部分指标上 SigFusion 并非最优（如 VIF-TNO 的 SD 与 VIFF 略低、MIF MRI-PET 的 SD、MFIF-LYTRO 的 SD），说明优势是"多数指标领先"而非全面碾压。

## 6. 主要结论与发现

- SigFusion 在 **VIF、MIF、MFIF、MEF 四类任务上多数指标达到 SOTA**，是首个信号级 SSL 图像融合方法。
- **SM 不可或缺**：任意移除（全去 / 去高频 / 去低频）都导致性能下降，验证其调制自然图像信号至目标模态的关键作用。
- **SigFormer 设计有效**：Transformer + EWT 的组合优于纯 Transformer、CNN 替代 Transformer、以及 DWT 替代 EWT 的变体。
- **Pretext 预训练显著提升**：有 PT 明显优于无 PT，且"无 PLGN 的 PT"也不如默认方案，说明数据集合成与伪标签生成的价值。
- **可视化验证**：调制后的自然图像在视觉上与目标模态一致（红外强度、边缘弱化、离焦模糊、曝光变化等），信号确实被"推向"目标模态。
- **可迁移性**：PLGN 合成的大规模数据集可用于提升其他 IF 模型的性能（结论指向补充材料）。

## 7. 优点

- **范式创新**：首次把 IF 的数据集合成与融合任务统一在**信号级 SSL** 框架下，一个框架适配四类融合任务。
- **降域差距的思路新颖**：用 1D 信号（幅度/频率/相位）抽象图像，绕开模态、分辨率、动态范围差异，比像素级/特征级合成更贴近真实分布。
- **组件复用性强**：SigFormer 既作 PLGN 组件又作融合骨干，参数共享、结构自洽。
- **经典与深度结合**：把 EWT 分解-重构与 Transformer
