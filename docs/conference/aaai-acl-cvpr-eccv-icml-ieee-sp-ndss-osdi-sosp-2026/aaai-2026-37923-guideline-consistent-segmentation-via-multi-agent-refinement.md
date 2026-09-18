---
title: Guideline-Consistent Segmentation via Multi-Agent Refinement
title_zh: 基于多智能体精炼的准则一致分割
authors: "Vanshika Vats, Ashwani Rathee, James Davis"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37923/41885"
tags: ["query:seg"]
score: 6.0
evidence: 基于文本准则的免训练开放词汇分割
tldr: 现有开放词汇分割方法在面对长段落式标注准则时难以忠实遵循，且传统方案需反复重训练。本文提出免训练的多智能体Worker-Supervisor迭代精炼框架，协调通用视觉语言模型执行分割。实验表明该方法在复杂准则下显著提升标注一致性与分割准确度，为开放词汇语义分割提供新范式。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37923/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 2208, \"height\": 1116}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37923/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 2921, \"height\": 1815}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37923/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 5908, \"height\": 1780}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37923/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 4309, \"height\": 3448}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37923/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 5278, \"height\": 3333}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37923/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 2149, \"height\": 1731}]"
motivation: 真实场景语义分割不仅要求掩码准确，还须严格遵循冗长复杂的文本标注准则，传统方法依赖昂贵且需随准则更新的重训练。
method: 提出免训练的多智能体框架，在Worker-Supervisor迭代精炼架构中协调通用视觉语言模型完成分割。
result: 实验显示该方法在段落级复杂准则下比现有开放词汇分割方法更忠实地遵循规则并提升掩码准确度。
conclusion: 该工作为准则约束下的开放词汇语义分割提供了无需重训练的通用解决思路。
---

## Abstract
Semantic segmentation in real-world applications often requires not only accurate masks but also strict adherence to textual labeling guidelines. These guidelines are typically complex and long, and both human and automated labeling often fail to follow them faithfully. Traditional approaches depend on expensive task-specific retraining that must be repeated as the guidelines evolve. Although recent open-vocabulary segmentation methods excel with simple prompts, they often fail when confronted with sets of paragraph-length guidelines that specify intricate segmentation rules. To address this, we introduce a multi-agent, training-free framework that coordinates general-purpose vision-language models within an iterative Worker-Supervisor refinement architecture. The Worker performs the segmentation, the Supervisor critiques it against the retrieved guidelines, and a lightweight reinforcement learning stop policy decides when to terminate the loop, ensuring guideline-consistent masks while balancing resource use. Evaluated on the Waymo and ReasonSeg datasets, our method notably outperforms state-of-the-art baselines, demonstrating strong generalization and instruction adherence.

---

## 论文详细总结（自动生成）

# 论文总结：Guideline-Consistent Segmentation via Multi-Agent Refinement

## 1. 核心问题与整体含义
- **研究动机**：真实场景中的语义分割不仅要求像素级准确，还要求严格遵循文本标注准则。这些准则通常冗长、复杂，例如 Waymo 中行人类别需“包含滑板骑行者、排除人体模型”等。
- **现有问题**：
  - 传统监督分割依赖固定类别，面对新类别或准则演化时需昂贵重标注与重训练。
  - 开放词汇分割方法擅长短提示，但在段落级、规则密集的准则下容易失败。
  - 人工标注的“真值”本身也可能违反准则，如图 2 所示 Waymo 同一场景不同时间戳标注不一致。
- **整体含义**：论文提出一种**免训练、多智能体、迭代精炼**的准则一致语义分割框架，使通用视觉语言模型能够遵循长而复杂的文本准则，无需针对任务重新训练。

## 2. 方法论
- **核心思想**：在 Worker–Supervisor 迭代循环中协调通用 VLM 与冻结的 SAM，通过上下文检索、监督批评和强化学习停止策略，生成符合准则的分割掩码。
- **输入与准则结构化**：
  - 输入图像、提示词 P 和详细准则 G。
  - 使用 GPT-4o 将准则转为结构化 JSON，赋予唯一 ID：G = {G0, G1, …, Gm}。
- **上下文构建**：
  - 将准则编码存入 FAISS 向量数据库。
  - Enricher：用 Gemma3-4B 生成图像描述，构造查询 Q = {P, caption, H×W}。
  - Retriever：用 SentenceTransformer（all-MiniLM-L6-v2）编码查询，余弦检索 top-k=8 条最相关准则，避免无关规则干扰。
- **Smart Crop**：
  - 将图像缩放至 0.8×，用 OWLv2 获得粗框。
  - 根据目标分布与空间布局做垂直切分，保持左右目标数量大致均衡，提升小/远目标检测。
- **Validation Module：Worker–Supervisor 循环**：
  - **Worker**：基于提示和上下文检测目标，输出边界框、类别、ID；用冻结 SAM2.1 生成掩码。
  - **Supervisor eval**：检查三类问题：漏检、误检、掩码精炼机会；输出结构化 JSON 批评与建议。
  - **Supervisor boxgen**：根据批评生成候选边界框。
  - **SigLIP Verifier**：对候选区域与标签做图文匹配，sigmoid 概率 ≥ 0.5 才接受。
  - **Worker 更新**：漏检则加框并分割；误检则用负点提示 SAM 擦除；精炼则调整框后重分割。
- **Adaptive Iteration Controller (AiRC)**：
  - 将停止决策建模为有限时域 MDP。
  - 问题计数：\(I_t = I_{miss} + I_{false} + 0.1 I_{ref}\)。
  - 状态：\(s = 2d + v\)，其中 \(d \in \{0,1,2\}\) 表示场景密度，\(v \in \{0,1\}\) 表示是否仍有违规。
  - 动作：STOP 或 CONTINUE。
  - 奖励：
    - CONTINUE 时：\(r = (I_t - I_{t+1}) - c + b[I_{t+1}=0]\)；
    - STOP 且 \(I_t=0\) 时：0；
    - STOP 且 \(I_t>0\) 时：\(-p\)。
  - 使用表格 Q-learning，若 \(Q(s, CONTINUE) > Q(s, STOP)\) 则继续，否则停止。
  - 实现中 MIN_ITERS=2，MAX_ITERS=4，平均约 2.6 次迭代。

## 3. 实验设计
- **数据集/场景**：
  - **Waymo Perception Dataset**：聚焦 Pedestrian 类，因边界微妙且易错。因原始真值常违反准则，作者人工筛选 101 个严格符合准则的样本，来自 55 个多样场景，覆盖晴天、雨天、夜晚。
  - **ReasonSeg val**：200 张真实场景图像，带像素级掩码和文本推理提示，用于测试泛化性。
- **Benchmark 与指标**：
  - 主要指标：gIOU、cIOU。
  - 辅助指标：mPr、mRec、mDice。
- **对比方法**：
  - LISA-7B、LISA-13B、GroundedSAM、READ、Gemini-2.5、SegZero。
  - ReasonSeg 还对比 SEEM、FaST、LISA-7B(ft)、LISA-13B-LLava-1.5(ft) 等。
- **Waymo 文本设置**：
  - S：单字主类名 “Pedestrian”。
  - C：精简短句准则。
  - F：完整长准则。
- **主要结果**：
  - Waymo 全准则下：gIOU 80.57、cIOU 86.70、mPr 91.06、mRec 84.78。
  - 相比最强短句全准则基线提升 +57.16 gIOU，相比 Gemini-2.5 基线提升 +11.55 gIOU，相比 SOTA 提升 +8.61 gIOU。
  - ReasonSeg：gIOU 68.1、cIOU 66.4，比最强基线 SegZero 提升 +5.5 gIOU。
- **消融实验**：
  - 比较 Worker-only、加入 Context、加入 Supervisor。
  - Waymo 上上下文与监督均提升；ReasonSeg 上上下文收益小，但监督精炼显著。
- **AiRC 分析**：
  - 动态停止比硬停在 2 次迭代平均多解决 0.61 vs 0.29 个违规，提升 110%，但仅对 48% crop 增加额外迭代。

## 4. 资源与算力
- **推理硬件**：单张 RTX3080 GPU，可灵活拆分到 3×GPU 以提高效率。
- **模型与 API**：
  - Worker 与 Supervisor 使用 Gemini-2.5-flash-preview-05-20 API。
  - 分割使用 SAM2.1 hiera large，冻结不微调。
  - 粗检测使用 OWLv2。
  - 图像描述使用 Gemma3-4B。
  - 文本嵌入使用 SentenceTransformer all-MiniLM-L6-v2。
  - 验证使用 SigLIP。
- **训练时长**：未明确提及，因为方法整体为**免训练**框架；仅 AiRC 的 Q 表在运行间持久化。
- **成本**：平均约 2.6 次迭代，约 $0.0088/样本（Gemini-2.5-flash）。

## 5. 实验数量与充分性
- **实验组数**：
  - 两个数据集：Waymo、ReasonSeg。
  - Waymo 下三种文本长度设置：单字、精简、完整准则。
  - 多个 SOTA 基线对比。
  - 消融实验：Worker、Context、Supervisor 组合。
  - AiRC 动态停止与硬停止对比。
  - 三次独立随机种子运行，报告均值与标准差。
- **充分性**：
  - 覆盖长准则、短提示、真实场景、不同天气与场景密度，较全面。
  - 三次随机种子缓解 VLM 非确定性。
  - 人工筛选 Waymo 子集以避免噪声真值误导，但也带来样本量小和选择偏差风险。
- **公平性**：
  - 在统一指标下与多种 SOTA 比较。
  - 但部分基线原本针对短提示，长准则下性能下降可能不完全代表其最佳适配能力。
  - 依赖专有 API，复现条件受外部模型版本影响。

## 6. 主要结论与发现
- 免训练多智能体迭代精炼可显著提升长准则下的分割一致性。
- 上下文检索能避免指令过载，使 VLM 只关注场景相关规则。
- Supervisor 反馈能有效恢复漏检、删除误检并精炼掩码。
- AiRC 能自适应分配计算资源，在困难场景多迭代，在简单场景早停。
- 在 Waymo 与 ReasonSeg 上均优于现有 SOTA，说明方法具有泛化性和指令遵循能力。
- 冻结 VLM 与 SAM 可避免数据集过拟合，保持通用性。

## 7. 优点
- **免训练**：无需任务特定重训练，准则变化时只需更新文本与检索库。
- **长准则处理能力强**：通过准则结构化、FAISS 检索和迭代监督，克服短提示方法的局限。
- **多智能体分工明确**：Worker 分割、Supervisor 批评与建议、SigLIP 验证，结构清晰。
- **RL 自适应停止**：用轻量 Q-learning 平衡精度与 API 成本，优于固定迭代次数。
- **工程细节扎实**：Smart Crop、SigLIP 验证、负点擦除、动态 thinking 模式等提升鲁棒性。
- **实验较客观
