---
title: "BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching"
title_zh: BokehFlow：基于流匹配的免深度可控散景渲染
authors: "Yachuan Huang, Xianrui Luo, Qiwen Wang, Liao Shen, Jiaqi Li, Huiqiang Sun, Zihao Huang, Wei Jiang, Zhiguo Cao"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37431/41393"
tags: ["query:neural-bokeh"]
score: 9.0
evidence: 基于流匹配的可控散景渲染，直接合成逼真散景
tldr: 现有可控散景渲染方法大多依赖精确深度图，而生成式方法又受限于可控性和效率。本文提出BokehFlow，一种基于流匹配的免深度可控散景渲染框架，可直接从全焦图像合成逼真散景，并通过交叉注意力机制实现语义级控制。实验表明该方法在无需深度输入的情况下仍能取得高质量、可控的散景效果，为移动端人像虚化提供了更简洁的渲染路径。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37431/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1639, \"height\": 863}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37431/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1689, \"height\": 727}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37431/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1662, \"height\": 860}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37431/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1710, \"height\": 492}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37431/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 833, \"height\": 640}]"
tables_json: "[{\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37431/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 859, \"height\": 182}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37431/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1810, \"height\": 457}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37431/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 812, \"height\": 182}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37431/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 852, \"height\": 184}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37431/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 848, \"height\": 220}, {\"url\": \"assets/tables/aaai-2026-accepted/aaai-2026-37431/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 874, \"height\": 302}]"
motivation: 现有可控散景渲染依赖精确深度图，生成式方法又难以兼顾可控性与效率。
method: 提出基于流匹配的免深度框架，直接从全焦图像合成散景，并用交叉注意力实现语义控制。
result: 在无需深度输入的前提下，实现了逼真且可控的散景渲染效果。
conclusion: 为免深度、可控且高效的散景渲染提供了新的生成式解决方案。
---

## Abstract
Bokeh rendering simulates the shallow depth-of-field effect in photography, enhancing visual aesthetics and guiding viewer attention to regions of interest. Although recent approaches perform well, rendering controllable bokeh without additional depth inputs remains a significant challenge. Existing classical and neural controllable methods rely on accurate depth maps, while generative approaches often struggle with limited controllability and efficiency. In this paper, we propose BokehFlow, a depth-free framework for controllable bokeh rendering based on flow matching. BokehFlow directly synthesizes photorealistic bokeh effects from all-in-focus images, eliminating the need for depth inputs. It employs a cross-attention mechanism to enable semantic control over both focus regions and blur intensity via text prompts. To support training and evaluation, we collect and synthesize four datasets. Extensive experiments demonstrate that BokehFlow achieves visually compelling bokeh effects and offers precise control, outperforming existing depth-dependent and generative methods in both rendering quality and efficiency.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机与背景）

- **任务背景**：散景（Bokeh）渲染模拟摄影中的浅景深效果，通过选择性模糊来突出兴趣区域、改善构图并提升视觉美感。
- **核心问题**：如何在**不依赖深度图**的条件下，实现高质量、可控、实时的散景渲染。
- **现有方法的三类局限**：
  - **经典渲染方法**：依赖显式物理相机模型与精确深度图，深度不准确时易在遮挡/深度边界产生伪影。
  - **神经渲染方法**：虽能端到端生成较自然结果，但本质上仍依赖准确深度输入，真实场景中深度噪声会削弱鲁棒性。
  - **生成式方法**：如扩散模型可生成高保真图像，但现有文本到图像散景方法通常不支持全焦图像输入，且难以控制对焦区域；同时扩散采样轨迹弯曲，推理开销大。
- **论文整体含义**：提出 **BokehFlow**，将散景生成建模为潜在空间中的直接分布传输，使用流匹配实现免深度、语义可控、少步/单步采样的散景渲染。作者称其为“首个基于流匹配的免深度可控散景渲染框架”。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：
  - 不预测显式深度图，而是直接从全焦图像（AiF）的潜在表示传输到散景图像（Bokeh）的潜在表示。
  - 用流匹配学习直线、高效的速度场，支持快速采样。
  - 用文本提示控制对焦区域和模糊强度，通过交叉注意力注入控制信息。

- **潜在空间流匹配**：
  - 使用 VAE 编码器 \(E\) 将全焦图像 \(I_A\) 和散景图像 \(I_B\) 映射为潜在变量：
    - \(z_A = E(I_A)\)，\(z_B = E(I_B)\)。
  - 对散景潜变量加噪，构造线性插值路径：
    - \(\phi_t(z_B) = t z_B + (1-t)\epsilon\)，其中 \(\epsilon \sim \mathcal{N}(0,I)\)，\(t \in [0,1]\)。
  - 对应速度场为：
    - \(v_t(\phi_t(z_B)) = \phi_t(z_B) - \epsilon\)。
  - 生成过程遵循 ODE：\(d\phi_t(z_B) = v_t(\phi_t(z_B)) dt\)。

- **从“噪声→散景”改为“全焦→散景”的直接传输**：
  - 传统流匹配/扩散通常从高斯噪声 \(\epsilon\) 开始预测到目标分布。
  - 论文重新定义传输路径为从全焦潜变量 \(z_A\) 到散景潜变量 \(z_B\)。
  - 训练目标改为：
    - \(L^{Direct}_{FM} = \mathbb{E}_t \| N_{fm}(\phi_t(z_B), z_A
