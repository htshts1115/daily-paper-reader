---
title: "LensStyle: Learning the Optical Aesthetics for Controllable Stylized Lens Effect Rendering"
title_zh: LensStyle：学习可控风格化镜头效果渲染的光学美学
authors: "Yachuan Huang, Liwen Xiao, Liao Shen, Qiwen Wang, Huiqiang Sun, Zhiyu Pan, Zhiguo Cao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1906.pdf"
tags: ["query:cv-render"]
score: 9.0
evidence: 可控风格化镜头效果与散景渲染，建模光圈、渐晕与衍射
tldr: 现有镜头效果渲染方法主要模拟从小光圈到大光圈的模糊过渡，却忽视光圈形状、渐晕与衍射带来的美学风格，难以生成多样的大光圈散景或小光圈星芒等现象。本文提出LensStyle统一框架，通过联合连续-离散控制显式建模镜头美学，实现可控的风格化镜头效果渲染。实验表明该方法能生成多样化且可控的散景与镜头现象。该工作为散景点扩散函数合成与移动端虚化管线提供了重要参考。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 476, \"height\": 715}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 476, \"height\": 715}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 476, \"height\": 715}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 476, \"height\": 635}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 476, \"height\": 635}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 476, \"height\": 635}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 476, \"height\": 635}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 473, \"height\": 715}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 476, \"height\": 635}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 476, \"height\": 715}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 476, \"height\": 635}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 476, \"height\": 715}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 4225, \"height\": 2200}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-014.webp\", \"caption\": \"\", \"page\": 7, \"index\": 14, \"width\": 3932, \"height\": 2617}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-015.webp\", \"caption\": \"\", \"page\": 7, \"index\": 15, \"width\": 364, \"height\": 379}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-016.webp\", \"caption\": \"\", \"page\": 11, \"index\": 16, \"width\": 2089, \"height\": 266}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-017.webp\", \"caption\": \"\", \"page\": 11, \"index\": 17, \"width\": 2089, \"height\": 305}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-018.webp\", \"caption\": \"\", \"page\": 12, \"index\": 18, \"width\": 1742, \"height\": 276}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-019.webp\", \"caption\": \"\", \"page\": 12, \"index\": 19, \"width\": 473, \"height\": 349}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-020.webp\", \"caption\": \"\", \"page\": 12, \"index\": 20, \"width\": 2089, \"height\": 275}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-021.webp\", \"caption\": \"\", \"page\": 12, \"index\": 21, \"width\": 2089, \"height\": 266}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-07da212b680ddc11ab504cfb/fig-022.webp\", \"caption\": \"\", \"page\": 13, \"index\": 22, \"width\": 4212, \"height\": 1104}]"
motivation: 现有镜头效果渲染只关注小到大光圈的模糊过渡，忽视光圈形状、渐晕与衍射带来的风格化美学。
method: 提出LensStyle统一框架，通过联合连续-离散控制显式建模镜头美学，生成可控风格化镜头效果。
result: 可生成多样的大光圈散景与小光圈星芒等效果，实现风格与模糊的可控渲染。
conclusion: 为镜头美学与散景渲染提供统一可控方案，对移动端虚化管线具有参考价值。
---

## Abstract
The visual aesthetics of photographs are deeply influencedby lens characteristics such as aperture shape, optical vignetting and op-tical diffraction, which together define a camera’s unique optical style.Existing lens effect rendering methods primarily focus on accurately sim-ulating the blur transition from small to large apertures but overlook thestylistic aspects of lens effects. As a result, they fail to produce diversebokeh effects under large apertures or capture distinctive photographicphenomena such as starbursts that emerge under small apertures. In thiswork, we introduce LensStyle, a unified framework for controllable styl-ized lens effect rendering that explicitly models lens aesthetics throughjoint continuous–discrete control. Our model incorporates a Dual-PathController that disentangles continuous optical parameter modulation(e.g., focus distance and blur strength) from discrete lens-style condi-tioning (e.g., circular, polygonal, donut, cat-eye, and starburst effects),enabling fine-grained, interpretable, and physically grounded lens manip-ulation within a single unified framework. To support model training, wecurate a comprehensive MultiLens dataset containing multi-lens imagepairs synthesized under real optical constraints. Extensive experimentsdemonstrate that LensStyle achieves superior realism, controllability, andaesthetic quality compared with existing lens effect rendering approachesand diffusion-based image editing models, advancing computational pho-tography toward multiple-lens-style simulation.

---

## 论文详细总结（自动生成）

# LensStyle 论文中文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：照片的视觉美学深受镜头光学特性的影响——光圈形状、光学渐晕（optical vignetting）与光学衍射（optical diffraction）共同定义了相机的"镜头风格"。圆形/多边形光圈在大光圈下产生独特散景形状；球差或折返镜头产生甜甜圈形散景；边缘渐晕带来猫眼效果；小光圈衍射则产生星芒图案。
- **核心问题**：现有镜头效果渲染方法（传统/神经散景渲染、扩散驱动散景生成）主要关注**从小光圈到大光圈的模糊过渡**，只建模"模糊量"，却忽视了"模糊风格"。
- **具体缺陷**：无法在大光圈下生成多样化的散景效果（多边形、甜甜圈、猫眼等），也无法捕捉小光圈下特有的星芒（starburst）现象。
- **整体含义**：本文提出 LensStyle，一个统一的可控风格化镜头效果渲染框架，通过**联合连续–离散控制**显式建模镜头美学，推动计算摄影走向多镜头风格模拟。

## 2. 方法论

### 2.1 核心思想
- 采用**基于流匹配（flow matching）的生成架构**，将"全清晰图像 → 风格化镜头图像"的转换建模为隐空间中的连续传输过程。
- 核心组件为**双路径控制器（Dual Path Controller）**，将连续光学参数调制与离散镜头风格条件解耦。
- **推理阶段无需深度图**（depth-free），深度仅在数据集合成时用于生成物理一致的监督信号。

### 2.2 关键技术细节
- **整体框架**：由三部分组成——(1) 隐自编码器（VAE）编解码图像；(2) 双路径控制器；(3) 基于流的渲染网络。
- **流匹配损失**：给定全清晰隐码 $z_A$ 与镜头风格隐码 $z_L$，定义线性插值 $\phi_t(z_L)=(1-t)z_A+tz_L$，网络预测速度场 $v_t(\phi_1(z_L))=\phi_1(z_L)-\phi_t(z_L)$，损失为
  $\mathcal{L}_{FM}=\mathbb{E}_t\|N_{fm}(\phi_t(z_L),z_A,z_C,z_D,t)-v_t(\phi_1(z_L))\|_2^2$，其中 $z_C$ 为连续参数嵌入，$z_D$ 为离散风格嵌入。

- **连续光学参数调制（COPM）分支**：
  - 对焦点距离、模糊强度归一化后做傅里叶特征编码，得到高维嵌入 $\mathbf{p}$；
  - 通过轻量 MLP 生成自适应缩放/偏移系数 $\gamma(\mathbf{p})$、$\beta(\mathbf{p})$，对中间特征做仿射调制：$h'=\gamma(\mathbf{p})\odot h+\beta(\mathbf{p})$。

- **离散镜头风格交叉注意力（DLSC）分支**：
  - 将风格类别（圆形、多边形、甜甜圈、猫眼、星芒）经文本编码器（CLIP）编码为 $z_T$；
  - 通过交叉注意力注入主干：$\mathrm{CrossAttn}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d})V$，其中 $Q=W_Q h'$、$K=W_K z_T$、$V=W_V z_T$。

### 2.3 MultiLens 数据集合成（统一光学前向模型）
- **散焦 PSF**：$B(x,y)=A(x,y)/\sum_{x',y'}A(x',y')$，即归一化的光圈投影。
- **衍射 PSF**：采用 Fraunhofer 衍射 $D(u,v)=|\mathcal{F}\{A(x,y)\}|^2$，衍射尖峰数量与朝向由光圈叶片数 $N_b$ 和旋转角 $\theta_0$ 决定。
- **四类光圈函数**：圆形（半径 $r_0$）、正 $N_b$ 边形（各边方向 $\theta_k$）、甜甜圈（内外半径 $r_1=\mu r_2$）、猫眼（椭圆裁剪，含离轴位移 $\delta_x$）。
- **深度一致的渲染**：定义空间变化散焦强度 $K(p)=\alpha|Z(p)-Z_f|$（$Z_f$ 为对焦深度，$\alpha$ 控制模糊强度），最终图像为空间变化卷积与衍射项叠加：
  $I_L(p)=\sum_q I_A(q)\cdot B_{K(p)}(p-q)+\lambda_d\cdot H(I_A)(p)\cdot D(p)$，其中 $H$ 提取高亮区域，$\lambda_d$ 控制衍射强度。
- **数据集构成**：共 303,000 对样本，源自 3,000 个全清晰场景——300,000 对散焦样本（4 种光圈几何 × 5 个对焦距离 × 5 个模糊强度）加 3,000 对衍射样本。

### 2.4 优化目标
- 总损失 $\mathcal{L}=\mathcal{L}_{FM}+\lambda_1\mathcal{L}_{rec}+\lambda_2\mathcal{L}_{perc}$，其中 $\mathcal{L}_{rec}$ 为像素级 L1 重建损失，$\mathcal{L}_{perc}$ 为 VGG 感知损失，系数 $\lambda_1=0.2$、$\lambda_2=0.5$。

## 3. 实验设计

- **数据集 / 场景**：
  - **MultiLens**（自建，合成）：用于训练与定量评估，包含圆形、多边形、甜甜圈、猫眼、星芒等风格。
  - **EBB400**（真实世界数据集）：用于评估标准圆形散景渲染的真实场景泛化能力。
  - **用户研究图像**：从 Unsplash 采集 32 张真实全清晰图像，覆盖人像、动物、室内外、白天/夜晚等多样内容。

- **Benchmark 与指标**：采用 PSNR、SSIM、LPIPS（LPIPS 对模糊更敏感，更贴近人眼感知）。

- **对比方法**：
  - 圆形散景：MPIB、BokehMe、Dr.Bokeh、BokehDiff（均为开源自监督/扩散基线，输入依赖 Depth Anything V2 预测的深度图）。
  - 其他风格（多边形/甜甜圈/猫眼/星芒）：UltraEdit、SuperEdit 等指令式图像编辑模型，以及在其 MultiLens 数据集上微调后的版本 UltraEdit*、SuperEdit*。
  - 星芒方面，因文献 [20] 未公开实现，改用图像编辑模型对比。

- **用户研究**：58 名参与者，采用 A/B 成对比较协议，从美学质量、风格保真度、内容一致性三方面评价。

## 4. 资源与算力

- **GPU 型号**：NVIDIA RTX A6000。
- **GPU 数量**：论文**未明确说明**具体使用的 GPU 数量。
- **训练配置**：MultiLens 数据集，分辨率 512×384，训练 10K 迭代，Adam 优化器，初始学习率 3×10⁻⁵，3K 迭代后线性衰减至 3×10⁻⁷。
- **模型规模**：8× 下采样 VAE（4 通道隐表示）；条件 U-Net（8 输入通道、4 输出通道），基于预训练 SD2.1 初始化；CLIP 文本编码器；MLPγ/MLPβ 为 3 层 MLP 带 SiLU 激活。
- **训练时长 / 总计算量**：**未提及**。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 定量对比 2 组（表 1 覆盖多边形/甜甜圈/猫眼/星芒四种风格；表 2 覆盖 MultiLens-Circle 与 EBB400 圆形散景）。
  - 定性对比 2 组（图 4 对散景渲染方法，图 5 对图像编辑方法）。
  - 用户研究 1 组（表 3，4 组对比）。
  - 消融实验 1 组（表 4，含 3 个变体 + 全模型）。
- **充分性评估**：
  - 实验覆盖了多风格、合成与真实数据集、定量与定性、客观指标与主观用户研究，**整体较为充分**。
  - **公平性**：为图像编辑基线额外提供微调版本（SuperEdit*、UltraEdit*）以作公平比较；所有散景基线共享同一深度图预测结果，体现了较好的对照公平性。
  - **潜在不足**：星芒效果因缺乏可公开复现的基线，仅与编辑模型比较，横向对比略弱；用户研究样本量（58 人、32 图）相对有限。

## 6. 主要结论与发现

- LensStyle 在**圆形散景**渲染上于 MultiLens 与 EBB400 两数据集均取得最高 PSNR/SSIM 与最低 LPIPS，优于 MPIB、BokehMe、Dr.Bokeh、BokehDiff。
- 在**其他风格**（六边形、甜甜圈、猫眼、星芒）上，相比微调后的编辑模型仍有 **1.1–1.8 dB PSNR 提升**与 **15–25% 的 LPIPS 相对下降**。
- 用户研究显示：相比 SuperEdit/UltraEdit 及其微调版本，本方法偏好率分别达 76.8%/88.4%/60.8%/76.5%。
- 消融实验证实三个核心组件（流匹配、COPM、DLSC）均为必要：去除流匹配导致结构保持不稳定与过平滑；去除 COPM 破坏连续参数插值单调性；去除 DLSC 削弱复杂风格的特定特征。
- 由于无需深度输入，在深度估计不准确的场景下，本方法避免了基线误模糊对焦区域的问题。

## 7. 优点

- **统一框架**：在单一流匹配模型内同时实现连续光学参数（对焦距离、模糊强度）与离散镜头风格（5 类）的联合控制。
- **双路径解耦设计**：将物理参数调制与风格语义条件显式分离，兼顾可解释性与物理一致性。
- **物理先验驱动**：数据集合成基于统一光学前向模型，融合几何光学的散焦与波动光学的衍射，覆盖从小光圈星芒到大光圈多样散景的完整现象。
- **推理无需深度**：避免了真实场景中深度估计不可靠带来的误差传播，实用性强。
- **实验设计较严谨**：为主流编辑模型提供微调版本作为公平对照，并辅以用户研究验证主观美学质量。

## 8. 不足与局限

- **品牌级镜头模拟缺失**：作者明确指出无法模拟 Fuji、Sony、Nikon、Canon 等不同品牌 DSLR 的散景特性，风格空间仍有限。
- **算力信息不完整**：未披露 GPU 数量与训练总时长，可复现性与效率评估受限。
- **训练数据以合成为主**：MultiLens 基于 ReDWeb 深度图合成，训练依赖深度真值，合成数据与真实光学成像可能存在域差距（domain gap）。
- **星芒对比基线不足**：因缺乏可复现的物理模拟基线，星芒效果仅与图像编辑模型对比，说服力略弱。
- **用户研究规模有限**：58 名参与者、32 张图像，可能无法充分覆盖广泛的审美偏好与场景多样性。
- **风格空间封闭**：目前仅支持预设的 5 类离散风格，无法连续插值或生成任意光圈几何（如非规则叶片形状、多叶片组合等）。

（完）
