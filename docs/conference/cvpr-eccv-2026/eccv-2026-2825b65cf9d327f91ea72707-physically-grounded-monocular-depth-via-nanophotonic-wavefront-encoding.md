---
title: Physically Grounded Monocular Depth via Nanophotonic Wavefront Encoding
title_zh: 基于纳米光子波前编码的物理接地单目深度
authors: "Bingxuan Li, Jiahao Wu, Yuan Xu, Zezheng Zhu, Yunxiang Zhang, Kenneth Chen, Yanqi Liang, Nanfang Yu, Qi Sun"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/4456.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 利用深度基础模型实现精确度量单目深度感知
tldr: 深度基础模型能从单张RGB图像提供强先验，但缺乏物理深度线索，导致度量尺度存在歧义。本文引入超薄平面光学元件金属透镜，在单次拍摄中将深度相关位移编码到两束偏振波前，并通过输入适配策略微调预训练深度基础模型以对齐光学信号。作者还构建了仿真数据管线以扩展训练数据。该方法实现了精确的度量单目深度感知。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 588, \"height\": 676}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 588, \"height\": 676}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 364, \"height\": 364}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 589, \"height\": 676}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 589, \"height\": 676}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 2689, \"height\": 1065}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-007.webp\", \"caption\": \"\", \"page\": 5, \"index\": 7, \"width\": 808, \"height\": 934}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-008.webp\", \"caption\": \"\", \"page\": 5, \"index\": 8, \"width\": 829, \"height\": 942}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 809, \"height\": 935}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-010.webp\", \"caption\": \"\", \"page\": 5, \"index\": 10, \"width\": 809, \"height\": 935}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-011.webp\", \"caption\": \"\", \"page\": 5, \"index\": 11, \"width\": 809, \"height\": 935}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 809, \"height\": 935}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 809, \"height\": 935}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 2780, \"height\": 1111}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 558, \"height\": 1173}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-017.webp\", \"caption\": \"\", \"page\": 6, \"index\": 17, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-018.webp\", \"caption\": \"\", \"page\": 6, \"index\": 18, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-022.webp\", \"caption\": \"\", \"page\": 6, \"index\": 22, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-023.webp\", \"caption\": \"\", \"page\": 6, \"index\": 23, \"width\": 1108, \"height\": 1108}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 2413, \"height\": 915}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-025.webp\", \"caption\": \"\", \"page\": 8, \"index\": 25, \"width\": 488, \"height\": 488}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 1849, \"height\": 1848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 1849, \"height\": 1848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 1849, \"height\": 1848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 1849, \"height\": 1848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 2772, \"height\": 2772}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 1849, \"height\": 1848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-032.webp\", \"caption\": \"\", \"page\": 8, \"index\": 32, \"width\": 1849, \"height\": 1848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-033.webp\", \"caption\": \"\", \"page\": 8, \"index\": 33, \"width\": 488, \"height\": 268}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-034.webp\", \"caption\": \"\", \"page\": 8, \"index\": 34, \"width\": 386, \"height\": 386}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-035.webp\", \"caption\": \"\", \"page\": 8, \"index\": 35, \"width\": 389, \"height\": 389}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-036.webp\", \"caption\": \"\", \"page\": 11, \"index\": 36, \"width\": 600, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-037.webp\", \"caption\": \"\", \"page\": 11, \"index\": 37, \"width\": 600, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-038.webp\", \"caption\": \"\", \"page\": 11, \"index\": 38, \"width\": 600, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-039.webp\", \"caption\": \"\", \"page\": 11, \"index\": 39, \"width\": 600, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-040.webp\", \"caption\": \"\", \"page\": 11, \"index\": 40, \"width\": 600, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-041.webp\", \"caption\": \"\", \"page\": 11, \"index\": 41, \"width\": 600, \"height\": 450}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-042.webp\", \"caption\": \"\", \"page\": 12, \"index\": 42, \"width\": 2878, \"height\": 780}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-043.webp\", \"caption\": \"\", \"page\": 12, \"index\": 43, \"width\": 1740, \"height\": 1137}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-044.webp\", \"caption\": \"\", \"page\": 12, \"index\": 44, \"width\": 1596, \"height\": 1190}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-045.webp\", \"caption\": \"\", \"page\": 12, \"index\": 45, \"width\": 1596, \"height\": 1190}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-046.webp\", \"caption\": \"\", \"page\": 12, \"index\": 46, \"width\": 832, \"height\": 621}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-047.webp\", \"caption\": \"\", \"page\": 12, \"index\": 47, \"width\": 832, \"height\": 621}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-048.webp\", \"caption\": \"\", \"page\": 12, \"index\": 48, \"width\": 832, \"height\": 621}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-049.webp\", \"caption\": \"\", \"page\": 12, \"index\": 49, \"width\": 830, \"height\": 623}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-050.webp\", \"caption\": \"\", \"page\": 12, \"index\": 50, \"width\": 832, \"height\": 621}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-051.webp\", \"caption\": \"\", \"page\": 12, \"index\": 51, \"width\": 830, \"height\": 623}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-2825b65cf9d327f91ea72707/fig-052.webp\", \"caption\": \"\", \"page\": 14, \"index\": 52, \"width\": 1200, \"height\": 450}]"
motivation: 深度基础模型缺乏物理深度线索，导致单目深度存在度量尺度歧义。
method: 用金属透镜将深度相关位移编码进偏振波前，并微调预训练深度基础模型对齐光学信号。
result: 在单次单目拍摄中实现了精确的度量深度感知，并构建仿真数据管线。
conclusion: 融合纳米光子物理线索可有效消除深度基础模型的度量歧义。
---

## Abstract
Depth foundation models (DFMs) offer strong learned priors for 3D perception from single RGB images but lack physical depth cues, leading to ambiguities in metric scale. We introduce metalenses, an emerging class of ultrathin planar optical elements, as a solution to physically encode missing metric depth cues via nanophotonics. In this paper, we bridge the gap between metalens and DFMs to achieve accurate metric monocular depth sensing. In a single monocular shot, our metalens embeds depth-dependent positional shifts into two polarized optical wavefronts. With an input adaptation strategty, we enable direct fine-tuning that aligns a pretrained DFM with the optical signals. To scale the training data, we further develop a comprehensive simulation pipeline that synthesizes metalens responses from RGB-D datasets, incorporating physical factors to minimize the sim-to-real gap. Experiments demonstrate that this approach outperforms both monocular metric depth estimation and depth-from-defocus baselines, showing an effective pathway for accurate monocular metric depth sensing.

---

## 论文详细总结（自动生成）

# 论文总结：基于纳米光子波前编码的物理接地单目深度

## 1. 核心问题与整体含义

- **研究动机**：深度基础模型（Depth Foundation Models, DFMs）如 Depth Anything V2 等，通过大规模数据学习到了丰富的几何先验，在单目深度估计上表现优异。然而，单张 RGB 图像本质上缺乏**物理深度线索**，导致度量尺度（metric scale）估计存在固有的不适定性（ill-posedness），在需要精确度量深度的应用中产生歧义与不准确。
- **现有方案的不足**：
  - 引入 LiDAR 等辅助传感器虽能提供精确度量监督，但依赖主动、高能耗硬件，增加体积与系统复杂度，偏离严格单目设定。
  - 推理时优化（如利用散焦模糊线索）耗时过长（约 5 分钟/帧）。
  - 传统深度从散焦（DfD）方法破坏高频细节、灵敏度低；双像素/偏振方案依赖特定传感器或额外组件。
- **核心问题**：能否**仅通过紧凑单目设备中的被动光学元件**，不依赖主动传感和额外传感器，实现 DFMs 的物理接地？
- **整体含义**：本文提出用**双折射金属透镜（birefringent metalens）**将缺失的度量深度线索通过纳米光子学物理编码进偏振波前，桥接金属透镜与 DFMs，实现精确的度量单目深度感知。该工作为 VR/AR、微型机器人、医疗内窥镜等嵌入式 3D 视觉系统提供了新路径。

## 2. 方法论

### 核心思想
- 利用定制的**双折射金属透镜**将入射光分解为两束正交偏振通道，每束由不同的深度相关点扩散函数（PSF）形成。两通道沿同一光路在单次曝光中投影到传感器上，其共轭 PSF 间的**位置偏移**编码了度量深度。
- 两个图像源自同一视点、无多视角视差，因此与立体视觉有本质区别。
- 通过**输入适配策略**将双偏振通道转换为三通道表示，直接微调预训练 DFM（Depth Anything V2），无需修改网络架构。

### 关键技术细节

**（1）双折射金属透镜与偏振深度编码**
- 金属透镜独立调制 x 和 y 偏振光的相位 ψk = ψf,k + ψr,k（k ∈ {x, y}），其中 ψf,k 提供聚焦能力，ψr,k 设计为产生深度相关的 PSF 旋转。
- 采用**旋转 PSF**：PSF 随深度 z 旋转角度 Δφi(z)：
  $$\Delta\phi_i(z)=\frac{\pi R^2}{N\lambda}\left(\frac{1}{z}-\frac{1}{z_f}\right)$$
  其中 R 为光瞳半径，N 为同心环数（N=8），λ 为波长，z_f 为对焦深度。
- 将光瞳分为 N=8 个同心环，每个环具有拓扑荷 n（n=1,…,N），x 偏振相位按环形区域分段定义；y 偏振相位为该图案旋转 180°。
- 两种偏振图案相差 180°，其相对视差向量角度直接追踪共同旋转 Δφi(z)，形成单调的几何深度线索。
- **偏振复用**：通过聚焦相位 ψf,k 引入相反的垂直偏转，将两偏振图像在传感器上空间分离到上下半区。

**（2）物理接地单目深度（模型适配）**
- 骨干模型采用基于 DPT 架构的 Depth Anything V2（ViT-Small/Base/Large 三个变体）。
- **输入适配策略**：将双偏振观测 (Ix, Iy) 转换为三通道输入 (Ix, Iy, (Ix+Iy)/2)，匹配单目深度模型预训练输入格式，保留场景结构并注入物理编码的度量深度线索，无需修改网络层或增加辅助分支。
- 消融表明该简单适配已足够，附加解码器侧融合模块（如 PromptDA 设计）无显著优势。

**（3）仿真数据管线与 sim-to-real 桥接**
- 光学前向模型将 3D 场景建模为逐层 2D 卷积之和：
  $$I_k=\sum_{n=1}^{N}(S\odot M_n)*P_k(z_n)$$
  其中 S 为场景辐照度，M_n 为第 n 个深度 bin 的二值掩码，PSF 用 FFT 实现基尔霍夫衍射积分模拟。
- **去遮挡感知光学前向模型**：标准线性模型在深度突变区域失效（亮遮挡边缘、暗去遮挡间隙、陡峭表面混叠条纹）。本文引入专门模块：先生成逐层不透明度与亮度图，检测深度不连续，进行边缘外推与背景补全，最后 alpha 校正归一化输出。
- **偏振感知数据增强**：全局缩放（光照变化）、高斯掩码局部亮度扰动（空间偏振失衡）、泊松/高斯噪声（传感器与环境）、高斯模糊（制造缺陷）。
- **少样本真实适配**：手动分割物体并赋予近似平面深度，混合 5 个真实样本（概率 0.05）缩小剩余域差异。

**（4）实现细节**
- 金属透镜：直径 3 mm，工作波长 590 nm，700 nm 高十字形双折射 TiO2 纳米柱，400 nm 亚波长间距，500 µm 厚玻璃基底；制备含电子束光刻、原子层沉积 TiO2、干法刻蚀与等离子灰化三步。
- 成像系统：金属透镜距 20 MP、1 英寸单色 CMOS 传感器 37.6 mm，配 590 nm 带通滤光片；对焦深度 35 cm，深度感知范围 20–120 cm。
- 训练：从度量预训练权重出发，在 Hypersim 数据集微调；深度范围线性映射到 0.2–1.2 m；损失 L = L1 + 0.5 Lgrad；训练 80k 步，学习率 4×10⁻⁶，批量大小 2（Large）或 8（Small/Base）。

## 3. 实验设计

### 数据集与场景
- **仿真实验**：
  - **NYU Depth V2**：标准室内基准，含稠密 LiDAR 真值。
  - **MIT-CGH-4k**：合成数据集，含随机放置 3D 物体，作为零样本基准评估泛化与物理线索利用能力。
  - **FlyingThings3D**：用于与 DfD 基线公平对比，匹配其 1–5 m 范围（金属透镜缩放至 5 mm 直径、50 mm 焦距）。
- **物理实验**：光学平台上安装金属透镜深度相机原型与目标物体，精确控制距离；采集 42 个场景、25 个不同物体（含单/多物体设置，20 个物体未见于 5 张训练集）。

### Benchmark 与对比方法
- **MMDE 基线**：Depth Anything v2/v3、DepthPro、Lotus、Marigold、Metric3D v2、MoGe v2、UniDepth v2、ZoeDepth，以及双传感器方法 PromptDA（RGB+LiDAR）。
- **DfD 基线**：DeepDfD、Split-Aperture。
- **评估指标**：MAE、RMSE、AbsRel、δ0.5（部分实验用 log10、δ1）。
- **对齐策略**：对基线采用逐图像最优线性对齐 {s, t}，消除全局尺度/平移歧义（使基线表现偏高）；LiDAR 仿真通过 10× 下采样真值深度并加 1–2 cm 均匀噪声模拟 iPhone LiDAR 精度。
- **隔离实验**：微调无深度编码的 DepthAnything v2，以区分物理深度线索与数据集微调带来的增益。

### 消融实验
- 性能增益分解（表 4）：金属透镜设计（Meta）、ViT 架构、预训练先验（Prior）三因素。
- 输入适配 vs 解码器融合（表 5）。
- sim-to-real 迁移（表 6）：去遮挡建模、数据增强各组件（光照失衡、模糊、噪声）在仅合成与含真实数据两种训练机制下的影响。
- 预训练先验保持性分析：用 CKA 相似度比较灰度、单偏振三通道复制、伪 RGB 与原始 RGB 输入的特征差异。

## 4. 资源与算力

- **训练配置**：训练 80k 步，学习率 4×10⁻⁶，批量大小 2（Large）或 8（Small/Base）。
- **硬件**：论文**未明确说明**使用的 GPU 型号、数量及具体训练时长。
- 仅提及推理时优化方法（如 Marigold 类）在现代 GPU 上约需 5 分钟，本文方法避免了此类开销。
- 物理原型硬件参数：3 mm 金属透镜、20 MP 单色 CMOS、590 nm 带通滤光片等。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 仿真对比：2 个数据集（NYU Depth V2、MIT-CGH-4k）× 约 12 种方法（含 3 种本文变体）。
  - 物理实验：42 个场景、25 个物体，对比约 12 种方法。
  - DfD 对比：1 个数据集（FlyingThings3D）× 3 种方法。
  - 消融实验：4 组主要消融（性能增益分解、输入适配 vs 融合、sim-to-real 组件、先验保持性 CKA 分析），其中 sim-to-real 消融含 6 种配置 × 2 种训练机制。
- **充分性与客观性评价**：
  - **充分**：覆盖仿真与物理、多数据集、多基线、多层次消融，且对基线采用逐图像最优对齐（对基线有利），评估较为严格。
  - **公平**：与 LiDAR 辅助方法 PromptDA 对比时模拟了 LiDAR 噪声；与 DfD 基线对比时匹配光学参数（焦距、深度范围）与模型容量（Small 骨干 vs U-Net）。
  - **客观**：通过微调无编码的 DepthAnything v2 隔离数据集微调效应，证明增益来自物理编码而非过拟合。
  - 潜在不足：物理实验的真值通过手动分割 + 已知安装距离赋予近似平面深度（平均标签不确定性 < 1 cm），非稠密真值；真实场景数量（42 个）相对有限。

## 6. 主要结论与发现

- **性能领先**：在 NYU Depth V2 和 MIT-CGH-4k 仿真基准上，本文方法在所有无 LiDAR 基线中表现最佳，且与 LiDAR 辅助的 PromptDA 高度竞争（更低 RMSE、AbsRel、δ0.5，L1 相当）。
- **物理实验验证**：在物理原型上持续优于所有无 LiDAR 基线，接近 PromptDA，且即使对基线施加最优尺度/平移对齐后仍保持明显优势。
- **优于 DfD**：在 FlyingThings3D 上全面超越 DeepDfD 和 Split-Aperture。
- **增益来源**：预训练先验是性能提升的主要驱动力；金属透镜设计提供优于 DeepDfD 光学的物理接地；ViT 与同规模 U-Net 的架构差异不显著。
- **输入适配有效**：简单三通道适配优于解码器侧融合，且不引入额外参数。
- **sim-to-real 关键因素**：去遮挡建模和偏振感知增强（尤其光照失衡建模）对零样本泛化至关重要；仅靠真实数据无法完全补偿不准确的光学建模。
- **先验保持性**：伪 RGB 输入相对 RGB 的 CKA 相似度在各层均高于 0.83，最后三个 block 高于 0.95，与灰度基线差距约 0.04，证明色度到偏振的重映射未造成比去色更大的表示偏移。

## 7. 优点

- **方法创新性强**：首次将双折射金属透镜的偏振复用旋转 PSF 与深度基础模型结合，实现被动、单传感器、单次曝光的物理接地度量深度。
- **光学设计精巧**：旋转 PSF 相比标准散焦更抗噪且保留高频细节；偏振隔离单瓣消除重影；可见光 TiO2 金属透镜与 DFM 先验对齐。
- **模型适配简洁高效**：输入适配策略无需修改架构或增加参数，即可复用预训练先验。
- **仿真管线细致**：去遮挡感知前向模型显式处理非对称 PSF 的遮挡/去遮挡双重挑战，配合偏振感知增强显著缩小 sim-to-real 差距。
- **实验设计严谨**：对基线采用有利的最优对齐、模拟 LiDAR 噪声、匹配 DfD 光学参数与模型容量、隔离数据集微调效应，结论可信度高。
- **系统集成度高**：将 PSF 工程、光聚焦、偏振复用集成于单个元件，避免严重模糊与额外组件。

## 8. 不足与局限

- **概念验证性质**：当前系统是物理接地的概念验证，非可部署的深度相机。
- **光子预算受限**：3 mm、f/11.3 孔径与 10 nm 带通滤光片大幅降低孔径-光谱通量，仅适合光照良好、近距离场景与较长曝光。
- **偏振复用代价**：将两偏振视图映射到独立传感器区域，降低有效视场或采样密度，在非散粒噪声受限场景下

在非散粒噪声受限场景下，可能因通道分离导致每路有效像素数减半，进而降低信噪比与空间分辨率；在低照度、快速运动或高动态范围场景中更明显。此外，偏振通道间的微小配准误差、偏振串扰、视场渐晕以及传感器上下半区响应不一致，都会破坏 PSF 偏移线索的可靠性。

- **工作距离与景深受限**：当前设计主要覆盖 20–120 cm、对焦于 35 cm，属于近距室内场景。超出该范围后，PSF 旋转灵敏度、信噪比与标定精度都会下降，难以直接推广到远距、车载或大场景深度估计。
- **标定与制造公差敏感**：方法依赖金属透镜双偏振相位、PSF 模型、传感器位置和偏振通道配准的高精度标定。纳米柱尺寸、刻蚀误差、波长漂移、温度变化或装配偏差都可能改变实际 PSF，进而影响度量深度的稳定性。
- **窄带单色与光子效率约束**：590 nm、10 nm 带通滤光片虽然有利于偏振与 PSF 建模，但牺牲了大量光谱通量，并限制彩色成像能力。因此系统更适合静态或慢速、光照充足的场景，对暗光、运动模糊和低曝光条件不友好。
- **真实实验规模与真值质量有限**：物理实验仅含 42 个场景、25 个物体，且真值由手动分割与已知距离赋予近似平面深度，并非稠密度量真值。虽然平均标签不确定性小于 1 cm，但仍不足以全面评估复杂几何、透明/镜面/低纹理物体以及多物体遮挡场景。
- **泛化边界尚未充分验证**：仿真与物理实验主要集中于室内近距、受控光照和有限物体类别。对户外、雨雾、强逆光、透明材质、镜面反射、细薄结构以及极端纹理缺失区域的鲁棒性仍缺少系统评估。
- **依赖预训练 DFM 先验**：性能增益很大程度来自 Depth Anything V2 等基础模型的预训练先验。若替换为其他深度模型、跨域部署或预训练权重分布不匹配，输入适配策略与度量映射可能需要重新训练或校准。
- **系统集成与可部署性不足**：当前原型仍处于光学平台概念验证阶段，尚未展示与紧凑相机模组、移动端 SoC 或内窥镜等真实嵌入式平台的集成方案，体积、功耗、散热与量产一致性仍待验证。
- **复现信息不完整**：论文未明确给出 GPU 型号、数量、训练总时长与完整数据生成/标定流程细节，可能影响第三方复现与公平比较。
- **总体定位**：该工作证明了“纳米光子波前编码 + 深度基础模型”实现被动单目度量深度的可行性，但距离全天候、宽动态、小型化、低功耗的实用深度相机仍有明显工程与算法差距。

（完）
