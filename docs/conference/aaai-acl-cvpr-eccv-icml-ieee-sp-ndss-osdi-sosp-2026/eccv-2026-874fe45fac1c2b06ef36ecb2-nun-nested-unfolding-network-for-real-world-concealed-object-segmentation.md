---
title: "NUN: Nested Unfolding Network for Real-World Concealed Object Segmentation"
title_zh: NUN：面向真实世界隐藏物体分割的嵌套展开网络
authors: "Chunming He, Rihan Zhang, Longxiang Tang, Dingming Zhang, Bojian Zhang, Fengyang Xiao, Jingjia Feng, Sina Farsiu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/3369.pdf"
tags: ["query:seg"]
score: 5.0
evidence: 面向真实世界分割的展开网络
tldr: 真实世界视觉感知需要同时应对图像退化与高层语义理解，但复原偏好细粒度纹理、分割偏好语义对比，二者存在内在冲突。作者提出嵌套展开网络NUN，把抗退化的展开网络嵌入到分割导向展开网络的每个阶段，使两项任务在各自子空间优化又受控交互。实验表明该框架在隐藏物体分割上兼顾纹理恢复与语义分割效果。该工作为退化条件下的分割提供了统一且可解释的求解框架。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 452, \"height\": 337}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-016.webp\", \"caption\": \"\", \"page\": 1, \"index\": 16, \"width\": 452, \"height\": 338}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 503, \"height\": 677}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 502, \"height\": 675}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 502, \"height\": 675}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 502, \"height\": 675}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-021.webp\", \"caption\": \"\", \"page\": 13, \"index\": 21, \"width\": 551, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-022.webp\", \"caption\": \"\", \"page\": 13, \"index\": 22, \"width\": 551, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-023.webp\", \"caption\": \"\", \"page\": 13, \"index\": 23, \"width\": 524, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-024.webp\", \"caption\": \"\", \"page\": 13, \"index\": 24, \"width\": 524, \"height\": 395}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-025.webp\", \"caption\": \"\", \"page\": 13, \"index\": 25, \"width\": 393, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-026.webp\", \"caption\": \"\", \"page\": 13, \"index\": 26, \"width\": 393, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-027.webp\", \"caption\": \"\", \"page\": 13, \"index\": 27, \"width\": 393, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-028.webp\", \"caption\": \"\", \"page\": 13, \"index\": 28, \"width\": 393, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-029.webp\", \"caption\": \"\", \"page\": 13, \"index\": 29, \"width\": 393, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-030.webp\", \"caption\": \"\", \"page\": 13, \"index\": 30, \"width\": 393, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-031.webp\", \"caption\": \"\", \"page\": 13, \"index\": 31, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-032.webp\", \"caption\": \"\", \"page\": 13, \"index\": 32, \"width\": 500, \"height\": 394}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-033.webp\", \"caption\": \"\", \"page\": 13, \"index\": 33, \"width\": 551, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-034.webp\", \"caption\": \"\", \"page\": 13, \"index\": 34, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-035.webp\", \"caption\": \"\", \"page\": 13, \"index\": 35, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-036.webp\", \"caption\": \"\", \"page\": 13, \"index\": 36, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-037.webp\", \"caption\": \"\", \"page\": 13, \"index\": 37, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-038.webp\", \"caption\": \"\", \"page\": 13, \"index\": 38, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-039.webp\", \"caption\": \"\", \"page\": 13, \"index\": 39, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-040.webp\", \"caption\": \"\", \"page\": 13, \"index\": 40, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-041.webp\", \"caption\": \"\", \"page\": 13, \"index\": 41, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-042.webp\", \"caption\": \"\", \"page\": 13, \"index\": 42, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-043.webp\", \"caption\": \"\", \"page\": 13, \"index\": 43, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-044.webp\", \"caption\": \"\", \"page\": 13, \"index\": 44, \"width\": 551, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-045.webp\", \"caption\": \"\", \"page\": 13, \"index\": 45, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-046.webp\", \"caption\": \"\", \"page\": 13, \"index\": 46, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-047.webp\", \"caption\": \"\", \"page\": 13, \"index\": 47, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-048.webp\", \"caption\": \"\", \"page\": 13, \"index\": 48, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-049.webp\", \"caption\": \"\", \"page\": 13, \"index\": 49, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-050.webp\", \"caption\": \"\", \"page\": 13, \"index\": 50, \"width\": 499, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-051.webp\", \"caption\": \"\", \"page\": 13, \"index\": 51, \"width\": 551, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-052.webp\", \"caption\": \"\", \"page\": 13, \"index\": 52, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-053.webp\", \"caption\": \"\", \"page\": 13, \"index\": 53, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-054.webp\", \"caption\": \"\", \"page\": 13, \"index\": 54, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-055.webp\", \"caption\": \"\", \"page\": 13, \"index\": 55, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-056.webp\", \"caption\": \"\", \"page\": 13, \"index\": 56, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-057.webp\", \"caption\": \"\", \"page\": 13, \"index\": 57, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-058.webp\", \"caption\": \"\", \"page\": 13, \"index\": 58, \"width\": 523, \"height\": 395}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-059.webp\", \"caption\": \"\", \"page\": 13, \"index\": 59, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-060.webp\", \"caption\": \"\", \"page\": 13, \"index\": 60, \"width\": 551, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-061.webp\", \"caption\": \"\", \"page\": 13, \"index\": 61, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-062.webp\", \"caption\": \"\", \"page\": 13, \"index\": 62, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-063.webp\", \"caption\": \"\", \"page\": 13, \"index\": 63, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-064.webp\", \"caption\": \"\", \"page\": 13, \"index\": 64, \"width\": 521, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-065.webp\", \"caption\": \"\", \"page\": 13, \"index\": 65, \"width\": 470, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-066.webp\", \"caption\": \"\", \"page\": 13, \"index\": 66, \"width\": 470, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-067.webp\", \"caption\": \"\", \"page\": 13, \"index\": 67, \"width\": 470, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-068.webp\", \"caption\": \"\", \"page\": 13, \"index\": 68, \"width\": 470, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-069.webp\", \"caption\": \"\", \"page\": 13, \"index\": 69, \"width\": 470, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-070.webp\", \"caption\": \"\", \"page\": 13, \"index\": 70, \"width\": 470, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-071.webp\", \"caption\": \"\", \"page\": 13, \"index\": 71, \"width\": 524, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-072.webp\", \"caption\": \"\", \"page\": 13, \"index\": 72, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-073.webp\", \"caption\": \"\", \"page\": 13, \"index\": 73, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-074.webp\", \"caption\": \"\", \"page\": 13, \"index\": 74, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-075.webp\", \"caption\": \"\", \"page\": 13, \"index\": 75, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-076.webp\", \"caption\": \"\", \"page\": 13, \"index\": 76, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-077.webp\", \"caption\": \"\", \"page\": 13, \"index\": 77, \"width\": 524, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-078.webp\", \"caption\": \"\", \"page\": 13, \"index\": 78, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-079.webp\", \"caption\": \"\", \"page\": 13, \"index\": 79, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-080.webp\", \"caption\": \"\", \"page\": 13, \"index\": 80, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-081.webp\", \"caption\": \"\", \"page\": 13, \"index\": 81, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-082.webp\", \"caption\": \"\", \"page\": 13, \"index\": 82, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-083.webp\", \"caption\": \"\", \"page\": 13, \"index\": 83, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-084.webp\", \"caption\": \"\", \"page\": 13, \"index\": 84, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-085.webp\", \"caption\": \"\", \"page\": 13, \"index\": 85, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-086.webp\", \"caption\": \"\", \"page\": 13, \"index\": 86, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-087.webp\", \"caption\": \"\", \"page\": 13, \"index\": 87, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-088.webp\", \"caption\": \"\", \"page\": 13, \"index\": 88, \"width\": 524, \"height\": 395}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-089.webp\", \"caption\": \"\", \"page\": 13, \"index\": 89, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-090.webp\", \"caption\": \"\", \"page\": 13, \"index\": 90, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-091.webp\", \"caption\": \"\", \"page\": 13, \"index\": 91, \"width\": 314, \"height\": 393}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-874fe45fac1c2b06ef36ecb2/fig-092.webp\", \"caption\": \"\", \"page\": 13, \"index\": 92, \"width\": 524, \"height\": 393}]"
motivation: 真实场景视觉感知需同时处理低级图像退化与高级语义理解，而复原与分割目标存在冲突。
method: 提出嵌套展开网络NUN，将抗退化展开网络嵌入分割导向展开网络的每一阶段协同优化。
result: 在隐藏物体分割任务上兼顾细粒度纹理恢复与语义对比，提升真实退化下的分割效果。
conclusion: 为退化图像上的分割问题提供了可分离又受控交互的统一框架。
---

## Abstract
Real-world visual perception demands joint handling of low-level image degradation and high-level semantic understanding, yet thesetwo objectives inherently conflict: restoration seeks fine-grained texturerecovery while segmentation prioritizes semantic contrast. We proposethe nested unfolding network (NUN), a principled framework that re-solves this conflict by nesting one deep unfolding network (DUN) in-side another. NUN embeds a degradation-resistant unfolding network(DeRUN) within each stage of a segmentation-oriented unfolding network(SODUN), enabling both tasks to optimize in their own subspaces whileinteracting in a controlled manner. DeRUN handles unknown degrada-tion through proximal gradient unfolding with learnable operators thatimplicitly approximate it, while SODUN performs reversible foreground-background estimation. A bi-directional unfolding interaction mechanismuses IQA to select optimal DeRUN outputs, and a cross-stage consis-tency loss ensures robust predictions under varying restoration quality.Theoretically, under local assumptions, we show that NUN reduces di-rect parameter-level gradient conflict through disjoint parameter setsand achieves a degradation-sensitivity bound, where degradation affectssegmentation only through the inner-loop optimization and restorationapproximation errors. We instantiate NUN on concealed object segmen-tation and demonstrate consistent superiority over SOTA alternativesacross 12 benchmarks. The code is available at https://github.com/ChunmingHe/NUN.

---

## 论文详细总结（自动生成）

# NUN：面向真实世界隐藏物体分割的嵌套展开网络 — 论文总结

## 1. 核心问题与整体含义

- **背景动机**：真实世界视觉感知需要同时应对**低层图像退化**（低光、雾、低分辨率等）与**高层语义理解**。在隐藏物体分割（Concealed Object Segmentation, COS）中，目标本身与背景高度融合、判别线索本就微弱，退化会进一步遮蔽这些线索，使分割难度显著上升。
- **核心矛盾**：将图像复原（restoration）与分割（segmentation）结合时存在**内在优化冲突**——复原追求细粒度纹理保真，分割强调高层语义对比。
- **已有方案的局限**：
  - **两阶段管线**（先复原再分割）：能部分隔离退化，但丧失任务间反馈，复原无法利用分割线索。
  - **耦合展开方法**（如 RUN）：两任务在共享优化阶段中交错，但**共享参数导致梯度冲突**，两任务更新都受损；且依赖预定义退化类型，泛化受限。
- **论文主张**：需要一种"原则性架构"，让复原与分割**在各自子空间中优化**，同时进行**受控的相互精化**。为此提出**嵌套展开网络 NUN（Nested Unfolding Network）**，采用 **DUN-in-DUN** 结构：将抗退化展开网络（DeRUN）嵌入到分割导向展开网络（SODUN）的每一个阶段中。

---

## 2. 方法论

### 2.1 核心思想
- 基于两个洞察：(1) 深度展开（DUN）提供可解释的迭代优化与天然的多阶段稳定性；(2) 嵌套结构天然为两任务创建**分离的优化回路**，同时共享的多阶段推进实现结构化信息交换。
- 整体可解释为**双层优化（BLO）**：外层优化分割（在复原图像上），内层优化复原（以分割变量为条件）。

### 2.2 关键技术细节

**（a）SODUN —— 分割导向展开网络**
- 从分割模型出发：将干净图像 X 分解为前景 F 与背景 B，优化 `L(F,B) = ½‖X−F−B‖² + βφ(F) + λϕ(B)`；代入 F = X⊙M 得到掩码形式。
- 用近端梯度（PG）算法交替优化 M 与 B：
  - **掩码梯度步**：`M̂k = Mk−1 − αM(Y⊙(Y⊙Mk−1 + Bk−1 − Y))`；借助 DeRUN 时，用增强结果 `Xk−1` 替换低质输入 `Y`。
  - **掩码近端步**：采用 **VSS（Visual State Space）模块**捕捉非局部依赖，并拼接 ResNet50 深度特征 `E(·)`；同时使用复原图与原图以缓解复原偏差。
  - **背景估计**：`B̂k = Bk−1 − αB(Bk−1 + Xk−1⊙Mk − Xk−1)`，近端项用三层 U 型网络。
- 通过**在掩码域与 RGB 域可逆地估计前景/背景**，迫使模型关注模糊边界区域，抑制假阳/假阴。

**（b）DeRUN —— 抗退化展开网络**
- 退化过程建模为 `Y = DX + N`，D 未知。复原目标 `L(X) = ½‖Y−DX‖² + γω(X)`。
- 用**可学习残差卷积算子** `RC_D` 与 `RC_D^T`（共享结构）隐式近似 D 与 Dᵀ：
  - `RC_D(X) = σk,n ⊙ (CRC(X) + X) + μk,n`，其中 CRC 为 Conv-ReLU-Conv 块。
  - `{σ, μ}` 可**直接由网络学习**（隐式盲退化建模，无需外部先验）；也可选**条件化于退化描述子 dk,n**，默认由冻结的 **DA-CLIP** 提供：`σ = conv3(li(dk,n))`，`μ = conv3(li(dk,n))`。
- **梯度更新**：`X̂k,n = Xk,n−1 − αX · RC_D^T(RC_D(Xk,n−1) − Xk−1)`，可解释为渐进去除残余退化。
- **近端更新**：`Xk,n = X1(X̂k,n) + X2(Bk, Mk, Y)`，其中 X2 引入**分割线索**，让复原网络优先处理分割不确定的模糊区域，形成天然协同。

**（c）BUI —— 双向展开交互机制**
- **IQA 选择**：对中间输出 {Xk−1,n} 用综合 IQA（TOPIQ + Q-Align + MUSIQ）打分 `S(X) = IQA(X)`，选最高质量者 `X^{T1}` 回填到后续 SODUN 与 DeRUN 更新中。
- **跨阶段一致性损失 Lcsc**：约束最优（T1）与次优（T2）输入下的预测一致，提升对复原质量波动的鲁棒性。
- **抗误差传播**：IQA 过滤低质复原 + CSC 损失消除伪影，缓解早期掩码错误误导复原的风险。

**（d）理论分析**
- **梯度冲突**：耦合方法在共享参数 θ 上优化 `L = Lseg + Lres`，当 `cos(∇Lseg, ∇Lres) < 0` 时交叉项 `2⟨∇Lseg, ∇Lres⟩` 削弱有效梯度范数；NUN 的 DeRUN 参数 θres 与 SODUN 参数 θseg **互不相交**，各自获得无妥协的参数级梯度（仅通过功能输出 X^{T1} 与 M 存在受控耦合）。
- **定理 1（内循环收敛）**：在 Lres 局部 Lr-光滑、μ-强凸，且步长 αX ≤ 1/Lr 时，DeRUN **线性收敛**：`‖Xk,N − X*k‖ ≤ (1 − μ/Lr)^{N/2} ‖Xk,0 − X*k‖`。
- **定理 2（退化敏感性界）**：在 Lseg 对 X 为 L0-Lipschitz 假设下，`|Lseg(Mk,Bk; X^{T1}) − Lseg(Mk,Bk; X)| ≤ L0(δk + δres)`，其中 δk 为优化误差（随 N 指数衰减），δres 为不可约复原误差。即**退化只通过内循环优化误差与复原近似误差影响分割**。

**（e）损失函数**
- 总损失 `Lt = Lbasic + ε·Lcsc`；`Lbasic` 联合监督分割精度与复原质量，含加权 BCE、加权 IoU 与 `‖Xk − X‖²`，并对第 k 阶段施加 `1/2^{K−k}` 的递增权重（鼓励迭代后期生成更高质量输出）。

---

## 3. 实验设计

### 3.1 数据集与场景（共 12 个 benchmark）

| 任务 | 数据集 | 规模/说明 |
|---|---|---|
| 伪装目标检测 COD（干净） | CHAMELEON / CAMO / COD10K / NC4K | 76 / 1250 / 5066 / 4121；训练用 1000 CAMO + 3040 COD10K |
| 息肉分割 PIS | CVC-ColonDB / ETIS | PVT-V2 backbone |
| 透明物体检测 TOD | GDD / GSD | 训练 2980 GDD + 3202 GSD |
| 隐藏缺陷检测 CDD | CDS2K | **零样本**，直接用 COD 训练模型测试 |
| 合成退化 COD | 上述 COD 数据集 | 低光（Retinex 策略）、雾（大气散射模型）、低分辨率（实用退化模型），各含 light/medium/heavy 三级 |
| 真实低质子集 | PCOD-LQ / MCOD-LQ | 四位标注者 ≥3 票共识筛选，共 160 张（90 + 70），含过曝、降雪等分布外退化 |

- 退化类型按场景匹配：息肉→低分辨率；室内透明物体→低光；室外透明物体→组合退化。

### 3.2 评价指标
- COD：MAE（M ↓）、自适应 F-measure（Fβ ↑）、E-measure（Eφ ↑）、结构度量（Sα ↑）
- PIS：mDice、mIoU、Sα；TOD：mIoU、Fmaxβ；CDD：8 项指标
- 复原质量：PSNR、FID、用户研究（12 名被试）

### 3.3 对比方法
- **COS 类**：FEDER、FSEL、RUN、BSA-Net、CamoDiff、VSCode、C3Net、EBLNet、RFENet、PolypPVT、MEGANet、HitNet
- **基础模型类**：RobustSAM、SAMadapter（SAM-ViT-H）
- **复原类**：DiffIR（用于复原质量对比）
- **Backbone 分组**：ResNet50、Res2Net50、PVT-V2、DINOv2-L，同组内保证 backbone、输入分辨率、训练计划一致。

### 3.4 消融实验
- 组件级消融（SODUN / DeRUN / BUI 逐项加入，Tab. 9）
- SODUN 内部设计（正则项、VSS vs CNN、U 型网络 vs Transformer、移除 Y，Tab. 10）
- DeRUN 内部设计（隐式 vs 显式先验、轻量网络 vs DiffIR、移除 X2 分割线索，Tab. 11）
- BUI 内部设计（单一 MUSIQ vs 综合 IQA、有无 Lcsc，Tab. 11）
- 退化先验配置（隐式学习 / VLM@stage1 / VLM@every iteration / 已知退化类型上界，Tab. 14）

---

## 4. 资源与算力

- **GPU**：2 张 NVIDIA RTX 4090。
- **优化器**：Adam，动量 (0.9, 0.999)。
- **训练配置**：输入分辨率 352×352，batch size 36，初始学习率 1×10⁻⁴，每 80 epoch 衰减 0.1 倍。
- **网络规模**：SODUN 阶段数 K = 4；嵌套 DeRUN 阶段数随 K 变化，N ∈ {4, 3, 3, 2}。
- **推理开销**：默认配置（VLM@stage1）38 ms，逐迭代 VLM 44 ms，隐式学习 30 ms，已知退化类型上界 22 ms。
- **未明确说明**：论文**未报告总训练时长、总 GPU 小时数或能耗**，仅给出硬件型号与超参数配置。

---

## 5. 实验数量与充分性

### 实验规模
- **主实验**：4 大 COS 任务 × 干净/退化两种设定，覆盖 12 个 benchmark，另加 2 个真实低质子集。
- **消融实验**：4 张消融表（Tab. 9–11、14），涵盖 3 大模块及多个子设计变体。
- **扩展实验**：与 3 种分割框架的集成验证、与基础模型
