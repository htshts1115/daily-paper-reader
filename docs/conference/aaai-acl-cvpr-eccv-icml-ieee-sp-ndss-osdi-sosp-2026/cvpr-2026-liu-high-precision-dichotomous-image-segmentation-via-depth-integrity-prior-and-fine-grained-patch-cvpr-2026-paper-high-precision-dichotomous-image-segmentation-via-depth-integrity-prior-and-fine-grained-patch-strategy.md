---
title: High-Precision Dichotomous Image Segmentation via Depth Integrity-Prior and Fine-Grained Patch Strategy
title_zh: 基于深度完整性先验与细粒度分块的高精度二值图像分割
authors: "Liu, Xianjie, Fu, Keren, Zhao, Qijun"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_High-Precision_Dichotomous_Image_Segmentation_via_Depth_Integrity-Prior_and_Fine-Grained_Patch_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 5.0
evidence: 结合深度先验的精细二值分割与清晰边界
tldr: 高精度二值图像分割需从高分辨率图中提取精细目标，现有方法在效率与精度间难以兼顾。本文提出深度完整性先验，认为完整目标在深度图中呈内部平滑、边界锐利的低方差区域，并配合细粒度分块策略实现高效精细分割。实验表明该方法在提升边界精度的同时兼顾效率，对细结构与边界敏感的分割需求有参考价值。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 11841, \"height\": 3708}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 2450, \"height\": 345}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1720, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 3, \"index\": 4, \"width\": 3390, \"height\": 1110}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 2235, \"height\": 1215}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 3725, \"height\": 1240}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-liu-high-precision-dichotomous-image-segmentation-via-depth-integrity-prior-and-fine-grained-patch-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 2040, \"height\": 845}]"
motivation: 高精度二值图像分割在效率与精度间难以兼顾，非扩散方法语义弱、扩散方法计算昂贵。
method: 提出深度完整性先验，将完整目标视为深度图中的低方差平滑区域，并结合细粒度分块策略进行精细分割。
result: 实验表明该方法在提升细粒度目标边界精度的同时保持了较高计算效率。
conclusion: 该工作为高精度细结构图像分割提供了结合深度先验的实用方案。
---

## Abstract
High-precision dichotomous image segmentation (DIS) is a task of extracting fine-grained objects from high-resolution images.Existing methods trade efficiency for accuracy: non-diffusion methods are fast but suffer from weak semantics and unstable spatial priors, causing false detections; diffusion-based methods offer high accuracy via strong generative priors but are computationally expensive.In depth maps, a complete object appears as a low variance region with a smooth interior and sharp boundaries, whereas the background exhibits a chaotic, high variance pattern due to disconnected surfaces at varying depths. We refer to this as the depth integrity-prior.Inspired by this, and noting that DIS currently lacks depth maps, we leverage pseudo-depth information from monocular depth estimation models to obtain essential semantic understanding, thereby rapidly revealing spatial differences across target objects and the background.To exploit this prior, we propose the Prior-guided Depth Fusion Network (PDFNet), which fuses RGB and pseudo-depth features for depth-aware structure perception. We further introduce a novel depth integrity-prior loss to enforce depth consistency in segmentation and a fine-grained enhancement module with adaptive patch selection to sharpen boundaries.Notably, PDFNet with DAM-v2 achieves SOTA (F^ max _b 0.915 on DIS-VD and 0.915 on DIS-TE) using less than half the params of diffusion-based methods.

---

## 论文详细总结（自动生成）

# 论文总结：基于深度完整性先验与细粒度分块的高精度二值图像分割

## 1. 核心问题与研究动机

- **任务背景**：高精度二值图像分割（DIS）旨在从高分辨率图像中逐像素精细提取前景目标，广泛应用于图像编辑、增强现实等场景。
- **核心矛盾**：现有方法在效率与精度之间难以兼顾——
  - **非扩散方法**（CNN/Transformer）：轻量、推理快（FPS>3），但感受野受限，语义弱、空间先验不稳定，易产生误检/漏检。
  - **扩散方法**：借助大规模生成先验精度高，但参数量巨大（>865M）、推理极慢（FPS<1），难以实用。
- **关键观察（深度完整性先验）**：在深度图中，完整目标表现为**内部平滑、边界锐利的低方差区域**；背景因不同深度表面断裂而呈**高方差混乱模式**。据此可区分目标与背景。
- **解决思路**：DIS 此前缺乏深度图，本文利用单目深度估计模型（DAM-v2）生成伪深度，引入**深度完整性先验**作为任务自适应引导，兼顾易获取性、高性能与强引导性。

## 2. 方法论

### 2.1 核心思想
- 首次将**深度作为新模态**引入 DIS，提出 **PDFNet（Prior-guided Depth Fusion Network）**，融合 RGB 与伪深度特征实现深度感知的结构感知。
- 配套设计**深度完整性先验损失**与**细粒度增强模块（自适应分块选择）**，以锐化边界。

### 2.2 关键技术细节

- **深度生成**：DAM-v2 将输入图像映射为归一化深度图 D∈[0,1]。
- **多阶段特征提取**：
  - 主编码器分别提取 RGB 与深度多尺度特征 {F^v_i}、{F^d_i}（i=1..4）。
  - 并行分支将图像切分为 **64 个 patch（8×8）**，经 patch 编码器处理后重组为高分辨率特征序列 {F^p_i}。
  - 跨尺度 3×3 卷积融合多级特征，得到 {F^v_5, F^d_5, F^p_5}。
- **精炼解码**：每阶段集成 **FSE（特征选择与提取）模块**，依据上一阶段预测的边界与完整性线索动态增强显著特征，并用跨注意力融合多模态。
- **深度精炼**：专用解码器执行深度重建任务，引导共享编码器学习对分割与深度估计均有益的表示；每阶段为两层 3×3 卷积 + SiLU + RMSNorm。
- **深度监督与多特征融合**：多阶段深度监督，最终预测逐步上采样并与浅层编码器特征融合。

### 2.3 FSE 模块
- 对上一阶段预测 P_{i+1} 做平均池化得 P^p，绝对差得边界图 B_i：
  - `B_i(x,y)=1 if |P_{i+1}(x,y)−P^p_{i+1}(x,y)|>τ else 0`（τ=0.1）
- 边界抑制得目标完整性图：`S_i = ReLU(P_{i+1} − B_i)`
- 将 B_i 分为 64 个 patch，二值化选择得边界响应得分 B^d_i，据此加权增强含边界的 patch。
- **CoA（跨模态注意力）**：基于 QKV 交互、RMSNorm 归一化注意力输出、SwiGLU FFN 与残差连接，实现视觉-深度、视觉-patch 的跨模态交互：
  - `F^{Np*}_i = CoA(F^P_{pi} ⊙ (1+B^d_i), F^P_{vdi})`
  - `F^{Nd*}_i = CoA(F^P_{di} ⊙ (1+S_i), F^P_{vpi})`
  - 再经两级 CoA 融合，最终更新 F^{v*}_i、F^{p*}_i、F^{d*}_i。

### 2.4 深度完整性先验损失
- **深度稳定性约束**：基于深度偏差自适应加权交叉熵，惩罚两类错误——偏离目标均值的假阳性（FP）和深度一致却被漏掉的假阴性（FN）。
  - 均值：`μ = Σ(D⊙M)/ΣM`
  - `l_v = E[−log P_y ⊙ (diff ⊙ (FP−FN) + FN)]`，其中 `diff=(D−μ)^2`
- **深度连续性约束**：在深度梯度大的位置加大对分割误差的惩罚，使预测掩码与深度梯度对齐。
  - `l_g = E[−log P_y ⊙ (|G_x|+|G_y|)]`（Sobel 算子）
- 最终：`l_inte = (l_v + l_g)/2`

### 2.5 总损失
- 分割监督：`l = l_wBCE + l_wIoU + l_SSIM/2 + l_inte`
- 深度精炼监督：SILog 损失
- 总损失：`L = l_f + λ1·Σ_{i=1}^{5} l_i^f + λ2·(l_SILog + λ1·Σ_{i=1}^{5} l_i^SILog)`，λ1=0.5，λ2=0.1

## 3. 实验设计

- **数据集**：DIS-5K（5,470 张图、225 类，含 DIS-TR 3,000、DIS-VD 470、DIS-TE1-4 各 500）。
- **评价指标**：F^max_β、F^w_β、S_α、E^m_ϕ、M（MAE）。
- **对比方法**：
  - 非扩散：IS-Net、UDUN、InSPyReNet、MVANet、BiRefNet
  - 扩散：GenPercept、DiffDIS
  - RGB-D SOD：MAGNet、CPNet，以及将 MVANet 适配为 RGB-D 的 MVANet*
- **PDFNet 变体**：PDFNet-S/B/L（分别使用 DAM-v2 Small/Base/Large 生成伪深度）。
- **额外泛化实验**：HRSOD 任务（HRSOD-TE 400、UHRSD-TE 988），对比 PGNet、InSPyReNet、BiRefNet。
- **深度生成器鲁棒性**：DAM-S、DAM-v2 S/B/L、DepthPro（1B）。

## 4. 资源与算力

- **GPU**：RTX-4090（文中仅提及型号，**未说明 GPU 数量**）。
- **训练配置**：Swin-B 骨干（ImageNet-21K 预训练）；输入 1024²；100 epochs；AdamW，lr=1×10⁻⁵，batch size=1；HRSOD 实验训练 40 epochs。
- **推理时间**：DAM-v2 S/B/L 默认管线分别 47ms/91ms/127ms；PDFNet-S/B/L 整体 FPS 为 5.7/4.5/3.9（含深度生成）。
- **未明确说明**：总训练时长、GPU 数量、能耗等。

## 5. 实验数量与充分性

- **主实验**：DIS-VD、DIS-TE1-4、DIS-TE(ALL) 共 6 个测试集，覆盖 11 种以上对比方法。
- **消融实验**：
  - 组件消融（S、Bd、FSE、Depth 逐项加入）
  - 深度损失消融（LSILog、Linte 组合）
  - Linte 在其他模型（MAGNet、CPNet）上的通用性验证
  - patch 数量消融（1×1 至 16×16，对比 MVANet）
  - 不同深度生成器质量的影响
- **泛化实验**：HRSOD/UHRSD 两个高分辨率显著目标检测数据集。
- **充分性与公平性评价**：
  - 实验覆盖面较广，消融较系统，主实验与泛化实验兼具。
  - 所有模型均使用官方参数并在同一 RTX-4090 上重跑、统一 1024² 输入，公平性较好。
  - 对 DiffDIS 的“pre-metric binarization”差异做了说明并选择不采用二值化以保持一致。
  - 消融主要在 DIS-VD 上进行，规模相对有限。

## 6. 主要结论与发现

- PDFNet 在 DIS-VD 与 DIS-TE 上达到 **F^max_β 0.915** 的 SOTA，参数不足扩散方法的 **50%**。
- 在 DIS-TE(ALL) 上较 MVANet 分别提升 **0.7%/1.5%/0.6%/1.2%/0.5%**（F^max_β、F^w_β、S_α、E^m_ϕ、M）。
- 在部分指标上超过扩散方法 DiffDIS，同时推理效率显著更高。
- 深度完整性先验可显著提升目标完整性检测；Linte 可推广至 MAGNet、CPNet 等模型。
- 模型对伪深度质量具有较强鲁棒性（即使使用 DepthPro 1B 也保持高性能）。
- 在 HRSOD/UHRSD 上同样超越 PGNet、InSPyReNet、BiRefNet，展现良好泛化能力。

## 7. 优点

- **新颖的先验视角**：首次将深度模态引入 DIS，提出“深度完整性先验”，观察直观且具物理意义。
- **损失设计精巧**：深度稳定性约束与连续性约束分别针对 FP/FN 与边界对齐，公式可解释性强，且具跨模型通用性。
- **效率与精度平衡好**：以非扩散范式达到接近/超越扩散方法的精度，参数量与推理速度优势明显。
- **分块策略有针对性**：8×8 patch 密度经消融验证最优，配合全分辨率主分支保留全局上下文。
- **实验较全面**：涵盖 DIS 主任务、HRSOD 泛化、深度生成器鲁棒性、跨模型损失通用性。
- **公平对比意识**：统一重跑、统一输入分辨率，并说明 DiffDIS 的二值化差异。

## 8. 不足与局限

- **依赖外部伪深度生成**：引入额外推理开销（FPS 3.9–5.7，低于 BiRefNet 的 6），且伪深度质量会影响上限。
- **算力信息不完整**：未报告 GPU 数量、训练总时长，复现成本不透明。
- **消融规模有限**：组件与损失消融主要在 DIS-VD（470 张）上进行，结论的统计稳健性有待更大规模验证。
- **失败案例分析缺失**：论文未系统讨论误分割或深度先验失效的场景（如透明物体、反光表面、深度估计失败区域）。
- **深度生成器权衡**：DepthPro（1B）精度略高但参数量大、速度更慢，实际部署需权衡。
- **应用限制**：对实时性要求高且无 GPU 的场景仍不友好；伪深度在特定域（医学、显微等）可能不适用。
- **指标依赖**：未采用 pre-metric binarization，与部分扩散方法的原始报告不完全可比，横向对比需谨慎。

（完）
