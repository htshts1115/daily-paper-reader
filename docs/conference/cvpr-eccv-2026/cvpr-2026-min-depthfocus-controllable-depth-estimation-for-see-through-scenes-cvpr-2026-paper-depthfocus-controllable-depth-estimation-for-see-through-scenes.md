---
title: "DepthFocus: Controllable Depth Estimation for See-Through Scenes"
title_zh: DepthFocus：面向穿透场景的可控深度估计
authors: "Min, Junhong, Kim, Jimin, Kim, Minwook, Min, Cheol-Hui, Jeon, Youngpil, Choi, Minyong"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Min_DepthFocus_Controllable_Depth_Estimation_for_See-Through_Scenes_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 6.0
evidence: 透射材质导致的分层深度歧义
tldr: 真实世界深度往往并不唯一，透射材质会产生分层歧义，而现有深度估计模型只能输出锚定最近表面的静态深度图，多头的扩展也受固定特征表示瓶颈制约。DepthFocus 提出可操控的视觉 Transformer，把深度估计重新定义为条件感知控制，依据物理参考深度动态调制计算。该方法能按需聚焦到指定深度层，为透明与穿透场景的深度感知提供了可控的新思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-min-depthfocus-controllable-depth-estimation-for-see-through-scenes-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 2381, \"height\": 595}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-min-depthfocus-controllable-depth-estimation-for-see-through-scenes-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 5481, \"height\": 4088}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-min-depthfocus-controllable-depth-estimation-for-see-through-scenes-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 2159, \"height\": 1078}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-min-depthfocus-controllable-depth-estimation-for-see-through-scenes-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 1372, \"height\": 1041}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-min-depthfocus-controllable-depth-estimation-for-see-through-scenes-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 1511, \"height\": 332}]"
motivation: 真实深度并不唯一，透射材质造成分层歧义，现有模型只能输出锚定最近表面的静态深度图。
method: 提出可操控视觉 Transformer DepthFocus，依据物理参考深度动态调制计算，实现条件感知的深度估计。
result: 模型可按需聚焦指定深度层，缓解固定特征表示带来的瓶颈。
conclusion: 为透明与穿透场景提供了可控深度感知的新思路。
---

## Abstract
Depth in the real world is rarely singular. Transmissive materials create layered ambiguities that confound conventional perception systems. Existing models remain passive; conventional approaches typically estimate static depth maps anchored to the nearest surface, and even recent multi-head extensions suffer from a representational bottleneck due to fixed feature representations. This stands in contrast to human vision, which actively shifts focus to perceive a desired depth. We introduce DepthFocus, a steerable Vision Transformer that redefines stereo depth estimation as condition-aware control. Instead of extracting fixed features, our model dynamically modulates its computation based on a physical reference depth, integrating dual conditional mechanisms to selectively perceive geometry aligned with the desired focus. Leveraging a newly curated large-scale synthetic dataset, DepthFocus achieves state-of-the-art results across all evaluated benchmarks, including both standard single-layer and complex multi-layered scenarios. While maintaining high precision in opaque regions, our approach effectively resolves depth ambiguities in transparent and reflective scenes by selectively reconstructing geometry at a target distance. This capability enables robust, intent-driven perception that significantly outperforms existing multi-layer methods, marking a substantial step toward active 3D perception. \noindent Project page: \href https://junhong-3dv.github.io/depthfocus-project/ this https URL .

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：真实世界中的深度往往不是单一值。透明、半透明、反射材料会让多个深度层在同一像素上叠加，形成“穿透场景”中的分层歧义。
- **现有范式局限**：主流单目/立体深度估计模型是被动的，通常只输出锚定最近可见表面的静态深度图；即使近期多头扩展尝试估计多层，也因固定特征表示而遭遇“表示瓶颈”，难以同时编码多个冲突几何。
- **人类视觉对比**：人类会主动调整焦点，按意图观察前景或背景。论文希望把深度估计从“被动回归静态深度”重新定义为“条件感知控制”，让模型按用户指定的物理参考深度选择性重建某一层几何。
- **整体含义**：DepthFocus 试图在保持标准不透明场景精度的同时，解决透明/反射/多层场景的深度歧义，推动面向机器人的主动、意图驱动 3D 感知。

## 2. 方法论：核心思想与关键技术

- **核心思想**：将深度估计建模为条件函数 \(f(x,c)\)，其中 \(x\) 为图像，\(c\in[0,1]\) 是标量控制变量，代表用户意图的物理距离/焦点。模型不一次性回归所有层，而是预测与参考深度对齐的那一层表面。
- **理想条件估计器性质**：
  - **不透明确定性**：不透明区域深度不随 \(c\) 改变。
  - **透射单调性**：在透明区域，\(c\) 增大时估计深度应单调向更远层移动，不能回退到更浅层。
  - **参考邻近与离散选择**：在候选深度集合中，选择距离参考深度平面 \(d_{\text{ref}}(c)\) 最近的有效层。
- **控制变量物理化**：将 \(c\) 映射为参考视差：
  \[
  d_{\text{ref}}(c)=(1-c)\cdot d_{\max}
  \]
  从而让 \(c\) 成为归一化视锥坐标，控制目标深度平面。
- **条件特征调制**：
  - **C-MoE（条件混合专家）**：路由器 \(R(x,c)\) 根据输入和 \(c\) 生成专家权重，组合若干专家子网络，专家数通常 \(N\le 3\)，以动态选择特征变换路径。
  - **DCI（直接条件注入）**：用单头注意力式机制注入 \(c\)，形式为 \(A(x,c)=\sigma(q_x\cdot k_c)\cdot v_c\)，再投影并加回特征流，显式引导网络关注目标深度。
- **架构集成**：基于强立体匹配基线构建。重骨干网络只运行一次，随后在条件多分辨率融合和条件迭代细化阶段插入 C-block，其中并行使用 DCI 和 C-MoE 替代标准 FFN 或注意力块，从而在调整 \(c\) 时无需重复执行重骨干。
- **训练监督**：
  - 在视差域中动态分配标签：选择不超过参考视差 \(d_{\text{ref}}(c)\) 的最大有效视差；若不存在，则选最小视差。即让模型对准参考深度平面“后方”的最近有效层。
  - 使用辅助分割头，鼓励骨干编码玻璃、镜面等透射/反射材质语义，辅助消歧。

## 3. 实验设计

- **单层深度 benchmark**：
  - **Booster** 与 **Middlebury v3**。
  - 指标：EPE、Bad-x，在非遮挡区域评估。
  - 将 DepthFocus 设置为“最近意图”以预测第一可见表面，验证标准不透明/反射透射场景精度。
- **多层合成 benchmark**：
  - 自建高分辨率、照片级合成数据，包含重叠透射表面。
  - 评估不透明区域及透射区域第 1 至第 4 层。
  - 对比单层模型：Sel-IGEV、StereoAnywhere、FoundationStereo、S²M²、S²M²(ft)。
  - 对比多层基线：RAFT-(4layer)、ASGrasp-2layer-ft、ASGrasp-4layer-ft。
- **真实实验室双层 benchmark**：
  - 5 个场景，使用 60% 与 80% 透射率亚克力板，机械臂精确放置，形成受控双层配置。
  - 共 180 个立体对；背景层 GT 由移除板后使用结构光 3D 扫描仪获得。
- **LayeredFlow 验证集**：
  - 真实世界多层/非朗伯场景，稀疏标记 GT，层 1 至层 3。
- **消融实验**：
  - 在合成 benchmark 上移除 C-MoE、DCI、Seg Loss、Data Curation，分析各组件贡献。
- **评估协议注意点**
