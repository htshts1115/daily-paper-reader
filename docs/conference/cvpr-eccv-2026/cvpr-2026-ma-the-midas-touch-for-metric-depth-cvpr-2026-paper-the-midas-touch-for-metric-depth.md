---
title: The Midas Touch for Metric Depth
title_zh: 度量深度的点金之笔
authors: "Ma, Yu, Guo, Zizhan, Xiong, Zuyi, Zhang, Haoran, Feng, Yi, Zhao, Hongbo, Wang, Hanli, Fan, Rui"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Ma_The_Midas_Touch_for_Metric_Depth_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 用稀疏3D数据将相对深度转为度量深度
tldr: 相对深度估计虽泛化良好，却因缺乏度量尺度、局部不一致与计算效率低而难以实用。本文提出MTD，用极稀疏3D数据将相对深度转换为度量深度：先经稀疏图优化做分段尺度恢复，再用不连续感知测地代价进行逐像素精修。方法可解释、轻量且泛化性强，在深度补全与估计任务上显著超越既有方法，推动相对深度落地应用。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 3, \"index\": 1, \"width\": 785, \"height\": 353}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 785, \"height\": 353}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 3, \"index\": 3, \"width\": 488, \"height\": 295}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 3, \"index\": 4, \"width\": 488, \"height\": 295}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 3, \"index\": 5, \"width\": 782, \"height\": 353}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 3, \"index\": 6, \"width\": 782, \"height\": 353}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 3, \"index\": 7, \"width\": 1564, \"height\": 283}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 3, \"index\": 8, \"width\": 1564, \"height\": 283}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 8, \"index\": 9, \"width\": 626, \"height\": 469}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-ma-the-midas-touch-for-metric-depth-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 8, \"index\": 10, \"width\": 626, \"height\": 469}]"
motivation: 相对深度泛化好却缺少度量尺度、存在局部不一致且计算效率低，限制其实用性。
method: 用极稀疏3D数据，经稀疏图优化分段恢复尺度，再用不连续感知测地代价逐像素精修。
result: 在深度补全与估计任务上大幅提升精度，且方法可解释、轻量、泛化强。
conclusion: 为相对深度向度量深度转换提供可解释且高效的通用框架。
---

## Abstract
Recent advances have markedly improved the cross-scene generalization of relative depth estimation, yet its practical applicability remains limited by the absence of metric scale, local inconsistencies, and low computational efficiency. To address these issues, we present Midas Touch for Depth (MTD), a mathematically interpretable approach that converts relative depth into metric depth using only extremely sparse 3D data. To eliminate local scale inconsistencies, it applies a segment-wise recovery strategy via sparse graph optimization, followed by a pixel-wise refinement strategy using a discontinuity-aware geodesic cost. MTD exhibits strong generalization and achieves substantial accuracy improvements over previous depth completion and depth estimation methods. Moreover, its lightweight, plug-and-play design facilitates deployment and integration on diverse downstream 3D tasks.

---

## 论文详细总结（自动生成）

# 《The Midas Touch for Metric Depth》论文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：以 MiDaS、DepthAnything 系列为代表的相对深度估计基础模型在跨场景泛化（zero-shot）上取得显著进展，但其实际应用仍受三大限制：
  - **缺乏度量尺度（scale ambiguity）**：输出仅为相对深度，无法直接用于需要绝对尺度的下游任务；
  - **局部尺度不一致（local inconsistencies）**：不同实例或区域存在各自的尺度比与偏移，单一全局重缩放无法适配；
  - **计算效率低**：大参数量与推理延迟限制部署。
- **既有方案的不足**：
  - 全局最小二乘尺度恢复精度有限，无法处理局部变化；
  - 网络化方法（如 BP-Net、DMD 3C）需域内大规模训练，泛化性差、成本高。
- **整体含义**：论文提出 **MTD（Midas Touch for Depth）**，一种**非参数、可数学解释、无需微调**的通用范式，仅用极稀疏的 3D 数据（称"3D seeds"）即可将相对深度高效、准确地转化为度量深度，且具备即插即用、轻量化的特点，可服务 SLAM、占用预测、多视图立体等下游 3D 任务。

## 2. 方法论

### 2.1 核心思想
- 采用**由粗到细（coarse-to-fine）**的两阶段管线：先用**分段（segment-wise）尺度恢复**消除局部尺度不一致，再用**逐像素（pixel-wise）精修**补偿残余误差。
- 不微调深度基础模型，避免性能退化，保持可解释性与高效率。

### 2.2 关键技术细节

**（a）分段尺度恢复（Segment-Wise Recovery）**

- **逐段标定（Per-Segment Calibration）**：
  - 对彩色图 I 做超像素分割得到段集合 $S=\{S_i\}$，将 3D seeds $X$ 投影到图像平面；
  - 对含投影 seed 的段 $i\in Q$，设 $X_i=\{X_j^i\}$，每个 seed 通过单调双射提供标量代理 $\xi_j^i$（等价于深度 $z_j^i$）；
  - 对 seed 像素处的相对深度 $d_j^i$，估计每段的标定函数 $g_i: d \mapsto \xi$，通过对齐 $\{d_j^i\}$ 与 $\{\xi_j^i\}$ 的经验分布获得（最小二乘或中值匹配）；参数存入查找表以便并行传播。

- **稀疏图优化（Sparse Graph Optimization）**：
  - 构造超像素图 $G=(V,E)$，顶点为段，边权 $w_{ij}$ 由质心距离的衰减核定义，并用基于中值的自适应尺度参数归一化；
  - 每个节点仅保留 $N$ 个最近邻以稀疏化，降低内存与计算量；
  - 求解图正则化二次问题：
    $$\min_{\{\theta_i\}} \sum_{i\in Q}\|\theta_i-\hat\theta_i\|^2 + \sum_{(i,j)\in E} w_{ij}\|\theta_i-\theta_j\|^2$$
    即在保留有 seed 段锚定的同时，促使相邻段共享相似的传输参数；
  - 采用**闭式近似**高效求解，将可靠标定从 $Q$ 传播至无 seed 段，再提升回图像域：$\xi(p)=g_i(d(p))$。

**（b）逐像素精修（Pixel-Wise Refinement）**

- **不连续感知测地代价**：
  - 定义一阶余项 $R(p,q) = z(q)-z(p)-\frac{1}{2}(\nabla z(p)+\nabla z(q))^\top(q-p)$，该余项**反对称**（消除方向偏置，仿射 $z$ 时为零）；
  - 命题 1 证明存在轴平行折线路径 $L_{p\to q}$ 使 $|R(p,q)| \le \int_{L_{p\to q}} \phi\, ds$，其中 $\phi = \sqrt{z_{uu}^2+z_{vv}^2}$；
  - 定义**不连续感知测地代价** $d_\phi(p,q)=\inf_{L\in\mathcal{L}_{p\to q}}\int_L \phi\, ds$，即共形黎曼度量 $\phi^2 I_2$ 下的测地距离；
  - 离散化后用黎曼和近似路径代价，深度不连续处 $\phi$ 很大，跨边界路径代价高，从而**限制深度传播在可靠空间范围内**。

- **动态规划（Dynamic Programming via Path Integrals）**：
  - 将测地代价递推为动态规划代价函数：
    $$d_\phi(p_0,p_K) \le \inf(W(p_{K-1}\to p_K)) + d_\phi(p_0,p_{K-1})$$
  - 初始化：可靠 seed 像素代价设最小值；
  - 更新式（凸组合形式，步长 $1/(k+1)$）：
    $$z^{(k+1)}(p)=\left(1-\frac{1}{k+1}\right)z^{(k)}(p)+\frac{1}{k+1}\hat z^{(k)}(p\mid q,\Delta p)$$
    其中 $\hat z^{(k)}(p\mid q,\Delta p)=\alpha^{(k)}(q)^\top\Psi(\Delta p)$，$\Psi$ 为阶跃域上的基函数；
  - 该方案**扩展了有效感受野**，超越局部邻域交互。

**（c）计算效率改进**

- 通过**知识蒸馏**压缩深度基础模型：以 DepthAnythingV2 为教师，TinyViT / EfficientViT 为学生骨干，采用特征蒸馏与 logit 蒸馏目标；蒸馏数据来自 VKITTI2、Hypersim、TartanAir、SA-1B。

## 3. 实验设计

### 3.1 数据集与场景
- **零样本泛化评测**：nuScenes、DDAD、Make3D、DIODE、ETH3D、ScanNet、VOID(1500)、SUN-RGBD、HAMMER、IBims-1、KITTI、NYU-Depth V2；
- **蒸馏数据**：VKITTI2、Hypersim、TartanAir、SA-1B；
- **规避重叠**：KITTI 与 NYUv2 被排除在零样本评测之外，避免训练-测试重叠。

### 3.2 Benchmark 与评价指标
- 指标：RMSE、MAE、AbsRel、SqRel、$\delta_i$（阈值 $1.25^i$）、SI log；
- 深度补全对比方法：CFormer、LRRU、BP-Net、DMD 3C、PromptDA、Marigold-DC；
- 深度估计对比方法：MiDaS、LeReS、DPT、Depth Pro、DepthAnythingV2、Marigold、GeoWizard、Lotus、DepthMaster、Metric3Dv2、UniDepthV2；
- 3D 数据采样：每场景仅使用 **1.0%–1.5%** 的可用 3D 数据（KITTI 用官方稀疏数据）。

### 3.3 下游应用验证
- 深度矫正（Intel RealSense D455 + Livox MID-70 作为 GT）；
- 多视图立体（VGGT 后端）；
- SLAM（KITTI Odometry，Droid 基线）；
- 占用预测（KITTI-360，BTS 等基线）。

## 4. 资源与算力

- **明确提到的硬件**：
  - 推理评测：单张 **NVIDIA RTX 3090**（480×640 输入分辨率）；
  - 嵌入式加速评测：**NVIDIA Jetson AGX Orin** 平台（经 TensorRT 与多线程加速）；
- **未明确说明的内容**：
  - 论文**未给出**知识蒸馏训练所用的 GPU 型号、数量与训练时长；
  - 也未报告模型训练总能耗或总机时。
- 文中仅给出后端开销数据：在 RTX 3090 上，MTD 后端仅需 **1.9 ms**，显存 < 1.8 GB，GPU 利用率 < 4%。

## 5. 实验数量与充分性

- **实验组数概览**：
  - **表 1**：深度补全零样本对比，覆盖 10 个数据集（nuScenes/DDAD/Make3D/DIODE/ETH3D/ScanNet/VOID1500/SUN-RGBD/HAMMER/IBims-1），对比 6 种 SoTA；
  - **表 2**：深度估计对比，覆盖 KITTI/NYUv2/ETH3D/ScanNet/DIODE，涉及 4 类相对深度方法 + 3 类扩散方法 + 2 类度量深度方法，每种分别给出"原版"与"+Ours"两行；
  - **表 3**：分段恢复与像素精修的统一消融（KITTI 户外 + VOID 室内），涵盖标定策略（中值/最小二乘/逆深度域）、图优化（全局/图基）、测地代价（w/o $d_\phi$/B-spline/多项式/k=3/5）；
  - **图 3**：不同骨干（EfficientViT-B0/B1、TinyViT、DAV2-S/B/L）的 RMSE–推理时间权衡；
  - **图 4**：3D seed 稀疏度（NP）与分段尺度超参搜索；
  - **图 5**：Jetson AGX Orin 上的加速推理时间；
  - **表 4**：4 项下游应用（深度矫正、MVS、SLAM、占用预测）；
  - **图 6–7**：定性可视化（RealSense 矫正、VGGT 重建、KITTI Odometry 轨迹）。
- **充分性评估**：
  - 数据集覆盖室内外、合成与真实，零样本设置严格；
  - 消融维度较全面，包含策略选择、域表示、基函数、迭代次数等；
  - 引入跨骨干对比，验证方法对基础模型容量的鲁棒性。
- **客观与公平性**：
  - 所有方法在统一零样本条件下评测，KITTI/NYUv2 被排除以避免重叠；
  - 对相对深度方法保留其原有 3D 输入条件，仅限制 seed 比例，控制变量较严谨；
  - 但仍存在部分数据集上非全面领先（如 IBims-1 的 RMSE/MAE 略逊于 Marigold-DC）。

## 6. 主要结论与发现

- MTD 在深度补全任务上**全面超越** SoTA：例如在 nuScenes 上相较 Marigold-DC 将 MAE 降低 0.418、RMSE 降低 0.537；
- 作为即插即用模块，可显著降低各类相对深度/扩散/度量深度模型的 AbsRel 并提升 $\delta_1$，与 DepthAnythingV2 搭配时取得最佳综合表现；
- **不依赖高容量基础模型**：可弥合 DepthAnythingV2 与 MiDaS 之间的性能差距，甚至在仅 ~20M 参数以下的轻量骨干下仍保持可接受精度；
- **极稀疏条件下稳健**：seed 极少时退化为最小二乘基线（内置保护），随 seed 增多 MAE 显著下降，而全局最小二乘几乎无进一步收益；
- 后端开销极低（1.9 ms / <1.8 GB），在 Jetson AGX Orin 上可达**实时**；
- 下游应用收益明显：SLAM 轨迹误差大幅下降（如 Seq 00 从 66.562 降至 25.017）、占用预测精度提升、RealSense 深度质量显著改善、VGGT 结合后超越 MVSAnywhere。

## 7. 优点

- **可解释性强**：基于稀疏图优化与测地距离的严格数学推导（含命题 1 与测地度量证明），非黑盒；
- **免训练、免微调**：不修改基础模型权重，避免性能退化，即插即用；
- **多模态兼容**：可接受 LiDAR、立体视差、对应匹配等多种 3D seed 形式；
- **效率与精度兼顾**：后端开销可忽略，便于边缘部署；
- **内置鲁棒性**：seed 极稀时自动退化为最小二乘，避免失效；
- **实验体系完整**：跨 10+ 数据集零样本评测 + 4 项下游任务验证，覆盖室内外与合成/真实场景；
- **提供实用超参指引**：揭示 NP 与最优分段尺度的反比趋势，便于工程调参。

## 8. 不足与局限

- **训练算力信息缺失**：知识蒸馏部分的 GPU 型号、数量、训练时长等均未披露，复现成本不透明；
- **部分指标未全面领先**：如 IBims-1 上 RMSE（0.190 vs 0.176）、MAE（0.072 vs 0.038）、HAMMER RMSE（0.093 vs 0.054）仍略逊于 Marigold-DC，说明在特定室内小场景下扩散类方法仍有优势；
- **依赖超参数**：分段尺度、近邻数 $N$、迭代次数 $k$ 等需按 NP 调整，跨场景部署需额外调参；
- **仍依赖 3D seed**：论文自述未来工作希望"仅用 3D seed 做初始化，并在持续学习框架下逐步消除该需求"，说明当前方法尚未完全摆脱对稀疏 3D 输入的依赖；
- **标定函数的单调双射假设**：对代理 $\xi$ 与深度 $z$ 之间的单调映射存在前提，若代理量存在系统性偏差可能影响精度；
- **应用限制**：面向需要绝对尺度的任务（自动驾驶、机器人）收益最大，而对仅需相对结构的任务收益有限；SLAM 实验中"Ours"在某些序列（如 Seq 06 的 Droid+LiDAR 104.552）显示基线差异较大，需注意对比公平性解读。

（完）
