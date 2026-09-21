---
title: Real-Time Dynamic Scene Rendering with Controlled Compressibility and Contact Awareness
title_zh: 具有可控压缩性与接触感知的实时动态场景渲染
authors: "Shi, Boya, Guan, Naiyang, Yi, Xiaodong"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Real-Time_Dynamic_Scene_Rendering_with_Controlled_Compressibility_and_Contact_Awareness_CVPR_2026_paper.pdf"
tags: ["query:cv-render"]
score: 4.0
evidence: 实时动态渲染与遮挡边界处理
tldr: 现有动态场景渲染多假设刚体或方向受限运动，真实接触与运动常违反该假设，在遮挡边界产生伪影。本文提出源感知的统一动态渲染框架，通过Helmholtz分解、各向异性可压缩方向先验与仿射族等流形约束保证高斯基元一致性。大量基准实验显示其能有效减少接触与遮挡边界伪影，提升实时动态渲染的物理一致性与鲁棒性。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 7, \"index\": 1, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 7, \"index\": 2, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 7, \"index\": 3, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 7, \"index\": 10, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 7, \"index\": 12, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 7, \"index\": 13, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 7, \"index\": 14, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 7, \"index\": 15, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 7, \"index\": 16, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 7, \"index\": 17, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 7, \"index\": 18, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 7, \"index\": 19, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 960, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 8, \"index\": 21, \"width\": 690, \"height\": 518}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 690, \"height\": 518}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 8, \"index\": 23, \"width\": 690, \"height\": 518}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-real-time-dynamic-scene-rendering-with-controlled-compressibility-and-contact-awareness-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 691, \"height\": 518}]"
motivation: 动态场景渲染的刚性或方向受限假设被真实运动违反，遮挡边界易生伪影。
method: 提出源感知框架，以Helmholtz分解、各向异性先验与仿射族约束高斯基元一致性。
result: 在大量基准上减少接触与遮挡边界伪影，保持实时渲染性能。
conclusion: 提升实时动态渲染的物理一致性与鲁棒性。
---

## Abstract
Existing dynamic scene rendering methods often adopt rigid-body or direction-limited assumptions, yet real-world motion and contact routinely violate these, producing artifacts near occlusion boundaries. To address this, we introduce a unified, source-aware framework for dynamic rendering that enforces the consistency of Gaussian primitives under explicit manifold constraints. We project predicted velocities onto physically grounded priors via efficient, parallel inner solves: (i) a Helmholtz parameterization that separates divergence-free and potential-flow motion components; (ii) an anisotropic, compressible directional prior; and (iii) an affine family that disentangles rotation from isotropic scaling. Experiments on extensive benchmarks show consistent improvements over state-of-the-art methods in reconstruction fidelity and temporal coherence. Our approach ensures physically realistic rendering, especially near contacts, and substantially reduces motion-boundary artifacts.

---

## 论文详细总结（自动生成）

# 论文总结：Real-Time Dynamic Scene Rendering with Controlled Compressibility and Contact Awareness

## 1. 核心问题与整体含义
- **研究动机**：现有动态场景渲染方法多采用刚体、无源、体积保持或方向受限的运动假设，但真实世界中的压缩/膨胀、出现/消失、接触与摩擦经常违反这些假设。
- **核心问题**：在动态视角合成与重建中，若忽略可压缩性和接触约束，容易在遮挡边界、运动界面产生拉伸、拖影、穿透等伪影，导致物理不合理和时序不一致。
- **整体含义**：论文试图在 3D Gaussian Splatting / 动态神经渲染框架中引入源项感知的连续性约束和接触感知的物理先验，在保持实时渲染效率的同时，提升动态场景的物理一致性和重建质量。

## 2. 方法论
### 2.1 核心思想
- 将动态场景中的信号演化建模为**带源项的连续性方程**：  
  \(\partial_t \psi + u\cdot\nabla\psi + \psi\nabla\cdot u = q\)。  
  其中 \(u\) 为速度场，\(q\) 为源汇项：\(q>0\) 表示生成/出现，\(q<0\) 表示消失/耗散。
- 通过显式源项 \(q\)，把“运动导致的密度变化/压缩”与“真实外观出现或消失”区分开。
- 采用**投影式交替优化**：内层将预测速度投影到物理可行的先验流形上，外层用投影场监督可学习模型；内层保持线性、凸或小规模可高效求解。

### 2.2 关键参数化与约束
- **亥姆霍兹参数化**：将速度分解为无散度分量与势流分量：  
  \(u = u_\tau + P\nabla\Phi\)，其中 \(u_\tau\) 无散度，势流分量承担体积变化/压缩性。
- **各向异性可压缩方向先验**：将可压缩变化限制在预设子空间 \(E=\mathrm{span}(V)\) 内，通过投影 \(P=VV^\top\) 控制体积变化方向，并用 \(\lambda_{\text{comp}}\) 惩罚可压缩流。
- **仿射运动族**：  
  \(u(x,t)=\Omega x+E_0x+\kappa x+b\)。  
  其中 \(\Omega\) 为反对称旋转，\(E_0\) 为对称无迹剪切，\(\kappa\) 为各向同性缩放，\(b\) 为平移。该参数化解耦旋转、剪切、体积缩放和平移。
- **源项建模**：源汇场 \(q\) 用基函数展开，或采用比例衰减先验 \(q=\lambda_t\psi\)，以较少参数表达外观变化。
- **可辨识性处理**：引入全局质量预算、零均值规范、边界感知基和课程学习，逐步启用可压缩性与源项，避免发散与源项混淆。

### 2.3 接触与流
