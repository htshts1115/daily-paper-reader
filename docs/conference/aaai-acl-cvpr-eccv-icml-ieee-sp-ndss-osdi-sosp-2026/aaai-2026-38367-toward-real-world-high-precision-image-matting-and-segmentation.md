---
title: Toward Real-World High-Precision Image Matting and Segmentation
title_zh: 面向真实世界的高精度图像抠图与分割
authors: "Haipeng Zhou, Zhaohu Xing, Hongqiu Wang, Jun Ma, Ping Li, Lei Zhu"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/38367/42329"
tags: ["query:matting"]
score: 9.0
evidence: 面向发丝等精细细节的高精度图像抠图与分割
tldr: 高精度场景解析（含图像抠图与二值分割）需要预测发丝等极细细节掩码，但现有方法多针对显著单目标，交互式方法类别无关泛化差，且依赖不协调的合成数据导致真实场景泛化不佳。本文提出前景一致性学习模型FCLM，通过深度感知蒸馏迁移深度知识并结合前景一致性约束。该设计在真实场景中提升细节保留与泛化能力，直接服务于人像抠图与前景完整性需求。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38367/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 868, \"height\": 349}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38367/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 796, \"height\": 530}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38367/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 879, \"height\": 255}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38367/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 872, \"height\": 528}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38367/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1676, \"height\": 1066}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-38367/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 727, \"height\": 324}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38367/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 773, \"height\": 283}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38367/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1830, \"height\": 370}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38367/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 854, \"height\": 322}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38367/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 854, \"height\": 231}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38367/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1830, \"height\": 771}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-38367/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 855, \"height\": 201}]"
motivation: 高精度抠图与分割需保留发丝等细节，但现有方法依赖合成数据且真实场景泛化差。
method: 提出前景一致性学习模型FCLM，采用深度感知蒸馏迁移深度知识并强化前景一致性。
result: 实验表明该方法在真实场景中更好地保留精细细节并提升跨类别泛化能力。
conclusion: 该工作为真实世界高精度抠图与分割提供了有效方案，契合人像抠图需求。
---

## Abstract
High-precision scene parsing tasks, including image matting and dichotomous segmentation, aim to accurately predict masks with extremely fine details (such as hair). Most existing methods focus on salient, single foreground objects. While interactive methods allow for target adjustment, their class-agnostic design restricts generalization across different categories. Furthermore, the scarcity of high-quality annotation has led to a reliance on inharmonious synthetic data, resulting in poor generalization to real-world scenarios. To this end, we propose a Foreground Consistent Learning model, dubbed as FCLM, to address the aforementioned issues. Specifically, we first introduce a Depth-Aware Distillation strategy where we transfer the depth-related knowledge for better foreground representation. Considering the data dilemma, we term the processing of synthetic data as domain adaptation problem where we propose a domain-invariant learning strategy to focus on foreground learning. To support interactive prediction, we contribute an Object-Oriented Decoder that can receive both visual and language prompts to predict the referring target. Experimental results show that our method quantitatively and qualitatively outperforms state-of-the-art methods.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机和背景）

- **任务定位**：论文面向高精度场景解析，包括**图像抠图（image matting）**与**二分图像分割（dichotomous segmentation）**，目标是预测具有极细细节（如发丝、绳索纤维等）的精细掩码，服务于 AR/VR、图像编辑等应用。
- **核心痛点**：
  - 多数现有方法聚焦**显著、单一前景目标**，对多实例、开放类别场景泛化差。
  - 交互式方法虽可调整目标，但通常**类别无关（class-agnostic）**，难以区分语义目标。
  - 高质量真实标注稀缺，导致大量方法依赖**不协调合成数据**（前景与背景拼接不自然），产生明显域差距。
  - 多阶段方法（如 Ground-DINO + SAM + refinement）流程复杂，且存在误差传播问题。
- **动机验证**：表 1 显示，P3M-Net、MatteFormer、MODNet 等在合成数据上训练后，在真实 P3M-500-P 测试集上性能显著下降，说明不协调合成数据会损害真实场景泛化。
- **整体含义**：论文将“不协调合成数据”的处理形式化为**域适应问题**，提出前景一致性学习模型 **FCLM**，试图在真实世界高精度抠图与分割中兼顾细节、泛化与交互性。

## 2. 方法论：核心思想与关键技术

- **总体框架**：FCLM 训练时输入一对共享同一前景的图像 A（合成/替换背景）与 B（真实或合成），学习跨背景一致的前景表示；推理时仅使用学生模型与解码器。
- **Depth-Aware Distillation（DAD）**：
  - 教师模型为 **Depth-Anything V2 Large**，学生模型为 **DINOV2**（分割用 Base，抠图用 Small）。
  - 不直接对齐输出深度，而是在**特征层**蒸馏，避免额外学生深度头。
  - 使用教师生成的深度图，经阈值 δ=0.25 得到前景权重 d+ 与背景权重 d−。
  - 引入 meta-net τ 与 context token ε，将教师特征投影为前景/背景表示。
  - 蒸馏损失可概括为：对 A、B 两图，分别用 d+、d− 加权对齐学生特征与教师投影特征；最终用 KL 散度衡量。
- **Foreground Consistent Domain Adaptation（FCDA）**：
  - 将 A、B 视为不同域，使用域判别器 h(·) 与梯度反转层（GRL）进行对抗学习，促使学生编码器产生域不变特征。
  - 引入 **token exchange**：在相同索引处随机交换 A、B 的视觉 token，比例 25%，以增强前景一致性并抑制背景域偏差。
  - 用真实掩码 M 过滤前景 token，得到两组前景特征分布。
  - 使用 **Optimal Transport（OT）损失** 对齐前景分布，成本矩阵采用余弦不相似度，并用 Sinkhorn-nopp 求解。
  - 背景不做 OT 对齐，作者认为背景对最终预测贡献有限。
- **Object-Oriented Decoder**：
  - 支持视觉 prompt（box、point、scribble）与文本 prompt。
  - 视觉 prompt 通过坐标位置编码得到稀疏嵌入；无 prompt 时初始化为零。
