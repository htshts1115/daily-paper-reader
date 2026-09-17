---
title: Pixel-wise Planarity for High-Precision Monocular Plane Segmentation
title_zh: 面向高精度单目平面分割的逐像素平面性预测
authors: "Ahmetcan Yavuz, Alpay Ozkan, Rémi Pautrat, Shaohui Liu, Marc Pollefeys"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/12362.pdf"
tags: ["query:mono-depth"]
score: 5.0
evidence: 基于单目深度与法线骨干的平面分割
tldr: 单目平面分割受区域分组不精确与几何不一致监督影响，常出现过度分割与错误平面。本文提出逐像素平面性预测框架，基于预训练的单目几何骨干同时预测深度与表面法线，并引入平面性头估计每像素平面置信度，推理时用轻量区域生长结合三者形成几何一致的平面段。实验验证其鲁棒性。该工作间接依赖单目深度估计，属于相关几何任务而非深度估计本身。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-022.webp\", \"caption\": \"\", \"page\": 5, \"index\": 22, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-023.webp\", \"caption\": \"\", \"page\": 6, \"index\": 23, \"width\": 3008, \"height\": 872}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-024.webp\", \"caption\": \"\", \"page\": 10, \"index\": 24, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-025.webp\", \"caption\": \"\", \"page\": 10, \"index\": 25, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-026.webp\", \"caption\": \"\", \"page\": 10, \"index\": 26, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-027.webp\", \"caption\": \"\", \"page\": 10, \"index\": 27, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-028.webp\", \"caption\": \"\", \"page\": 10, \"index\": 28, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-029.webp\", \"caption\": \"\", \"page\": 10, \"index\": 29, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-030.webp\", \"caption\": \"\", \"page\": 10, \"index\": 30, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-031.webp\", \"caption\": \"\", \"page\": 10, \"index\": 31, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-032.webp\", \"caption\": \"\", \"page\": 10, \"index\": 32, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-033.webp\", \"caption\": \"\", \"page\": 10, \"index\": 33, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-034.webp\", \"caption\": \"\", \"page\": 10, \"index\": 34, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-035.webp\", \"caption\": \"\", \"page\": 10, \"index\": 35, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-036.webp\", \"caption\": \"\", \"page\": 10, \"index\": 36, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-037.webp\", \"caption\": \"\", \"page\": 10, \"index\": 37, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-038.webp\", \"caption\": \"\", \"page\": 10, \"index\": 38, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-039.webp\", \"caption\": \"\", \"page\": 10, \"index\": 39, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-040.webp\", \"caption\": \"\", \"page\": 10, \"index\": 40, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-041.webp\", \"caption\": \"\", \"page\": 10, \"index\": 41, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-042.webp\", \"caption\": \"\", \"page\": 10, \"index\": 42, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-043.webp\", \"caption\": \"\", \"page\": 10, \"index\": 43, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-044.webp\", \"caption\": \"\", \"page\": 10, \"index\": 44, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-045.webp\", \"caption\": \"\", \"page\": 10, \"index\": 45, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-046.webp\", \"caption\": \"\", \"page\": 10, \"index\": 46, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-047.webp\", \"caption\": \"\", \"page\": 10, \"index\": 47, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-048.webp\", \"caption\": \"\", \"page\": 10, \"index\": 48, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-049.webp\", \"caption\": \"\", \"page\": 10, \"index\": 49, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-050.webp\", \"caption\": \"\", \"page\": 10, \"index\": 50, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-051.webp\", \"caption\": \"\", \"page\": 10, \"index\": 51, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-052.webp\", \"caption\": \"\", \"page\": 10, \"index\": 52, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-053.webp\", \"caption\": \"\", \"page\": 10, \"index\": 53, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-054.webp\", \"caption\": \"\", \"page\": 14, \"index\": 54, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-055.webp\", \"caption\": \"\", \"page\": 14, \"index\": 55, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-056.webp\", \"caption\": \"\", \"page\": 14, \"index\": 56, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-057.webp\", \"caption\": \"\", \"page\": 14, \"index\": 57, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-058.webp\", \"caption\": \"\", \"page\": 14, \"index\": 58, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-059.webp\", \"caption\": \"\", \"page\": 14, \"index\": 59, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-060.webp\", \"caption\": \"\", \"page\": 14, \"index\": 60, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-061.webp\", \"caption\": \"\", \"page\": 14, \"index\": 61, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-062.webp\", \"caption\": \"\", \"page\": 14, \"index\": 62, \"width\": 644, \"height\": 476}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-063.webp\", \"caption\": \"\", \"page\": 15, \"index\": 63, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-064.webp\", \"caption\": \"\", \"page\": 15, \"index\": 64, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-065.webp\", \"caption\": \"\", \"page\": 15, \"index\": 65, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-066.webp\", \"caption\": \"\", \"page\": 15, \"index\": 66, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-067.webp\", \"caption\": \"\", \"page\": 15, \"index\": 67, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-068.webp\", \"caption\": \"\", \"page\": 15, \"index\": 68, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-069.webp\", \"caption\": \"\", \"page\": 15, \"index\": 69, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-070.webp\", \"caption\": \"\", \"page\": 15, \"index\": 70, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-071.webp\", \"caption\": \"\", \"page\": 15, \"index\": 71, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-072.webp\", \"caption\": \"\", \"page\": 15, \"index\": 72, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-073.webp\", \"caption\": \"\", \"page\": 15, \"index\": 73, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-074.webp\", \"caption\": \"\", \"page\": 15, \"index\": 74, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-075.webp\", \"caption\": \"\", \"page\": 15, \"index\": 75, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-076.webp\", \"caption\": \"\", \"page\": 15, \"index\": 76, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-077.webp\", \"caption\": \"\", \"page\": 15, \"index\": 77, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-078.webp\", \"caption\": \"\", \"page\": 15, \"index\": 78, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-079.webp\", \"caption\": \"\", \"page\": 15, \"index\": 79, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-080.webp\", \"caption\": \"\", \"page\": 15, \"index\": 80, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-081.webp\", \"caption\": \"\", \"page\": 15, \"index\": 81, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-082.webp\", \"caption\": \"\", \"page\": 15, \"index\": 82, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-083.webp\", \"caption\": \"\", \"page\": 15, \"index\": 83, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-084.webp\", \"caption\": \"\", \"page\": 15, \"index\": 84, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-085.webp\", \"caption\": \"\", \"page\": 15, \"index\": 85, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-086.webp\", \"caption\": \"\", \"page\": 15, \"index\": 86, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-3e5b184e9065d27afbbdc7e0/fig-087.webp\", \"caption\": \"\", \"page\": 15, \"index\": 87, \"width\": 640, \"height\": 480}]"
motivation: 单目平面分割因区域分组不精确与几何不一致的监督，常出现过分割与错误平面检测。
method: 提出逐像素平面性预测框架，基于预训练单目几何骨干预测深度与法线，并加入平面性头。
result: 推理时结合深度、法线与平面性进行轻量区域生长，形成几何一致的平面分割。
conclusion: 表明基于深度与法线先验的逐像素平面性可提升单目平面分割鲁棒性。
---

## Abstract
Plane segmentation from a single RGB image remains chal-lenging due to imprecise region grouping and geometrically inconsistentsupervision, often leading to over-segmentation and false planar detections.We propose instead a pixel-wise planarity prediction framework for ro-bust monocular plane segmentation. Building on a pretrained monoculargeometric backbone predicting depth and surface normals, we introducea dedicated planarity head that estimates per-pixel planarity confidence.During inference, predicted depth, normals, and planarity are combinedin a lightweight region-growing procedure that enforces geometric consis-tency when forming plane segments. We further analyze existing planeground-truth annotations and demonstrate substantial geometric incon-sistencies under strict distance thresholds. Across multiple datasets, ourmethod achieves improved geometric precision and segmentation qualitycompared to prior state-of-the-art approaches, while improving computa-tional efficiency.

---

## 论文详细总结（自动生成）

# 论文总结：Pixel-wise Planarity for High-Precision Monocular Plane Segmentation

## 1. 核心问题与整体含义

- **研究背景**：平面结构（墙面、地板、天花板、道路、建筑立面）普遍存在于人造环境中，精确的单目平面分割对 SLAM、几何感知重建、房间布局估计、Gaussian Splatting 等下游任务至关重要。
- **核心问题**：现有单目平面分割方法（如基于实例检测器或 Transformer 架构直接预测平面掩码与参数）虽在基准上表现良好，但仍存在**边界不准确**与**假阳性检测**问题，尤其是对"平滑但非平面"的区域（如曲面）易误判为平面。
- **根本原因**：
  - 平面性（planarity）本身很少被显式建模为稠密信号，分割质量高度依赖真值（GT）的几何质量。
  - 现有 GT 多通过几何拟合程序生成，在严格距离阈值下存在显著几何不一致，导致模型训练时被误导，产生过分割与错误平面。
- **整体意义**：论文主张将"几何一致性建模"与"实例级分组"解耦，通过显式逐像素平面性预测 + 几何约束区域生长，实现高精度、可泛化、计算高效的单目平面分割。

## 2. 方法论

### 2.1 核心思想

- 在预训练单目几何骨干（MoGeV2，预测深度、表面法线、3D 点图）之上，附加一个**轻量逐像素平面性预测头**，并在推理阶段将其与深度、法线联合用于**几何驱动的区域生长**，形成平面段后再用最小二乘拟合平面参数。
- 同时提出**新的几何一致 GT 生成流程**，修正现有标注的几何不一致问题。

### 2.2 关键技术细节

**(a) 真值几何一致性重审**

- 将像素 $(u,v)$ 结合深度 $d$ 反投影为 3D 点：$\mathbf{P} = d \cdot \mathbf{K}^{-1}[u,v,1]^\top$，其中 $\mathbf{K}$ 为相机内参。
- 定义点到平面 $(n,c)$ 的内点判定：$|n^\top P - c| < \tau$。
- 平面段内点比率：$\rho(\mathcal{S},\tau) = \frac{1}{|\mathcal{S}|}\sum_{i\in\mathcal{S}} \mathbbm{1}[|n^\top P_i - c| < \tau]$。
- 新 GT 生成：从 GT mesh 或深度出发，结合语义分割，在 3D 中渐进生长平面，严格约束距离误差与法线角度误差的内点比例，并限制"一个平面只能属于一个语义标签"，过滤非平面物体（实现细节见补充材料）。

**(b) 平面性头（Planarity Head）**

- 骨干与原始预测头完全**冻结**，仅训练平面性头（4.7M 参数）。
- 架构镜像法线预测头，仅改为单输出通道 + Sigmoid 激活；额外延迟约 10%。
- 用**法线头预训练权重初始化**（因平面性由法线场局部变化决定，法线头特征已编码该结构；非强制，仅加速收敛）。
- 监督信号：由 GT 平面标注派生的二值平面性图（属于任一平面实例为 1，否则为 0），损失为二值交叉熵：
  $\mathcal{L} = -\frac{1}{N}\sum_i [y_i \log \hat{y}_i + (1-y_i)\log(1-\hat{y}_i)]$。

**(c) 几何驱动区域生长**

- 推理时，平面性置信度超过阈值 $\tau_p$ 的像素视为平面候选。
- 对每个候选像素，在 $5\times5$ 邻域内联合检验三个条件：
  1. 邻居也是平面候选（超过 $\tau_p$）；
  2. 邻居位于法线场平滑区域（Sobel 法线梯度幅值 $< \sqrt{2-2\cos\theta}$）；
  3. 深度差在相对容差内（$|d_c - d_n| < \tau_{rel}\cdot d_c$，尺度自适应）。
- 若某像素至少 $T$ 个邻居（共 24 个）满足全部条件，则标记为连接。
- 对连接图做连通组件得到最终平面段；**所有邻域并行一次评估**，无需迭代 BFS/DFS，便于 GPU 高效执行。
- 刻意**避免由深度微分计算法线**（深度导数放大噪声、在缺失值和边界处不稳定、造成法线与深度误差相关耦合）。
- 平面参数恢复：对每段 3D 点用 SVD 求解 $\hat{n},\hat{d} = \arg\min \sum_i (n^\top P_i - d)^2$，约束 $\|n\|=1$。

### 2.3 实现细节

- 训练配置：AdamW，学习率 $1\times10^{-4}$，权重衰减 $1\times10^{-5}$，batch size 4，分辨率 $476\times644$，2 epochs，12 小时，1 张 NVIDIA RTX 3090。
- 区域生长阈值：$\tau_p=0.3$，$\theta=5^\circ$，$\tau_{rel}=0.025$，$T=8$。

## 3. 实验设计

### 3.1 数据集与场景

| 数据集 | 类型 | 用途 |
|---|---|---|
| ScanNet++ | 室内真实 | 训练/验证/测试 |
| Hypersim | 室内合成 | 训练/验证/测试 |
| Virtual KITTI 2 | 室外合成 | 训练/验证/测试 |
| SYNTHIA | 室外合成 | 训练/验证/测试 |

- 表 1 给出各数据集场景数与帧数的训练/验证/测试划分（如 ScanNet++：180/12/42 场景）。

### 3.2 评估基准与指标

- **3D 平面指标**：在误差阈值 $\tau$ 下计算精度与召回率；室内阈值 $\{1,5,10\}$ mm，室外 $\{2,5,10\}$ cm；设置内点比率门限 $\rho=0.9$；RANSAC 拟合阈值等于评估阈值以保证一致性。
- **2D 分割指标**：Rand Index（RI，越高越好）、Variation of Information（VOI，越低越好）、Segmentation Covering（SC，越高越好），遵循 PlaneNet 协议。
- 统一输入分辨率与评估协议。

### 3.3 对比方法

- PlaneRCNN、PlaneTR、PlanarRecon、PlaneRecTR、Zeroplane（使用官方模型 + DUSt3R 骨干）。
- MonoPlane 官方实现未公开，用 Sequential-RANSAC 近似其几何拟合阶段。
- 额外重训练 Zeroplane（相同 DINOv2 骨干、相同初始权重、相同 GT、其原训练方法）以隔离"更强先验"与"本文分组框架"的贡献。

## 4. 资源与算力

- **明确提及**：训练在 **1 张 NVIDIA RTX 3090** 上进行，共 **12 小时**，**2 epochs**，分辨率 $476\times644$，batch size 4。
- 效率对比实验：在**同一张 RTX 3090** 上以 FP16 精度对 ScanNet++ 的 1000 张图像（统一缩放至 $480\times640$）测量参数量与 FPS。
- 论文**未提及**多卡训练、总 GPU 时或更大规模算力投入，也未说明推理阶段的具体显存占用。

## 5. 实验数量与充分性

- **主要实验组数**（约 8–10 组）：
  1. 表 2：GT 几何一致性分析（PlaneRCNN GT vs. 新 GT，ScanNet / ScanNet++，多阈值）。
  2. 表 3：室内平面分割（ScanNet++、Hypersim，多阈值 + 2D 指标）。
  3. 表 4：室外平面分割（SYNTHIA、VKITTI2）。
  4. 表 5：区域生长线索消融（N / N+D / N+D+P）。
  5. 表 6：效率对比（参数量 + FPS）。
  6. 表 7：几何骨干影响（Metric3D V2、Depth Anything V2、MoGeV2 交叉组合）。
  7. 表 8：与重训练 Transformer 基线（Zeroplane†）对比。
  8. 表 9：跨域泛化（室内训练 → 室外测试）。
  9. 图 4、图 6：定性对比与内点/外点可视化。
  10. 图 5：in-the-wild 互联网图像泛化。
  11. 补充材料：平面性头损失函数（BCE、focal、DICE 及组合）与区域生长阈值敏感性。
- **充分性与公平性评估**：
  - **充分**：覆盖室内/室外、真实/合成、多阈值、2D+3D 双指标、跨域与 in-the-wild 场景，消融维度较全面。
  - **客观公平**：统一输入分辨率与评估协议；RANSAC 拟合阈值与评估阈值一致；对 Zeroplane 使用官方模型；重训练基线共享骨干与初始权重，控制变量较严格。
  - **潜在偏差**：MonoPlane 因官方代码未公开而用 Sequential-RANSAC 近似，可能不完全代表其真实性能；补充材料内容未在正文详述，部分结论无法独立核验。

## 6. 主要结论与发现

- 现有平面 GT 在严格距离阈值下存在**显著几何不一致**（如 PlaneRCNN GT 在 ScanNet 上 @0.1cm 精度为 0.0，@0.5cm 仅 6.7；ScanNet++ 上 @0.1cm 为 50.7），新 GT 将 ScanNet++ @0.1cm 精度提升至 60.2。
- 显式逐像素平面性建模是必要的：仅靠深度与法线的平滑性无法区分"平滑曲面"与"真平面"。
- 在所有数据集与阈值上，本方法**精度均优于所有对比方法**，在严格阈值下提升尤为显著；召回与 2D 分割指标保持竞争力。
- 消融显示：深度单独几乎无效（@0.1cm 精度 0.6），法线是主要分组信号（43.0），加入相对深度提升至 45.5，加入平面性后大幅提升至 62.1（SC 从 0.59 升至 0.66）。
- 效率上，本方法（335.6M 参数，13.3 FPS）比多数基线更轻更快。
- 骨干可替换（Metric3D V2、Depth Anything V2 均可工作），但同一 MoGeV2 骨干提供深度、法线、平面性时几何最一致、效果最佳。
- 重训练 Zeroplane 即便使用相同先验与域内数据，严格阈值精度仍远低于本方法，说明**仅提升骨干不足**，显式平面性与几何约束分组才是关键。
- 跨域泛化（室内训练 → 室外测试）与 in-the-wild 图像上均保持较高精度与稳定分组，避免过度假阳性。

## 7. 优点

- **问题洞察新颖**：首次系统量化并揭示现有平面 GT 的几何不一致性，并据此提出新的几何一致 GT 生成流程。
- **方法轻量模块化**：仅训练 4.7M 参数的平面性头，骨干冻结，可无缝集成到其他单目深度/法线预测器，额外延迟约 10%。
- **算法效率高**：区域生长采用并行单次邻域评估 + 连通组件，避免迭代 BFS/DFS，适合 GPU 加速；整体 FPS 优于多数基线。
- **设计决策有依据**：明确论证为何不用深度微分求法线（噪声放大、边界不稳定、误差耦合），以及为何用相对深度容差（尺度鲁棒）。
- **实验严谨**：多数据集、多阈值、2D+3D 双指标体系；控制变量地重训练基线；跨域与 in-the-wild 验证

（接上文）等，验证了方法的鲁棒性与泛化能力。

- **可解释性与可控性强**：平面性阈值、法线角度阈值、相对深度容差、邻域连接数等超参数均有明确几何含义，便于按场景调节，且补充材料提供了敏感性分析。
- **对下游任务友好**：输出稠密平面段 + 精确平面参数，可直接服务于 SLAM、布局估计、Gaussian Splatting 等需要几何一致平面表示的任务。
- **对比公平透明**：主动重训练 Zeroplane 并共享骨干与初始权重，隔离"更强几何先验"与"分组框架"的贡献，避免了常见的不公平对比。

## 8. 局限性

- **依赖单目几何骨干质量**：平面性头建立在 MoGeV2 等骨干的深度与法线预测之上，骨干在弱纹理、镜面/透明表面、强透视或极端光照下的误差会直接传播到平面分割结果。
- **平面性监督依赖 GT 质量**：平面性头的训练标签由（新生成的）GT 平面实例派生，若 GT 本身在复杂场景（如薄结构、曲面过渡区）存在歧义，监督信号仍可能带偏。
- **曲面与平面边界判定**：论文指出平滑曲面易被误判为平面，虽通过显式平面性缓解，但对"近平面曲面"（如大曲率半径圆柱面）与真正平面的区分阈值仍依赖超参数，存在边界模糊地带。
- **区域生长的连通性假设**：基于 $5\times5$ 邻域的并行连接判据假设平面在图像空间局部连通，对于被遮挡、断裂或跨语义边界的同一平面，可能被切分为多个段，需要后续合并策略（论文未详述合并）。
- **实验范围**：主要在合成数据集（Hypersim、VKITTI2、SYNTHIA）与 ScanNet++ 上评估，真实室外大规模场景（如城市级 LiDAR 对齐数据）验证有限；in-the-wild 评估以定性为主。
- **MonoPlane 对比不完整**：因官方实现未公开，仅用 Sequential-RANSAC 近似其几何拟合阶段，可能低估或高估其真实性能，削弱了与该方法对比的结论强度。
- **训练数据与算力规模**：仅 2 epochs、单卡 12 小时，虽体现高效，但也意味着未探索更长训练或更大数据对性能上限的影响。

## 9. 启示与可迁移思路

- **"几何一致性"应作为一等公民**：论文最核心的启示是——在几何感知任务中，标注/真值的几何自洽性可能比模型架构更重要。这一思路可迁移到深度估计、法线估计、光流等任务的 GT 构建与评估。
- **解耦"逐像素属性预测"与"实例级分组"**：将稠密平面性预测（像素级）与区域生长（实例级）分离，避免了端到端实例分割模型对边界与假阳性的敏感性，这种"稠密信号 + 几何约束后处理"的范式可推广到其他结构化分割任务（如直线、柱面、对称结构检测）。
- **轻量适配器 + 冻结骨干**：仅训练 4.7M 参数的头、冻结强预训练骨干，是当前大模型时代低成本适配下游几何任务的有效范式，且用相关任务头（法线头）初始化可加速收敛。
- **避免误差耦合的设计哲学**：明确拒绝用深度微分求法线，改用法线头独立预测，避免深度噪声与法线误差相关耦合——这一"解耦误差源"的工程直觉值得在其他多信号融合任务中借鉴。
- **并行化几何后处理**：将迭代式区域生长改写为"单次并行邻域评估 + 连通组件"，是让传统几何算法适配 GPU 的通用技巧，可迁移到点云分割、超像素等。
- **公平对比的严谨态度**：主动重训练基线以控制变量，是论文写作与实验设计中值得学习的规范。

## 10. 总体评价

本文针对单目平面分割中"边界不准、假阳性多"的痛点，从**数据（GT 几何一致性）**与**方法（显式平面性 + 几何驱动分组）**两个层面同时入手，提出了一个轻量、模块化、可解释且高效的框架。其最大贡献不仅在于性能提升，更在于**系统性地揭示并量化了现有平面 GT 的几何不一致问题**，并给出可复现的修正流程，这对整个平面分割乃至更广泛的几何感知社区具有方法论价值。

方法设计上，逐像素平面性头与并行区域生长的组合兼顾了精度与效率，消融实验清晰证明了各几何线索（法线 > 相对深度 > 平面性）的递进贡献，且骨干可替换性验证了其通用性。实验在室内/室外、真实/合成、跨域、in-the-wild 多维度展开，指标覆盖 2D 与 3D，对比方法涵盖主流基线与重训练控制变量，整体严谨客观。

局限主要在于对骨干质量的依赖、曲面边界判定的模糊性以及真实室外大规模验证的不足，但这些并不影响其核心贡献的说服力。总体而言，这是一篇**问题洞察深刻、方法简洁有效、实验扎实**的几何感知工作，为后续单目平面分割与几何一致标注研究提供了有价值的参考范式。

（完）
