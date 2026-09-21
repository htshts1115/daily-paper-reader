---
title: "There and Back Again: A Flexible-Frame Transformer for Multi-Exposure Fusion"
title_zh: 往复之间：面向多曝光融合的灵活帧数Transformer
authors: "Lishen Qu, Yao Liu, shihao zhou, Jie Liang, Hui Zeng, Lei Zhang, Jufeng Yang"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/8673.pdf"
tags: ["query:cv-render"]
score: 4.0
evidence: 多曝光融合，属于图像融合流水线
tldr: 针对多曝光融合中不同曝光帧数需分别部署模型、效率低的问题，论文提出FreeMEF——首个可变帧数Transformer融合框架。它无需重训练或改结构即可无缝适配任意数量输入曝光帧，从而统一建模宽动态范围场景。实验表明该方法在保持融合质量的同时提升了部署效率，为计算摄影中的图像融合提供灵活方案。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-001.webp\", \"caption\": \"\", \"page\": 6, \"index\": 1, \"width\": 4288, \"height\": 2848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 4288, \"height\": 2848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 4288, \"height\": 2848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-004.webp\", \"caption\": \"\", \"page\": 6, \"index\": 4, \"width\": 4288, \"height\": 2848}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-005.webp\", \"caption\": \"\", \"page\": 7, \"index\": 5, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-006.webp\", \"caption\": \"\", \"page\": 7, \"index\": 6, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-007.webp\", \"caption\": \"\", \"page\": 7, \"index\": 7, \"width\": 727, \"height\": 485}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-008.webp\", \"caption\": \"\", \"page\": 7, \"index\": 8, \"width\": 727, \"height\": 485}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-009.webp\", \"caption\": \"\", \"page\": 10, \"index\": 9, \"width\": 429, \"height\": 298}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-010.webp\", \"caption\": \"\", \"page\": 10, \"index\": 10, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-011.webp\", \"caption\": \"\", \"page\": 10, \"index\": 11, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-012.webp\", \"caption\": \"\", \"page\": 10, \"index\": 12, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-013.webp\", \"caption\": \"\", \"page\": 10, \"index\": 13, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-014.webp\", \"caption\": \"\", \"page\": 10, \"index\": 14, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-015.webp\", \"caption\": \"\", \"page\": 10, \"index\": 15, \"width\": 1264, \"height\": 854}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-016.webp\", \"caption\": \"\", \"page\": 10, \"index\": 16, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-017.webp\", \"caption\": \"\", \"page\": 10, \"index\": 17, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-018.webp\", \"caption\": \"\", \"page\": 10, \"index\": 18, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-019.webp\", \"caption\": \"\", \"page\": 10, \"index\": 19, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-020.webp\", \"caption\": \"\", \"page\": 10, \"index\": 20, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-021.webp\", \"caption\": \"\", \"page\": 10, \"index\": 21, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-022.webp\", \"caption\": \"\", \"page\": 10, \"index\": 22, \"width\": 430, \"height\": 298}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-023.webp\", \"caption\": \"\", \"page\": 10, \"index\": 23, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-024.webp\", \"caption\": \"\", \"page\": 10, \"index\": 24, \"width\": 430, \"height\": 297}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-025.webp\", \"caption\": \"\", \"page\": 10, \"index\": 25, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-026.webp\", \"caption\": \"\", \"page\": 10, \"index\": 26, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-027.webp\", \"caption\": \"\", \"page\": 10, \"index\": 27, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-028.webp\", \"caption\": \"\", \"page\": 10, \"index\": 28, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-029.webp\", \"caption\": \"\", \"page\": 10, \"index\": 29, \"width\": 1263, \"height\": 854}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-030.webp\", \"caption\": \"\", \"page\": 10, \"index\": 30, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-031.webp\", \"caption\": \"\", \"page\": 10, \"index\": 31, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-032.webp\", \"caption\": \"\", \"page\": 12, \"index\": 32, \"width\": 1493, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-033.webp\", \"caption\": \"\", \"page\": 12, \"index\": 33, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-034.webp\", \"caption\": \"\", \"page\": 12, \"index\": 34, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-035.webp\", \"caption\": \"\", \"page\": 12, \"index\": 35, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-036.webp\", \"caption\": \"\", \"page\": 12, \"index\": 36, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-037.webp\", \"caption\": \"\", \"page\": 12, \"index\": 37, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-038.webp\", \"caption\": \"\", \"page\": 12, \"index\": 38, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-039.webp\", \"caption\": \"\", \"page\": 12, \"index\": 39, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-040.webp\", \"caption\": \"\", \"page\": 12, \"index\": 40, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-041.webp\", \"caption\": \"\", \"page\": 12, \"index\": 41, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-042.webp\", \"caption\": \"\", \"page\": 12, \"index\": 42, \"width\": 1500, \"height\": 996}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-043.webp\", \"caption\": \"\", \"page\": 12, \"index\": 43, \"width\": 1493, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-044.webp\", \"caption\": \"\", \"page\": 12, \"index\": 44, \"width\": 1500, \"height\": 996}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-045.webp\", \"caption\": \"\", \"page\": 12, \"index\": 45, \"width\": 1500, \"height\": 996}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-046.webp\", \"caption\": \"\", \"page\": 12, \"index\": 46, \"width\": 1500, \"height\": 996}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-047.webp\", \"caption\": \"\", \"page\": 12, \"index\": 47, \"width\": 1500, \"height\": 996}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-048.webp\", \"caption\": \"\", \"page\": 12, \"index\": 48, \"width\": 1493, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-049.webp\", \"caption\": \"\", \"page\": 12, \"index\": 49, \"width\": 1493, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-050.webp\", \"caption\": \"\", \"page\": 12, \"index\": 50, \"width\": 1493, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-051.webp\", \"caption\": \"\", \"page\": 12, \"index\": 51, \"width\": 1493, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-052.webp\", \"caption\": \"\", \"page\": 12, \"index\": 52, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-053.webp\", \"caption\": \"\", \"page\": 12, \"index\": 53, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-054.webp\", \"caption\": \"\", \"page\": 12, \"index\": 54, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-055.webp\", \"caption\": \"\", \"page\": 13, \"index\": 55, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-056.webp\", \"caption\": \"\", \"page\": 13, \"index\": 56, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-057.webp\", \"caption\": \"\", \"page\": 13, \"index\": 57, \"width\": 727, \"height\": 484}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-058.webp\", \"caption\": \"\", \"page\": 13, \"index\": 58, \"width\": 727, \"height\": 484}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-059.webp\", \"caption\": \"\", \"page\": 13, \"index\": 59, \"width\": 727, \"height\": 484}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-060.webp\", \"caption\": \"\", \"page\": 13, \"index\": 60, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-061.webp\", \"caption\": \"\", \"page\": 14, \"index\": 61, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-062.webp\", \"caption\": \"\", \"page\": 14, \"index\": 62, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-063.webp\", \"caption\": \"\", \"page\": 14, \"index\": 63, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-064.webp\", \"caption\": \"\", \"page\": 14, \"index\": 64, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-065.webp\", \"caption\": \"\", \"page\": 14, \"index\": 65, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-066.webp\", \"caption\": \"\", \"page\": 14, \"index\": 66, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-067.webp\", \"caption\": \"\", \"page\": 14, \"index\": 67, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-068.webp\", \"caption\": \"\", \"page\": 14, \"index\": 68, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-069.webp\", \"caption\": \"\", \"page\": 15, \"index\": 69, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-070.webp\", \"caption\": \"\", \"page\": 15, \"index\": 70, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-071.webp\", \"caption\": \"\", \"page\": 15, \"index\": 71, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-072.webp\", \"caption\": \"\", \"page\": 15, \"index\": 72, \"width\": 1500, \"height\": 1000}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-9e7b962c1256459316735316/fig-073.webp\", \"caption\": \"\", \"page\": 15, \"index\": 73, \"width\": 1500, \"height\": 1000}]"
motivation: 传统多曝光融合方法固定输入帧数，不同帧数需求需维护多个模型，部署效率低下。
method: 提出FreeMEF，首个灵活帧数Transformer，可在不重训练和改结构情况下处理任意数量曝光输入。
result: 实验表明该方法在多种帧数设置下均能完成高质量多曝光融合，并提升部署效率。
conclusion: 为计算摄影图像融合提供了可灵活扩展的统一框架。
---

## Abstract
Multi-exposure fusion (MEF) brings the dynamic range ofconventional cameras closer to that of human vision, producing imageswith rich scene content. Given the large variability in scene luminance,exposure strategies often require different numbers of frames to capturethe full radiance range faithfully. However, conventional MEF techniquesare typically designed for a fixed number of inputs, forcing deploymentsystems to maintain separate models for different frame-count require-ments, which undermines deployment efficiency. To address this limita-tion, we propose FreeMEF, the first flexible-frame transformer for MEFthat seamlessly accommodates varying numbers of input exposures with-out retraining or architectural changes. The proposed approach consistsof two key modules. First, we introduce a recurrent state space mod-ule (RSSM) that sequentially fuses features from arbitrary sequencesvia adaptive alignment and state-space recurrent modeling, thereby pro-viding global information guidance for the subsequent restoration. Sec-ond, we devise a global feature guided block (GFGB) incorporating anextremity-aware hybrid attention (EAHA) and an affine-injection feed-forward network (AFFN), which effectively resolves the similarity para-dox while simultaneously optimizing contrast and brightness regulation.Extensive experiments on three benchmark datasets demonstrate the ef-fectiveness of our method, which performs favorably against state-of-the-art methods both quantitatively and qualitatively. The code is availableat https://github.com/qulishen/FreeMEF.

---

## 论文详细总结（自动生成）

# FreeMEF 论文总结：面向多曝光融合的灵活帧数 Transformer

## 1. 核心问题与整体含义（研究动机与背景）

- **任务背景**：高动态范围（HDR）成像是计算摄影的核心问题之一。单帧方法难以恢复已因饱和或欠曝而丢失的信息，因此多曝光融合（MEF）成为主流方案——在不同曝光值下拍摄多张 LDR 图像，直接融合为一张细节丰富的 HDR 风格图像（避免 CRF 标定与后续 tone-mapping 带来的伪影）。
- **问题一：固定输入帧数的架构约束**。现有学习型 MEF/HDR 方法普遍假设固定的曝光策略，网络结构针对 2、3 或 5 帧设计。当设备或拍摄模式改变帧数时，必须重新调整架构（如输入嵌入层通道维度）并重新训练，导致部署系统需维护多个模型，效率低下。
- **问题二：注意力机制中的“相似性悖论”（Similarity Paradox）**。HDR 成像的核心目标恰恰是恢复**过曝饱和区域**，而这些区域与正常曝光帧在像素级上相似度极低。标准 cross-attention 基于 Q–K 相似度匹配，会把低权重分配给最需要修复的区域，从而无法有效聚合互补信息。
- **问题三：既有注意力融合范式的缺陷**。（a）先融合再做 self-attention 易产生鬼影；（b）先 cross-attention 再融合的成对交互设计难以自然扩展到可变长度序列。
- **整体含义**：论文提出 **FreeMEF**——据称是首个“灵活帧数（flexible-frame）”MEF Transformer，训练与推理阶段均可接受任意数量的输入曝光帧，无需重新设计或重训练，从而在统一框架下兼顾融合质量与部署效率。

## 2. 方法论

### 2.1 核心思想

- **“There and Back Again”范式**：先通过循环机制把所有曝光帧特征**聚合为一个全局融合特征 H_T**，再将全局特征以 cross-attention 方式**回注（back）到基帧**上进行引导式复原，从而在概念上解耦“参考特征”与“基帧特征”。
- **总体流程**：RSSM 逐帧递归融合 → 得到全局融合特征 H_T → U 形 Transformer 编码器-解码器以基帧与 H_T 为输入，通过多尺度 GFGB 逐级精炼。

### 2.2 关键技术细节

**（1）特征提取（FEM）**
- 对每一帧 I_t 使用共享的轻量 FEM（两层 3×3 卷积 + ReLU）提取浅层特征 F_t，t ∈ {0,…,T}；I_0 为基帧，其余为辅助帧。

**（2）循环状态空间模块（RSSM）**
- **可变形对齐**：基于上一时刻隐状态 H_{t-1} 与当前特征 F_t 预测偏移量 ΔP_t（两层卷积 + LeakyReLU），用可变形卷积 DCN 将 F_t 对齐为 F̄_t，处理运动导致的错位。
- **ASE 全局建模**：输入特征经线性投影升维后拆分为数据分支 U_t 与门控分支 Z_t；数据分支经 SiLU + 深度卷积后送入**注意力状态空间方程（ASE）**。ASE 通过提示池 P = MN（M 为块特有系数矩阵、N 为共享基矩阵，秩 r ≪ min{N_p, d}），并用 Gumbel-Softmax 生成可微 one-hot 路由矩阵 R，得到实例相关提示 P = RP，将输出方程改写为 y_t = (C + P) h_t + D x_t，从而在因果状态历史中注入非因果的全局语义上下文。
- **隐状态更新**：用 sigmoid 门控 G_t = σ(W[H_t-1, Y_t]) 做残差式更新：H_t = H_{t-1} + G_t ⊙ (W_p([Y_t, H_{t-1}]) − H_{t-1})。该循环结构天然支持任意输入长度，且可自适应剔除冗余特征。

**（3）全局特征引导块（GFGB）= EAHA + AFFN**

- **极端感知混合注意力（EAHA）**：
  - 从基帧生成主查询 Q_base，从全局特征生成 K、V，并额外从全局特征生成**参考查询 Q_ref** 作为“回退搜索向量”。
  - 通过 E = σ(W_d^E F_0^l) 估计**极端图 E**（标记饱和像素），构造混合查询：Q_hybrid = (1−E) ⊙ Q_base + E ⊙ Q_ref。良好曝光区（E≈0）按基帧内容查询；饱和区（E≈1）切换为 Q_ref，利用历史自身的结构先验检索特征。
  - 沿通道维做注意力：Attention = V̂ · Softmax(K̂ᵀ Q̂_hybrid / α)，α 为可学习温度。数学上 K̂ᵀ Q̂_hybrid 等价于 self-attention 图与 cross-attention 图的加权和，**不增加额外计算开销**。
- **仿射注入前馈网络（AFFN）**：
  - 从全局历史 H_T^l 经全局平均池化 + 卷积拆分预测仿射参数 γ, β ∈ R^{1×1×C}。
  - 计算：X̂ = W_p²·Gating(X ⊙ (1+γ) + β)，其中 Gating(X) = GELU(W_d³W_p³(LN(X))) ⊙ W_d⁴W_p⁴(LN(X))。
  - 作用：显式地依据全局 HDR 亮度统计重新校准局部特征的对比度与亮度，缓解 LDR→HDR 的域偏移。

## 3. 实验设计

- **训练数据集**：
  - Kalantari et al. 数据集（每样本 3 帧 LDR + 1 张 HDR，HDR 经 tone-mapping 转 PNG）；
  - Real-HDRV 数据集（同样按 MEFLUT 的处理方式转换）。
  - 5 帧训练时，通过曝光模拟将 Kalantari 数据集从 3 帧扩展到 5 帧。
- **跨数据集测试 / Benchmark**：
  - 主实验：Kalantari 与 Real-HDRV 上以 3 帧训练、3 帧推理。
  - 泛化实验：Kalantari 上训练，在 **SICE 数据集**的 **2 帧 / 3 帧 / 5 帧**三个子集上测试，考察不同输入帧数下的泛化性。
- **评价指标**：PSNR ↑、SSIM ↑、LPIPS ↓，并报告 FLOPs（G）与参数量（M）。
- **对比方法（8 个 SOTA）**：
  - HDR 专用：HDR-Transformer（ECCV'22）、MEFLUT（ICCV'23）、SCTNet（ICCV'23）、SAFNet（ECCV'24）、AFUNet（ICCV'25）；
  - 通用图像复原：Restormer（CVPR'22）、MambaIRv2（CVPR'25）、ASTv2（TPAMI'25）。
  - 对固定 3 帧方法，最小化修改其输入嵌入层以适配 2/5 帧，其余结构不变；通用模型则调整初始嵌入通道维度后重新训练。
- **消融实验**：以 Restormer 的 CNN embedding、MDTA、GDFN 作为对照，替换 FreeMEF 的 RSSM、EAHA、AFFN，共 8 组配置（a–h），并保证各模块参数预算均衡。
- **融合顺序研究**：在 SICE 5 帧推理下比较 4 种融合顺序（暗→亮、亮→暗、相似曝光优先、差异大优先）。
- **定性对比**：Kalantari、Real-HDRV、SICE 上的可视化；EAHA/AFFN 的消融可视化；并行融合 vs. 递归融合的特征级对比；失败案例（颜色偏移）展示。
- **训练配置**：四阶段编码器-解码器 + 额外瓶颈阶段，dim = 32，各阶段块数 [2,2,2,2] + 2 个精炼块；patch 256×256，每 GPU batch size = 2，Adam 优化器，初始学习率 2×10⁻⁴，weight decay 0，β₁=0.9、β₂=0.999，Cosine Annealing Restart Cyclic 调度，共 300k 次迭代（两周期 92k + 208k），L1 损失。

## 4. 资源与算力

- **论文未明确披露 GPU 型号、数量与训练总时长**。文中仅给出：patch 尺寸 256×256、每 GPU batch size = 2、总迭代 300k、Adam 及学习率调度策略；致谢中提到使用了**南开大学超级计算中心（NKSC）**的算力，但未说明具体硬件规模。
- 效率指标方面，论文报告了 FreeMEF 的 FLOPs 为 **41.496 G**、参数量为 **8.900 M**，并称相比 AFUNet 与 HDR-Transformer 分别节省约 39% 与 56% 的计算量，参数量处于移动端可部署的合理范围。
- 结论：**算力开销信息不完整**，难以复现训练成本，也无法评估其训练能耗与碳足迹。

## 5. 实验数量与充分性

**实验规模概览：**
- 表 1：2 个数据集 × 8 个对比方法 + 本方法（3 帧设置），共约 9 组定量对比。
- 表 2：SICE 上 3 种帧数（2/3/5）× 8 个对比方法 + 本方法，共约 27 组定量结果。
- 表 3：8 组消融配置（单模块加入 a–d、单模块移除 e–h）。
- 表 4：4 种融合顺序的对比。
- 多组定性可视化（图 5、6、8、9、10）与特征级融合机制对比（图 7）。

**充分性与公平性评价：**
- **优点**：覆盖了同域（Kalantari、Real-HDRV）与跨域（SICE 2/3/5 帧）两类评测；对固定帧数基线做了“最小化适配 + 重训练”的处理，通用复原模型也重训以匹配输入帧数，比较相对公平；消融实验采用参数量预算均衡的对照模块，控制变量较严谨；额外考察了融合顺序这一实际部署中易被忽略的因素。
- **局限**：
  - 跨数据集泛化只在 SICE 一个数据集上验证，样本外场景有限；
  - 5 帧训练数据是通过**曝光模拟合成**的，与真实 5 帧采集存在域差异；
  - 未做真实噪声/低光条件下的鲁棒性测试，也未报告推理延迟（仅报告 FLOPs）；
  - 消融的对照模块全部取自 Restormer，缺乏与其他 SSM/注意力变体的横向对照。

## 6. 主要结论与发现

- **定量优势**：Kalantari 上 PSNR 达 28.418 dB，比第二名高 **1.192 dB**；Real-HDRV 上 26.077 dB，高出 **0.515 dB**；SSIM 与 LPIPS 亦全面领先。
- **跨帧数泛化**：在 SICE 的 2/3/5 帧测试中，PSNR 分别高出第二名 **1.748 / 0.657 / 1.116 dB**，在 2 帧与 5 帧场景提升尤为显著，说明递归融合 + 基帧/参考特征解耦能有效缓解固定输入方法在极端帧数下的信息压缩与丢失问题。
- **模块有效性**：RSSM、EAHA、AFFN 单独引入分别带来 **0.472 / 0.372 / 0.347 dB** 的 PSNR 增益；移除后分别下降 **0.526 / 0.581 / 0.397 dB**，三者协同（全模型）达到 28.418 dB。
- **融合机制**：并行融合在特征层面即引入严重鬼影，后续 self-attention 与 FFN 难以补救；递归式“往复”融合可显著抑制鬼影。
- **融合顺序**：暗→亮、相似曝光优先、差异大优先三种顺序表现稳健；**亮→暗顺序性能明显下降**，且将暗帧置于末端易引入噪声。建议把长曝光帧安排在融合流程末端。
- **失败模式**：当曝光级差过大（基帧过暗、长曝光帧严重饱和）时，融合结果相对 GT 存在**轻微色彩偏移**。

## 7. 优点

- **问题定位精准**：同时抓住“固定帧数架构”与“相似性悖论”两个真实且互补的痛点，动机清晰、切中实际部署需求。
- **方法设计巧妙**：
  - 以循环 + 状态空间建模替代并行融合，天然支持任意帧数，无需改架构或重训练；
  - EAHA 用可学习的极端图在 Q_base 与 Q_ref 间做空间门控，**在不增加计算量的前提下**等价实现 self-attention 与 cross-attention 的加权融合，直击饱和区域检索失效问题；
  - AFFN 将全局 HDR 亮度统计以仿射参数（γ, β）注入 FFN，显式处理 LDR→HDR 的亮度/对比度域偏移，思路借鉴自适应实例归一化但更贴合 HDR 任务。
- **效率与精度兼顾**：8.9 M 参数、41.5 G FLOPs，显著低于 AFUNet 与 HDR-Transformer，具备移动端部署潜力。
- **实验设计有加分项**：跨帧数泛化评测、融合顺序敏感性分析、特征级融合机制可视化对比，均超出常规 MEF 论文的评测范围。
- **可复现性**：公开代码仓库，训练超参数描述详尽。

## 8. 不足与局限

- **算力信息缺失**：未报告 GPU 型号/数量、训练时长与总计算量，影响复现成本评估与公平性判断。
- **作者自陈的局限**：曝光级差过大时存在色彩偏移，源于基帧过暗与长曝光帧过饱和，颜色偏离真实场景。
- **实验覆盖不足**：
  - 跨数据集验证仅在 SICE 上进行，未在更多真实移动端 HDR 数据集（如该团队引用的 Real-HDRV 之外的场景）上验证泛化；
  - 5 帧训练样本为曝光模拟合成，真实 5 帧场景下的性能未充分证实；
  - 未评估真实噪声、动态大运动、夜间低光等困难条件下的鲁棒性；
  - 未报告推理延迟/显存占用，FLOPs 不足以反映移动端实际部署表现。
- **方法与实现风险**：
  - 融合顺序对性能有可观测影响（亮→暗顺序显著下降），但论文未给出自动排序或顺序不变性的解决方案，实际部署需依赖人工调度；
  - 递归结构本质上是串行的，随帧数增加推理延迟线性增长，论文未讨论帧数扩展时的时延代价；
  - 极端图 E 由单层卷积 + sigmoid 从基帧特征估计，其在复杂光照（如局部高光、彩色光源）下的可靠性未做专门验证。
- **对比公平性的潜在偏差**：固定帧数基线仅做“最小化适配 + 重训”，而 FreeMEF 受益于多帧训练带来的先验（论文自己也指出这是其在 2 帧场景占优的原因之一），因此 2 帧对比可能对基线不完全公平；此外，消融对照模块单一（均取自 Restormer），参数预算平衡但架构多样性有限。
- **应用限制**：参数量 8.9 M 在对比方法中偏大（高于 ASTv2 的 7.751 M、AFUNet 的 1.138 M），对极致轻量化的移动端场景可能仍是负担。

（完）
