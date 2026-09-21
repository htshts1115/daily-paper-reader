---
title: "Hybrid-LUT: Channel-Aware Hybrid Lookup Table and Filtering for Efficient Image Restoration"
title_zh: Hybrid-LUT：面向高效图像恢复的通道感知混合查找表与滤波
authors: "Zhilin Ai, Boyu Li, Sidi Yang, Wenqing Shi, Wenyong Zhou, Binxiao Huang, Chenchen Ding, Ngai Wong"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/7329.pdf"
tags: ["query:cv-render"]
score: 5.0
evidence: 面向图像恢复的高效硬件友好查找表与滤波
tldr: 现有基于RGB查找表的图像去噪方法需为三个通道并行维护相同LUT，片上存储开销大，而仅在亮度通道处理又会引入色彩失真和残留伪影。本文提出Hybrid-LUT，一种基于YUV的非对称通道处理框架，将查找表与滤波统一设计。实验表明该方法在保持高效率和硬件友好性的同时缓解了色偏与残留伪影。其高效滤波思路可迁移至移动端虚化与实时渲染管线。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-001.webp\", \"caption\": \"\", \"page\": 4, \"index\": 1, \"width\": 645, \"height\": 645}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-002.webp\", \"caption\": \"\", \"page\": 4, \"index\": 2, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-003.webp\", \"caption\": \"\", \"page\": 4, \"index\": 3, \"width\": 359, \"height\": 359}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-004.webp\", \"caption\": \"\", \"page\": 4, \"index\": 4, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-005.webp\", \"caption\": \"\", \"page\": 4, \"index\": 5, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-006.webp\", \"caption\": \"\", \"page\": 4, \"index\": 6, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-007.webp\", \"caption\": \"\", \"page\": 5, \"index\": 7, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-008.webp\", \"caption\": \"\", \"page\": 5, \"index\": 8, \"width\": 358, \"height\": 336}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-009.webp\", \"caption\": \"\", \"page\": 5, \"index\": 9, \"width\": 358, \"height\": 336}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-010.webp\", \"caption\": \"\", \"page\": 5, \"index\": 10, \"width\": 358, \"height\": 336}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-011.webp\", \"caption\": \"\", \"page\": 5, \"index\": 11, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-012.webp\", \"caption\": \"\", \"page\": 5, \"index\": 12, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-013.webp\", \"caption\": \"\", \"page\": 5, \"index\": 13, \"width\": 358, \"height\": 336}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-014.webp\", \"caption\": \"\", \"page\": 5, \"index\": 14, \"width\": 500, \"height\": 334}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-015.webp\", \"caption\": \"\", \"page\": 5, \"index\": 15, \"width\": 360, \"height\": 335}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-016.webp\", \"caption\": \"\", \"page\": 5, \"index\": 16, \"width\": 358, \"height\": 336}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-017.webp\", \"caption\": \"\", \"page\": 5, \"index\": 17, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-018.webp\", \"caption\": \"\", \"page\": 5, \"index\": 18, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-019.webp\", \"caption\": \"\", \"page\": 5, \"index\": 19, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-020.webp\", \"caption\": \"\", \"page\": 5, \"index\": 20, \"width\": 358, \"height\": 336}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-021.webp\", \"caption\": \"\", \"page\": 5, \"index\": 21, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-022.webp\", \"caption\": \"\", \"page\": 5, \"index\": 22, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-023.webp\", \"caption\": \"\", \"page\": 5, \"index\": 23, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-024.webp\", \"caption\": \"\", \"page\": 8, \"index\": 24, \"width\": 1000, \"height\": 500}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-025.webp\", \"caption\": \"\", \"page\": 9, \"index\": 25, \"width\": 772, \"height\": 546}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-8e94d6d7f1350f1eeff54476/fig-026.webp\", \"caption\": \"\", \"page\": 9, \"index\": 26, \"width\": 772, \"height\": 547}]"
motivation: 现有RGB查找表去噪需三通道并行导致片上存储开销大，而仅在亮度通道处理又会造成色彩失真。
method: 提出Hybrid-LUT，一种基于YUV的非对称通道处理框架，将查找表与滤波统一设计。
result: 在保持高效率和硬件友好性的同时缓解了色偏与残留伪影。
conclusion: 提供高效图像滤波方案，其思路可迁移到移动端虚化与实时渲染管线。
---

## Abstract
Lookup table (LUT)-based image denoising methods haveattracted increasing attention due to their high efficiency and hardware-friendly properties. However, existing RGB-LUT approaches require threeidentical LUTs to process RGB channels in parallel, resulting in largeon-chip SRAM consumption. A simple alternative is to apply LUT pro-cessing only to the luminance (Y) channel in the YUV color space toreduce memory usage. However, this naive strategy leads to degradedrestoration quality, since ignoring the chrominance (UV) channels in-troduces color distortion and residual artifacts. In this work, we pro-pose Hybrid-LUT, a YUV-based asymmetric channel-processing frame-work that combines LUT and filtering in a unified design. Specifically, amulti-band LUT branch with pixel-level weight fusion is applied to theY channel to recover fine textures, while lightweight filtering is used forthe UV channels to maintain color consistency. This design reduces LUTstorage by two-thirds compared with RGB-LUT methods while main-taining the same runtime throughput. Extensive experiments show thatHybrid-LUT achieves state-of-the-art (SOTA) performance across mul-tiple benchmarks with only 421 KB of storage. In particular, our methodsurpasses existing LUT-based denoising approaches by at least 0.63 dBCPSNR on real-world datasets, demonstrating its effectiveness for imagedenoising on resource-constrained edge devices.

---

## 论文详细总结（自动生成）

# Hybrid-LUT 论文中文结构化总结

## 1. 核心问题与研究动机

- **背景**：图像恢复（去噪）领域中，DNN 方法（DnCNN、SwinIR、Restormer 等）保真度高，但参数量大、浮点运算密集、内存带宽需求高，难以部署在功耗与存储受限的边缘设备上。
- **LUT 路线**：查找表方法以"空间换时间"，预先计算退化输入到恢复输出的映射并存储，推理时仅做表索引，**完全消除乘累加（MAC）运算**，延迟极低且硬件行为确定。
- **核心痛点**：
  - LUT 存储随输入维度指数增长（3D RGB LUT 为 $O(N^3)$），迅速超出片上 SRAM 容量。
  - 现有 RGB-LUT 方法为保持吞吐，需为 R/G/B 三通道**并行部署三份相同 LUT 与查表流水线**，造成大量冗余存储。
  - 若简单地在 YUV 空间只对亮度 Y 做 LUT、丢弃 UV 处理，则会产生**色彩失真与残留伪影**，恢复质量下降。
- **本文定位**：提出 Hybrid-LUT，一个 YUV 空间下的**非对称通道处理框架**，将 LUT 与滤波统一设计——Y 通道用 LUT 恢复纹理，UV 通道用轻量滤波保持色彩一致性。

## 2. 方法论

### 2.1 核心思想

- 利用 YUV 的**去相关特性**：Y 通道集中了绝大部分结构与亮度信息，U/V 动态范围低、空间细节少、频谱衰减快（论文用 PSD 分析验证：干净 Y 的高频能量显著高于 UV，而含噪 UV 的高频能量主要由随机噪声而非纹理构成）。
- 因此采用**非对称资源分配**：把存储与算力集中于 Y 通道，UV 仅做均值滤波，从而在同等吞吐下将 LUT 存储降至 RGB-LUT 的约 1/3。

### 2.2 上界分析（设计依据）

- 表 1（CBSD68, AWGN σ=15）：固定 Y 为 SRLUT 时，UV 由均值滤波换成 GT 仅提升 **0.75 dB**；固定 UV 为均值滤波时，Y 由 SRLUT 换成 GT 提升 **7.72 dB**。证明 Y 通道主导恢复质量。

### 2.3 关键结构

- **训练网络**：
  - 先做 YUV 跨通道处理（基于 DNLUT 的 inter-channel 模块，密集连接：1×4 conv + GELU、四个 dense block、1×1 conv + Tanh），再做非线性增益放大做能量归一化。
  - 8-bit Y 分解为 **4-bit MSB + 4-bit LSB** 两个分支，每分支含三个互补 LUT 单元。
  - 每个核采样模式对应一个六层 CNN：首层 1×3 卷积 → 四个 1×1 卷积（64 通道，ReLU）→ 1×1 卷积 + ReLU + Tanh。
- **转 LUT**：枚举 3/4 维输入的全部组合，将 CNN 输出存表；输入 [0,255] 以 **24 为采样间隔**均匀量化，输出量化为 8-bit 整数 [-127,127]；存储量为 $v^n$。
- **推理公式**：分支输出为各 LUT 在旋转集成下的平均——
  $\hat{y}_i=\frac{1}{N}\sum_{k=0}^{N}\frac{1}{M_k}\sum_{j=0}^{M_k}R_j^{-1}\big(\mathrm{LUT}_k(R_j(x_i))\big)$
  其中 $R_j$ 为第 $j$ 个 90° 旋转（前三种核组合用 4 个旋转，L-LUT 用 2 个），$N$ 为核数量；最终输出使用 4D simplex 插值、1D 线性插值与 softmax 以抑制索引伪影。
- **像素级加权融合**：
  - 用 5×5 滑窗计算局部方差 $\sigma^2$ 作为纹理复杂度指标，归一化后查一个轻量 **1-D LUT** 得到融合权重。
  - 高方差（纹理丰富）区域放大保边单元输出；低方差（平坦）区域优先强去噪单元，从而在去噪强度与细节保持间自适应平衡，克服静态、内容无关的核堆叠导致的过度平滑。
- **互补核设计（位平面感知）**：
  - 四种 3 像素核组合，借旋转与膨胀获得不同感受野：**HD-LUT**（5×5，水平/对角）、**HDBLRC-LUT**（d=1，六核，9×9）、**HDBL-LUT**（d=2，四核，13×13）、**L-LUT**（3×3 单 L 形核）。
  - **MSB 分支**（承载主要结构，自相关曲线宽缓、存在长程依赖）：HD + HDBLRC + HDBL，侧重结构去噪与大范围颜色一致性。
  - **LSB 分支**（近乎被量化残差淹没，自相关呈脉冲状、无长程依赖）：HD + HDBLRC + L-LUT，侧重像素级高频细节精修。
  - 最终配置为两阶段级联残差结构；Y 输出与 UV 均值滤波结果融合后转回 RGB。

## 3. 实验设计

- **数据集与场景**：
  - 训练集：**DIV2K**。
  - 合成噪声测试：**CBSD68、Kodak24、Urban100、McMaster**，AWGN σ = 15/25/50。
  - 真实噪声：**SIDD** 训练集训练，**SIDD 验证集**与 **DnD** 评测（DnD 仅在线提供 PSNR）。
- **评价指标**：CPSNR（颜色 PSNR）与 SSIM；验证阶段用 Y-PSNR 监控。
- **对比基线**：
  - LUT 类：SRLUT、BDLUT、MuLUT、RCLUT、SPFLUT、DNLUT（当前 SOTA）。
  - 传统方法：CBM3D、MCWNNM。
  - DNN 类：DnCNN、SwinIR。
- **消融实验**：
  - 通道架构：YUV 非对称（Y-LUT + UV 均值滤波）vs 纯 RGB-LUT vs YUV 对称（三通道全 LUT）。
  - 融合权重：固定平均 / 可学习 per-tensor / per-row / pixel-wise。
  - LUT 单元组合：5 种 MSB–LSB 配置（278 KB ~ 446 KB）。
- **效率评估**：在 **Samsung Exynos 1580** 移动平台测 256×256 与 512×512 的运行时与能耗（能耗按 MAC 数估算，参考 AdderSR）。

## 4. 资源与算力

- 文中明确提到：**Nvidia RTX 3090 GPU** 训练，**200K 次迭代**，batch size 16，Adam 优化器（β₁=0.9, β₂=0.999, ε=1e-8），MSE 损失（仅 Y 通道），余弦退火学习率 1e-4 → 5e-5，随机裁剪 48×48 图像块并做旋转/翻转增强。
- **未明确说明**：GPU 数量、总训练墙钟时长、单次实验的完整能耗开销。
- 硬件部署方面仅给出移动端 CPU（Java API）实测，**FPGA/ASIC 实测结果缺失**，论文只称"可进一步通过 FPGA 获得收益"。

## 5. 实验数量与充分性

- **规模**：4 个合成噪声数据集 × 3 个噪声等级 + 2 个真实噪声数据集；对比 10 个基线方法；3 组消融（共约 12 个配置）；1 组移动端效率对比。整体覆盖面较广。
- **充分性评价**：
  - 优点：消融维度设计有层次（架构 / 融合粒度 / 核组合），且给出存储–性能权衡曲线（421 KB 配置优于 446 KB 配置）。
  - 局限：
    - 消融实验基本只在 **σ=15** 下进行，未覆盖 σ=25/50 与真实噪声，泛化性证据不足。
    - 缺少对 **UV 滤波核选择**的消融（为何是均值滤波而非引导滤波/双边滤波等轻量替代）。
    - 缺少 **MSB/LSB 位宽分解（4+4 vs 8-bit vs 5+3）** 的对比。
    - 表 1 的上界分析仅在 CBSD68 单一数据集上给出。
- **公平性**：
  - 与 LUT 基线在同一评测协议下比较，相对公平；但存储对比存在**口径差异**（模型大小 KB vs 硬件物理内存 MB），跨方法直接对比需谨慎。
  - 效率
