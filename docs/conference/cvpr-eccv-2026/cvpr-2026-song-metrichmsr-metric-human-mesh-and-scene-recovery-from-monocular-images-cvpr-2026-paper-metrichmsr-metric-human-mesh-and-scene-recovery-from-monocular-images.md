---
title: "MetricHMSR: Metric Human Mesh and Scene Recovery from Monocular Images"
title_zh: MetricHMSR：从单目图像恢复度量人体网格与场景
authors: "Song, Chentao, Zhang, He, Yuan, Haolei, Lin, Haozhe, Tao, Jianhua, Zhang, Hongwen, Yu, Tao"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Song_MetricHMSR_Metric_Human_Mesh_and_Scene_Recovery_from_Monocular_Images_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 4.0
evidence: 从单目图像进行度量人体与场景三维恢复
tldr: 由于相机模型假设不现实及度量感知本身困难，已有方法难以用统一模块同时估计人体姿态与度量三维位置。本文提出MetricHMSR，通过引入相机射线编码边界框与透视投影内参，并采用人体混合专家模型将图像特征与射线特征动态路由到任务专家。实验表明该统一框架可同时实现度量人体网格与场景恢复。该工作为单目度量感知提供了统一思路，但与通用深度估计任务关联较间接。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 654, \"height\": 560}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 643, \"height\": 472}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 549, \"height\": 565}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 368, \"height\": 476}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 756, \"height\": 413}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1011, \"height\": 422}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 4, \"index\": 7, \"width\": 500, \"height\": 333}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 4, \"index\": 8, \"width\": 500, \"height\": 333}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 4, \"index\": 9, \"width\": 491, \"height\": 324}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 733, \"height\": 595}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 1305, \"height\": 1125}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 8, \"index\": 12, \"width\": 1920, \"height\": 1080}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 8, \"index\": 13, \"width\": 452, \"height\": 281}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 8, \"index\": 14, \"width\": 2169, \"height\": 1220}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 8, \"index\": 15, \"width\": 1884, \"height\": 1053}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 8, \"index\": 16, \"width\": 2169, \"height\": 1220}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 8, \"index\": 17, \"width\": 1650, \"height\": 928}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 8, \"index\": 18, \"width\": 486, \"height\": 459}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-song-metrichmsr-metric-human-mesh-and-scene-recovery-from-monocular-images-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 8, \"index\": 19, \"width\": 1920, \"height\": 1080}]"
motivation: 相机模型假设不现实且度量感知困难，已有方法难以统一估计人体姿态与度量三维位置。
method: 提出MetricHMSR，用相机射线编码边界框与内参，并以人体混合专家动态路由图像与射线特征。
result: 在统一框架内同时实现度量人体网格与场景恢复。
conclusion: 为单目度量感知提供统一思路，但与通用深度估计关联较间接。
---

## Abstract
We introduce MetricHMSR (Metric Human Mesh and Scene Recovery), a novel approach for metric human mesh and scene recovery from monocular images. Due to unrealistic assumptions in the camera model and inherent challenges in metric perception, existing approaches struggle to achieve human pose and metric 3D position estimation through a unified module.To address this limitation, MetricHMSR incorporates camera rays to comprehensively encode both the bounding box information and the intrinsic parameters of perspective projection. Then we proposed Human Mixture-of-Experts (MoE), the model dynamically routes image features and ray features to task-specific experts for specialized understanding of different data aspects, enabling a unified framework that simultaneously perceives the local pose and the global 3D position.Based on the results above, we further refine the existing monocular metric depth estimation method to achieve more accurate results, ultimately enabling the seamless overlay of humans and scenes in 3D space.Comprehensive experimental results demonstrate that the proposed method achieves state-of-the-art performance on both human mesh and scene recovery.

---

## 论文详细总结（自动生成）

# MetricHMSR 论文中文总结

## 1. 核心问题与整体含义
- **研究动机**：从单张单目图像同时恢复人体网格与3D场景，是计算机视觉与图形学的基础问题；但现有方法受单目尺度模糊、弱透视相机假设、相机模型不真实等限制，难以恢复**度量尺度**的人体形状与全局3D位置。
- **关键痛点**：
  - 相机内参、边界框信息与人体3D位置密切相关，但现有网络未能有效利用。
  - 图像裁剪与缩放破坏度量线索。
  - 局部姿态与全局平移特征高度耦合，常需多阶段流水线，导致误差累积。
  - 引入外部单目度量深度估计模块会限制整体性能。
- **整体含义**：论文提出统一框架 MetricHMSR，旨在从单目图像恢复**度量人体网格**（姿态、度量形状、全局位置）与**度量3D场景**，实现人体与场景在3D空间中的物理一致对齐，对物理AI、具身AI等范式有重要意义。

## 2. 方法论
- **核心思想**：
  - 提出 **MetricHMR** 恢复度量人体网格，再以人体网格为几何锚点，引导单目度量深度细化，形成 **MetricHMSR**。
  - 用**边界相机射线图**显式编码相机内参、边界框、裁剪与缩放信息。
  - 用 **HumanMoE** 动态路由图像与射线特征，解耦局部姿态与全局位置。
- **关键技术细节**：
  - **SMPL 参数化**：目标为恢复姿态参数 \(\theta \in \mathbb{R}^{72}\)、形状参数 \(\beta \in \mathbb{R}^{10}\)、全局平移 \(t_{global} \in \mathbb{R}^3\)。
  - **输入与编码**：裁剪图像与对应边界射线图分别由 ViTPose 和 ViT-Large-Patch16-224 编码，拼接后输入 HumanMoE；内参未知时用 AnyCalib 估计。
  - **边界射线图**：由原始内参 \(K\) 和裁剪框、缩放因子 \(s\) 计算变换后内参 \(K'\)，再按 \(d = K'^{-1}[u,v,1]\) 生成像素对齐相机射线；未知内参时用图像长边近似焦距、图像中心为主点。
  - **HumanMoE**：
    - 包含 **Patch MoE** 与 **Global MoE**，分别建模局部语义与全图上下文。
    - MoE 层采用软 MoE，含 4 个路由图像专家、1 个共享图像专家、1 个射线专家。
    - 路由为加权组合，并加入负载均衡损失 \(L_{aux} = \lambda K \sum_i p_i^2\)，防止专家使用坍缩。
  - **损失设计**：\(L = \lambda_{J2D}L_{J2D} + \lambda_{J3D}L_{J3D} + \lambda_{V3D}L_{V3D} + \lambda_\theta L_\theta + \lambda_\beta L_\beta + \lambda_h L_h\)，并采用过完备损失，如引入身高监督。
  - **人体引导度量深度细化**：
    - 以 MapAnything 预测深度 \(z_{in}(x)\) 为基础，用混合 UNet–ViT 预测逐像素仿射场 \((s(x), b(x))\)，得到 \(\hat{z}(x) = s(x)z_{in}(x) + b(x)\)。
    - 将人体网格投影为稀疏锚点 \(z_{hmr}(x)\) 与掩码 \(M_a(x)\)，施加锚点一致性损失。
    - 总损失：\(L = \lambda_d L_{depth} + \lambda_a L_{anchor} + \lambda_{tv} L_{tv} + \lambda_{var} L_{var}\)，正则化保持平滑并接近全局均值。

## 3. 实验设计
- **训练数据集**：MetricHMR 在 BEDLAM、AIC、COCO、MPII、3DPW 上训练；深度细化网络进一步在 PROX RGB-D 上训练。
- **评估基准与场景**：
  - 全局轨迹：EMDB-2（动态相机，预测外参/GT外参）、RICH（静态相机）。
  - 局部姿态：3DPW、EMDB-1。
  - 度量深度：PROX。
  - 额外构造 **Syn-Focal** 合成数据集评估焦距变化鲁棒性，并可视化根关节分布。
- **对比方法**：包括 SLAHMR、GVHMR、TRAM、PromptHMR-vid、GLAMR、COIN、TRACE、WHAM、Human3R、HMR2.0、PersPose、CameraHMR、PromptHMR、Metric3D、Unidepth、MapAnything 等，区分在线与离线范式。
- **评价指标**：
  - 人体：PVE、MPJPE、PA-MPJPE。
  - 全局运动：WA-MPJPE100、W-MPJPE100、RTE、ERVE。
  - 深度：AbsRel、MAE、\(\delta_1\)。
- **主要结果**：
  - 3DPW 上取得最佳 PA-MPJPE 33.6、MPJPE 53.0、PVE 62.7。
  - EMDB-2 动态相机预测外参下：WA-M 72.1、W-M 199.5、RTE 1.4、ERVE 10.6，与SOTA离线方法相当。
  -
