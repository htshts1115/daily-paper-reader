---
title: "OmniDS: Dual-Stream Context Fusion for Omnidirectional Depth from Fisheye Cameras"
title_zh: OmniDS：面向鱼眼相机全向深度的双流上下文融合
authors: "Chaesong Park, Jihyeon Hwang, Muyeol Sung, Jongwoo Lim"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6709.pdf"
tags: ["query:stereo-depth"]
score: 4.0
evidence: 多相机深度估计中的遮挡与薄结构歧义
tldr: 针对多鱼眼相机环视全向深度估计中宽基线导致的可见性冲突——不同相机观测同一物体的不同部分，固定投影聚合在遮挡边界和薄结构处产生歧义匹配证据——本文提出迭代深度细化框架OmniDS。方法用动态上下文融合替代刚性的鱼眼到等距柱面采样，并结合跨视图融合迭代精化深度。实验表明该方法有效缓解遮挡边界与薄结构处的匹配歧义，提升全向深度估计质量，为多相机深度估计提供了新思路。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b5a48c92c25f5105ddff4b81/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 4166, \"height\": 1549}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b5a48c92c25f5105ddff4b81/fig-002.webp\", \"caption\": \"\", \"page\": 6, \"index\": 2, \"width\": 1261, \"height\": 647}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-b5a48c92c25f5105ddff4b81/fig-003.webp\", \"caption\": \"\", \"page\": 13, \"index\": 3, \"width\": 1832, \"height\": 1995}]"
motivation: 多鱼眼相机全向深度因宽基线导致可见性冲突，固定投影聚合在遮挡边界与薄结构处匹配证据模糊。
method: 提出迭代深度细化框架OmniDS，以动态上下文融合替代刚性鱼眼到ERP采样，并结合跨视图融合。
result: 缓解了遮挡边界与薄结构附近的匹配歧义，提升全向深度估计质量。
conclusion: 为多鱼眼全向深度估计提供了动态上下文融合的细化思路。
---

## Abstract
Omnidirectional depth estimation from multi-fisheye camerarigs is complicated by visibility conflicts: wide baselines cause differentcameras to observe different portions, or even different faces, of the sameobject, so aggregating their features into a unified equirectangular (ERP)representation under fixed projection produces ambiguous matching ev-idence near occlusion boundaries and thin structures. Although existingmethods mitigate this by down-weighting unreliable views, they do notresolve the underlying discrepancy because context formation and cross-view fusion remain tied to rigid fisheye-to-ERP sampling. We presentOmniDS, an iterative depth refinement framework that replaces rigidaggregation by combining dynamic context fusion with consensus-awaremulti-view similarity. A dual-stream encoder pairs a lightweight CNNfor geometric detail with a frozen DINOv3 for semantic priors; their fea-tures are reprojected into ERP space at each refinement step via learnedview weighting and deformable cross-attention with geometric distortionbias. In parallel, a multi-view consensus volume captures global cross-camera agreement through group-wise correlation and feature variance,regularized by a 3D U-Net. For efficient deployment, we distill the dual-stream representation into a single MobileNet-based encoder. OmniDSachieves state-of-the-art performance on the OmniThings, OmniHouse,and Sunny benchmarks while maintaining competitive inference speed.Project page and codes are available here.

---

## 论文详细总结（自动生成）

# OmniDS 论文中文总结

## 1. 核心问题与研究动机

- **应用背景**：全向（360°）深度感知是机器人自主导航、避障、SLAM、AR/VR 远程呈现的关键能力。多鱼眼相机环视系统（multi-fisheye rig）因结构紧凑、成本低、覆盖完整，成为实用的传感配置。
- **核心难题**：多鱼眼相机全向深度估计受**可见性冲突（visibility conflicts）**困扰。
  - 宽基线导致不同相机观测同一物体的不同部分，甚至不同表面（不同外观与法向）。
  - 在固定投影下将多相机特征聚合到统一等距柱面（ERP）表示时，遮挡边界与薄结构附近会产生**歧义甚至矛盾的匹配证据**。
  - 具体表现为两类问题：(i) **遮挡泄漏**——被遮挡相机贡献背景像素；(ii) **自遮挡**——可见相机把不同表面映射到同一 ERP 单元。
- **现有方法的不足**：以往方法通过视图加权（如 RomniStereo）或中心视图处理（如 MDP-Omni）抑制不可靠视图，但只是**降权**而非解决根本矛盾，因为**上下文构建与跨视图融合仍依赖刚性的鱼眼到 ERP 采样**。
- **两个瓶颈**：(i) 仅靠 CNN 特征构建的上下文在弱纹理区域表现弱；(ii) 固定投影/聚合无法在可见性不连续与薄结构边界处自适应采样与融合。

## 2. 方法论

### 核心思想
用**迭代深度细化框架**替代刚性聚合，结合**动态 ERP 上下文融合**与**共识感知的多视图相似度**，在每个细化步骤动态重投影特征。

### 关键技术细节

- **双流编码器（Dual-Stream Encoder）**
  - CNN 流：轻量 18 层残差网络，捕获细粒度纹理与局部边缘，用于所有几何操作（相关性、分组相关性、ERP 上下文）。
  - DINO 流：冻结的 DINOv3 ViT + 可学习投影头，提供语义与结构先验，应对弱纹理、反射、复杂遮挡。

- **动态上下文融合（Context Fusion，每次迭代动态更新）**
  - **CNN 分支**：将 ERP 像素按当前深度反投影到 4 个鱼眼视图，网格采样得到 CNN 特征；用轻量网络预测相机权重并经 Softmax 归一化（式 1），再加权求和（式 2）。
  - **DINO 分支**：用**可变形交叉注意力**（4 头、每头 4 个采样点）替代简单网格采样；查询为可学习 ERP 嵌入 + 当前深度编码；在参考点周围学习采样偏移（式 3）。
  - **几何畸变偏置**：按到相机中心的径向距离生成偏置项（式 4），鼓励模型更依赖鱼眼高分辨率中心区域。
  - **融合**：残差逐点卷积 `F_context = F_dino-erp + Fuse([F_dino-erp; F_cnn-erp])`（式 5）。

- **相似度体（Similarity Volumes）**
  - **相关性剖面（Correlation Profile）**：按 RomniStereo 的参考/目标配对做通道级相关（式 6），并用 2D 空间聚合器平滑局部噪声。
  - **多视图共识体（Multi-View Consensus Volume）**：融合 (a) 8 组**分组相关性**（保留多模态匹配成本分布）；(b) 跨 4 相机的**特征方差**（深度正确时方差小，遮挡边界或错误假设时方差大）；两者拼接后用 **3D U-Net** 正则化，强制全局几何一致性。
  - 两类体均组织为 **4 级多尺度金字塔**，供 ConvGRU 查询。

- **迭代深度细化**
  - 逆深度初始化为深度范围中点（96 bin 中的 48），用 ConvGRU 迭代预测残差更新：`h(t) = GRU(h(t-1), [F_context(t); m(t)])`，`d̂(t) = d̂(t-1) + ∆d(t)`（式 7）。
  - 最终经凸上采样在空间与深度轴各放大 2×。
  - 损失为加权序列损失（式 8），γ=0.9 强调后期迭代。

- **特征蒸馏（高效部署）**
  - 将两个冻结教师编码器蒸馏为单个 U-Net 风格 MobileNetV2 学生编码器，输出两个特征图（×2 替代 CNN，×16 替代 DINO，均 32 通道）。
  - 蒸馏损失为加权特征 MSE（式 9），λ_cnn=1.0、λ_dino=10.0（更强调难匹配的 DINO 表示）。
  - 蒸馏用 AdamW（lr 5e-4, wd 1e-5）在 OmniThings 上训练 1 epoch；随后学生替换教师，端到端微调 15 epoch。

## 3. 实验设计

- **数据集**：OmniThings（大规模物体中心）、OmniHouse（真实室内）、Sunny / Cloudy / Sunset（户外驾驶，同布局不同天气）。均为**合成**数据。
  - 每样本含 4 张 220° 鱼眼图（768×800），GT 逆深度图在 ERP 球面 360×640。
- **Benchmark / 指标**：在**逆索引空间**评估，将逆深度离散为 N 个索引，报告 >1、>3、>5（索引误差超阈值的像素百分比）、MAE、RMS。
- **对比方法**：OmniMVS、OmniMVS+32、S-OmniMVS、RomniStereo 32/64、MDP-Omni（当前 SOTA）。
- **训练协议**：
  - 先在 OmniThings 上训练 30 epoch；
  - 再在 OmniHouse + Sunny 混合集上做蒸馏微调（15 epoch）。
  - 分两种设置报告：仅 OmniThings 训练 vs. 进一步微调。
- **消融实验**：
  - 表 3：相似度/上下文配置（CNN/DINO/MVC/可变形等 6 种组合 a–f）。
  - 表 4：相似度体设计（Corr / 2D Aggr. / MVC 共 3 种配置）。

## 4. 资源与算力

- 文中**明确提到**：推理延迟在 **NVIDIA RTX 4070 SUPER** 上测量，蒸馏版约 102 ms（≈10 FPS）。
- **未明确说明**：训练所用 GPU 型号与数量、总训练时长、显存占用等均未给出。
- 仅给出训练**轮数**：OmniThings 预训练 30 epoch，蒸馏与微调各 15 epoch。
- 注意：MDP-Omni 的推理延迟因源码未公开，是按性能比例**推算**而非实测。

## 5. 实验数量与充分性

- **规模**：5 个数据集 × 2 种训练设置（仅预训练 / 微调），约 6 个对比基线，2 组消融表（共 9 种配置），外加定性对比与失败案例分析。
- **充分性**：
  - 覆盖面较广：室内/户外、不同天气、跨域泛化均有评估；消融覆盖了上下文分支、相似度体、可变形注意力等关键组件。
  - 定量 + 定性结合，并报告了效率（延迟）指标。
- **客观性与公平性存疑点**：
  - 仅在**合成数据**上评估，未涉及真实世界数据。
  - MDP-Omni 的延迟为**推算值**，非同一环境实测，效率对比不完全公平。
  - 消融实验仅在 Sunny 单数据集上进行（30 epoch 统一协议），代表性有限。
  - 消融中 MVC 的收益并非一致（见下）。

## 6. 主要结论与发现

- **SOTA 性能**：在 OmniThings、OmniHouse、Sunny（以及 Cloudy、Sunset）上，Ours/Ours-ft 在多数指标上最优。
  - 仅 OmniThings 训练即展现强跨域泛化，MAE/RMS 最低。
  - 微调后：OmniHouse MAE 0.28 / RMS 0.89；Sunny MAE 0.28 / RMS 1.32；OmniThings MAE 由 1.96 降至 1.70。
- **效率**：Ours-ft 推理 148 ms；蒸馏版 **102 ms（快 31.1%）**，精度仅轻微下降（OmniThings MAE 1.70→2.11），在 OmniHouse/Sunny 上保持竞争力。
- **定性发现**：在物体边界、大面积平面（墙/天花板）、薄结构（杆/标志）与反射/透明区域（窗户）上误差更低、几何更锐利。
- **消融结论**：
  - CNN + DINO 双上下文优于任一单分支。
  - MVC 对最严阈值（>1）改善最明显，但并非在所有指标上一致获益（会略增 RMS）。
  - 默认上下文 + CNN+DINO 组合给出最佳总体权衡。

## 7. 优点

- **问题定位准确**：明确指出刚性 fisheye-to-ERP 采样是可见性冲突无法根治的根源，而非简单降权。
- **方法创新性**：
  - 动态上下文融合（每次迭代重投影 + 学习视图权重 + 可变形交叉注意力 + 畸变偏置），比固定投影更适应遮挡与薄结构。
  - 多视图共识体引入**跨相机特征方差**作为全局一致性信号，超越传统成对相关。
  - 双流设计（CNN 几何细节 + DINOv3 语义先验）互补，符合近期密集匹配研究趋势。
- **实用性**：蒸馏到单 MobileNet 编码器，显著降低延迟，适合算力受限部署。
- **评估较全面**：多数据集、跨域、多指标、定量+定性+消融+效率。

## 8. 不足与局限

- **数据局限**：仅在**合成数据**上评估，未验证真实鱼眼数据（存在标定噪声、镜头畸变、光照等差异），泛化到真实场景存疑。
- **相机配置固定**：仅针对固定 4 相机环视系统，未支持任意数量/布局的相机，也未考虑标定噪声——作者自述为未来工作。
- **效率**：非蒸馏版 148 ms 尚非严格实时；蒸馏版在 OmniThings 上精度下降较明显（>1 由 25.14 升至 26.22，MAE 1.70→2.11）。
- **消融局限**：仅单一数据集（Sunny）；MVC 组件收益不一致（RMS 上升），其通用性有待进一步验证。
- **公平性风险**：MDP-Omni 延迟为推算值；训练算力信息缺失，难以评估可复现性与资源门槛。
- **失败案例**：论文提及定性失败案例置于补充材料，正文未充分讨论。

（完）
