---
title: "CLDefocus: Physically Grounded Compound-Lens Defocus Blur Synthesis"
title_zh: CLDefocus：物理驱动的复合镜头散焦模糊合成
authors: "Yunkyu Lee, Woohyeok Kim, Sunghyun Cho"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/8682.pdf"
tags: ["query:neural-bokeh"]
score: 9.0
evidence: 带遮挡处理的深度感知散焦渲染与点扩散函数合成
tldr: 现有去散焦方法受限于训练数据的镜头多样性与真实感不足，跨相机泛化差。本文提出 CLDefocus，整合基于 Debye CZT 传播的高效波动光学 PSF 计算、带遮挡处理的深度感知散焦渲染，以及辐射线性空间中的模糊合成与相机 ISP 模拟。该统一管线可规模化生成多样复合镜头的真实散焦数据集，为深度感知散焦渲染与点扩散函数合成提供了物理可解释的框架。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-001.webp\", \"caption\": \"\", \"page\": 11, \"index\": 1, \"width\": 457, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-002.webp\", \"caption\": \"\", \"page\": 11, \"index\": 2, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-003.webp\", \"caption\": \"\", \"page\": 11, \"index\": 3, \"width\": 454, \"height\": 301}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-004.webp\", \"caption\": \"\", \"page\": 11, \"index\": 4, \"width\": 454, \"height\": 301}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-005.webp\", \"caption\": \"\", \"page\": 11, \"index\": 5, \"width\": 457, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-006.webp\", \"caption\": \"\", \"page\": 11, \"index\": 6, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-007.webp\", \"caption\": \"\", \"page\": 11, \"index\": 7, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-008.webp\", \"caption\": \"\", \"page\": 11, \"index\": 8, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-009.webp\", \"caption\": \"\", \"page\": 11, \"index\": 9, \"width\": 457, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-010.webp\", \"caption\": \"\", \"page\": 11, \"index\": 10, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-011.webp\", \"caption\": \"\", \"page\": 11, \"index\": 11, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-012.webp\", \"caption\": \"\", \"page\": 11, \"index\": 12, \"width\": 457, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-013.webp\", \"caption\": \"\", \"page\": 11, \"index\": 13, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-014.webp\", \"caption\": \"\", \"page\": 11, \"index\": 14, \"width\": 454, \"height\": 300}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-015.webp\", \"caption\": \"\", \"page\": 11, \"index\": 15, \"width\": 457, \"height\": 301}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-016.webp\", \"caption\": \"\", \"page\": 15, \"index\": 16, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-017.webp\", \"caption\": \"\", \"page\": 15, \"index\": 17, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-018.webp\", \"caption\": \"\", \"page\": 15, \"index\": 18, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-019.webp\", \"caption\": \"\", \"page\": 15, \"index\": 19, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-020.webp\", \"caption\": \"\", \"page\": 15, \"index\": 20, \"width\": 400, \"height\": 400}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9d885f1e53fbf48d0ffb650b/fig-021.webp\", \"caption\": \"\", \"page\": 15, \"index\": 21, \"width\": 400, \"height\": 400}]"
motivation: 去散焦方法受训练数据镜头多样性不足与真实感差限制，跨相机泛化差。
method: 整合波动光学 PSF 计算、带遮挡的深度感知散焦渲染与线性空间模糊及 ISP 模拟。
result: 统一管线可规模化生成多样复合镜头的真实散焦数据集。
conclusion: 为深度感知散焦渲染与 PSF 合成提供了物理可解释的框架。
---

## Abstract
Defocus blur degrades fine image structures and limits vi-sual perception, which can adversely affect downstream vision tasks. Al-though recent deep learning deblurring methods have achieved strongperformance, their effectiveness depends on training data and often de-grades across cameras and lenses due to limited optical diversity and re-alism in existing datasets. In this paper, we propose a pipeline for synthe-sizing realistic defocus deblurring datasets for diverse compound lenses.It integrates efficient wave-optics PSF computation via Debye CZT prop-agation, depth-aware defocus rendering with occlusion handling, and blursynthesis in the radiometrically linear space with camera ISP simulation.This unified pipeline enables the scalable generation of photorealisticdefocus datasets with diverse lens characteristics. Using our pipeline,we generate CLDefocus, a large-scale synthetic dataset containing lens-diverse defocus image pairs. We further analyze the limitations of real-captured defocus datasets and show that such imperfections can biasfull-reference evaluation. Extensive experiments demonstrate that mod-els trained on CLDefocus achieve improved cross-device generalizationcompared to models trained on existing real and synthetic datasets. Codeand dataset are available at: https://github.com/lykelee/CLDefocus.

---

## 论文详细总结（自动生成）

# 论文总结：CLDefocus — 物理驱动的复合镜头散焦模糊合成

## 1. 核心问题与整体含义

- **研究动机**：散焦模糊会破坏图像精细结构，直接损害目标检测、人脸识别、语义分割等下游视觉任务。近年来基于深度学习的去散焦方法性能显著提升，但其效果高度依赖训练数据的真实性与光学多样性。
- **核心痛点**：
  - **真实拍摄数据集**（如 DPDD、RTF、RealDOF、SDD）需在不同光圈下重复拍摄同一静态场景，扩展性差，镜头多样性受限，且存在亮度变化、空间错位、残留散焦等缺陷。
  - **早期合成数据集**（如 SYNDOF）使用圆盘或高斯核近似，无法刻画镜头特有的像差与 PSF 形状。
  - **较新的波动光学合成方法**（Huygens 原理 / Rayleigh–Sommerfeld 积分）物理严谨，但采样密度要求苛刻、计算代价高，难以大规模覆盖多镜头、变深度的散焦场景。
  - 多数合成方法在非线性 sRGB 空间直接做卷积，忽略相机 ISP，破坏光度真实性。
- **整体含义**：论文提出一套统一的、物理可解释的散焦数据合成管线，并据此构建大规模、镜头多样化的合成数据集 CLDefocus，旨在从根本上解决去散焦模型的跨设备泛化问题，同时揭示真实数据集 GT 缺陷对全参考评测的偏置效应。

## 2. 方法论

### 2.1 核心思想
将「高效波动光学 PSF 计算 → 深度感知遮挡渲染 → 线性空间模糊合成 + ISP 模拟」三个环节统一为一条可扩展的合成管线。

### 2.2 关键技术细节

- **PSF 计算（第 3 节）**：
  - 采用**混合策略**：光线追迹获取出瞳球面上的波前采样 → Zernike 多项式拟合得到连续解析波前 → 通过 Debye 公式传播到传感器平面。
  - **Debye CZT**：将 Debye 衍射积分写成傅里叶形式（式 1），利用 **Chirp Z-Transform（CZT）** 替代 FFT，从而自由控制输出采样间距与 ROI，使 PSF 网格与传感器像素对齐，同时借助 Bluestein 算法保持高效。
  - **显式采样条件**（式 2）：$N > N_{\inf} = \frac{4NA^2\sqrt{n_t^2 - NA^2}|z|}{\lambda}$，并取 $N = 2N_{\inf}$ 抑制混叠；对输出网格做 $u=5$ 倍超采样后再降采样。
  - 对离轴点源，先旋转坐标系对齐光轴，再套用轴上 Debye 公式；采用标量衍射近似（低 NA、自然场景偏振可忽略）。
  - **三阶段复合镜头 PSF 流程**：①出瞳球面波前采样（含光线遮挡隐函数 → 光阑形状掩膜）；②Zernike 波前表示；③Debye CZT 衍射计算。

- **数据合成管线（第 4 节）**：
  - **镜头收集与筛选**：从 Zemax 公开库下载 1,281 个摄影定焦/变焦设计，按 F 数、总长、NA < 0.6、像差稳定性等条件筛出 **700 个镜头**。
  - **深度估计与镜头采样**：用 Depth Pro 估计单目度量深度；用近轴近似评估候选镜头，剔除 CoC 过大或采样需求过高的镜头，随机采样有效的 (镜头, 对焦距离) 对。
  - **深度感知 PSF 渲染**：
    - 按**带符号 CoC** 将深度量化成 K 层（同层内 CoC 差小于 1 像素），对被前景遮挡区域做 inpainting 并将不透明度掩膜置 1。
    - 采用**分层前后合成公式**（式 4）：$C^{\text{blur}}_i = P_i * C_i + (1 - P_i * A_i)\cdot C^{\text{blur}}_{i-1}$，从后向前累积，最终得到模糊线性图像 $I^{\text{lin}}_b = C^{\text{blur}}_K$。
  - **光度一致性**：模糊合成全程在**辐射线性空间**进行；再经逆部分 ISP 回到 RAW 域加噪，最后前向 ISP 得到 sRGB 模糊图；清晰图由同一 ISP 处理线性清晰图得到。

### 2.3 算法流程（文字概括）
RAW 清晰图块 → 部分 ISP 转线性 RGB → 深度估计 → 深度量化分层 → 按层计算 Debye CZT PSF → 线性空间分层合成 → 加噪 → 前向 ISP → 输出 sRGB 模糊–清晰成对数据。

## 3. 实验设计

- **数据集**：
  - 自建 **CLDefocus**：40,000 训练 / 1,000 验证 / 1,000 测试，分辨率 384×384；源图采用 DPDD 的 RAW 清晰图（350/74/76 划分），镜头按 420/140/140 划分，二者均不重叠。
  - 对比训练集：**DPDD**（真实拍摄）、**SYNDOF**（简化模糊模型合成）。
  - 测试集：**CLDefocus**、**RTF**、**RealDOF**、**DPDD**。
- **Benchmark 指标**：
  - 全参考：PSNR、SSIM、LPIPS。
  - 无参考：NIQE、MUSIQ、TOPIQ。
- **对比方法/模型**：主模型采用 **NRKNet**，并说明在 Restormer、NAFNet、IFAN 等其他去模糊模型上观察到相同趋势（见补充材料）。
- **额外实验**：
  - **Debye CZT vs. Rayleigh–Sommerfeld**：采样稳定性与计算耗时对比。
  - **真实 GT 缺陷分析**：几何错位、光度错位、残留模糊对全参考指标的偏置。
  - **消融实验**：w/o Lens（高斯核替代）、w/o ISP、w/o Depth。
  - **PSF 可视化**：多镜头、多视场位置的 PSF 形态展示。

## 4. 资源与算力

- 论文仅说明实现使用 **JAX**（GPU 加速数值计算）与 **ZERNIPAX**（Zernike 多项式求值），**未明确提及 GPU 型号、数量、训练总时长或具体算力规模**。
- 仅在效率对比中给出单次 PSF 计算耗时：Debye CZT **0.018 s** vs. Rayleigh–Sommerfeld（N=256）**45.1 s**；复杂度分别为 $O((N+M)^2\log(N+M))$ 与 $O(N^2M^2)$。
- 训练协议上，NRKNet 按 350,000 次迭代（等效 4,000 epoch × batch 4）匹配 DPDD 原始设置，但未报告硬件配置与墙钟时间。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 主对比：3 种训练集 × 4 个测试集 × 2 类指标（全参考 + 无参考），共约 8 张结果表组。
  - 消融：3 个组件（镜头 PSF、ISP、深度）各去掉一次，共 3 组定量 + 定性对比。
  - 方法学对比：Debye CZT 与 Rayleigh–Sommerfeld 在 7 种采样密度下的稳定性与耗时对比。
  - 真实数据集 GT 缺陷分析：几何 / 光度 / 残留模糊三类定性分析 + PSNR 反例展示。
  - PSF 可视化：多镜头 × 多视场位置示例。
- **充分性评估**：
  - **优点**：覆盖真实/合成多类基线，全参考与无参考指标并重，消融设计对应管线三大模块，且额外分析了 GT 偏置这一常被忽视的问题。
  - **公平性**：训练协议统一，镜头与源图划分不重叠，对比相对客观。
  - **潜在不足**：主模型仅 NRKNet，其他模型结果置于补充材料；消融未报告多次随机种子或统计显著性；对 CLDefocus 自身测试集存在「同分布优势」，跨数据集结论需结合全参考指标偏置谨慎解读。

## 6. 主要结论与发现

- **CLDefocus 训练模型**在自建测试集上全参考与无参考指标均最佳，验证其物理一致性与镜头多样性。
- **跨设备泛化**：在真实 benchmark（RTF、RealDOF、DPDD）上，CLDefocus 训练模型的**无参考指标整体更优**，恢复出更锐利、伪影更少的细节；DPDD 训练模型因过拟合单一镜头配置而跨镜头泛化受限，SYNDOF 因简化模糊模型泛化差。
- **全参考指标存在偏置**：真实 GT 中的几何错位、光度错位与残留散焦会使 PSNR/SSIM 偏好「保持略糊」的保守预测，与视觉质量不一致。
- **Debye CZT 优势**：具备显式采样准则、无需经验调参即可稳定生成无混叠 PSF，且计算速度远快于 Rayleigh–Sommerfeld（约 2,500 倍）。
- **消融结论**：
  - 用高斯核替代镜头 PSF → 性能显著下降，残留模糊明显；
  - 移除 ISP/噪声 → 性能明显下降；
  - 移除深度分层（单层均匀卷积）→ 整体指标仅轻微下降，但在散焦突变边缘出现集中伪影，说明深度建模对处理不连续散焦至关重要。

## 7. 优点

- **物理可解释性强**：从光线追迹 → Zernike 波前 → Debye CZT 衍射，全链条物理建模，避免经验核近似。
- **计算高效且可扩展**：CZT 提供灵活 ROI/采样控制，显式采样条件保证稳定性，支撑 700 镜头 × 变深度的大规模 PSF 生成。
- **管线完整度高**：同时处理 PSF 计算、遮挡一致的深度分层合成、线性空间模糊与 ISP 仿真，避免 sRGB 空间卷积的光度失真。
- **数据贡献扎实**：CLDefocus 规模达 4 万对，镜头与源图划分严格不重叠，并做清晰度过滤剔除低质 GT。
- **批判性分析**：主动揭示真实散焦数据集 GT 缺陷对全参考评测的偏置，为后续评测标准提供重要参考。
- **灵活性**：可控参数（模糊等级、镜头、对焦距离）支持课程学习等任务特定数据集设计。

## 8. 不足与局限

- **PSF 精度限制**：Debye 近似在**严重离轴视场**下可能不准，且无法刻画复杂光阑形状；标量衍射近似在偏振敏感或高 NA 场景不适用。
- **深度依赖**：依赖单目深度估计（Depth Pro），**深度图不精确**会导致不合理合成结果。
- **ISP 简化**：采用的 ISP 模型较简单，难以覆盖真实相机的多样化 ISP 特性，可能引入域差距。
- **评测偏差风险**：CLDefocus 测试集与训练集同源同管线，模型在其上的高分部分来自分布一致性；跨真实数据集的结论主要依赖无参考指标，而全参考指标受 GT 缺陷影响存在系统偏置。
- **算力信息缺失**：未报告 GPU 型号、数量与训练时长，复现与成本评估存在困难。
- **实验覆盖**：主模型单一（NRKNet），其他模型仅在补充材料；消融未报告方差/显著性；未涉及下游任务（检测、分割）的端到端验证。
- **应用限制**：依赖公开 Zemax 镜头库与特定 RAW 源图，镜头库代表性、源场景分布均可能影响实际部署泛化性。

（完）
