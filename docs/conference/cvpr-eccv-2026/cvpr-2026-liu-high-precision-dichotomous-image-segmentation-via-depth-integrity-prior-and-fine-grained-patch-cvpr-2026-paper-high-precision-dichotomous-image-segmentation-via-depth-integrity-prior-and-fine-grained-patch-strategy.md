---
title: High-Precision Dichotomous Image Segmentation via Depth Integrity-Prior and Fine-Grained Patch Strategy
title_zh: 基于深度完整性先验与细粒度分块策略的高精度二值图像分割
authors: "Liu, Xianjie, Fu, Keren, Zhao, Qijun"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_High-Precision_Dichotomous_Image_Segmentation_via_Depth_Integrity-Prior_and_Fine-Grained_Patch_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 6.0
evidence: 深度先验辅助精细前景分割
tldr: 高精度二值图像分割需要从高分辨率图像中提取细粒度目标，非扩散方法速度快但语义弱、空间先验不稳，扩散方法精度高却计算昂贵。该工作发现深度图中完整目标表现为内部平滑、边界锐利的低方差区域，背景则因深度不连续呈高方差混沌模式，据此提出深度完整性先验，并结合细粒度分块策略实现高精度分割。实验在精度与效率之间取得更好折中，为精细前景提取提供了新的空间线索。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 11841, \"height\": 3708}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 2450, \"height\": 345}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1720, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 3, \"index\": 4, \"width\": 3390, \"height\": 1110}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 2235, \"height\": 1215}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 3725, \"height\": 1240}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 2040, \"height\": 845}]"
motivation: 高精度二值图像分割需从高分辨率图像提取细粒度目标，现有方法在效率与精度之间难以兼顾。
method: 提出深度完整性先验，利用完整目标在深度图中内部平滑、边界锐利的低方差特性，并结合细粒度分块策略。
result: 在精度与效率之间取得更好折中，减少误检并稳定空间先验。
conclusion: 为精细前景分割引入了新的深度空间线索。
---

## Abstract
High-precision dichotomous image segmentation (DIS) is a task of extracting fine-grained objects from high-resolution images.Existing methods trade efficiency for accuracy: non-diffusion methods are fast but suffer from weak semantics and unstable spatial priors, causing false detections; diffusion-based methods offer high accuracy via strong generative priors but are computationally expensive.In depth maps, a complete object appears as a low variance region with a smooth interior and sharp boundaries, whereas the background exhibits a chaotic, high variance pattern due to disconnected surfaces at varying depths. We refer to this as the depth integrity-prior.Inspired by this, and noting that DIS currently lacks depth maps, we leverage pseudo-depth information from monocular depth estimation models to obtain essential semantic understanding, thereby rapidly revealing spatial differences across target objects and the background.To exploit this prior, we propose the Prior-guided Depth Fusion Network (PDFNet), which fuses RGB and pseudo-depth features for depth-aware structure perception. We further introduce a novel depth integrity-prior loss to enforce depth consistency in segmentation and a fine-grained enhancement module with adaptive patch selection to sharpen boundaries.Notably, PDFNet with DAM-v2 achieves SOTA (F^ max _b 0.915 on DIS-VD and 0.915 on DIS-TE) using less than half the params of diffusion-based methods.

---

## 论文详细总结（自动生成）

# 论文总结：基于深度完整性先验与细粒度分块策略的高精度二值图像分割

### 1. 核心问题与整体含义

- **任务背景**：高精度二值图像分割（DIS）旨在从高分辨率图像中像素级地分离前景目标，广泛用于图像编辑、增强现实等需要高保真掩码的场景。
- **核心矛盾**：现有方法在效率与精度之间难以兼顾。
  - **非扩散方法**：轻量、推理快，但在高分辨率下全局结构与局部细节难以同时建模，语义弱、空间先验不稳，易产生误检/漏检。
  - **扩散方法**：借助大规模生成先验，精度高、复杂场景一致性好，但参数量巨大、推理极慢，实际应用受限。
- **关键观察**：在深度图中，完整目标通常表现为内部平滑、边界锐利的低方差区域；背景因深度不连续呈高方差、混沌模式。作者将其定义为 **深度完整性先验（depth integrity-prior）**。
- **整体含义**：论文首次将深度作为 DIS 的新模态，利用单目深度估计模型生成的伪深度提供强空间引导，提出 **PDFNet**，在非扩散范式下以更少参数取得与扩散方法竞争甚至部分指标更优的结果。

### 2. 方法论

- **核心思想**：利用伪深度图中的目标-背景结构差异，融合 RGB、伪深度和细粒度分块特征，实现深度感知的结构感知与边界细化。
- **整体架构 PDFNet**：
  - 使用 DAM-v2 生成归一化伪深度图 \(D \in [0,1]\)。
  - 主编码器提取多尺度 RGB 特征 \(F^v_i\) 和深度特征 \(F^d_i\)。
  - 并行分块分支将图像划分为 \(8\times8=64\) 个 patch，经 patch 编码器后重组为高分辨率特征 \(F^p_i\)。
  - 解码器每阶段引入 **FSE 模块**，基于上一阶段预测的边界与完整性线索动态增强特征，并用跨模态注意力融合多模态信息。
  - 额外设置 **深度细化解码器**，用伪深度重建任务正则化共享编码器，促进模型从 RGB 中提取细粒度结构。
  - 采用深监督与多特征融合，最终预测逐步上采样并融合浅层特征。
- **FSE 与自适应 patch 选择**：
  - 对上一阶段预测 \(P_{i+1}\) 做平均池化得到 \(P^p_{i+1}\)。
  - 边界图 \(B_i(x,y)=1\) 若 \(|P_{i+1}(x,y)-P^p_{i+1}(x,y)|>\tau\)，否则为 0，\(\tau=0.1\)。
  - 目标完整性图 \(S_i=\mathrm{ReLU}(P_{i+1}-B_i)\)，抑制边界、突出目标内部连续区域。
  - 将边界图分为 64 个 patch，得到每个 patch 的边界响应 \(B^d_i\)，用于选择性增强含目标边界的 patch。
  - 通过跨模态注意力 CoA 融合视觉-深度 \(F^{Pvd}_i\)、视觉-分块 \(F^{Pvp}_i\)，并逐步更新 \(F^v_i, F^p_i, F^d_i\)。
- **深度完整性先验损失**：
  - 计算 GT 掩码区域 \(M\) 内的平均深度：\(\mu=\sum(D\odot M)/\sum M\)。
  - 深度稳定性约束：用 \(diff=(D-\mu)^2\) 对假阳性 FP 和假阴性 FN 进行差异化加权，惩罚偏离目标均值的 FP，也惩罚深度一致却被漏掉的 FN。
  - 具体形式：\(l_v=\mathbb{E}[-\log(P_y\odot(diff\odot(FP-FN)+FN))]\)，其中 \(P_y=P\odot M+(1-P)\odot(1-M)\)。
  - 深度连续性约束：\(l_g=\mathbb{E}[-\log(P_y\odot(|G_x|+|G_y|))]\)，其中 \(G_x,G_y\) 为 Sobel 深度梯度，强调深度突变处与目标边界一致。
  - 最终深度完整性先验损失：\(l_{inte}=(l_v+l_g)/2\)。
- **总损失**：
  - 分割损失组合加权 BCE、加权 IoU、SSIM 与 \(l_{inte}\)：\(l=l_{wBCE}+l_{wIoU}+l_{SSIM}/2+l_{inte}\)。
  - 深度细化使用 SILog 损失。
  - 总体损失：\(L=l_f+\lambda_1\sum_{i=1}^5 l_i^f+\lambda_2(l_{SILog}+\lambda_1\sum_{i=1}^5 l_i^{SILog})\)，其中 \(\lambda_1=0.5,\lambda_2=0.1\)。

### 3. 实验设计

- **数据集与 benchmark**：
  - 主要在 **DIS-5K** 上评测，包含 DIS-TR（3000）、DIS-VD（470）、DIS-TE1~TE4（各 500，共 2000），覆盖 225 类、由简到繁。
  - 额外在 **HRSOD** 任务上验证泛化：HRSOD-TE（400）、UHRSD-TE（988）。
- **评价指标**：\(F^{max}_\beta\)、\(F^w_\beta\)、\(E_m^\phi\)、\(S_\alpha\)、MAE（\(M\)）。
- **对比方法**：
  - 非扩散 DIS：IS-Net、UDUN、InSPyReNet、BiRefNet、MVANet。
  - 扩散方法：GenPercept、DiffDIS。
  - RGB-D SOD：MAGNet、CPNet，以及将 MVANet 适配为 RGB-D 输入的 MVANet*。
  - HRSOD 对比：PGNet、InSPyReNet、BiRefNet。
- **实现细节**：
  - 输入统一 resize 到 \(1024^2\)。
  - 骨干为 ImageNet-21K 预训练的 Swin-B。
  - 训练 100 epochs，AdamW，学习率 \(1\times10^{-5}\)，batch size 1。
  - 数据增强包括随机水平翻转、旋转、颜色抖动。
  - 伪深度由 DAM-v2 Small/Base/Large 生成；模型输入深度来自默认 \(518^2\rightarrow1024^2\)，监督目标来自更高保真 \(1024^2\rightarrow1024^2\)。
  - DAM-v2 S/B/L 推理耗时约 47ms/91ms/127ms。

### 4. 资源与算力

- 文中明确：所有实验在 **RTX-4090** 上进行，使用 Swin-B 预训练骨干，训练 100 epochs，batch size 为 1。
- **未明确说明**：
  - 使用的 GPU 数量；
  - 总训练时长、总 GPU 小时数；
  - 完整训练与推理的能耗或成本。
- 给出了部分推理时间：DAM-v2 Small/Base/Large 单次深度生成约 47/91/127ms；PDFNet-S/B/L 的 FPS 分别为 5.7、4.5、3.9，且包含深度生成时间。

### 5. 实验数量与充分性

- **主实验**：
  - 在 DIS-VD、DIS-TE1~TE4、DIS-TE(ALL) 上对比 10 余种方法，报告 5 个指标，规模较大。
  - PDFNet-S/B/L 分别对应不同 DAM-v2 深度生成器，体现深度质量影响。
- **消融实验**：
  - 组件消融：S、Bd、FSE、Depth 等模块。
  - 深度损失消融：SILog 与 \(L_{inte}\) 的组合。
  - patch 数量消融：\(1\times1\) 到 \(16\times16\)，发现 \(8\times8=64\) 最佳。
  - \(L_{inte}\) 泛化性：在 MAGNet、CPNet、PDFNet 上验证。
  - 深度生成器鲁棒性：DAM-S、DAM-v2 S/B/L、DepthPro 1B。
  - 跨任务泛化：HRSOD/UHRSD。
- **充分性与公平性**：
  - 实验覆盖面较广，包括主基准、消融、跨任务、跨深度生成器，较充分。
  - 作者说明所有模型使用官方参数并在 RTX-4090 上重跑，尽量公平。
  - 对 DiffDIS 的“pre-metric binarization”差异有说明，并选择与 MVANet/BiRefNet 一致的不二值化协议。
  - **局限**：部分消融仅在 DIS-VD（470 张）上进行；未在全部 DIS-TE 子集重复消融；参数量统计中 PDFNet 需加上深度生成器参数，不同变体外部依赖不同，公平性仍受深度生成器影响。

### 6. 主要结论与发现

- PDFNet 在 DIS 上达到非扩散方法中的 SOTA，并在 \(F^{max}_\beta\) 上匹配或超过扩散方法。
  - PDFNet-L 在 DIS-VD 上 \(F^{max}_\beta=0.915\)，DIS-TE(ALL) 上 \(F^{max}_\beta=0.915\)。
  - 相比 MVANet，在 DIS-TE(ALL) 上 \(F^{max}_\beta\)、\(F^w_\beta\)、\(S_\alpha\)、\(E_m^\phi\)、MAE 均有提升。
  - 相比 DiffDIS，PDFNet-L 在部分指标如 \(F^{max}_\beta\)、\(S_\alpha\) 上更优，但 \(F^w_\beta\)、\(E_m^\phi\)、MAE 仍略逊。
- 参数量与效率优势明显：
  - PDFNet 使用不到扩散方法 50% 的参数；
  - FPS 高于 DiffDIS（0.8），低于 BiRefNet（6）和 MVANet（6.5），但包含深度生成后仍具实用速度。
- 深度完整性先验有效：
  - 深度输入显著提升目标完整性检测；
  - \(L_{inte}\) 可提升 PDFNet，也可提升 MAGNet、CPNet 等其他模型，显示通用性。
- 细粒度分块策略有效：
  - \(8\times8\) patch 在保留全局上下文的同时增强局部边界细节，优于 \(2\times2\)、\(4\times4\)、\(16\times16\)。
- 泛化能力：
  - 在 HRSOD/UHRSD 上超过 PGNet、InSPyReNet、BiRefNet；
  - 对不同质量伪深度生成器具有较强鲁棒性。

### 7. 优点

- **新模态引入**：首次在 DIS 中系统引入深度模态，提出深度完整性先验，为后续多模态 DIS 研究提供参考。
- **损失设计新颖且通用**：\(L_{inte}\) 同时约束
