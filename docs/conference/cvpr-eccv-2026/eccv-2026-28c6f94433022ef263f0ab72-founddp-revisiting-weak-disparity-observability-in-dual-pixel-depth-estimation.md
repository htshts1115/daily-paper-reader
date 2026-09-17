---
title: "FoundDP: Revisiting Weak Disparity Observability in Dual-Pixel Depth Estimation"
title_zh: FoundDP：重新审视双像素深度估计中的弱视差可观测性
authors: "fengchen he, Hao Xu, Dayang Zhao, Tingwei Quan, Shaoqun zeng"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/7935.pdf"
tags: ["query:stereo-depth"]
score: 8.0
evidence: 双像素小基线度量深度，结合单目深度基础模型先验
tldr: 双像素成像可借助子孔径视差从单相机获得度量深度，但有效基线极小导致视差可观测性弱，在无纹理、低对比或下采样区域出现结构退化与深度失败。本文提出FoundDP统一框架，将双像素度量深度与单目深度基础模型的全局结构先验相结合，通过双像素深度保持度量尺度，并利用ViT特征恢复结构一致性。该方法在小基线弱视差条件下提升深度可靠性，为手机等小型化设备的深度估计提供思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-28c6f94433022ef263f0ab72/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 2516, \"height\": 1644}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-28c6f94433022ef263f0ab72/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 3945, \"height\": 2174}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-28c6f94433022ef263f0ab72/fig-003.webp\", \"caption\": \"\", \"page\": 8, \"index\": 3, \"width\": 1799, \"height\": 661}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-28c6f94433022ef263f0ab72/fig-004.webp\", \"caption\": \"\", \"page\": 10, \"index\": 4, \"width\": 4512, \"height\": 2443}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-28c6f94433022ef263f0ab72/fig-005.webp\", \"caption\": \"\", \"page\": 13, \"index\": 5, \"width\": 1756, \"height\": 1314}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-28c6f94433022ef263f0ab72/fig-006.webp\", \"caption\": \"\", \"page\": 13, \"index\": 6, \"width\": 1793, \"height\": 814}]"
motivation: 双像素成像有效基线极小，视差可观测性弱，在无纹理低对比区域易出现结构退化与深度失败。
method: 提出FoundDP，融合双像素度量深度与单目深度基础模型的全局结构先验，用ViT特征恢复结构一致性。
result: 在保持度量尺度的同时恢复结构一致性，缓解弱视差区域的深度失败。
conclusion: 为小基线双像素深度估计提供统一框架。
---

## Abstract
Dual-pixel (DP) imaging enables metric depth estimation from a single camera using sub-aperture disparity. However, the extremely small e(cid:27)ective baseline limits disparity observability, leading to structural degradation and depth failure in textureless, low-contrast, or downsampled regions. Existing DP-based methods rely primarily on local disparity cues and therefore become unreliable when disparity signals are weak or ambiguous. To address this limitation, we propose FoundDP, a uni(cid:28)ed framework that integrates metric DP depth with global structural priors from a monocular depth foundation model. Our method preserves metric scale through DP-derived depth and leverages Vision Transformer (ViT) features to restore structural consistency in weakdisparity regions. To ensure reliable metric guidance under DP imaging conditions, we identify and mitigate ViT representation degradation induced by DP defocus blur via ViT feature alignment, enabling stable metric-guided depth estimation. Extensive experiments on synthetic and real-world DP benchmarks show that FoundDP delivers superior performance, with consistent gains in structural (cid:28)delity and metric accuracy, especially under reduced disparity observability. Code will be available at: https://github.com/EchoLighting/FoundDP • •

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究背景**：双像素（Dual-Pixel, DP）成像通过将每个像素拆分为左右子像素，使单相机具备隐式立体能力，可从子孔径视差中获得具有物理尺度的度量深度。
- **核心问题**：DP 成像的有效基线极小，导致视差可观测性天然受限。在无纹理、低对比、平面、远距离或下采样区域，局部视差信号容易接近噪声水平，造成结构退化和深度预测失败。
- **现有方法矛盾**：
  - 传统 DP 深度方法依赖局部子像素对应关系，在弱视差区域不可靠。
  - 单目深度基础模型（如 Depth Anything V2、MoGe）具有强全局结构推理能力，但缺少物理度量尺度，预测通常只能确定到仿射变换。
- **整体含义**：论文试图调和“物理可观测性”与“结构推理”之间的矛盾，提出 FoundDP，用 DP 深度提供度量锚点，用 ViT 基础模型先验恢复弱视差区域的结构一致性。

## 2. 方法论

- **核心思想**：将 DP 成像的度量深度线索与单目深度基础模型的全局结构先验统一起来；DP 深度保持绝对尺度，基础模型特征补偿弱视差区域的结构缺失。
- **整体流程**：
  - 输入左右 DP 图像 \(I_L, I_R\)。
  - DDE 模块产生初始度量深度 \(D_{dp}\)。
  - SR 模块对 \(D_{dp}\) 做残差结构校正，得到 \(D_{metric}\)。
  - DG 模块用 \(D_{metric}\) 引导 ViT 结构特征，输出最终深度 \(D_{guide}\)。
- **DP Depth Estimation Module（DDE）**：
  - 左右图像经共享权重编码器提取多尺度特征。
  - 构建 3D cost volume，采用以零视差为中心的对称位移假设，匹配 DP 子孔径的光学对称性。
  - 使用 3D 卷积正则化 cost volume，并通过 Softmin 沿视差维回归连续深度，避免离散量化伪影。
  - 输出 \(D_{dp}\)，具备物理度量尺度，但弱视差区域仍可能结构退化。
- **Structure Refinement Module（SR）**：
  - 预测残差校正场：\(\Delta D = SR(I_L, I_R, D_{dp})\)。
  - 最终：\(D_{metric} = D_{dp} + \Delta D\)。
  - 采用层次化编码器-解码器、多尺度残差卷积、通道注意力和 2D 位置编码，保留度量尺度的同时修补结构不连续。
- **Depth Guidance Module（DG）**：
  - 使用预训练 ViT 编码器提取多级 token 特征，并重塑为多尺度特征图。
  - 在 DPT 风格解码器中，将归一化后的度量深度 \(\hat{D}\) 作为空间条件注入。
  - 特征更新形式：\(X' = X + \phi(X) + g(\hat{D}) \odot \psi(\hat{D})\)，通过门控机制选择性增强几何可靠区域。
- **ViT 特征对齐**：
  - 论文指出 DP 散焦模糊会造成 ViT 表示退化，影响深度引导稳定性。
  - 使用清晰 RGB 图像和其 DP 退化版本，通过共享 ViT 编码器施加特征对齐损失：
    \[
    L_{align} = \sum_l \|\Phi_l(I_{clear}) - \Phi_l(I_{blur})\|_2^2
    \]
  - 该策略使退化特征向清晰输入的特征分布对齐，提升引导稳定性。
- **损失函数**：
  - 统一使用对数深度空间的 Smooth L1 损失监督三个阶段。
  - 不使用 SiLog 等尺度不变损失，因为 DP 有能力恢复度量深度，必须保留绝对尺度。
- **训练策略**：
  - 分阶段优化：先独立训练 DDE；再冻结 DDE 训练 SR；然后引入并精炼 ViT 编码器；最后冻结 DDE、SR、ViT，仅优化 DPT 解码器。

## 3. 实验设计

- **数据集与场景**：
  - 合成数据：NYUData，使用基于射线追踪的 DP 模拟器生成左右 DP 图像对。
  - 真实数据：DP2020、DP5K、DP2019，提供 DP 左右图像对和深度标注。
  - 自建下采样数据集：DPDown70，使用 Canon EOS R6 Mark II + RF 50mm 镜头、f/8 光圈拍摄，约 1k 训练图像、约 70 测试样本；原始 4000×6000 图像缩放到 512×768。
  - 所有有效深度线性映射到 1–10 m，超出范围忽略。
- **Benchmark 与指标**：
  - Affine-Invariant Error：AI(1)、AI(2)，越低越好。
  - Rank Consistency：\(1-|\rho_s|\)，越低越好。
  - Threshold Accuracy：Acc-1（\(\delta < 1.25\)）、Acc-2（\(\delta < 1.25^2\)），越高越好。
  - 弱视差区域通过 Sobel 梯度响应、平滑、阈值化和形态学操作生成掩码。
- **对比方法**：
  - DPNet、DDDNet、SFBDNet、CADSNet。
  - 所有方法在相同预处理和度量协议下评估。
- **实验类型**：
  - 全局定量比较：NYUData、DP2020、DP5K、DP2019。
  - 弱视差区域定量比较：同上四个数据集。
  - 下采样鲁棒性：DPDown70。
  - 视差可观测性分析：用下采样因子作为连续可观测性代理，观察 Acc-1 变化。
  - 消融实验：DDE、SR、DG 模块贡献；ViT 特征对齐；ViT 特征余弦相似度。
  - 定性比较：正常场景、弱视差区域、下采样场景。

## 4. 资源与算力

- 论文明确提到：
  - 使用 PyTorch 实现。
  - 训练在单张 NVIDIA RTX 4090D GPU 上完成。
  - 使用 Adam 优化器，初始学习率 \(1 \times 10^{-4}\)。
  - 每个阶段训练 100 个 epoch。
  - 图像统一缩放到 512×768 进行训练和评估。
- 未明确说明：
  - 总训练时长、总 GPU 小时数。
  - 显存占用、推理速度、模型参数量、能耗等。
  - 是否使用混合精度、分布式训练等细节。

## 5. 实验数量与充分性

- **实验规模**：
  - 表 1：4 个公开数据集上的全局定量比较。
  - 表 2：4 个公开数据集上的弱视差区域定量比较。
  - 表 3：自建 DPDown70 下采样数据集定量比较。
  - 表 4：DDE、SR、DG 模块消融，4 种配置。
  - 表 5：ViT 特征对齐消融，2 种配置。
  - 表 6：ViT 特征余弦相似度分析。
  - 图 5：深度精度随视差可观测性变化的分析。
  - 图 6：模块消融的定性结果。
  - 图 1、图 4：定性比较。
- **充分性评价**：
  - 覆盖合成与真实数据、全局与弱视差区域、下采样鲁棒性、模块消融和表示对齐分析，整体较充分。
  - 使用多指标评估结构保真、排序一致性和度量精度，评价较全面。
  - 所有对比方法采用相同预处理和度量协议，公平性较好。
- **潜在不足**：
  - 自建 DPDown70 测试样本约 70 张，规模偏小。
  - 对比方法主要是 DP 专用方法，未与最新基础模型融合式 DP 方法或更多通用度量深度方法全面比较。
  - 弱视差掩码阈值和形态学参数未在正文详细展开，可能影响可复现性。
  - 仅以 DAV2 作为基础模型，未验证其他基础模型替换效果。

## 6. 主要结论与发现

- FoundDP 在合成和真实 DP 基准上取得优于或媲美现有 DP 方法的表现，尤其在弱视差区域和下采样条件下提升明显。
- DP 深度提供度量尺度，基础模型 ViT 特征提供全局结构先验，两者互补能有效缓解弱视差导致的结构退化和深度失败。
- ViT 特征对齐能显著缓解 DP 散焦模糊造成的表示退化：特征余弦相似度从 0.8737 提升到 0.9454。
- 消融表明：
  - SR 减少局部不连续和深度空洞。
  - DG 带来最大性能增益，说明全局结构先验在弱视差条件下非常关键。
  - ViT 特征对齐进一步提升所有指标。
- 视差可观测性越低，所有 DP 方法性能都会下降；但 FoundDP 下降更缓，鲁棒性更强。
- 论文认为，在极小基线和低视差条件下，引入基础模型级结构推理是稳定度量 DP 深度的必要途径。

## 7. 优点

- **问题定位清晰**：准确指出 DP 深度估计的根本瓶颈是弱视差可观测性，而非单纯网络容量或训练数据不足。
- **方法设计有针对性**：用 DP 深度保持度量尺度，用 ViT 先验恢复结构，分工明确。
- **发现并处理 ViT 表示退化**：将 DP 散焦模糊导致的 ViT 特征偏移视为引导不稳定来源，并提出特征对齐策略，具有新意。
- **训练策略稳定**：分阶段优化避免多模块异质目标同时训练带来的不稳定。
- **损失函数选择合理**：坚持对数空间 Smooth L1 而非尺度不变损失，符合 DP 度量深度的物理属性。
- **实验较全面**：覆盖合成、真实、弱视差、下采样、消融和可观测性分析，多指标评估增强说服力。
- **弱视差区域提升显著**：表 2 显示在弱区域中相对竞争方法的优势比全局评估更明显。

## 8. 不足与局限

- **仍依赖可观测视差**：当 DP 测量被强噪声或极端光学退化严重破坏时，性能可能下降。
- **基础模型适应不完美**：ViT 基础模型原本在清晰自然图像上预训练，对 DP 特定成像特性的适应仍有限。
- **计算开销较大**：引入 ViT 编码器和 DPT 解码器增加计算负担，限制资源受限设备上的实时部署。
- **自建数据集规模有限**：DPDown70 仅约 70 个测试样本，且使用特定相机、镜头和光圈，泛化性证据有限。
- **下采样作为可观测性代理**：虽然合理，但不能完全等价于真实场景中由纹理缺失、低光、远距离等造成的弱视差

条件，因此结论外推需谨慎。  
- **弱视差掩码依赖后处理**：通过 Sobel 梯度、平滑、阈值化和形态学操作生成掩码，阈值与核参数可能影响弱视差区域划分，不同数据集上的可复现性和公平性需要更多说明。  
- **计算与部署分析缺失**：论文引入 ViT 编码器和 DPT 风格解码器，但未报告参数量、显存占用、推理延迟和吞吐量，难以判断其在实际移动端或嵌入式 DP 相机上的可行性。  
- **基础模型选择较单一**：主要基于 Depth Anything V2 验证，未系统比较其他单目深度基础模型或度量深度模型，因此“基础模型先验”这一结论的普适性仍待检验。  
- **跨域与动态场景验证不足**：实验集中在静态场景和特定数据集，未充分覆盖动态物体、透明/反射表面、运动模糊、极端光照等真实挑战。  
- **训练流程较复杂**：分阶段冻结与解冻 DDE、SR、ViT、DPT 解码器，虽然有助于稳定优化，但也增加训练调参成本和复现难度。  
- **失败案例讨论有限**：论文强调弱视差和下采样下的改进，但对严重噪声、遮挡、重复纹理或 DP 光学退化极端情况下的失败模式缺少深入分析。  

## 9. 总体评价与启示

- **核心贡献明确**：FoundDP 将 DP 成像的物理度量能力与单目基础模型的全局结构先验结合，针对弱视差区域的结构退化提出了一条合理且有效的技术路线。  
- **方法设计具有层次性**：DDE 负责度量深度初估，SR 负责残差结构修补，DG 负责基础模型引导，三者分工清晰，消融实验也支持各模块的有效性。  
- **ViT 特征对齐是亮点**：论文没有简单套用基础模型，而是注意到 DP 散焦模糊会造成 ViT 表示退化，并通过清晰/退化特征对齐提升引导稳定性，这一观察具有较好的启发性。  
- **实验评价较全面**：合成与真实数据、全局与弱视差区域、下采样鲁棒性、模块消融、表示相似度分析和定性比较共同支撑结论，整体说服力较强。  
- **仍属于强经验性融合框架**：DP 线索与基础模型先验的融合方式、门控机制和特征对齐损失更多依赖实验验证，理论层面的可解释性和最优性尚不充分。  
- **实际部署需谨慎**：若目标平台对算力、延迟和功耗敏感，ViT 与 DPT 解码器带来的开销可能成为瓶颈，未来需要轻量化、蒸馏或剪枝版本。  
- **对领域启示**：在极小基线、低视差可观测性条件下，单纯依赖局部子像素匹配可能触及物理上限；引入具有全局结构推理能力的基础模型，并保持度量尺度约束，是提升 DP 深度鲁棒性的可行方向。  

（完）
