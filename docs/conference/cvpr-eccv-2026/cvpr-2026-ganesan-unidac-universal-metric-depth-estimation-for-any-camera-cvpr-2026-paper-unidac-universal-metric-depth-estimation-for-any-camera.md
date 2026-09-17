---
title: "UniDAC: Universal Metric Depth Estimation for Any Camera"
title_zh: UniDAC：面向任意相机的通用度量深度估计
authors: "Ganesan, Girish Chandar, Guo, Yuliang, Ren, Liu, Liu, Xiaoming"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ganesan_UniDAC_Universal_Metric_Depth_Estimation_for_Any_Camera_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 通用单目度量深度估计与零样本泛化
tldr: 单目度量深度估计在需要精确空间理解的真实应用中至关重要，但已有方法难以跨鱼眼、360度等多样相机类型泛化。本文提出UniDAC框架，通过解耦度量与相机表征，用单一模型实现跨域通用鲁棒性。实验表明该方法无需在训练中引入大视场数据或分域单独建模，即可在多种相机上取得强零样本泛化。该工作推动了度量深度估计在异构相机场景下的统一与实用化。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 2934, \"height\": 1769}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 3005, \"height\": 505}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 3682, \"height\": 1382}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 5, \"index\": 4, \"width\": 1121, \"height\": 929}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 5, \"index\": 5, \"width\": 899, \"height\": 419}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 8, \"index\": 6, \"width\": 437, \"height\": 1201}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 8, \"index\": 7, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 8, \"index\": 8, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 8, \"index\": 9, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 8, \"index\": 10, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 8, \"index\": 11, \"width\": 446, \"height\": 1063}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 8, \"index\": 12, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 8, \"index\": 13, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 8, \"index\": 14, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 8, \"index\": 15, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 8, \"index\": 16, \"width\": 437, \"height\": 647}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 8, \"index\": 17, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 8, \"index\": 18, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 8, \"index\": 19, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 8, \"index\": 20, \"width\": 1539, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 8, \"index\": 21, \"width\": 465, \"height\": 647}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 8, \"index\": 23, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 8, \"index\": 25, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 770, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 439, \"height\": 647}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 8, \"index\": 32, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 8, \"index\": 33, \"width\": 1154, \"height\": 770}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ganesan-unidac-universal-metric-depth-estimation-for-any-camera-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 8, \"index\": 34, \"width\": 1154, \"height\": 770}]"
motivation: 已有单目度量深度估计方法难以跨鱼眼、360度等多样相机类型泛化。
method: 提出UniDAC框架，通过解耦度量与相机表征，用单一模型实现跨相机域的通用鲁棒度量深度。
result: 无需大视场训练数据或分域模型，在多种相机上实现强零样本泛化。
conclusion: 推进了异构相机下度量深度估计的统一与实用化。
---

## Abstract
Monocular metric depth estimation (MMDE) is a core challenge in computer vision, playing a pivotal role in real-world applications that demand accurate spatial understanding. Although prior works have shown promising zero-shot performance in MMDE, they often struggle with generalization across diverse camera types, such as fisheye and 360^\circ cameras. Recent advances have addressed this through unified camera representations or canonical representation spaces, but they require either including large FoV camera data during training or separately trained models for different domains. We propose UniDAC, an MMDE framework that presents universal robustness in all domains and generalizes across diverse cameras using a single model. We achieve this by decoupling metric depth estimation into relative depth prediction and spatially varying scale estimation, enabling robust performance across different domains. We propose a lightweight Depth-Guided Scale Estimation module that upsamples a coarse scale map to high resolution using the relative depth map as guidance to account for local scale variations. Furthermore, we introduce RoPE-\phi, a distortion-aware positional embedding that respects the spatial warping in Equi-Rectangular Projections (ERP) via latitude-aware weighting. UniDAC achieves state of the art (SoTA) in cross-camera generalization by consistently outperforming prior methods across all datasets.

---

## 论文详细总结（自动生成）

# UniDAC：面向任意相机的通用度量深度估计 —— 结构化总结

## 一、核心问题与研究动机

- **任务背景**：单目度量深度估计（Monocular Metric Depth Estimation, MMDE）是 2D 到 3D 视觉的桥梁，对自动驾驶、机器人、AR/VR 等需要精确空间测量的应用至关重要。
- **已有进展**：近年工作通过相机参数条件化（UniDepth）、规范空间映射（Metric3D v2）或显式尺度估计（MoGe-2）实现了较好的零样本 MMDE，但主要针对**透视（pinhole）相机**。
- **核心痛点**：
  - 透视相机训练的模型在**鱼眼、360° 等大视场（large-FoV）相机**上泛化很差。
  - UniK3D 通过球谐角表示统一多相机，但**训练时依赖大视场数据**，且性能受训练相机多样性限制。
  - DAC 通过 ERP 规范空间 + FoV 对齐实现跨相机泛化，但**需要为室内/室外分别训练模型**；其统一模型 DACU 因试图学习单一全局尺度而性能显著下降。
- **本文设问**：能否在不显著扩大模型与数据规模的前提下，用**单一模型**同时覆盖"任意相机几何 + 任意场景域"？
- **核心洞察**：度量深度可解耦为**相对深度（局部、域无关）**与**尺度（全局、域相关）**两部分；二者依赖不同的上下文范围，应分别由编码器的早期特征与晚期全局特征承担。

---

## 二、方法论

### 1. 核心思想：度量深度解耦
- 依据 $D_m = s D_{rel} + t$，将度量深度分解为：
  - **相对深度图** $D_{rel}$：仅依赖局部像素变化（物体形状、边界），域无关；
  - **尺度与偏移** $\{s, t\}$：依赖整幅场景（室内约 10 m、室外约 80 m），域相关。
- 目的：避免模型在室内外差异极大的深度范围之间"混淆"，实现室内外统一建模。

### 2. 相对深度估计
- 输入 ERP 图像 $I \in \mathbb{R}^{H\times W\times 3}$，编码器 $E$ 输出特征划分为早期局部特征 $F_l$ 与末端全局特征 $F_g$。
- 用解码器 $D$ 从 $F_l$ 预测相对深度 $\hat{D}_{rel}$，再做**中值归一化**得到 $D_{rel} = \hat{D}_{rel}/\hat{s}$，$\hat{s} = \mathrm{Median}(\hat{D}_{rel})$，以避免任意尺度干扰后续尺度估计。

### 3. 深度引导的尺度估计（Depth-Guided Scale Estimation, DGSE）
- **动机**：理论上相对深度与度量深度仅差一对 1-D 标量，但实际预测的相对深度存在**空间非均匀的拉伸/压缩**（局部误差、遮挡），单一标量 $s$ 无法补偿（论文图 2 以 Abs.Rel 误差对比了无缩放/中值缩放/深度引导缩放三种情形）。
- **低分辨率尺度图预测**：对 $F_g$ 做自注意力 + 浅层 MLP，得到 $S_r = \mathrm{MLP}(\mathrm{SelfAttn}(F_g)) \in \mathbb{R}^{h\times w}$；偏移量 $t$ 由 $F_g$ 的 CLS token 经浅层 MLP 回归。
- **深度引导上采样（非参数化，几乎零额外开销）**：
  1. 对 $D_{rel}$ 做中值池化（核与步长均为 $r$）得到低分辨率 $D_{rel}^r$；
  2. 对每个像素 $p$，在邻域 $\Omega=\{-1,0,1\}^2$ 上计算距离矩阵 $\Delta[p]=\{|D_{rel}[p]-D_{rel}^r[p_r+\delta p]|\}$；
  3. 对 $-\Delta$ 做 softmax 得到逐像素权重 $W[p]=\mathrm{softmax}(-\Delta[p])\in\mathbb{R}^{H\times W\times 9}$；
  4. 加权求和 $S[p]=W[p,:]^\top \mathcal{N}(S_r,p_r)$，得到高分辨率尺度图 $S$。
- **最终度量深度**：$D_m = S \odot D_{rel} + t$（$\odot$ 为 Hadamard 积）。
- **优势**：尺度图由全局特征产生，但通过相对深度的边界信息路由到高分辨率，使空间一致区域共享一致尺度，且避免转置卷积的算力开销与高维输出的估计困难。

### 4. RoPE-φ：畸变感知位置编码
- 问题：ERP 中相同的像素距离，在球面上对应的**测地距离**随纬度变化——同一纬度上靠近极点的像素实际 3D 间距更小（论文图 5）。
- 测地距离公式：$G(p_1,p_2)=\arccos(\sin\phi_1\sin\phi_2+\cos\phi_1\cos\phi_2\Delta\theta)$；当 $\Delta\phi=0$ 时可近似 $G \propto \cos\phi\,\Delta\theta$。
- 对 2D-RoPE 旋转矩阵施加纬度权重：$R_\phi[n]=R[n]\,w(\phi_n)$，$w(\phi)=\delta+(1-\delta)\cos\phi$，$w\in[\delta,1]$；$\delta=1$ 时退化为标准 2D-RoPE，故后者是 RoPE-φ 的特例。

### 5. 优化目标
- 统一使用 SIlog 损失（可写成 $\sqrt{V[\epsilon_p]+(1-\lambda)E^2[\epsilon_p]}$ 形式）：
  - 相对深度损失 $L_{rel}$：取 $\lambda=1$，即**纯尺度不变**损失；
  - 度量深度损失 $L_m$：取 $\lambda=0.85$，即标准的"尺度不变 + 尺度相关"混合损失。

---

## 三、实验设计

### 训练数据（仅透视图像，1.1M 张）
- **室内**：HM3D（tiny）、Hypersim、Taskonomy（tiny，经 OmniData 提供）。
- **室外**：DDAD、LYFT、Argoverse2（去除前视相机）、A2D2（去除后中相机）。
- 论文描述为"670K 室内 + 780K 室外"，与"合计 1.1M"存在数值不一致（详见"不足"）。

### 测试数据（零样本、跨相机）
- **鱼眼**：ScanNet++（室内）、KITTI-360（室外）；
- **360°**：Pano3D-GV2、Matterport3D（后者仅用于表 2，因在 UniK3D 训练集中而被表 1 排除）。

### 对比方法
- **UniK3D**（球谐角表示，训练含大 FoV 数据，推理不需相机参数）；
- **DAC**：DACI / DACO（分域训练）、DACU（室内外联合训练，作者自行复现以保证公平）；
- **UniDepth**、**Metric3D v2**（引自 DAC 的评测结果）。

### 评测指标
- δ1 ↑（阈值 1.25 的 inlier 比例）、A.Rel ↓（绝对平均相对误差）、RMSE ↓。

### 实现配置
- PyTorch + CUDA；ViT-L 编码器（DINO 预训练）+ DPT 解码器；AdamW（β₁=0.9, β₂=0.999），初始学习率 1e-4，余弦退火至 1/10；120k 迭代，batch size 128；沿用 DAC 的 FoV 对齐、多分辨率采样与 ERP 增强。
- 消融实验使用 ViT-B，训练于 HM3D + KITTI-360。

---

## 四、资源与算力

- 论文**未披露 GPU 型号、数量与训练时长**（仅给出迭代数 120k、batch size 128、优化器与学习率调度等超参数）。
- 训练数据规模约 1.1M 张透视图像（论文自述），模型方面表 1 列出 UniDAC-ViT-L 的规模为 1.45M（该列数值单位标注存疑，与 ViT-L 实际参数量量级不符，疑为排版/单位问题）。
- 消融实验统一用 ViT-B 以降低开销，但同样未报告绝对算力消耗。
- **结论：算力可复现性信息不足**，这是该工作对外部复现与能耗评估的一项明显缺口。

---

## 五、实验数量与充分性

- **主实验 2 组大规模表格**：
  - 表 1：通用域鲁棒性（室内外统一模型 × 3 个数据集：ScanNet++、Pano3D-GV2、KITTI-360）；
  - 表 2：跨相机泛化（对比 DACI/DACO/DACU 等 5 个变体 × 4 个数据集，含 Matterport3D）。
- **消融实验 2 组**：
  - 表 3：尺度估计形式对比（不缩放/不"解耦"、单一标量 $s\in\mathbb{R}$、尺度图 $S\in\mathbb{R}^{H\times W}$）；
  - 表 4：位置编码对比（2D-RoPE vs. RoPE-φ）。
- **定性结果**：图 6 在 ScanNet++、Pano3D-GV2、KITTI-360 上给出 RGB、GT 与预测深度的可视化与 A.Rel 误差图。
- **充分性与公平性评价**：
  - **公平性较好**：作者自行复现了未公开的 DACU，并统一了训练设置；因 Matterport3D 出现在 UniK3D 训练集中，主动将其从表 1 移除；同时明确指出 UniK3D 使用大 FoV 训练数据，与仅用透视图像训练的方法不构成严格对等比较。
  - **充分性有限**：消融仅在 2 个数据集、ViT-B 骨干上进行，且消融数据存在明显室内偏置（HM3D 310K vs. DDAD 80K），结论的外推性受限；缺少对 DGSE 上采样窗口大小、中值池化核 $r$、权重衰减系数 $\delta$ 等关键超参的敏感性分析；缺少与 MoGe-2、UniDepth v2 等较新方法在同协议下的对比；缺少对鱼眼畸变校正/相机标定误差鲁棒性的分析。

---

## 六、主要结论与发现

- **跨相机泛化 SOTA**：UniDAC 在全部测试数据集上一致优于仅用透视图像训练的先前方法，甚至在多数指标上超过使用大 FoV 数据训练的 UniK3D。
  - ScanNet++：δ1 = 0.918（相对 UniK3D 0.651、DACU 0.658 提升约 26%），A.Rel 0.097、RMSE 0.277；
  - Pano3D-GV2：δ1 = 0.768（较 DACU 0.684 提升约 8.4%），接近使用同类 360° 数据训练的 UniK3D（0.785）；
  - KITTI-360：δ1 = 0.836，优于 UniK3D（0.817）约 2%；
  - Matterport3D：δ1 = 0.745，优于 DACU（0.662）。
- **解耦的有效性**：尺度图 $S\in

$\mathbb{R}^{H\times W}$（深度引导、空间可变）优于单一标量 $s\in\mathbb{R}$，而后者又优于不做任何尺度解耦/缩放的基线；这直接验证了"相对深度与尺度分离 + 空间自适应尺度图"的设计必要性——若强行用单一全局尺度统一室内外，模型必须在差异极大的深度范围间折中，导致 DACU 式的性能塌陷。
- **位置编码的有效性**：表 4 表明，以 RoPE-φ 替换标准 2D-RoPE 在鱼眼与 360° 数据上取得一致提升，说明显式建模 ERP 纬度方向测地距离变化、抑制极点附近的虚假邻近关系，对畸变鲁棒性有实质贡献；且 $\delta=1$ 的退化关系保证该模块可与现有 RoPE 实现兼容，几乎不增加推理成本。
- **总体结论**：度量深度的"相对—尺度"解耦使单一模型无需大视场训练数据即可跨相机、跨场景域泛化，在室内外统一设定下同时超过分域训练的 DAC 系列与使用大 FoV 数据训练的 UniK3D。

---

## 七、局限性与未来工作

- **训练数据仍限于透视图像**：虽然本文证明"不必依赖大 FoV 数据"，但这也意味着模型在极端畸变（如鱼眼边缘、双鱼眼拼接缝、非标准投影）下的上界仍受训练相机多样性制约，未探索加入少量大 FoV 数据是否可进一步提升。
- **强依赖 ERP 规范空间与 FoV 对齐**：方法建立在 DAC 的 ERP 重投影管线之上，对相机内参/畸变系数的估计误差、以及非理想标定的鲁棒性缺乏分析。
- **尺度图与偏移的可解释性有限**：$S$ 由全局特征经自注意力产生，$t$ 由 CLS token 回归，但论文未分析二者在室内/室外切换时的行为，也未给出失败案例（如镜面、天空、透明物体）的系统讨论。
- **算力与效率报告缺失**：未报告 GPU 型号、数量、训练时长及推理延迟/显存，削弱了可复现性与部署可行性评估。
- **消融外推性受限**：仅在 ViT-B、HM3D + KITTI-360 的偏室内数据配比上验证，且未对 DGSE 上采样窗口 $\Omega$、中值池化核 $r$、纬度权重下限 $\delta$ 等关键超参做敏感性分析。
- **未与最新方法同协议对比**：缺少 MoGe-2、UniDepth v2 等在统一评测协议下的比较，也缺少视频/时序一致性、动态场景等扩展讨论。

---

## 八、写作与表达评价

- **优点**：
  - 动机链条清晰：从"透视模型在大 FoV 相机失效"→"度量深度可解耦"→"DGSE + RoPE-φ"，逻辑自洽。
  - 图示有说服力：图 2 用三种缩放策略的 Abs.Rel 对比直观说明单一标量的不足；图 5 用球面测地距离示意 ERP 纬度畸变。
  - 公平性意识较强：主动剔除与 UniK3D 训练集重叠的 Matterport3D、自行复现 DACU、明示与 UniK3D 的数据不对等。
- **不足**：
  - 存在数值表述不一致：正文"670K 室内 + 780K 室外"与"合计 1.1M"相互矛盾；表 1 中 UniDAC-ViT-L 规模标注为 1.45M，与 ViT-L 参数量量级明显不符（疑为排版或单位问题）。
  - 部分公式（如 SIlog 损失的两种写法、RoPE-φ 与标准 2D-RoPE 的退化关系）解释偏简，需读者自行推导。
  - 消融章节篇幅较短，超参选择依据说明不足。

---

## 九、总体评价与启示

- **核心贡献**：提出"相对深度（局部、域无关）+ 空间可变尺度图（全局、域相关）"的解耦范式，配合深度引导的尺度上采样与畸变感知的 RoPE-φ，使**单一模型**在**任意相机几何 × 任意场景域**下实现零样本度量深度估计，且训练仅需透视图像。
- **方法论启示**：
  - "解耦 + 路由"的思路可迁移至其他需要跨域统一输出的回归任务（如表面法线、光流、相机内参估计）。
  - 用相对深度作为"几何引导"来上采样低分辨率尺度图，是一种以极低算力代价换取空间自适应性的优雅设计，避免了转置卷积与高维输出回归的困难。
  - 将位置编码与球面几何绑定（RoPE-φ）为 ERP/全景视觉的 Transformer 建模提供了可复用组件。
- **实践价值**：在自动驾驶（鱼眼环视）、机器人（全景感知）、AR/VR（360° 内容）等需要跨相机部署且难以获取大 FoV 训练数据的场景中具有直接应用潜力。
- **待补强方向**：补充算力与效率报告、扩大消融范围与数据集覆盖、引入大 FoV 数据或自监督信号的增量实验、以及对标定误差与极端畸变的鲁棒性分析。

（完）
