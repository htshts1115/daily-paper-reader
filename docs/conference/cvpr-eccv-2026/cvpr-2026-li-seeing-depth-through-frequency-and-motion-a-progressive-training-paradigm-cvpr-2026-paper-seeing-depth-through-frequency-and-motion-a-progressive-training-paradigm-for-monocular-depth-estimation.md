---
title: "Seeing Depth Through Frequency and Motion: A Progressive Training Paradigm for Monocular Depth Estimation"
title_zh: 透过频率与运动看深度：单目深度估计的渐进式训练范式
authors: "Li, Ke, Song, Bolin, Liu, Hongbo"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Li_Seeing_Depth_Through_Frequency_and_Motion_A_Progressive_Training_Paradigm_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 自监督单目深度估计，频率引导深度网络
tldr: 自监督单目深度估计虽进展显著，但频率混叠与跨帧运动建模不足导致深度边界模糊、相机运动估计欠佳。本文提出渐进式自监督框架，集成频率引导深度网络FGDepth与位姿查询网络PQNet：前者通过即插即用的频率引导采样模块增强高频细节、抑制混叠，后者用通道对齐注意力建模细粒度跨帧运动。实验表明该方法产生边界更锐利的深度图并改善位姿估计，提升了自监督深度估计的整体质量。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1761, \"height\": 976}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 3, \"index\": 2, \"width\": 2331, \"height\": 1060}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 3, \"index\": 3, \"width\": 1172, \"height\": 750}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 811, \"height\": 915}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 6, \"index\": 5, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 1242, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 832, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 6, \"index\": 9, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 6, \"index\": 15, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 6, \"index\": 16, \"width\": 1242, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 6, \"index\": 17, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 6, \"index\": 18, \"width\": 866, \"height\": 375}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 6, \"index\": 19, \"width\": 832, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 7, \"index\": 20, \"width\": 640, \"height\": 192}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 7, \"index\": 21, \"width\": 1704, \"height\": 852}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 7, \"index\": 22, \"width\": 512, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 7, \"index\": 23, \"width\": 640, \"height\": 192}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 7, \"index\": 24, \"width\": 512, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 7, \"index\": 25, \"width\": 512, \"height\": 256}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 7, \"index\": 26, \"width\": 640, \"height\": 192}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-li-seeing-depth-through-frequency-and-motion-a-progressive-training-paradigm-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 7, \"index\": 27, \"width\": 1719, \"height\": 1031}]"
motivation: 自监督单目深度估计受频率混叠与跨帧运动建模不足影响，深度边界模糊。
method: 提出渐进式自监督框架，包含频率引导深度网络FGDepth与位姿查询网络PQNet。
result: 频率引导采样增强高频细节抑制混叠，通道对齐注意力提升跨帧运动估计，深度边界更锐利。
conclusion: 该范式有效改善深度边界质量与相机运动估计。
---

## Abstract
Self-supervised monocular depth estimation has achieved remarkable progress in recent years, yet frequency aliasing and the lack of fine-grained cross-frame motion modeling still lead to blurred depth boundaries and suboptimal camera motion estimation.To address these challenges, we propose a progressive self-supervised framework that integrates a Frequency-Guided Depth Network (FGDepth) and a PoseQuery Network (PQNet). FGDepth incorporates a plug-and-play Frequency-Guided Sampling module that explicitly enhances high-frequency details and suppresses aliasing artifacts, producing depth maps with sharper boundaries. PQNet employs channel-aligned attention to model fine-grained cross-frame motion features, enabling more accurate and robust camera motion estimation. Furthermore, we design a progressive three-stage decoupled training strategy that effectively leverages the complementarity between depth and pose estimation, further improving overall performance.Extensive experiments on the KITTI benchmark demonstrate state-of-the-art performance, achieving a 4.1% reduction in Sq Rel over strong baselines, and our method also exhibits excellent cross-dataset generalization on Make3D. Ablation studies further validate the effectiveness of each proposed component.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **任务背景**：单目深度估计（MDE）是三维场景理解的核心任务，因仅需单目相机、硬件成本低，在自动驾驶与增强现实领域具有重要价值。自监督方法以图像重建为监督信号，摆脱了对大规模标注数据的依赖。
- **现存瓶颈**：
  - **频率混叠**：受 Nyquist-Shannon 采样定理启发，作者认为编码器-解码器结构下采样时，高频分量（如物体边缘、纹理等深度关键信息）被折叠进低频带，后续上采样无法有效恢复，导致深度边界模糊、细结构（如电线杆）无法解析，出现"边界渗色"伪影。
  - **跨帧运动建模不足**：现有 PoseNet 通常在网络早期融合相邻帧，难以建模细粒度的跨帧几何对应关系，导致相机运动估计欠佳。
  - **深度与位姿互补性未被充分利用**：二者本可相互强化（准确位姿可改善深度，反之亦然），但常规单阶段联合训练未能充分挖掘这一潜力。
- **整体含义**：论文提出一个渐进式自监督框架，从"频率"和"运动"两个视角同时切入，试图同时提升深度边界精度与位姿估计质量，为自监督 MDE 提供新的训练范式。

## 2. 方法论：核心思想、关键技术细节与算法流程

### 2.1 FGDepth：频率引导深度网络
- **核心思想**：将高频细节保留与混叠抑制显式地建模为频率域的双路径操作，并封装为即插即用、与架构无关的 **FGS（Frequency-Guided Sampling）块**，可无缝嵌入各类编码器-解码器或 Transformer 深度网络。
- **双路径设计**：
  - **高通增强路径**：从编码器特征中恢复并重新注入丢失的高频细节。
  - **低通滤波路径**：在解码器上采样时抑制混叠伪影，同时保留低频结构的语义完整性。
- **关键公式**：
  - 自适应低通核：`w_LP = softmax(Conv3×3(F_lr))`，高通核取互补：`w_HP = I − w_LP`。
  - 频率引导重建（谱补偿机制）：
    - `F̂_hr = (w_HP · F_hr + F_hr) + (w_LP · F_lr)↑`
    - 前项为**高频补偿**，后项为**带限基座**（上采样后），二者相加得到最终高频特征。
- **整体架构**：多路径 Transformer 编码器提取多尺度特征；解码器在每次上采样前用 FGS 块增强特征；跳跃连接融合语义与结构线索；多尺度视差头在 1/8、1/4、1/2 和全分辨率输出深度图。

### 2.2 PQNet：带通道对齐注意力的位姿查询网络
- **核心思想**：用跨帧查询的方式显式建模相邻帧之间的细粒度空间对齐，捕捉运动敏感特征。
- **网络组成**：Pose Stem（特征提取）→ PoseQuery Layer（跨帧对齐）→ Pose Trunk（高层运动表示）→ Pose Head（回归相对位姿）。
- **通道对齐注意力（CAA）**：
  - 对目标帧特征 `f_t` 做查询投影，对源帧 `f_s` 做键/值投影，所有投影**通道共享**以保证语义一致性。
  - 注意力计算：`CAA_{t→s} = Softmax(Q_t K_s^T / √d + BE) · V_s`，其中 `BE` 编码相对空间位置。
  - 并行计算自注意力 `SA_t`、`SA_s`，最终通过 **CAFuse**（轻量通道注意力）对拼接特征重标定，得到 `f_{t→s}`。
  - 为降低复杂度，特征被划分为不重叠的 **7×7 窗口**，CAA 与 SA 在窗口内计算后重新组装。

### 2.3 渐进式三阶段训练策略
- **动机**：深度与位姿可相互促进，需解耦优化以充分利用互补性。该策略理论上等价于**非凸非精确块坐标下降（BCD）**，交替近似更新可稳定收敛至驻点。
- **Stage 1 — 自监督 MDE 联合训练**：标准范式，以视图合成 `Î_{s→t}` 为代理任务，最小化光度损失 `L_p = (1−α)|I_t − Î_{s→t}| + α·(1−SSIM)/2`。
- **Stage 2 — 训练 PQNet**：冻结预训练深度网络，训练 PQNet；在光度损失基础上引入基于 SE(3) 李群的**互逆位姿约束**：`L_pose = ‖R_{t→s}R_{s→t} − I‖₁ + ‖R_{s→t}t_{t→s} + t_{s→t}‖₂`，即强制前后向位姿近似互逆，增强时序一致性（旋转项用 L1 增强抗噪，平移项用 L2 鼓励平滑回归）。
- **Stage 3 — 微调 FGDepth**：冻结 PQNet，将深度网络的普通上采样块替换为 FGS 块，仅训练涉及 FGS 的模块，利用预训练权重专注从高频线索恢复边缘与纹理等结构信息。

## 3. 实验设计

- **数据集与场景**：
  - **KITTI Depth**：采用 Eigen 划分，39,810 个单目三元组用于训练，4,424 用于验证，官方测试集 697 张图像（LiDAR 真值）。
  - **Make3D**：134 张图像（城市+自然场景），用于**零样本泛化**测试，不做微调。
  - **KITTI Odometry**：官方里程计划分，11 段序列（IMU/GPS 真值，仅用于评估），训练不使用，按标准协议测试序列 09–10。
- **Benchmark 与评价指标**：深度指标包括 Abs Rel、Sq Rel、RMSE、RMSE log 及 δ<1.25¹/²/³ 精度阈值（越低/越高越好的方向明确）；位姿采用 5 帧绝对轨迹误差（ATE）。
- **对比方法**：与大量自监督方法对比，包括 Zhou et al.、Vid2Depth、GeoNet、DDVO、Struct2depth、Monodepth2、CAdepth、R-MSFM6、MonoViT、SC-DepthV3、MonoFormer、SwinDepth、Lite-Mono、DNA-Depth-B1、HiDNet、RTIA-Mono、Gao et al.、GeoDepth 等；Make3D 上还对比了 Karsch、Liu、Laina 等监督方法。

## 4. 资源与算力

- **明确提及**：
  - 硬件：24 核 Intel 工作站，64GB 内存，**2 张 NVIDIA RTX 3090 GPU（每张 24GB 显存）**。
  - 框架：PyTorch v1.9.0；输入图像统一缩放至 **640×192**。
  - 超参设置（学习率、epoch 数、batch size 等）与基线 MonoViT 保持一致以保证公平比较。
- **未明确说明**：论文**未给出具体训练时长、总迭代次数或单次训练耗时**等细节。

## 5. 实验数量与充分性

- **实验规模**：
  - 主实验：KITTI 上与约 20 种方法的大规模定量对比（Table 1）。
  - 泛化实验：Make3D 零样本测试（Table 2）。
  - 位姿实验：KITTI Odometry 序列 09/10 的 ATE 对比（Table 4）。
  - 消融实验：
    - FGS 块的空间域与频率域双重分析（Fig. 7）。
    - FGDepth 与 PQNet 单独/组合的有效性（Table 3 上半部分）。
    - 三种训练策略（Batch / Epoch / Stage）对比（Table 3 下半部分）。
    - 补充材料中还涉及 FGS 搭配其他骨干、不同分辨率、PoseQuery Layer 插入位置等。
- **充分性与公平性评价**：
  - **充分**：覆盖深度精度、位姿精度、跨数据集泛化、模块消融、训练策略消融，维度较全面；提供了定性可视化（KITTI、Make3D 深度图，边界细节对比）。
  - **客观公平**：统一输入分辨率、统一超参与基线一致、与大量同协议方法对比，主实验对比具有说服力；消融在控制变量的前提下逐项验证各组件贡献。
  - **局限**：主要定量实验集中在 KITTI，其他数据集（Make3D）规模较小且仅作零样本验证；对训练策略的讨论以消融为主，缺少不同数据集下的策略验证。

## 6. 主要结论与发现

- **深度估计**：FGDepth 在 KITTI 上取得全部指标最优，Abs Rel 0.096、Sq Rel 0.679，显著超越 MonoViT（Sq Rel 降低 4.1%）与 DNA-Depth 等方法，且在复杂场景下更稳健。
- **泛化能力**：在 Make3D 零样本设置下同样全面领先，Sq Rel 与 RMSE 分别较基线降低 4.75% 与 1.86%，验证跨数据集鲁棒性。
- **位姿估计**：PQNet 显著提升 ATE 精度，序列 09/10 均优于联合训练基线；且更稳定的深度网络也能反过来提升位姿精度。
- **训练策略**：三阶段渐进策略在所有指标上最优，相比常规单阶段联合训练实现 Sq Rel 降低 3.55%；而 Batch 式交替训练因优化器内部状态频繁失效导致性能最差，Epoch 式也略逊于联合训练。
- **核心洞见**：深度与位姿网络存在**互相强化**关系；渐进式解耦优化可能是自监督学习领域值得探索的新范式。

## 7. 优点（方法与实验亮点）

- **理论动机清晰**：以 Nyquist-Shannon 采样定理为切入点解释深度边界模糊的成因，并将问题形式化为频率混叠与谱补偿，思路新颖且自洽。
- **模块即插即用**：FGS 块与架构无关，可嵌入 CNN/Transformer 深度网络，工程实用性强、通用性好。
- **注意力设计高效**：PQNet 采用通道共享投影保证语义一致性，并用 7×7 窗口局部注意力降低计算复杂度，兼顾精度与效率。
- **训练范式有理论支撑**：三阶段策略与块坐标下降（BCD）对应，非经验性拼凑，训练稳定性与收敛性有理论依据。
- **实验覆盖全面**：深度、位姿、泛化、消融、定性/定量、空间域/频率域多维验证，对比方法数量多，说服力较强。
- **无额外场景假设**：不依赖显式几何先验，可迁移至不同骨干，通用性优于依赖特定先验的方法。

## 8. 不足与局限

- **数据集覆盖有限**：主要评估集中在 KITTI（驾驶场景），Make3D 仅作零样本小规模测试，缺少如 Cityscapes、NYUv2 等其他场景（室内、非结构化）的大规模验证。
- **动态场景处理未深入**：论文提到动态场景与光度一致性假设违背是难点，但方法本身未显式建模运动物体，动态场景下的表现仍依赖光度损失的鲁棒性。
- **训练成本与时长未披露**：三阶段训练需要依次训练/冻结多个网络，计算开销可能高于单阶段联合训练，但论文未给出训练时长、显存占用等量化数据。
- **算力与可复现性**：仅用 2 张 RTX 3090，未说明训练轮数与总耗时，复现难度评估受限。
- **频率方法的上限**：FGS 基于空间域滤波近似频率处理，论文自称相比全局傅里叶变换更高效，但未与频域全局方法做充分的直接对比，其相对优势的边界尚不明确。
- **偏差风险**：消融实验中的部分结论（如 Batch 策略失败）可能受具体实现与超参影响，结论的普适性需更多验证；主要指标提升幅度（如 Sq Rel 降低 3~4%）虽显著但相对有限，实际应用收益需结合下游任务评估。
- **应用限制**：自监督 MDE 固有的尺度模糊问题仍需评估时对齐真值尺度，实际部署时仍受该限制约束。

（完）
