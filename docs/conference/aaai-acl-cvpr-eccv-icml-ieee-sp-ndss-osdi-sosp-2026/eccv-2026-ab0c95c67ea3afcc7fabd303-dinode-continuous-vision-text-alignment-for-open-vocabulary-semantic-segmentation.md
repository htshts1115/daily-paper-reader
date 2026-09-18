---
title: "DINOde: Continuous Vision-Text Alignment for Open-Vocabulary Semantic Segmentation"
title_zh: DINOde：面向开放词汇语义分割的连续视觉文本对齐
authors: "Sung-Hoon Yoon, Hoyong Kwon, Changgyoon Oh, KUK-JIN YOON"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2958.pdf"
tags: ["query:seg"]
score: 9.0
evidence: 视觉文本对齐的开放词汇语义分割
tldr: 论文针对开放词汇语义分割中DINOv3视觉表征强但缺乏原生文本对齐、难以直接分割未定义类别的问题，提出基于常微分方程的DINOde框架。方法用语义文本流将CLIP文本嵌入沿连续ODE轨迹演化到DINO流形，并用全局上下文流逐步精化CLS令牌的整体图像表示。实验表明该对齐显著提升开放词汇分割性能，为文本引导的通用分割提供新思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 4212, \"height\": 2218}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-002.webp\", \"caption\": \"\", \"page\": 7, \"index\": 2, \"width\": 1325, \"height\": 697}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-003.webp\", \"caption\": \"\", \"page\": 7, \"index\": 3, \"width\": 552, \"height\": 252}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-004.webp\", \"caption\": \"\", \"page\": 7, \"index\": 4, \"width\": 960, \"height\": 459}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 500, \"height\": 334}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 500, \"height\": 334}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 404, \"height\": 363}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-008.webp\", \"caption\": \"\", \"page\": 10, \"index\": 8, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-009.webp\", \"caption\": \"\", \"page\": 10, \"index\": 9, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-010.webp\", \"caption\": \"\", \"page\": 10, \"index\": 10, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-011.webp\", \"caption\": \"\", \"page\": 10, \"index\": 11, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-012.webp\", \"caption\": \"\", \"page\": 10, \"index\": 12, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-013.webp\", \"caption\": \"\", \"page\": 10, \"index\": 13, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-014.webp\", \"caption\": \"\", \"page\": 10, \"index\": 14, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-015.webp\", \"caption\": \"\", \"page\": 10, \"index\": 15, \"width\": 464, \"height\": 282}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-016.webp\", \"caption\": \"\", \"page\": 15, \"index\": 16, \"width\": 500, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-017.webp\", \"caption\": \"\", \"page\": 15, \"index\": 17, \"width\": 519, \"height\": 330}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-018.webp\", \"caption\": \"\", \"page\": 15, \"index\": 18, \"width\": 500, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-019.webp\", \"caption\": \"\", \"page\": 15, \"index\": 19, \"width\": 500, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-020.webp\", \"caption\": \"\", \"page\": 15, \"index\": 20, \"width\": 519, \"height\": 330}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-021.webp\", \"caption\": \"\", \"page\": 15, \"index\": 21, \"width\": 500, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-022.webp\", \"caption\": \"\", \"page\": 15, \"index\": 22, \"width\": 500, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-023.webp\", \"caption\": \"\", \"page\": 15, \"index\": 23, \"width\": 519, \"height\": 330}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-024.webp\", \"caption\": \"\", \"page\": 15, \"index\": 24, \"width\": 500, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-025.webp\", \"caption\": \"\", \"page\": 15, \"index\": 25, \"width\": 500, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-026.webp\", \"caption\": \"\", \"page\": 15, \"index\": 26, \"width\": 519, \"height\": 330}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-027.webp\", \"caption\": \"\", \"page\": 15, \"index\": 27, \"width\": 500, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-028.webp\", \"caption\": \"\", \"page\": 15, \"index\": 28, \"width\": 500, \"height\": 376}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-029.webp\", \"caption\": \"\", \"page\": 15, \"index\": 29, \"width\": 519, \"height\": 330}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-ab0c95c67ea3afcc7fabd303/fig-030.webp\", \"caption\": \"\", \"page\": 15, \"index\": 30, \"width\": 500, \"height\": 375}]"
motivation: DINOv3视觉表征强但缺乏原生文本对齐，难直接用于开放词汇分割。
method: 用ODE轨迹将CLIP文本嵌入对齐到DINO流形，并精化全局图像表示。
result: 显著提升开放词汇语义分割精度，支持未定义类别。
conclusion: 为文本引导的通用分割建立连续视觉文本对齐范式。
---

## Abstract
Open-vocabulary semantic segmentation (OVSS) leveragestextual semantics to segment objects beyond predefined categories. Whilethe self-supervised model DINOv3 provides strong structured visual rep-resentations, its lack of native textual alignment hinders direct applica-tion to OVSS. To bridge this gap, we propose DINOde, an ODE-basedframework that continuously aligns CLIP text embeddings to the DINOvisual manifold. Our approach employs two complementary components:(i) Semantic Text Flow (STF), which evolves text embeddings toward theDINO manifold through a continuous ODE trajectory, and (ii) GlobalContext Flow (GCF), which progressively refines the holistic image rep-resentation carried by DINO’s CLS token. To preserve the hypersphericalgeometry of the feature space during this evolution, we further intro-duce Velocity Tangent Projection, which constrains the learned veloc-ity field to the tangent space through projection. By modeling align-ment as a continuous trajectory, DINOde avoids the manifold entan-glement inherent in discrete MLP projections and yields more robustcross-modal alignment. Extensive experiments demonstrate that DIN-Ode consistently outperforms existing methods and achieves state-of-the-art performance across multiple OVSS benchmarks. The code is availableat https://github.com/yoon307/DINOde.

---

## 论文详细总结（自动生成）

# DINOde 论文总结

## 1. 核心问题与整体含义

- **研究背景**：开放词汇语义分割（OVSS）旨在利用文本语义分割预定义类别之外的对象，是自动驾驶、医学影像等真实场景部署的关键能力。
- **现有瓶颈**：
  - CLIP 等视觉语言模型的视觉编码器主要面向全局图文对齐优化，输出表征粗糙且空间纠缠，不适合稠密预测。
  - 自监督模型（DINO/DINOv2/DINOv3）具有优越的定位与对象中心表征能力，但完全在视觉模态内训练，表征空间与文本语义**天然不对齐**，无法直接进行开放词汇推理。
  - 现有桥接方案（如 dino.txt 需从头训练文本编码器；Talk2DINO 用非线性 MLP 映射）本质上是用**单步、离散的欧氏捷径**近似复杂的跨模态变换，忽视特征流形的内在曲率，导致语义纠缠与邻域关系扭曲。
- **整体含义**：论文提出 **DINOde**，将视觉-文本对齐建模为**连续 ODE 轨迹**，让 CLIP 文本嵌入沿平滑流形演化至 DINOv3 视觉流形，避免离散投影带来的流形纠缠，为文本引导的通用分割建立连续对齐范式。

## 2. 方法论

### 2.1 核心思想
- 用神经常微分方程（Neural ODE）替代单步 MLP 投影，学习一个**时变速度场**，使文本嵌入在单位超球面上连续、几何保持地流向 DINO 视觉流形。
- 同时对齐**局部（文本嵌入）**与**全局（CLS token）**表征，最大化全局-局部语义一致性。

### 2.2 关键组件

- **语义文本流（STF）**：
  - 先经可学习线性投影将 CLIP 文本嵌入映射到 DINO 维度并 ℓ2 归一化，得到初始状态 `z0 = Norm(W·z_text)`。
  - 以 DINO patch token 的 top-K 池化结果 `z_img = Norm(Pool(Z_img))` 作为视觉监督目标。
  - 通过 ODE `dz_t/dt = v_θ(z_t, t)` 从 t=0 积分到 t=1，得到对齐后的文本锚点 `ẑ_text = z1`。
  - 时间条件通过正弦嵌入 γ(t) 以特征级调制注入速度网络。

- **全局上下文流（GCF）**：
  - 对 DINOv3 的 [CLS] token 先做轻量投影与 ℓ2 归一化，得到 `c0`。
  - 用另一速度网络 `u_φ` 沿 ODE `dc_t/dt = u_φ(c_t, t)` 演化，得到精化的全局表征 `ẑ_cls = c1`。
  - 与 STF 类似采用 VTP 与欧拉求解器。

- **速度切向投影（VTP）**：
  - 为保持超球面几何，将速度投影到当前状态的切空间：
    `ṽ_θ(z_t,t) = v_θ(z_t,t) − ⟨v_θ(z_t,t), z_t⟩ z_t`（GCF 同理）。
  - 积分时每步更新后重新归一化：`z_{t+Δt} = Norm(z_t + Δt·ṽ_θ(z_t,t))`。

- **损失函数**：
  - 拼接池化 patch 表征与精化 CLS token 构成全局图像表示 `z_img|| = [z_img; ẑ_cls] ∈ R^{2D}`。
  - 文本侧将 `ẑ_text` 复制为 `z_text|| ∈ R^{2D}`，计算余弦相似度矩阵，采用 **CLIP 风格对称对比损失**（双向交叉熵，温度 τ=0.07）。

- **推理流程**：对候选类别提取 CLIP 文本嵌入 → 经 STF 前向积分得到语义锚点 → 与 DINO patch token 计算余弦相似度 → 生成稠密分割图。

## 3. 实验设计

- **数据集（8 个 OVSS benchmark）**：
  - 含背景类：Pascal VOC 2012 (V21)、Pascal Context (C60)、COCO Object。
  - 不含背景类：COCO Stuff、Cityscapes、ADE20K、Pascal VOC 2012 (V20)、Pascal Context (C59)。
- **评估协议**：输入图像短边缩放到 448，滑动窗口 448×448、步长 224；文本嵌入用标准模板平均（如 "a photo of a {class}"）；主指标为 **mIoU**。
- **对比方法**：
  - 免训练方法：MaskCLIP、SCLIP、ClearCLIP、NACLIP、FreeDA、ProxyCLIP、CLIPer。
  - 弱监督方法：GroupViT、TCL、dino.txt、Talk2DINO。
  - 特别设置 **Talk2DINO\***：使用官方 checkpoint 替换为 DINOv3 骨干，并穷举搜索最优背景阈值，确保公平对比。
- **消融与诊断实验**：
  - 组件分析（STF / VTP / GCF 的独立与组合贡献）。
  - ODE 步数消融（N_step = 5 / 10 / 50）。
  - 骨干泛化（DINOv3 ViT-L/B/S × CLIP ViT-L/B）。
  - 几何诊断（邻域保持、测地一致性、类结构保持、对齐空间紧致度）。
  - STF 逐步演化分析（定量 mIoU 曲线 + Cityscapes 定性结果）。

## 4. 资源与算力

- **骨干模型**：DINOv3 ViT-L/16（视觉）+ CLIP ViT-L/14（文本），二者均冻结。
- **训练数据**：仅使用 COCO 2017 Caption 训练集（约 **118k** 图像），远少于 CC3M（~3.3M）或 CC12M（~12.4M）。
- **硬件与时长**：**单张 NVIDIA RTX 3090**，batch size 256，训练 20 个 epoch，学习率 1×10⁻⁴，权重衰减 0.01；**含缓存阶段总训练时间约 4 小时**。
- **效率说明**：由于骨干冻结，可预缓存嵌入；对齐后的文本锚点按类别集缓存一次，推理阶段进一步节省算力。

## 5. 实验数量与充分性

- **实验规模**：覆盖 8 个数据集、约 6 大类实验（组件消融、步数消融、骨干泛化、几何诊断、SOTA 对比、演化过程分析），另含定性对比。
- **充分性**：
  - 组件消融逐项验证 STF、VTP、GCF 的独立贡献，逻辑清晰。
  - 骨干泛化覆盖视觉 ViT-S/B/L 与文本 ViT-B/L，验证方法不依赖特定骨干。
  - 几何诊断用 4 项定量指标直接验证"流形保持"这一核心动机，而非仅看最终精度。
- **客观与公平性**：
  - 对 Talk2DINO 使用相同 DINOv3 骨干重跑（Talk2DINO\*），并穷举背景阈值，比较基准较为公平。
  - 同时报告"含/不含 mask refinement"两组结果，避免后处理带来的不公平增益。
  - 局限：所有实验仅在 COCO Caption 上训练，未验证其他训练集或更大规模数据下的表现；对比方法的超参调优细节披露有限。

## 6. 主要结论与发现

- DINOde 在 **8 个 benchmark 中的 6 个**取得最优，未加 mask refinement 时平均 mIoU 达 **49.5%**，加入后达 **50.1%**。
- 相比同骨干的 Talk2DINO\*，未加 mask refinement 时平均提升 **1.9%p**（47.6 → 49.5）。
- ODE 连续对齐**一致优于** MLP 离散投影：步数越多性能先快速上升（1→8 步），8→10 步趋于收敛，过多步数会因数值积分误差累积而轻微"过冲"。
- VTP 与 GCF 均带来稳定增益，二者互补：VTP 保持超球几何稳定性，GCF 引入全局上下文避免文本流偏向局部视觉特征。
- 几何诊断显示 STF 在邻域保持、测地一致性、类结构保持、对齐空间紧致度四项指标上均优于 MLP 基线。
- 论文展望：现代 MLLM 用单层 MLP 投影冻结视觉特征，与本工作的离散基线类似，连续 ODE 对齐有望提升 MLLM 的细粒度视觉 grounding。

## 7. 优点

- **方法新颖且动机扎实**：将跨模态对齐建模为流形上的连续流，切中 MLP 单步投影破坏几何结构这一根本问题。
- **几何约束设计精巧**：VTP 通过切空间投影严格保证演化过程停留在超球面上，兼具理论优雅性与实际增益。
- **双流互补**：STF 处理文本→视觉，GCF 精化全局 CLS，局部与全局语义协同。
- **极高的数据与算力效率**：仅 118k 图文对、单卡 3090、4 小时即可完成训练，远低于同类弱监督方法，实用性强。
- **验证维度全面**：不仅有精度对比，还提供几何诊断、步数演化曲线、定性分割图，形成"动机—机制—结果"的完整证据链。
- **公平对比意识**：为 SOTA 基线统一骨干并调优背景阈值，同时给出含/不含后处理两组结果。

## 8. 不足与局限

- **训练数据覆盖有限**：仅在 COCO Caption（118k）上训练，未验证更大规模或领域特定图文对（如 CC3M/CC12M）下的扩展性。
- **推理需数值积分**：需多步欧拉迭代（N_step=10），相比单次 MLP 前向略增推理开销；步数过多还会导致误差累积与性能过冲。
- **部分 benchmark 非最优**：在 Stuff、City 等数据集上并非全部领先（如无 mask refinement 时 Stuff 31.6 低于 Talk2DINO\* 的 32.6），方法在不同场景下的稳健性仍有提升空间。
- **背景类处理依赖阈值搜索**：含背景类数据集需穷举最优背景阈值，实际部署中可能需额外调参。
- **应用边界**：论文仅停留在 OVSS 任务，向 MLLM 等其他多模态场景的迁移只是作为未来工作提出，尚未验证。
- **潜在偏差风险**：评估沿用既有 OVSS 协议与提示模板，性能可能受模板选择影响；弱监督对比方法的重训细节披露有限，公平性虽经努力但仍可能存在隐含差异。

（完）
