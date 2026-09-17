---
title: "Lite Any Stereo: Efficient Zero-Shot Stereo Matching"
title_zh: 轻量任意立体：高效零样本立体匹配
authors: "Jing, Junpeng, Luo, Weixun, Mao, Ye, Mikolajczyk, Krystian"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Jing_Lite_Any_Stereo_Efficient_Zero-Shot_Stereo_Matching_CVPR_2026_paper.pdf"
tags: ["query:stereo-depth"]
score: 8.0
evidence: 高效零样本双目深度估计
tldr: 现有立体匹配方法为追求精度往往显著增大模型规模，而轻量模型通常被认为缺乏零样本泛化能力。本文提出Lite Any Stereo双目深度估计框架，设计紧凑但表达力强的骨干网络与混合代价聚合模块，并采用百万级数据的三阶段训练策略缩小仿真到真实的差距。实验表明该超轻模型在多个基准上取得领先的零样本泛化性能。该工作证明高效模型同样可以实现强泛化，为移动端双目深度提供可行方案。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 659, \"height\": 499}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 945, \"height\": 477}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 906, \"height\": 610}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 787, \"height\": 237}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 787, \"height\": 237}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 4, \"index\": 6, \"width\": 787, \"height\": 237}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-jing-lite-any-stereo-efficient-zero-shot-stereo-matching-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 4, \"index\": 7, \"width\": 787, \"height\": 237}]"
motivation: 立体匹配领域一味追求精度导致模型体积激增，轻量模型被认为难以具备零样本泛化能力。
method: 提出紧凑骨干网络与混合代价聚合模块，并设计百万级数据的三阶段训练策略以弥合仿真到真实的差距。
result: 超轻量模型在多个基准上取得领先的零样本立体匹配精度，排名第一。
conclusion: 证明高效模型也能实现强泛化，为移动端双目深度估计提供可行方案。
---

## Abstract
Recent advances in stereo matching have focused on accuracy, often at the cost of significantly increased model size. Traditionally, the community has regarded efficient models as incapable of zero-shot ability due to their limited capacity. In this paper, we introduce Lite Any Stereo, a stereo depth estimation framework that achieves strong zero-shot generalization while remaining highly efficient. To this end, we design a compact yet expressive backbone to ensure scalability, along with a carefully crafted hybrid cost aggregation module. We further propose a three-stage training strategy on million-scale data to effectively bridge the sim-to-real gap. Together, these components demonstrate that an ultra-light model can deliver strong generalization, ranking 1st across four widely used real-world benchmarks. Remarkably, our model attains accuracy comparable to or exceeding state-of-the-art non-prior-based accurate methods while requiring less than 1% computational cost, setting a new standard for efficient stereo matching.

---

## 论文详细总结（自动生成）

# Lite Any Stereo 论文总结

## 1. 核心问题与整体含义
- **研究动机**：立体匹配近年主要追求精度，导致模型规模与计算量急剧增大；高效轻量模型通常被认为容量有限、难以具备零样本泛化能力。
- **背景矛盾**：已有基于单目深度先验的立体模型零样本能力强，但计算代价高；高效模型速度快，却往往依赖特定域微调，跨域泛化差距明显。
- **整体含义**：论文提出 **Lite Any Stereo**，试图证明“超轻量模型也能实现强零样本泛化”，并在多个真实基准上达到领先水平，同时计算量低于准确型模型 1% 以下。

## 2. 方法论
- **总体框架**：特征提取 → 相关性/cost volume 构建 → 混合代价聚合 → 视差估计。
- **紧凑骨干网络**：
  - 采用 MobileNetV2 作为骨干，ImageNet 预训练，不引入 DepthAnything 等外部深度先验，以降低开销。
  - 左右图像共享权重，提取多尺度特征，并统一上采样到 1/4 分辨率。
- **相关性/cost volume**：
  - 在 1/4 分辨率上，对左右特征做内积构建 cost volume，视差范围为 `[0, Dmax/4]`。
- **混合代价聚合模块**：
  - 核心为 `Cagg = G2D(G3D(C))`，即先 3D 聚合、再 2D 聚合的串行设计。
  - 3D 卷积分支用于建模视差维度的结构化连续性；2D 分支采用 ConvNeXt 层进行高效空间精修。
  - 只保留少量 3D 组件，约 4.8% 比例，避免 3D 卷积主导计算量；3D 卷积核采用 `(3,3,3)`。
  - 消融显示 3D→2D 串行优于纯 2D、双边、2D→3D、交错等设计。
- **视差估计**：
  - 对聚合后的 cost volume 使用 soft-argmax 回归 1/4 分辨率视差。
  - 再通过 convex upsampling 恢复全分辨率视差图。
- **三阶段训练策略**：
  - **Stage ① 合成数据监督**：在约 1.8M 合成标注样本上端到端监督训练，损失为 smooth L1 视差损失。
  - **Stage ② 自蒸馏**：教师与学生同架构，教师输入干净数据，学生输入强扰动数据；教师权重固定，学生通过视差损失和特征对齐损失学习域不变表示。特征对齐损失为 `1 - cos` 相似度。
  - **Stage ③ 真实无标签知识蒸馏**：收集约 0.5M 真实立体图像对，用 FoundationStereo 生成密集伪标签，对轻量模型进行微调。该阶段不再使用自蒸馏。
  - 数据选择上强调质量优先于规模，低质量或域特定真实数据可能损害零样本性能。

## 3. 实验设计
- **评测数据集/场景
