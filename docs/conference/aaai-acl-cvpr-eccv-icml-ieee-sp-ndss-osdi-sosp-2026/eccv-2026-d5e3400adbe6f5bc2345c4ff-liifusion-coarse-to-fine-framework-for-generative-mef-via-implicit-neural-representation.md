---
title: "LIIFusion: Coarse-to-fine Framework for Generative MEF via Implicit Neural Representation"
title_zh: LIIFusion：基于隐式神经表示的由粗到细生成式多曝光融合框架
authors: "Sangmin Han, Jinho Kim, Jinwoo Kim, Dongyoung Kim, Seon Joo Kim"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/5205.pdf"
tags: ["query:cv-render"]
score: 4.0
evidence: 由粗到细的生成式多曝光融合框架
tldr: 多曝光融合需合并不同曝光的互补亮度信息，同时处理几何差异并补全缺失细节，而扩散类生成方法计算昂贵且难以保饱和区结构。作者提出LIIFusion由粗到细框架，在粗阶段做低分辨率生成式融合并结合自适应曝光校正恢复结构。该框架平衡了融合质量与效率。虽面向曝光融合，其融合与生成思路对移动摄影图像融合具参考价值。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 520, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 523, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 523, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-004.webp\", \"caption\": \"\", \"page\": 10, \"index\": 4, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-005.webp\", \"caption\": \"\", \"page\": 10, \"index\": 5, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-006.webp\", \"caption\": \"\", \"page\": 10, \"index\": 6, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-007.webp\", \"caption\": \"\", \"page\": 10, \"index\": 7, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-008.webp\", \"caption\": \"\", \"page\": 10, \"index\": 8, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-009.webp\", \"caption\": \"\", \"page\": 10, \"index\": 9, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-010.webp\", \"caption\": \"\", \"page\": 10, \"index\": 10, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-011.webp\", \"caption\": \"\", \"page\": 10, \"index\": 11, \"width\": 572, \"height\": 381}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-012.webp\", \"caption\": \"\", \"page\": 10, \"index\": 12, \"width\": 566, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-013.webp\", \"caption\": \"\", \"page\": 10, \"index\": 13, \"width\": 566, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-014.webp\", \"caption\": \"\", \"page\": 10, \"index\": 14, \"width\": 567, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-015.webp\", \"caption\": \"\", \"page\": 10, \"index\": 15, \"width\": 566, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-016.webp\", \"caption\": \"\", \"page\": 10, \"index\": 16, \"width\": 567, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-017.webp\", \"caption\": \"\", \"page\": 10, \"index\": 17, \"width\": 566, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-018.webp\", \"caption\": \"\", \"page\": 10, \"index\": 18, \"width\": 567, \"height\": 378}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-019.webp\", \"caption\": \"\", \"page\": 10, \"index\": 19, \"width\": 566, \"height\": 377}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-020.webp\", \"caption\": \"\", \"page\": 12, \"index\": 20, \"width\": 412, \"height\": 306}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-021.webp\", \"caption\": \"\", \"page\": 12, \"index\": 21, \"width\": 413, \"height\": 306}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-022.webp\", \"caption\": \"\", \"page\": 12, \"index\": 22, \"width\": 411, \"height\": 306}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-023.webp\", \"caption\": \"\", \"page\": 12, \"index\": 23, \"width\": 411, \"height\": 306}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-024.webp\", \"caption\": \"\", \"page\": 12, \"index\": 24, \"width\": 413, \"height\": 306}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-025.webp\", \"caption\": \"\", \"page\": 12, \"index\": 25, \"width\": 412, \"height\": 306}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-026.webp\", \"caption\": \"\", \"page\": 13, \"index\": 26, \"width\": 960, \"height\": 640}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-027.webp\", \"caption\": \"\", \"page\": 13, \"index\": 27, \"width\": 959, \"height\": 642}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-028.webp\", \"caption\": \"\", \"page\": 13, \"index\": 28, \"width\": 960, \"height\": 640}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-029.webp\", \"caption\": \"\", \"page\": 13, \"index\": 29, \"width\": 959, \"height\": 642}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-030.webp\", \"caption\": \"\", \"page\": 13, \"index\": 30, \"width\": 960, \"height\": 640}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d5e3400adbe6f5bc2345c4ff/fig-031.webp\", \"caption\": \"\", \"page\": 13, \"index\": 31, \"width\": 960, \"height\": 640}]"
motivation: 多曝光融合需处理几何差异与细节缺失，扩散类生成方法计算昂贵且难保饱和区域结构。
method: 提出LIIFusion由粗到细框架，粗阶段做低分辨率生成式融合并配合自适应曝光校正恢复结构，采用隐式神经表示。
result: 该框架在融合质量与计算效率间取得平衡，更好地保留饱和区与精细结构。
conclusion: 工作为生成式图像融合提供了高效方案，对移动摄影中的图像融合任务具借鉴意义。
---

## Abstract
Multi-exposure fusion (MEF) expands the luminance rangebeyond what a single exposure can capture. Combining images takenat different exposure levels requires handling geometric differences whilenaturally merging their complementary brightness information. It of-ten demands generative completion where details are missing. Diffusion-based generative methods address these challenges, however, they arecomputationally expensive and struggle to preserve fine structures in sat-urated regions. We propose LIIFusion, a coarse-to-fine framework thatbalances fusion quality and efficiency in generative MEF. The coarsestage performs low resolution generative fusion, enhanced by an adaptiveexposure correction that recovers structure lost in saturated over-exposedareas. The fine stage adapts a local implicit image function into a multi-exposure fusion function: conditioned on the HR OE/UE sources and thecoarse output, it queries arbitrary target coordinates and fuses sourceevidence regard- less of the HR input resolution. LIIFusion achieves upto 3.5× speed-up over existing generative methods while maintainingor improving structural fidelity and perceptual quality. We believe thisframework provides an effective pathway toward making generative MEFmore practical in real-world applications.

---

## 论文详细总结（自动生成）

# LIIFusion 论文详细总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：计算摄影中的核心难题是捕获高动态范围（HDR）场景。受限于标准传感器有限的动态范围，单次曝光往往无法覆盖场景的完整亮度范围，导致背景过曝或前景欠曝。多曝光融合（MEF）通过拍摄不同曝光水平的图像序列并合成一张高质量图像来缓解这一问题。
- **传统方法的局限**：
  - 早期手工方法依赖多尺度金字塔融合与对比度/饱和度/曝光度等低层启发式度量，易产生光晕，且缺乏语义感知能力。
  - 深度学习 MEF 方法提升了鲁棒性，但动态范围仍有限（约 3–4 档），在运动场景中易出现鬼影，在极端动态范围场景中大量区域饱和，需要生成式补全而非简单混合。
- **生成式 MEF 的挑战**：近期扩散模型方法（如 UltraFusion）将 MEF 重新表述为引导式修补任务，能有效抑制鬼影并合成饱和区域结构，但带来新权衡：
  - 计算昂贵：扩散模型在固定分辨率（如 512×512）下运行，高分辨率融合需按块（patch-wise）采样，耗时可达数小时。
  - 结构不确定：在饱和区域引导较弱时，纯生成式融合仍可能产生结构不确定或色调不稳定的结果。
- **论文目标**：提出 **LIIFusion**，一个由粗到细的生成式 MEF 框架，将低分辨率扩散先验与高分辨率隐式神经表示（INR）精修模块相协调，在融合质量与效率之间取得平衡。

## 2. 方法论：核心思想与关键技术细节

### 核心思想
将生成式 MEF 解耦为两个阶段：**全局潜在空间融合**（粗阶段，低分辨率扩散）与**局部 RGB 空间高分辨率证据融合**（细阶段，INR）。这不是简单的“扩散+超分”级联，而是针对 MEF 任务的特异性分解。

### 符号定义
- 高分辨率过曝/欠曝输入：$I_{oe}, I_{ue} \in \mathbb{R}^{H \times W \times 3}$
- 低分辨率对应：$I^{LR}_{oe}, I^{LR}_{ue} \in \mathbb{R}^{h \times w \times 3}$（双三次下采样，$H > h, W > w$）
- 生成式 MEF 模型 $g$ 产生粗融合图 $I^{LR}_{mef}$
- 最终输出：$I^{HR}_{mef} \in \mathbb{R}^{H \times W \times 3}$

### 粗阶段（Coarse Fusion）
- 以 **UltraFusion**（扩散式生成 MEF）为骨干先验，在降采样曝光对上执行低分辨率融合。
- 使用 RAFT 估计光流 $F_{oe \to ue}$，将 UE 图像变形对齐得到 $\tilde{I}_{ue}$，减少鬼影。
- 扩散模型在接近其预训练尺度上运行，仅需少量前向传播（最多 1–2 次），避免昂贵的按块采样：
  $$I^{LR}_{mef} = g(I^{LR}_{oe}, \tilde{I}^{LR}_{ue})$$

### 自适应曝光校正（Adaptive Exposure Correction, AEC）
- 动机：过曝输入严重饱和时，VAE 解码器中的保真度引导不可靠，低分辨率下更甚。
- **曝光差异估计**：转换到 LAB 空间取亮度通道，计算差异图
  $$L^{LR}_{diff} = \min(\max(L^{LR}_{oe} - L^{LR}_{ue}, 0), 1)$$
- **自适应亮度调整**：生成逐像素权重图并做 gamma 校正
  $$W = (1 - \alpha \cdot L^{LR}_{diff})^{1/2.2}$$
  $$I'^{LR}_{oe} = I^{LR}_{oe} \odot W$$
- 校正后的 $I'^{LR}_{oe}$ 替换原 OE 图像参与保真度引导。

### 细阶段（Fine Fusion）
- 将 **LIIF** 适配为多曝光条件融合函数，而非单图像超分解码器。
- 两个编码器：$E_{coarse}$ 编码粗融合图得 $f_{coarse}$；$E_{fine}$ 编码拼接的 HR 曝光对得 $f_{fine}$。
- 在任意查询坐标 $x$ 处对两个特征图做双线性插值，得到 $z_{coarse}, z_{fine}$，拼接后由轻量 MLP $f_\theta$ 解码：
  $$s = f_\theta([z_{coarse}, z_{fine}], [x, c])$$
  其中 $c$ 为 cell，表示查询像素的相对尺寸，使函数可适应不同输出分辨率。
- 因为函数在连续坐标上查询并直接以 HR OE/UE 为条件，同一学到的融合函数可整合任意分辨率 HR 输入的证据。
- **训练损失**：对真值 $I_{GT}$ 的 L1 损失
  $$\mathcal{L}_{fusion} = \|I^{HR}_{mef} - I_{GT}\|_1$$

### 实现细节
- $E_{fine}$ 接收每个目标像素周围 19×19 局部块（来自 $I_{oe}, I_{ue}$），实现为 4 层 CNN。
- $E_{coarse}$ 采用 SwinIR 骨干（遵循 LIIF 惯例）。
- Adam 优化器，学习率 $1 \times 10^{-4}$，批大小 16，训练 500 epoch。

## 3. 实验设计

### 数据集
- **训练**：从 **SICE** 数据集随机选取欠曝/过曝对；用 Vimeo-90K 提取的遮挡掩码乘到 UE 图像上模拟动态错位；SICE 标签数据作为真值并随机下采样得到三元组 $\{I_{oe}, I_{ue}, I^{LR}_{mef}\}$。
- **评估**：
  - **MEFB**：100 个静态曝光对
  - **UltraFusion Benchmark**：100 个真实拍摄的欠/过曝对，曝光差异更大
  - **RealHDRV**：50 个包含多样运动的动态场景

### 评价指标
- **MEF-SSIM**（结构感知融合指标）
- 四个无参考图像质量评估（NRIQA）指标：**MUSIQ、PAQ2PIQ、DeQA-Score、HyperIQA**
- 额外报告总推理时间、参数量、单图 FLOPs。

### 对比方法
- 传统/非生成式：**MEF-LUT、HSDS-MEF、U2Fusion、MEF-GAN、Defusion**

### 实验内容
- 动态数据集（RealHDRV）与 UltraFusion Benchmark 的定量对比（Tab. 2）
- 静态 MEFB 数据集对比（Tab. 3）
- FLOPs 与参数量对比（Tab. 4）
- 定性对比：超 HDR 场景（Fig. 3）与动态运动场景（Fig. 4）
- 消融实验：AEC 模块、LIIF vs LIIFusion、训练数据集（伪标签）、细融合的曝光输入策略
- 用户偏好研究（22 名参与者）
- 粗阶段不同分辨率的推理分析

## 4. 资源与算力

- **训练**：单张 **NVIDIA H100 GPU**，训练 500 epoch，完整收敛约需 **22 小时**。
- **推理测试**：单张 **NVIDIA RTX A5000**（部分分辨率分析实验用 H100）。
- 论文明确说明了 GPU 型号、训练时长与推理硬件，算力信息较为透明。

## 5. 实验数量与充分性

- **实验组数**：共约 10 组主要实验，覆盖 3 个评估数据集、多种指标、5 个以上对比方法，以及 5 组消融/分析实验（AEC、LIIF 适配、伪标签、曝光输入、分辨率），另含用户偏好研究。
- **充分性**：
  - 静态与动态场景均有覆盖，指标兼顾结构保真（MEF-SSIM）与感知质量（多个 NRIQA），维度较全面。
  - 消融设计针对性强：AEC 验证结构恢复作用，曝光输入消融（去掉/单独/组合 OE、UE）有力证明了模型确实在做多曝光融合而非单纯超分。
  - 伪标签实验探讨了数据可扩展性，具有额外价值。
- **公平性**：对比方法涵盖传统、深度学习和生成式各类，且同时报告时间/FLOPs/参数量，兼顾质量与效率维度，比较相对客观。
- **潜在偏差**：MEF 无唯一真值，主要依赖 NRIQA 指标，这类指标本身可能存在偏差；训练数据基于 SICE 并叠加合成遮挡掩码模拟运动，与真实动态场景仍有差距。

## 6. 主要结论与发现

- **效率**：LIIFusion 相比现有生成式方法（UltraFusion）实现最高 **3.5× 加速**（论文正文亦称推理时间约为其四分之一），FLOPs 减少超过 3 倍，同时参数量仅略增（1.872B vs 1.860B）。
- **质量**：在所有 NRIQA 指标上持续超越传统方法（MEF-LUT、HSDS-MEF 等），并达到或超过生成式基线 UltraFusion；MEF-SSIM 结构保真度也具竞争力。
- **AEC 的作用**：数值增益温和，但定性影响显著——能防止扩散模型在饱和区合成模糊/扭曲内容，保证粗阶段结构可靠。
- **LIIF 适配的必要性**：将 LIIF 用作融合模块（而非超分）在所有指标上均优于预训练 LIIF 和从零训练的 LIIF，证明“学习融合多曝光输入”比“简单上采样粗融合结果”更有效。
- **曝光输入贡献**：OE 贡献最大（亮区保留更多结构），UE 提供互补信息；二者与粗结果联合使用时融合最连贯。
- **用户偏好**：LIIFusion 获得最高最佳选择率（61.36%）和最佳平均排名（1.52），显著优于 UltraFusion（21.21%）。
- **可扩展性**：用 UltraFusion 生成的伪标签训练，性能与使用 SICE 人工标签几乎相当，表明强生成模型可作为可扩展的标签生成器。

## 7. 优点

- **任务特异性分解**：明确提出并非“扩散+超分”通用级联，而是将生成式 MEF 分解为全局潜在空间融合与局部 HR 证据融合，思路清晰。
- **首次将 INR 引入 MEF**：利用 LIIF 的连续坐标查询特性，实现分辨率无关的高分辨率细节融合，直接注入原始 HR 曝光证据。
- **AEC 模块设计巧妙**：简单而有效地在低分辨率、饱和区域为扩散模型提供可靠结构引导，解决了生成式融合的关键痛点。
- **效率与质量兼顾**：在保持甚至提升生成式质量的同时大幅降低计算成本，向实际部署迈进。
- **实验扎实**：消融全面，特别是曝光输入消融有力地论证了“真融合”而非“伪超分”；用户研究提供了主观质量证据。
- **数据可扩展性探讨**：伪标签实验为 MEF 数据集扩展提供了新思路。

## 8. 不足与局限

- **依赖粗阶段结构可靠性**：最终输出仍受粗生成阶段结构可靠性的影响；细阶段只能精修，无法重新诠释底层结构（如 Fig. 5 所示）。
- **速度仍非实时**：尽管大幅加速，仍慢于轻量方法（如 MEF-LUT，0.5 秒 vs 数分钟），限制实时应用场景。
- **极端场景残余伪影**：在极大遮挡或快速运动场景中，仍可能产生细微鬼影，需要更运动感知的生成机制。
- **评估偏差风险**：MEF 缺乏唯一真值，主要依赖 NRIQA 指标，可能存在感知评估偏差；训练用合成遮挡掩码模拟动态，与真实动态场景存在域差距。
- **粗阶段分辨率权衡**：提高粗分辨率可改善感知质量，但运行时间显著增加，因此采用固定粗分辨率，可能牺牲部分细节潜力。
- **参数量偏大**：虽然 FLOPs 大幅降低，但参数量（1.872B）仍远高于轻量方法，且略高于 UltraFusion，部署资源需求仍较高。
- **泛化性未充分验证**：仅在 SICE 训练、三个基准评估，跨域泛化能力（如不同相机、极端光照）尚待进一步验证。

（完）
