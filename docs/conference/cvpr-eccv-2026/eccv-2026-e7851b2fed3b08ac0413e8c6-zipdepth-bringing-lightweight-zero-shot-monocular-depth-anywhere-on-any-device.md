---
title: "ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device"
title_zh: ZipDepth：让轻量零样本单目深度估计随处、随处可用
authors: "Fabio Tosi, Luca Bartolomei, Matteo Poggi, Stefano Mattoccia"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/14420.pdf"
tags: ["query:mono-depth"]
score: 10.0
evidence: 面向移动与嵌入式设备的轻量零样本单目深度
tldr: 深度基础模型虽具备稳健的零样本泛化能力，但计算量远超嵌入式与移动平台；现有轻量方案多局限于单域自监督范式，在域偏移下会静默失效。本文提出ZipDepth紧凑单目深度网络，结合可重参数化编码解码器与来自基础模型的大规模知识蒸馏，并在大规模多域数据上训练。该网络仅610万参数，可在服务器GPU到受限设备上实时运行，实验表明其取得领先的零样本深度性能。该工作为移动端部署高质量深度估计提供了可行方案。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 1344, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 500, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1787, \"height\": 980}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 2405, \"height\": 1462}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 1344, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 500, \"height\": 350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 1787, \"height\": 980}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 2405, \"height\": 1462}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-009.webp\", \"caption\": \"\", \"page\": 12, \"index\": 9, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-010.webp\", \"caption\": \"\", \"page\": 12, \"index\": 10, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-011.webp\", \"caption\": \"\", \"page\": 12, \"index\": 11, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-012.webp\", \"caption\": \"\", \"page\": 12, \"index\": 12, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-013.webp\", \"caption\": \"\", \"page\": 12, \"index\": 13, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-014.webp\", \"caption\": \"\", \"page\": 12, \"index\": 14, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-015.webp\", \"caption\": \"\", \"page\": 12, \"index\": 15, \"width\": 1242, \"height\": 375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-016.webp\", \"caption\": \"\", \"page\": 12, \"index\": 16, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-017.webp\", \"caption\": \"\", \"page\": 12, \"index\": 17, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-018.webp\", \"caption\": \"\", \"page\": 12, \"index\": 18, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-019.webp\", \"caption\": \"\", \"page\": 12, \"index\": 19, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-020.webp\", \"caption\": \"\", \"page\": 12, \"index\": 20, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-021.webp\", \"caption\": \"\", \"page\": 12, \"index\": 21, \"width\": 6211, \"height\": 4137}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-022.webp\", \"caption\": \"\", \"page\": 12, \"index\": 22, \"width\": 720, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-023.webp\", \"caption\": \"\", \"page\": 12, \"index\": 23, \"width\": 720, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-024.webp\", \"caption\": \"\", \"page\": 12, \"index\": 24, \"width\": 720, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-025.webp\", \"caption\": \"\", \"page\": 12, \"index\": 25, \"width\": 720, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-026.webp\", \"caption\": \"\", \"page\": 12, \"index\": 26, \"width\": 720, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-027.webp\", \"caption\": \"\", \"page\": 12, \"index\": 27, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-028.webp\", \"caption\": \"\", \"page\": 12, \"index\": 28, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-029.webp\", \"caption\": \"\", \"page\": 12, \"index\": 29, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-030.webp\", \"caption\": \"\", \"page\": 12, \"index\": 30, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-031.webp\", \"caption\": \"\", \"page\": 12, \"index\": 31, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-032.webp\", \"caption\": \"\", \"page\": 12, \"index\": 32, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-033.webp\", \"caption\": \"\", \"page\": 12, \"index\": 33, \"width\": 1024, \"height\": 768}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-034.webp\", \"caption\": \"\", \"page\": 12, \"index\": 34, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-035.webp\", \"caption\": \"\", \"page\": 12, \"index\": 35, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-036.webp\", \"caption\": \"\", \"page\": 12, \"index\": 36, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-037.webp\", \"caption\": \"\", \"page\": 12, \"index\": 37, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-038.webp\", \"caption\": \"\", \"page\": 12, \"index\": 38, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-039.webp\", \"caption\": \"\", \"page\": 14, \"index\": 39, \"width\": 1800, \"height\": 1200}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-040.webp\", \"caption\": \"\", \"page\": 14, \"index\": 40, \"width\": 1800, \"height\": 1200}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-041.webp\", \"caption\": \"\", \"page\": 14, \"index\": 41, \"width\": 1800, \"height\": 1200}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-042.webp\", \"caption\": \"\", \"page\": 15, \"index\": 42, \"width\": 1920, \"height\": 1024}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-043.webp\", \"caption\": \"\", \"page\": 15, \"index\": 43, \"width\": 2048, \"height\": 1152}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-044.webp\", \"caption\": \"\", \"page\": 15, \"index\": 44, \"width\": 2048, \"height\": 1375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-045.webp\", \"caption\": \"\", \"page\": 15, \"index\": 45, \"width\": 2048, \"height\": 1365}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-046.webp\", \"caption\": \"\", \"page\": 15, \"index\": 46, \"width\": 960, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-047.webp\", \"caption\": \"\", \"page\": 15, \"index\": 47, \"width\": 896, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-048.webp\", \"caption\": \"\", \"page\": 15, \"index\": 48, \"width\": 2048, \"height\": 1375}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-e7851b2fed3b08ac0413e8c6/fig-049.webp\", \"caption\": \"\", \"page\": 15, \"index\": 49, \"width\": 768, \"height\": 512}]"
motivation: 深度基础模型计算量过大难以部署到移动端，而轻量方案多局限于单域且在域偏移下失效。
method: 提出ZipDepth，结合可重参数化编码解码器与基础模型的大规模知识蒸馏，在多域数据上训练。
result: 仅610万参数即可在受限设备上实时运行，并取得领先的零样本深度性能。
conclusion: 为移动端部署高质量零样本单目深度估计提供了可行方案。
---

## Abstract
Monocular depth estimation has seen remarkable progressthrough foundation models achieving robust zero-shot generalization, yettheir computational demands place them far beyond the reach of em-bedded and mobile platforms. Lightweight alternatives exist, but havebeen developed almost exclusively within single-domain, self-supervisedparadigms, failing silently under domain shift. We present ZipDepth, acompact monocular depth network that bridges this gap by combining anefficient reparameterizable encoder-decoder with large-scale knowledgedistillation from a foundation model over a large multi-domain train-ing set. Comprising just 6.1M parameters, ZipDepth runs at real-timerates from server GPUs to power-constrained devices, achieving the besttrade-off between zero-shot accuracy and deployment efficiency amonglightweight models across five benchmarks, taking a significant step to-wards the accuracy of foundation models with 50× more parameters.

---

## 论文详细总结（自动生成）

# ZipDepth 论文中文总结

## 1. 核心问题与研究动机

- **背景**：单目深度估计长期是病态问题（单张 2D 图像对应无穷多 3D 场景），但对自动驾驶、机器人操作、AR、场景重建等应用至关重要。
- **范式演进**：
  - 早期监督方法（Eigen 等）与自监督方法（基于光度一致性）均局限于单一数据集/传感器/场景类别，跨域性能差。
  - 深度基础模型（Depth Anything v2、Marigold、Metric3D、DepthPro 等）借助 DINOv2、ViT、扩散骨干实现了稳健的零样本泛化，但代价极高：300–900M 参数、数百至数千 GFLOPs、需数十块高端 GPU 训练数周。例如 DA-V2-Large 在 15W Jetson Orin NX 上仅 0.3 FPS，在智能手机上完全不可用。
  - 轻量网络（Lite-Mono、GuideDepth、FastDepth、PyDNet）仅 1–8M 参数，可在 CPU/嵌入式加速器上实时运行，但几乎全部在单域自监督范式下开发（KITTI 或 NYUv2），在域偏移下会"静默失效"。
- **核心矛盾**：零样本泛化需要大模型，实时部署需要小模型，二者在文献中长期不可兼得。
- **论文主张**：弥合该鸿沟需在**训练数据**与**架构设计**两条战线同时推进——仅让紧凑网络接触多样的大规模教师监督还不够，架构还必须在严苛的参数与延迟预算内保留深度不连续与物体边界等细粒度结构。

## 2. 方法论

### 2.1 核心思想
将基础模型（DA-V2-Large）的跨域知识通过教师-学生蒸馏迁移到一个紧凑、可重参数化、可原生导出的 CNN 中，从而把"泛化能力"与"模型容量"解耦。全部算子均限定为 TensorRT / CoreML / NNAPI 原生支持的算子，导出时无需自定义算子或图手术。

### 2.2 编码器
- **Split Stem**：不使用两次连续 stride-2 卷积直接降到 H/4，而是保留 H/2 的中间激活 `s_{1/2}`（C=48）作为专用跳跃连接，为解码器提供边界线索而不增加编码器全分辨率开销；`s_{1/4}` 进入 Stage 1。
- **可重参数化骨干**：以 RepVGG 式单元为基础，训练时并行 3×3 卷积、1×1 卷积与（通道匹配时的）恒等捷径三支路，BN 后相加再过 ReLU；推理时三支路代数融合为单个 3×3 卷积并吸收偏置，为无损操作，且适用于网络中所有 ConvBN 层。输出步长 {4, 8, 16, 32}。
- **多尺度上下文（Stage 2）**：用仅含深度可分离卷积的并行空洞模块（r=1 与 r=2）替代标准空洞卷积（后者在移动 NPU 上非单位步长缺乏高效融合核），融合后有效感受野达 5×5。
- **条带池化注意力（Stage 2）**：用水平/垂直条带平均捕捉长程上下文，复杂度 O(N)。将原版有界于 [1,2] 的加性门（只能放大）替换为**对称 sigmoid 门** `f ← f·σ(BN(W_g∗(f̄_H+f̄_W)))`。
- **通道与全局上下文（Stage 3）**：在最后一个重参数化块后接 SE 通道注意力与 Global Context 块（softmax 加权空间池化聚合单一场景向量，瓶颈压缩比 4），均为 O(N)，避免在嵌入式硬件上代价过高的全自注意力。
- **Stage 4**：两个重参数化块，步长 32，输出最粗特征 f4。
- **SPPF + 跨尺度精修**：SPPF 在 C4/4 瓶颈投影上级联三次 5×5 最大池化；随后双向跨尺度模块通过分组 1×1 卷积在 Stage 3 与 Stage 4 间交换信息。

### 2.3 解码器
- **渐进多尺度融合**：由粗到细，每级将高分辨率编码器跳跃特征与上采样后的粗特征经分组 1×1 卷积投影后相加并过 BN+ReLU；分组数取输入/输出通道数的最大公约数（上限 4）以降低内存带宽。通道宽度从 stride 32 的 3C_dec 递减至 stride 4 的 C_dec，解码器占总参数不足 3%。
- **高分辨率跳跃**：四级融合至 stride 4 后，在 stride 2 融合 split-stem 跳跃 `s_{1/2}`（C_half=32），由 3×3 卷积头预测半分辨率深度图 `d̂_{1/2}`，最终仅经一次 2× 上采样得到全分辨率图（有效输出步长 1）。
- **硬件自适应凸上采样**（训练前按目标硬件选择路径）：
  - **GPU/TensorRT 路径**：借鉴 RAFT，卷积头预测每像素 3×3 邻域掩码并经 softmax 归一化（温度 τ），用 unfold（replicate 填充）提取邻域，做凸组合后经 PixelShuffle 与 ReLU 输出；softmax 保证输出被约束在局部邻域内。
  - **NPU/移动路径**：仅用标准 Conv2D 与插值算子，学习一个门控 α∈(0,1)（由 1×1 降维 + 深度可分离 5×5 + 1×1 投影生成，前两步各接 BN 与 ReLU）在最近邻与双线性上采样间混合，α 在深度不连续处偏向最近邻、平滑区域偏向双线性。
  - 两条路径的最终 ReLU 在推理时均融合进前序卷积。

### 2.4 训练目标
- 采用 MiDaS / DA-V2 的**尺度-平移不变（SSI）目标**，计算损失前对预测与目标按有效像素做逐图像中位数与 MAD 归一化，消除仿射歧义。
- 总损失 `L = λ_ssi·L_ssi + λ_grad·L_grad`，其中 L_ssi 为归一化后的平均绝对误差，L_grad 为多尺度梯度损失，权重取 λ_ssi=1.0、λ_grad=2.0（沿用 DA-V2 配置）。

## 3. 实验设计

- **训练数据**：17 个真实场景数据集（Object365、ADE20K、COCO、SA-1B、OpenImages v7、Google Landmarks、MegaDepth、Mapillary、Cityscapes、BDD100K、DrivingStereo、Gated2Depth、Trans10K、Flickr1024、HRWSI、HoloPix50K、ACDC），共约 **14.1M 图像**；深度伪标签由 DA-V2-Large 离线生成；使用温度缩放的分域平衡采样器缓解数据集规模不均衡。
- **评测协议**：遵循 Marigold 的评测方法，在 **5 个训练中未见过的真实数据集**上零样本测试：NYUv2（654 张室内）、ScanNet（800 张）、KITTI（Eigen split 652 张街景）、ETH3D（454 张高分辨率）、DIODE（325 室内 + 446 室外）。预测经最小二乘对齐到 GT 后报告 **AbsRel** 与 **δ1**。
- **对比方法**：
  - **大型预训练模型**：DPT-Hybrid、DPT-Large、Omnidata-v2、Marigold、DA-V2-Small/Base/Large（用官方权重零样本评测）。
  - **轻量模型**：Lite-Mono、GuideDepth、FastDepth、PyDNet（均在本文训练集上用相同协议重训，以隔离训练数据差异），以及 MiDaS-Small。
- **效率评测**：在 Jetson Orin NX 15W 模式下测量参数量、MACs、FPS 与每帧能耗（统一 384×384 输入、FP32）。
- **消融实验**：架构组件（去 SE+GCBlock / 去 SPPF+Cross-Scale / 去半分辨率路径）、上采样策略（双线性 vs 凸上采样 GPU/NPU 路径）、数据规模（1%、10%、25%、50%、100%）。
- **部署评测**：9 个硬件平台，从 350W 服务器 GPU 到 5W 智能手机。
- **定性评测**：5 个基准的可视化对比；另在 DA-2K 的恶劣天气、航拍、透明/反射、水下场景上做零样本定性验证。

## 4. 资源与算力

- **训练算力**：论文明确说明仅使用 **2 块 NVIDIA RTX 3090 GPU、训练 3 天**，与基础模型通常需要数十块高端 GPU 形成鲜明对比。
- **训练调度**：三阶段渐进分辨率——256×256 训练 10 epoch（每 GPU batch 192，峰值 LR 2×10⁻³）→ 384×384 训练 5 epoch（batch 128，LR 5×10⁻⁴）→ 512×512 训练 3 epoch（batch 96，LR 2.5×10⁻⁴）；每阶段由上一阶段检查点初始化；LR 先半 epoch 线性预热再余弦退火至峰值的 1%；仅用随机方形裁剪与 0.5 概率水平翻转，无其他数据增强。
- **额外算力**：致谢中提到 CINECA 通过 ISCRA 计划提供的 HPC 资源（用途未详述）。
- **推理侧**：模型 6.1M 参数（训练时 6.79M，融合后 6.14M）、3.0 GMACs，可在服务器 GPU 至手机端实时运行。

## 5. 实验数量与充分性

- **实验规模**：约 12 个对比方法 × 5 个零样本基准的主表；3 组消融（架构 4 个配置、上采样 3 种策略、数据规模 5 档）；9 个硬件平台的部署剖析；5 个基准的定性对比 + DA-2K 4 类极端场景定性。整体覆盖面较广。
- **公平性设计（亮点）**：
  - 轻量基线全部在**同一训练集、同一训练协议/调度**下从零重训，且不使用预训练编码器，以隔离"训练数据差异"与"架构差异"；对无法精确复现的架构，尽量匹配 batch size 与总迭代数。
  - 基础模型使用官方权重零样本评测。
  - 效率指标统一在 384×384 输入、FP32 下测量，并说明各模型内部会 resize 到自身原生分辨率。
- **客观性注意点**：
  - 由于轻量基线为近似重训（论文自述"approximate the protocol"），其成绩可能不完全等价于各自最优配置，存在轻微低估或高估风险。
  - 边界质量评测仅在合成的 UnrealStereo4K 上以 SI-BF1 衡量，
