---
title: "NVGS: Neural Visibility for Occlusion Culling in 3D Gaussian Splatting"
title_zh: NVGS：3D高斯泼溅中用于遮挡剔除的神经可见性
authors: "Zoomers, Brent, Hahlbohm, Florian, Vanherck, Joni, Jorissen, Lode, Magnor, Marcus, Michiels, Nick"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Zoomers_NVGS_Neural_Visibility_for_Occlusion_Culling_in_3D_Gaussian_Splatting_CVPR_2026_paper.pdf"
tags: ["query:cv-render"]
score: 4.0
evidence: 面向高效实时渲染的遮挡剔除
tldr: 3D高斯泼溅虽可用视锥剔除与细节层次加速渲染，但高斯半透明特性使遮挡剔除难以应用。本文提出NVGS，用小型共享MLP学习各高斯的视角相关可见性函数，在光栅化前查询并剔除被遮挡图元，并借助Tensor Core高效执行。实验表明该方法能有效减少渲染图元数量、加速渲染，为大规模场景实时渲染提供了可复用的遮挡剔除方案。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 3610, \"height\": 1194}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1632, \"height\": 545}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 900, \"height\": 596}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 3, \"index\": 4, \"width\": 2149, \"height\": 1064}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 5, \"index\": 5, \"width\": 4096, \"height\": 1767}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 3433, \"height\": 2007}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 8, \"index\": 7, \"width\": 2664, \"height\": 1164}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zoomers-nvgs-neural-visibility-for-occlusion-culling-in-3d-gaussian-splatting-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 8, \"index\": 8, \"width\": 3367, \"height\": 1352}]"
motivation: 高斯半透明特性使遮挡剔除难以用于3D高斯泼溅的渲染加速。
method: 用小型共享MLP学习视角相关可见性函数，在光栅化前剔除被遮挡图元。
result: 借助Tensor Core高效执行神经查询，减少图元并加速渲染。
conclusion: 为大规模实时渲染提供可复用的神经遮挡剔除方法。
---

## Abstract
3D Gaussian Splatting can exploit frustum culling and level-of-detail strategies to accelerate rendering of scenes containing a large number of primitives. However, the semi-transparent nature of Gaussians prevents the application of another highly effective technique: occlusion culling. We address this limitation by proposing a novel method to learn the viewpoint-dependent visibility function of all Gaussians in a trained model using a small, shared MLP across instances of an asset in a scene. By querying it for Gaussians within the viewing frustum prior to rasterization, our method can discard occluded primitives during rendering. Leveraging Tensor Cores for efficient computation, we integrate these neural queries directly into a novel instanced software rasterizer. Our approach outperforms the current state of the art for composed scenes in terms of VRAM usage and image quality, utilizing a combination of our instanced rasterizer and occlusion culling MLP, and exhibits complementary properties to existing LoD techniques. The source code is available at https://brent-zoomers.github.io/nvgs/

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：3D Gaussian Splatting（3DGS）已能高质量、快速地重建与渲染三维场景，并可通过视锥剔除（frustum culling）和细节层次（LoD）加速大规模场景渲染。
- **核心问题**：3DGS 使用半透明高斯图元，传统图形学中针对不透明三角形的**遮挡剔除（occlusion culling）**难以直接应用，因为高斯的可见性并非简单二值。
- **关键观察**：标准体积渲染中，一旦透射率（transmittance）饱和，后续高斯对最终颜色贡献极小，可被安全丢弃。这构成一种“软遮挡”，且会随距离增大而增强。
- **整体含义**：论文提出 NVGS，将视角相关的高斯可见性函数学习并烘焙进小型 MLP，在光栅化前剔除被遮挡高斯，并结合实例化光栅器，面向由多个 3DGS 资产组合而成的大规模场景，显著降低 VRAM 占用并提升渲染质量与速度。其目标应用包括游戏、影视等大规模组合场景实时渲染。

## 2. 方法论：核心思想、关键技术细节与流程

- **总体框架**：方法包含三部分：
  1. 从预训练 3DGS 资产中提取可见性监督数据；
  2. 将可见性蒸馏到轻量 MLP；
  3. 使用新型实例化、遮挡感知光栅器进行渲染。

- **可见性提取**：
  - 先移除极低不透明度高斯，并对资产中心化，简化训练与渲染。
  - 根据资产包围盒对角线投影屏幕尺寸，计算相机采样距离范围。近端取投影对角线覆盖 90%，远端取 5
