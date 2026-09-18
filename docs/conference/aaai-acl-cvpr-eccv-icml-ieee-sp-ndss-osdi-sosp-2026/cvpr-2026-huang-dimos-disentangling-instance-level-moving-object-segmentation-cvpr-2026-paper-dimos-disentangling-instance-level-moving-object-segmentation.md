---
title: "DIMOS: Disentangling Instance-level Moving Object Segmentation"
title_zh: DIMOS：解耦实例级运动目标分割
authors: "Huang, Hongxiang, Ren, Hongwei, Lin, Xiaopeng, Huang, Yulong, Xie, Zeke, Cheng, Bojun"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Huang_DIMOS_Disentangling_Instance-level_Moving_Object_Segmentation_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 4.0
evidence: 事件与图像融合的实例级运动目标分割
tldr: 针对多模态运动实例分割中事件特征稀疏、且外观属性与运动线索纠缠导致小目标分割困难的问题，本文提出DIMOS方法，通过解耦事件与图像特征中的外观和运动信息，增强跨模态融合。实验表明该方法提升了对小型运动实例的分割精度，为交通监控与自动驾驶等场景的实例级运动分割提供了有效思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-huang-dimos-disentangling-instance-level-moving-object-segmentation-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 2962, \"height\": 1175}]"
motivation: 现有多模态运动实例分割方法受限于事件特征稀疏及外观与运动线索纠缠，难以分割小型运动实例。
method: 提出DIMOS，解耦事件与图像特征中的外观和运动信息，增强跨模态融合以提升实例级运动分割。
result: 在运动实例分割基准上改善了对小型运动目标的定位与分割精度。
conclusion: 表明解耦外观与运动线索有助于跨模态融合，推动运动实例分割应用。
---

## Abstract
Moving instance segmentation (MIS) attracts increasing attention due to its broad applications in traffic surveillance, autonomous driving, and animal tracking. Event cameras record asynchronous brightness changes, providing high temporal resolution and dynamic range, which makes them highly sensitive to motion information. By fusing event and image features, motion cues from events can complement spatial details from images, enhancing the performance of MIS. However, current multimodal MIS methods still struggle to segment small moving instances, as event cameras often yield sparse features under limited resolution. Moreover, event features entangle appearance attributes with motion cues, which further restricts effective cross-modal fusion. To address these challenges, we first propose a dual-disentangling feature extraction framework that separates and extracts appearance and motion information within both image and event modalities, thereby improving feature density. Subsequently, a multi-granularity cross-modal alignment is introduced to align distributionally and semantically consistent features across modalities, enabling more effective fusion with rich spatial and temporal details. The experiment results demonstrate that our method achieves state-of-the-art performance in multimodal MIS, especially for small instances under challenging conditions such as fast motion and low-light settings.

---

## 论文详细总结（自动生成）

# DIMOS：解耦实例级运动目标分割——论文中文总结

## 1. 核心问题与整体含义

- **研究任务**：实例级运动目标分割（Moving Instance Segmentation, MIS），要求不仅区分目标类别，还要分割每个独立运动实例并判断其运动状态，广泛应用于交通监控、自动驾驶、动物追踪等。
- **背景动机**：
  - 纯图像方法在低光照、逆光、高速运动、运动模糊等极端条件下性能受限。
  - 事件相机具有高时间分辨率、高动态范围、低延迟、低功耗等优势，适合捕捉运动信息，但空间分辨率低、事件流稀疏且异步，难以提供稠密空间上下文。
  - 现有多模态 MIS 通常遵循“图像提供外观、事件提供运动”的简化范式，导致小目标特征密度不足；同时事件特征中外观属性与运动线索高度纠缠，削弱跨模态融合效果。
- **整体含义**：论文提出 DIMOS，核心思想是在图像和事件两个模态内部同时解耦并提取外观与运动特征，再通过多粒度跨模态对齐增强融合，从而提升小实例、快速运动和低光场景下的分割性能。

## 2. 方法论

### 2.1 问题定义与输入表示
- 输入为图像帧 \(I_t\) 和同一时间区间的事件流 \(E_{[t,t+\Delta t]}\)。
- 输出为每个实例的掩码 \(\hat{m}_k\) 和二值运动标签 \(\hat{y}_k\)，即 \(\hat{M}=\{\hat{m}_k\}_{k=1}^K\)，\(\hat{Y}=\{\hat{y}_k\}_{k=1}^K\)。
- 事件被离散化为 \(B\) 个时间 bin，并累积为体素表示 \(V_t(x,y,b)\)，其中每个事件 \(e_i=(x_i,y_i,t_i,p_i)\) 按极性 \(p_i\) 和时间距离加权累加。
- 最终输入为 \(X=\{I_t,V_t\}\)，通过可学习映射 \(f_\phi(X)=(\hat{M},\hat{Y})\) 完成预测。

### 2.2 总体框架
DIMOS 包含四个主要组件：
- **双解耦模块**：在图像和事件模态内分别提取外观与运动特征。
- **跨模态对齐与融合模块**：多粒度对齐后进行跨模态融合。
- **跨类型交互模块**：通过 cross-attention 联合推理外观与运动线索。
- **任务特定解码模块**：分别处理外观相关任务和运动相关任务。

### 2.3 双解耦机制
-
