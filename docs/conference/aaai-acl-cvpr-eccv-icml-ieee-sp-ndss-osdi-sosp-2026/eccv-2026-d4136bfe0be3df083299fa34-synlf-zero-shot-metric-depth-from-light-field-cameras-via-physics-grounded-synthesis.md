---
title: "SynLF: Zero-Shot Metric Depth from Light Field Cameras via Physics-Grounded Synthesis"
title_zh: SynLF：通过物理驱动合成实现光场相机的零样本度量深度
authors: "Zhexuan Cao, Yuduo Guo, Peisheng Ding, Zhan Shi, Hui Qiao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6018.pdf"
tags: ["query:mono-depth"]
score: 7.0
evidence: 零样本度量深度估计
tldr: 单目度量深度估计因尺度歧义而病态，光场相机虽可借微基线视差恢复度量深度，但现有学习方法受训练数据稀缺与朗伯假设限制。本文提出SynLF，通过物理驱动的光场合成在线生成监督数据，并用先验初始化的迭代估计器VisDepth显式进行多视图遮挡推理。实验证明其在真实场景中实现鲁棒的零样本度量深度估计，显著提升泛化能力。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1276, \"height\": 2270}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-009.webp\", \"caption\": \"\", \"page\": 2, \"index\": 9, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-010.webp\", \"caption\": \"\", \"page\": 2, \"index\": 10, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-011.webp\", \"caption\": \"\", \"page\": 2, \"index\": 11, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-012.webp\", \"caption\": \"\", \"page\": 2, \"index\": 12, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-013.webp\", \"caption\": \"\", \"page\": 2, \"index\": 13, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 768, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 768, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 485, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 485, \"height\": 359}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 974, \"height\": 962}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-019.webp\", \"caption\": \"\", \"page\": 8, \"index\": 19, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-020.webp\", \"caption\": \"\", \"page\": 8, \"index\": 20, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-021.webp\", \"caption\": \"\", \"page\": 8, \"index\": 21, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-023.webp\", \"caption\": \"\", \"page\": 8, \"index\": 23, \"width\": 688, \"height\": 689}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 574, \"height\": 575}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-025.webp\", \"caption\": \"\", \"page\": 8, \"index\": 25, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-027.webp\", \"caption\": \"\", \"page\": 12, \"index\": 27, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-028.webp\", \"caption\": \"\", \"page\": 12, \"index\": 28, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-029.webp\", \"caption\": \"\", \"page\": 12, \"index\": 29, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-030.webp\", \"caption\": \"\", \"page\": 12, \"index\": 30, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-031.webp\", \"caption\": \"\", \"page\": 12, \"index\": 31, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-032.webp\", \"caption\": \"\", \"page\": 12, \"index\": 32, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-033.webp\", \"caption\": \"\", \"page\": 12, \"index\": 33, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-034.webp\", \"caption\": \"\", \"page\": 12, \"index\": 34, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-035.webp\", \"caption\": \"\", \"page\": 12, \"index\": 35, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-036.webp\", \"caption\": \"\", \"page\": 12, \"index\": 36, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-037.webp\", \"caption\": \"\", \"page\": 12, \"index\": 37, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-038.webp\", \"caption\": \"\", \"page\": 12, \"index\": 38, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-039.webp\", \"caption\": \"\", \"page\": 12, \"index\": 39, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-040.webp\", \"caption\": \"\", \"page\": 12, \"index\": 40, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-041.webp\", \"caption\": \"\", \"page\": 12, \"index\": 41, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-042.webp\", \"caption\": \"\", \"page\": 12, \"index\": 42, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-043.webp\", \"caption\": \"\", \"page\": 12, \"index\": 43, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-044.webp\", \"caption\": \"\", \"page\": 12, \"index\": 44, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-045.webp\", \"caption\": \"\", \"page\": 12, \"index\": 45, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-046.webp\", \"caption\": \"\", \"page\": 12, \"index\": 46, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-047.webp\", \"caption\": \"\", \"page\": 12, \"index\": 47, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-048.webp\", \"caption\": \"\", \"page\": 12, \"index\": 48, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-049.webp\", \"caption\": \"\", \"page\": 12, \"index\": 49, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-050.webp\", \"caption\": \"\", \"page\": 12, \"index\": 50, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-051.webp\", \"caption\": \"\", \"page\": 12, \"index\": 51, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-052.webp\", \"caption\": \"\", \"page\": 12, \"index\": 52, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-053.webp\", \"caption\": \"\", \"page\": 14, \"index\": 53, \"width\": 717, \"height\": 537}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-054.webp\", \"caption\": \"\", \"page\": 14, \"index\": 54, \"width\": 712, \"height\": 536}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-055.webp\", \"caption\": \"\", \"page\": 14, \"index\": 55, \"width\": 717, \"height\": 537}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-056.webp\", \"caption\": \"\", \"page\": 14, \"index\": 56, \"width\": 712, \"height\": 536}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-057.webp\", \"caption\": \"\", \"page\": 14, \"index\": 57, \"width\": 717, \"height\": 537}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-058.webp\", \"caption\": \"\", \"page\": 14, \"index\": 58, \"width\": 712, \"height\": 536}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-059.webp\", \"caption\": \"\", \"page\": 14, \"index\": 59, \"width\": 717, \"height\": 537}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d4136bfe0be3df083299fa34/fig-060.webp\", \"caption\": \"\", \"page\": 14, \"index\": 60, \"width\": 717, \"height\": 537}]"
motivation: 单目度量深度存在尺度歧义，光场学习方法受训练数据稀缺与外观过拟合限制。
method: 提出物理驱动的光场合成PG-LF，并设计先验初始化迭代估计器VisDepth做多视图遮挡推理。
result: 在真实场景中实现鲁棒的零样本度量深度估计，提升跨域泛化。
conclusion: 缓解数据稀缺并增强光场度量深度估计的真实世界鲁棒性。
---

## Abstract
Accurate monocular metric depth estimation remains inher-ently ill-posed due to scale ambiguity. Light field cameras mitigate thisambiguity by capturing micro-baseline disparities within a single lensto recover metric depth, but current learning-based solutions are lim-ited by scarce training data and often overfit Lambertian appearancepatterns, restricting real-world robustness. To address this, we proposeSynLF, which alleviates data scarcity via physics-grounded light field(PG-LF) synthesis and performs robust real-world metric depth esti-mation through VisDepth, a prior-initialized iterative estimator with ex-plicit multi-view occlusion reasoning. During training, we synthesize lightfield supervision on-the-fly from RGB-D via physics-grounded light fieldsynthesis, including geometry-consistent view synthesis, depth-dependentdefocus, and non-Lambertian perturbations. At inference, the model isdirectly evaluated on real light field captures without fine-tuning. Ex-tensive experiments demonstrate that SynLF generalizes zero-shot toour custom real-world light field dataset, which features highly chal-lenging conditions such as transparency, reflections, specular highlights,and textureless regions. It achieves 30 mm absolute and 1.4% relativeerrors across 0.5–2.5 m, demonstrating that physics-grounded LF syn-thesis from large-scale RGB-D provides a scalable and storage-efficientalternative to conventional light field acquisition for accurate single-lensmetric depth estimation.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：单目度量深度估计因尺度歧义而本质病态，仅凭单张 RGB 难以恢复绝对尺度。
- **光场相机的优势**：光场相机在单镜头内捕获微基线多视角视差，天然编码度量深度线索，可缓解尺度歧义。
- **现有瓶颈**：
  - 学习型光场深度估计受训练数据稀缺限制，现有监督光场数据集规模远小于大规模 RGB-D 语料。
  - 模型易过拟合理想朗伯外观，在遮挡、非朗伯表面、弱纹理等真实复杂场景中泛化差。
  - 多视角证据聚合多为隐式加权，缺少显式可见性约束，导致几何推理脆弱。
- **整体含义**：论文提出 SynLF，通过物理驱动光场合成从大规模 RGB-D 在线生成监督，并结合显式可见性推理的迭代深度估计器，实现真实光场相机上的零样本度量深度估计。

## 2. 方法论

### 2.1 核心思想

- 训练阶段：用 **PG-LF synthesis** 从 RGB-D 在线合成光场监督，避免预渲染光场数据集。
- 推理阶段：将训练好的 **VisDepth** 直接用于真实光场捕获，无需微调；输出视差后经相机标定的视差-深度映射转为度量深度。
- 关键耦合：合成与估计共享同一深度感知前向投影算子，使模型学习几何对应而非外观捷径。

### 2.2 PG-LF 合成

- **几何一致视图合成**：
  - 深度转视差：\(d = \alpha / Z_c - \beta\)，其中 \(\alpha\) 控制视差尺度，\(\beta\) 设零视差参考面。
  - 中心视图像素投影到子孔径视图：\(x_i = x_c + u_i d,\ y_i = y_c + v_i d\)。
  - 采用深度感知前向 splatting 与 z-buffer 式可见性选择：碰撞时保留最近样本，缓解遮挡错误排序。
  - 对去遮挡空洞使用随机填充策略，防止捷径学习。
- **深度依赖散焦**：
  - 真实光场相机存在随深度变化的离焦模糊；薄透镜模型下 CoC 与 \(|1/z - 1/z_f|\) 成正比，进而与 \(|d|\) 成正比。
  - 实现上按视差分层，每层分配高斯核，按后到前顺序合成，保留遮挡边界。
- **非朗伯扰动**：
  - 针对镜面反射、透明等非朗伯表面，显式扰动用于子孔径视图合成的视差，使投影样本偏离几何正确位置，模拟光度匹配失败。
  - 仅扰动子孔径视图，中心视图不变；仅作用于局部深度平坦但有纹理区域，排除深度边界和弱纹理区。

### 2.3 VisDepth 可见性感知迭代估计

- **先验引导视差初始化**：
  - 全分辨率 CNN 提取中心视图与源视图特征，构建原始光场相关体 \(C_{\mathrm{raw}}\)。
  - 引入冻结的单目基础模型 Depth Anything V2-Small 提供语义/结构先验 \(F_{\mathrm{mono}}\)。
  - 通过轻量 3D 代价聚合得到 \(C_{\mathrm{reg}}\)，再经 soft-argmin 回归初始视差 \(d_0\)。
- **显式可见性引导迭代估计**：
  - 每次迭代用当前视差 \(d_k\)，通过 PG-LF 中相同的深度感知前向投影计算各源视图可见性图 \(V_k^{(v)}\)。
  - 用可见性掩码聚合原始相关代价：\(C_{\mathrm{vis}}^k = \sum_v C_{\mathrm{raw}}^{(v)} \odot V_k^{(v)} / \sum_v V_k^{(v)}\)。
  - 将 \(C_{\mathrm{reg}}\) 与 \(C_{\mathrm{vis}}^k\) 拼接融合为 \(G_k\)，沿当前视差附近采样局部 1D 特征。
  - 多尺度 ConvGRU 更新隐藏状态并预测视差残差，\(d_{k+1}=d_k+\Delta d_k\)；训练与推理均迭代 24 次。
- **训练损失**：
  - 初始化损失 \(\mathcal{L}_{\mathrm{init}}=\|d_0-d\|_1\)。
  - 迭代损失 \(\mathcal{L}_{\mathrm{gru}}=\sum_k \gamma^{K-k}\|d_k-d\|_1\)，后期迭代权重更大。
  - 多尺度梯度正则 \(\mathcal{L}_{\mathrm{grad}}\)，对最终预测与真值做尺度-平移不变对齐后约束结构一致性。
  - 总损失为三者加权和。

## 3. 实验设计

- **训练数据集**：Hypersim，77,400 张逼真室内 RGB-D，过滤无效深度后 74,013 张；视差参数 \(\alpha=16,\ \beta=-9\)。
- **真实世界数据集**：
  - 自建光场采集系统：工业相机 + 9×9 微透镜阵列，配合高精度结构光相机获取度量深度。
  - 室内：173 组带标注捕获，覆盖漫反射物体及镜面金属、塑料、玻璃、反射显示屏等非朗伯材料。
  - 户外：30 组无标注光场，仅定性评估。
  - 结构光在严重透明/强反射区域可能失效，定量评估仅使用有效标注像素，所有方法在相同有效区域比较。
- **Benchmark 与指标**：
  - 真实室内数据上报告 MAE、RMSE、AbsRel、δ1。
  - 跨数据集评估使用公开 HCI 4D Light Field 与 Inria Dense Light Field，报告 MSE×100 与 BP0.07。
- **对比方法**：
  - 光场深度方法：OAVC、OACC-Net、OPAL、PlaneNet、ESMNet。
  - 控制变体：HCI 训练的 VisDepth、无单目先验、无显式可见性推理。
  - 跨数据集：PlaneNet、OACC-Net、OAVC。
- **主要定量结果**：
  - 真实室内零样本：SynLF 达 MAE 30.05 mm、RMSE 144.34 mm、AbsRel 1.38%、δ1 98.77%，优于所有对比方法。
  - 相比 PlaneNet，MAE 从 91.31 mm 降至 30.05 mm；相比 ESMNet，从 110.86 mm 降至 30.05 mm。
  - 与相同 VisDepth 但 HCI 训练相比，MAE 从 52.95 mm 降至 30.05 mm。
- **消融与补充实验**：
  - 互控实验：PlaneNet/VisDepth × HCI/PG-LF，验证 PG-LF 数据收益与 VisDepth 架构收益正交。
  - 材料分层：漫反射、镜面、透明场景误差依次升高。
  - 散焦与非朗伯扰动消融：两者独立有效，组合最佳。
  - GRU 迭代次数：6→24 次使 MAE 从 36.39 mm 降至 30.05 mm。
  - 单目先验规模：DAv2-Small 到 DAv2-Large 无明显提升。
  - 跨数据集：HCI 训练方法在 Inria 上退化明显，SynLF 与 OAVC 跨集更稳定；SynLF 在 HCI 上略优于 OAVC，在 Inria 上有竞争力。
  - 户外定性：展示稳定视差与结构边界。

## 4. 资源与算力

- 论文明确给出的训练设置：
  - PyTorch 实现。
  - Hypersim 上训练，约 8K 优化步，约两遍训练集。
  - AdamW，总 batch size 16。
  - 随机裁剪 768×768。
  - 学习率 5×10⁻⁵ 线性 warmup 至 5×10⁻⁴，再多项式衰减至 1×10⁻⁵。
  - ConvGRU 迭代 24 次。
- **未明确说明**：
  - GPU 型号、数量、显存、训练总时长、能耗等均未在论文正文中报告。
  - 因此无法准确评估训练算力成本与复现门槛。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 真实室内零样本对比：1 组主实验，含 5 个外部基线 + 3 个自身变体。
  - 互控数据/架构实验：4 种组合。
  - 材料分层实验：3 类材料、143 个可分离场景。
  - 跨数据集实验：HCI 4D 与 Inria Dense 两个公开 benchmark。
  - 消融实验：散焦 × 非朗伯扰动 4 种组合；GRU 迭代次数；单目先验规模。
  - 定性实验：真实室内挑战场景与户外场景。
- **充分性评价**：
  - 覆盖了零样本泛化、跨数据集、数据/架构解耦、关键模块消融、材料难度分层，整体较充分。
  - 对比方法包含优化型与学习型代表方法，且统一使用官方预训练模型、不做微调或测试时适配，比较相对公平。
  - 真实数据所有方法在相同有效像素区域评估，减少部分偏差。
- **潜在不足**：
  - 真实数据集为自建，规模有限，且透明/反射区域 GT 依赖结构光有效性掩码，可能引入材料相关偏差。
  - 户外无定量标注，仅有定性结果。
  - 跨数据集上 SynLF 并非所有指标最优，HCI 域内 MSE 高于 HCI 训练方法。
  - 未报告多次运行方差或统计显著性检验。

## 6. 主要结论与发现

- 真实世界光场深度估计的主要瓶颈不仅是模型设计，更是理想化监督与真实成像条件之间的不匹配。
- 大规模 RGB-D 数据在保留多视图几何并引入物理非理想效应后，可转化为有效光场监督。
- PG-LF 合成提供数据层面的显著收益，独立于模型架构；VisDepth 提供正交的架构收益。
- 显式可见性推理对遮挡、深度不连续、弱纹理和视图相关外观变化下的鲁棒性至关重要。
- 单目先验的作用主要是稳定初始化，而非最终精度来源；更强先验未必带来提升。
- SynLF 在 0.5–2.5 m 范围内实现约 30 mm 绝对误差和 1.4% 相对误差，证明物理驱动合成可替代传统光场采集，支持零样本单镜头度量深度估计。

## 7. 优点

- **任务驱动的合成设计**：不追求通用照片级真实，而是选择性建模直接破坏视差对应的因素：遮挡、深度依赖散焦、非朗伯外观。
- **在线合成、存储高效**：无需预渲染大量子孔径视图，直接从 RGB-D 在线生成监督，可扩展至大规模数据。
- **几何一致性保障**：前向 splatting、z-buffer 可见性和共享投影算子使合成与推理紧密耦合，减少外观捷径。
- **显式可见性推理**：VisDepth 在迭代中动态计算每视图可见性并掩码聚合代价，优于隐式加权。
- **零样本泛化强**：在自建真实挑战场景中显著优于多个光场深度基线，且无需微调。
- **实验设计较严谨**：互控实验分离数据与架构贡献；材料分层揭示误差来源；跨数据集校准泛化性。
- **工程可行性**：推理阶段不需要 PG-LF 合成，仅需训练后的 VisDepth 与离线相机标定。

## 8. 不足与局限

- **合成仍为近似**：未完整建模真实光场形成过程、复杂光学效应和严重材料相关外观变化。
- **场景覆盖有限**：定量评估集中于静态室内场景；动态场景、复杂户外场景未定量验证。
- **透明/反射区域 GT 困难**：结构光在透明或强反射区域本身可能失效，即使使用有效掩码，GT 质量仍可能影响评估。
- **跨数据集精度非全面领先**：在 HCI 和 Inria 上并非所有指标最优，HCI 域内 MSE 高于 HCI 训练方法。
- **依赖单目基础模型先验**：虽然 DAv2-Large 未提升，但初始化仍依赖冻结的 Depth Anything V2-Small。
- **相机与标定依赖**：度量深度转换依赖相机特定视差-深度映射，跨不同光场相机需重新标定。
- **算力信息缺失**：未报告 GPU 型号、数量、训练时长，复现成本与可扩展性评估不完整。
- **潜在数据偏差**：训练主要来自 Hypersim 合成室内数据，真实测试集为自建，二者域差异和采集偏差可能影响泛化结论。
- **应用限制**：当前方法面向静态场景单帧光场度量深度，对动态物体、极端透明/镜面、远距离或强运动模糊场景的鲁棒性仍待验证。

（完）
