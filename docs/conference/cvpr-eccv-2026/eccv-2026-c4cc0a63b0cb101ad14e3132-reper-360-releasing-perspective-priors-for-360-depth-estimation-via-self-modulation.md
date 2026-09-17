---
title: "RePer-360: Releasing Perspective Priors for 360° Depth Estimation via Self-Modulation"
title_zh: RePer-360：通过自调制释放透视先验的360°深度估计
authors: "Cheng Guan, Chunyu Lin, Zhijie Shen, Junsong Zhang, Jiyuan Wang"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/3695.pdf"
tags: ["query:mono-depth"]
score: 7.0
evidence: 通过自调制将深度基础模型适配到全景深度
tldr: 深度基础模型在透视图像上表现优异，却因透视与全景域之间的几何差异而难以泛化到360°图像，全量微调又需大量全景数据。本文提出RePer-360，一种畸变感知的自调制框架，通过轻量几何对齐引导模块从ERP与立方投影导出调制信号，引导模型进入全景域而不丢失预训练透视先验。实验证明该方法在单目全景深度估计上有效。该工作为深度基础模型跨域迁移提供了思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 1694, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 558, \"height\": 571}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 1692, \"height\": 844}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 828, \"height\": 416}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1090, \"height\": 544}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 931, \"height\": 578}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 689, \"height\": 427}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-010.webp\", \"caption\": \"\", \"page\": 5, \"index\": 10, \"width\": 944, \"height\": 586}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-011.webp\", \"caption\": \"\", \"page\": 5, \"index\": 11, \"width\": 951, \"height\": 590}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 689, \"height\": 429}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 950, \"height\": 591}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 951, \"height\": 592}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 1620, \"height\": 1004}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 682, \"height\": 1149}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 646, \"height\": 1085}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 684, \"height\": 1116}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 1862, \"height\": 1156}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 1580, \"height\": 834}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 1684, \"height\": 842}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-022.webp\", \"caption\": \"\", \"page\": 12, \"index\": 22, \"width\": 1686, \"height\": 838}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-023.webp\", \"caption\": \"\", \"page\": 12, \"index\": 23, \"width\": 1648, \"height\": 834}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-024.webp\", \"caption\": \"\", \"page\": 12, \"index\": 24, \"width\": 838, \"height\": 420}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-025.webp\", \"caption\": \"\", \"page\": 12, \"index\": 25, \"width\": 1149, \"height\": 575}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-026.webp\", \"caption\": \"\", \"page\": 12, \"index\": 26, \"width\": 840, \"height\": 422}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-027.webp\", \"caption\": \"\", \"page\": 12, \"index\": 27, \"width\": 842, \"height\": 416}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-028.webp\", \"caption\": \"\", \"page\": 12, \"index\": 28, \"width\": 840, \"height\": 418}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-029.webp\", \"caption\": \"\", \"page\": 12, \"index\": 29, \"width\": 1646, \"height\": 824}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-030.webp\", \"caption\": \"\", \"page\": 12, \"index\": 30, \"width\": 806, \"height\": 404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-031.webp\", \"caption\": \"\", \"page\": 12, \"index\": 31, \"width\": 806, \"height\": 404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-032.webp\", \"caption\": \"\", \"page\": 12, \"index\": 32, \"width\": 1644, \"height\": 824}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-033.webp\", \"caption\": \"\", \"page\": 12, \"index\": 33, \"width\": 1716, \"height\": 856}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-034.webp\", \"caption\": \"\", \"page\": 12, \"index\": 34, \"width\": 802, \"height\": 406}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-035.webp\", \"caption\": \"\", \"page\": 12, \"index\": 35, \"width\": 806, \"height\": 404}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-036.webp\", \"caption\": \"\", \"page\": 12, \"index\": 36, \"width\": 1646, \"height\": 824}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-037.webp\", \"caption\": \"\", \"page\": 12, \"index\": 37, \"width\": 1644, \"height\": 824}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-038.webp\", \"caption\": \"\", \"page\": 13, \"index\": 38, \"width\": 1696, \"height\": 852}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-039.webp\", \"caption\": \"\", \"page\": 13, \"index\": 39, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-040.webp\", \"caption\": \"\", \"page\": 13, \"index\": 40, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-041.webp\", \"caption\": \"\", \"page\": 13, \"index\": 41, \"width\": 1692, \"height\": 846}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-042.webp\", \"caption\": \"\", \"page\": 13, \"index\": 42, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-043.webp\", \"caption\": \"\", \"page\": 13, \"index\": 43, \"width\": 1008, \"height\": 504}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-044.webp\", \"caption\": \"\", \"page\": 15, \"index\": 44, \"width\": 1980, \"height\": 1080}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-045.webp\", \"caption\": \"\", \"page\": 15, \"index\": 45, \"width\": 2048, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-046.webp\", \"caption\": \"\", \"page\": 15, \"index\": 46, \"width\": 868, \"height\": 436}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4cc0a63b0cb101ad14e3132/fig-047.webp\", \"caption\": \"\", \"page\": 15, \"index\": 47, \"width\": 876, \"height\": 444}]"
motivation: 在透视图像上训练的深度基础模型难以泛化到360°全景图像，而全量微调又需要大量全景数据。
method: 提出RePer-360，一种畸变感知的自调制框架，用轻量几何对齐引导模块从ERP与CP两种投影导出调制信号。
result: 在保留透视先验的同时适配全景域，提升了单目全景深度估计性能。
conclusion: 展示了利用自调制复用深度基础模型先验以迁移到新成像域的可行性。
---

## Abstract
Recent depth foundation models trained on perspective im-agery achieve strong performance, yet generalize poorly to 360∘ imagesdue to the substantial geometric discrepancy between perspective andpanoramic domains. Moreover, fully fine-tuning these models typicallyrequires large amounts of panoramic data. To address this issue, wepropose RePer-360, a distortion-aware self-modulation framework formonocular panoramic depth estimation that adapts depth foundationmodels while preserving powerful pretrained perspective priors. Specifi-cally, we design a lightweight geometry-aligned guidance module to derivea modulation signal from two complementary projections (i.e., ERP andCP) and use it to guide the model toward the panoramic domain withoutoverwriting its pretrained perspective knowledge. We further introduce aSelf-Conditioned AdaLN-Zero mechanism that produces pixel-wise scalingfactors to reduce the feature distribution gap between the perspectiveand panoramic domains. In addition, a cubemap-domain consistency lossfurther improves training stability and cross-projection alignment. Byshifting the focus from complementary-projection fusion to panoramic do-main adaptation under preserved pretrained perspective priors, RePer-360surpasses standard fine-tuning methods while using only 1% of the train-ing data. Under the same in-domain training setting, it further achievesan approximately 20% improvement in RMSE. The code is available athttps://github.com/munimo/RePer360.

---

## 论文详细总结（自动生成）

# RePer-360 论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **核心问题**：在透视图像上训练的深度基础模型（如 Depth Anything Models, DAM）虽然性能强大，但在 360° 全景图像上泛化能力显著下降。根本原因在于透视域与全景域之间存在**严重的几何差异**——预训练表征遵循透视域的统计特性，而全景畸变破坏了这种统计一致性。
- **现有方案的两条路径及其局限**：
  - **投影推理-融合范式**（如 MoGe-2、ST²360D、OmniFusion、HRDFuse）：将全景切分为多个透视视图分别推理再融合。缺点是视图间近似独立、未显式建模全局球面几何，且多视图推理带来额外计算开销和延迟。
  - **全景域微调范式**（如 PanDA 使用 LoRA、Depth Anywhere 使用蒸馏）：依赖大规模全景数据，且未显式建模全景畸变，可能**覆盖或损坏**预训练透视先验，导致表征漂移，损害泛化性。
- **关键发现与动机**：作者先尝试"互补投影特征硬融合"（冻结骨干，融合 CP 与 ERP 特征），但仅获得边际提升，假设硬融合扰动了预训练特征统计。由此提出核心观点：**互补投影特征不应被硬融合为新表征，而应作为结构化引导信号，以实现更稳定的域迁移**。

## 2. 方法论

### 核心思想
将全景适配重新表述为**畸变感知、基于引导的域自适应**：不进行直接特征融合，而是通过基于归一化的调制对齐跨域特征分布，在适应全景畸变的同时避免覆盖预训练透视先验。框架遵循"引导—调制—监督"流程。

### 关键技术细节

**（1）Geometry-Aligned Guidance (GAG) 模块**
- 动机：CP 每个面更接近骨干训练分布，提供可靠局部结构但存在边界不连续；ERP 保持连续全景布局、提供稳定全局上下文但畸变更强。二者互补。
- 流程：
  - 将 ERP 特征投影到立方体域得到 F_E2C。
  - 通过仿射归一化进行无参数的通道级统计对齐：计算 F_E2C 与 F_CP 的通道均值 μ 与标准差 σ，将 CP 特征的统计量对齐到 ERP（式 4：F′_CP = σ_E2C · (F_CP − μ_CP)/σ_CP + μ_E2C）。
  - 将校准后的 CP 特征投影回 ERP 域得到 F_aligned。
  - 学习自适应门控 G = Sigmoid(F_g([F_aligned, F_ERP]))，逐像素选择更合适的来源。
  - 最终引导：F_GAG = G ⊙ F_aligned + (I − G) ⊙ F_ERP。
- **重要**：F_GAG 不替换骨干表征，仅用于参数化后续调制。

**（2）Self-Conditioned AdaLN-Zero (SCAdaLN-Zero) 模块**
- 与 DiT 使用外部预定义 1D 条件（时间步/类别标签）不同，本模块使用来自 GAG 的**内部几何推导的 2D 信号**作为自条件。
- 用轻量网络生成调制参数：P = DSC(SiLU(F_GAG))，其中 DSC 为深度可分离卷积；P 沿通道拆分为六组参数：β_attn、γ_attn、g_attn、β_mlp、γ_mlp、g_mlp。
- 调制函数：modulate(F, β, γ) = F ⊙ (1 + γ) + β。
- 在自注意力路径与 FFN 路径中分别用 LayerNorm（无标准可学习仿射参数）+ 调制 + 门控残差连接。
- **零初始化策略**：调制网络最后一层卷积零初始化，使模块初始退化为标准 Transformer 块，保证训练稳定。
- 设计依据：尺度/位移调制比显式特征融合更可控（重加权归一化特征而非替换内容）。

**（3）损失函数**
- **E2C Consistency Loss (ECCLoss)**：动机是 ERP 中极区像素占比过大、信息密度与像素分布失配，导致监督偏向畸变严重区域。做法是将预测与真值深度从 ERP 变换到 CP，采用尺度-平移不变 MAE（SSI-MAE），B 通常取 6（立方体六面）。
- 总监督损失：L_S = L_SILog + L_Grad + λ_E · L_ECC。

## 3. 实验设计

- **数据集**：
  - 域内评估：Matterport3D、Stanford2D3D（真实室内全景）。
  - 零样本评估：仅用 Structured3D 与 Deep360 合成数据训练，在 Matterport3D、Stanford2D3D 及 SUN360 上测试。
- **训练设置**：分辨率 504×1008，评估时上采样至 512×1024，遵循 PanDA 评估协议。
- **Benchmark 与对比方法**：
  - 全景深度方法：BiFuse、UniFuse、BiFuse++、PanoFormer、HRDFuse、Elite360D、Depth Anywhere、SGFormer、PanDA-L / PanDA-L*。
  - 零样本对比：Marigold、DAM v1、DAM v2、PanDA-L。
- **评价指标**：Abs Rel、Sq Rel、RMSE、δ1、δ2、δ3。
- **消融实验**：
  - 架构消融（a–d）：无条件退化版、交叉注意力替代调制、单分支条件（ERP 或 CP）、完整 GAG 条件。
  - ECCLoss 有无对比、注意力类型（PanoAttn vs NormalAttn）对比、UniFuse CEE 融合变体对比。
  - 预训练初始化影响：DAMv2 vs DINOv2。
  - 表征漂移分析（余弦相似度、线性 CKA）与第 4 层特征图可视化。

## 4. 资源与算力

- **GPU**：8 张 NVIDIA RTX A4000。
- **框架与优化器**：PyTorch，Adam 优化器，初始学习率 5×10⁻⁵，其他超参数默认；批大小 1。
- **数据增强**：左右翻转、全景水平旋转、亮度调整。
- **骨干网络**：冻结的 DAM v2（ViT-L），与 PanDA 使用相同预训练权重；模块集成在奇数编号层（层数消融见补充材料）。
- **训练时长**：论文**未明确说明**具体训练时长或迭代次数。
- **数据规模**：本方法使用约 1K（Stanford2D3D）/ 8K（Matterport3D）样本，相比 PanDA-L* 的约 120K 样本仅约 1%。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 2 个真实数据集上的域内定量对比（Table 1）。
  - 2 个数据集上的零样本对比（Table 2）。
  - 1 个数据集（Matterport3D）上的架构消融（Table 3，约 9 个配置）。
  - 预训练初始化对比（Table 4，3 个配置）。
  - 表征漂移分析与特征可视化（Fig. 8）。
  - 定性对比：域内（Fig. 5）、零样本 SUN360（Fig. 6）、自采集真实全景（补充材料）。
- **充分性评价**：
  - **较为充分**：覆盖域内、零样本、消融、可视化、表征漂移等多维度，消融设计系统（条件来源、注入方式、损失、注意力、初始化）。
  - **公平性**：消融实验统一冻结骨干、训练数据与优化策略，较为公平；与 PanDA-L 的公平对比（非预训练版本）单独列出。
  - **客观性**：同时报告 Abs Rel、RMSE、δ 等多指标，且明确指出 PanDA-L* 与 PanDA-L 的训练协议差异，避免误导。
  - 但消融主要在单一数据集（Matterport3D）上进行，跨数据集消融覆盖有限。

## 6. 主要结论与发现

- RePer-360 在 Matterport3D 与 Stanford2D3D 上均达到 SOTA。
- **数据效率突出**：仅用约 1% 训练数据（1K vs 120K）即超越此前 SOTA。
- 在公平对比（非预训练 PanDA-L）下：Matterport3D 上 Abs Rel 提升 12.3%、RMSE 提升 17.3%；Stanford2D3D 上分别提升 34.2% 与 22.3%。
- 零样本设置下（仅用 Structured3D + Deep360 训练）：Stanford2D3D 上 Abs Rel 提升 42.3%、RMSE 提升 14.0%。
- **架构发现**：归一化调制优于显式特征值级混合（交叉注意力）；GAG 条件优于单分支 ERP/CP 条件；硬融合（UniFuse CEE）不足以为投影差距适配。
- ECCLoss 对性能有一致性贡献；替换全景注意力为标准自注意力仅有微小差异，说明框架不紧耦合于特定注意力算子。
- **表征漂移**：交叉注意力引起大幅且不稳定的层级漂移；PanDA 接近骨干；RePer-360 保持高相似度且层间演化平滑一致，即"受控的几何感知适配"。
- 即使用任务无关的 DINOv2 初始化，RePer-360 仍具竞争力，说明不单纯依赖深度预训练初始化。

## 7. 优点

- **范式创新**：将全景适配从"互补投影融合"重新表述为"基于引导的、保先验的域自适应"，思路清晰且具启发性。
- **数据高效**：用 1% 数据超越大规模预训练方法，实际部署价值高。
- **调制优于融合的实证支持**：通过消融、表征漂移与特征可视化多角度验证了归一化调制的优越性，而非仅凭最终指标。
- **模块设计精巧**：
  - GAG 通过统计对齐 + 学习门控实现互补投影的自适应整合，无参数统计对齐降低复杂度。
  - SCAdaLN-Zero 将 DiT 的外部条件推广为内部几何推导的 2D 自条件，并保留零初始化带来的训练稳定性。
- **损失设计有几何依据**：ECCLoss 从 ERP 像素分布与信息密度失配的角度切入，在 CP 域施加一致性约束，动机充分。
- **实验严谨**：明确区分不同训练协议，消融控制变量严格，并公开代码。

## 8. 不足与局限

- **训练时长/算力细节缺失**：未报告训练迭代次数、总训练时长或总 GPU 小时数，复现成本不易评估。
- **消融覆盖范围有限**：架构消融仅在 Matterport3D 上进行，未在 Stanford2D3D 或零样本设置下重复验证。
- **数据域偏窄**：主要聚焦室内数据集（Matterport3D、Stanford2D3D），零样本定性仅在 SUN360 上展示，缺乏室外大规模定量评估。
- **依赖特定骨干与初始化**：主实验基于 DAM v2 ViT-L，虽有 DINOv2 补充实验，但未探索其他深度基础模型（如 Depth Anything v1 之外的架构）的通用性。
- **超参数敏感性未知**：λ_E 等损失权重、模块插入层数的选择依据仅部分在补充材料中说明，正文未充分讨论敏感性。
- **理论分析有限**：对"为何归一化调制优于融合"主要依赖实证与表征相似度分析，缺乏更深入的理论解释。
- **潜在偏差风险**：训练数据量小（1K/8K），虽体现数据效率，但也可能意味着方法对数据分布较为敏感，泛化到极端场景（如大范围室外、动态场景）的能力有待验证。

（完）
