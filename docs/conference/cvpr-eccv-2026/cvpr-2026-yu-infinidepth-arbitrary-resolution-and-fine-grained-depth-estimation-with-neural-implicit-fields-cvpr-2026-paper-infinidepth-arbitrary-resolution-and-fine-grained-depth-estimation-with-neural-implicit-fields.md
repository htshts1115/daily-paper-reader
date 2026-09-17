---
title: "InfiniDepth: Arbitrary-Resolution and Fine-Grained Depth Estimation with Neural Implicit Fields"
title_zh: "InfiniDepth:基于神经隐式场的任意分辨率细粒度深度估计"
authors: "Yu, Hao, Lin, Haotong, Wang, Jiawei, Li, Jiaxin, Wang, Yida, Zhang, Xueyang, Wang, Yue, Zhou, Xiaowei, Hu, Ruizhen, Peng, Sida"
date: 2026-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2026/papers/Yu_InfiniDepth_Arbitrary-Resolution_and_Fine-Grained_Depth_Estimation_with_Neural_Implicit_Fields_CVPR_2026_paper.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 基于隐式场的任意分辨率精细单目深度估计
tldr: "现有深度估计方法只能在离散图像网格上预测深度,限制了输出分辨率的可扩展性并阻碍几何细节恢复。本文提出InfiniDepth,将深度表示为神经隐式场,通过局部隐式解码器在连续二维坐标上查询深度,实现任意分辨率与细粒度深度估计。作者构建了源自五款游戏的4K高质量合成基准用于评测,实验显示方法达到先进水平。该工作突破了离散网格表示对深度估计的固有约束。"
source: CVPR-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-001.webp\", \"caption\": \"\", \"page\": 1, \"index\": 1, \"width\": 471, \"height\": 317}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-002.webp\", \"caption\": \"\", \"page\": 1, \"index\": 2, \"width\": 3084, \"height\": 1338}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-003.webp\", \"caption\": \"\", \"page\": 1, \"index\": 3, \"width\": 775, \"height\": 477}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-004.webp\", \"caption\": \"\", \"page\": 1, \"index\": 4, \"width\": 948, \"height\": 420}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-005.webp\", \"caption\": \"\", \"page\": 1, \"index\": 5, \"width\": 1630, \"height\": 1218}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-006.webp\", \"caption\": \"\", \"page\": 1, \"index\": 6, \"width\": 357, \"height\": 431}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-007.webp\", \"caption\": \"\", \"page\": 1, \"index\": 7, \"width\": 798, \"height\": 458}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-008.webp\", \"caption\": \"\", \"page\": 1, \"index\": 8, \"width\": 1630, \"height\": 1218}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-009.webp\", \"caption\": \"\", \"page\": 1, \"index\": 9, \"width\": 886, \"height\": 448}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-010.webp\", \"caption\": \"\", \"page\": 1, \"index\": 10, \"width\": 369, \"height\": 424}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-011.webp\", \"caption\": \"\", \"page\": 1, \"index\": 11, \"width\": 1070, \"height\": 550}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-012.webp\", \"caption\": \"\", \"page\": 1, \"index\": 12, \"width\": 1918, \"height\": 1274}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-013.webp\", \"caption\": \"\", \"page\": 1, \"index\": 13, \"width\": 470, \"height\": 339}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-014.webp\", \"caption\": \"\", \"page\": 1, \"index\": 14, \"width\": 578, \"height\": 344}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-015.webp\", \"caption\": \"\", \"page\": 1, \"index\": 15, \"width\": 637, \"height\": 496}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-016.webp\", \"caption\": \"\", \"page\": 1, \"index\": 16, \"width\": 578, \"height\": 346}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-017.webp\", \"caption\": \"\", \"page\": 1, \"index\": 17, \"width\": 578, \"height\": 352}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-018.webp\", \"caption\": \"\", \"page\": 1, \"index\": 18, \"width\": 834, \"height\": 419}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-019.webp\", \"caption\": \"\", \"page\": 1, \"index\": 19, \"width\": 502, \"height\": 476}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-020.webp\", \"caption\": \"\", \"page\": 1, \"index\": 20, \"width\": 540, \"height\": 467}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-021.webp\", \"caption\": \"\", \"page\": 3, \"index\": 21, \"width\": 564, \"height\": 445}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-022.webp\", \"caption\": \"\", \"page\": 3, \"index\": 22, \"width\": 409, \"height\": 324}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-023.webp\", \"caption\": \"\", \"page\": 3, \"index\": 23, \"width\": 437, \"height\": 300}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-024.webp\", \"caption\": \"\", \"page\": 3, \"index\": 24, \"width\": 424, \"height\": 290}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-025.webp\", \"caption\": \"\", \"page\": 4, \"index\": 25, \"width\": 497, \"height\": 289}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-026.webp\", \"caption\": \"\", \"page\": 4, \"index\": 26, \"width\": 500, \"height\": 285}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-027.webp\", \"caption\": \"\", \"page\": 4, \"index\": 27, \"width\": 508, \"height\": 335}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-028.webp\", \"caption\": \"\", \"page\": 4, \"index\": 28, \"width\": 509, \"height\": 335}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-029.webp\", \"caption\": \"\", \"page\": 7, \"index\": 29, \"width\": 483, \"height\": 308}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-030.webp\", \"caption\": \"\", \"page\": 7, \"index\": 30, \"width\": 488, \"height\": 301}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-031.webp\", \"caption\": \"\", \"page\": 7, \"index\": 31, \"width\": 474, \"height\": 307}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-032.webp\", \"caption\": \"\", \"page\": 7, \"index\": 32, \"width\": 483, \"height\": 310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-033.webp\", \"caption\": \"\", \"page\": 7, \"index\": 33, \"width\": 483, \"height\": 310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-034.webp\", \"caption\": \"\", \"page\": 7, \"index\": 34, \"width\": 479, \"height\": 310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-035.webp\", \"caption\": \"\", \"page\": 7, \"index\": 35, \"width\": 472, \"height\": 310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-036.webp\", \"caption\": \"\", \"page\": 7, \"index\": 36, \"width\": 470, \"height\": 310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-037.webp\", \"caption\": \"\", \"page\": 7, \"index\": 37, \"width\": 477, \"height\": 310}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-038.webp\", \"caption\": \"\", \"page\": 7, \"index\": 38, \"width\": 488, \"height\": 308}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-039.webp\", \"caption\": \"\", \"page\": 7, \"index\": 39, \"width\": 476, \"height\": 294}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-040.webp\", \"caption\": \"\", \"page\": 7, \"index\": 40, \"width\": 476, \"height\": 301}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-041.webp\", \"caption\": \"\", \"page\": 7, \"index\": 41, \"width\": 480, \"height\": 301}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-042.webp\", \"caption\": \"\", \"page\": 7, \"index\": 42, \"width\": 474, \"height\": 299}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-043.webp\", \"caption\": \"\", \"page\": 7, \"index\": 43, \"width\": 481, \"height\": 301}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-044.webp\", \"caption\": \"\", \"page\": 7, \"index\": 44, \"width\": 354, \"height\": 347}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-045.webp\", \"caption\": \"\", \"page\": 7, \"index\": 45, \"width\": 518, \"height\": 742}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-046.webp\", \"caption\": \"\", \"page\": 7, \"index\": 46, \"width\": 370, \"height\": 364}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-047.webp\", \"caption\": \"\", \"page\": 7, \"index\": 47, \"width\": 374, \"height\": 420}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-048.webp\", \"caption\": \"\", \"page\": 7, \"index\": 48, \"width\": 344, \"height\": 379}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-049.webp\", \"caption\": \"\", \"page\": 7, \"index\": 49, \"width\": 510, \"height\": 299}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-050.webp\", \"caption\": \"\", \"page\": 7, \"index\": 50, \"width\": 389, \"height\": 366}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-051.webp\", \"caption\": \"\", \"page\": 7, \"index\": 51, \"width\": 386, \"height\": 354}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-052.webp\", \"caption\": \"\", \"page\": 8, \"index\": 52, \"width\": 471, \"height\": 269}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-053.webp\", \"caption\": \"\", \"page\": 8, \"index\": 53, \"width\": 472, \"height\": 268}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-054.webp\", \"caption\": \"\", \"page\": 8, \"index\": 54, \"width\": 472, \"height\": 268}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-055.webp\", \"caption\": \"\", \"page\": 8, \"index\": 55, \"width\": 481, \"height\": 285}, {\"url\": \"assets/figures/cvpr-2026-accepted/cvpr-2026-yu-infinidepth-arbitrary-resolution-and-fine-grained-depth-estimation-with-neural-implicit-fields-cvpr-2026-paper/fig-056.webp\", \"caption\": \"\", \"page\": 8, \"index\": 56, \"width\": 422, \"height\": 303}]"
motivation: 针对现有深度估计只能在离散图像网格上预测、难以扩展分辨率和恢复几何细节的问题。
method: "将深度表示为神经隐式场,通过简单的局部隐式解码器在连续二维坐标查询深度。"
result: "实现任意分辨率与细粒度深度估计,并在构建的五款游戏4K合成基准上取得先进性能。"
conclusion: 突破了离散网格表示对深度估计分辨率与细节的固有约束。
---

## Abstract
Existing depth estimation methods are fundamentally limited to predicting depth on discrete image grids. Such representations restrict their scalability to arbitrary output resolutions and hinder the geometric detail recovery. This paper introduces InfiniDepth, which represents depth as neural implicit fields. Through a simple yet effective local implicit decoder, we can query depth at continuous 2D coordinates, enabling arbitrary-resolution and fine-grained depth estimation. To better assess our method's capabilities, we curate a high-quality 4K synthetic benchmark from five different games, spanning diverse scenes with rich geometric and appearance details. Extensive experiments demonstrate that InfiniDepth achieves state-of-the-art performance on both synthetic and real-world benchmarks across relative and metric depth estimation tasks, particularly excelling in fine-detail regions. It also benefits the task of novel view synthesis under large viewpoint shifts, producing high-quality results with fewer holes and artifacts. Code and data will be made publicly available.

---

## 论文详细总结（自动生成）

# InfiniDepth 论文中文结构化总结

## 1. 核心问题与整体含义（研究动机与背景）

- **核心问题**：现有单目深度估计方法从根本上被限制在**离散图像网格**上预测深度，这种表示方式导致两个关键缺陷：
  - **分辨率不可扩展**：输出分辨率被训练图像尺寸所束缚，无法自由地产生任意分辨率的深度图。
  - **几何细节丢失**：在整张网格上预测深度需要卷积上采样或从潜变量线性投影到深度块，前者引入平滑效应，后者难以捕捉局部几何变化，二者都会牺牲高频细节。
- **背景脉络**：
  - 传统方法（如条件随机场）受限于优化复杂度和可扩展性。
  - 深度学习主流方法（DepthAnything、MoGe、Marigold、PPD 等）虽泛化性强，但仍采用离散 2D 网格表示，在几何变化剧烈区域预测失败。
- **整体含义**：论文提出 **InfiniDepth**，将深度建模为**神经隐式场**，在连续 2D 坐标上查询深度，从而突破离散网格对分辨率与细节的固有约束，并进一步惠及大视角变化下的新视角合成（NVS）。

## 2. 论文提出的方法论

### 2.1 核心思想

- 将深度估计形式化为一个隐式函数：对任意连续 2D 坐标 $(x,y) \in [0,W]\times[0,H]$，以输入 RGB 图像 $I$ 为条件预测深度值：
  $$d_I(x,y) = \mathcal{N}_\theta(I, (x,y))$$
- 采用**多尺度局部隐式解码器**实例化 $\mathcal{N}_\theta$，结合轻量 MLP 头输出深度，实现分辨率无关、局部化的深度预测。

### 2.2 关键技术细节

- **特征查询（Feature Query）**：
  - 使用 ViT 编码器提取多阶段特征 token，通过 reassemble 块构建特征金字塔 $\{f^k\}_{k=1}^L$。
  - 浅层特征上采样到更高空间分辨率以保留细节，深层特征保持原分辨率以保留语义。
  - 对连续查询坐标 $(x,y)$，按比例映射到各尺度 $(x_k, y_k)$，在局部网格邻域 $\mathcal{N}_k$ 内通过**双线性插值**聚合特征，得到各尺度特征 token $f^k_{(x,y)}$。
- **深度解码（Depth Decoding）**：
  - 从浅到深逐级层次化融合，采用**残差门控融合块**：
    $$h_{k+1} = \mathrm{FFN}_k\left(f^{k+1}_{(x,y)} + g_k \odot \mathrm{Linear}(h_k)\right)$$
    其中 $g_k \in (0,1)^{C_{k+1}}$ 为可学习通道门控，$\odot$ 为逐元素乘。
  - 最终融合特征 $h_L$ 经 MLP 头输出深度：$d_I(x,y) = \mathrm{MLP}(h_L)$。
- **无限深度查询（Infinite Depth Query）**：
  - 动机：逐像素深度反投影得到的点云因透视投影和表面朝向存在严重密度不平衡，导致大视角 NVS 质量下降。
  - 定义自适应权重估计每像素对应的微分表面积：
    $$w(x,y) = \frac{d_I(x,y)^2}{|n(x,y)\cdot v(x,y)| + \varepsilon} \propto \Delta S(x,y)$$
    其中 $d^2$ 补偿深度平方缩放，$|n\cdot v|$ 补偿表面朝向效应。
  - 表面法线由隐式场可微性通过雅可比计算：
    $$n(x,y) = \frac{\partial_x X \times \partial_y X}{\|\partial_x X \times \partial_y X\|}$$
  - 依据权重分配亚像素查询预算，在像素块内均匀分布查询坐标，反投影后得到近似均匀覆盖表面的 3D 点云。
- **网络与训练**：
  - 编码器为 **DINOv3 ViT-Large**，取第 4、11、23 层，分别投影到 256/512/1024 维，第 4、11 层分别上采样 4×、2×。
  - 训练数据全部为合成数据（Hypersim、VKITTI、TartanAir、IRS、UnrealStereo4K、UrbanSyn）。
  - 支持稀疏采样监督，随机抽取 $N$ 个坐标-深度对计算 L1 损失：$\mathcal{L} = \frac{1}{N}\sum_{i=1}^N |d_i - \hat{d}_i|$。

## 3. 实验设计

### 3.1 数据集与 Benchmark

- **自建基准 Synth4K**：从 5 款游戏采集的 4K RGB-D 数据（Synth4K-1 至 Synth4K-5），覆盖室内外多样场景；额外构建**高频（HF）掩码**，按多尺度拉普拉斯能量采样像素，用于针对性评估细节预测。
- **真实世界数据集**：KITTI、ETH3D、NYUv2、ScanNet、DIODE。

### 3.2 评估任务与指标

- **相对深度估计**：零样本评估，报告 $\delta_1$（真实数据集）；Synth4K 上报告 $\delta_{0.5}$、$\delta_1$、$\delta_2$（全图与 HF 细节区域）。
- **度量深度估计**：结合稀疏深度输入（采用 PromptDA 的 depth prompt 模块，记为 Ours-Metric），报告 $\delta_{0.01}$、$\delta_{0.02}$、$\delta_{0.04}$。

### 3.3 对比方法

- **相对深度**：DepthAnything、DepthAnythingV2、DepthPro、MoGe、MoGe-2、Marigold、PPD。
- **度量深度**：Marigold-DC、Omni-DC、PriorDA、PromptDA。
- **公平性控制**：所有基线使用相同输入分辨率与相同稀疏深度采样；Synth4K 上基线输出上采样至 4K，而 InfiniDepth 直接在 4K 查询。

### 3.4 消融与扩展实验

- 深度表示消融（vs. DPT 离散网格解码器，共享 DINOv3 编码器与 Hypersim 训练数据）。
- 隐式解码器设计消融（多尺度查询与融合机制、显式学习偏移 vs. 双线性插值、交叉注意力 vs. 共享 MLP）。
- 图像编码器消融（DINOv3 vs. DINOv2）。
- 应用实验：扩展轻量 Gaussian Splatting 头，与 ADGaussian 对比大视角 NVS。

## 4. 资源与算力

- **GPU 型号与数量**：8 张 NVIDIA A800 GPU。
- **训练配置**：每 GPU batch size 为 4，共训练 **800k 步**，优化器为 AdamW，学习率 $1\times10^{-5}$。
- **说明**：论文正文（第 3.4 节）明确给出了上述算力信息；更详细的训练数据与策略在补充材料中提供。

## 5. 实验数量与充分性

- **实验组数概览**：
  - Synth4K 上 5 个子集 × 全图/HF 细节 × 相对/度量两类任务（表 1、表 2）。
  - 真实数据集 5 个 × 相对/度量两类任务（表 3、表 4）。
  - 消融实验覆盖 10 个数据集（5 个 Synth4K 子集 + 5 个真实数据集），涉及深度表示、多尺度查询、编码器三组变量（表 5）。
  - 定性对比（图 5、图 6）与 NVS 应用实验（图 1(c)、图 8）。
- **充分性评价**：
  - 覆盖合成与真实、相对与度量、全图与高频细节、定量与定性多个维度，较为充分。
  - 消融实验设计合理，控制了编码器与训练数据变量，能有效隔离"隐式场表示"的贡献。
  - 公平性方面，统一输入分辨率与稀疏深度采样，并对基线输出做上采样以匹配 4K 评估，处理得当。
  - **潜在不足**：相对深度任务在真实数据集上指标趋于饱和（$\delta_1$ 普遍 >97%），论文也承认此时定量指标区分度有限，需依赖定性结果佐证。

## 6. 论文的主要结论与发现

- InfiniDepth 在 **Synth4K** 上所有指标均显著超越现有方法，尤其在高频细节区域优势明显。
- 在**真实世界基准**上，相对深度估计与当前 SOTA 持平（Ours-Relative），度量深度估计（Ours-Metric）则取得明确提升。
- 将深度建模为神经隐式场相比离散网格 DPT 解码器，在度量深度任务上带来大幅提升（如 Synth4K-1 $\delta_{0.01}$ 从 62.4 提升到 72.7），相对深度任务上亦有中等增益。
- 多尺度特征查询机制对性能贡献显著；DINOv3 编码器优于 DINOv2。
- 结合无限深度查询策略，可生成表面均匀分布的 3D 点，在大视角变化下实现更完整、更少孔洞与伪影的 NVS。

## 7. 优点

- **表示创新**：首次系统地将深度建模为神经隐式场，实现连续坐标查询，天然支持任意分辨率与细粒度预测，突破离散网格的固有限制。
- **架构简洁有效**：局部隐式解码器 + 双线性插值 + 残差门控融合，结构轻量却性能强劲。
- **自监督友好**：因隐式场特性，可灵活使用稀疏坐标-深度对监督，无需完整深度图。
- **几何一致性强**：隐式场可微性使得表面法线可由雅可比解析获得（图 4），为均匀点云生成提供几何基础。
- **应用拓展性好**：无限深度查询策略解决逐像素反投影的密度不平衡问题，显著改善大视角 NVS。
- **基准贡献**：构建 Synth4K 4K 合成基准及 HF 掩码，填补高分辨率、细粒度深度评估的空白。
- **实验严谨**：控制变量充分，定量与定性结合，消融覆盖关键设计。

## 8. 不足与局限

- **时序一致性缺失**：仅针对单目单视图深度数据训练，应用于视频时未显式约束时间一致性，可能出现跨帧闪烁。
- **训练数据全为合成数据**：虽理由是真实数据深度噪声大、不完整，但可能带来合成到真实的域偏差风险。
- **真实数据集指标饱和**：相对深度任务在真实基准上各方法 $\delta_1$ 接近，定量区分度低，结论更多依赖定性观察。
- **度量深度依赖稀疏深度输入**：Ours-Metric 需额外稀疏深度，非纯 RGB 方案，应用场景受限。
- **效率未在正文详述**：计算效率与参数量评估放在补充材料，正文未给出推理速度等实用指标。
- **NVS 实验规模有限**：仅与 ADGaussian 对比，NVS 评估的广度与深度有待进一步扩展。
- **未来方向**：作者提出扩展至多视图设置以提升时间稳定性与 3D 一致性。

（完）
