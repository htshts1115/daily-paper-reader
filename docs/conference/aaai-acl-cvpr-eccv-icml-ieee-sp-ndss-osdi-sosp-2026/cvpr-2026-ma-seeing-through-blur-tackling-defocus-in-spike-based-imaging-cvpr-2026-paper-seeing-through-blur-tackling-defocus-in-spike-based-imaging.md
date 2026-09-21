---
title: "Seeing Through Blur: Tackling Defocus in Spike-Based Imaging"
title_zh: 穿透模糊：解决脉冲成像中的散焦问题
authors: "Ma, Xiantao, Dong, Siwei, Zhu, Lin, Wang, Lizhi, Huang, Hua"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_Seeing_Through_Blur_Tackling_Defocus_in_Spike-Based_Imaging_CVPR_2026_paper.pdf"
tags: ["query:neural-bokeh"]
score: 5.0
evidence: 用薄透镜近似建模散焦形成
tldr: 脉冲相机重建中运动模糊与噪声已有研究，但浅景深或镜头调节延迟导致的散焦模糊仍未被充分探索。该文提出DeSpike，首个面向脉冲相机的端到端散焦去除框架，先用物理启发的薄透镜近似显式建模散焦形成过程以模拟脉冲响应，再结合多时间尺度处理进行复原。实验证明其在真实散焦场景下的有效性。其价值在于将散焦物理建模引入脉冲成像，但目标是去模糊而非散景渲染。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 4, \"index\": 1, \"width\": 443, \"height\": 467}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 520, \"height\": 414}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 656, \"height\": 419}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 656, \"height\": 419}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 656, \"height\": 419}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 5, \"index\": 6, \"width\": 567, \"height\": 230}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 802, \"height\": 497}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 801, \"height\": 498}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 6, \"index\": 9, \"width\": 800, \"height\": 498}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 803, \"height\": 498}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 802, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 799, \"height\": 498}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 800, \"height\": 497}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 987, \"height\": 615}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 987, \"height\": 613}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 984, \"height\": 615}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 6, \"index\": 17, \"width\": 984, \"height\": 612}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 6, \"index\": 18, \"width\": 980, \"height\": 611}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 796, \"height\": 499}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 798, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 801, \"height\": 499}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 6, \"index\": 22, \"width\": 801, \"height\": 499}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 6, \"index\": 23, \"width\": 984, \"height\": 613}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 6, \"index\": 24, \"width\": 802, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 6, \"index\": 25, \"width\": 800, \"height\": 496}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 6, \"index\": 26, \"width\": 985, \"height\": 614}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 6, \"index\": 27, \"width\": 984, \"height\": 616}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 6, \"index\": 28, \"width\": 800, \"height\": 498}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 6, \"index\": 29, \"width\": 801, \"height\": 499}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 6, \"index\": 30, \"width\": 800, \"height\": 498}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-seeing-through-blur-tackling-defocus-in-spike-based-imaging-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 539, \"height\": 484}]"
motivation: 脉冲相机成像中由浅景深或镜头调节延迟引起的散焦模糊尚未被充分研究，却影响自动驾驶等实际应用。
method: 提出DeSpike，用物理启发的薄透镜近似显式建模散焦形成过程，并结合多时间尺度处理实现端到端散焦去除。
result: 实验表明该方法能有效建模并去除脉冲成像中的散焦模糊，提升重建质量。
conclusion: 该工作将散焦物理建模引入脉冲相机复原，聚焦去模糊而非虚化渲染，方向相关但目标不同。
---

## Abstract
Spike cameras are a novel class of neuromorphic vision sensors that capture scene dynamics with ultra-high temporal resolution via spike planes. While recent methods have addressed motion blur and noise in spike-based reconstruction, defocus blur caused by shallow depth of field or lens adjustment delays remains a critical yet underexplored issue in real-world applications such as autonomous driving. In this work, we present DeSpike, the first end-to-end defocus removal framework specifically designed for spike cameras. Our method begins by explicitly modeling the defocus formation process using a physics-inspired thin-lens approximation to simulate spike responses under optical blur. Guided by this formulation, DeSpike employs multi-temporal-scale integrate-and-fire (IF) neurons to compensate for FPN and extract defocus-aware features from spike streams. These features are then processed by a physics-informed deblurring module constructed from learnable discrete PSF priors. To address spatially variant blur, we introduce a Transformer-based fusion mechanism that adaptively weighs multi-scale deblurring results through attention across defocus levels. Finally, a coarse-to-fine iterative refinement stage combines spike features and PSF priors for progressive restoration. Extensive experiments on both synthetic and real-world defocused spike datasets demonstrate that our method achieves superior performance over state-of-the-art deblurring approaches in terms of structural fidelity, perceptual sharpness, and contrast, setting a new benchmark for defocus-aware spike-based image reconstruction.

---

## 论文详细总结（自动生成）

# 论文总结：Seeing Through Blur: Tackling Defocus in Spike-Based Imaging（DeSpike）

## 1. 核心问题与整体含义

- **研究背景**：脉冲相机（Spike Camera）是一类神经形态视觉传感器，通过 Integrate-and-Fire（IF）机制以极高时间分辨率（最高约 40,000 Hz）输出脉冲平面（spike planes），在自动驾驶、机器人、高速动态场景重建等任务中具有潜力。
- **已有研究的空白**：现有脉冲相机重建工作主要处理**运动模糊**与**传感器噪声**；而由浅景深或镜头调焦延迟引起的**散焦模糊（defocus blur）**仍未被充分探索。
- **散焦的特殊性**：与运动模糊不同，散焦属于**光学层面的空间扩散**，会改变光子到达传感器的空间分布，进而改变脉冲发放行为——局部光子密度下降，导致脉冲延迟甚至缺失。
- **现有散焦相关方法的局限**：已有脉冲相机自动对焦方法多依赖手工指标或迭代优化，且本质上是“预防式”的，无法从**已经散焦的脉冲流**中恢复信息。
- **整体含义**：论文提出 **DeSpike**，声称是首个面向脉冲相机的端到端散焦去除与图像重建框架，为散焦感知的脉冲成像重建建立新基准。

## 2. 方法论

### 2.1 核心思想

- 从物理层面显式建模散焦如何影响脉冲采样，再以该模型指导网络设计：**多时间尺度 IF 神经元提取散焦感知特征 + 可学习离散 PSF 先验去模糊 + Transformer 多尺度融合 + 由粗到细迭代精炼**。
- 目标是从散焦脉冲流中直接重建清晰强度图像，而非仅做自动对焦或后处理去模糊。

### 2.2 物理建模

- 采用**薄透镜近似**：由薄透镜方程 \(1/f = 1/u + 1/v\) 推导弥散圆（CoC）半径 \(r = \frac{D}{2}\cdot\frac{\Delta v}{v}\)。
- 用二维高斯核近似 PSF：\(G(x,y;\sigma)=\frac{1}{2\pi\sigma^2}\exp(-\frac{x^2-y^2}{2\sigma^2})\)（原文公式形式如此）。
- 散焦图像强度建模为清晰图像与 PSF 的卷积：\(I_{\text{blur}} = I * G\)。
- 散焦脉冲发放模型：\(S(x,y,t)=1\) 当且仅当 \(\int_{t_n}^{t}\eta\cdot(I*G)(x,y,\tau)d\tau \ge \theta\)，否则为 0。
- **关键推论**：散焦降低单像素有效强度，减缓积分速度，导致脉冲延迟或缺失。

### 2.3 散焦脉冲流的时空特性分析

论文指出三种机制：
- **局部积分失衡**：PSF 作为空间低通滤波，重新分配局部能量，导致像素间积分速率非均匀。
- **非单调时间扰动**：部分脉冲因局部衰减而延迟，部分因邻域能量流入而提前，破坏时间顺序一致性。
- **结构依赖的时间扭曲**：高梯度边缘与平坦区域的时间偏移方向不同，造成时间剪切与空间特征错位。

### 2.4 网络架构

- **多时间尺度神经元积分（Multi-Temporal-Scale Neuronal Integration）**
  - 使用非脉冲神经元（可微膜积分）在多个时间窗口 \(\{T_1,\dots,T_n\}\) 上累积脉冲输入，\(F_i = SN(S(T_i))\)。
  - 文中设置 \(n=5\)，\(T_i\) 分别为 64、96、128、160、192。
  - 在膜电位更新中嵌入 **FPN 校正**：\(V(t)=V(t-1)+\gamma(x,y)\cdot S(t)\)，其中 \(\gamma(x,y)=R(x_m,y_m)/R(x,y)\)，通过均匀光场景标定得到。
- **物理启发离散 PSF 先验**
  - 构建一组可学习卷积核 \(\{k_1,\dots,k_m\}\)，初始化为不同 \(\sigma_j\) 的高斯核。
  - 对每个时间特征图做卷积：\(D_{i,j}=k_j * F_i\)，得到不同散焦程度下的去模糊候选。
- **多尺度迭代精炼（Multi-Scale Iterative Refinement）**
  - 将特征下采样到多个空间分辨率，与离散核卷积，并通过 Transformer 融合模块与上一阶段重建结果聚合：
    \(Rec_j = M(T(F), Rec_{j-1}\uparrow \otimes \sum_{p=1}^{G} k_p * F)\)，\(j=1,2,3\)。
- **多尺度损失**
  - 总损失：\(L=\lambda_1\sum_{i=1}^{N_t}\sum_{s=1}^{N_s}\beta_{i,s}L_{i,s}^{MSE}+\lambda_2 L_{FFT}+\lambda_3 L_{LPIPS}\)。
  - \(N_t=5\)，\(N_s=3\)；\(\beta_1\sim\beta_5=0.1,0.3,0.5,0.7,1.0\)；\(\lambda_1,\lambda_2,\lambda_3=1,0.2,0.2\)。
  - LPIPS 与 FFT 损失仅施加于最终输出（最粗空间尺度）。

## 3. 实验设计

### 3.1 数据集与场景

- **模拟数据**：基于 **DPDD 数据集**生成散焦脉冲序列与对应清晰 GT。训练集 350 对，测试集 32 对。
- **真实数据**：使用脉冲相机额外采集 **75 个真实散焦脉冲序列**。
- **额外场景实验**：
  - 不同焦距距离（焦平面前、焦平面附近、焦平面后）。
  - 不同时间窗口长度（200、64、32 时间步）。
  - 动态场景（高速驾驶、玩偶跳舞）。

### 3.2 评价指标

- **模拟数据**：PSNR、SSIM、LPIPS。
- **真实数据**：Contrast（对比度）与 RankIQA（无参考图像质量评估）。

### 3.3 对比方法

- 以 TFP、TFI 两种脉冲重建方法作为前端，分别接 GKMNet、NRKNet 去模糊模型：
  - TFI-GKMNet、TFI-NRKNet、TFP-GKMNet、TFP-NRKNet。
- 以 RSIR、Spk2ImgNet 作为重建前端，接 GKMNet、NRKNet：
  - RSIR-GKMNet、Spk2ImgNet-GKMNet、RSIR-NRKNet、Spk2ImgNet-NRKNet。
- 上述部分方法还提供了在模拟数据集上**重新训练**的版本（带 * 号），如 TFI-GKMNet*、TFP-NRKNet*、RSIR-GKMNet* 等。
- 表 1 共列出 **16 个对比组合 + 本文方法**。

## 4. 资源与算力

- 文中明确提到：
  - **GPU**：单张 **NVIDIA GeForce RTX 4090**。
  - **Batch size**：2。
  - **训练轮数**：2,000 epochs。
  - **学习率**：初始 1e-4，每 500 epochs 衰减 0.8。
- **未明确说明**：
  - 总训练时长（小时/天）。
  - GPU 数量虽写“single”，但未说明是否使用多卡并行或分布式训练。
  - 模型参数量、推理速度、显存占用等效率指标均未报告。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 模拟数据定量对比：32 个测试样本，17 种方法（含本文）。
  - 真实数据定量对比：75 个序列，同样多方法。
  - 消融实验：5 组（去掉多时间尺度 MTS、去掉多空间尺度 MSS、去掉 FPN 补偿 NC、去掉 Transformer、去掉物理核模块）。
  - 不同焦距实验：3 种焦平面位置。
  - 不同时间窗口实验：200、64、32 三种设置。
  - 定性对比：模拟数据、真实静态场景、真实动态场景、不同焦距、不同时间窗口。
- **充分性评价**：
  - 消融较完整，覆盖了核心模块。
  - 对比方法数量较多，且包含重训练版本，增强了公平性。
  - 但模拟数据仅基于 **DPDD 一个数据集**，场景多样性有限。
  - 真实数据无 GT，只能使用无参考指标，定量评估的客观性受限。
  - 未报告统计显著性检验或多次运行的方差。

## 6. 主要结论与发现

- DeSpike 在模拟数据上取得 **PSNR 18.94、SSIM 0.57、LPIPS 0.25**，在 PSNR 和 LPIPS 上优于所有对比方法。
- 在真实数据上取得 **RankIQA 4.74、Contrast 0.15**，在所有指标上最优。
- SSIM 略低于 GKMNet 的 TFP 去模糊结果，但作者认为整体优势仍然显著。
- 在焦平面前、附近、后三种散焦距离下均能稳定恢复纹理结构。
- 在较短时间窗口（64、32）下性能有所下降，但仍优于对比方法。
- 消融表明：
  - 去掉多时间尺度设计性能下降明显。
  - 去掉多尺度迭代精炼性能下降。
  - 去掉 FPN 补偿性能下降显著。
  - 去掉 Transformer 模块性能下降最大。
  - 去掉物理核模块性能下降，验证物理先验有效性。

## 7. 优点

- **问题新颖**：首次系统性地将散焦问题引入脉冲相机重建，填补了该方向空白。
- **物理与网络结合紧密**：从薄透镜模型、CoC、高斯 PSF 到 IF 脉冲发放，建立了较完整的物理退化模型，并用于指导网络设计。
- **架构设计有针对性**：
  - 多时间尺度 IF 神经元对应散焦引起的脉冲延迟/提前。
  - 可学习离散 PSF 核对应不同散焦程度。
  - Transformer 融合对应空间非均匀散焦。
  - 由粗到细迭代对应渐进恢复。
- **工程细节考虑较全**：将 FPN 校正嵌入膜电位更新，提升真实场景鲁棒性。
- **实验覆盖较广**：模拟与真实、静态与动态、不同焦距、不同时间窗口、消融实验均有涉及。
- **对比基线丰富**：不仅比较端到端方法，还比较了“先重建后去模糊”的多种流水线组合，并重训练部分方法。

## 8. 不足与局限

- **真实数据评估受限**：真实场景无清晰 GT，只能依赖 RankIQA 和 Contrast 等无参考指标，难以全面反映结构保真度。
- **SSIM 并非最优**：在模拟数据上 SSIM 低于 GKMNet 的 TFP 去模糊结果，说明结构相似性方面仍有提升空间。
- **模拟数据单一**：仅基于 DPDD 数据集生成散焦脉冲，未在更多样化数据集或不同传感器参数下验证泛化性。
- **PSF 假设较强**：采用高斯 PSF 近似，对非高斯、非均匀或复杂镜头像差散焦的适用性未充分讨论。
- **效率信息缺失**：未报告参数量、FLOPs、推理速度、训练总时长，难以评估实际部署可行性。
- **对比公平性存在一定疑问**：
  - 部分对比方法是“TFP/TFI + 去模糊”的两阶段流水线，与端到端 DeSpike 的任务设定不完全对等。
  - 带 * 的重训练版本与原始版本混排，训练配置是否完全一致未详细说明。
- **动态散焦建模有限**：论文关注静态散焦或运动诱导散焦，但对焦平面快速变化、变焦过程中的连续散焦动态建模讨论较少。
- **应用限制**：方法依赖脉冲相机硬件与标定 FPN 矩阵，在未标定或硬件差异较大的设备上可能性能下降。

（完）
