---
title: Consistent Monocular Depth Estimation with Contact Region Boundary-Aware Refinement
title_zh: 具有接触区域边界感知细化的连贯单目深度估计
authors: "Yinuo Wang, QingMiao QingMiao, Wangmeng Zuo"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6965.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 边界感知的单目深度估计框架
tldr: 现有单目深度估计虽整体精度较高，但在物体与支撑面等接触区域常出现错误的深度不连续。本文提出边界感知的单目深度估计框架，通过显式检测并过滤接触边界作为结构先验，构建边界感知表示以实现接触区域深度一致学习。实验表明该方法能有效改善接触区域的深度连续性。该工作为单目深度估计的结构一致性提供了新思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-006.webp\", \"caption\": \"\", \"page\": 2, \"index\": 6, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-007.webp\", \"caption\": \"\", \"page\": 2, \"index\": 7, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-008.webp\", \"caption\": \"\", \"page\": 2, \"index\": 8, \"width\": 560, \"height\": 560}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 1247, \"height\": 944}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-010.webp\", \"caption\": \"\", \"page\": 13, \"index\": 10, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-011.webp\", \"caption\": \"\", \"page\": 13, \"index\": 11, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-012.webp\", \"caption\": \"\", \"page\": 13, \"index\": 12, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-013.webp\", \"caption\": \"\", \"page\": 13, \"index\": 13, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-014.webp\", \"caption\": \"\", \"page\": 13, \"index\": 14, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-015.webp\", \"caption\": \"\", \"page\": 13, \"index\": 15, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-016.webp\", \"caption\": \"\", \"page\": 13, \"index\": 16, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-017.webp\", \"caption\": \"\", \"page\": 13, \"index\": 17, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-018.webp\", \"caption\": \"\", \"page\": 13, \"index\": 18, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-019.webp\", \"caption\": \"\", \"page\": 13, \"index\": 19, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-020.webp\", \"caption\": \"\", \"page\": 13, \"index\": 20, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-021.webp\", \"caption\": \"\", \"page\": 13, \"index\": 21, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-022.webp\", \"caption\": \"\", \"page\": 13, \"index\": 22, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-023.webp\", \"caption\": \"\", \"page\": 13, \"index\": 23, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-024.webp\", \"caption\": \"\", \"page\": 13, \"index\": 24, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-025.webp\", \"caption\": \"\", \"page\": 13, \"index\": 25, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-026.webp\", \"caption\": \"\", \"page\": 13, \"index\": 26, \"width\": 599, \"height\": 440}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-027.webp\", \"caption\": \"\", \"page\": 13, \"index\": 27, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-028.webp\", \"caption\": \"\", \"page\": 13, \"index\": 28, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-029.webp\", \"caption\": \"\", \"page\": 13, \"index\": 29, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-030.webp\", \"caption\": \"\", \"page\": 13, \"index\": 30, \"width\": 1300, \"height\": 859}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-328a1eaaeb5e2184cd7714bb/fig-031.webp\", \"caption\": \"\", \"page\": 13, \"index\": 31, \"width\": 1300, \"height\": 859}]"
motivation: 现有单目深度估计在物体接触区域会产生错误的深度不连续，影响结构一致性。
method: 提出边界检测与过滤模块显式识别接触区域，构建边界感知表示进行深度一致学习。
result: 在接触区域显著减少了错误的深度不连续，提升了深度预测的一致性。
conclusion: 将接触边界作为结构先验可有效改善单目深度估计的连续性。
---

## Abstract
While contemporary monocular depth estimation (MDE)methods achieve remarkable overall acacy, they consistently produce er-roneous depth discontinuities at object contact regions, particularly be-tween objects and supporting surfaces. In this paper, we address this crit-ical limitation by presenting a boundary-aware monocular depth estima-tion framework that enforces depth continuity at contact areas throughthe principled exploitation of contact boundaries as explicit structuralpriors. Specifically, we propose a boundary detection and filtering modulethat explicitly identifies object contact regions, yielding a novel boundary-aware representation that enables depth-consistent learning at contactareas. Furthermore, we introduce a boundary-aware feature fusion strat-egy that seamlessly incorporates contact boundary priors into the depthdecoding process, effectively rectifying the persistent discontinuities thatelude existing approaches. Our framework further supports interactiverefinement, allowing users to manually specify missing contact bound-aries for controllable depth correction. Extensive experiments on threeunseen benchmarks with dense object interactions demonstrate the ef-fectiveness of our approach, consistently outperforming baselines withparticularly pronounced gains in contact regions. Code is available athttps://github.com/abai969/contact-depth-refinement.git

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：现有单目深度估计（MDE）方法在整体精度上已取得显著进展，但在**物体接触区域**（尤其是物体与支撑面之间）常产生错误的深度不连续。
- **问题根源**：
  - 像素级监督将每个像素独立处理，忽略像素间几何依赖。
  - 基于 3D 点云表示的方法虽增强了几何一致性，但仍缺乏对**接触结构**的显式建模。
  - 边缘感知方法通常把所有边缘视为深度不连续线索，未区分“真实接触边界”与普通边缘。
- **整体含义**：论文提出将**接触边界作为显式结构先验**，引导深度解码器在物理相邻表面间保持深度连续，从而提升接触区域的深度一致性与 3D 几何连贯性，并支持用户交互式修正。

## 2. 方法论

- **核心思想**：先识别“哪里应保持深度连续”，再将该信息注入深度解码过程。框架建立在 MoGe 之上，MoGe 预测仿射不变 3D 点图，并采用全局/局部对齐损失、法向损失和掩码损失。
- **基础流程**：
  - 输入图像 \(I\) 经 DINOv2 骨干提取视觉特征 \(F\)。
  - 多尺度卷积解码器输出仿射不变 3D 点图 \(\hat P\)，其 z 坐标编码深度。
  - 使用 ROE 算法优化全局尺度 \(s\) 与平移 \(t\)，并通过多尺度局部对齐损失增强局部几何。
- **接触边界检测与过滤模块**：
  - **边缘检测**：采用 MuGE 多粒度边缘检测器，参数 \(a=0.5\)，得到密集边缘图 \(E\)，兼顾物体间边界与物体内部边缘。
  - **接触边界过滤**：
    - 使用 SigLIP 视觉编码器提取语义增强特征 \(S\)。
    - 对每个边缘点，沿其法线方向在两侧采样特征 \(s_i^+\)、\(s_i^-\)，计算差值 \(\Delta s_i\)，并拼接为边缘特征 \(t_i\)。
    - 轻量 MLP 分类器预测该边缘点是否为接触边界，得到接触概率图 \(\hat B\)。
    - 训练损失包括：带位置权重的 BCE 损失 \(L_{bce}\)，以及沿连续边界曲线的边缘方差损失 \(L_e\)，总损失 \(L_F = L_{bce} + \lambda_e L_e\)。
- **边界感知深度估计**：
  - **边界特征融合**：用 ResNet 编码器将 \(\hat B\) 提升为高维边界特征 \(C\)，与图像特征 \(F\) 多尺度融合为 \(\tilde F\)，再经解码器得到边界增强点云 \(\hat P'\)。
  - **边界感知监督**：
    - \(L_{bd}\)：接触边界像素上的深度对齐损失。
    - \(L_{grad}\)：沿 ground-truth 梯度法向的梯度一致性损失。
    - \(L_m\)：沿同一法向的平滑正则，抑制边界区域振荡。
    - \(L_{cons}\)：当边界图为全零时，约束辅助预测与冻结 MoGe 输出一致，防止边界不可靠时解码器偏离。
  - 总损失：\(L_B = \lambda_b L_{bd} + \lambda_g L_{grad} + \lambda_m L_m + \lambda_{aux} L_{cons}\)。
  - 最终训练目标：\(L_{total} = L_{MoGe} + L_F + L_B\)。
- **交互式细化**：用户可手动指定缺失的接触边界，实现可控的局部深度修正。

## 3. 实验设计

- **训练数据**：从 Hypersim 合成室内数据集中随机选取 **4,000 张图像**，利用其高质量深度图与自然接触边界过渡。
- **测试 benchmark**：三个训练中未见过的室内数据集：
  - **NYUv2**：标准室内深度估计 benchmark。
  - **iBims-1**：高分辨率深度图，便于评估精细几何结构。
  - **HAMMER**：包含缺失纹理、反射表面、透明材质等困难场景。
- **评估指标**：
  - 深度：绝对相对误差 \(Rel_d\)、内点率 \(\delta_1\)。
  - 点图：相对点误差 \(Rel_p\)、内点率 \(\delta_p^1\)。
  - 覆盖三种深度表示：scale-invariant、affine-invariant、affine-invariant disparity；点图覆盖 scale-invariant、affine-invariant、local affine-invariant。
  - 额外在接触区域附近报告仿射不变指标。
- **对比方法**：SharpNet、ZoeDepth、DUSt3R、DepthFM、Depth Anything V1/V2、Metric3D V2、UniDepth、MoGe 等。
- **实验类型**：
  - 表 1：三 benchmark 上的相对深度估计。
  - 表 2：三 benchmark 上的相对点估计。
  - 表 3：NYUv2 与 iBims-1 接触区域深度估计。
  - 表 4：iBims-1 上的消融实验。
  - 图 3：定性比较与 in-the-wild 示例。

## 4. 资源与算力

- 文中明确提到：所有实验在**单张 NVIDIA A100-80G GPU** 上完成。
- 训练策略：
  - 第一阶段：冻结接触边界过滤模块骨干，仅训练 MLP 分类器 **5 epochs**，batch size 2，学习率 \(1\times10^{-4}\)。
  - 第二阶段：整体联合微调 **12 epochs**，batch size 8；过滤骨干与深度编码器学习率 \(1\times10^{-6}\)，新增模块学习率 \(1\times10^{-5}\)，每 200 步减半。
- **未明确说明**：GPU 总数量、总训练时长、能耗、多次运行方差等。文中仅说明使用单卡，未给出完整算力开销。

## 5. 实验数量与充分性

- **实验组数**：
  - 三个零样本 benchmark 上的深度与点图评估。
  - 两个数据集上的接触区域专门评估。
  - 一组逐步消融：边缘检测、接触边界过滤、辅助一致性损失 \(L_{cons}\)。
  - 定性对比覆盖测试集与互联网 in-the-wild 图像。
- **充分性**：
  - 覆盖多数据集、多指标、多深度/点图表示，整体较充分。
  - 接触区域单独评估是亮点，能揭示全局指标掩盖的局部问题。
  - 消融实验验证了过滤模块与 \(L_{cons}\) 的必要性，尤其说明“直接融合所有边缘”会导致点图几何严重退化。
- **局限**：
  - 消融仅在 **iBims-1** 上进行，跨数据集泛化性验证不足。
  - 交互式细化仅有定性展示，缺少量化用户研究或修正成功率。
  - 部分方法在部分指标上缺失结果，局部点图在 NYUv2/HAMMER 上不可用。
  - 未报告统计显著性检验或多次运行方差，公平性总体较好但稳健性证据有限。

## 6. 主要结论与发现

- 将接触边界作为结构先验可有效减少物体接触区域的错误深度不连续。
- 在三个未见 benchmark 上，方法一致优于 MoGe 等强基线，尤其在接触区域提升明显：
  - iBims-1 接触区域 \(Rel_d\) 从 **1.71 降至 1.25**。
  - iBims-1 仿射不变点误差从 **3.61 降至 3.52**，局部点误差从 **4.16 降至 4.03**。
- 直接融合所有边缘虽能小幅改善深度指标，但会严重破坏全局 3D 点图一致性；过滤模块与辅助一致性损失 \(L_{cons}\) 对稳定几何至关重要。
- 方法支持交互式修正，可处理自动提取失败的接触边界。
- 仅需有限训练数据即可取得上述改进。

## 7. 优点

- **问题定义新颖**：明确区分“普通边缘”与“接触边界”，将接触关系作为显式结构先验。
- **方法设计系统**：检测—过滤—融合—边界感知监督形成完整链路。
- **语义增强过滤**：利用 SigLIP 视觉语言特征，无需推理时文本输入即可获得关系语义。
- **多尺度边界融合**：将边界概率图编码后注入深度解码器，兼顾结构与上下文。
- **损失设计互补**：零阶深度对齐、一阶梯度一致、平滑正则和辅助一致性共同作用。
- **交互式细化**：提供用户可控的深度修正接口，增强实用性。
- **实验亮点**：接触区域专门评估、零样本三 benchmark、有限训练数据、定性 in-the-wild 展示。

## 8. 不足与局限

- **依赖外部预训练模型**：MuGE、SigLIP2、MoGe、ResNet-18 等引入额外先验与计算开销，可能带来域偏差。
- **接触边界真值自动生成**：依赖边缘检测与深度一致性验证，在透明、反射、弱纹理区域可能不可靠，HAMMER 上的表现也显示困难场景仍有挑战。
- **交互式细化不可扩展**：依赖人工指定边界，主观性强，缺少量化评估。
- **场景覆盖有限**：训练与测试均为室内场景，未验证自动驾驶、户外、机器人等应用。
- **改进幅度不均**：部分全局指标提升较小，如 NYUv2 scale-invariant \(Rel_d\) 仅从 3.44 降至 3.43；主要收益集中在接触区域。
- **消融范围有限**：仅在 iBims-1 上做消融，未跨数据集验证各组件鲁棒性。
- **算力报告不完整**：未给出总训练时长、GPU 数量、能耗与重复实验方差。
- **应用限制**：边界图缺失或错误时，方法效果可能退化；虽然 \(L_{cons}\) 可缓解，但无法完全消除对边界质量的依赖。

（完）
