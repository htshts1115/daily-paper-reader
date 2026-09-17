---
title: "TR2M: Transferring Monocular Relative Depth to Metric Depth with Language Descriptions and Dual-Level Scale-Oriented Contrast"
title_zh: TR2M：借助语言描述与双层尺度对比将单目相对深度迁移为度量深度
authors: "Cui, Beilei, Huang, Yiming, Bai, Long, Ren, Hongliang"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Cui_TR2M_Transferring_Monocular_Relative_Depth_to_Metric_Depth_with_Language_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 9.0
evidence: 借助语言将单目相对深度迁移为度量深度
tldr: 度量深度估计受限于特定域，相对深度估计泛化好但尺度不确定，阻碍下游应用。本文提出TR2M框架，以文本描述与图像为输入，通过双层尺度导向对比学习估计重缩放因子，将相对深度迁移为度量深度。实验表明该方法可泛化到不同域并解决尺度不确定问题，提升单目深度在真实场景的可用性。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
motivation: 度量深度估计受域限制，相对深度估计泛化好但尺度不确定，影响下游应用。
method: 以文本描述和图像为输入，用双层尺度导向对比学习估计重缩放因子，将相对深度迁移为度量深度。
result: 在跨域场景下有效解决尺度不确定问题并提升度量深度精度。
conclusion: 为相对深度到度量深度的通用迁移提供语言引导框架。
---

## Abstract
This work presents a generalizable framework to transfer relative depth to metric depth. Current monocular depth estimation methods are mainly divided into metric depth estimation (MMDE) and relative depth estimation (MRDE). MMDEs estimate depth in metric scale but are often limited to a specific domain. MRDEs generalize well across different domains, but with uncertain scales that hinder downstream applications. To this end, we aim to build up a framework to solve scale uncertainty and transfer relative depth to metric depth. Previous methods used language as input and estimated two factors for conducting rescaling. Our approach, TR2M, utilizes both text descriptions and images as inputs and estimates two rescale maps to transfer relative depth to metric depth at the pixel level. Features from two modalities are fused with a cross-modality attention module to better capture scale information. A strategy is designed to construct and filter confident pseudo metric depth for more comprehensive supervision. We also develop dual-level scale-oriented contrastive learning to utilize depth distribution as guidance to enforce the model learning about intrinsic cues consistent with the scale distribution. TR2M only exploits a small number of trainable parameters to train on datasets in various domains and experiments not only demonstrate TR2M's great performance in seen datasets but also reveal superior zero-shot capabilities on five unseen datasets. We show the huge potential in pixel-wise transferring relative depth to metric depth with language assistance instead of large-size metric depth models with large amounts of training data. Code is available at: https://github.com/BeileiCui/TR2M.

---

## 论文详细总结（自动生成）

# TR2M 论文总结

## 1. 核心问题与整体含义
- 单目深度估计主要分为两类：**度量深度估计（MMDE）** 能输出米制尺度，但通常受限于特定域，依赖相机内参、传感器或域内微调，跨域泛化差；**相对深度估计（MRDE）** 泛化能力强，但尺度不确定，难以直接用于机器人导航、规划等需要绝对尺度的下游任务。
- 论文目标是：**把泛化性强的相对深度迁移为度量深度**，在尽量轻量、跨域的条件下解决尺度不确定问题。
- 已有语言辅助方法如 RSA 多使用全局 scale/shift 因子重缩放，存在两个问题：一是相对深度局部错误会被保留甚至放大；二是相同语言描述可能对应不同深度分布，且特征层面的尺度一致性常被忽视。
- TR2M 的定位是：以图像和文本描述为输入，预测**像素级 rescale maps**，将相对深度逐像素迁移到度量深度；论文声称是首个用文本描述做相对深度到度量深度像素级变换的工作。

## 2. 方法论
- **核心思想**：冻结预训练的相对深度模型生成相对深度 \(D_r\)，再用一个轻量可训练网络，根据 RGB 图像 \(I\) 和文本描述 \(L\)，预测尺度图 \(A\) 和平移图 \(B\)，对 \(D_r\) 做逐像素重缩放，得到度量深度。
- **网络结构**：
  - 图像和文本分别经冻结编码器提取特征：图像编码器为 DINOv2 ViT-L，文本编码器为 CLIP ViT-L/14。
  - 使用**跨模态注意力模块**融合图像与文本特征：图像特征作为 query，分别聚合图像和文本的 key/value，再经 skip connection 得到融合特征。
  - 两个轻量 DPT 风格解码头分别输出尺度图 \(A\in\mathbb{R}^{H\times W}\) 和平移图 \(B\in\mathbb{R}^{H\times W}\)。
  - 最终度量深度写作 \(\hat{D}_m = 1/(A \odot D_r + B)\)，即对相对深度做逐像素尺度/平移调整后取倒数。
- **伪度量深度监督**：
  - 用最小二乘对相对深度与真值度量深度做全局对齐，求 \(\tilde{\alpha}, \tilde{\beta}\)，生成伪度量深度 \(D_m^{pseudo}=\tilde{\alpha}D_r+\tilde{\beta}\)。
  - 若伪深度的阈值精度 \(\delta_1\) 大于预设阈值 \(\rho\)，则将其作为额外监督，缓解 GT 稀疏导致的监督不足。
- **双层尺度导向对比学习（Dual-Level Scale-Oriented Contrast）**：
  - **图像级粗对比**：按伪尺度因子排序图像嵌入，尺度相近的图像特征互相吸引，尺度差异大的互相排斥，使整体嵌入与尺度分布对齐。
  - **像素级细对比**：按深度分布把像素分成若干类，同类像素特征为正样本，异类为负样本，最大化正样本相似度、最小化负样本相似度；采用 EMA 双分支结构。
  - 总对比损失为 \(L_{soc}=L_{coarse}+L_{fine}\)。
- **总损失**：
  - 包含尺度不变 log 损失 \(L_{si}\)、阈值伪 SI log 损失 \(L_{tp-si}\)、尺度导向对比损失 \(L_{soc}\)、边缘感知平滑损失 \(L_{es}\)。
  - 训练目标为 \(L=\lambda_1L_{si}+\lambda_2L_{tp-si}+\lambda_3L_{soc}+\lambda_4L_{es}\)。

## 3. 实验设计
- **训练/主要评估数据集**：NYUv2、KITTI、VOID、C3VD，覆盖室内、室外、手术等场景，用同一模型实现跨域迁移。
- **零样本评估数据集**：SUN RGB-D、iBims-1、HyperSim、DIODE Outdoors、SimCol，共 5 个未见数据集，包含真实与合成、室内外与手术场景。
- **文本描述生成**：跟随 RSA，用 LLaVA v1.6 Vicuna 和 Mistral 生成图像文本描述。
- **评估指标**：AbsRel、RMSE、RMSE log、log10、\(\delta_1\)、\(\delta_2\)、\(\delta_3\)；前四者越低越好，后三者越高越好。
- **对比方法**：
  - 直接度量深度估计：DA、DA V2、ZoeDepth、UniK3D、Metric3Dv2、UniDepth。
  - 间接/迁移方法：DA 的 Median/Linear Fit/Global 缩放、DepthCLIP、DepthLM、ScaleDepth、WorDepth、RSA。
- **公平性设置**：所有方法评估均不做后处理，如尺度对齐或 median scaling；部分基线在作者环境中复现并用 * 标注。

## 4. 资源与算力
- 文中明确提到实验在 **NVIDIA RTX4090 GPU** 上进行。
- 训练配置：AdamW 优化器，batch size 8，学习率 \(1\times10^{-5}\)，每 epoch 衰减 0.9，训练 20 epochs。
- 模型规模：TR2M 仅 **19M 可训练参数**，训练图像约 **102K**；冻结模型包括 Depth Anything-Small 作为相对深度模型、CLIP ViT-L/14 文本编码器、DINOv2 ViT-L 图像编码器。
- **未明确说明**：GPU 数量、总训练时长、能耗、推理速度等；因此复现成本和实际部署开销无法从正文完整判断。

## 5. 实验数量与充分性
- 主要定量实验：
  - NYUv2：表 1，对比直接和间接度量深度方法。
  - KITTI：表 2，对比室外场景方法。
  - 零样本：表 3，在 5 个未见数据集上评估，并计算平均排名。
- 消融实验：
  - 表 4：验证 rescale maps、阈值伪深度监督 \(L_{tp-si}\)、尺度导向对比 \(L_{soc}\) 的有效性。
  - 表 5：验证文本信息与图像信息的互补性。
  - 补充材料中另有更多消融和设置说明。
- 充分性评价：
  - 覆盖多域训练、多个零样本数据集、多类对比方法，实验规模较充分。
  - 评估无后处理，较严格；部分基线复现，公平
