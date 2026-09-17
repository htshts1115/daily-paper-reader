---
title: Zero-shot Depth from Defocus
title_zh: 零样本散焦深度估计
authors: "Yiming Zuo, Hongyu Wen, Venkat Subramanian, Patrick Chen, Karhan Kayan, Mario Bijelic, Felix Heide, Jia Deng"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/3173.pdf"
tags: ["query:mono-depth"]
score: 7.0
evidence: 散焦深度的零样本泛化
tldr: 针对散焦深度估计(DfD)方法易过拟合并缺乏零样本泛化的问题，本文提出真实世界基准ZEDD与网络架构FOSSA。ZEDD包含8.3倍于先前基准的场景及更高质量的图像和深度真值；FOSSA为面向DfD任务的Transformer架构，核心是带对焦距离嵌入的堆栈注意力层，可高效跨焦栈交换信息。实验证明其在零样本条件下具备良好泛化能力，为真实场景散焦深度估计提供了新基准与架构。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 557, \"height\": 572}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 1824, \"height\": 1216}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 565, \"height\": 571}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 561, \"height\": 567}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 564, \"height\": 571}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 564, \"height\": 572}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 567, \"height\": 572}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-015.webp\", \"caption\": \"\", \"page\": 3, \"index\": 15, \"width\": 576, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 917, \"height\": 610}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 1010, \"height\": 673}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 1010, \"height\": 673}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-019.webp\", \"caption\": \"\", \"page\": 3, \"index\": 19, \"width\": 1010, \"height\": 673}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-020.webp\", \"caption\": \"\", \"page\": 3, \"index\": 20, \"width\": 1118, \"height\": 743}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-021.webp\", \"caption\": \"\", \"page\": 3, \"index\": 21, \"width\": 576, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-022.webp\", \"caption\": \"\", \"page\": 3, \"index\": 22, \"width\": 576, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-023.webp\", \"caption\": \"\", \"page\": 5, \"index\": 23, \"width\": 701, \"height\": 698}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-024.webp\", \"caption\": \"\", \"page\": 5, \"index\": 24, \"width\": 598, \"height\": 595}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-025.webp\", \"caption\": \"\", \"page\": 5, \"index\": 25, \"width\": 598, \"height\": 595}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-026.webp\", \"caption\": \"\", \"page\": 5, \"index\": 26, \"width\": 703, \"height\": 697}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-027.webp\", \"caption\": \"\", \"page\": 5, \"index\": 27, \"width\": 1026, \"height\": 684}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-028.webp\", \"caption\": \"\", \"page\": 5, \"index\": 28, \"width\": 912, \"height\": 608}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-029.webp\", \"caption\": \"\", \"page\": 7, \"index\": 29, \"width\": 1197, \"height\": 900}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-030.webp\", \"caption\": \"\", \"page\": 11, \"index\": 30, \"width\": 486, \"height\": 324}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-031.webp\", \"caption\": \"\", \"page\": 11, \"index\": 31, \"width\": 486, \"height\": 324}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-032.webp\", \"caption\": \"\", \"page\": 11, \"index\": 32, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-033.webp\", \"caption\": \"\", \"page\": 11, \"index\": 33, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-034.webp\", \"caption\": \"\", \"page\": 11, \"index\": 34, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-035.webp\", \"caption\": \"\", \"page\": 11, \"index\": 35, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-036.webp\", \"caption\": \"\", \"page\": 11, \"index\": 36, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-037.webp\", \"caption\": \"\", \"page\": 11, \"index\": 37, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-038.webp\", \"caption\": \"\", \"page\": 11, \"index\": 38, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-039.webp\", \"caption\": \"\", \"page\": 11, \"index\": 39, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-040.webp\", \"caption\": \"\", \"page\": 11, \"index\": 40, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-041.webp\", \"caption\": \"\", \"page\": 11, \"index\": 41, \"width\": 486, \"height\": 324}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-042.webp\", \"caption\": \"\", \"page\": 11, \"index\": 42, \"width\": 486, \"height\": 323}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-043.webp\", \"caption\": \"\", \"page\": 11, \"index\": 43, \"width\": 660, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-c4e6f712d36326847ec8c2fe/fig-044.webp\", \"caption\": \"\", \"page\": 11, \"index\": 44, \"width\": 486, \"height\": 323}]"
motivation: 现有散焦深度方法易过拟合特定数据集，缺乏对真实场景的零样本泛化能力。
method: 提出真实世界DfD基准ZEDD，并设计基于Transformer的FOSSA网络，含带对焦距离嵌入的堆栈注意力层。
result: ZEDD场景数为先前基准的8.3倍且图像与深度真值质量更高，FOSSA实现高效跨焦栈信息交互与零样本泛化。
conclusion: 为散焦深度估计建立了更具挑战性的零样本评测基准与有效架构。
---

## Abstract
Depth from Defocus (DfD) is the task of estimating a densemetric depth map from a focus stack. Unlike previous works overfittingto a certain dataset, this paper focuses on the challenging and practi-cal setting of zero-shot generalization. We first propose a new real-worldDfD benchmark ZEDD, which contains 8.3× more scenes and signifi-cantly higher quality images and ground-truth depth maps comparedto previous benchmarks. We also design a novel network architecturenamed FOSSA. FOSSA is a Transformer-based architecture with noveldesigns tailored to the DfD task. The key contribution is a stack atten-tion layer with a focus distance embedding, allowing efficient informa-tion exchange across the focus stack. Finally, we develop a new trainingdata pipeline allowing us to utilize existing large-scale RGBD datasetsto generate synthetic focus stacks. Experiment results on ZEDD andother benchmarks show a significant improvement over the baselines,reducing errors by up to 55.7%. The ZEDD benchmark is released athttps://zedd.cs.princeton.edu. The code and checkpoints are re-leased at https://github.com/princeton-vl/FOSSA.Input: Focus stack and corresponding focus distancesFocus Distance = 0.8m Focus Distance = 1.6m Focus Distance = 3.1m Focus Distance = 8.1mDFF-FV 𝛿! = 0.71 MoGe-2 𝛿! = 0.45 𝛿! = 0.98Existing depth from defocus Monocular depth models suffer Ours Ground Truthmodels are not generalizable from scale ambiguity*Equal contribution.

---

## 论文详细总结（自动生成）

# 《Zero-Shot Depth from Defocus（零样本散焦深度估计）》论文总结

---

## 1. 核心问题与研究动机

- **任务定义**：散焦深度估计（Depth from Defocus, DfD）要求从一组在同一视点、同一光圈下，但**对焦距离不同**的像素对齐图像（focus stack，焦栈）及其对焦距离元数据中，回归出稠密的**度量（metric）深度图**。
- **应用价值**：焦栈本身蕴含丰富的场景几何信息——随着焦平面从近到远扫过，不同深度的物体依次清晰又依次模糊。该深度图可用于后期散焦控制、新视角合成、重打光等下游任务。
- **核心痛点一：模型泛化能力差**。以往 DfD 工作（DefocusNet、DFF、HybridDepth、DualFocus、DEReD 等）普遍采用**同域（in-domain）训练/测试**范式，训练与评测都在同一数据集上（如 DDFF、NYU 均不足 1000 个样本），网络设计容量与可扩展性不足，导致在未见域上性能急剧下降，难以落地。
- **核心痛点二：缺乏高质量基准**。已有基准存在明显缺陷：
  - 大量工作用 **2D PSF 合成**焦栈，只能近似真实光学模糊，无法复现依赖 3D 几何的真实散焦；
  - DDFF 是唯一有真实焦栈与稠密深度的数据集，但焦栈由光场相机合成，**光圈极小（等效 F15）**，散焦效果几乎不可见；深度真值来自结构光传感器，分辨率低、噪声大、量程仅 3.5m；
  - MobileDepth 仅 11 个场景且**无深度真值**，无法定量评测。
- **整体含义**：本文首次系统性地将 DfD 推向**零样本泛化（zero-shot generalization）**设定，同时补齐"基准"与"模型"两端，为真实场景散焦深度估计建立新的评测与架构范式（ECCV 2026）。

---

## 2. 方法论

### 2.1 总体框架：FOSSA（FOcuS Stack Attention Transformer）

- 两阶段结构：
  1. **焦栈特征提取阶段**（L1 = 4 层）：每层包含（i）**权重共享**的 ViT Block 逐图独立处理；（ii）**堆栈注意力层（Stack Attention）**在焦栈维度上做信息交换。
  2. **特征坍缩与精修阶段**：沿焦栈维度对特征取平均，坍缩为单张全局特征图，再经 L2 = 8 个 ViT Block 精修，最后由标准 **DPT 头**回归稠密度量深度。

### 2.2 关键技术细节

- **ViT 主干**：采用标准 ViT Block（多头自注意力 + FFN + 残差 + 归一化），图像切为 p×p patch 并嵌入为 token，得到特征图 F ∈ R^{C×(H/p×W/p)}；权重在焦栈内共享，因此天然支持任意栈长。
- **堆栈注意力层（核心贡献）**：
  - 将每张图的对焦距离 d_i 经两层 MLP 编码为 C 维向量，**加到该图的图像 token 上**（focus distance embedding，作为度量锚点）；
  - 将 M 张图的特征沿栈维拼接成 4D 张量 F′ ∈ R^{M×C×(H/p×W/p)}，**仅沿栈维做自注意力**；
  - 对每个 patch 位置，在 M 个对焦设置间聚合"由模糊到清晰再到模糊"的变化线索，从而获得单张图无法提供的度量深度线索；
  - **效率优势**：注意力二次复杂度只发生在栈长 M（远小于空间 token 数）上，代价极低。
- **设计动机**：DfD 的关键几何信号不在单张图内，而**跨焦栈**；且仅嵌入对焦距离（不像 DDFS 那样嵌入完整相机参数），通过训练时多样化组合来获得对焦距与光圈的鲁棒性。
- **可扩展性**：完全基于标准 Transformer 组件，可直接继承 DepthAnything v2 等强预训练权重；相比之下前作大量依赖自定义层，难以放大规模。

### 2.3 训练数据管线（合成焦栈）

- 用**弥散圆（CoC）**建模模糊强度：
  - `CoC = (|D − d| / D) · f² / (N(d − f))`，其中 D 为物体深度、d 为对焦距离、f 为焦距、N 为 f 数；
  - 由 CoC 生成逐像素 PSF 模糊核，对 RGB 图像做卷积。
- **域随机化（关键）**：
  - 不假设高斯 PSF（前作常用），而是**随机化 PSF 形状**，覆盖衍射受限到散焦主导的不同成像区间；
  - 随机化 **f 数**、**对焦距离分布**（近/远边界与中间插值方式），以提升泛化性。
- **损失函数**：`L = SiLog(D̂, D) + 0.1 · GradMatching(D̂, D)`，其中 SiLog 取 λ = 0.5 以平衡度量与相对监督。
- **归一化**：使用 CSTM-label 归一化（依赖真值焦距），在归一化深度空间预测；训练与评测均向基线提供真值焦距以保证公平。

### 2.4 ZEDD 基准的采集流程

- **硬件**：Sony α1-II DSLR + Sony FE 50mm F1.4 GM 定焦大光圈镜头，4K 分辨率。
- **内参标定**：针对"镜头呼吸"（对焦时 FoV 变化），定义 canonical 空间（对焦距离设为 3.08m），用 Kalibr 标定内参，其余对焦距离图像 warp 到该空间。
- **对焦距离标定**：读取镜头马达 4 位 hexcode，通过与平行标定板共标定（OpenCV 求内/外参），将 hexcode 的 z 分量作为真值对焦距离，建立稀疏但精确的查找表。
- **软件控制**：程序化设定马达位置，保证"图像–对焦距离"映射可复现，并消除机械振动导致的栈内失配。
- **深度真值**：Ouster OS0-128 LiDAR（量程 100m，亚厘米精度）；手持移动**累积约 600 帧**，Open3D + ICP 配准并降噪得到稠密世界点云；再通过离线标定的 `cam_T_lidar` 与逐点云 ICP 求得的 `lidar_T_world`，投影至相机坐标系，用 **z-buffering** 生成深度图（可达 1080p，无遮挡缺失区），最后人工质检与清理。

---

## 3. 实验设计

### 3.1 数据集与基准

- **ZEDD（主基准，真实）**：100 个唯一场景（教室、走廊、机器人实验室、办公室、厨房、花园等室内外场景），每个场景 9 个对焦距离（0.82–8.10m）× 6 档光圈（F1.4/2.0/2.8/4.0/5.6 及 F16 全清晰）= 54 张图；深度真值分辨率 1824×1216。评测时随机划分 50/50 验证/测试，取 5 张图、FD = {0.8, 1.7, 3.1, 4.9, 8.1}m、F/2.8。
- **Infinigen Defocus（合成基准）**：基于 Infinigen Indoors 程序化生成，用 Blender Cycles 光线追踪渲染真实散焦，200 个场景，FD = {0.8, 1.7, 3.0, 4.7, 8.0}m，F/1.4；真值完美但照片真实度低于真实数据。
- **真实 RGBD 数据集（合成焦栈）**：iBims（室内）、DIODE（室内+室外）、HAMMER（透明物体），由真值深度按 CoC 合成焦栈，光圈 F/1.4，对焦距离依场景深度统计采样以模拟摄影者行为。
- **DDFF**：沿用前作的数据划分与指标，报告零样本与微调两种设定。

### 3.2 对比方法

- **单目深度基线**：DepthAnything v2、DepthPro、UniDepthV2、MoGe-2（输入为 F/16 全清晰图；作者明确声明这不是"替代单目深度"的正面对比，而是定位参照）。
- **DfD 基线**：DFF-FV、DFF-DFV、DEReD、HybridDepth；DDFF 上另有 DefocusNet、DualFocus、原版 DDFF。多 checkpoint 的基线取最优。
- 额外做了 **DFF-DFV 用本文同款数据/损失重训（†）** 的对照，以分离"架构贡献"与"数据管线贡献"。

### 3.3 指标

- AbsRel、δ1.05 / δ1.25（δ1.25 即常用 δ1）、MAE、MSE、RMSE、SqRel 等。

### 3.4 消融与鲁棒性

- **消融（Tab. 5，ViT-S，700×512，单卡 L40）**：① 无堆栈注意力层；② 无对焦距离嵌入（改用正弦位置编码）；③ 坍缩位置 L1=2；④ 坍缩位置 L1=6；⑤ 在 DPT 内融合（VideoDA 式）；⑥ 训练时不随机化模糊核；⑦ 不随机化对焦距离分布。
- **鲁棒性（ZEDD 验证集）**：光圈（F1.4→F5.6）、对焦距离分布（均匀 / 近端密集 / 极端（只取最小三个+最大两个） / 随机 5/9）、焦栈长度（2–9 张）。

---

## 4. 资源与算力

- **训练配置**：40 个 epoch，batch size 8，指数学习率调度，**4 × L40 GPU（48GB 显存），训练耗时约 2 天**。
- **训练数据规模**：Hypersim（66k 样本，室内）+ TartanAir（307k 样本，室外）合成焦栈；训练栈长固定为 5。
- **模型规模**：ViT-S 与 ViT-B 两档；ViT-S 约 42.5M 参数、1.56GB 显存、51.9ms 推理、370.4 GFLOPS（700×512）。
- **微调**：DDFF 上基于 DDFF 训练集（400 样本）再训 150 epoch（未单独说明微调算力）。
- **初始化**：ViT Block 由 DepthAnything v2 室内度量 checkpoint 初始化；堆栈注意力层 MLP 零初始化。

---

## 5. 实验数量与充分性评估

- **实验体量**：
  - 5 个评测数据集/基准（ZEDD、Infinigen Defocus、iBims、DIODE、HAMMER）+ DDFF 的零样本与微调两种设定；
  - 对比 4 个单目深度方法与 4–6 个 DfD 方法，并额外重训一个 DfD 基线做归因对照；
  - 1 组含 7 个变体的消融（覆盖架构组件、坍缩位置、域随机化三大类）；
  - 3 组鲁棒性实验（光圈、对焦距离分布、栈长，其中栈长覆盖 2–9 张）。
- **充分性与公平性**：
  - **较充分**：消融覆盖了论文的每一个核心设计选择，且同一结论在 ZEDD 与 Infinigen 两个域上一致，说明设计不依赖特定数据集；鲁棒性实验覆盖了实际部署最关心的变量；在 ZEDD 上同时报告 δ 与误差类指标（MAE/MSE/RMSE），信息量足。
  - **公平性措施**：向所有方法（含单目基线）提供真值焦距；多 checkpoint 基线取最优；对 DfD 基线用相同数据与损失重训以剥离数据管线的贡献。
  - **潜在偏差**：ZEDD 测试集仅 50 个场景，样本量偏小；真实 RGBD 数据集的焦栈是**合成**的，仍属"半真实"评测；DDFF 表格中的基线数字直接取自 DualFocus 论文，非本文复现。

---

## 6. 主要结论与发现

- **零样本性能大幅领先**：
  - ZEDD：ViT-B 达 δ1.25 = 0.918、AbsRel = 0.089，相比最佳单目基线 DepthPro（0.201）**AbsRel 降低 55.7%**；所有 DfD 基线在 ZEDD 上表现很差（最强 DFF-FV 的 δ1.25 = 0.576 甚至略逊于 MoGe-2 的 0.580），印证其泛化能力不足。
  - Infinigen Defocus：AbsRel 0.085 vs DepthPro 0.176，**降低 51.7%**，且能准确恢复细杆状结构并保持全局尺度正确。
  - DIODE：AbsRel 0.160 vs DepthPro 0.289，**降低 44.6%**；HAMMER（透明物体）δ1.25 = 0.999、AbsRel 低至 0.017。
  - DDFF 微调后 MSE = 2.8×10⁻⁴，相比此前 SOTA DualFocus（4.7×10⁻⁴）**降低 40.4%**。
- **归因结论**：用同款数据/损失重训的

DFF-DFV（†）在 ZEDD 上的 AbsRel 从原版的 0.2xx 量级明显下降，但仍显著逊于 FOSSA，说明**性能提升的主要来源是架构设计（堆栈注意力 + 对焦距离嵌入 + 大规模预训练初始化），数据管线与域随机化带来的是叠加增益而非全部贡献**。这一对照有效回应了"是否只是靠合成数据堆量"的质疑。

- **消融结论（Tab. 5，ZEDD + Infinigen 一致）**：
  - **堆栈注意力层是最关键的组件**：去掉后 ZEDD 上 δ1.25 大幅下降、AbsRel 显著上升，说明"跨焦栈的显式信息交换"才是 DfD 的几何信号来源，仅靠 ViT 逐图处理再融合并不够。
  - **对焦距离嵌入同样不可替代**：替换为正弦位置编码后性能明显退化，印证对焦距离是度量深度的**尺度锚点**——没有它，网络只能回归相对深度而无法输出度量值。
  - **坍缩位置存在最优区间**：L1 = 2 时栈内交互不足，L1 = 6 时坍缩前的空间特征提取又不够充分，L1 = 4 取得最佳平衡；说明"栈内交互"与"单图空间建模"需要合理的算力分配。
  - **在 DPT 头内部做融合（VideoDA 式）明显劣于在特征主干中做堆栈注意力**，说明栈维交互必须发生在**高维语义特征**层面，而非最终输出层面。
  - **域随机化（PSF 形状 + 对焦距离分布）各自都带来稳定增益**，且二者叠加效果最好，验证了"不假设高斯 PSF、随机化对焦采样"这一设计对真实泛化的价值。

- **鲁棒性结论**：
  - **对光圈鲁棒**：从 F1.4 到 F5.6，性能下降平缓；即使在训练时未曾显式强调的 F5.6 下仍保持领先，说明模型没有过拟合到某个特定的模糊强度。
  - **对对焦距离分布鲁棒**：在"均匀 / 近端密集 / 极端（仅最小三个 + 最大两个）/ 随机 5/9"四种采样方式下均稳定；极端采样下性能有所下降但仍在可用范围，说明模型确实学到了"从模糊变化率推断深度"的物理规律，而非依赖均匀覆盖。
  - **对焦栈长度鲁棒**：在 2–9 张的范围内单调改善且始终可用，**即使只用 2 张图也能给出合理深度**；这得益于权重共享的 ViT 主干与栈维注意力对栈长天然无依赖，而多数 DfD 基线被固定栈长绑定。
  - 整体上，鲁棒性实验支撑了论文的核心主张：FOSSA 的泛化能力来自**架构的物理归纳偏置**，而非对训练分布的拟合。

---

## 7. 局限性

- **依赖真值对焦距离元数据**：方法与评测均要求输入每张图的精确对焦距离（及归一化所需的焦距），这与相机 EXIF 通常只给出粗略焦距/无对焦距离的现实存在差距；论文虽做了对焦距离分布的鲁棒性测试，但未系统评测**对焦距离存在噪声或缺失**时的退化程度。
- **训练仍依赖合成焦栈**：主训练数据（Hypersim、TartanAir）与真实 RGBD 数据集上的评测焦栈均由 CoC 卷积合成，尽管做了 PSF 形状随机化，仍无法完全复现真实镜头的像差、渐晕、镜头呼吸等效应；真实焦栈目前只用于 ZEDD 评测。
- **ZEDD 规模有限**：100 个场景、测试集 50 个场景，场景类型以室内与近场室外为主，对远距离（>10m）、强运动、极端光照等条件的覆盖不足；深度量程与对焦范围（0.82–8.10m）也限制了远场结论的推广。
- **计算开销**：ViT-B 在 4×L40 上训练约 2 天、单帧推理数十毫秒，相对轻量 DfD 方法仍偏重；论文未给出移动端部署或实时性方案。
- **单目基线的对比边界**：作者已声明与 DepthAnything v2 等的对比是"定位参照"而非正面对抗，但这意味着论文尚未回答"在焦栈信息可得时，DfD 相比单目深度 + 后处理的净收益"这一问题。
- **DDFF 数字来源**：DDFF 表格中的部分基线结果直接引用自 DualFocus 论文，非本文复现，跨论文对比存在实现与评测细节不一致的风险。

---

## 8. 总体评价

- **贡献定位清晰且互补**：本文同时补齐了 DfD 领域的"基准"（ZEDD：真实焦栈 + LiDAR 稠密深度 + 可复现对焦距离标定）与"模型"（FOSSA：可继承大规模预训练、栈长无关、物理归纳偏置明确）两端，是少见的"数据 + 方法"双轮驱动工作。
- **方法设计有物理依据**：把"跨焦栈的模糊变化"这一 DfD 的核心几何信号，用**只在栈维做注意力**这一轻量、可扩展的方式显式建模，并配合对焦距离嵌入提供度量锚点，设计动机与消融结论高度自洽。
- **实验说服力强**：在 5 个基准 + DDFF 的零样本与微调设定上一致领先，消融覆盖每一个核心设计选择，鲁棒性覆盖光圈、对焦分布、栈长三个实际部署关键变量，并用"同款数据重训基线"的对照把架构贡献与数据贡献分离——这在同类工作中属于较严格的实验标准。
- **工程价值高**：权重共享 + 标准 ViT Block 的架构使模型天然支持任意栈长、可直接吃下 DepthAnything v2 等预训练权重，为后续规模化与落地提供了清晰的扩展路径。
- **待补之处**：对焦距离元数据的现实可得性、真实焦栈训练数据的匮乏、ZEDD 的场景与量程覆盖、以及真实场景下的实时性，仍是该方法走向实用需要继续解决的问题。

---

（完）
