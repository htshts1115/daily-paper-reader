---
title: "OMoBlur: An Object Motion Blur Dataset and Benchmark for Real-World Local Motion Deblurring"
title_zh: OMoBlur：面向真实场景局部运动去模糊的物体运动模糊数据集与基准
authors: "Yu, Dingchuan, Li, Jiatong, Zhou, Jingwen, Zhuge, Zhengyue, Chen, Yueting, Li, Qi"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_OMoBlur_An_Object_Motion_Blur_Dataset_and_Benchmark_for_Real-World_CVPR_2026_paper.pdf"
tags: ["query:cv-render"]
score: 4.0
evidence: 物体运动模糊数据集与局部去模糊基准
tldr: 静态场景中的物体运动模糊具有空间异质性，而现有数据集或存在残余错位，或合成模糊无法模拟曝光积分过程。本文提出物理驱动的OMoBlur数据集，通过可编程传感器控制模拟真实曝光积分，提供两万对模糊-清晰-掩码数据，并据此提出OMDNet去模糊网络。实验表明合成模糊分布与真实模糊高度对齐。该工作服务于运动去模糊，与虚化/散景渲染主题仅弱相关。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 958, \"height\": 720}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 800, \"height\": 600}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 1920, \"height\": 360}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 4, \"index\": 6, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 4, \"index\": 7, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 4, \"index\": 8, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 4, \"index\": 9, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 4, \"index\": 10, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 4, \"index\": 11, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 4, \"index\": 12, \"width\": 2000, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 4, \"index\": 13, \"width\": 1920, \"height\": 360}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 4, \"index\": 14, \"width\": 1920, \"height\": 360}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 1946, \"height\": 1436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 1195, \"height\": 347}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 7, \"index\": 17, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 7, \"index\": 18, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 7, \"index\": 19, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 7, \"index\": 21, \"width\": 727, \"height\": 396}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 454, \"height\": 455}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 485, \"height\": 485}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 674, \"height\": 674}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 674, \"height\": 674}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 674, \"height\": 674}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 832, \"height\": 372}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 1920, \"height\": 360}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 1034, \"height\": 194}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-omoblur-an-object-motion-blur-dataset-and-benchmark-for-real-world-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 8, \"index\": 32, \"width\": 2000, \"height\": 375}]"
motivation: 静态场景中的物体运动模糊空间异质，现有数据集或因分光采集存在残余错位，或合成模糊无法建模曝光积分过程。
method: 提出物理驱动的OMoBlur数据集，通过可编程传感器控制模拟真实曝光积分，提供两万对模糊-清晰-掩码数据，并据此提出OMDNet去模糊网络。
result: 数据集覆盖多种物体运动类型，使合成模糊分布与真实模糊高度对齐，为局部运动去模糊提供基准。
conclusion: 为真实手持场景的物体运动去模糊提供了更真实的物理数据集与基准，但与虚化渲染目标不同。
---

## Abstract
Object motion blur in static scenes is spatially heterogeneous, differing from conventional deblurring problems yet frequently occurring in real handheld capture scenarios. Existing datasets either rely on costly beam-splitting capture with residual misalignment or employ synthetic blur that fails to model the continuous photon-integration process during exposure. To overcome these limitations, we introduce OMoBlur, a physically grounded dataset that emulates realistic exposure integration via programmable sensor control, ensuring close alignment between synthetic and real blur distributions. OMoBlur provides 20,000 blur-sharp-mask pairs covering diverse object motion types. Leveraging this dataset, we further propose OMDNet, an object-motion-aware deblurring network that integrates a Motion-Appearance Extract Block, a Flow-Guided Gate Predictor, and an Adaptive Gated Fusion mechanism. This design enables the network to selectively restore blurred regions while preserving static backgrounds, without requiring pixel-accurate mask annotations. Extensive experiments demonstrate that OMoBlur's physically faithful data collection and large-scale diversity significantly enhance the network's generalization to real-world motion blur, establishing OMoBlur and OMDNet as a robust benchmark and practical solution for local motion deblurring. The dataset and code is publicly released at https://yudingchuan.github.io/OMoBlur_homepage/.

---

## 论文详细总结（自动生成）

# OMoBlur 论文深度总结

## 一、核心问题与整体含义（研究动机与背景）

- **问题定位**：静态场景中由独立运动物体产生的**物体运动模糊**（object motion blur）具有显著的空间异质性——模糊局部化、不连续，多物体以不同速度/方向运动并相互遮挡，与相机抖动引起的全局连续模糊有本质差异，且在实际手持拍摄场景中频繁出现。
- **现有数据集的两难困境**：
  - **全真实采集类**（如 ReLoBlur、RealBlur、RBI）：使用同轴分光相机同步捕获模糊-清晰对，但硬件笨重、难以规模化，且光学与电子不一致导致像素级几何/光度对齐困难，残余错位反而损害监督训练。
  - **多帧累加合成类**（如 GoPro）：通过平均连续帧合成模糊，但依赖简化模型，受读出时间限制导致有效曝光比 ρt 极低（此前约 10%），模糊轨迹不自然、不连续，与真实模糊存在域差距。
  - **卷积核类**：空间变化的核无法遵循物理运动学约束（如滚轮摆线路径），且无法建模运动物体引起的**时变前景/背景遮挡混合过程**（单个像素在曝光期间同时积分前景与背景光子）。
- **整体含义**：论文主张从物理曝光积分过程出发重建模糊形成模型，提出首个大规模、物理忠实的物体运动模糊数据集 **OMoBlur**（2 万+ 模糊-清晰-掩码三元组），并配套设计 **OMDNet** 去模糊网络，作为局部运动去模糊的稳健基准与实用方案。

## 二、方法论

### 2.1 物理模糊建模（数据集基础）

- **RAW 成像模型**：传感器输出可建模为光子到达率 p(t,x,y) 在曝光区间 ΔT 上的积分，再经增益 G 与噪声 ε 的转换管线 C(·) 得到 RAW 信号。
- **简化累加模型**：B = g( (1/n) Σ g⁻¹[Sᵢ] )，其中 Sᵢ 为单帧经 ISP 后的 RGB 图像，g⁻¹ 为逆相机响应。
- **升级为时间积分信号累加模型**：在 g⁻¹→ISP⁻¹、相邻帧时间连续、增益恒定、噪声可忽略的前提下，模糊图像可近似为**曝光时间 nΔt、增益 G/n 下的一次真实长曝光**，即：
  - B ≈ ISP( C( ∫ p(t)dt, G/n ) )
- **关键约束**：有效曝光比 ρt = Δt/(tᵢ₊₁ - tᵢ) 决定了模糊轨迹的物理连续性；现有方法用 gamma 近似或逆 ISP 无法忠实还原信号累加，高倍帧插值（FI）虽视觉自然但与真实曝光过程不符。

### 2.2 物体运动分类

- **面内运动（in-plane）**：垂直光轴平移 + 绕光轴旋转，对应明确的 2D 图像变换，问题相对受约束。
- **面外运动（out-of-plane）**：沿光轴平移或 yaw/pitch 旋转，引入深度缩放、自遮挡等 3D 几何效应，属严重病态逆问题。
- 该分类指导数据采集，确保覆盖全难度谱系。

### 2.3 图像采集与数据集构建

- **硬件选择**：Basler a2A1920-160ucBAS 工业相机，直接输出 RAW（即 g⁻¹ ≡ ISP⁻¹，避免未知逆响应）；Basler C23-0824-5M 镜头，8mm 焦距（≈45mm 全画幅等效）。
- **重叠曝光策略**：下一帧曝光在上一帧读出期间即开始；ROI 限制为 1920×360 使读出时间降至 1921μs，曝光时间设为 1960μs，达成 **500fps、ρt = 98%**（对比此前约 10%）。
- **残余 2% 曝光间隙补偿**：通过成像几何分析选择光学参数，使曝光间隙内物体位移限制在 **0.1 像素**，逼近真实模糊形成条件。
- **构建流程**（Fig.3）：
  1. 平均连续 RAW 帧 → 经 ISP 转 RGB 得到模糊图；
  2. 单帧 RAW 经 ISP 转 RGB，中间帧作为清晰 GT；
  3. 连续帧经 MeFlow 估计光流 → 聚类 + 后处理生成模糊掩码；
  4. 光流在重复纹理/暗背景处有误差 → 训练时用 AGF 缓解不可靠掩码监督，测试集掩码**人工校正**以保证公平评测；
  5. 过滤无效场景后发布 **20,000+ 三元组**。

### 2.4 OMDNet 网络架构

- **整体结构**：U-Net 骨干 + SIMO 配置，将跳连接替换为双路径 **Motion-Appearance Extract Block (MAEB)**，实现多尺度特征灵活传播。
- **MAEB**：
  - 共享 NAFBlock 作为 stem；
  - 外观分支：另一 NAFBlock；
  - 运动分支：**Differential Transposed Attention Module (Diff-TAM)**——受差分放大器与差分注意力启发，通过成对注意力路径比较抑制背景响应，沿通道维度做 Restormer 式转置注意力，仅在 MAEB 内使用以控制开销。
- **Flow-guided Gate Predictor (FGP)**：
  - 融合运动特征与上采样低层光流预测，生成双向光流 F = {F₋→₀, F₊→₀} 与流掩码 O∈[0,1]；
  - 将流幅值 ‖F‖ 与 F 拼接得到门控 bGᵢ；
  - **两项流监督约束**：
    1. **Warp 约束**：用 F 将 GT 中间帧反变换应重建首/末清晰帧；
    2. **Merge 约束**：融合 bmᵢ = (2/3)(bSᵢ₋⊗O + bSᵢ₊⊗(1-O)) + (1/3)bSᵢ 匹配 mᵢ = (1/3)(Sᵢ₋+Sᵢ+Sᵢ₊)。
- **Adaptive Gated Fusion (AGF)**：掩码仅作**软先验**，训练时计算两种门控输出并共同监督：
  - 标准式：bSᵢG = bSᵢ⊗bGᵢ + Bᵢ⊗(1-bGᵢ)；
  - 增强式：bS*ᵢG = bSᵢ⊗bGᵢ + (Mᵢ⊗Bᵢ+(1-Mᵢ)⊗Sᵢ)⊗(1-bGᵢ)；
  - 增强式在背景像素用 Sᵢ 替代 Bᵢ，促使 bGᵢ→0，从而纠正掩码不准与静态背景误激活；**测试时仅输出标准式**。
- **损失函数**（总损失 L = λ₁L_warp + λ₂L_merge + λ₃L_r + λ₄L_g，λ = 0.05/0.4/1.0/0.4）：
  - L_warp：双向 L1 取 min，避免运动方向歧义导致网络坍缩为单一混合流场；
  - L_merge：L1 软监督流与 bSᵢ；
  - L_r：L1 + FFT 强监督 bSᵢ；
  - L_g：对两种门控输出取平均监督。

## 三、实验设计

- **数据集/场景**：
  - 主评测：**OMoBlur** 测试集，原生分辨率 1920×360（18,910 训练对 / 1,354 测试对）；
  - 泛化评测：**ReLoBlur** 真实采集数据（图像下采样 2× 统一尺度）；
  - 对照合成策略：**GoPro**（官方预训练）、**OMoBlur-FI**（REDS 协议：500fps→125fps，EMA-VFI 做 16× 插值后合成）。
- **Benchmark 指标**：PSNR/SSIM、**加权 PSNR/SSIM**（聚焦模糊区域）、LPIPS(VGG)、DISTS。
- **对比方法**：CNN 类（MIMO-UNet、NAFNet、LBAG）、Transformer 类（Restormer、LMD-ViT）、Mamba 类（EVSSM）。
- **训练设置**：Adam，batch size 8，500K 迭代，初始学习率 1×10⁻⁴ 并在预定里程碑衰减；采用类似 BAPC 的模糊感知裁剪策略采样 256×256 patch。

## 四、资源与算力

- 论文明确提到评测使用 **1 块 NVIDIA GeForce RTX 4090 GPU**（用于 OMoBlur 测试集原生分辨率评测）。
- 文中**未明确说明**训练所用 GPU 数量、训练总时长、采集阶段总耗时等具体算力开销。
- 采集端硬件信息较详细（Basler 工业相机 + 8mm 镜头，500fps，ρt=98%），但未给出采集总时长与数据量存储规模。

## 五、实验数量与充分性

- **主要实验组**：
  1. OMoBlur 基准定量对比（6 个基线 + OMDNet，6 项指标，Tab.1）；
  2. 视觉对比（Fig.6：OMoBlur 自旋球 + ReLoBlur 运动汽车）；
  3. 跨数据集泛化（Fig.7：MIMO-UNet/Restormer 分别在 GoPro、OMoBlur-FI、OMoBlur 上训练后于 ReLoBlur 评测）；
  4. 合成策略对比（Fig.8：OMoBlur vs OMoBlur-FI 视觉难以区分）；
  5. **消融实验**（Tab.2：MAEB、FGP、Diff-TAM 三模块逐项叠加，4 组配置）；
  6. 门控机制对比（Fig.9：与 LBAG 门控、人工标注对比；Fig.10：静态区域保持 MAE 定量对比，无门控 / LBAG 门控 / 本文门控）。
- **充分性评价**：
  - **优点**：覆盖定量+定性、自数据集+跨数据集、模块消融+机制对比，维度较完整；对门控设计做了专门的静态区域保持定量分析（MAE）。
  - **可议之处**：跨数据集评测因"中间帧 vs 起始帧"目标不一致，**仅做定性比较**，未提供可比数值；未报告方差/多次运行结果；消融仅报告单组数值，缺少误差棒或显著性分析；对训练数据规模、掩码噪声鲁棒性等未做敏感性分析。

## 六、主要结论与发现

- OMoBlur 的物理忠实采集与大规模多样性**显著提升**网络对真实运动模糊的泛化能力；在 ReLoBlur 上训练的模型（Fig.1）不如在 OMoBlur 上训练的模型泛化好。
- **OMDNet 在 OMoBlur 全部指标上最优**，尤其在加权 PSNR/SSIM（34.04 / 0.8716）与感知指标 LPIPS（0.2171）/DISTS（0.0788）上增益最显著，说明其在模糊区域恢复与视觉真实感上优势突出。
- 全局 PSNR/SSIM 提升幅度相对较小是**有意设计**：门控机制避免强行修正模糊-清晰对中的固有残余错位，从而保护静态背景。
- 跨数据集泛化中，OMoBlur 训练的模型能干净去除旋转车轮摆线拖影、旋转球体等复杂运动，甚至比 ReLoBlur 的 GT 更干净；而 GoPro 训练的模型产生伪影，OMoBlur-FI 训练的模型在面内旋转与面外运动场景中基本失败。
- 门控对比：LBAG 门控在静态背景产生误激活，本文 AGF 更准确聚焦真实模糊区域；静态区域 MAE 从无门控的 0.041/0.026 降至 0.007/0.006。

## 七、优点

- **物理建模严谨**：从光子积分出发推导时间积分信号累加模型，并给出成立前提（g⁻¹→ISP⁻¹、时间连续、增益恒定、噪声可忽略），而非经验性合成。
- **采集工程精细**：工业相机直出 RAW、重叠曝光将 ρt 提升至 98%（远超此前约 10%）、几何分析将残余间隙位移限制到 0.1 像素，从源头缩小合成-真实域差距。
- **数据规模与多样性**：20K+ 三元组，覆盖行人、车辆、球类、手持海报/书法等场景，涵盖面内/面外运动全难度谱系。
- **方法设计巧妙**：
  - Diff-TAM 借鉴差分放大器思想抑制背景响应，专为运动模式分离设计；
  - AGF 用掩码作软先验、双门控互补监督，**无需像素级精确掩码标注**，鲁棒应对算法掩码误差与配对不完美；
  - L_warp 的双向 min 设计避免运动方向歧义导致网络坍缩。
- **实验对照有说服力**：通过 GoPro / OMoBlur-FI / OMoBlur 三方跨数据集训练对照，直接验证物理忠实性对泛化的价值；图 8 显示 FI 与真实模糊"视觉难以区分"但泛化差距显著，凸显物理一致性而非视觉相似性的重要性。

## 八、不足与局限

- **算力信息不透明**：仅提及 1 张 RTX 4090 用于评测，训练 GPU 数量、训练时长、采集总耗时均未披露，复现成本难以评估。
- **跨数据集评测可比性受限**：因目标帧定义不同（OMoBlur 重建中间帧，ReLoBlur 面向起始帧），跨数据集**仅能定性比较**，缺乏可量化的泛化数值。
- **掩码质量依赖与人工介入**：训练掩码由 MeFlow 光流+聚类自动生成，在重复纹理/暗背景下存在误差；测试集掩码需**人工校正**，意味着测试集标注成本高且可能引入主观偏差，也影响数据集的可扩展性。
- **合成-真实间隙未完全消除**：仍存在 2% 曝光间隙（虽经光学补偿限制到 0.1 像素），且假设处于线性响应区、增益已校准，实际场景偏离这些前提时有效性待验证。
- **场景覆盖偏差**：数据以可控室内/近距离场景为主（海报、书法、球类、行人、车辆），对极端光照、远距离、高速运动、多物体密集遮挡等更复杂真实场景的覆盖程度未充分讨论。
- **应用限制**：方法针对静态背景+独立运动物体的局部模糊，不适用于相机抖动全局模糊、动态相机场景或全图模糊；门控机制本质上是"选择性恢复"，对模糊区域边界的精细处理仍依赖门控预测精度。
- **与虚化/散景渲染任务弱相关**：该工作聚焦运动去模糊的复原方向，与光学虚化（bokeh）渲染目标不同，跨任务迁移价值有限。

（完）
