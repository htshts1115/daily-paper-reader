---
title: "RoSAMDepth: Robust Self-supervised Depth Estimation Leveraging Segment Anything Model"
title_zh: RoSAMDepth：利用分割一切模型的鲁棒自监督深度估计
authors: "Gao, Xuanang, Ning, Zhiwei, Zhang, Gengming, Cao, Jiaxi, Yang, Runze, Zheng, Zhonglong, Yang, Jie, Xiao, Rong, Liu, Wei"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_RoSAMDepth_Robust_Self-supervised_Depth_Estimation_Leveraging_Segment_Anything_Model_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 利用SAM目标级先验的鲁棒自监督单目深度估计
tldr: 现有自监督深度估计方法未考虑目标级信息，导致物体内部深度容易偏移，并在恶劣条件下变得模糊。本文提出RoSAMDepth框架，借助分割一切模型提供的丰富目标级先验增强鲁棒深度估计，通过分割引导的表示对比、自适应区域异常值处理等机制将目标感知注入特征空间。实验表明该方法在多种复杂条件下保持高质量深度。该工作提升了自监督深度估计的鲁棒性与物体边界一致性。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 775, \"height\": 435}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 775, \"height\": 435}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 775, \"height\": 435}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 3, \"index\": 10, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 3, \"index\": 11, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 3, \"index\": 12, \"width\": 546, \"height\": 303}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 3, \"index\": 13, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 3, \"index\": 14, \"width\": 546, \"height\": 303}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 3, \"index\": 15, \"width\": 546, \"height\": 303}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 546, \"height\": 303}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 546, \"height\": 307}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 495, \"height\": 275}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 3, \"index\": 19, \"width\": 546, \"height\": 303}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 4, \"index\": 20, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 8, \"index\": 21, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 8, \"index\": 22, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 8, \"index\": 23, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 8, \"index\": 25, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 8, \"index\": 26, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 8, \"index\": 30, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 8, \"index\": 31, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 8, \"index\": 32, \"width\": 544, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 8, \"index\": 33, \"width\": 708, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 8, \"index\": 34, \"width\": 708, \"height\": 393}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 8, \"index\": 35, \"width\": 708, \"height\": 416}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 8, \"index\": 36, \"width\": 708, \"height\": 418}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 8, \"index\": 37, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 8, \"index\": 38, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 8, \"index\": 39, \"width\": 576, \"height\": 320}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-gao-rosamdepth-robust-self-supervised-depth-estimation-leveraging-segment-anything-model-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 8, \"index\": 40, \"width\": 576, \"height\": 320}]"
motivation: 多数深度估计方法忽略目标级信息，导致物体内部深度偏移并在恶劣条件下模糊。
method: 提出RoSAMDepth，利用分割一切模型的目标级先验，通过分割引导表示对比与自适应区域异常值处理增强鲁棒性。
result: 在多种复杂条件下维持高质量深度估计，物体内部深度更一致。
conclusion: 引入目标级先验有效提升自监督深度估计的鲁棒性。
---

## Abstract
Robust depth estimation aims to maintain high-quality depths across diverse conditions. However, most existing methods estimate depth without taking into account the object-level information. As a result, the predicted depth may easily deviate within objects and become blurred under adverse conditions. To overcome this weakness, we propose RoSAMDepth, a novel framework that can assist robust self-supervised depth estimation in leveraging rich and diverse object-level priors from the Segment Anything Model (SAM). We focus on incorporating object-level information across three key aspects: a segment-guided representation contrasting method that injects object-level awareness into the feature representation space; an adaptive regional outlier masking strategy combined with a regional Gaussian likelihood loss that enforces regional depth smoothness; and an object-level reliability estimation strategy that mitigates the influence of unreliable supervision. Extensive experiments across multiple datasets and diverse weather conditions demonstrate that our method produces sharper, more accurate depth predictions, consistently outperforming state-of-the-art methods.

---

## 论文详细总结（自动生成）

# RoSAMDepth 论文总结

## 1. 核心问题与研究背景

- **任务定位**：单目深度估计是自动驾驶、机器人、AR/VR 等领域的基础任务。自监督方法通过立体像对或单目视频中的几何约束学习深度，避免了对昂贵真实深度标注的依赖。
- **核心痛点**：
  - 现有自监督方法在标准白天条件下表现良好，但在**夜间、雨天等恶劣条件**下，光度一致性假设被破坏，性能显著退化。
  - 更关键的是，**大多数方法忽略目标级（object-level）信息**，导致预测深度在物体内部容易发生偏移，物体边界模糊，在复杂环境下预测不稳定。
  - 早期方法针对单一条件（如夜间）设计；近期方法虽追求统一鲁棒性，但**对退化区域一视同仁**，未考虑语义/目标级差异对深度估计的影响。
- **为何不用语义分割**：语义分割无法区分同类实例（如两辆车深度差异可能极大）、类别集合受限、跨域泛化差。
- **为何选择 SAM**：Segment Anything Model 在大规模多样化数据上预训练，能分离实例，对未见物体和恶劣天气具有强零样本鲁棒性，是更优的目标级先验来源。
- **整体含义**：本文首次有效将 SAM 集成到鲁棒自监督深度估计中，仅在训练阶段离线使用预生成的 SAM 掩码作为目标级先验，提升恶劣条件下的深度质量与边界清晰度。

## 2. 方法论

### 2.1 核心思想
在 Syn2Real-Depth 的合成到真实训练范式基础上（教师网络 Φt 固定，学生网络 Φs 初始化自 Φt 并微调），从两个互补方向利用 SAM 目标级先验：
1. **目标感知表示学习**：让深度网络在特征层面隐式学习分割概念。
2. **基于目标级先验的深度学习**：改进监督信号，实现区域一致性与可靠性感知。

SAM 掩码通过 "segment-everything" 模式生成，经后处理（每个像素分配给包含它的最大面积掩码）得到不重叠区域划分，全部离线预生成。

### 2.2 关键技术细节

**（1）SRC：分割引导表示对比**
- 将 SAM 掩码最近邻插值到各解码器尺度，对每个分割区域内的特征取平均得到原型（特征与原型均在通道维归一化，约束在单位超球面）。
- 采用 InfoNCE 损失，拉近像素特征与其所属区域原型、推远与其他区域原型，促使同区域特征形成紧凑聚类。
- **关键设计**：对比施加在**特征层面而非最终深度**。原因是 SAM 常将单一物体过分割为多部分，若在深度上强制每个掩码边界不连续会引入错误监督；在特征空间传递先验则允许网络隐式学习目标感知表示。

**（2）AROM + 区域高斯似然损失（目标感知平滑）**
- **传统平滑损失的缺陷**：基于一阶深度导数与图像边缘权重，仅在深度边界附近产生弱局部梯度；在"深度估计错误但局部平滑"的区域（如误判为连续的背景）无法响应。
- **AROM**：对每个物体计算教师逆深度的均值 dt,i 与标准差 σt,i，得到归一化偏差图 δ；引入**自适应阈值** τ = τ0 + λσt,i（高方差区域放宽、同质区域收紧）；通过温度控制的锐化 sigmoid 生成异常值抑制掩码 Mout（异常值处取值低）。
- **区域高斯似然损失 Lrgl**：将每个区域内教师逆深度建模为高斯分布，惩罚学生深度偏离区域统计量，并用 (1−Mout) 加权，使监督聚焦于异常值区域，产生强而非局部的梯度。
- Mout 具有双重作用：既引导 Lrgl，也在深度蒸馏损失中抑制异常值误差传播。

**（3）ORE：目标级可靠性估计**
- **动机**：像素级光度误差与深度可靠性不匹配——物体内部像素外观相似，即使整体深度被错误缩放，仍可能出现偶然对齐，导致仅识别出零散不可靠像素。
- **方法**：计算像素级光度误差 pe（L1 + SSIM 组合），按 SAM 掩码聚合为每物体平均误差 pe_i；与全图平均误差 pe 比较，得到可靠性图 R（误差偏离全局越大的物体可靠性越低）；构造加权图 Wrel = R + ε。

**（4）总损失**
- 鲁棒深度蒸馏损失 Ld = Mout · Wcst · Wrel · |Ds − Dt| / Ds（Wcst 为基线模型的一致性重加权图）。
- 总损失 Ltotal = Ld + λ1·Lsrc + λ2·Lrgl + Lext（Lext 为基线辅助损失）。

## 3. 实验设计

- **数据集**：
  - **nuScenes**：21,476 张训练图像（15,129 白天、3,796 雨天、2,551 夜间），6,019 个连续帧对评估（4,449 白天、1,088 雨天、602 夜间），指标计算范围 0.1–80 m。
  - **Oxford RobotCar**：17,790 张白天 + 19,162 张夜间训练，1,411 张单帧测试（702 白天、709 夜间），指标范围 0.1–50 m。
- **评估指标**：AbsRel、SqRel、RMSE、δ1。
- **设置**：单帧（相同输入）与多帧（时序相邻输入）两种；训练调度沿用 Syn2Real-Depth。
- **对比方法**：Monodepth2、R4Dyn（雷达）、RNW、Robust-Depth、md4all-AD/DD、DM-MDE、Syn2Real-Depth、Manydepth，以及 RobotCar 上的 DeFeatNet、ADIDS、WSGD 等。
- **定性对比**：在雨天、夜间、白天眩光等场景下与 md4all、Syn2Real-Depth 比较深度边界与一致性。

## 4. 资源与算力

- 文中明确给出的训练配置：PyTorch 实现，Adam 优化器，**batch size = 10**，学习率 8e−5 且每 5 个 epoch 衰减 0.5，学生网络训练 **10 个 epoch**；SAM 使用现成的默认 **ViT-H** 预训练模型（仅离线预生成掩码）。
- **未明确说明**：GPU 型号、GPU 数量、总训练时长、显存占用等硬件资源信息均未在正文中提及，也未给出 SAM 掩码预生成的耗时统计。这是一个可复现性上的信息缺口。

## 5. 实验数量与充分性

- **主实验**：2 个数据集 × 多条件（白天/夜间/雨天）× 单帧/多帧，共约 4 组主对比表格。
- **消融实验**：
  - 表 3：SRC / AROM / Lrgl / ORE 四组件的逐项累加消融（在夜间与雨天条件下）。
  - 表 4：不同平滑损失定义对比（图像边缘感知、SAM 边界感知、AROM & Lrgl）。
  - 表 5：SRC 不同实现方式对比（施加于预测深度 vs. 特征层面）。
- **定性实验**：多场景可视化对比。
- **充分性评价**：
  - 消融覆盖了全部三个贡献点，且包含对失败设计的对比（SRC on Ds），论证较客观。
  - 在两个主流数据集上均与大量 SOTA（含合成数据训练与真实数据训练方法）对比，公平性较好。
  - **不足**：所有实验均基于驾驶场景数据集（nuScenes、RobotCar），未覆盖室内、机器人等场景；未报告参数量/推理速度等效率指标；对超参数 τ0、λ、β 的敏感性缺乏分析；SAM 掩码质量对结果的影响未做定量研究。

## 6. 主要结论与发现

- 在 nuScenes 上，相比 Syn2Real-Depth，在单帧与多帧、各条件下平均相对提升：AbsRel 2.8%、SqRel 2.7%、RMSE 0.6%、δ1 0.9%。
- 在 RobotCar 上，相比 Syn2Real-Depth 提升：AbsRel 4.4%、SqRel 7.6%、RMSE 4.7%、δ1 0.9%（尤其夜间提升明显）。
- 定性结果显示：在雨天低对比度、夜间弱光与强眩光场景下，本方法能保持更锐利的物体结构与边界，抑制反射伪影，准确恢复物体间空间关系。
- 消融证实：SRC 直接作用于预测深度会因 SAM 过分割而性能下降；AROM 与 Lrgl 必须配合使用（单独去掉任一项都会退化）；ORE 能进一步提升蒸馏损失的有效性。

## 7. 优点

- **创新性**：首次将 SAM 目标级先验有效引入鲁棒自监督深度估计，且仅在训练阶段离线使用掩码，不增加推理开销。
- **设计巧妙**：
  - SRC 在特征层面而非深度层面做对比，规避了 SAM 过分割带来的错误监督，思路清晰。
  - AROM 采用随区域方差自适应的阈值，兼顾高方差结构（地面、建筑）与同质区域，比固定阈值更合理。
  - ORE 将可靠性评估从像素级提升到目标级，直击像素级光度误差的固有缺陷（图 4 的深度缩放实验很有说服力）。
- **实验扎实**：消融完整，覆盖三组件的独立与组合效果，并包含反例验证；在两个不同数据集、多天气条件下与众多 SOTA 对比，结果一致性较好。
- **与基线正交**：方法建立在 Syn2Real-Depth 之上，属于可叠加的改进，便于后续工作借鉴。

## 8. 不足与局限

- **硬件资源未披露**：缺少 GPU 型号、数量、训练时长等信息，影响复现与算力评估。
- **场景覆盖有限**：仅在 nuScenes 与 Oxford RobotCar 两个驾驶数据集上验证，未涉及室内、非结构化环境或机器人场景；对雾天、雪天等条件未单独评估。
- **依赖 SAM 掩码质量**：方法高度依赖 SAM 的过分割/漏分割行为，但未定量分析掩码质量波动对深度性能的影响；掩码预生成的开销与存储成本未讨论。
- **超参数敏感性缺失**：τ0、λ、β、温度 T 等关键超参数缺乏敏感性分析或调参依据。
- **效率与实时性**：未报告推理速度、参数量、显存等，难以判断实际部署可行性。
- **提升幅度有限**：在 nuScenes 的 RMSE 与 δ1 上提升仅 0.6% 与 0.9%，部分条件（如 nuScenes 夜间 RMSE 7.966 vs. 7.949）甚至略有退步，说明改进并非在所有指标上一致。
- **对教师模型的依赖**：仍沿用固定教师蒸馏范式，若教师本身在极端条件下严重错误，学生可能继承其偏差（尽管 ORE 部分缓解了该问题）。

（完）
