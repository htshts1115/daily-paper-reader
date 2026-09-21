---
title: Towards Photorealistic and Efficient Bokeh Rendering via Diffusion Framework
title_zh: 面向真实感与高效率散景渲染的扩散框架
authors: "Shi, Linxiao, Zheng, Siming, Wang, Zerong, Zhang, Hao, Chen, Jinwei, Li, Bo, Chen, Shifeng, Jiang, Peng-Tao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_Towards_Photorealistic_and_Efficient_Bokeh_Rendering_via_Diffusion_Framework_CVPR_2026_paper.pdf"
tags: ["query:neural-bokeh"]
score: 9.0
evidence: 面向手机的高效神经散景渲染统一扩散框架
tldr: 针对手机小光圈难以产生自然散景、且高倍变焦下细节丢失、两步式增强加渲染效率低的问题，论文提出MagicBokeh统一扩散式散景渲染框架。它采用交替训练策略与聚焦机制，在单一网络中同时完成画质增强与散景合成，避免误差累积。实验表明该方法在高质量与高效率上均优于现有学习式方法，为移动端人像虚化提供实用方案。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 675, \"height\": 702}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 675, \"height\": 702}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 675, \"height\": 702}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 6, \"index\": 9, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 596, \"height\": 391}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 596, \"height\": 391}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 597, \"height\": 392}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 598, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 596, \"height\": 392}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 595, \"height\": 391}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 584, \"height\": 391}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 6, \"index\": 17, \"width\": 584, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 6, \"index\": 18, \"width\": 584, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 584, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 6, \"index\": 20, \"width\": 584, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 6, \"index\": 21, \"width\": 584, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 812, \"height\": 536}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 8, \"index\": 23, \"width\": 408, \"height\": 439}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-shi-towards-photorealistic-and-efficient-bokeh-rendering-via-diffusion-framework-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 408, \"height\": 439}]"
motivation: 手机小光圈难以生成自然散景，现有学习式方法在高倍变焦下细节损失严重，两步式流水线效率低。
method: 提出MagicBokeh统一扩散框架，通过交替训练策略与聚焦机制同时完成画质增强与散景渲染。
result: 实验表明该方法在保持真实感散景的同时显著提升效率，优于现有学习式方法。
conclusion: 为移动端神经散景渲染提供统一高效的高质量框架。
---

## Abstract
Existing mobile devices are constrained by compact optical designs, such as small apertures, which make it difficult to produce natural, optically realistic bokeh effects. Although recent learning-based methods have shown promising results, they still struggle with photos captured under high digital zoom levels, which often suffer from reduced resolution and loss of fine details. A naive solution is to enhance image quality before applying bokeh rendering, yet this two-stage pipeline reduces efficiency and introduces unnecessary error accumulation. To overcome these limitations, we propose MagicBokeh, a unified diffusion-based framework designed for high-quality and efficient bokeh rendering. Through an alternative training strategy and a focus-aware masked attention mechanism, our method jointly optimizes bokeh rendering and super-resolution, substantially improving both controllability and visual fidelity. Furthermore, we introduce degradation-aware depth module to enable more accurate depth estimation from low-quality inputs. Experimental results demonstrate that MagicBokeh efficiently produces photorealistic bokeh effects, particularly on real-world low-resolution images, paving the way for future advancements in bokeh rendering. Our code and models are available at this \href https://github.com/vivoCameraResearch/MagicBokeh url .

---

## 论文详细总结（自动生成）

# MagicBokeh：面向真实感与高效率散景渲染的扩散框架——论文深度总结

## 1. 核心问题与整体含义（研究动机与背景）

- **硬件瓶颈**：移动设备受限于紧凑光学设计（小光圈等），难以直接拍摄出自然、符合光学规律的真实散景（bokeh）效果。
- **现有方法的局限**：
  - 经典方法依赖光线追踪或物理光学模型，计算复杂度随采样空间指数增长，难以实时渲染；且依赖完美的深度/视差图，在真实场景中往往产生不自然的局部遮挡伪影或颜色渗漏。
  - 基于学习的方法（如 BokehMe、MPIB、EBokehNet、BokehDiff）虽能改善伪影，但**普遍假设输入是高质量、全聚焦图像**，无法应对高倍数字变焦场景（放大 5×–15×）中出现的噪声放大、主体边界模糊、纹理合成失真等问题。
- **两阶段流水线的缺陷**：先做真实世界图像超分辨率（Real-ISR），再做散景渲染，会带来两个问题——① Real-ISR 输出不完美导致**误差累积**，在后续散景渲染中被进一步放大；② 需要两次独立模型推理，**效率低下**。
- **关键观察与动机**：扩散模型（如 Stable Diffusion）在生成细粒度细节上具有优势，且生成的图像本身常带有散景先验（bokeh prior）。由此作者提出疑问：能否设计一个**统一的单步扩散框架**，同时提升高倍变焦摄影下散景渲染的质量与效率？该工作即 MagicBokeh。

## 2. 方法论：核心思想与关键技术细节

### 2.1 总体架构（两个主要部分）
- **单步 HQ 特征提取（Single-Step HQ Feature Extraction）**：直接将 LQ 图像（不加噪声）输入，最大化保留语义内容并消除随机噪声采样的不确定性；在 VAE 编码器（仅第一阶段训练）与改造后的轻量 U-Net 中注入 LoRA，用 L2 损失 + LPIPS 损失监督微调。
- **可控散景渲染（Controllable Bokeh Rendering）**：引入 ControlNet 作为条件控制模块，以**散焦图（defocus map）**为结构条件，散焦半径计算为：

  $$r = K\,|d - d_f|$$

  其中 $d$ 为像素视差，$d_f$ 为用户指定的对焦位置视差，$K$ 为模糊强度，$r$ 为模糊半径。由此可生成具有可控景深（DoF）、同时保持对焦区域语义一致性的散景效果。

### 2.2 交替训练策略（Alternative Training Strategy）
- **问题**：将 Real-ISR 与散景渲染端到端联合训练时，两任务优化目标冲突，且两任务训练样本数量不均衡，导致网络偏向单一任务，主体区域的 ISR 质量下降。
- **方案**：先以超分预训练初始化模型（获得较强的 Real-ISR 能力）；随后**循环交替**两个训练阶段：
  - **散景渲染阶段**：固定原始扩散模型与预训练 HQ 特征提取模型，仅训练 ControlNet 与焦点感知掩码注意力中的 bokeh LoRA 层；输入为 LQ 全聚焦图像 + 散焦图条件。
  - **Real-ISR 阶段**：输入 LQ–HQ 图像对，散焦图设为**全零**（表示全聚焦条件），仅优化 U-Net 中的 SR LoRA 层。
- 通过交替切换任务焦点，有效减少任务间干扰。

### 2.3 焦点感知掩码注意力（Focus-aware Mask Attention, FAMA）
- **问题**：直接把散景条件注入生成过程，常导致对焦区域恢复质量下降。
- **方案**：利用散焦图提取主体信息并二值化，构造焦点注意力掩码 $M$，调制自注意力：

  $$\text{Attention} = \text{softmax}\left(\frac{QK^\top + M}{\sqrt{d}}\right)V$$

  掩码定义为：$M(x,y)=0$ 当该位置属于焦点区域，否则为 $-\infty$。
- **效果**：将视差图划分为前/背景二值区域，约束自注意力在各区域内操作，使 ISR 分支专注对焦主体、散景分支专注背景虚化。在 Real-ISR 阶段掩码 $M$ 置 0 以恢复整幅图像。

### 2.4 退化感知深度估计（Degradation-aware Depth Estimation）
- **问题**：Depth Anything v2 在高质量数据上表现优异，但在 LQ 图像上精度急剧下降，错误的视差图会劣化 SR 散景渲染结果。
- **方案**：采用**自特征蒸馏**框架，以预训练 Depth Anything v2 同时作为教师与学生网络；教师输入 HQ 图像，学生输入模拟退化图像，通过编码器特征蒸馏与输出监督使二者特征保持一致，从而提升 LQ 输入下深度估计的鲁棒性与准确性。

### 2.5 效率优化（模型压缩）
- 基于 SD2.1，通过**块剪枝（block pruning）**移除 U-Net 中全部交叉注意力层与中间阶段模块，并去除文本编码器，消除 prompt 依赖、降低计算开销；LoRA 注入 VAE 编码器与轻量 U-Net。

## 3. 实验设计

### 3.1 数据集与场景
- **训练数据**：HQ 特征提取模型在 LSDIR 及 FFHQ 的 1 万张人脸子集上训练；散景 GT 由作者自建的**基于光线追踪的薄透镜渲染器**生成；LQ–HQ 图像对用 **Real-ESRGAN 退化管线**合成，LQ 图像上采样至 512×512 后输入模型。
- **Benchmark**：
  - **EBB400-LQ**：从 EBB 数据集随机选取 400 对图像并人工标注对焦区域，并用 Real-ESRGAN 管线模拟退化，用于高倍变焦散景渲染评测。
  - **真实世界用户研究**：用 iPhone 13 Pro 采集 50 张真实 LQ 图像（人像、风景、室内外场景，5×–15× 变焦，平均分辨率 4032×3024）。

### 3.2 对比方法
- **两阶段流水线**：SOTA 单步 Real-ISR 方法 **OSEDiff**、**S3Diff** 分别搭配散景渲染方法 **BokehMe**、**Dr.Bokeh**、**BokehDiff**。
- **公平性处理**：对比方法在得到 SR 图像后使用 Depth Anything v2 生成视差图；MagicBokeh 则用退化感知深度模块从原始 LQ 输入估计更鲁棒的视差图；所有视差图归一化到 0–1。

### 3.3 评价指标
- 全参考指标：PSNR、SSIM、LPIPS、DISTS、FID；
- 无参考指标：NIQE、MANIQA、MUSIQ、CLIP-IQA；
- 效率指标：推理时间（512×512 输入，L40s GPU）；
- 主观评价：50 名参与者的用户偏好研究。

## 4. 资源与算力

- **训练硬件与时长**：文中明确说明整个训练过程在 **4 张 NVIDIA L40 GPU** 上进行，耗时约 **20 小时**。
- **推理测试硬件**：推理时间在 **L40s GPU** 上测量（512×512 输入）。
- **优化器与学习率**：AdamW；HQ 特征提取与散景阶段学习率 5e-5，Real-ISR 阶段学习率 5e-6；训练时使用随机水平翻转增强数据。
- 未明确说明具体显存占用、批大小与总迭代步数等更细粒度算力信息。

## 5. 实验数量与充分性

- **主要对比实验**：在 EBB400-LQ 上与 6 组两阶段基线组合（2 种 ISR × 3 种散景渲染）进行定量对比，并给出定性可视化（图 4）。
- **用户研究**：50 名参与者对真实世界高倍变焦图像做主观偏好选择。
- **消融实验**：针对三个核心组件——FAMA、交替训练策略、退化感知深度模块，共构造 **4 组变体**（w/o FAMA、w/o Strategy、w/o DA depth 及完整模型）在 EBB400-LQ 上评测，并配有可视化对比（图 6）。
- **扩展应用实验**：重聚焦（refocusing）任务演示。
- **充分性与客观性评估**：
  - **优点**：覆盖合成退化与真实场景、定量 + 定性 + 主观三类评估；消融设计针对性强，能验证各组件贡献；对比方法涵盖 SOTA 且注明所用视差图来源。
  - **不足**：消融实验仅在单一数据集（EBB400-LQ）上进行；用户研究样本量（50 人、50 张图）相对有限；作者自己也指出在部分无参考指标上不如 BokehDiff，并解释为 BokehDiff 在 EBB400-LQ 上产生错误对焦分布所致——这一解释虽合理，但客观上说明定量比较存在指标失真风险。

## 6. 主要结论与发现

- MagicBokeh 是**首个专为高倍变焦散景渲染设计的统一单步扩散框架**，在单一架构中同时完成 Real-ISR 与散景渲染，避免了传统两阶段方法的误差累积与低效率。
- 在 EBB400-LQ 上取得 SOTA 定量结果：PSNR 24.23、SSIM 0.8623、LPIPS 0.2786、DISTS 0.1600，推理时间仅 **0.1062 s**，显著快于所有对比的两阶段方法（如 Dr.Bokeh+ 达 2.99 s）。
- 用户研究中获得 **71.7% 的人类偏好率**，远超其他方法组合。
- 消融实验证实：FAMA 能有效解耦对焦主体与离焦区域（显著提升无参考指标）；交替训练策略提升散景渲染质量；退化感知深度模块在定性上改善了 LQ 图像的深度估计质量。
- 方法还能泛化到**重聚焦（refocusing）**任务，实现从咖啡杯到背景椅子的平滑焦点转移。
- 即使不使用任何文本条件，MagicBokeh 在 Real-ISR 任务上相比单步 Real-ISR 方法仍表现良好。

## 7. 优点

- **方法创新性**：首次将 Real-ISR 与散景渲染统一进单步扩散框架，直击高倍变焦移动摄影的真实痛点，工程与学术价值兼具。
- **训练策略巧妙**：交替训练 + 全零散焦图复用，有效缓解两任务目标冲突与样本不均衡问题，无需复杂多任务损失设计。
- **FAMA 机制**：利用散焦图二值化掩码调制自注意力，显式解耦前景恢复与背景虚化，思路清晰且可解释性强。
- **效率优化务实**：通过块剪枝去除交叉注意力、文本编码器与中间模块，在移动端部署友好；推理时间仅 0.1062 s，具备实用价值。
- **深度估计鲁棒性**：退化感知深度模块以自蒸馏方式提升 LQ 输入下的深度估计，解决了两阶段方案依赖 SR 输出质量的问题。
- **实验设计较全面**：合成退化 + 真实场景 + 用户研究 + 消融 + 扩展应用，多维度验证方法有效性；公平性方面主动说明各方法视差图来源。

## 8. 不足与局限

- **指标表现存在争议**：在部分无参考指标（如 MUSIQ、MANIQA）上未全面领先，作者将其归因于 BokehDiff 产生错误对焦分布导致指标虚高，但这说明定量指标与实际感知质量存在偏差，评测体系仍不完美。
- **消融实验覆盖有限**：所有消融均在 EBB400-LQ 单一数据集上完成，未在真实世界数据集上做消融，结论的泛化性有待进一步验证。
- **深度模块增益有限**：退化感知深度模块在定量指标上提升不显著，仅通过定性对比体现优势，缺乏更客观的量化证据（如深度估计精度指标）。
- **用户研究规模偏小**：50 名参与者、50 张图像，覆盖场景与人群代表性有限，主观结论的统计稳健性存疑。
- **训练数据依赖合成**：散景 GT 来自自建光线追踪渲染器，与真实光学散景可能存在域差距；LQ 退化用 Real-ESRGAN 模拟，难以完全复现真实手机高倍变焦的混合噪声、运动模糊与有损压缩。
- **公平性细节存疑**：两阶段对比方法使用 SR 图像后由 Depth Anything v2 生成视差图，而本文方法使用原始 LQ 输入 + 退化感知深度模块，输入条件不完全对等，可能对基线不利。
- **应用限制**：仅验证了 512×512 分辨率下的推理效率，未报告高分辨率（如 4032×3024 原始拍摄尺寸）下的实际运行表现与显存占用；未讨论视频流等实时场景的适用性。

（完）
