---
title: "Guardians of the Hair: Rescuing Soft Boundaries in Depth, Stereo, and Novel Views"
title_zh: 发丝守护者：在深度、立体与新颖视角中挽救软边界
authors: "Zhang, Xiang, Zhang, Yang, Mehl, Lukas, Gross, Markus, Schroers, Christopher"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Zhang_Guardians_of_the_Hair_Rescuing_Soft_Boundaries_in_Depth_Stereo_CVPR_2026_paper.pdf"
tags: ["query:matting"]
score: 8.0
evidence: 利用抠图数据集与深度修复网络恢复发丝软边界
tldr: 细发丝等软边界因前景背景线索混淆而困扰三维视觉任务。本文提出HairGuard框架，利用图像抠图数据集构建训练数据流程，并设计深度修复网络自动识别软边界区域，通过门控残差模块在保持全局深度质量的同时精细修复边界。该方法可即插即用地增强主流深度模型，对发丝细节抠图与深度边界处理均有价值。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 4110, \"height\": 1831}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 3, \"index\": 11, \"width\": 4642, \"height\": 1724}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 4, \"index\": 12, \"width\": 4051, \"height\": 2256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 4, \"index\": 13, \"width\": 3933, \"height\": 2433}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 4, \"index\": 14, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 4, \"index\": 15, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 4, \"index\": 16, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 4, \"index\": 17, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 4, \"index\": 18, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 4, \"index\": 19, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 4217, \"height\": 1783}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 4158, \"height\": 1819}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 7, \"index\": 26, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 7, \"index\": 27, \"width\": 1000, \"height\": 1000}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 7, \"index\": 28, \"width\": 1000, \"height\": 1000}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 7, \"index\": 29, \"width\": 1000, \"height\": 1000}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 7, \"index\": 30, \"width\": 1000, \"height\": 1000}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 7, \"index\": 31, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 7, \"index\": 32, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 7, \"index\": 33, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 7, \"index\": 34, \"width\": 640, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 8, \"index\": 35, \"width\": 500, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 8, \"index\": 36, \"width\": 500, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-zhang-guardians-of-the-hair-rescuing-soft-boundaries-in-depth-stereo-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 8, \"index\": 37, \"width\": 1000, \"height\": 375}]"
motivation: 细发丝等软边界因前景背景线索混叠而成为三维视觉中的难点，现有深度模型难以恢复此类细节。
method: 提出HairGuard，借助图像抠图数据集构建训练流程，设计带门控残差的深度修复网络定位并精修软边界。
result: 该方法可即插即用集成到先进深度模型，在保持全局深度质量的同时显著改善软边界细节。
conclusion: 该工作为发丝等软边界在深度、立体及新视角任务中的恢复提供了通用增强方案。
---

## Abstract
Soft boundaries, like thin hairs, are commonly observed in natural and computer-generated imagery, but they remain challenging for 3D vision due to the ambiguous mixing of foreground and background cues. This paper introduces Guardians of the Hair (HairGuard), a framework designed to recover fine-grained soft boundary details in 3D vision tasks. Specifically, we first propose a novel data curation pipeline that leverages image matting datasets for training and design a depth fixer network to automatically identify soft boundary regions. With a gated residual module, the depth fixer refines depth precisely around soft boundaries while maintaining global depth quality, allowing plug-and-play integration with state-of-the-art depth models. For view synthesis, we perform depth-based forward warping to retain high-fidelity textures, followed by a generative scene painter that fills disoccluded regions and eliminates redundant background artifacts within soft boundaries. Finally, a color fuser adaptively combines warped and inpainted results to produce novel views with consistent geometry and fine-grained details. Extensive experiments demonstrate that HairGuard achieves state-of-the-art performance across monocular depth estimation, stereo image/video conversion, and novel view synthesis, with significant improvements in soft boundary regions.

---

## 论文详细总结（自动生成）

## 论文总结：Guardians of the Hair（HairGuard）

### 1. 核心问题与研究动机

- **核心问题**：软边界（soft boundaries）——如细发丝、半透明结构——因像素同时混合前景与背景贡献（alpha 混合），在三维视觉任务中造成深度不确定性与对应关系歧义，导致现有方法难以恢复其精细几何与纹理。
- **背景痛点**：
  - 显式深度方法（Depth Anything V2、Depth Pro、UniDepthV2）在软边界处常出现深度断裂、发丝脱离表面、边界破碎等问题（图 2）。
  - 隐式生成方法（ReCamMaster、StereoCrafter）虽能处理复杂遮挡，但受生成模型幻觉影响，在软边界处纹理不一致，且潜空间压缩导致细节退化。
  - 深度误差会传播至立体转换与新视角合成等下游任务，造成次优结果。
- **整体含义**：论文提出 **HairGuard** 框架，受图像抠图（image matting）中 alpha 合成公式启发，将软边界建模为显式可学习问题，在单目深度估计、立体图像/视频转换、新视角合成三类任务中系统性挽救软边界细节。

### 2. 方法论

- **核心思想**：以 alpha 合成公式 `I = α·I_FG + (1−α)·I_BG` 为理论基础，将软边界定义为 `α ∈ (0,1)` 的混合区域，利用图像抠图数据集构建训练数据，并设计三个协同组件：**depth fixer**、**scene painter**、**color fuser**。

- **数据策展（Data Curation）**：
  - 以抠图数据集作为前景 `I_FG = {(α, I_FG)_i}`，图像数据集作为背景 `I_BG`。
  - 通过阈值 `α_th` 生成 alpha 掩码 `M_α = {p | α_th < α(p)}`。
  - 前景深度 `d_FG = M_α ⊙ Depth(I_FG)`，背景深度 `d_BG = Depth(I_BG)`，随机采样深度值重缩放 `d_FG` 以增强数据。
  - 深度合成：`d = d_FG ⊙ M_α + d_BG ⊙ (1 − M_α)`；通过变化 `α_th` 生成成对训练数据（低阈值 → 精细 GT，高阈值 → 模拟破损输入）。
  - 对 `M_α` 施加随机高斯模糊以生成输入 `d_in`，GT 使用未模糊掩码以保留锐利边界。

- **Depth Fixer 网络设计**：
  - 双分支结构：特征分支（DINOv2 + DPT）提取深层语义；像素分支（U-Net）捕捉局部结构与边界细节。
  - 自动定位：对输入深度施加 Sobel 算子生成边缘引导 `e = Sobel(d_in)`，与图像、深度拼接后输入像素分支。
  - **门控残差机制**：预测门控图 `G ∈ [0,1]`，`G < 1` 表示软边界区域；精修深度 `ˆd = d_in · G + d_res · (1 − G)`，仅对软边界区域施加修正，保持全局深度质量。
  - **两阶段训练**：
    - 第一阶段：`L_depth^stage1 = L1(ˆd, d_GT) + L_α(ˆd ⊙ M_soft, d_GT ⊙ M_soft)`，其中 `L_α` 为 ViTMatte 抠图损失，防止门控坍缩为 `G=1`。
    - 第二阶段：`L_depth^stage2 = L_α(ˆd, d_GT)`，全局施加抠图损失以消除第一阶段产生的光晕伪影。

- **视合成流程**：
  - 先基于修复后深度进行前向 warping，保留高保真纹理。
  - **Scene Painter**：基于预训练 VACE（Wan2.1-1.3B）微调，填充去遮挡区域并消除软边界内冗余背景伪影。
  - **数据策展**：利用光流估计器预测背景光流，前景施加随机平移位移，通过 `f = f_FG ⊙ M_α + f_BG ⊙ (1 − M_α)` 合成光流，生成 warped 图像与 GT 视图。
  - **Color Fuser**：基于预训练 VAE，设计 **dual skip 模块**将 inpainted 与 warped 图像的多尺度特征及 warped 掩码送入 VAE 解码器，补偿纹理细节。
  - 训练目标：`L_color = L1(ˆI, I_GT) + λ · L_lpips(ˆI, I_GT)`，其中 `λ = 0.1`。

### 3. 实验设计

- **训练数据集**：
  - 背景多视图数据集：RealEstate10K、DL3DV-10K。
  - 前景抠图数据集：AM-2K、Distinctions-646、Composition-1K。
- **评估数据集与 Benchmark**：
  - 自建 **Marvel-10K**：501 段漫威电影立体视频，共 12,525 对立体帧，含复杂发丝与电影级场景。
  - 深度估计零样本基准：NYUv2、KITTI、ETH3D、ScanNet、DIODE。
  - 自然图像抠图数据集：AIM-500、P3M-10K（用于评估真实世界软边界性能）。
- **对比方法**：
  - 深度估计：Depth Anything V2、Depth Pro、UniDepthV2（即插即用集成对比）。
  - 立体转换：StereoDiffusion、Mono2Stereo、StereoCrafter、ViewCrafter、NVS-Solver、ReCamMaster、SplatDiff。
  - 新视角合成：NVS-Solver、ViewCrafter、ReCamMaster、SplatDiff。
- **评估指标**：
  - 深度边界：DBE completeness/accuracy、EP、ER；零样本深度：AbsRel、δ1。
  - 立体转换：PSNR、SSIM、RMSE、LPIPS、DISTS、SIoU。
  - 新视角合成：FID、CLIP-F。
- **用户研究**：27 名参与者，在 AIM-500 与 P3M-10K 全量评估集（1000 张自然图像）上对并排视频结果投票，共收集 1332 票。

### 4. 资源与算力

- **GPU**：4 张 NVIDIA RTX A6000。
- **总训练时长**：约 4 天。
- **各模块训练细节**：
  - Depth Fixer：448×448 patch，batch size 32，学习率 1×10⁻⁵，两阶段各 35K 迭代。
  - Scene Painter：480×832 分辨率，batch size 4，学习率 1×10⁻⁵，10K 迭代。
  - Color Fuser：448×448 patch，batch size 16，学习率 1×10⁻⁵，35K 迭代。
- 论文明确给出了上述算力信息，未提及推理阶段的具体资源消耗。

### 5. 实验数量与充分性

- **实验组数概览**：
  - 深度边界准确率（表 1）：3 个基础深度模型 × 2 个抠图数据集，共 6 组对比。
  - 零样本深度估计（表 2）：3 个基础模型 × 5 个基准数据集，共 15 组对比。
  - 立体图像/视频转换（表 3）：8 种方法 × 2 种任务 × 6 个指标。
  - 消融实验（表 4）：4 组配置（基线、+Depth Fixer、+Scene Painter、+Color Fuser）。
  - 新视角合成（表 5）：5 种方法 × 2 个数据集 × 2 个指标。
  - 用户研究：27 人、1332 票。
- **充分性与客观性评估**：
  - 覆盖了三大任务、多个公开基准与自建基准，消融实验清晰验证各组件贡献，用户研究规模合理。
  - 对比方法均为近年 SOTA，指标多样（像素级、特征级、立体专用指标），较为全面。
  - 零样本深度实验显示深度修复器不损害基础模型的泛化能力（表 2 中多数指标持平或略优），体现了公平性。
  - 局限：Marvel-10K 为自建数据集，未公开；部分对比方法可能未在其最优配置下运行；软边界评估主要依赖抠图数据集，真实场景覆盖仍有限。

### 6. 主要结论与发现

- HairGuard 在单目深度估计、立体图像/视频转换、新视角合成三类任务上均达到 **SOTA 性能**，尤其在软边界区域提升显著。
- Depth Fixer 以即插即用方式集成到 Depth Anything V2、Depth Pro、UniDepthV2，在 AIM-500 与 P3M-10K 上大幅提升边界精度（如 EP 从 19.90% 提升至 34.56%，ER 从 6.50% 提升至 13.08%），同时不损害零样本深度性能。
- 在 Marvel-10K 立体转换基准上，HairGuard 在所有指标上优于 StereoDiffusion、Mono2Stereo、StereoCrafter、SplatDiff 等方法（PSNR 36.59 vs. 36.23，LPIPS 0.0909 vs. 0.1116，SIoU 0.3337 vs. 0.3259）。
- 消融实验表明：Depth Fixer 改善 warping 几何（SIoU 提升），Scene Painter 提升感知质量但引入纹理幻觉，Color Fuser 融合两者优势，最终取得最佳 PSNR 与 LPIPS。
- 用户研究证实 HairGuard 在新视角合成上显著优于对比方法。

### 7. 优点

- **问题定位精准**：将软边界从图像抠图领域显式引入 3D 视觉，填补了现有深度/视合成方法在发丝等细节上的系统性空白。
- **数据策展巧妙**：无需人工标注软边界深度，利用现成抠图数据集合成高质量训练对，可扩展性强。
- **门控残差设计**：仅对软边界区域施加修正，保持全局深度质量，支持即插即用集成，工程实用价值高。
- **两阶段训练策略**：有效避免门控坍缩与光晕伪影，兼顾局部细节与全局一致性。
- **Color Fuser 的 dual skip 机制**：在生成模型纹理幻觉与 warping 背景冗余之间取得平衡，保留高频细节。
- **实验全面**：覆盖深度、立体、新视角三大任务，包含零样本泛化测试、消融实验与用户研究，结论可信度较高。

### 8. 不足与局限

- **论文未设独立 Limitations 章节**，以下为基于内容的推断：
  - **数据依赖**：训练高度依赖图像抠图数据集的质量与多样性，若目标场景与抠图数据集分布差异大，泛化能力可能受限。
  - **前景运动简化**：视合成数据策展中前景仅施加纯平移运动，未模拟旋转、缩放或非刚性形变，可能限制对复杂动态场景的适应。
  - **自建基准未公开**：Marvel-10K 数据集未说明是否公开，影响结果可复现性与公平对比。
  - **计算成本**：训练需 4 张 A6000 共 4 天，且 Scene Painter 基于 1.3B 参数视频扩散模型，推理开销可能较高。
  - **生成模型固有风险**：Scene Painter 仍基于扩散模型，在极端遮挡或复杂软边界处可能残留幻觉，Color Fuser 虽缓解但未完全消除。
  - **软边界定义依赖阈值**：`α_min`、`α_max`、`α_th` 等超参数需手动设定，不同场景下的最优阈值可能不同。
  - **评估局限**：新视角合成在抠图数据集上使用 FID/CLIP-F 等无参考指标，缺乏几何一致性定量评估；立体转换仅在自建 Marvel-10K 上评测，未在公开立体基准上验证。

（完）
