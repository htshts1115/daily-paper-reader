---
title: "BokehCrafter: Taming Video Diffusion Models for Controllable Bokeh Rendering"
title_zh: BokehCrafter：驾驭视频扩散模型实现可控散景渲染
authors: "Qiwen Wang, Liao Shen, Jiaqi Li, Tianqi Liu, Huiqiang Sun, Zihao Huang, Yachuan Huang, Xianrui Luo, Zhiguo Cao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37969/41931"
tags: ["query:neural-bokeh"]
score: 8.0
evidence: 面向可控散景渲染的视频扩散框架，实现时序一致散景
tldr: 现有散景渲染方法多依赖视差图与焦距、模糊半径等输入，在视频场景中难以保持时序一致性。本文提出BokehCrafter，首个面向视频的散景渲染扩散框架，通过双流注意力整合参考图像分支与渲染分支，从全焦视频生成时序连贯、视觉美观的散景效果。该方法在保持用户友好输入条件的同时显著提升了视频散景的稳定性与真实感，拓展了神经散景渲染的应用范围。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37969/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1838, \"height\": 543}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37969/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1833, \"height\": 692}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37969/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1846, \"height\": 552}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37969/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1844, \"height\": 924}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37969/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1842, \"height\": 576}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37969/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1847, \"height\": 460}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37969/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 888, \"height\": 263}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37969/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 875, \"height\": 346}]"
motivation: 现有散景渲染依赖视差图等输入，视频场景下时序一致性差。
method: 提出首个视频扩散散景框架，用双流注意力整合参考图像与渲染分支。
result: 从全焦视频生成时序连贯且视觉美观的散景效果。
conclusion: 将神经散景渲染从单图扩展到时序一致的视频场景。
---

## Abstract
Bokeh is used in photography to emphasize the selected subject by smoothly blurring the out-of-focus region with appealing highlights. While recent advances have achieved impressive results in rendering realistic blur, existing frameworks typically rely on disparity maps and bokeh-relevant inputs (e.g., focal distance and blur size), and face significant challenges in video bokeh rendering due to limited temporal consistency. In this paper, we propose BokehCrafter, the first video diffusion framework that generates temporally coherent and visually pleasing bokeh effects from all-in-focus video inputs under user-friendly input conditions. Specifically, we leverage a dual-stream attention mechanism, integrating a reference image branch and a rendering instruction branch. We propose a Bokeh Image Extraction (BIE) module and a CLIP-based text encoder to extract image and text features, respectively, whose outputs are fused via a Text-Image Fusion (TIF) module to enable fine-grained and controllable bokeh rendering. To support the novel capabilities of our model, we construct Video Bokeh Scenes (VBS), a large-scale dataset containing a wide variety of bokeh videos with corresponding rendering instructions, across various scenes and rendering settings. Extensive experiments demonstrate that our method significantly outperforms state-of-the-art methods in both bokeh rendering quality and temporal consistency.

---

## 论文详细总结（自动生成）

# BokehCrafter 论文中文总结

## 1. 核心问题与整体含义

- **研究背景**：散景（Bokeh）是摄影中通过平滑虚化焦外区域、形成美观高光来突出主体的效果。高质量散景通常依赖专业设备与经验，因此从全焦图像/视频生成可控散景具有实际价值。
- **现有问题**：
  - 经典与神经散景渲染方法多针对**单张全焦图像**，缺乏视频时序一致性建模，逐帧渲染易产生闪烁和伪影。
  - 多数方法强依赖**视差图/深度图**，渲染质量受深度估计精度影响明显。
  - 可控渲染常需输入**焦距、模糊半径等镜头参数**，对普通用户不够友好。
- **整体含义**：论文提出 **BokehCrafter**，声称是首个面向视频散景渲染的视频扩散框架，目标是在仅给定**全焦视频、文本渲染指令、参考散景图像**的条件下，生成时序连贯、视觉美观且可控的散景视频，从而把神经散景渲染从单图扩展到视频场景。

## 2. 方法论

- **核心思想**：将视频散景渲染建模为条件去噪扩散过程，在预训练视频 VAE 的潜空间中完成扩散，并利用文本指令与参考图像共同控制散景风格。
- **问题形式化**：
  - 输入：全焦视频 \(V_{aif}\)、文本指令 \(T\)、参考散景图像 \(I_{ref}\)。
  - 目标：建模条件分布 \(p(V_{bok} | V_{aif}, I_{ref}, T)\)。
  - 视频先经 VAE 编码为潜变量 \(Z_0\)，加噪后训练去噪网络 \(\epsilon_\theta\)，损失为预测噪声与真实噪声的均方误差。
- **网络架构**：
  - **BIE（Bokeh Image Extraction）模块**：用 CLIP 图像编码器提取参考图密集视觉特征 \(F_{img}\)，再通过一组可学习 query token 和 Q-Former 交叉注意力，提取与散景风格相关的紧凑表示 \(F_{bok}\)，如模糊模式、模糊强度等，而非记忆参考图场景内容。
  - **TIF（Text-Image Fusion）模块**：采用双流交叉注意力。文本特征 \(F_{txt}\) 与散景图像特征 \(F_{bok}\) 分别与骨干特征 \(F_{in}\) 做交叉注意力，再相加融合：  
    \(F_{out} = TCA(F_{in}, F_{txt}) + ICA(F_{in}, F_{bok})\)。
  - 融合后的条件特征引导去噪 U-Net，最终由 VAE 解码为散景视频。
- **训练与推理策略**：
  - **Reference Content Decoupling（RCD）**：训练时从不同场景但相同散景条件下选择参考帧，避免模型过拟合参考图场景内容，更贴近推理时用户无法提供同场景散景参考的情况。
  - **Condition Dropout**：训练时随机丢弃图像条件、文本条件或二者同时丢弃，各占 5%，增强模型在部分条件缺失下的鲁棒性。
  - **Dual-Condition Classifier-Free Guidance**：推理时分别计算无条件、仅图像条件、图像+文本条件的噪声预测，再按图像引导强度 \(\lambda_I\) 和文本引导强度 \(\lambda_T\) 组合，实现双条件控制。
- **数据构建相关公式**：散景模糊半径简化为 \(r = K \cdot (1/z - 1/z_f)\)，其中 \(K\) 为模糊大小，\(z\) 为像素深度，\(z_f\) 为焦平面深度。

## 3. 实验设计

- **数据集/场景**：
  - 论文构建 **Video Bokeh Scenes（VBS）** 数据集，包含 6,100 个多样化场景，其中 5,760 训练、300 测试、40 验证。
  - 每个场景在 5 个焦距和 3 个模糊大小下渲染，得到 15 个散景变体，总计 86,400 训练视频、4,500 测试视频、600 验证视频；整体 91.5k 视频、超 140 万帧。
  - 场景分布：室内/室外约 47%/53%；白天 76%，黄昏 6%，夜晚 18%。指令长度 90% 以上在 12–16 词。
  - 另收集 **Expert Ref Set**：用专业 DSLR 在不同光学条件下拍摄的真实散景图像，推理时作为参考图池。
- **Benchmark**：由于现有 SVB 视频散景数据集不公开，所有评估均在自建 VBS 上进行，并按小、中、大模糊尺寸分组评测。
- **评价指标**：
  - 渲染质量：PSNR、SSIM、LPIPS。
  - 时序一致性：基于相邻帧差分误差的公式，值越低越好。
- **对比方法**：
  - 经典渲染：RVR、SteReFo；其中 RVR† 加入权重归一化以缓解深度不连续伪影。
  - 神经渲染：DeepLens、MPIB、BokehMe、VBR。
- **用户研究**：
  - 收集 30 个真实世界视频，分辨率 1024×576，生成相同设置下的散景视频。
  - 91 名志愿者进行成对比较，随机顺序与位置，选择感知质量更好、更真实的方法。
- **消融实验**：分别验证 RCD、BIE、TIF 的有效性。

## 4. 资源与算力

- 论文明确提到：
  - 使用 **8 张 A100 GPU** 训练。
  - 初始学习率 \(1 \times 10^{-5}\)，batch size 为 8，训练 **50K steps**。
  - 采样使用 DDIM 与双条件 classifier-free guidance。
  - 对输入视频应用随机缩放和平移增强。
- 未明确说明：
  - 总训练时长、总 GPU 小时数、能耗、推理硬件配置、推理单视频耗时等。
  - 因此算力成本只能部分判断，完整训练开销信息不足。

## 5. 实验数量与充分性

- **主要实验组数**：
  - 表 1：在 VBS 上按小/中/大模糊尺寸，对比 6 个基线方法及本文方法，共多组定量结果。
  - 表 2：3 组消融实验：w/o RCD、w/o BIE、w/o TIF。
  - 表 3：6 组用户偏好对比，分别对 RVR†、SteReFo、DeepLens、MPIB、BokehMe、VBR。
  - 另有定性比较、真实视频可视化比较；论文还提到对视差图加腐坏后评估，但细节在补充材料。
- **充分性**：
  - 定量、定性、消融和用户研究均有覆盖，实验设计较完整。
  - 用户研究规模为 91 人、30 个真实视频，能提供主观偏好证据。
- **客观与公平性**：
  - 所有方法在相同 VBS 测试集上比较，RVR 做了权重归一化增强，较公平。
  - 但 SVB 数据集不公开，无法在第三方视频散景 benchmark 上验证，存在单一数据集偏差风险。
  - 本文方法不需要视差图和镜头参数，而多数基线需要，输入条件并不完全对等；这既是方法优势，也意味着比较目标偏向“用户友好可控渲染”而非严格同条件复现。

## 6. 主要结论与发现

- BokehCrafter 在 VBS 上取得最佳 PSNR、SSIM、LPIPS 和时序一致性，优于 RVR、SteReFo、DeepLens、MPIB、BokehMe、VBR。
- 方法无需视差图、焦距或模糊大小等参数，仅依赖文本指令和参考散景图像，用户控制更直观。
- 视频扩散模型中的时序注意力层带来天然的帧间一致性优势。
- 消融表明：
  - 使用不同场景参考图训练优于同场景参考图，说明 RCD 能减少过拟合。
  - 去掉 BIE 后质量显著下降，说明 Q-Former 对参考图散景特征的解析很关键。
  - 去掉 TIF 后仅保留文本流，渲染质量下降，说明参考图条件对理解目标散景风格重要。
- 用户研究显示用户明显偏好本文方法，对 DeepLens 的偏好优势最大，对 VBR 的优势为 62.35% / 37.65%。

## 7. 优点

- **任务新颖**：首次将视频扩散模型系统用于可控视频散景渲染。
- **输入友好**：摆脱视差图和复杂镜头参数，改为文本指令+参考图像，更接近普通用户使用方式。
- **架构设计合理**：BIE 提取风格化散景特征，TIF 双流融合文本与图像条件，兼顾语义控制与视觉风格控制。
- **训练策略有针对性**：RCD、Condition Dropout、双条件 CFG 分别针对泛化、鲁棒性和可控性。
- **数据集贡献**：VBS 规模较大，包含多场景、多焦距、多模糊大小及对应文本指令，并补充 Expert Ref Set。
- **实验较全面**：定量、定性、消融、真实视频用户研究结合，结论支撑较强。

## 8. 不足与局限

- **推理成本高**：作为视频扩散模型，需要多步去噪，计算开销较大；论文也将其列为未来工作。
- **训练开销报告不完整**：仅给出 8×A100、50K steps，未说明总时长、GPU 小时和能耗。
- **评测覆盖有限**：由于 SVB 不公开，只在自建 VBS 上评测，缺少公开第三方视频散景 benchmark 验证。
- **合成数据域差距**：VBS 的配对散景视频主要由渲染引擎生成，虽然使用真实视频和真实 Expert Ref Set 做补充，但仍可能存在合成到真实的域偏移。
- **用户研究细节有限**：虽有人类偏好实验，但未详细报告参与者背景、视频内容分布、置信区间或显著性检验。
- **条件依赖风险**：参考图像和文本指令的质量会影响结果；若用户难以提供合适参考图，实际可用性可能受限。
- **比较公平性可讨论**：基线多依赖视差图和镜头参数，而本文方法使用不同输入条件；虽然体现用户友好优势，但也使“同条件公平比较”存在一定解释空间。
- **超参数与失败案例分析不足**：双条件 CFG 的 \(\lambda_I\)、\(\lambda_T\) 选择影响、文本指令敏感性、极端场景失败案例等未充分展开。

（完）
