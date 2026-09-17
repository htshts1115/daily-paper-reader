---
title: "Iris: Bringing Real-World Priors into Diffusion Model for Monocular Depth Estimation"
title_zh: Iris：将真实世界先验引入扩散模型的单目深度估计
authors: "Cai, Xinhao, Pei, Gensheng, Sun, Zeren, Yao, Yazhou, Shen, Fumin, Wang, Wenguan"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Cai_Iris_Bringing_Real-World_Priors_into_Diffusion_Model_for_Monocular_Depth_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 融合真实先验的扩散模型单目深度估计
tldr: 传统前馈单目深度估计依赖海量数据却仍丢失细节，而扩散模型方法虽具生成先验却难以完成合成到真实的迁移。本文提出Iris确定性框架，将真实世界先验融入扩散模型，采用两阶段先验到几何的确定性调度，通过谱门控蒸馏迁移低频真实先验并保留高频细节。实验表明该方法能保持精细细节、强泛化到真实场景，且在有限训练数据下保持高效。该工作为单目深度估计提供了兼顾细节与泛化的新范式。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1466, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1466, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 932, \"height\": 624}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 932, \"height\": 624}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 4, \"index\": 10, \"width\": 479, \"height\": 319}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 4, \"index\": 11, \"width\": 479, \"height\": 319}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 2000, \"height\": 1337}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 2000, \"height\": 1337}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 2000, \"height\": 1338}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 2000, \"height\": 1345}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 7, \"index\": 21, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 1490, \"height\": 997}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 1490, \"height\": 997}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 7, \"index\": 26, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 7, \"index\": 27, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 7, \"index\": 28, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 7, \"index\": 29, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 7, \"index\": 30, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 7, \"index\": 31, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 7, \"index\": 32, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 7, \"index\": 33, \"width\": 1490, \"height\": 997}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 7, \"index\": 34, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 7, \"index\": 35, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 7, \"index\": 36, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 7, \"index\": 37, \"width\": 1490, \"height\": 998}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 7, \"index\": 38, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 7, \"index\": 39, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 7, \"index\": 40, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 7, \"index\": 41, \"width\": 1490, \"height\": 996}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 7, \"index\": 42, \"width\": 1490, \"height\": 997}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 7, \"index\": 43, \"width\": 1490, \"height\": 997}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 8, \"index\": 44, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 8, \"index\": 45, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 8, \"index\": 46, \"width\": 1465, \"height\": 977}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-cai-iris-bringing-real-world-priors-into-diffusion-model-for-monocular-depth-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 8, \"index\": 47, \"width\": 1465, \"height\": 977}]"
motivation: 前馈方法依赖海量数据仍缺失细节，扩散方法则难以完成合成到真实的域迁移。
method: 提出Iris确定性框架，采用两阶段先验到几何调度与谱门控蒸馏，将真实世界先验注入扩散模型。
result: 在保持精细细节的同时实现从合成到真实场景的强泛化，且训练数据需求少、效率高。
conclusion: 为兼顾细节与泛化的单目深度估计提供了新思路。
---

## Abstract
In this paper, we propose Iris, a deterministic framework for Monocular Depth Estimation (MDE) that integrates real-world priors into the diffusion model. Conventional feed-forward methods rely on massive training data, yet still miss details. Previous diffusion-based methods leverage rich generative priors yet struggle with synthetic-to-real domain transfer. Iris, in contrast, preserves fine details, generalizes strongly from synthetic to real scenes, and remains efficient with limited training data. To this end, we introduce a two-stage Priors-to-Geometry Deterministic (PGD) schedule: the prior stage uses Spectral-Gated Distillation (SGD) to transfer low-frequency real priors while leaving high-frequency details unconstrained, and the geometry stage applies Spectral-Gated Consistency (SGC) to enforce high-frequency fidelity while refining with synthetic ground truth. The two stages share weights and are executed with a high-to-low timestep schedule. Extensive experimental results confirm that Iris achieves significant improvements in MDE performance with strong in-the-wild generalization.

---

## 论文详细总结（自动生成）

# Iris：将真实世界先验引入扩散模型的单目深度估计——论文结构化总结

## 1. 核心问题与研究动机

- **任务背景**：单目深度估计（MDE）是三维重建、自动驾驶、条件图像生成等应用的基础任务，要求同时建模全局布局与局部几何。
- **核心瓶颈在于训练数据**：
  - 真实数据集监督不完美，深度图标注不准确、细节保留差；
  - 合成数据集标注完美，但规模有限，且与真实图像存在显著域差距。
- **现有方法的两难**：
  - 前馈式方法（如 Depth Anything V2）通过规模化数据（6200 万张图像）获得强泛化，但训练成本难以复现，且细节与边界精度仍不足；
  - 扩散模型方法（如 Marigold、Lotus）能借助 Stable Diffusion 的生成先验重建细节与边界，但整体精度不及 DAv2，且合成到真实的迁移能力弱。
- **核心研究问题**：在有限的标注数据与算力预算下，能否构建一个既保留细粒度细节、又具备强跨域泛化、并能与超大规模训练模型竞争的深度估计器？
- **整体含义**：Iris 将扩散范式改造为确定性的前馈架构，通过"先验到几何"的两阶段调度，把真实世界先验注入扩散模型，在不依赖海量标注的前提下兼顾细节保真与跨域泛化。

## 2. 方法论

### 2.1 核心思想

- 提出 **Priors-to-Geometry Deterministic（PGD）** 两阶段确定性框架，两阶段共享同一 U-Net 权重，仅以不同扩散时间步作为条件索引，去除多步采样与随机噪声注入。
- 关键洞察是 **频率-可靠性错配**：教师伪标签仅在低频（全局布局、物体范围）可靠，而扩散模型输出携带丰富高频（细节、边界）。单次训练中同时回归两类信号会造成梯度干扰，损害细节建模并引入教师特有伪影。

### 2.2 关键技术细节

- **阶段一：先验对齐（高时间步，低 SNR，t=1000）**
  - 预测器在高时间步下运行，条件化于 `t_high` 时倾向于全局布局与边界结构。
  - 使用冻结的真实图像教师（DAv2-Large）提供伪标签。
- **阶段二：几何精修（低时间步，高 SNR，t=500）**
  - 以阶段一输出为输入，在合成数据真值监督下精修，获得高频细节、度量标定与薄结构。
- **Spectral-Gated Distillation（SGD，谱门控蒸馏）**
  - 在潜在空间学习一个极轻量的可微低通门（仅 3 个参数：截止频率 κ、斜率 β、残差强度 s）。
  - 门控形式为 `G(z) = z + s·(iFFT(M⊙FFT(z)) − z)`，其中 `M(ω)=Sigmoid(β(κ−‖ω‖₂))`。
  - 学生只匹配教师伪标签的**低频谱**，转移域鲁棒的布局与尺度先验，高频分量有意不加约束，避免刻入教师伪影。
- **Spectral-Gated Consistency（SGC，谱门控一致性）**
  - 观察到阶段一虽只受低频对齐，却常产生更锐利的边界与纹理（低频监督减少了冲突高频信号，隐含促使边界更陡峭）。
  - 复用同一掩码取互补高频掩码，定义独立参数的高通门 `G_high`，用 stop-gradient 让阶段二在高频带对齐阶段一，并加辅助约束抑制阶段一高频过激活。
- **训练目标**
  - 总损失 `L = L_depth + γ·L_recon`，其中 `L_depth = ‖ŷ_geo − y‖² + α·L_sgd + β·L_sgc`。
  - 引入图像重建约束（在阶段二同时重建真实与合成图像）以缓解微调 Stable Diffusion 时的灾难性遗忘，保留文本到图像骨干的细粒度建模能力。
  - 推理时丢弃门控与教师分支，仅保留确定性前馈路径。

## 3. 实验设计

- **训练数据集**：
  - Hypersim（合成室内，约 39K，576×768）；
  - Virtual KITTI（合成室外，约 20K，352×1216）；
  - SA-1B（真实图像，仅取 100K，由 DAv2 生成伪标签，576×768）。
  - 每批次按固定概率采样：Hypersim 60%、VKITTI 10%、SA-1B 30%。
- **评估基准**：零样本仿射不变深度估计，覆盖 5 个真实数据集——NYUv2、ScanNet（室内）、KITTI（室外）、ETH3D、DIODE（多样场景）。
- **评价指标**：AbsRel（绝对平均相对误差，越低越好）、δ1（满足 max(a/d, d/a) < 1.25 的像素比例，越高越好）。
- **对比方法**（共 16 种）：
  - 判别式前馈方法：DiverseDepth、MiDaS、LeRes、Omnidata、DPT、HDN、DepthAnything、DepthAnything V2；
  - 扩散类方法：Diffusion-E2E-FT、GeoWizard、Marigold（含 LCM 变体）、Lotus-D、Lotus-G、GenPercept。
- **其他实验**：推理效率对比（表 2）、组件消融（表 3）、超参数消融（表 4）、定性对比（图 6）与消融可视化（图 7）。

## 4. 资源与算力

- **明确提及**：4 张 NVIDIA A100 40GB GPU，总 batch size 为 32；Adam 优化器，学习率 7.5×10⁻⁶；α=1、γ=1、β=0.1。
- **未明确说明**：具体训练时长（小时/天数）、总训练步数、单卡显存占用、训练总能耗等均未在文中给出，可复现成本需结合代码库进一步确认。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 1 组主实验：5 个数据集 × 16 种方法的零样本仿射不变对比；
  - 1 组推理效率对比（4 种方法）；
  - 1 组组件消融（7 种配置 a–g，覆盖随机/确定性、单阶段/两阶段、普通蒸馏/SGD、是否加 SGC）；
  - 1 组超参数消融（8 种 (α, β, γ) 组合）；
  - 多组定性可视化（跨场景对比、SGD/SGC 效果可视化）。
- **充分性评价**：
  - 消融设计较为系统，逐步验证了确定性化、两阶段解耦、SGD、SGC 各自的贡献，并专门验证了过激活约束的必要性；
  - 主实验覆盖室内、室外与多样场景，跨域泛化评估较全面；
  - 客观性方面，采用公开基准与统一评价指标，对比方法涵盖判别式与扩散式主流工作；
  - 公平性方面，Iris 训练数据量（59K 合成 + 100K 真实伪标签）远小于 DAv2（62.6M），对比中已注明数据规模差异，属于"数据效率"维度的对照，但并非同等数据量下的严格公平对比。

## 6. 主要结论与发现

- Iris 在所有 16 种方法中取得 **All Avg Ranking 与 Group Avg Ranking 双第一**；在扩散类方法中精度最佳。
- 在仅使用 59K 合成图像 + 100K 真实伪标签图像的条件下，性能可与使用 6200 万图像的 DAv2 系列竞争，并在多数数据集上领先，体现显著的数据效率优势。
- 推理效率优于 DAv2（1.3s vs 2.2s @1536²），远快于多步扩散方法 Marigold（377.7s）。
- 两阶段解耦有效缓解了低频真实先验与高频合成线索之间的梯度干扰；SGD 避免教师伪影植入，SGC 进一步将阶段一的锐利边界传递给阶段二；重建损失提升细节保留。
- 定性结果显示 Iris 在多样挑战场景中具有准确的度量尺度、丰富的细节与纹理，跨场景泛化稳定。

## 7. 优点

- **方法创新性**：把"频率-可靠性错配"这一观察转化为显式的频域门控机制，SGD 与 SGC 分别处理低频先验迁移与高频细节继承，思路清晰且相互呼应。
- **参数极轻**：低通/高通门各仅 3 个可学习参数，几乎不增加训练与推理开销。
- **架构高效**：确定性单步前馈，丢弃多步采样与文本条件，推理速度快，便于部署。
- **数据与算力友好**：在有限数据与 4 卡 A100 规模下即可复现，回应了 DAv2 训练规模难以复制的现实痛点。
- **实验设计亮点**：消融实验逐层剥离各组件贡献，且专门验证了"过激活约束"这一非平凡设计；同时报告了推理效率这一实用指标。
- **可扩展性**：文中指出该确定性扩散公式可将深度与表面法线统一于同一模型，具备多任务共享先验的潜力。

## 8. 不足与局限

- **教师依赖与偏差风险**：真实先验完全来自 DAv2 伪标签，教师自身的系统性偏差可能被继承；SA-1B 与部分评测集可能存在潜在内容重叠，影响泛化结论的纯度。
- **训练细节披露不足**：未报告训练时长、总步数、显存占用等，复现成本与能耗评估受限。
- **数据公平性**：与 DAv2 的对比是"小数据 vs 海量数据"的效率对照，而非同等数据规模下的严格控制实验；主表中也未提供同等数据量下重训基线的结果。
- **评测范围**：仅评估仿射不变深度，未涉及度量深度、视频时序一致性、极端天气/夜间等更困难场景；DIODE 等数据集上仍落后于 Lotus-D，说明并非全面占优。
- **消融覆盖有限**：超参数消融只覆盖 KITTI、ETH3D、ScanNet 三个数据集，未在全部五个基准上验证敏感性；对时间步选择（t=1000/500）未见系统扫描。
- **应用限制**：依赖 Stable Diffusion V2 骨干，模型体积与显存需求对边缘设备仍不友好；重建损失与门控机制增加了训练阶段的复杂度。

（完）
