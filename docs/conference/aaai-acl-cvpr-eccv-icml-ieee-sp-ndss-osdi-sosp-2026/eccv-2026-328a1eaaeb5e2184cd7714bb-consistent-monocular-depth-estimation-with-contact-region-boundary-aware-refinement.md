---
title: Consistent Monocular Depth Estimation with Contact Region Boundary-Aware Refinement
title_zh: 具有接触区域边界感知细化的单目深度估计
authors: "Yinuo Wang, QingMiao QingMiao, Wangmeng Zuo"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6965.pdf"
tags: ["query:mono-depth"]
score: 6.0
evidence: 带接触区域边界感知细化的单目深度估计
tldr: 现有单目深度估计虽整体精度较高，却在物体与支撑面等接触区域产生错误的深度不连续。作者提出边界感知的单目深度估计框架，利用接触边界作为显式结构先验，设计边界检测与过滤模块识别接触区域，实现接触处的深度一致性学习。该工作改善边界处的深度质量，对边界敏感的深度应用具有参考意义。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 1247, \"height\": 944}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-010.webp\", \"caption\": \"\", \"page\": 13, \"index\": 10, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-011.webp\", \"caption\": \"\", \"page\": 13, \"index\": 11, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-012.webp\", \"caption\": \"\", \"page\": 13, \"index\": 12, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-013.webp\", \"caption\": \"\", \"page\": 13, \"index\": 13, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-014.webp\", \"caption\": \"\", \"page\": 13, \"index\": 14, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-015.webp\", \"caption\": \"\", \"page\": 13, \"index\": 15, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-016.webp\", \"caption\": \"\", \"page\": 13, \"index\": 16, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-017.webp\", \"caption\": \"\", \"page\": 13, \"index\": 17, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-018.webp\", \"caption\": \"\", \"page\": 13, \"index\": 18, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-019.webp\", \"caption\": \"\", \"page\": 13, \"index\": 19, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-020.webp\", \"caption\": \"\", \"page\": 13, \"index\": 20, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-021.webp\", \"caption\": \"\", \"page\": 13, \"index\": 21, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-022.webp\", \"caption\": \"\", \"page\": 13, \"index\": 22, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-023.webp\", \"caption\": \"\", \"page\": 13, \"index\": 23, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-024.webp\", \"caption\": \"\", \"page\": 13, \"index\": 24, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-025.webp\", \"caption\": \"\", \"page\": 13, \"index\": 25, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-026.webp\", \"caption\": \"\", \"page\": 13, \"index\": 26, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-027.webp\", \"caption\": \"\", \"page\": 13, \"index\": 27, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-028.webp\", \"caption\": \"\", \"page\": 13, \"index\": 28, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-029.webp\", \"caption\": \"\", \"page\": 13, \"index\": 29, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-030.webp\", \"caption\": \"\", \"page\": 13, \"index\": 30, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-031.webp\", \"caption\": \"\", \"page\": 13, \"index\": 31, \"width\": 1300, \"height\": 859}]"
motivation: 单目深度估计在物体接触区域产生错误深度不连续。
method: 提出边界感知框架，用接触边界先验与边界检测过滤模块约束。
result: 实现接触区域的深度一致性学习，改善边界深度质量。
conclusion: 为边界敏感的深度估计提供了结构先验思路。
---

## Abstract
While contemporary monocular depth estimation (MDE)methods achieve remarkable overall acacy, they consistently produce er-roneous depth discontinuities at object contact regions, particularly be-tween objects and supporting surfaces. In this paper, we address this crit-ical limitation by presenting a boundary-aware monocular depth estima-tion framework that enforces depth continuity at contact areas throughthe principled exploitation of contact boundaries as explicit structuralpriors. Specifically, we propose a boundary detection and filtering modulethat explicitly identifies object contact regions, yielding a novel boundary-aware representation that enables depth-consistent learning at contactareas. Furthermore, we introduce a boundary-aware feature fusion strat-egy that seamlessly incorporates contact boundary priors into the depthdecoding process, effectively rectifying the persistent discontinuities thatelude existing approaches. Our framework further supports interactiverefinement, allowing users to manually specify missing contact bound-aries for controllable depth correction. Extensive experiments on threeunseen benchmarks with dense object interactions demonstrate the ef-fectiveness of our approach, consistently outperforming baselines withparticularly pronounced gains in contact regions. Code is available athttps://github.com/abai969/contact-depth-refinement.git

---

## 论文详细总结（自动生成）

# 论文总结：Consistent Monocular Depth Estimation with Contact Region Boundary-Aware Refinement

## 1. 核心问题与整体含义
- **研究动机**：单目深度估计（MDE）虽整体精度不断提升，但在物体接触区域，尤其是物体与支撑面之间，常产生错误的深度不连续。像素级监督忽略像素间几何依赖；基于 3D 点云表示的方法虽增强几何一致性，仍在细粒度接触处出现断裂。
- **核心问题**：现有方法缺少对“物体接触结构”的显式建模，不知道哪些物理相邻表面应保持深度连续，因此会在接触边界处产生虚假深度跳变。
- **整体含义**：论文将接触边界作为显式结构先验引入深度解码，目标是提升接触区域的深度连续性与局部 3D 几何一致性，并支持用户交互式指定缺失接触边界以进行可控深度校正。

## 2. 方法论
### 2.1 核心思想
- 在 MoGe（affine-invariant 单目几何估计器）基础上，先检测并过滤物体接触边界，再将接触边界先验融合进深度解码器，并在训练中施加接触区域深度一致性约束。
- 整体流程：输入 RGB → 边缘检测 → 接触边界过滤 → 边界编码与多尺度融合 → 边界感知深度解码 → 接触区域深度监督。

### 2.2 关键技术细节
- **边缘检测模块**：采用 MuGE 多粒度边缘检测器，参数 \(a=0.5\)，从输入图像得到稠密边缘图 \(E\)，同时覆盖物体间边界与物体内部结构边界。
- **接触边界过滤模块**：
  - 使用预训练 SigLIP 视觉编码器提取语义增强特征 \(S\)。
  - 对边缘像素 \(q_i=(x_i,r_i)\)，沿局部法向两侧采样特征 \(s_i^+\)、\(s_i^-\)，计算跨边界差异 \(\Delta s_i=s_i^+-s_i^-\)。
  - 拼接特征 \(t_i=\psi(s_i,s_i^+,s_i^-,\Delta s_i)\)，输入轻量 MLP 分类器预测接触概率，形成接触边界图 \(\hat{B}\)。
  - 训练损失为加权 BCE 损失 \(L_{bce}\) 与边缘方差正则 \(L_e\) 之和：\(L_F=L_{bce}+\lambda_e L_e\)，其中 \(\lambda_e=100\)。
- **边界感知特征融合**：
  - 用 ResNet 编码器将 \(\hat{B}\) 编码为边界特征 \(C\)。
  - 将 \(C\) 与图像特征 \(F\) 多尺度融合为 \(\tilde{F}\)，再由深度解码器生成边界感知的 affine-invariant 点云 \(\hat{P}'\)。
- **边界感知深度监督**：
  - 在接触边界像素集合 \(M_b\) 上施加深度对齐损失 \(L_{bd}\)。
  - 引入一阶梯度一致性损失 \(L_{grad}\) 与法向平滑损失 \(L_m\)，约束接触区域深度梯度与平滑性。
  - 引入辅助一致性损失 \(L_{cons}\)：当边界图置零时，辅助预测应与冻结 MoGe 输出一致，防止边界不可靠时解码器偏离原预测。
  - 边界损失：\(L_B=\lambda_b L_{bd}+\lambda_g L_{grad}+\lambda_m L_m+\lambda_{aux}L_{cons}\)，权重为 0.4、0.3、0.3、500。
- **总损失**：\(L_{total}=L_{MoGe}+L_F+L_B\)，其中 \(L_{MoGe}\) 包含全局对齐、局部多尺度对齐、法向与有效区域损失。

### 2.3 算法流程简述
1. 输入图像，DINOv2 提取视觉特征 \(F\)，MuGE 提取边缘图 \(E\)。
2. SigLIP 提取语义特征，结合边缘点法向采样，MLP 预测接触概率，得到 \(\hat{B}\)。
3. ResNet 编码 \(\hat{B}\)，与 \(F\) 融合后送入深度解码器，得到边界感知点云。
4. 在接触边界区域施加深度、梯度、平滑与辅助一致性损失，联合优化
