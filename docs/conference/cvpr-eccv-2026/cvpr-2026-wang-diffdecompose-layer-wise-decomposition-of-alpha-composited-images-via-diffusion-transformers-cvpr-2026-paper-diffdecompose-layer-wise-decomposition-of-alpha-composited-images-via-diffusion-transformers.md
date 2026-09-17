---
title: "DiffDecompose: Layer-Wise Decomposition of Alpha-Composited Images via Diffusion Transformers"
title_zh: DiffDecompose：基于扩散Transformer的Alpha合成图像逐层分解
authors: "Wang, Zitong, Zhao, Hang, Zhou, Qianyu, Lu, Xuequan, Li, Xiangtai, Yang, Hao, Yang, Bo, Song, Yiren"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_DiffDecompose_Layer-Wise_Decomposition_of_Alpha-Composited_Images_via_Diffusion_Transformers_CVPR_2026_paper.pdf"
tags: ["query:matting"]
score: 6.0
evidence: 分离半透明与透明层遮挡
tldr: 针对现有图像分解方法因掩码先验依赖、静态物体假设和数据匮乏而难以分离半透明或透明层遮挡的问题，本文提出Alpha合成图像逐层分解这一新任务，旨在从单张重叠图像中恢复各组成层。作者构建了首个大规模高质量透明/半透明数据集AlphaBlend，并利用扩散Transformer建模非线性遮挡下的层歧义。实验表明该方法能在透明遮挡场景下有效分解前景层，为真实世界的透明前景分离提供了新数据与生成式框架。
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 505, \"height\": 504}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 1024, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 500, \"height\": 500}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 1570, \"height\": 1310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 509, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 509, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 1, \"index\": 16, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 4, \"index\": 17, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 4, \"index\": 18, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 4, \"index\": 19, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 4, \"index\": 20, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 4, \"index\": 21, \"width\": 512, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 4, \"index\": 22, \"width\": 1536, \"height\": 512}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 4, \"index\": 23, \"width\": 481, \"height\": 492}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 5, \"index\": 24, \"width\": 1889, \"height\": 979}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 6, \"index\": 25, \"width\": 4650, \"height\": 1436}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 6, \"index\": 26, \"width\": 4745, \"height\": 3251}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 8, \"index\": 27, \"width\": 916, \"height\": 584}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 8, \"index\": 28, \"width\": 3634, \"height\": 1672}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-wang-diffdecompose-layer-wise-decomposition-of-alpha-composited-images-via-diffusion-transformers-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 8, \"index\": 29, \"width\": 3645, \"height\": 1111}]"
motivation: 现有图像分解方法受掩码先验依赖与静态假设限制，难以分离半透明或透明层的遮挡。
method: 提出Alpha合成图像逐层分解新任务，构建大规模透明/半透明数据集AlphaBlend，并采用扩散Transformer进行层分解。
result: 在透明与半透明非线性遮挡条件下从单张重叠图像恢复组成层，缓解层歧义与数据稀缺问题。
conclusion: 为透明/半透明前景分离提供了新任务设定、数据集与生成式方法。
---

## Abstract
Diffusion models have recently motivated great success in many generation tasks like object removal. Nevertheless, existing image decomposition methods struggle to disentangle semi-transparent or transparent layer occlusions due to mask prior dependencies, static object assumptions, and the lack of datasets. In this paper, we delve into a novel task: Layer-Wise Decomposition of Alpha-Composited Images, aiming to recover constituent layers from single overlapped images under the condition of semi-transparent/transparent alpha layer non-linear occlusion. To address challenges in layer ambiguity, generalization, and data scarcity, we first introduce AlphaBlend, the first large-scale and high-quality dataset for transparent and semi-transparent layer decomposition, containing six subtasks with different characteristics (e.g., translucent flare removal, semi-transparent cell decomposition, glassware decomposition). Building on this dataset, we present DiffDecompose, a diffusion Transformer-based framework that learns the posterior over possible layer decompositions conditioned on the input image, semantic prompts, and blending type. Rather than regressing alpha mattes directly, DiffDecompose performs In-Context Decomposition, enabling the model to predict one or multiple layers without per-layer supervision, and introduces Layer Position Encoding Cloning to maintain pixel-level correspondence across layers. Extensive experiments on the proposed AlphaBlend dataset and public LOGO dataset verify the effectiveness of DiffDecompose. Code will be publicly available at https://github.com/Wangzt1121/DiffDecompose.

---

## 论文详细总结（自动生成）

# DiffDecompose 论文结构化总结

## 1. 核心问题与研究动机

- **任务背景**：随着扩散模型在图像生成/编辑领域的成熟，*层级分解（layer-wise decomposition）* 因能提供对单个图层的细粒度控制而受到关注——目标是把一张图像拆解为前景物体、其 alpha 蒙版及潜在深度排序。
- **核心痛点**：现有方法在**半透明/透明场景**下失效，主要存在两大限制：
  - **图层级修复（layer-level inpainting）的局限**：基于掩码的方法（如 SDXL-inpainting、Inpaint Anything）只能处理目标级遮挡；对于**全图级掩码**（如眩光、雨雾、水印）完全无能为力。
  - **难以处理非线性图层**：已有工作多针对不透明/实体物体，将合成简化为像素叠加，忽略了透明玻璃、半透明细胞等**非线性混合**（颜色与透明度耦合）。
- **本文提出的新任务 LDAC（Layer-Wise Decomposition of Alpha-Composited Images）**：在**无掩码先验**条件下，从单张 Alpha 合成图中直接恢复背景层与 alpha 前景层。
- **任务的两大挑战**：
  - **图层歧义与颜色-透明度耦合**：前后景处于同一视觉平面，缺乏深度/边缘可分性，属严重病态问题。
  - **缺乏大规模数据集**：现有数据集（如 MULAN）多由 AI 生成，合成图与原始前景/背景存在像素级差异，导致分解失败。
- **整体含义**：为真实世界中透明/半透明前景分离提供**新任务设定 + 首个大规模数据集 + 生成式框架**，可支撑视频生成、场景理解等下游可编辑任务。

---

## 2. 方法论

### 2.1 核心思想

- 将分解问题从**直接回归 alpha matte** 重新表述为**学习合成层上的后验分布**，条件为：观测图像 $z$、语义提示 $t$、混合类型 $\tau$。
- 形式化定义：给定观测图 $z = \mathcal{G}(x, y)$（$x$ 为 RGBA 前景，$y$ 为 RGB 背景，$\mathcal{G}$ 为未知的混合算子），目标是恢复合理的 $(x, y)$ 使 $\mathcal{G}(x,y) \approx z$。
- 后验建模：$p_\theta(x, y \mid z, \tau) = \int p(x, y \mid z_0)\, p_\theta(z_0 \mid z, \tau)\, dz_0$。
- 对比传统 inpainting：$p_\theta(y \mid z, m) = \int p(y \mid z_0) p_\theta(z_0 \mid z, m) dz_0$，仅在掩码区域内预测像素，物理上不一致。

### 2.2 框架流程（DiffDecompose）

1. **AlphaVAE 微调**：先在 AlphaBlend 前景上微调 AlphaVAE（30k 步），获得提取 RGBA 特征的能力。
2. **编码阶段**：用微调后的 AlphaVAE 分别编码前景 $x$、背景 $y$、合成图 $z$ 为潜空间特征 $f_x, f_y, f_z$；提示经冻结的 T5-XXL 提取文本特征 $f_t$。
3. **分解阶段**：通过 **ICD** 拼接 $z$ 的干净条件 token 与 $x, y$ 的噪声 token，利用双向注意力实现条件生成。
4. **推理阶段**：观测图 $z$ 直接输入模型，输出分解结果 $x$ 与 $y$（无需掩码）。

### 2.3 两项关键技术

- **In-Context Decomposition (ICD)**：
  - 将图层分解视为**上下文感知的空间分离问题**，联合利用视觉潜表示（$f_x, f_y, f_z$）与文本潜表示（$f_t$）推断前后景的空间组织与语义一致性。
  - 通过拼接序列 `[˜c_z; ˜c_x; ˜c_y; c_T]` 进行联合注意力（MMA）：
    $\mathrm{MMA} = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d}}\right)V$。
  - 保持 $y$ 处于**无噪声状态**，保留原图高频纹理与细节，防止迭代去噪中的退化。
  - 支持**单层/多层预测**，无需逐层显式监督。

- **Layer Position Encoding Cloning (LPEC)**：
  - 从合成图 $z$ 生成两套位置编码 PE 与 PE'，注入到 token 表示：
    - $\tilde{c}_x = c_x + \mathrm{PE}$（前景）
    - $\tilde{c}_y = c_y + \mathrm{PE}'$，$\tilde{c}_z = c_z + \mathrm{PE}'$（背景与合成图共享坐标框架）
  - 通过 **PE ⊥ PE'** 使前景与背景保持**互不干扰的位置空间**，保持像素级对应、避免图层空间纠缠与特征混叠。

---

## 3. 实验设计

### 3.1 数据集 / 场景

- **AlphaBlend（本文自建）**：首个大规模高质量透明/半透明图层分解数据集，含 **6 个子任务**，每个子任务约 **5,000–10,000 训练图 + 500 测试图**：
  - Subtask I：Translucent Flare Removal（半透明眩光去除）
  - Subtask II：Translucent Occlusion Removal（半透明遮挡去除，如雨雾窗）
  - Subtask III：Semi-transparent Watermark Removal（半透明水印去除）
  - Subtask IV：Transparent Glassware Decomposition（透明玻璃器皿分解）
  - Subtask V：Semi-transparent Cell Decomposition（半透明细胞分解）
  - Subtask VI：X-ray Contraband Decomposition（X 光违禁品分解）
- 各子任务采用**任务特异的混合公式**（alpha blending、screen mode、加性、乘法/折射等），以捕捉非线性合成行为。
- **LOGO 公开数据集**：使用其三个测试基准 **LOGO-H / LOGO-L / LOGO-G**（水印去除），验证泛化性。

### 3.2 Benchmark 与评价指标

- 指标：**RMSE↓、SSIM↑、LPIPS↓、FID↓**。
- LOGO 评测前做掩码膨胀（5×5 kernel，5 次迭代）以减少边界伪影。

### 3.3 对比方法

- PowerPoint、Flux-ControlNet、SDXL-inpainting、ClipAway、Inpaint Anything 等 5 种 SOTA 修复类方法。

---

## 4. 资源与算力

- **GPU**：**单张 H20 GPU**。
- **训练配置**：
  - AlphaVAE 微调：30,000 步。
  - Flux + LoRA 微调：rank 128、batch size 1、学习率 $10^{-4}$、30,000 步。
- **说明**：论文未明确提及总训练时长、是否使用多卡或多次重复实验，也未报告推理速度/显存开销；算力规模披露较简略。

---

## 5. 实验数量与充分性

- **主要定量实验**：覆盖 **9 个 benchmark 单元**（LOGO 三子集 + AlphaBlend 六子任务），逐一对比 5 个基线。
- **消融实验**：
  - **AlphaBlend 数据集有效性**（AlphaVAE 微调前后），在 4 个子任务上报告前景指标。
  - **LPEC 有效性**，在 4 个子任务上报告背景指标。
  - **ICD 有效性**，通过图 7 定性展示。
- **定性对比**：图 4（六子任务）、图 5（与 SOTA 对比）、图 6（AlphaBlend 消融）、图 7（LPEC/ICD 消融）、图 8（SDXL-inpainting 失败案例）。
- **充分性评价**：
  - **优点**：任务覆盖面广（6 类真实场景 + 公开数据集），消融完整对应两大核心模块，指标齐全（4 类）。
  - **待商榷**：LOGO 结果中 FID 在 LOGO-L 上略逊于 Inpaint Anything（24.20 vs 23.71），作者解释为 LOGO-L 结构规整、对掩码友好，属"非掩码 vs 掩码"的方法性差异；但该解释缺乏更细致的误差分析支撑。
  - 未报告**运行时间、参数量、误差棒/多次重复**，公平性方面未明确说明基线超参调优细节。

---

## 6. 主要结论与发现

- DiffDecompose 在 AlphaBlend 与 LOGO 上**全面优于 SOTA 修复类方法**，平均提升约 **RMSE 36.3%、SSIM +1.2%、LPIPS 52.8%**。
- 在复杂场景（X 光违禁品、透明窗遮挡）中实现**最高 4× 更低 RMSE、3× 更好 LPIPS**。
- 对**全图级透明遮挡**（雨、光）无需掩码即可有效解耦，而所有基线严重失败。
- 关键发现：**alpha 通道中的颜色纠缠是 LDAC 的核心难点**——在全图级遮挡任务上，AlphaBlend 微调带来的提升（Foggy 提升 9.47，Glare 提升 24.99）远大于目标级任务（约 0.39–0.87）。
- 消融表明：LPEC 对图层信息对齐至关重要，去除后玻璃分解 RMSE 从 7.99 劣化至 24.60；ICD 缺失则退化为普通 inpainting。

---

## 7. 优点

- **任务创新**：首次提出 LDAC 任务，形式化地将图层分解建模为**条件后验生成**，突破掩码依赖与静态假设。
- **数据集贡献**：AlphaBlend 是**首个大规模透明/半透明分解数据集**，6 类真实场景覆盖安全、玻璃、生物、X 光等领域，混合公式贴合物理特性（如 X 光累积变暗、玻璃折射高光）。
- **技术设计精巧**：
  - **ICD** 支持无逐层监督的单/多层联合预测，泛化性强。
  - **LPEC** 通过前景与背景位置编码分离（PE ⊥ PE'）优雅地解决层间空间纠缠。
  - 保持背景 token **无噪声**，保留高频细节。
- **实验覆盖广**：6 子任务 + 公开数据集 + 多指标 + 多模块消融，定量与定性结合，失败案例分析（图 8）有说服力。
- **无掩码范式的实用价值**：对全图级退化（雨、雾、光）具备真实可用的鲁棒性。

---

## 8. 不足与局限

- **算力披露不完整**：仅提及单张 H20、30k 步，未给出训练时长、显存占用、推理成本，复现与效率评估信息不足。
- **实验严谨性**：
  - 未报告多次运行的**方差/误差棒**，统计显著性不明。
  - 基线超参、公平性设置（是否同等调优）描述不足。
  - LOGO-L 上 FID 落后，作者解释较为单薄。
- **数据偏差风险**：AlphaBlend 多为**合成数据**（前景 alpha + 自然 RGB 背景 + 人为混合公式），虽优于纯 AI 生成数据集，但可能与真实物理成像仍存在域差距；真实采集场景的泛化性未充分验证。
- **应用限制**：
  - 病态反问题本质导致**分解不唯一**，模型输出的是"合理"而非"真实"的层，存在多解风险。
  - 依赖语义提示与混合类型输入，任务提示设计对结果影响未做敏感性分析。
  - 六类子任务各自独立，**跨任务统一模型能力**与**未见混合类型**的泛化性有待进一步检验。
- **评测维度局限**：主要评估背景恢复质量（RMSE/SSIM/LPIPS），对**前景层本身（alpha 精度、透明度保真度）**的定量评估相对薄弱，缺少专门的 alpha matte 指标。

（完）
