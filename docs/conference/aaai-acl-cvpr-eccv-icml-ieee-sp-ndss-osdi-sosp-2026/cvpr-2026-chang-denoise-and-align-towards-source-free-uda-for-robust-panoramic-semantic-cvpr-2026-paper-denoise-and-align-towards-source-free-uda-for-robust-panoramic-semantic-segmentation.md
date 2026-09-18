---
title: "Denoise and Align: Towards Source-Free UDA for Robust Panoramic Semantic Segmentation"
title_zh: 去噪与对齐：面向鲁棒全景语义分割的无源域无监督域适应
authors: "Chang, Yaowen, Cao, Zhen, Zheng, Xu, Mi, Xiaoxin, Dong, Zhen"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Chang_Denoise_and_Align_Towards_Source-Free_UDA_for_Robust_Panoramic_Semantic_CVPR_2026_paper.pdf"
tags: ["query:seg"]
score: 5.0
evidence: 面向全景语义分割的无源域无监督域适应
tldr: 全景语义分割对360度场景理解至关重要，但全景投影的严重几何畸变与密集标注成本限制了进展，且无源域无监督域适应约束放大了域偏移与伪标签噪声。本文提出去噪与对齐策略以缓解这些问题，提升伪标签可靠性与分割鲁棒性。该工作属于语义分割领域的域适应分支，与面向虚化的人像分割需求关联较弱。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 608, \"height\": 404}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 613, \"height\": 442}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 615, \"height\": 435}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 2809, \"height\": 554}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 399, \"height\": 311}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 399, \"height\": 309}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 609, \"height\": 407}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 610, \"height\": 417}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 613, \"height\": 420}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 610, \"height\": 416}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 610, \"height\": 508}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 3, \"index\": 16, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 3, \"index\": 17, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 3, \"index\": 18, \"width\": 3580, \"height\": 317}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 4, \"index\": 19, \"width\": 1632, \"height\": 1026}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 4, \"index\": 20, \"width\": 1632, \"height\": 1026}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 4, \"index\": 21, \"width\": 1632, \"height\": 1026}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 4, \"index\": 22, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 4, \"index\": 23, \"width\": 1024, \"height\": 200}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 4, \"index\": 24, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 4, \"index\": 25, \"width\": 1024, \"height\": 200}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 4, \"index\": 26, \"width\": 1024, \"height\": 200}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 4, \"index\": 27, \"width\": 1024, \"height\": 200}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 4, \"index\": 28, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 4, \"index\": 29, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 6, \"index\": 30, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 6, \"index\": 31, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 6, \"index\": 32, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 6, \"index\": 33, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 6, \"index\": 34, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 6, \"index\": 35, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 6, \"index\": 36, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 6, \"index\": 37, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 6, \"index\": 38, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 6, \"index\": 39, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 6, \"index\": 40, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 6, \"index\": 41, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 6, \"index\": 42, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 6, \"index\": 43, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 6, \"index\": 44, \"width\": 2048, \"height\": 400}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 7, \"index\": 45, \"width\": 4096, \"height\": 1408}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 7, \"index\": 46, \"width\": 4096, \"height\": 1408}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 7, \"index\": 47, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 7, \"index\": 48, \"width\": 4096, \"height\": 1408}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 7, \"index\": 49, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 7, \"index\": 50, \"width\": 4096, \"height\": 1408}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 7, \"index\": 51, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 7, \"index\": 52, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 7, \"index\": 53, \"width\": 4096, \"height\": 1408}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 7, \"index\": 54, \"width\": 4096, \"height\": 2048}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 7, \"index\": 55, \"width\": 4096, \"height\": 1408}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-chang-denoise-and-align-towards-source-free-uda-for-robust-panoramic-semantic-cvpr-2026-paper/fig-056.webp\", \"caption\": \"\", \"page\": 7, \"index\": 56, \"width\": 4096, \"height\": 2048}]"
motivation: 全景语义分割受几何畸变与标注昂贵限制，无源域适应下域偏移与伪标签噪声更严重。
method: 提出去噪与对齐相结合的无源域无监督域适应框架，提升伪标签可靠性与跨域鲁棒性。
result: 实验表明该方法缓解了域偏移，改善了全景语义分割在无源数据下的性能。
conclusion: 该工作推进了全景语义分割的域适应研究，但与虚化人像分割需求关联有限。
---

## Abstract
Panoramic semantic segmentation is pivotal for comprehensive 360deg scene understanding in critical applications like autonomous driving and virtual reality. However, progress in this domain is constrained by two key challenges: the severe geometric distortions inherent in panoramic projections and the prohibitive cost of dense annotation. While Unsupervised Domain Adaptation (UDA) from label-rich pinhole-camera datasets offers a viable alternative, many real-world tasks impose a stricter source-free (SFUDA) constraint where source data is inaccessible for privacy or proprietary reasons. This constraint significantly amplifies the core problems of domain shift, leading to unreliable pseudo-labels and dramatic performance degradation, particularly for minority classes. To overcome these limitations, we propose the DAPASS framework. DAPASS introduces two synergistic modules to robustly transfer knowledge without source data. First, our Panoramic Confidence-Guided Denoising (PCGD) module generates high-fidelity, class-balanced pseudo-labels by enforcing perturbation consistency and incorporating neighborhood-level confidence to filter noise. Second, a Contextual Resolution Adversarial Module (CRAM) explicitly addresses scale variance and distortion by adversarially aligning fine-grained details from high-resolution crops with global semantics from low-resolution contexts. DAPASS achieves state-of-the-art performances on outdoor (Cityscapes-to-DensePASS) and indoor (Stanford2D3D) benchmarks, yielding 55.04% (+2.05%) and 70.38% (+1.54%) mIoU, respectively.

---

## 论文详细总结（自动生成）

# 论文总结：Denoise and Align: Towards Source-Free UDA for Robust Panoramic Semantic Segmentation

## 1. 核心问题与整体含义
- **研究背景**：360° 全景语义分割对自动驾驶、VR/AR 等场景理解很重要，但面临两个核心挑战：
  - 全景图像经等距柱状投影（ERP）后存在严重几何畸变，尤其是极区拉伸、赤道相对稳定。
  - 像素级全景标注成本极高，数据稀缺。
- **问题设定**：利用标注丰富的针孔图像域进行无监督域适应（UDA）是一种替代方案，但很多真实任务有隐私、版权或存储限制，无法访问源域数据，因此需要更严格的**无源域无监督域适应（SFUDA）**。
- **核心困难**：SFUDA 下域偏移被放大，自训练伪标签不可靠，且源域类别分布长尾会导致少数类在目标域性能显著下降。
- **整体含义**：论文提出 **DAPASS** 框架，希望在无源数据条件下，将针孔图像预训练模型稳健迁移到全景语义分割任务，同时缓解伪标签噪声、全景畸变、尺度变化和类别不平衡。

## 2. 方法论
### 2.1 核心思想
- DAPASS 由两个协同模块组成：
  - **PCGD：Panoramic Confidence-Guided Denoising**，用于生成高质量、类别更均衡的伪标签，抑制噪声监督。
  - **CRAM：Cross-Resolution Attention Module**，通过高分辨率局部细节与低分辨率全局上下文的多分辨率融合，应对全景畸变和尺度变化。
- 整体目标：仅有预训练源模型 \(F_S\) 和无标注目标全景数据 \(D_T\)，适应得到目标模型 \(F_T\)。

### 2.2 PCGD：全景置信度引导去噪
- **一致性/不一致集合划分**：
  - 对目标图像进行扰动预测，计算一致性分数 \(CS\)。
  - 公式核心为负 KL 散度：比较初始源模型参数 \(\Theta^0\) 与自训练后参数 \(\Theta^\tau\) 的预测差异。
  - \(CS\) 越高表示预测越稳定。按 Top-P% 划分：
    - 一致集合 \(D_T^c\)：较可靠样本。
    - 不一致集合 \(D_T^{ic}\)：噪声较大样本。
- **Path A：双层邻居去噪**：
  - 对每个不一致样本 \(x_i \in D_T^{ic}\)，在特征空间检索最相似的一致样本 \(x_j \in D_T^c\)。
  - 使用双层优化：
    - 内层：用 \(x_i\) 的伪标签更新一次模型参数。
    - 外层：检查该更新是否也能改善稳定邻居 \(x_j\) 的预测，只有满足才认为更新可靠。
  - 目的：防止噪声样本直接污染模型。
- **Path B：类别均衡 Copy-Paste**：
  - 构建每个类别的 Top-K 高质量一致样本池 \(D_{Tca}^c\)，尤其针对少数类。
  - 通过 copy-paste 将少数类目标粘贴到其他样本中，增加稀有类别监督。
  - 若检索到的稳定邻居缺少某些类别，则从类别池中借用并粘贴补偿。
  - 对应损失为 \(L_{bal}\)，与 Path A 共同更新模型。
- **算法流程简述**：
  1. 计算所有目标样本一致性分数并划分一致/不一致集合。
  2. 构建每类 Top-K 池。
  3. 每轮训练中执行 Path A 邻居去噪。
  4. 执行 Path B 类别均衡 copy-paste。
  5. 返回适应后的目标模型。

### 2.3 CRAM：跨分辨率注意力模块
- **动机**：ERP 全景图像存在纬度相关畸变，局部细节和全局上下文需要互补。
- **双分支设计**：
  - **LR context 分支**：从高分辨率目标图像裁剪区域并下采样，获得低分辨率全局上下文。
  - **HR detail 分支**：从 LR context crop 中再随机裁剪高分辨率细节区域。
- **多分辨率融合**：
  - LR 分支预测全局语义 \(\hat{y}_{LR}\)，HR 分支预测局部细节 \(\hat{y}_{HR}\)。
  - 用可学习的尺度注意力图 \(a_{LR}\) 决定融合时更信任 LR 还是 HR。
  - 注意力由 LR context 预测，经 sigmoid 限制到 [0,1]。
  - 在 HR 细节区域外，注意力置零，得到 masked attention \(a'_{LR}\)。
  - 融合公式文字说明：
    - 将 HR 预测零填充对齐到上采样后的 context 尺寸。
    - 最终融合预测 = 上采样后的 \((1-a'_{LR}) \odot \hat{y}_{LR}\) + 上采样后的 \(a'_{LR} \odot \hat{y}_{HR}\)。
- **损失**：
  - 联合训练融合预测和 HR 细节预测。
  - \(L_{CRAM}^T = (1-\lambda_d) L_{ce}(\hat{y}_{LR,F}, p_{LR,F}, q_{LR,F}) + \lambda_d L_{ce}(\hat{y}_{HR}, p_{HR}, q_{HR})\)。
  - 使用温度缩放交叉熵，温度 \(\tau\) 可锐化或平滑伪标签分布。
  - \(\lambda_d\) 平衡 LR 上下文与 HR 细节分支。

## 3. 实验设计
### 3.1 数据集与场景
- **Cityscapes-to-DensePASS（C-to-D，室外）**：
  - Cityscapes：2975 张训练图像，19 类，作为源域预训练数据。
  - DensePASS：2500 张全景图像，其中 100 张标注作为测试集；训练部分作为无标注目标域。
- **Stanford2D3D-pinhole-to-SPan（Spin-to-SPan，室内）**：
  - Stanford2D3D 针孔数据：70496 张，13 类。
  - SPan 全景数据：1413 张室内全景。
  - 实验只关注两个数据集共有的 8 个类别。
- **评价指标**：mIoU。

### 3.2 对比方法
- **Source-only 基线**：仅用源域针孔数据训练，不适应。
- **SFUDA 方法**：
  - SFDA、DATC、360SFUDA++ w/ b1、360SFUDA++ w/ b2。
- **UDA 方法作为参考**：
  - ECANet、P2PDA、SIM、PCS、DAFormer、Trans4PASS-T、DPPASS-T、DATR-S、PVT-S、Trans4PASS+、MPA 等。
- 对比时区分是否 source-free，SFUDA 方法为主要公平比较对象；UDA 方法可访问源数据，因此主要作为参考。

### 3.3 主要结果
- **C-to-D**：
  - DAPASS w/ b1：53.16% mIoU。
  - DAPASS w/ b2：55.04% mIoU。
  - 相比 360SFUDA++，分别提升 +2.97% 和 +2.05%。
  - 显著超过 SF
