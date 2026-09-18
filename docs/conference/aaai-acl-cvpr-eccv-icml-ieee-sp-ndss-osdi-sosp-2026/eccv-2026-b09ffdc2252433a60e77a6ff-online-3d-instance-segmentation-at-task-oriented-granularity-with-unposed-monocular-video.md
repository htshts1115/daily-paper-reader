---
title: Online 3D Instance Segmentation at task-oriented granularity with Unposed Monocular Video
title_zh: 基于无位姿单目视频的任务导向粒度在线3D实例分割
authors: "Dong Wu, Baicheng Li, Yingdian Cao, Shunkai Zhou, Yiwen Lu, Hongbin Zha"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9032.pdf"
tags: ["query:seg"]
score: 6.0
evidence: 结合开放词汇检测与提示式2D分割的实例分割框架
tldr: 该论文针对开放世界场景中具身智能体难以实时、任务自适应地感知与交互物体的问题，提出一种面向无位姿单目视频的实时任务导向3D实例分割框架。方法上用开放词汇检测器与提示式2D分割模型逐帧解耦物体，同时借助稠密SLAM重建场景几何，并依据SLAM位姿图进行掩码选择与关联。实验表明该框架能在开放世界场景中实现实时、任务自适应的3D实例感知。其贡献在于把分割与识别的顺序倒置，为具身交互提供更实用的感知范式。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 596, \"height\": 327}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 610, \"height\": 634}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 865, \"height\": 644}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 1296, \"height\": 968}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-010.webp\", \"caption\": \"\", \"page\": 7, \"index\": 10, \"width\": 1296, \"height\": 968}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-012.webp\", \"caption\": \"\", \"page\": 7, \"index\": 12, \"width\": 632, \"height\": 472}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-013.webp\", \"caption\": \"\", \"page\": 7, \"index\": 13, \"width\": 775, \"height\": 556}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-014.webp\", \"caption\": \"\", \"page\": 7, \"index\": 14, \"width\": 465, \"height\": 299}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-015.webp\", \"caption\": \"\", \"page\": 7, \"index\": 15, \"width\": 512, \"height\": 368}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-016.webp\", \"caption\": \"\", \"page\": 7, \"index\": 16, \"width\": 512, \"height\": 368}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-017.webp\", \"caption\": \"\", \"page\": 7, \"index\": 17, \"width\": 370, \"height\": 368}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-018.webp\", \"caption\": \"\", \"page\": 7, \"index\": 18, \"width\": 368, \"height\": 367}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-019.webp\", \"caption\": \"\", \"page\": 7, \"index\": 19, \"width\": 369, \"height\": 368}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 487, \"height\": 354}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-021.webp\", \"caption\": \"\", \"page\": 7, \"index\": 21, \"width\": 1518, \"height\": 1089}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 1518, \"height\": 1089}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-023.webp\", \"caption\": \"\", \"page\": 13, \"index\": 23, \"width\": 503, \"height\": 372}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-024.webp\", \"caption\": \"\", \"page\": 13, \"index\": 24, \"width\": 503, \"height\": 373}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-025.webp\", \"caption\": \"\", \"page\": 13, \"index\": 25, \"width\": 508, \"height\": 373}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-026.webp\", \"caption\": \"\", \"page\": 13, \"index\": 26, \"width\": 508, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-027.webp\", \"caption\": \"\", \"page\": 13, \"index\": 27, \"width\": 508, \"height\": 371}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-028.webp\", \"caption\": \"\", \"page\": 13, \"index\": 28, \"width\": 503, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-029.webp\", \"caption\": \"\", \"page\": 13, \"index\": 29, \"width\": 508, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-030.webp\", \"caption\": \"\", \"page\": 13, \"index\": 30, \"width\": 508, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-031.webp\", \"caption\": \"\", \"page\": 13, \"index\": 31, \"width\": 503, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-032.webp\", \"caption\": \"\", \"page\": 13, \"index\": 32, \"width\": 503, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-033.webp\", \"caption\": \"\", \"page\": 13, \"index\": 33, \"width\": 503, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-034.webp\", \"caption\": \"\", \"page\": 13, \"index\": 34, \"width\": 508, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-035.webp\", \"caption\": \"\", \"page\": 13, \"index\": 35, \"width\": 508, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-036.webp\", \"caption\": \"\", \"page\": 13, \"index\": 36, \"width\": 593, \"height\": 438}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-037.webp\", \"caption\": \"\", \"page\": 13, \"index\": 37, \"width\": 533, \"height\": 392}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-038.webp\", \"caption\": \"\", \"page\": 13, \"index\": 38, \"width\": 477, \"height\": 355}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-039.webp\", \"caption\": \"\", \"page\": 13, \"index\": 39, \"width\": 508, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-040.webp\", \"caption\": \"\", \"page\": 13, \"index\": 40, \"width\": 503, \"height\": 372}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-041.webp\", \"caption\": \"\", \"page\": 13, \"index\": 41, \"width\": 504, \"height\": 372}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b09ffdc2252433a60e77a6ff/fig-042.webp\", \"caption\": \"\", \"page\": 13, \"index\": 42, \"width\": 504, \"height\": 372}]"
motivation: 传统自底向上分割先分割后识别，难以让具身智能体在开放世界场景中实时、任务自适应地感知并交互物体。
method: 逐帧用开放词汇检测器配合提示式2D分割模型解耦物体，同时用稠密SLAM重建几何，并依托位姿图选择与关联掩码。
result: 在无位姿单目视频上实现实时、任务导向的3D实例分割，验证了开放世界场景中感知与交互的可行性。
conclusion: 将分割与识别顺序倒置，为具身智能体的开放世界3D感知提供了一种任务自适应的新范式。
---

## Abstract
We present a real-time, task-oriented 3D instance segmenta-tion framework for unposed monocular video, enabling embodied agentsto task-adaptively perceive and interact with objects in open-world scenes.Unlike most previous bottom-up segmentation paradigms that segmentbefore recognition, we adopt a task-oriented segmentation approach.Specifically, objects are decoupled within each frame using an open-vocabulary detector combined with a prompt-based 2D segmentationmodel, while the 3D underlying geometry of the scene is simultane-ously being reconstructed using a modern dense SLAM system, whosecontinuously re-optimized camera poses and depth are unsuitable forincremental mask association. Guided by the SLAM-derived pose graph,we selectively associate multi-view masks and reuse the dense correspon-dences provided by the SLAM system, incrementally converting theminto geometric association scores with minimal additional computation.By incorporating semantic similarity and mutual exclusivity metrics, wedesign a priority-ordered mask clustering algorithm for efficient onlinemulti-view mask matching and merging. Evaluations on open-vocabulary3D instance segmentation benchmarks show that our method effectivelymitigates the performance degradation of existing approaches when usingdense SLAM reconstructions instead of depth-sensor point clouds. Onthe Replica dataset, using only unposed images, it even achieves resultscomparable to methods leveraging ground-truth depth and poses. Moreimportantly, qualitative results show that our method achieves more reli-able task-oriented 3D object disentanglement than previous bottom-upsegmentation paradigms.

---

## 论文详细总结（自动生成）

# 论文总结：基于无位姿单目视频的任务导向粒度在线 3D 实例分割

## 1. 核心问题与整体含义

- **研究背景**：3D 实例分割是具身智能的基础任务，但现有方法普遍假设可以离线获取完整的 RGB-D/LiDAR 传感器数据、并预先已知相机位姿。这一假设在具身应用中几乎不成立——智能体必须在实时约束下增量式地感知、重建与解析环境。
- **两大痛点**：
  - **硬件依赖**：深度传感器成本高、部署难；相比之下单目相机更廉价、易部署且语义信息更丰富。
  - **粒度僵化**：主流方法属于"自底向上（bottom-up）"范式，即**先分割、后识别**：
    - 一类方法（如 SAM3D、Sai3D）用 SAM 或超像素把场景中所有视觉可分解实体都切出来，导致过度分割、碎片化与冗余，且依赖耗时后处理；
    - 另一类（如 OpenMask3D、Open3DIS）依赖闭集类别的 2D/3D 预训练分割模型决定粒度，无法随任务动态调整。
- **核心洞察**：对每一个具体的具身任务而言，需要识别的物体类别集合通常是**任务相关且明确界定的**（如"找到浴缸上的毛巾"只需 {towel, bathtub}）。因此可以从 bottom-up 转向**任务导向（task-oriented）的自顶向下分割**范式。
- **整体含义**：论文提出一个面向**无位姿单目视频**的实时、任务导向 3D 实例分割框架，在不依赖离线点云与额外传感器、不做任何 3D 微调的前提下，实现开放世界、零样本、任务自适应的在线 3D 实例感知。
- **关键技术障碍**：现代稠密 SLAM（如 MASt3R-SLAM、VGGT-SLAM）虽能从无位姿视频在线重建，但其相机位姿与逐像素深度在后端被**持续优化**，作为增量式掩码关联的参考不稳定（历史关联无法随之回溯修正）；直接把 SLAM 输出替换传感器深度与 GT 位姿，会导致已有 3D 实例分割方法性能大幅退化。

## 2. 方法论

### 2.1 核心思想
- 以 **MASt3R-SLAM** 为在线重建基座，把"3D 实例分割"转化为**跨关键帧的 2D 实例掩码关联与聚类**问题。
- 关联度量刻意**避开被在线优化的状态变量**（位姿、深度），转而复用 SLAM 前端 pointmap matching 产生的**点级稠密对应**——该对应独立于位姿估计，在回环与后端优化后依然长期有效。

### 2.2 基础组件（Sec. 3.1）
- 输入 RGB 图像流，MASt3R-SLAM 输出关键帧的逐像素 3D pointmap $X_i$、置信度 $C_i$、以及全部帧的相机位姿 $T_t \in \mathrm{Sim}(3)$。
- Pointmap matching 提供帧间稠密像素对应 $\pi_{ij}: p_i \to p_j$ 与有效掩码 $V_{ij}$（3D 距离过大或置信度低者置为无效）。
- 增量维护**位姿图 $E$**：新帧与最近关键帧比较，几何匹配低于阈值则新增关键帧，边由时序或回环检测形成。

### 2.3 任务导向掩码表示（Sec. 3.2）
- 由 LLM 自动推断任务相关开放类别集合 $C$（如 {towel, bathtub}）。
- **YOLO-World** 生成类别感知的粗 2D 提案 → **SAM2** 精炼为高质量实例掩码。
- 按"小掩码保留优先"原则保证同一关键帧内掩码**互不重叠**，参数化为 $M^i_{id} \in \mathbb{Z}^{H\times W}$，$c_{in}\in C$ 为类别标签，$-1$ 为背景。
- 由于掩码与 pointmap 像素对齐，3D 实例分割等价于多视图掩码关联；关联完成后通过单级哈希映射更新跨视图实例 ID。

### 2.4 三种掩码关联准则（Sec. 3.3）
仅在位姿图新增边 $e_{ij}=(K_i,K_j)$ 时，对两端关键帧的掩码集合做成对计算，避免全帧对冗余计算：

- **几何关联度量（GAM）**：用双向对应 $\pi_{ij}$、$\pi_{ji}$ 将掩码投影到对端坐标系求重叠，定义有效重叠率 $or(n,m)$（分子为投影重叠且源像素有效的对应数，分母为源掩码内有效对应数）；再取双向最大值 $GAM(n,m)=\max(or(n,m),or(m,n))\in[0,1]$，以缓解因在线观测不完整导致的重叠率低估。
- **语义相似度度量（SSM）**：用 CLIP **一次性**预计算类别文本嵌入 $F=\{f_c\}$，每个掩码直接取所属类别的嵌入 $s_{in}=f_{c_{in}}$（无需裁剪实例再提图像特征，显著省算力），掩码对相似度为两嵌入的余弦相似度，取值 $[-1,1]$。
- **互斥性度量（MEM）**：同一关键帧内不同实例掩码不应被合并。对施加非重叠约束前的掩码对，若 IoU 小于阈值 $\epsilon$ 则 MEM 记为 1（互斥），否则为 0。用于抑制因欠分割（一个框天然包含邻物）或对应噪声造成的错误合并。
- 所有成对度量存入**稠密矩阵**，随机访问 O(1)，支持在线快速查改。

### 2.5 优先级有序的掩码合并（Sec. 3.4 + Algorithm 1）
- 把多视图掩码匹配建模为**在线聚类**：簇 = 代表同一物体的掩码集合。
- 流程：新增掩码边按 GAM、SSM 阈值过滤 → 按 **GAM 降序排序** → 依次处理：两掩码均未分配则新建簇；均已分配且不同簇则先查 MEM 判断是否冲突（冲突则丢弃该边，否则合并两簇）；仅一方已分配则查 MEM 后把未分配掩码并入。
- **簇级合并（IoU 准则）**：位姿图边稀疏，时间远但空间近的关键帧可能无边相连，故用第一阶段聚类结果计算各簇 3D 包围盒及其两两 IoU，按 IoU 降序合并，同样查 MEM 避免冲突掩码入同簇。
- 由于聚类算法高效，**每一步都用当前全部关联度量做最优聚类**，从而抑制在线场景中早期分割错误的累积。

### 2.6 实现细节（Sec. 3.5）
- 丢弃 YOLO-World 检测框与 SAM2 掩码重叠度低的检测结果。
- 统一超参：$\epsilon=0.2$，$\tau_{GAM}=0.25$，$\tau_{SSM}=0.85$，$\tau_{IoU}=0.1$；作者称性能对具体取值不敏感。

## 3. 实验设计

- **数据集与场景**：
  - **ScanNet200 验证集**：312 个场景，198 个预定义类别（开放词汇设置）。
  - **Replica**：48 个类别（开放词汇设置）。
- **输入设定**：仅使用单目视频、无位姿。用 `evo` 通过 Sim(3) 变换将估计轨迹与 GT 对齐，再把重建点云的语义/实例标签经最近邻顶点查找转移到 GT mesh 上评测。
- **评价指标**：沿用 ScanNet 评测方法，报告掩码重叠阈值 50% 与 25% 下的 AP（AP50 / AP25）。开放词汇设置下 AP 同时衡量实例分割质量与类别分配正确性；class-agnostic 设置下只衡量实例分割。
- **对比方法**：
  - ScanNet200：SAM3D（离线/在线）、OVIR-3D、Open3DIS、OpenIns3D、OpenMask3D、Open-YOLO 3D、EmbodiedSAM、OnlineAnySeg，以及本文方法。
  - Replica：OVIR-3D、Open3DIS、OpenMask3D、OpenScene、Open-YOLO 3D、离线前馈方法 **PanSt3R**、本文方法。
  - **输入替换实验**：把 Open-YOLO 3D 与 OnlineAnySeg 的输入替换为 MASt3R-SLAM 估计的点云与位姿，以在同等"困难"设定下比较。
- **定性对比**：在 ScanNet200 上与 Mask3D、OnlineAnySeg、SAM3D 三种 bottom-up 范式做可视化对比（如"找桌上的纸""找桌上的书""找沙发旁的靠垫""找浴缸边的毛巾"）。
- **消融实验**（Replica）：分别去掉 GAM、SSM、MEM、IoU 簇合并、优先级排序机制，共 5 组 + 完整系统。
- **运行时分析**：给出各模块耗时与系统 FPS。

## 4. 资源与算力

- **评测平台**：Intel i9-12900KS CPU + **单张 NVIDIA RTX 3090 GPU**。
- **训练开销**：方法为**零样本**，不依赖任何 3D 数据集做微调或后训练，因此**无训练时长**可报（仅 CLIP 文本嵌入预计算一次）。
- **未明确说明**：论文未提及 GPU 数量、总训练/调参算力、能耗等；仅给出推理时延与 FPS。
- **运行时间细节**（Replica `office0` 场景，按关键帧计）：
  - YOLO-World：30.1 ms；SAM2：132.4 ms；GAM 计算：9.0 ms/关键帧对；掩码合并：32 ms。
  - 系统整体：10.87 FPS（Replica office0）、7.32 FPS（ScanNet scene 0011_00）；对应 MASt3R-SLAM 单独运行为 11.23 FPS 与 7.58 FPS。主要耗时来自 SLAM 系统本身。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 2 个数据集的定量评测（ScanNet200 的开放词汇 + class-agnostic；Replica 的开放词汇）；
  - 1 组定性对比（4 个任务场景 × 3 个基线）；
  - 1 组 5 项消融 + 完整系统；
  - 1
