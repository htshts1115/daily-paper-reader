---
title: "SGS-3D: High-Fidelity 3D Instance Segmentation via Reliable Semantic Mask Splitting and Growing"
title_zh: SGS-3D：通过可靠语义掩码拆分与生长实现高保真三维实例分割
authors: "Chaolei Wang, Yang Luo, Jing Du, Siyu Chen, Yiping Chen, Ting Han"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37931/41893"
tags: ["query:seg"]
score: 6.0
evidence: 通过掩码拆分与生长的三维实例分割
tldr: 针对2D到3D提升式三维实例分割因语义引导模糊和深度约束不足而累积误差的问题，本文提出SGS-3D框架，先用几何基元净化并拆分模糊的提升掩码，再将其生长为场景中的完整实例。实验表明该方法在高保真三维实例分割上取得更高实例级精度，优于现有提升式方案，为三维场景理解提供了更可靠的掩码生成路径。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1746, \"height\": 414}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1727, \"height\": 923}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 822, \"height\": 511}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 750, \"height\": 637}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 812, \"height\": 419}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1831, \"height\": 849}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 842, \"height\": 361}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37931/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 835, \"height\": 251}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 870, \"height\": 300}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1810, \"height\": 690}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 868, \"height\": 275}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 496, \"height\": 262}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 378, \"height\": 261}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1849, \"height\": 396}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37931/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 855, \"height\": 139}]"
motivation: 基于2D到3D提升的三维实例分割因语义引导模糊与深度约束不足而累积误差，掩码不够精确。
method: 提出先拆分后生长框架，用几何基元净化并拆分模糊提升掩码，再在场景中生长为完整实例。
result: 在高保真三维实例分割任务上显著提升实例级精度，优于现有提升式方法。
conclusion: 证明几何约束与掩码生长策略可有效缓解提升误差，提升三维场景理解质量。
---

## Abstract
Accurate 3D instance segmentation is crucial for high-quality scene understanding in the 3D vision domain. However, 3D instance segmentation based on 2D-to-3D lifting approaches struggle to produce precise instance-level segmentation, due to accumulated errors introduced during the lifting process from ambiguous semantic guidance and insufficient depth constraints. To tackle these challenges, we propose Splitting and Growing reliable Semantic mask for high-fidelity 3D instance segmentation (SGS-3D), a novel "split-then-grow" framework that first purifies and splits ambiguous lifted masks using geometric primitives, and then grows them into complete instances within the scene. Unlike existing approaches that directly rely on raw lifted masks and sacrifice segmentation accuracy, SGS-3D serves as a training-free refinement method that jointly fuses semantic and geometric information, enabling effective cooperation between the two levels of representation. Specifically, for semantic guidance, we introduce a mask filtering strategy that leverages the co-occurrence of 3D geometry primitives to identify and remove ambiguous masks, thereby ensuring more reliable semantic consistency with the 3D object instances. For the geometric refinement, we construct fine-grained object instances by exploiting both spatial continuity and high-level features, particularly in the case of semantic ambiguity between distinct objects. Experimental results on ScanNet200, ScanNet++, and KITTI-360 demonstrate that SGS-3D substantially improves segmentation accuracy and robustness against inaccurate masks from pre-trained models, yielding high-fidelity object instances while maintaining strong generalization across diverse indoor and outdoor environments.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：3D 实例分割是自动驾驶、VR、多模态场景理解等任务的基础能力。现有全监督方法依赖大量 3D 标注，泛化到开放世界受限；因此利用 2D 预训练基础模型进行 2D-to-3D 提升成为重要方向。
- **核心问题**：基于 2D-to-3D 提升的 3D 实例分割存在两类误差累积：
  - 2D 语义引导模糊，导致提升后的掩码不准确；
  - 深度约束不足，投影/反投影过程中遮挡与深度误差影响实例边界。
- **现有方法不足**：
  - 特征型方法训练低效、错误传播；
  - 掩码型方法多直接依赖原始提升掩码或粗粒度合并超点，忽视 3D 几何线索，易把相邻但独立实例错误合并，产生过分割或碎片化。
- **论文含义**：提出 **SGS-3D**，一个 **training-free** 的“先拆分后生长”（split-then-grow）框架，联合语义与几何信息，对模糊提升掩码进行净化、拆分和生长，从而获得高保真 3D 实例分割。

## 2. 方法论

### 2.1 核心思想

- 不直接使用原始 2D 提升掩码，而是：
  1. 先利用 3D 几何基元过滤不可靠 2D 掩码；
  2. 再将 3D 语义掩码按空间连续性拆分成语义-几何种子；
  3. 最后通过特征引导生长与多视图渐进合并，形成完整实例。
- 整体为 **training-free refinement**，不需要在 3D 数据上训练。

### 2.2 关键技术细节

- **输入**：3D 点云 \(P\)（XYZRGB）、多张配准图像 \(\{I_t\}\)、相机内参与位姿。
- **超点过分割**：将点云过分割为 superpoints \(S=\{s_u\}\)，作为基本处理单元；每个超点有预训练高维特征 \(f_u\)。
- **点-图像映射（Point-Image Mapping）**：
  - 不依赖真实深度图，利用 Z-buffering 从点云和相机参数构建深度缓冲：
    \[
    D_t(u,v)=\min\{z_i \mid p_i\in P,\ \pi(p_i,K_t,T_t)=(u,v)\}
    \]
  - 通过视锥检查和深度一致性检查判断可见性：
    \[
    V_t(i)=\mathbf{1}(0\le u_i<W \land 0\le v_i<H)\cdot \mathbf{1}(|z_i-D_t(u_i,v_i)|\le \tau_{vis})
    \]
  - 得到逐点、逐视图的可见性与点到像素映射，用于后续遮挡感知关联。
- **2D 掩码生成**：
  - 使用 Grounding-DINO 根据文本提示提取高置信度框提示；
  - 再用 SAM 生成候选 2D 掩码。
- **共现掩码过滤（Co-occurrence Mask Filtering）**：
  - 对每个掩码，统计其在各视图中可见的 superpoints 集合 \(P^j_{vis,m}\)；
  - 要求点可见且投影落入掩码区域，且超点中超过 50% 点满足；
  - 定义可见性共现分数 \(c_m\)，衡量该掩码与其他候选掩码在跨视图可见超点集合上的一致性：
    \[
    c_m=\frac{1}{(K_{2D}-1)T}\sum_{n\ne m}\sum_j
    \frac{|P^j_{vis,m}\cap P^j_{vis,n}|}
    {\sqrt{|P^j_{vis,m}|\cdot |P^j_{vis,n}|}}
    \]
  - 低分掩码视为离群值并剪枝，从而去除过分割/欠分割的模糊掩码。
- **语义引导聚合（Semantic-Guided Aggregation）**：
  - **空间连续性拆分**：将过滤后的 2D 掩码提升为 3D 语义掩码，对每个 3D 语义掩码使用 HDBSCAN 按空间连续性拆分，得到“语义-几何种子”（semantic-geometric seeds），缓解相似外观但空间分离对象被错误合并的问题。
  - **单视图特征引导生长**：对种子与邻居超点定义亲和分数：
    \[
    \text{Affinity}(M'_{t,j},s_u)=\text{sim}(\bar f_{t,j},f_u)\cdot \text{Overlap}(M'_{t,j},s_u)
    \]
    其中相似度为余弦相似度，Overlap 为 3D 点集 IoU。迭代合并最高亲和邻居，直到剩余亲和可忽略，从而把碎片部分生长为完整实例。
  - **多视图渐进合并**：先合并不同视图中 3D 空间重叠极高的 proposals，确保无歧义匹配；随后逐步放宽重叠要求，融合同一大实例的碎片，最终得到完整 3D 实例。

## 3. 实验设计

- **数据集 / 场景**：
  - 室内：**ScanNet200**、**ScanNet++**
  - 室外：**KITTI-360**
- **Benchmark 指标**：
  - AP@50（AP50）、AP@25（AP25）
  - mAP：在 50% 到 95% IoU 阈值上以 5% 递增平均。
- **对比方法**：
  - 训练依赖型：UnScene3D、Segment3D、SAM-graph
  - training-free：HDBSCAN、Felzenszwalb、SAM3D、Open3DIS、SAI3D、SAM2Object
  - 开放词表/语义任务：OpenMask3D、OpenIns3D、OVIR-3D、SAM3D、SAI3D、SAM2Object 等
- **主要设置**：
  - **Ours−**：不使用 GT depth；
  - **Ours+**：使用 GT depth；
  - 室内基线大多使用 GT depth，室外 KITTI-360 无 GT depth。
- **主要结果**：
  - KITTI-360 上 Ours− 达 **32.9 mAP、43.7 AP50、53.4 AP25**，比 SAI3D 高 **+16.4 mAP**；
  - ScanNet200 上 Ours− 为 **30.5 mAP、47.2 AP50、62.2 AP25**，Ours+ 达 **34.3 mAP、51.3 AP50、64.6 AP25**；
  - ScanNet++ 上 Ours− 为 **22.5 mAP、36.6 AP50、53.0 AP25**，Ours+ 为 **23.7 mAP、39.6 AP50、54.3 AP25**。
- **开放词表语义结果**：ScanNet200 上 Ours 零样本 mAP 为 **21.1**，AP50 为 **29.4**，AP25 为 **35.0**，在 head/common/tail 类别上均优于若干零样本方法。
- **效率对比**：
  - 使用 10% 图像时，Ours 34.3 mAP、9.51s、62 个预测实例；
  - 仅用 2.5% 图像时，仍达 31.8 mAP、2.42s、68 个实例；
  - 相比 Open3DIS，用更少图像达到更高精度，并减少约 40% 过分割。

## 4. 资源与算力

- 论文中 **未明确说明** GPU 型号、数量、训练时长等算力信息。
- 原因是 SGS-3D 是 **training-free** 框架，不需要 3D 训练；但论文也未系统报告推理阶段的硬件配置、显存占用、并行设置等。
- 仅提供了推理效率相关数据，如不同输入图像比例下的运行时间（10% 图像约 9.51s，2.5% 图像约 2.42s），但未给出具体 GPU 型号。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 3 个主数据集：ScanNet200、ScanNet++、KITTI-360；
  - 1 组主对比实验，覆盖训练依赖与 training-free 方法；
  - 1 组开放词表/语义分割对比；
  - 1 组消融实验：CMF、SCP、FGG 三个组件；
  - 1 组不同 2D 视觉基础模型消融：Cropformer、SAM、YoloW-SAM、GD-SAM；
  - 1 组共现阈值 \(c_m\) 敏感性实验；
  - 1 组输入图像比例效率实验；
  - 1 组模拟遮挡鲁棒性实验；
  - 多组定性可视化与开放词表 3D 物体搜索展示。
- **充分性评价**：
  - 覆盖室内与室外、有深度与无深度、精度与效率、组件消融与鲁棒性，整体较充分。
  - 对比方法较多样，包含监督、零样本、training-free 方法。
  - 公平性方面：室内 2D-to-3D 提升基线多使用 GT depth，而 Ours− 不使用 GT depth，仍取得优势；Ours+ 进一步展示上限。
  - 但 KITTI-360 部分
