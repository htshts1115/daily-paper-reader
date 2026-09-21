---
title: "SD-PSFNet: Sequential and Dynamic Point Spread Function Network for Image Deraining"
title_zh: SD-PSFNet：用于图像去雨的序列动态点扩散函数网络
authors: "Jiayu Wang, Haoyu Bian, Haoran Sun, Shaoning Zeng"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37957/41919"
tags: ["query:cv-render"]
score: 5.0
evidence: 学习式点扩散函数退化建模
tldr: 该文针对雨滴多尺度物理特性复杂且与场景耦合、难以有效去雨的问题，提出SD-PSFNet。方法借鉴多阶段图像复原，引入点扩散函数机制刻画退化过程，用三级级联网络动态评估并细化退化估计，结合顺序特征融合。实验表明该方法能有效提升去雨效果。其价值在于以学习式PSF建模图像退化，这一思路对模糊与散景渲染中的点扩散函数合成具有方法借鉴意义。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37957/fig-001.webp\", \"caption\": \"\", \"page\": 3, \"index\": 1, \"width\": 7872, \"height\": 3464}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37957/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 3055, \"height\": 1166}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37957/fig-003.webp\", \"caption\": \"\", \"page\": 7, \"index\": 3, \"width\": 2846, \"height\": 900}]"
motivation: 雨滴具有复杂多尺度物理特性并与场景耦合，给图像去雨带来挑战。
method: 提出序列动态点扩散函数网络，用三级级联结构结合学习式PSF机制动态刻画雨痕光学退化。
result: 实验表明该方法通过多阶段动态评估与特征融合有效提升去雨复原效果。
conclusion: 该工作以学习式PSF建模退化，对模糊散景中的点扩散函数合成具有方法借鉴价值。
---

## Abstract
Image deraining is crucial for vision applications but is challenged by the complex multi-scale physics of rain and its coupling with scenes. To address this challenge, a novel approach inspired by multi-stage image restoration is proposed, incorporating Point Spread Function (PSF) mechanisms to reveal the image degradation process while combining dynamic physical modeling with sequential feature fusion transfer, named SD-PSFNet. Specifically, SD-PSFNet employs a sequential restoration architecture with three cascaded stages, allowing multiple dynamic evaluations and refinements of the degradation process estimation. The network utilizes components with learned PSF mechanisms to dynamically simulate rain streak optics, enabling effective rain-background separation while progressively enhancing outputs through novel PSF components at each stage. Additionally, SD-PSFNet incorporates adaptive gated fusion for optimal cross-stage feature integration, enabling sequential refinement from coarse rain removal to fine detail restoration. Our model achieves state-of-the-art PSNR/SSIM metrics on Rain100H (33.12dB/0.9371), RealRain-1k-L (42.28dB/0.9872), and RealRain-1k-H (41.08dB/0.9838). In summary, SD-PSFNet demonstrates excellent capability in complex scenes and dense rainfall conditions, providing a new physics-aware approach to image deraining.

---

## 论文详细总结（自动生成）

# SD-PSFNet 论文深度总结

## 1. 核心问题与研究动机

- **任务背景**：图像去雨是底层视觉的基础复原任务，对目标检测、自动驾驶、监控系统等下游应用至关重要。雨天图像存在可见度下降、对比度降低、细节丢失等问题，严重影响视觉处理性能。
- **核心挑战**：雨滴分布具有复杂性、多尺度性，且与背景场景高度耦合，去雨本质上是逆转复杂且空间变化的退化过程。
- **现有方法的不足**：
  - 大多数方法只学习数据到图像的映射关系，**忽视雨滴形成的光学物理属性**，导致无法动态适应不同雨型，缺乏可解释性。
  - Transformer、GAN、扩散模型虽性能优越，但参数量大、计算开销高，难以实时部署。
  - 已有的物理感知方法多依赖**固定先验假设（如静态 PSF 模板）**，难以捕捉雨痕的多尺度分布与雨滴光学差异。
- **整体含义**：论文回归 CNN 架构，提出一种基于**多尺度、数据驱动的动态点扩散函数（PSF）预测**的序列化去雨网络，试图在物理可解释性与计算效率之间取得平衡。

## 2. 方法论

### 2.1 核心思想
- 将 PSF 从**静态预设**转变为**数据驱动可学习**的形式，通过内容自适应的可学习退化模式字典线性组合来近似空间变化的退化函数 K(x, y)。
- 采用受 LSTM 与 MPRNet 启发的**多阶段序列化复原架构**，允许对退化过程进行多次动态评估与细化。

### 2.2 关键技术细节

- **动态 PSF 机制**：将任意空间变化退化函数近似为可学习卷积核字典 {k_j} 的加权组合：K(x,y) ≈ Σ w_j(x,y)·k_j，权重由神经网络从图像特征自适应映射得到，并附加物理约束。

- **多尺度 PSF 头（Multi-Scale PSF Head）**：
  - 用 3×3、5×5、7×7 三种尺度的预测头，分别捕捉高频细节退化、局部与全局均衡信息、宏观低频模式。
  - 流程：对编码器特征做自适应平均池化 → 1×1 卷积映射 → Softmax 归一化为概率分布 → 通道维拼接 → 通道注意力（CAB）融合 → 1×1 卷积投影为 K_c×K×K 的多通道 PSF 表示。
  - 强制**空间归一化约束**（每个通道元素和为 1），模拟能量守恒，防止背景像素被不合理放大或衰减。

- **PSF Block（PSFB）**：
  - **PSF 通道压缩器（PSF Channel Reducer）**：将多通道 PSF 压缩为单通道表示，降低计算复杂度，同时保持 PSF 物理属性（归一化）。
  - **PSF 感知注意力（PSF-Aware Attention）**：双路径机制——通道调制（生成 γ、β 参数，x_mod = x ⊙ γ + β）与空间注意力（上采样单通道 PSF 生成空间权重），实现物理引导的特征增强。

- **序列设计与增强特征融合**：
  - 跨阶段门控机制：F(t) = G_θ(F_current, F_prev) ⊙ F_current + (1 − G_θ) ⊙ F_prev，门控权重由当前与历史特征学习得到。
  - 在阶段输入、编码器层级、增强跨阶段特征融合（CSFF）三处使用双重自适应门控，保留低层细节与高层语义。

- **整体架构**：由 Stage In、多个 Stage Mid、Original Resolution Stage（ORStage）组成，各阶段输出中间复原结果 I_i、跨尺度特征 O_i、特征映射 H_i。

- **损失函数**：混合损失 = Charbonnier 损失（像素监督）+ 边缘感知损失（高频细节）+ 频域损失（对齐 PSF 特性），权重 α₁=0.05、α₂=0.01。

## 3. 实验设计

- **数据集 / 场景**：
  - 合成数据集：Rain100L、Rain100H
  - 真实数据集：RealRain-1K-L、RealRain-1K-H
  - 泛化实验额外使用：SPA-data、Rain13K、Rain200L
- **Benchmark**：PSNR 与 SSIM（训练/验证时 PSNR 仅在 Y 通道计算，测试时在 RGB 空间计算）。
- **对比方法**：
  - CNN 类：DerainNet、DDN、PreNet、SPANet、MPRNet、NAFNet、HINet、M3SNet
  - Transformer 类：Restormer、PromptIR、DRSFormer、NeRD-Rain-S
  - 因采用监督训练，排除与无监督 GAN 类去雨方法的对比。

## 4. 资源与算力

- **GPU**：单张 NVIDIA GeForce RTX 4090。
- **训练配置**：PyTorch 框架；τ=3 阶段，PSF 通道 K_c=40；主结果训练 2000 epochs（消融 τ 实验为 1000 epochs）；AdamW 优化器，初始学习率 1e-4，3-epoch 线性 warmup + 余弦退火至 1e-6；FP16 混合精度训练；梯度裁剪（max norm 2.0）。
- **训练细节**：图像裁剪为 128×128 块，ImageNet 均值方差归一化，随机翻转与几何变换增强。
- **未明确说明**：论文**未报告具体训练时长**（小时/天数），也未说明是否进行多次重复实验取平均。

## 5. 实验数量与充分性

- **主对比实验（表 1）**：在 4 个数据集上与 12 种 SOTA 方法对比，覆盖 CNN 与 Transformer 两类。
- **跨数据集评估（表 2）**：4 个训练集 × 5 个测试集的迁移矩阵，共 20 组实验。
- **泛化对比（表 3）**：合成到真实场景的泛化，对比 MPRNet、Restormer、NeRD-Rain-S。
- **消融实验（表 4）**：7 种递增配置（Baseline、Patch Split、Gate、层间更新、增强 CSFF、1 通道 PSF、40 通道 PSF），逐步验证各模块贡献。
- **参数 τ 消融（表 5）**：τ=0/1/2/3 共 4 组，同时报告参数量与 MACs。
- **定性对比**：图 2（Rain100L/H 视觉对比）、图 3（不同阶段复原进展）。
- **充分性评价**：
  - **优点**：消融设计**逐模块增量式**，清晰剥离各组件贡献；跨数据集迁移矩阵较全面；参数量与计算量均有报告。
  - **待商榷**：未提及多次运行取均值或方差，统计显著性未验证；部分数据集（如 Rain100L）上并非第一，未深入分析原因；PSF 通道数 K_c 等超参数缺乏敏感性分析。

## 6. 主要结论与发现

- 在 Rain100H（33.12dB/0.9371）、RealRain-1k-L（42.28dB/0.9872）、RealRain-1k-H（41.08dB/0.9838）上取得 SOTA。
- 相比基线 MPRNet，在 RealRain-1k-L 上 PSNR 提升 **5.04dB（13.5%）**。
- CNN 架构可媲美甚至超越部分 Transformer 方法（Restormer、PromptIR），同时保持效率优势。
- 各模块增量贡献：门控机制 +1.45dB、层级间更新 +1.76dB、增强 CSFF +1.0dB、1 通道 PSF +0.22dB。
- τ 从 0 增至 3，PSNR 从 40.81dB 提升至 41.54dB，代价是参数量从 3.64M 增至 9.63M。
- 合成与真实雨场景之间存在显著域间差距，跨域泛化仍是数据驱动方法的根本局限。

## 7. 优点

- **物理可解释性强**：将 PSF 从静态先验升级为数据驱动的动态多尺度预测，兼顾物理约束（能量守恒归一化）与自适应能力。
- **架构设计精巧**：多尺度 PSF 头 + 双路径 PSF 感知注意力 + 双重门控 CSFF，形成从粗去雨到细粒度细节复原的渐进式流程。
- **效率与性能平衡**：9.63M 参数、244.83G MACs，在 CNN 框架下达到接近或超越大参数 Transformer 的效果。
- **实验体系完整**：主对比、跨域迁移、泛化对比、多组消融（模块级 + 超参数级）层层递进。
- **损失函数设计合理**：像素、边缘、频域三域联合监督，与 PSF 物理特性对齐。

## 8. 不足与局限

- **算力与可复现性**：仅使用单张 RTX 4090，未报告训练时长；未见多次重复实验与方差报告，统计稳健性存疑。
- **实验覆盖偏差**：
  - 在 Rain100L 上未达最优（NeRD-Rain-S 更优），论文未深入分析。
  - 未与无监督/半监督方法对比（虽有说明，但可能遗漏部分适用场景）。
  - 缺少 PSF 通道数、阶段数之外其他关键超参（如字典大小、损失权重）的敏感性分析。
- **泛化局限**：合成与真实域间差距显著，跨域性能大幅下降（如 RealRain-1k-L 训练后测试 Rain100H 仅 14.34dB），说明模型学到的是数据集特定特征而非通用去雨原理。
- **应用限制**：论文强调实时性优势，但未给出实际推理速度（FPS）或延迟数据；视频/动态雨场景未涉及。
- **物理建模的近似性**：用有限字典近似任意空间变化退化函数，其覆盖能力与理论边界未被充分论证。

（完）
