---
title: Large-Scale Light Field Synthesis from Videos Enables Geometrically Consistent Bokeh Editing
title_zh: 大规模光场视频合成实现几何一致的散景编辑
authors: "Haoming Cai, Zhoutong Zhang, Christopher Metzler, Shumian Xin"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6560.pdf"
tags: ["query:neural-bokeh"]
score: 8.0
evidence: 基于光场的散景编辑与景深控制
tldr: 现有焦点与景深编辑工具在反射、精细结构等复杂几何场景下容易失效，其根源在于训练数据生成难以兼顾几何保真与可扩展性。本文提出Vid2Bokeh，利用前馈三维重建从随手拍摄的视频中重建稠密25×25光场，构建可扩展的散景数据采集流程。实验表明该方法能在复杂几何场景下保持几何一致的编辑效果，为拍摄后的焦点与景深控制提供更可靠的数据支撑。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 1217, \"height\": 354}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 2294, \"height\": 466}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1222, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 384, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 2294, \"height\": 466}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 1568, \"height\": 896}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 1568, \"height\": 896}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 1131, \"height\": 410}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-009.webp\", \"caption\": \"\", \"page\": 7, \"index\": 9, \"width\": 384, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-010.webp\", \"caption\": \"\", \"page\": 7, \"index\": 10, \"width\": 384, \"height\": 384}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-011.webp\", \"caption\": \"\", \"page\": 7, \"index\": 11, \"width\": 480, \"height\": 268}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-012.webp\", \"caption\": \"\", \"page\": 7, \"index\": 12, \"width\": 2456, \"height\": 660}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-013.webp\", \"caption\": \"\", \"page\": 7, \"index\": 13, \"width\": 2456, \"height\": 660}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-014.webp\", \"caption\": \"\", \"page\": 7, \"index\": 14, \"width\": 2456, \"height\": 660}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-015.webp\", \"caption\": \"\", \"page\": 8, \"index\": 15, \"width\": 3456, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-016.webp\", \"caption\": \"\", \"page\": 8, \"index\": 16, \"width\": 1166, \"height\": 518}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-017.webp\", \"caption\": \"\", \"page\": 9, \"index\": 17, \"width\": 5700, \"height\": 1500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-018.webp\", \"caption\": \"\", \"page\": 10, \"index\": 18, \"width\": 544, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-019.webp\", \"caption\": \"\", \"page\": 10, \"index\": 19, \"width\": 1022, \"height\": 408}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-020.webp\", \"caption\": \"\", \"page\": 11, \"index\": 20, \"width\": 1980, \"height\": 1204}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-021.webp\", \"caption\": \"\", \"page\": 12, \"index\": 21, \"width\": 3358, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-022.webp\", \"caption\": \"\", \"page\": 12, \"index\": 22, \"width\": 3358, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-023.webp\", \"caption\": \"\", \"page\": 13, \"index\": 23, \"width\": 3358, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-024.webp\", \"caption\": \"\", \"page\": 14, \"index\": 24, \"width\": 3358, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-025.webp\", \"caption\": \"\", \"page\": 14, \"index\": 25, \"width\": 3358, \"height\": 848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-026.webp\", \"caption\": \"\", \"page\": 15, \"index\": 26, \"width\": 2373, \"height\": 572}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d99ac3d61d89b6249daf739f/fig-027.webp\", \"caption\": \"\", \"page\": 15, \"index\": 27, \"width\": 2373, \"height\": 2241}]"
motivation: 现有焦点与景深编辑工具在反射和精细结构等复杂几何场景下失效，根源在于训练数据生成难以兼顾几何保真与可扩展性。
method: 提出Vid2Bokeh，通过前馈三维重建从随手视频重建稠密25×25光场，构建可扩展的散景数据采集流程。
result: 该流程生成几何一致的光场数据，使焦点与景深编辑在复杂几何场景下保持正确遮挡与细节。
conclusion: 为几何一致的散景编辑提供了可扩展的数据基础，提升后期景深控制质量。
---

## Abstract
Focus and depth of field (DoF) define where attention falls and how much of a scene appears sharp. Adjusting both after capture provides creators two-dimensional control over visual attention. However, existing focus and DoF editing tools fail when applied to scenes with complex geometries, such as reflections and fine features. This failure is a result of fundamental limitations in existing training data generation pipelines: current pipelines either sacrifice geometric fidelity for scalability, or sacrifice scalability for geometric fidelity. To address this, we present Vid2Bokeh, a scalable bokeh data acquisition pipeline that reconstructs dense 25×25 light fields from casual videos via feed-forward 3D reconstruction, bypassing depth estimation entirely and avoiding the geometric errors it introduces. The resulting Vid2Bokeh Dataset comprises over 100K light fields on diverse real-world scenes, simultaneously achieving scene diversity, optical density, and geometric fidelity that no existing bokeh dataset or bokeh data acquisition pipeline provides. By training on this geometrically faithful bokeh data, we introduce a diffusion model for full bidirectional focus–DoF editing that outperforms depth-based baselines on complex geometries. This result demonstrates that geometric fidelity in large-scale training data is the key to geometrically consistent bokeh editing.

---

## 论文详细总结（自动生成）

# Vid2Bokeh：大规模光场视频合成实现几何一致的散景编辑 —— 论文总结

## 1. 核心问题与研究动机

- **应用背景**：对焦（Focus）与景深（DoF）是视觉叙事的核心手段。后期散景编辑（post-capture bokeh editing）中，用户越来越需要"全参数"控制——无论输入是全焦图像还是已含自然散景的图像，都能同时移动焦平面并调节景深。
- **核心痛点**：现有方法在**复杂几何场景**（镜面反射、透明容器、细密结构如网球网/自行车辐条/树枝）上普遍失效，出现边界伪影、遮挡错误、过度模糊等。
- **根本原因不在模型，而在训练数据**：现有数据生成流程陷入一个"三难困境"（Table 1）：
  - **物理采集**（多相机/光场相机）：几何准确，但**不可扩展**、采集门槛高；
  - **合成式合成**（Compositional Synthesis，如 BokehDiff、BokehMe）：不依赖深度，但场景多样性受限；
  - **基于深度的合成**（如 DiffCamera、GenRefocus）：可扩展，但**必然（直接或间接）依赖深度估计**，深度误差会传播进训练监督信号，导致模型在复杂几何上系统性失败。
- **整体含义**：论文主张"**大规模训练数据中的几何保真度，而非模型架构，才是几何一致散景编辑的关键**"，并给出同时满足可扩展性与几何保真的数据采集方案。

## 2. 方法论

### 2.1 核心思想
用**前馈三维重建 + 光场表示**替代"深度图 + 2.5D 渲染"范式：光场天然建模视差与遮挡，无需显式深度即可正确解析反射与复杂遮挡，从而在源头避免几何误差进入监督数据。

### 2.2 关键技术流程（Vid2Bokeh Pipeline）

- **输入源**：DL3DV-10K 数据集中的真实视频（960p，含标定相机位姿）；每个片段视为短多视图序列。
- **光场构建**：随机选取若干帧作为参考视图，每个参考位姿定义一个光场中心；围绕中心沿水平/垂直轴扰动位姿（内参固定）生成 **25×25 虚拟相机网格**；用前馈 3D 模型 **LaCT**（test-time training 类方法）一次前向合成全部虚拟视角 RGB，得到稠密光场 L(u,v,s,t,c)，其中 (u,v) 为孔径平面角坐标，(s,t) 为空间像素坐标，c 为颜色通道。
- **场景自适应基线标定**：固定基线无法适配不同深度范围。用 **RAFT** 估计相邻视图光流，缩放基线使平均光流幅值落在经验区间 **1–3 像素**，保证跨场景视差一致、重聚焦稳定。
- **散景渲染（光场重聚焦公式）**：
  - I(s,t,c; κ, a) = ∬_{A(a)} L(u, v, s+κu, t+κv, c) du dv
  - 其中 κ 参数化焦平面位置，a 为孔径半径，A(a) 为半径 a 的圆形积分区域。小孔径趋近全焦（AiF），大孔径产生强散焦。
- **监督对生成**：随机采样两组光学配置 (κ₁,a₁) 与 (κ₂,a₂)=(κ₁+Δκ, a₁+Δa)，分别渲染得 I_in 与 I_gt，连续采样稠密覆盖整个"焦点–景深"联合空间。
- **数据集规模与效率**：Vid2Bokeh Dataset 含 **100K+ 真实场景光场**，角分辨率 25×25（超过既有光场数据集），单个光场在单张 A100 上合成 **<30 秒**，全数据集可**按需生成**并存储于 **10 TB** 以内。
- **编辑模型**：基于 **SDXL 微调**的扩散模型，实现**双向**焦点–景深编辑。
  - 偏移量 (Δκ, Δa) 经 Fourier 特征 + 轻量 MLP 编码为条件向量，参与 cross-attention；
  - 输入图与目标图经**冻结 VAE** 编码为隐变量 z_s、z_e，采用受 InstructMove 启发的**空间拼接（spatial concatenation）**设计，在拼接隐变量上做标准扩散训练；
  - 推理时源图编码为 z_s，目标分支初始化为纯噪声，U-Net 以 z_s 与 (Δκ,Δa) 为条件迭代去噪，输出指定光学配置下的编辑结果。

## 3. 实验设计

### 3.1 数据采集保真度验证
- **真实复杂场景定性对比**：与基于深度的合成（Depth-Anything 深度 + 深度式散景合成）对比，展示透明容器、自行车轮辐条、透视/遮挡场景下的失败与成功（Fig. 3）。
- **Blender 路径追踪定量验证**：渲染近全焦视频再过 Vid2Bokeh 流程，设两个参照：
  - **Blender Direct Bokeh**（路径追踪，物理真值）；
  - **Blender LF-based Bokeh**（直接从 Blender 提取的理想 25×25 光场，作为光场表示的理论上界）。
  - 指标：PSNR↑ / SSIM↑ / MS-SSIM↑ / LPIPS↓ / DISTS↓，在 **100 个不同视点**上平均；对照基线为 BokehDiff。
  - 结果：对 Direct GT，Vid2Bokeh 33.37/0.931/0.984/0.147/0.091 优于 BokehDiff 30.72/0.889/0.954/0.216/0.101；对上界参照亦接近。
- **重建误差鲁棒性压力测试**：故意喂入稀疏视图输入以在单视角中制造重建伪影，验证最终散景因 25×25 视角积分而保持无伪影（Fig. 5）。

### 3.2 编辑任务评测（四大任务）
1. **重聚焦（Refocusing）**：固定孔径，双向扫描 Δκ。基线含 DiffCamera（直接重聚焦）与"去模糊 + 重聚焦"流水线（DRBNet + Dr.Bokeh / BokehMe / BokehDiff）。遵循 BokehDiff 的评测协议，基线用**二分搜索**确定最佳焦深。结果：Ours 在近→远 29.62/0.907/0.198/0.108、远→近 29.51/0.893/0.183/0.121，全指标领先（Table 3）。
2. **散景渲染（Bokeh Rendering）**：固定焦平面、逐步增大孔径。测试于 **Vid2Bokeh 测试集**与 **EBB! 验证集**；基线 BokehMe、Dr.Bokeh、Bokehlicious、BokehDiff。EBB 孔径分布与训练分布差异大，故按 Bokehlicious 做法在 EBB 训练集做**一个 epoch 的轻量微调**对齐散景轮廓（Table 4）。
3. **散焦去模糊（Defocus Blur Removal）**：目标孔径近零。测试于 Vid2Bokeh 测试集与 **DPDD**，基线 DRBNet、Restormer（Table 5）。
4. **联合焦点–景深编辑**：单一模型内同时完成重聚焦与孔径调节，生成连贯的 2D focus–DoF 网格（Fig. 7）。
- 另有大量**真实图像定性对比**：网球场（前景网→背景场地）、细杆、自行车辐条、树与塔等（Fig. 8、Fig. 10、Fig. 11）。

## 4. 资源与算力

- **训练**：**8 张 NVIDIA A100 GPU，100K 迭代，约 4 天**。
- **数据生成**：单个 25×25 光场在**单张 A100 上 <30 秒**；全数据集存储 **≤10 TB**，可按需生成。
- 论文未给出模型参数量、推理时延、总 GPU 时数等更细的算力统计，也未报告数据生成的总耗时估算。

## 5. 实验数量与充分性评估

- **实验组数**：约 6 大组——(1) 复杂场景数据采集定性对比；(2) Blender 定量保真度验证（100 视点）；(3) 重建误差鲁棒性压力测试；(4) 重聚焦（2 个方向 × 4 个基线）；(5) 散景渲染（2 个数据集 × 4 个基线 × 5 个孔径）；(6) 去模糊（2 个数据集 × 2 个基线 × 5 个模糊等级），外加联合编辑的可视化验证。消融研究仅提及在补充材料中，正文未给出。
- **客观性与公平性**：
  - 优点：采用**两重参照**（物理路径追踪真值 + 光场理论上界）验证数据保真度，是较严谨的设计；基线评测遵循既有协议（BokehDiff 的二分搜索焦深）；对分布不匹配的 EBB 做了对齐微调。
  - 注意点：Vid2Bokeh 测试集的"真值"本身由本文流程合成，存在**自洽性偏置**（自产数据上评测自家方法），Blender 实验在一定程度上缓解了该疑虑；但 Blender 场景与真实复杂场景仍有域差。
  - 个别指标并非全面领先：EBB! 上 PSNR 24.02 略低于 BokehDiff 的 24.38，去模糊任务在 DPDD 上 PSNR/SSIM 也只是"有竞争力"而非最优。
  - 缺乏用户主观评测（user study）与人类感知层面的评估。

## 6. 主要结论与发现

- Vid2Bokeh 是**首个同时实现"无深度估计（Depth-Est-Free）"与"大规模可扩展"**的散景数据采集流程，破解了数据采集的保真–规模三难困境。
- 光场表示在散景合成上**本质上比 2.5D 深度图更稳健**，能自然解析反射、透明面、细结构遮挡。
- 光场积分对**单视角重建误差具有鲁棒性**，故不依赖完美的新视角合成质量。
- 仅用**标准扩散模型微调**（不做架构创新）即可在复杂几何上取得几何一致的双向焦点–景深编辑，说明**数据几何保真度是决定性因素**。
- 实际收益：采集门槛极低（只需随手拍摄的手持视频），无需单反、三脚架与像素级对齐，用户可自建训练数据。

## 7. 优点

- **范式创新**：把"数据生成"作为核心贡献，用前馈 3D 重建 + 光
