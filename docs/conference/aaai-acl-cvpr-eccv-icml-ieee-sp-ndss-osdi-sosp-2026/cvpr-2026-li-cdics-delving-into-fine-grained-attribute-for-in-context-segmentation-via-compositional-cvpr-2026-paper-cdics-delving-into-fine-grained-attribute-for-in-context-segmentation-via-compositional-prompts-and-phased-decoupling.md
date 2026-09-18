---
title: "CDICS: Delving Into Fine-Grained Attribute for In-Context Segmentation via Compositional Prompts and Phased Decoupling"
title_zh: CDICS：通过组合提示与分阶段解耦深入细粒度属性的上下文分割
authors: "Li, Zhiyu, Sheng, Dianmo, Chu, Qi, Chen, Shilong, Gong, Tao, Wei, Zhou, Yu, Nenghai"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Li_CDICS_Delving_Into_Fine-Grained_Attribute_for_In-Context_Segmentation_via_Compositional_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 6.0
evidence: 组合提示的通用图像分割
tldr: 上下文学习已成为构建通用图像分割模型的有效手段，但现有方法难以针对稀有复杂概念找到完全匹配的参考样本，且多局限于语义或实例级理解。作者提出CDICS框架，通过组合提示与分阶段任务解耦，让用户以更精细的方式控制分割目标。实验显示该方法能表达更精确的分割需求并提升细粒度属性分割效果。该工作为通用分割模型的可控性提供了新思路。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 6, \"index\": 1, \"width\": 573, \"height\": 285}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 573, \"height\": 286}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 873, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 905, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 872, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 574, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 905, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 873, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 6, \"index\": 9, \"width\": 573, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 906, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 906, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 873, \"height\": 291}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 575, \"height\": 291}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-cdics-delving-into-fine-grained-attribute-for-in-context-segmentation-via-compositional-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 905, \"height\": 289}]"
motivation: 通用分割模型依赖单张参考图，难以为稀有复杂概念找到匹配样本，也难表达精细需求。
method: 提出CDICS框架，利用组合提示与分阶段任务解耦实现组合提示控制的分割。
result: 在上下文分割上支持更精确的语义与实例级需求，缓解单样本匹配困难。
conclusion: 为上下文分割提供了可组合、可分阶段的通用分割新范式。
---

## Abstract
In-Context Learning (ICL) has shown great effectiveness in developing generalist image segmentation models. Its significant advantage over text-based descriptions is the ability to convey intricate visual appearance details through simple reference images. However, finding a perfectly matching single example for real-world rare and complex concepts is difficult. Moreover, existing methods are largely confined to semantic or instance-level understanding of the reference image, struggling to express more precise segmentation needs through the input. To address this, we propose CDICS, a novel framework that leverages Compositional prompts and phased task Decoupling to achieve compositional prompt-controlled In-Context Segmentation. Our method introduces compositional prompts derived from reference prompts, combining semantic, part and color images to dynamically define segmentation targets. To effectively fuse this control information, ensure synergy while suppressing interference, and mitigate feature coupling risks, our decoupled two-stage architecture firstly performs coarse-grained semantic localization, then refines the result using compositional appearance prompts to precisely match the specified attributes. This design extends traditional in-context segmentation, enabling it to support compositional prompts. Additionally, we reconstructed two datasets and their benchmarks to acquire data with part-color-specific attributes. Our method demonstrates superior performance on the compositional prompt-controlled in-context segmentation task. It also extends the capabilities of existing in-context segmentation, and makes an attempt toward real-world fine-grained segmentation.

---

## 论文详细总结（自动生成）

# CDICS 论文详细中文总结

## 1. 核心问题与研究动机

- **背景**：In-Context Learning（ICL）已成为构建通用图像分割模型的重要范式，其相较文本描述的优势在于能通过简单的参考图像传递复杂的视觉外观细节。
- **核心痛点**：
  - 现实世界中罕见、复杂概念很难找到"完美匹配"的单张参考图；
  - 现有方法大多局限于对参考图的**语义级或实例级**理解，难以表达更精细的分割需求（如"佩戴特定款式和颜色项链的人"）；
  - 用户需求多样：有时需要粗粒度语义分割，有时需要带精确外观条件的细粒度分割；
  - 纯文本描述颜色存在词汇有限、离散、歧义等问题（如电商产品匹配、工业质检场景）。
- **整体含义**：论文提出 **CDICS** 框架，首次尝试将**物体语义、部件形态、颜色属性**统一到分割流程中，实现组合提示（Compositional Prompts）控制下的细粒度、可控上下文分割，是对传统 in-context segmentation 范式的扩展。

## 2. 方法论

### 2.1 核心思想
- 将复杂的"语义-部件-颜色"组合分割任务**正交分解**为两个独立子问题：
  - **Stage 1：粗粒度语义定位**——回答"目标是什么？"；
  - **Stage 2：外观约束精炼**——回答"这个特定目标长什么样？"。
- 通过分阶段解耦避免不同约束之间的**特征耦合**问题，使模型能更专注于细粒度外观特征的学习与应用。

### 2.2 输入形式
- 目标图像 `I_tar`；
- 组合提示：语义参考 `(I_sem, M_sem)`、部件参考 `(I_part, M_part)`、颜色参考 `I_col`。

### 2.3 编码器阶段
- 使用 **DINOv2** 作为骨干网络提取特征；
- 通过 **Mask Pooling** 提取语义原型 `F_sem` 和部件原型 `F_part`，目标图像编码为 `F_tar`；
- **颜色融合模块（Color Fusion Module）**：
  - 将目标图像与参考颜色转换到 **CIELAB** 色彩空间；
  - 计算 **CIEDE2000 色差** `ΔE_00`，转化为相似度图：`M_sim = 1 − Norm(ΔE_00(I_tar, I_col))`；
  - 通过 **FiLM 层**生成通道级仿射参数 `γ, β`，调制目标特征：`F_tar_col = F_tar · (1 + γ) + β`。

### 2.4 Stage 1 解码器（粗粒度语义定位）
- 仅使用语义原型 `F_sem`，忽略部件与颜色细节；
- 采用 Transformer 解码器，可学习实例查询 `Q_ins` 与图像特征交互；
- 输出一组粗略实例掩码及语义标签，为第二阶段奠定基础。

### 2.5 Stage 2 解码器（外观约束精炼）
- **特征图加权**：将 Stage 1 的实例分数合并为语义区域分数图 `Score_sem`，加权得到 `F_tar^S2 = (Score_sem + 1) · F_tar^S1`，抑制背景噪声；
- **外观融合模块（Appearance Fusion）**：
  - 计算部件原型与颜色增强特征的余弦相似度，生成部件注意力图 `F_tar^cp`：`F_tar^cp = (sim(F_part, F_tar_col) + 1) · F_tar_col`；
  - 用 `F_tar^cp` 反向增强部件原型，得到"外观感知"的部件特征 `F_cp`；
  - 将 `F_cp` 与语义原型 `F_sem^S1` 融合生成组合原型 `F_scp`，再与原始语义特征拼接为最终组合特征 `F_sem^S2 ∈ R^{2×C}`。

### 2.6 细粒度分类与分割
- 最终分类将实例特征与统一拼接特征 `F_sem^S2` 比较，解决同类实例间的属性级区分；
- 损失函数：每个阶段均采用**匈牙利算法**进行预测-真值一对一匹配；
- 单阶段损失 `L_H^i` 包含分类项（负对数似然）与掩码项（BCE + Dice）；
- 总损失为两阶段之和：`L_total = Σ_{i=1}^{2} L_H^i`。

## 3. 实验设计

### 3.1 数据集
- **ColorPACO**：基于 PACO 重建，对每个部件实例标注精确 RGB 值（而非离散颜色标签），含 75 个物体、456 个物体-部件类别；
- **ColorPartImageNet**：基于 PartImageNet 重建，含 158 个类别，用于评估**域外泛化能力**；
- **COCO-Ins**：实例分割标注，用于训练增强基础实例识别能力；
- **COCO-20^i**：小样本分割（FSS）基准，用于与传统方法公平对比。
- **正负样本设计**：正样本（物体、部件、颜色均匹配）与负样本（类别存在但属性不匹配，GT 掩码全零）独立采样，比例约 3:1。

### 3.2 评价指标
- 分割精度：**IoU**、**AP**、**AP_50**；
- 指令判别能力：**FPR（False Positive Rate）**，衡量模型拒绝无效指令的能力。

### 3.3 对比方法
- **In-context segmentation**：SegGPT、Matcher、SINE、LDIS；
- **Referring segmentation**：OMG-LLaVA、PSALM、HyperSeg、DETRIS；
- **组合基线**：SINE + OIParts（后处理方式组合语义分割与部件分割并做颜色过滤）。

### 3.4 训练设置
- 基于 **SINE 架构**并加载其预训练权重；
- 在 ColorPACO 与 COCO-Ins 上以 1:1 采样比例联合训练；
- 评测在 ColorPartImageNet（域外）与 COCO-20^i（标准 FSS）上进行。

## 4. 资源与算力

- 论文明确说明：使用 **8 张 NVIDIA A6000 GPU**，**batch size 为 160**，训练 **60 个 epoch**；
- 优化器为 **AdamW**，初始学习率 **1×10^{-4}**；
- 未明确提及单次训练总时长、总 GPU 时数或推理阶段的计算开销；
- 致谢中提到使用了中国科学技术大学超级计算中心的先进计算资源。

## 5. 实验数量与充分性

- **主要对比实验**：在 3 个数据集（COCO-20^i、ColorPACO、ColorPartImageNet）上与 8 种以上方法（in-context + referring + 组合基线）对比；
- **实例分割对比**：在 ColorPACO 上对比 HyperSeg、PSALM、SINE 的 AP/AP_50；
- **消融实验**：3 组配置（Baseline / +Appearance Fusion / +Two Stage）在 ColorPACO 上进行；
- **可视化结果**：展示了组合提示（semantic-part-color 与 semantic-part）下的预测与 GT 对比。
- **充分性与客观性评价**：
  - 优点：对比方法覆盖两大主流范式，均使用官方代码与预训练权重，负样本独立采样以避免偏置，评价指标同时关注精度与指令判别能力；
  - 局限：消融实验仅在单一数据集（ColorPACO）上进行，未在 ColorPartImageNet 上做消融；未报告多次运行的方差或统计显著性；部分对比方法（如 referring segmentation 系列）在组合任务上可能存在领域不匹配，公平性存在一定讨论空间。

## 6. 主要结论与发现

- **ColorPACO 上**：CDICS 达到 **IoU 57.6%、FPR 3.9%**，相较最强 referring 方法 HyperSeg（IoU 42.9%、FPR 8.3%）IoU 提升 **14.7 个百分点**，FPR 降低超过一半；
- **ColorPartImageNet 上**：IoU **84.4%**、FPR **12.5%**；SegGPT 虽 IoU 最高（85.2%），但 FPR 高达 23.8%，存在"过度分割"倾向，CDICS 在精度与保真度之间取得更好平衡；
- **COCO-20^i 上**：IoU **65.2%**，表明新增组合理解模块未损害基础上下文分割能力；
- **实例分割**：ColorPACO 上 AP **20.8%**、AP_50 **34.9%**，显著超越对比方法；
- **消融结论**：Appearance Fusion 模块和 Two-Stage 策略均带来一致提升（IoU 从 50.3% → 51.4% → 58.9%，FPR 从 12.0% → 9.3% → 5.7%，AP_50 从 27.7% → 30.8% → 42.4%）。

## 7. 优点

- **方法创新**：
  - 首次将语义、部件、颜色三种视觉提示统一为组合提示用于 in-context segmentation；
  - 提出"粗语义 → 细外观"的两阶段解耦架构，有效缓解特征耦合；
  - 设计统一的 Appearance Fusion 模块，实现部件与颜色的协同融合并抑制干扰；
  - 采用 CIELAB + CIEDE2000 将颜色相似度转化为可量化的强度图，规避了语言颜色词汇的离散与歧义问题。
- **数据贡献**：重建了 ColorPACO 与 ColorPartImageNet 两个带部件-颜色细粒度标注的数据集，并设计正负样本划分与 FPR 指标；
- **实验设计**：同时覆盖组合细粒度分割与传统 FSS/实例分割任务，验证了方法的泛化性与基础能力保持；
- **实用价值**：面向电商产品匹配、工业质检等真实场景中颜色描述的模糊性问题，提供更用户友好、跨语言一致的颜色表示方式。

## 8. 不足与局限

- **颜色融合机制**：依赖手工设计的 CIELAB/CIEDE2000 色差函数，对光照、材质、透明等复杂外观的鲁棒性未充分讨论；相似度图归一化方式较简单；
- **架构依赖**：基于 SINE 架构构建并初始化其预训练权重，方法增益可能在部分程度上受限于骨干模型能力，未验证在其他骨干（如 SAM、Matcher）上的通用性；
- **属性维度有限**：仅覆盖"部件 + 颜色"两类细粒度属性，未涉及纹理、材质、形状、尺寸等其他外观维度；
- **实验覆盖**：
  - 消融实验仅在 ColorPACO 上进行，未在其他数据集验证；
  - 未报告推理速度、参数量、显存占用等效率指标；
  - 未报告多次运行的均值/方差，缺乏统计显著性分析；
- **数据集构建**：ColorPACO 与 ColorPartImageNet 均为作者自行重建，标注质量、标注一致性及潜在标注偏差未做详细量化分析；
- **对比公平性**：Referring segmentation 方法原本面向文本输入，迁移至组合视觉提示任务时可能存在领域不匹配，部分对比可能不完全公平；
- **应用限制**：两阶段解码结构在推理时增加延迟，对实时性要求高的场景可能不友好；负样本 FPR 虽降低但仍存在（ColorPartImageNet 上为 12.5%），在安全敏感场景中仍可能产生误激活。

（完）
