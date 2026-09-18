---
title: "Segmenting, Fast and Slow: Real-Time Open-Vocabulary Video Instance Segmentation with Dual-Path Processing"
title_zh: 快慢分割：面向实时开放词汇视频实例分割的双路径处理
authors: "Luca Barsellotti, Martin Sundermeyer, Mattia Segu, Nikita Araslanov, Muhammad Ferjad Naeem, Marcella Cornia, Yongqin Xian, Maxim Berman"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/12656.pdf"
tags: ["query:seg"]
score: 7.0
evidence: 面向移动端的实时开放词汇视频实例分割
tldr: 开放词汇视频实例分割正被DETR类目标中心模型主导，虽在像素解码与文本融合上有所加速，但在移动端实现高帧率实时推理仍是难题。本文提出SegFS双流快慢框架，在稀疏关键帧上用开放词汇目标模型预测实例表示，再投影回主干特征空间以调制轻量解码器。该设计在不牺牲精度的前提下显著提升效率，面向设备端实时分割，对移动端前景分割与实例级处理具有参考价值。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-001.webp\", \"caption\": \"\", \"page\": 6, \"index\": 1, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 720, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-009.webp\", \"caption\": \"\", \"page\": 14, \"index\": 9, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-010.webp\", \"caption\": \"\", \"page\": 14, \"index\": 10, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-011.webp\", \"caption\": \"\", \"page\": 14, \"index\": 11, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-012.webp\", \"caption\": \"\", \"page\": 14, \"index\": 12, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-013.webp\", \"caption\": \"\", \"page\": 14, \"index\": 13, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-014.webp\", \"caption\": \"\", \"page\": 14, \"index\": 14, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-015.webp\", \"caption\": \"\", \"page\": 14, \"index\": 15, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-016.webp\", \"caption\": \"\", \"page\": 14, \"index\": 16, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-017.webp\", \"caption\": \"\", \"page\": 14, \"index\": 17, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-018.webp\", \"caption\": \"\", \"page\": 14, \"index\": 18, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-019.webp\", \"caption\": \"\", \"page\": 14, \"index\": 19, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-020.webp\", \"caption\": \"\", \"page\": 14, \"index\": 20, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-021.webp\", \"caption\": \"\", \"page\": 14, \"index\": 21, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-022.webp\", \"caption\": \"\", \"page\": 14, \"index\": 22, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-023.webp\", \"caption\": \"\", \"page\": 14, \"index\": 23, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-4522c4b0ebcb1d7b0b4a68da/fig-024.webp\", \"caption\": \"\", \"page\": 14, \"index\": 24, \"width\": 1280, \"height\": 720}]"
motivation: 开放词汇视频实例分割在移动端实现高帧率实时推理仍面临效率瓶颈。
method: 提出SegFS双流快慢框架，在关键帧用开放词汇目标模型预测实例表示以调制轻量解码器。
result: 实验表明该框架在不牺牲精度的前提下显著提升推理效率，支持设备端实时分割。
conclusion: 该工作推动了开放词汇视频实例分割的移动端实时化，具较强工程参考价值。
---

## Abstract
Object-centric models inspired by DETR have become thedominant paradigm for open-vocabulary video instance segmentation(OV-VIS). While recent efforts have reduced the computational cost ofpixel decoding, textual modality fusion, and object decoding to makethese architectures more suitable for mobile devices, real-time on-deviceinference at high frame rates remains an open challenge. In this paper,we introduce SegFS, a dual-stream fast-slow framework that significantlyimproves efficiency without sacrificing accuracy. On sparse keyframes, anopen-vocabulary object-based model predicts instance-level representa-tions. These representations are then projected back into the backbonefeature space to condition a lightweight fast network, which efficientlyrelocalizes and segments the instances in subsequent frames. By shiftinginstance propagation from object decoding to feature-space condition-ing, our approach decouples multimodal semantic understanding fromdense mask prediction and enables efficient temporal propagation. Theproposed fast branch achieves up to 14× lower latency than the mobile-oriented MOBIUS model, while maintaining competitive segmentationperformance on standard OV-VIS benchmarks.

---

## 论文详细总结（自动生成）

# 论文总结：Segmenting, Fast and Slow（SegFS）

## 1. 核心问题与研究动机

- **任务背景**：开放词汇视频实例分割（OV-VIS）要求在给定任意文本类别集合的条件下，对视频中的目标进行逐帧分割、分类与跨帧跟踪，且类别可包含训练中未见的新概念。
- **主流范式**：受 DETR 启发的目标中心（object-centric）模型已成为 OV-VIS 的主导架构，通常由三部分组成——视觉骨干网络（Backbone）、特征增强器（Feature Enhancer，含像素解码器与早期文本-视觉融合）、目标解码器（Object Decoder）。
- **核心瓶颈**：尽管 MOBIUS、TROY-VIS 等工作已对像素解码与文本融合做了轻量化改造，但**特征增强器仍是压倒性的计算瓶颈**。论文图 1 显示，在 Samsung Galaxy S25 Ultra 上，特征增强器的设备端延迟远高于理论 FLOPs 所暗示的比例，且随分辨率和词表规模增长而急剧恶化。
- **研究目标**：在移动/边缘设备上实现**高帧率实时 OV-VIS**，在不显著牺牲分割精度的前提下突破算力限制。
- **整体含义**：论文提出 SegFS，一个"快慢双路径"框架——在稀疏关键帧上运行重模型（慢路径），在中间帧上运行轻量网络（快路径），将实例传播从"目标解码"转移到"特征空间条件化"，从而解耦多模态语义理解与稠密掩码预测。

## 2. 方法论

### 2.1 核心思想
- 关键帧上由慢路径（冻结的 GLEE/MOBIUS/TROY-VIS）提取高质量、文本对齐的**实例级目标嵌入**。
- 将这些嵌入**投影回骨干网络特征空间**，用于条件化一个轻量快网络；快网络直接复用骨干多尺度特征图（P2–P5），从而绕过昂贵的特征增强器与目标解码器。
- 核心直觉：**细粒度定位所需的空域语义已编码在骨干特征图中**，慢路径只需提供实例级语义即可。

### 2.2 关键技术细节

- **目标嵌入投影**：将慢路径解码出的目标嵌入经 3 层 FFN + LayerNorm 投影至快特征空间；随后分两路：
  - 分支一：按与文本类别的最大相似度选取 **Top-K 个目标嵌入**，并附加一个可学习的**背景 token**（共 K+1 个 token），经过两层自注意力与交叉注意力（以 P5 为 key/value）进行原型精炼。
  - 分支二：另一 3 层 FFN 将嵌入投影为 1×1 卷积核，用于最终掩码 logits 生成。
- **Fast Feature Aggregator（快特征聚合器）**：
  - *预处理*：将多尺度特征统一到 D=256 通道；低分辨率 {P4,P5} 用标准 1×1 卷积，高分辨率 {P2,P3} 用轻量 **DSConvGN 块**（3×3 深度卷积 + 1×1 逐点卷积 + GroupNorm + SiLU）。
  - *Object Guidance（目标引导）*：仅在最低分辨率 P5 上执行，包含两步：
    - **Object Injection**：计算 P5 每个空间单元与 K+1 个 token 的多头余弦相似度，经可学习温度 τ 缩放后按实例维 softmax，加权求和得到目标感知特征图 I5。
    - **Gated Fusion（门控融合）**：将 I5 经 DSConvGN 平滑后与原始 P5 融合，公式为：
      **Ṗ5 = P5 + σ(GateConv(P5 ∥ I5)) ⊙ DSConvGN(I5)**
      其中 σ 为 sigmoid，门控卷积预测空间混合掩码，既保留 P5 的精确视觉线索，又吸收 I5 的实例语义。
  - *渐进上采样*：将增强后的 Ṗ5 逐级上采样并与 P4、P3、P2 拼接融合（DSConvGN），最终经 1×1 卷积（以关键帧目标嵌入为卷积核）生成 N 个掩码激活。
- **训练策略**：在图像实例分割数据集上训练，无需视频标注。每次迭代图像依次经过慢、快两路；使用混合匹配代价（慢网络的类别 logits 与框预测 + 快网络的掩码预测）做匈牙利匹配，再由 Mask 与 DICE 损失监督快网络。
- **跟踪**：沿用 MinVIS 的 tracking-by-matching 范式，在整段视频上复用关键帧目标嵌入进行时序关联。

## 3. 实验设计

- **训练数据**（统一训练阶段，参照 MOBIUS）：
  - 图像实例分割：COCO、LVIS、BDD
  - 视频实例分割（作为图像使用）：YouTubeVIS19/21、OVIS
  - 指代分割：RefCOCO、RefCOCO+、RefCOCOg、RVOS
  - 开放世界分割：UVO、SA-1B（类别名统一为 "object"）
  - 排除了 Objects365、OpenImages 等检测数据集。
- **评测 Benchmark**：
  - 训练中见过的视频数据集：**YouTubeVIS19**（2,883 视频，40 类）、**OVIS**（901 视频，25 类，严重遮挡）。
  - 零样本开放世界大数据集：**BURST**（2,907 视频，425 基类/57 新类）、**LV-VIS**（4,828 视频，1,196 类）。
  - 输入统一缩放至短边 480 像素，T=5 帧传播，报告各数据集标准指标（AP、AP50、AP75、HOTA、mAP 等）。
- **慢网络（冻结）配置**：MOBIUS（MNv4-CM / MNv4-CL / ResNet50）、GLEE-Lite（ResNet50）、TROY-VIS（EfficientViT-L2），共 5 种。
- **对比方法**：
  - **Copy**：直接复制关键帧掩码（下界）。
  - **Reuse Objects**：在中间帧跳过目标解码器，复用关键帧实例嵌入（上界参考，类似 MobileInst/TROY-VIS 思路）。
  - **光流类**：RAFT（单次迭代）、LiteFlowNet2，通过光流 warp 关键帧掩码。
  - **MPVSS**：唯一已有的双网络传播方法（原为闭集 Mask2Former 设计），论文在其上重新训练以适配 OV-VIS 场景。
- **效率评测**：在 Samsung Galaxy S25 Ultra、Snapdragon 8 Gen 5、Snapdragon X2 Elite、XR2 Gen 2（Meta Quest 3）及 NVIDIA A100/T4 上测延迟；边缘设备通过 Qualcomm AI Hub 编译为 NPU 执行。摊销 FPS 按 6 帧跨度（1 关键帧 + 5 中间帧）计算。

## 4. 资源与算力

- **训练硬件**：明确提到使用 **4 张 NVIDIA A100 GPU**。
- **训练配置**：batch size 128，训练 **500,000 次迭代**，学习率 1e-4，多尺度训练；慢网络保持冻结，输出 300 个目标查询，选取 Top-50 用于 Object Guidance。
- **消融实验**：部分消融（如表 3、K 敏感性分析）使用 **100k 次迭代** 的较短训练配方。
- **推理评测**：边缘设备延迟在 Qualcomm AI Hub 上编译测量；GPU 延迟在 A100/T4 上测量。输入分辨率 480×480，词表 40 类。

## 5. 实验数量与充分性

- **主实验（表 1）**：5 种慢网络 × 7 种快路径方案（Copy、Reuse Objects、LiteFlowNet2、RAFT、MPVSS、SegFS，含上下界）在 4 个数据集（YouTubeVIS19、OVIS、BURST、LV-VIS）上全面对比，规模较大。
- **效率实验（表 2）**：5 种慢模型 + 4 种快路径基线 + 4 种 SegFS 配置，在 4 种边缘设备 + 2 种 GPU 上报告 FLOPs、参数量与延迟。
- **消融实验**：
  - 表 3：4 个模型组件（Injection、Background Token、Attention Proj.、Smoothing）的逐项消融，基于 MOBIUS-Mini-M。
  - 图 5：传播间隔 T ∈ [1,10] 的性能分析，覆盖全部 4 个数据集。
  - 图 6：K ∈ {10,20,...,100} 的敏感性分析，以及 T 与摊销 FPS 的关系。
- **定性结果**：图 7 展示 YouTubeVIS19 上与 MPVSS 的逐帧对比。
- **充分性评价**：
  - **优点**：覆盖多种骨干网络、多种数据集、多种传播策略，实验设计较为全面；对比基线既包含上下界（Copy/Reuse Objects），也包含强竞争者（MPVSS、光流方法），并公平地在其上重新训练 MPVSS。
  - **客观性**：慢网络统一冻结、统一训练配方，比较相对公平。
  - **局限**：消融实验仅基于 MOBIUS-Mini-M 一种慢网络，未在所有配置上验证组件贡献；部分实验（K 敏感性）训练轮数减少至 100k。

## 6. 主要结论与发现

- **效率**：SegFS 快路径相比 MOBIUS 最高实现 **14× 延迟降低**；在 MOBIUS 系列慢模型上，SegFS 是**唯一能跨越 30 FPS 实时阈值**的方法，摊销 FPS 约为基线 3 倍。
- **精度**：在标准 OV-VIS 基准上保持与参考上界（Reuse Objects）相当甚至更优的性能，精度下降控制在 **≤1 AP** 以内（部分配置如 MNv4-CM/MNv4-CL 上甚至持平或超越 Reuse Objects）。
- **核心验证**：证明了当目标只是传播已检测实例时，**昂贵的特征增强器是冗余的**；将实例嵌入注入骨干特征空间即可实现高质量重定位。
- **最优搭配**：SegFS 与 TROY-VIS 组合精度最高（因其将表征能力更多分配给骨干），但也是延迟最高的配置。
- **传播间隔分析**：传播语义嵌入的方法（Reuse Objects、MPVSS、SegFS）随 T 增大退化缓慢；而传播/ warp 像素级掩码的方法（Copy、RAFT、LiteFlowNet2）退化迅速。验证了"携带语义表征"优于"直接 warp 掩码"的直觉。
- **K 敏感性**：AP 在 K=50 时达到峰值，之后趋于平台；K 从 10 到 100 的开销增加可忽略（投影 0.245→0.340 GFLOPs，快聚合器 6.323→6.333 GFLOPs）。
- **实用部署建议**：在 30 FPS（33 ms/帧）场景下，可在每帧捕获后立即执行快聚合器（8.3 ms），其余约 25 ms 与慢路径计算重叠，对应 T≈5–6。

## 7. 优点

- **方法设计亮点**：
  - 提出清晰的双路径范式，将"多模态语义理解"与"稠密掩码预测"解耦，思路简洁而有效。
  - 将实例传播从目标解码层移至特征空间条件化，避免了光流估计与掩码 warp 的累积误差。
  - Object Guidance 的余弦相似度注入 + 门控融合设计巧妙，既保留骨干精确视觉线索，又注入实例语义。
  - 快网络通道统一为 256，使其计算开销与骨干容量基本解耦，工程可移植性强。
- **实验亮点**：
  - 训练仅用图像数据，无需昂贵的视频标注。
  - 评测覆盖 4 类数据集、5 种慢网络、6 种硬件平台，兼顾精度与真实设备延迟。
  - 引入 Copy 与 Reuse Objects 上下界，使各方法差异可解释为"传播损失"与"架构损失"。
  - 公平地重新训练并适配 MPVSS 到 OV-VIS 场景，对比客观。
  - 提供实用的部署策略分析（计算重叠、T 的选择）。

## 8. 不足与局限

- **精度损失**：在部分配置（如 GLEE-Lite/ResNet50）下，SegFS 相比 Reuse Objects 上界仍有约 4–5 AP 的下降，说明快路径的语义注入能力仍有提升空间。
- **消融覆盖有限**：模型组件消融仅在 MOBIUS-Mini-M 上完成，未验证在其他慢网络/骨干下的泛化性；K 敏感性实验训练轮数减半。
- **慢路径依赖**：方法建立在已有冻结 OV-VIS 模型之上，整体系统性能受慢网络质量制约；关键帧上的慢路径延迟仍然很高（如 GLEE ResNet50 达 587.9 ms），论文未深入讨论关键帧调度频率的自适应策略。
- **应用限制**：
  - 评测分辨率统一为 480×480、词表 40 类，更高分辨率与大词表场景下的表现未充分验证。
  - 边缘设备延迟依赖 Qualcomm AI Hub 的 NPU 编译，可能与其他部署栈存在差异。
  - 未涉及长时视频中的目标重现（re-identification）、严重遮挡下的身份保持等更复杂跟踪问题（OVIS 上精度下降即为例证）。
- **对比局限**：未与 SAM2 等基于记忆库的传播方法进行实验对比（文中仅定性提及），尽管作者解释了不采用其范式的原因。
- **偏差风险**：训练语料为作者自选的统一数据集组合，可能与某些基线的原始训练配方存在差异，影响跨方法比较的绝对公平性。

（完）
