---
title: "DiffDecompose: Layer-Wise Decomposition of Alpha-Composited Images via Diffusion Transformers"
title_zh: DiffDecompose：基于扩散Transformer的alpha合成图像逐层分解
authors: "Wang, Zitong, Zhao, Hang, Zhou, Qianyu, Lu, Xuequan, Li, Xiangtai, Yang, Hao, Yang, Bo, Song, Yiren"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DiffDecompose_Layer-Wise_Decomposition_of_Alpha-Composited_Images_via_Diffusion_Transformers_CVPR_2026_paper.pdf"
tags: ["query:matting"]
score: 6.0
evidence: 处理透明层遮挡的alpha合成图像分层分解
tldr: 现有图像分解方法因依赖掩码先验、假设目标静止且缺乏数据集，难以处理半透明或透明层的非线性遮挡。本文将alpha合成图像的分层分解定义为新任务，提出基于扩散Transformer的方法，并构建首个大规模高质量透明与半透明数据集AlphaBlend。实验表明该方法在层歧义、泛化与数据稀缺方面取得改进，对含透明物体的抠图与前景背景分离具有参考意义。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 505, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 1570, \"height\": 1310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 509, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 509, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 1, \"index\": 16, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 4, \"index\": 17, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 4, \"index\": 18, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 4, \"index\": 19, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 4, \"index\": 20, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 4, \"index\": 21, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 4, \"index\": 22, \"width\": 1536, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 4, \"index\": 23, \"width\": 481, \"height\": 492}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 5, \"index\": 24, \"width\": 1889, \"height\": 979}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 6, \"index\": 25, \"width\": 4650, \"height\": 1436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 6, \"index\": 26, \"width\": 4745, \"height\": 3251}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 916, \"height\": 584}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 3634, \"height\": 1672}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 3645, \"height\": 1111}]"
motivation: 现有分解方法依赖掩码先验且缺乏数据，难以处理半透明或透明层的非线性遮挡。
method: 提出基于扩散Transformer的逐层分解方法，并构建大规模透明与半透明数据集AlphaBlend。
result: 实验表明该方法在层歧义、泛化与数据稀缺问题上取得改进。
conclusion: 该工作为透明物体场景的前景背景分离与抠图提供了新任务与方法基础。
---

## Abstract
Diffusion models have recently motivated great success in many generation tasks like object removal. Nevertheless, existing image decomposition methods struggle to disentangle semi-transparent or transparent layer occlusions due to mask prior dependencies, static object assumptions, and the lack of datasets. In this paper, we delve into a novel task: Layer-Wise Decomposition of Alpha-Composited Images, aiming to recover constituent layers from single overlapped images under the condition of semi-transparent/transparent alpha layer non-linear occlusion. To address challenges in layer ambiguity, generalization, and data scarcity, we first introduce AlphaBlend, the first large-scale and high-quality dataset for transparent and semi-transparent layer decomposition, containing six subtasks with different characteristics (e.g., translucent flare removal, semi-transparent cell decomposition, glassware decomposition). Building on this dataset, we present DiffDecompose, a diffusion Transformer-based framework that learns the posterior over possible layer decompositions conditioned on the input image, semantic prompts, and blending type. Rather than regressing alpha mattes directly, DiffDecompose performs In-Context Decomposition, enabling the model to predict one or multiple layers without per-layer supervision, and introduces Layer Position Encoding Cloning to maintain pixel-level correspondence across layers. Extensive experiments on the proposed AlphaBlend dataset and public LOGO dataset verify the effectiveness of DiffDecompose. Code will be publicly available at https://github.com/Wangzt1121/DiffDecompose.

---

## 论文详细总结（自动生成）

# DiffDecompose 论文中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **研究动机**：扩散模型虽在图像生成/编辑（如图像修复、目标移除）上取得巨大成功，但现有图像分解方法在处理**半透明/透明层的非线性遮挡**时表现不佳，根源在于三点：
  - **依赖掩码先验**：基于掩码的修复方法（mask-based inpainting）需要精确掩码，对需要全图级掩码的场景（如眩光、雨雾、水印）完全失效。
  - **静态物体假设**：既有工作多针对不透明/实体物体，将合成简化为像素叠加，忽视了透明玻璃、半透明细胞等**非线性混合**（如 alpha blending、screen mode、加性混合）。
  - **数据集稀缺**：现有数据集多为 AI 生成，其重叠图像与初始前景/背景存在像素级差异，导致逐层分解失败。
- **整体含义**：论文提出一个全新生成式任务——**Alpha 合成图像的逐层分解（LDAC, Layer-Wise Decomposition of Alpha-Composited Images）**，目标是在无任何掩码先验条件下，从单张重叠图像中直接恢复出背景层与带 alpha 的前景层。
- **本质难点**：LDAC 是一个**病态逆问题**（ill-posed）——由于颜色与透明度在层间纠缠，同一合成图通常存在多个合理分解解；前景与背景占据同一视觉平面，缺乏深度或边缘对比来区分。

## 2. 方法论：核心思想与关键技术

### 核心思想
- 将 LDAC 重新表述为**概率生成问题**：学习给定观测图像 z、语义提示 τ 条件下的前景-背景联合后验分布，而非直接回归 alpha matte。
- 公式化表达：
  - 合成过程：`z = G(x, y)`，其中 x 为 RGBA 前景，y 为 RGB 背景，G 可为 alpha blending、加性、screen 等。
  - 分解目标：训练条件扩散模型学习 `p_θ(x, y | z, τ) = ∫ p(x, y | z₀) p_θ(z₀ | z, τ) dz₀`。
- 与掩码修复的对比：掩码修复只需预测被掩码区域的像素，而 LDAC 需同时联合预测前景与背景，保持语义一致性与组合一致性。

### 关键技术与流程
- **框架总览（两阶段）**：
  1. 在 AlphaBlend 数据集上**微调 AlphaVAE**，获得提取 RGBA 特征的能力。
  2. 用预训练 AlphaVAE 分别编码前景 x、背景 y、合成图 z，得到潜在空间特征；文本提示经冻结的 **T5XXL** 提取文本特征；通过 ICD 完成分解。
- **In-Context Decomposition（ICD，上下文分解）**：
  - 将干净条件 token（z）与噪声 token（x、y）在序列维度拼接，利用**双向注意力**实现条件生成。
  - 使模型在**无逐层监督**的情况下预测单层或多层结果。
  - 保持 y 处于无噪声状态，以保留原图高频纹理与细节，防止迭代去噪中的退化。
- **Layer Position Encoding Cloning（LPEC，层位置编码克隆）**：
  - 从合成图 z 生成两个位置编码 PE 和 PE'，分别注入 x 和（y, z）的 token 表示：
    - `c̃_x = c_x + PE`，`c̃_y = c_y + PE'`，`c̃_z = c_z + PE'`
  - 让背景 y 与合成图 z 共享统一坐标系，保持相对位置结构 `c̃_y(i,j) - c̃_z(i,j) = c_y(i,j) - c_z(i,j)`。
  - 保持 `PE ⊥ PE'`（前景与背景位置空间正交），避免层间空间干扰与特征混合，增强解耦。
- **Multi-Modality Attention（MMA，多模态注意力）**：
  - 将 `[c̃_z; c̃_x; c̃_y; c_T]` 拼接后做联合注意力：`MMA = softmax(QKᵀ/√d)V`。
  - 干净 token（z）引导噪声 token（x、y）的生成，噪声 token 又依据上下文条件被细化，保证生成层与输入条件的语义一致性。
- **文本提示设计**：描述包含前景、背景及二者合成关系（如 "Three sub-images. <image-1>: a transparent glass, <image-2>: a dinning room with some chairs, <image-3>: The overlapped of <image-1> and <image-2>."），引导层间语义关系理解。

## 3. 实验设计

### 数据集与场景
- **AlphaBlend（自建，首个大规模高质量透明/半透明分解数据集）**，包含 6 个子任务：
  - Subtask I：半透明眩光去除（Translucent Flare Removal）
  - Subtask II：半透明遮挡去除（Translucent Occlusion Removal）
  - Subtask III：半透明水印去除（Semi-transparent Watermark Removal）
  - Subtask IV：透明玻璃器皿分解（Transparent Glassware Decomposition）
  - Subtask V：半透明细胞分解（Semi-transparent Cell Decomposition）
  - Subtask VI：X 射线违禁品分解（X-ray Contraband Decomposition）
  - 每个子任务约 5,000–10,000 张训练图、300–500 张测试图（主实验统一用 500 张测试图）。
  - 采用**任务特定的非线性混合算子**构造，如 X 射线 `I = (1−α)·B + α·(A_α/255 · B/255 · 255)`、玻璃器皿的折射式混合、水印/细胞的加性混合、雨雾的 screen 式混合等。
- **LOGO 公开数据集**：使用 LOGO-H、LOGO-L、LOGO-G 三个测试基准，评估前先做 5×5 核、5 次迭代的掩码膨胀以公平对比。

### 评估指标
- RMSE ↓、SSIM ↑、LPIPS ↓、FID ↓。

### 对比方法
- PowerPoint（任务提示词修复）、Flux-ControlNet、SDXL-inpainting、ClipAway、Inpaint Anything。

### 实验类型
- 主实验（跨 6 个 AlphaBlend 子任务 + 3 个 LOGO 基准的定量对比）
- 定性对比（图 5）
- 消融实验：AlphaBlend 数据集有效性（AlphaVAE 微调前后）、LPEC 有效性、ICD 有效性。

## 4. 资源与算力

- 论文明确提到的训练配置：
  - **AlphaVAE 微调**：以 AlphaVAE 参数初始化，用 AlphaBlend 前景训练 **30,000 步**。
  - **主模型微调**：引入 **LoRA（rank=128）** 微调 **Flux** 架构，**batch size = 1**，**学习率 1e-4**，在 **H20 GPU** 上训练 **30,000 步**。
- **未明确说明的部分**：
  - 未说明所用 H20 GPU 的**数量**（单卡或多卡）。
  - 未说明总训练时长（小时/天）、推理成本、模型参数量等。
  - 仅提及单次训练步数与硬件型号，算力信息相对有限。

## 5. 实验数量与充分性

- **实验组数概览**：
  - 主定量实验：2 大类数据集（AlphaBlend 6 个子任务 + LOGO 3 个基准），每个子任务/基准对比 5 个基线方法，共 9 个评估场景 × 4 个指标。
  - 消融实验：
    1. **AlphaBlend 有效性**（表 2）：在 X-ray、玻璃器皿、半透明遮挡、眩光 4 个子任务上对比 w/o AlphaBlend 与完整方法。
    2. **LPEC 有效性**（表 3）：同样在 4 个子任务上对比 w/o LPEC 与完整方法。
    3. **ICD 有效性**（图 7）：去除 ICD 后退化为普通图像修复，展示定性差异。
  - 定性实验：6 个子任务生成结果（图 4）、与 SOTA 的定性对比（图 5）、LPEC/ICD 消融可视化（图 7）、SDXL-inpainting 在不同强度下的失败案例（图 8）。
- **充分性与客观性评价**：
  - **较充分**：覆盖 6 个差异较大的真实子任务、公开数据集与自建数据集结合、多指标评估、消融覆盖三大核心模块。
  - **相对客观**：所有对比方法均在同一 benchmark 与指标下评估，并对 LOGO 统一做掩码膨胀预处理。
  - **潜在不足**：消融实验仅报告了部分子任务（4 个），未覆盖全部 6 个子任务；LOGO 上 FID 指标存在个别非最优情况（LOGO-L 上 FID 24.20 略高于 Inpaint Anything 的 23.71），论文对此作了解释（LOGO-L 布局结构化、对掩码友好），但公平性仍可进一步讨论。

## 6. 主要结论与发现

- **方法有效性**：DiffDecompose 在两个数据集上全面优于 SOTA，平均 RMSE 提升 **36.3%**、SSIM 提升 **+1.2%**、LPIPS 提升 **52.8%**。
- **复杂场景优势显著**：在 X 射线违禁品去除、半透明窗户遮挡等场景中，RMSE 可低至基线的 **1/4**，LPIPS 好 **3 倍**；在雨、光等全图级遮挡上大幅领先所有基线，且无需掩码。
- **AlphaBlend 数据集的作用**：微调 AlphaVAE 后，前景分解的颜色偏移与饱和度下降明显改善；图像级遮挡任务（Foggy 改善 9.47、glare 改善 24.99 RMSE）比目标级任务（0.39–0.87 RMSE）受益更大，说明 alpha 通道的颜色纠缠显著增加分解难度。
- **LPEC 的作用**：显著提升层间解耦，去除后透明玻璃与违禁品分解会出现信息纠缠（如人脸、车身颜色混杂）。
- **ICD 的作用**：去除 ICD 后框架退化为普通图像修复，无法同时输出前景与背景层。
- **总体结论**：LDAC 任务可行，DiffDecompose 能有效解耦半透明/透明层，为透明物体场景的前景-背景分离与抠图提供了新任务与方法基础。

## 7. 优点

- **任务新颖且定义清晰**：首次提出 LDAC 任务，将半透明/透明层分解从掩码修复范式转变为概率后验生成问题，物理上更合理。
- **数据集贡献突出**：AlphaBlend 是首个覆盖 6 类透明/半透明真实场景的大规模高质量数据集，采用任务特定的非线性混合算子构造，规模与多样性较好。
- **方法设计有针对性**：
  - ICD 实现无逐层监督的多层联合预测，突破传统逐层回归 alpha matte 的局限。
  - LPEC 通过位置编码正交化解决层间空间纠缠，思路简洁有效。
  - 保持背景噪声无关（noise-free），保留高频细节，缓解迭代去噪退化。
- **实验扎实**：同时使用自建数据集与公开 LOGO 数据集，指标全面（RMSE/SSIM/LPIPS/FID），并配有充分的可视化与失败案例分析（如图 8 展示 SDXL-inpainting 在全图层编辑上的失败）。
- **实际应用价值**：可推广至透明玻璃替换、X 射线安检、细胞显微分离、水印去除、眩光/雨雾去除等多个下游场景。

## 8. 不足与局限

- **算力信息不完整**：未说明 H20 GPU 数量、总训练时长、推理效率，难以评估方法的实际部署成本与可复现性。
- **病态问题的多解性未被充分探讨**：论文承认 LDAC 存在多个合理分解解，但未系统评估生成解的多样性、稳定性或不确定性度量，也未讨论如何保证生成的分解层与真实物理层一一对应。
- **依赖任务特定混合算子构造数据**：AlphaBlend 各子任务使用了人工定义的混合公式（如 screen、加性、折射式），可能与真实世界物理过程存在偏差，合成到真实的泛化性有待验证。
- **消融覆盖不完整**：消融实验仅覆盖 4 个子任务，未覆盖全部 6 个；对 MMA、AlphaVAE 微调步数等超参数的影响未做充分敏感性分析。
- **LOGO 上并非全面最优**：LOGO-L 的 FID 略逊于 Inpaint Anything（24.20 vs 23.71），说明在结构化、掩码友好的场景中方法优势会被削弱。
- **应用限制**：
  - 需要输入任务特定的语义提示（prompt），提示质量可能影响结果。
  - 仍依赖扩散模型的迭代采样，推理速度可能较慢。
  - 对极端透明/高度非线性混合（如多层玻璃叠加）的鲁棒性尚不清楚。
- **对比公平性**：基线方法（如 SDXL-inpainting、Inpaint Anything）本质为掩码修复方法，与 LDAC 任务范式不同，在无掩码场景下的劣势部分源于任务设定差异，而非纯粹方法能力差距。

（完）
