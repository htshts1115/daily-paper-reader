---
title: "PTC-Depth: Pose-Refined Monocular Depth Estimation with Temporal Consistency"
title_zh: PTC-Depth：具有时间一致性的位姿细化单目深度估计
authors: "Han, Leezy, Kim, Seunggyu, Shim, Dongseok, Lee, Hyeonbeom"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Han_PTC-Depth_Pose-Refined_Monocular_Depth_Estimation_with_Temporal_Consistency_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 一致性感知的单目深度估计框架
tldr: 单目深度估计已广泛用于自动驾驶与移动机器人，但连续帧间常缺乏时间一致性，导致抖动甚至突变失效。本文提出一致性感知框架，利用轮式里程计与光流三角化估计相机位姿和稀疏深度，并据此更新深度预测以保持稳定连贯。实验表明该方法提升了跨帧深度的时间一致性。该工作为动态场景下的稳定深度估计提供了方案。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 9219, \"height\": 2988}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 6495, \"height\": 2541}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 3991, \"height\": 1882}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 8575, \"height\": 2566}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 10092, \"height\": 3284}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 1892, \"height\": 592}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-han-ptc-depth-pose-refined-monocular-depth-estimation-with-temporal-consistency-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 2999, \"height\": 2076}]"
motivation: 现有单目深度估计在连续帧间缺乏时间一致性，导致抖动和深度突变失效。
method: 利用轮式里程计与光流三角化估计相机位姿和稀疏深度，更新并约束深度预测。
result: 在深度范围突变等场景下保持了稳定连贯的深度输出，减少抖动。
conclusion: 引入位姿与稀疏深度约束可有效提升单目深度的时间一致性。
---

## Abstract
Monocular depth estimation (MDE) has been widely adopted in the perception systems of autonomous vehicles and mobile robots. However, existing approaches often struggle to maintain temporal consistency in depth estimation across consecutive frames. This inconsistency not only causes jitter but can also lead to estimation failures when the depth range changes abruptly. To address these challenges, this paper proposes a consistency-aware monocular depth estimation framework that leverages wheel odometry from a mobile robot to achieve stable and coherent depth predictions over time. Specifically, we estimate camera pose and sparse depth from triangulation using optical flow between consecutive frames. The sparse depth estimates are used to update a recursive Bayesian estimate of the metric scale, which is then applied to rescale the relative depth predicted by a pre-trained depth estimation foundation model. The proposed method is evaluated on the KITTI, TartanAir, MS2, and our own dataset, demonstrating robust and accurate depth estimation performance.

---

## 论文详细总结（自动生成）

# PTC-Depth 论文中文总结

## 1. 核心问题与整体含义
- **研究动机**：单目深度估计（MDE）已广泛用于自动驾驶、移动机器人等感知系统，但现有方法在连续帧之间常缺乏时间一致性，表现为深度抖动；当深度范围突然变化时，甚至会出现估计失效。
- **背景矛盾**：
  - 视频深度方法通常输出相对深度，时间上较平滑，但缺少绝对度量尺度，难以直接用于自动驾驶、3D 建图等需要真实尺度的任务。
  - 深度补全方法可借助 LiDAR 等稀疏深度获得高质量度量深度，但依赖额外深度传感器，不适用于仅有相机与里程计的场景。
  - 深度基础模型零样本泛化强、边界保持好，但输出多为相对深度，且逐帧预测仍可能不一致。
- **整体含义**：论文提出 PTC-Depth，一种一致性感知的单目度量深度估计框架。其核心是利用移动机器人已有的轮式里程计提供轻量度量参考，将基础模型的相对深度递归重缩放为时间一致、跨域可用的度量深度，而无需额外深度传感器或针对数据集微调。

## 2. 方法论
- **核心思想**：不直接在深度空间融合三角化深度与相对深度，而是估计一个潜在尺度场 \(S\)，使 \(Z = S \cdot d_{\text{rel}}\) 恢复度量深度，并用递归贝叶斯更新维持时间一致性。
- **总体流程**：
  1. **光流与运动场建模**：基于 Longuet-Higgins–Prazdny 运动场公式，将连续帧光流表示为相机旋转、平移与相对深度、全局尺度因子的函数。
  2. **里程计约束平移尺度**：将平移写成 \(T = b \hat{T}\)，其中 \(b\) 为轮式里程计或 GPS 给出的基线，\(\hat{T}\) 为单位方向向量，从而把尺度恢复与外部度量信息关联。
  3. **鲁棒位姿估计**：使用 RANSAC 排除动态物体等外点，并按图像网格均匀采样光流，避免运动估计偏向小区域；再用 Huber 加权 IRLS 精化位姿。
  4. **三角化与 Sampson 残差**：根据估计的相对位姿，最小化两条视线射线残差，得到稀疏三角化度量深度；用 Sampson 残差作为逐像素几何可靠性分数。
  5. **时间先验传播**：将上一帧贝叶斯融合后的后验深度 \(Z^{\text{post}}_{i-1}\) 用估计位姿投影到当前帧，形成当前帧深度先验。
  6. **贝叶斯尺度融合**：
     - 先验尺度 \(S^{\text{prior}} = Z^{\text{prior}} / d_{\text{rel}}\)；
     - 观测尺度 \(S^{\text{obs}} = Z^{\text{tri}} / d_{\text{rel}}\)；
     - 根据 Sampson 残差构造观测方差，并根据帧级中位残差膨胀先验方差；
     - 用卡方检验检测不一致像素，对一致像素执行带一致性上限的 Kalman 更新；
     - 方差更新采用 Joseph 形式以保证数值稳定。
  7. **超像素尺度整合**：用 Felzenszwalb 分割将图像划分为超像素，在每个超像素内取后验尺度
