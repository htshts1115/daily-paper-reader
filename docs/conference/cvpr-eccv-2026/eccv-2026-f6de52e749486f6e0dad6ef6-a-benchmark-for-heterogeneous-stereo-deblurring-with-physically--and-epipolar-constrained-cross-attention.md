---
title: A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention
title_zh: 面向异构立体去模糊的基准与物理及极线约束交叉注意力
authors: "Jiah Kim, Hoju Shin, Seung-Wook Kim, Seowon Ji"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2600.pdf"
tags: ["query:stereo-depth"]
score: 4.0
evidence: 面向手机双摄的极线约束交叉注意力立体处理
tldr: 手机双摄模块硬件异构常导致非对称模糊，而已有方法与基准多假设同构立体，未显式处理此类退化。本文构建基于真实手机立体拍摄的异构立体去模糊数据集，并提出物理与极线约束的交叉注意力模块PECA，将跨视角匹配限制在极线搜索窗口内。实验显示该轻量模块能有效抑制非对称模糊并提升立体匹配质量，对手机双摄成像与立体处理有参考价值。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 3450, \"height\": 1350}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 1280, \"height\": 720}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-006.webp\", \"caption\": \"\", \"page\": 4, \"index\": 6, \"width\": 507, \"height\": 365}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-007.webp\", \"caption\": \"\", \"page\": 13, \"index\": 7, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-008.webp\", \"caption\": \"\", \"page\": 13, \"index\": 8, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-009.webp\", \"caption\": \"\", \"page\": 13, \"index\": 9, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-010.webp\", \"caption\": \"\", \"page\": 13, \"index\": 10, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-011.webp\", \"caption\": \"\", \"page\": 13, \"index\": 11, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-012.webp\", \"caption\": \"\", \"page\": 13, \"index\": 12, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-013.webp\", \"caption\": \"\", \"page\": 13, \"index\": 13, \"width\": 485, \"height\": 273}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-014.webp\", \"caption\": \"\", \"page\": 13, \"index\": 14, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-015.webp\", \"caption\": \"\", \"page\": 13, \"index\": 15, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-016.webp\", \"caption\": \"\", \"page\": 13, \"index\": 16, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-017.webp\", \"caption\": \"\", \"page\": 13, \"index\": 17, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-018.webp\", \"caption\": \"\", \"page\": 13, \"index\": 18, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-019.webp\", \"caption\": \"\", \"page\": 13, \"index\": 19, \"width\": 579, \"height\": 325}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-020.webp\", \"caption\": \"\", \"page\": 13, \"index\": 20, \"width\": 485, \"height\": 273}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-021.webp\", \"caption\": \"\", \"page\": 13, \"index\": 21, \"width\": 485, \"height\": 273}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-022.webp\", \"caption\": \"\", \"page\": 13, \"index\": 22, \"width\": 485, \"height\": 273}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-023.webp\", \"caption\": \"\", \"page\": 13, \"index\": 23, \"width\": 485, \"height\": 273}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-024.webp\", \"caption\": \"\", \"page\": 13, \"index\": 24, \"width\": 485, \"height\": 273}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-025.webp\", \"caption\": \"\", \"page\": 14, \"index\": 25, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-026.webp\", \"caption\": \"\", \"page\": 14, \"index\": 26, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-027.webp\", \"caption\": \"\", \"page\": 14, \"index\": 27, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-028.webp\", \"caption\": \"\", \"page\": 14, \"index\": 28, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-029.webp\", \"caption\": \"\", \"page\": 14, \"index\": 29, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-030.webp\", \"caption\": \"\", \"page\": 14, \"index\": 30, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-031.webp\", \"caption\": \"\", \"page\": 14, \"index\": 31, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-032.webp\", \"caption\": \"\", \"page\": 14, \"index\": 32, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-033.webp\", \"caption\": \"\", \"page\": 14, \"index\": 33, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-034.webp\", \"caption\": \"\", \"page\": 14, \"index\": 34, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-035.webp\", \"caption\": \"\", \"page\": 14, \"index\": 35, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-036.webp\", \"caption\": \"\", \"page\": 14, \"index\": 36, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-037.webp\", \"caption\": \"\", \"page\": 14, \"index\": 37, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-038.webp\", \"caption\": \"\", \"page\": 14, \"index\": 38, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-039.webp\", \"caption\": \"\", \"page\": 14, \"index\": 39, \"width\": 523, \"height\": 294}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-f6de52e749486f6e0dad6ef6/fig-040.webp\", \"caption\": \"\", \"page\": 14, \"index\": 40, \"width\": 523, \"height\": 294}]"
motivation: 手机双摄硬件异构导致非对称模糊，现有方法与基准多假设同构立体设置，难以应对真实退化。
method: 构建真实手机立体拍摄的异构去模糊数据集，并提出受物理与极线约束的交叉注意力模块PECA。
result: PECA以轻量结构限制跨视角匹配范围，在异构立体去模糊任务上取得更优的清晰度与匹配效果。
conclusion: 为手机双摄非对称退化提供了数据与算法基准，可迁移到立体深度与立体匹配相关流程。
---

## Abstract
Modern stereo-capable smartphones enable immersive XRcontent capture. However, hardware heterogeneity across camera mod-ules often causes severe asymmetric blur artifacts. Existing methods andbenchmarks largely assume homogeneous stereo setups and therefore donot explicitly address such asymmetric degradation. To bridge this gap,we present a dedicated framework for heterogeneous stereo deblurring.First, we introduce the heterogeneous stereo deblurring (HSD) dataset,constructed from real smartphone stereo captures via multi-frame inte-gration. Second, we propose physically- and epipolar-constrained crossattention (PECA), a lightweight module that restricts cross-view match-ing to an epipolar search window bounded by an optics-derived dis-parity upper bound. By enforcing physically valid disparity constraints,PECA enables efficient and reliable cross-view feature fusion. Moreover,our confidence-weighted attention with residual fusion emphasizes cross-guided deblurring when correspondences are reliable, while naturallyfalling back to self-deblurring in occluded or unreliable regions. PECAis architecture-agnostic and consistently improves CNN-, Transformer-,and NAFNet-based baselines. Extensive experiments on HSD show thatPECA-enhanced models achieve improved restoration performance withfavorable efficiency. The dataset and source code are publicly released athttps://github.com/shinhoju/PECA.

---

## 论文详细总结（自动生成）

# 论文总结：面向异构立体去模糊的基准与物理/极线约束交叉注意力（PECA）

## 1. 核心问题与研究动机

- **背景**：现代智能手机普遍采用异构多摄系统（主摄 wide + 超广角 ultra-wide 等），并支持立体拍摄以服务 XR、双目显示等 3D 应用。
- **核心痛点**：手机并非经过标定的同构立体设备。主摄通常光圈更大且配备 OIS，超广角光圈较小且缺乏专用防抖，导致同一时刻两视角出现**系统性非对称模糊**（主摄清晰、超广角模糊）。
- **现有方法缺口**：
  - 多数立体复原工作（立体去模糊、立体超分）建立在**同构相机假设**上，采用对称建模，跨视角对应主要用于解决几何错位或相似退化视图间的细节迁移。
  - 已有异构多摄工作虽利用跨相机互补性，但多基于**未校正立体数据**，依赖全局稠密对应估计或迭代对齐，计算开销大且对传感器异构敏感。
  - 缺乏针对**校正后（rectified）异构立体**、以非对称模糊为主要目标的专用框架与基准。
- **整体含义**：论文主张把"硬件导致的模糊不对称"作为首要复原目标，并在设备级真实流水线约束（原生校正输出）下开展研究，同时提出配套数据集与轻量融合模块。

## 2. 方法论

### 2.1 核心思想与三条设计原则

- **(i) 非对称复原**：wide 视图作为清晰参考，ultra-wide 作为待复原目标，跨视角交互应是选择性的，而非强制对称复原。
- **(ii) 几何与物理约束的对应搜索**：校正使有效匹配限于极线扫描行；立体几何决定视差方向；相机参数给出物理可行的视差上界。
- **(iii) 无需显式匹配或掩码的鲁棒融合**：不做稠密匹配、不预测遮挡掩码，依靠置信度加权注意力 + 残差融合自然衰减不可靠区域。

### 2.2 网络总体框架

- 双分支编码器：主分支编码模糊超广角 $I_{UW} \to F_{UW}$；参考分支编码清晰 wide $I_W \to F_W$。
- PECA 模块在物理与几何约束的极线窗口内检索跨视角特征，经残差融合注入主分支，再由解码器输出复原图 $I'_{UW}$。

### 2.3 PECA 关键技术细节

- **特征嵌入**：以 1×1 逐点卷积将 $F_{UW}$、$F_W$ 映射到共享空间，
  $Q = \mathrm{Proj}(F_{UW}; W_q)$，$K = \mathrm{Proj}(F_W; W_k)$，$V = \mathrm{Proj}(F_W; W_v)$。
  query 来自退化视图，key/value 来自清晰参考，从结构上保证非对称检索。
- **物理视差上界**：设 $d^W_{min}$、$d^{UW}_{min}$ 为两相机最小对焦距离，定义有效最小采集距离 $d_{eff} = \max(d^W_{min}, d^{UW}_{min})$。结合基线 $B$ 与像素焦距 $f$，最大物理可行视差约为 $f\cdot B / d_{eff}$；在特征分辨率下按下采样因子 $S$ 缩放得
  $D_{phys} = \lfloor (f \cdot B / d_{eff}) \times 1/S \rfloor$。
  文中 W/UW 对的输入级视差上界约 **70 像素**，$S=4$ 时 $D_{phys} \approx 17$。
- **极线约束注意力**：由于校正后对应点位于同一行且视差方向单一，定义局部 1D 搜索窗
  $\Omega_{i,j} = \{(i,k) \mid j - D_{max} \le k \le j\}$，其中 $D_{max} \le D_{phys}$。
  跨视角特征为窗口内余弦相似度加权的 value 聚合：
  $F_{cross}(i,j) = \sum_{(i,k)\in\Omega_{i,j}} \mathrm{Softmax}_k\!\left(\frac{D_{cos}(Q_{i,j}, K_{i,k})}{\tau}\right) V_{i,k}$，
  $\tau$ 为控制注意力尖锐程度的温度。
- **置信度调制行为**：对应可靠时权重集中 → 强引导；遇遮挡、纹理歧义或残余校正误差时权重扩散 → 引导弱化，自然回退到自去模糊。
- **复杂度**：全局 2D 注意力 $O((HW)^2)$ → 全行 1D 注意力 $O(HW^2)$ → PECA $O(HW \cdot D_{max})$，实际 $D_{max} \ll W$。
- **互补特征融合**：$F_{fuse} = F_{UW} + \mathrm{Proj}(F_{cross}; W_{cross})$，残差形式相当于软性、数据自适应门控。
- **架构无关性**：模块可直接嵌入 CNN / Transformer / NAFNet 类骨干。

### 2.4 HSD 基准构建流程

- 使用商用手机（iPhone 15 Pro Max、iPhone 16 系列、iPhone 17）的立体拍摄模式，采集同步 wide/ultra-wide 视频，直接采用**设备原生流水线输出的校正结果**，不做额外标定。
- **模糊生成**：沿用 Nah 等人的时间积分协议，对目标时刻 $t$ 前后共 **11 帧**超广角帧取平均模拟长曝光积分；中心帧为 GT，同时刻 wide 帧作为清晰参考。因拍摄时相机运动平稳，模糊呈深度相关、空间变化而非均匀，避免低帧率平均的离散台阶伪影。
- **数据筛选**：计算积分模糊图与清晰超广角帧的 PSNR，**丢弃 PSNR > 33 dB** 的近静态样本，确保基准具有挑战性。
- **划分**：384 个场景按序列级划分，256 训练 / 128 测试；最终采样 **2200 训练对 / 1100 测试对**。分辨率从 1080×1920 双三次下采样到 **720×1280**。
- 明确说明**未建模卷帘快门效应**，需依赖设备相关读出与 ISP 假设。

## 3. 实验设计

- **数据集/场景**：自建 HSD 基准（室内外、不同光照与深度分布）；另加真实手持异构立体拍摄序列做定性评估（无 GT）。
- **对比骨干与变体**：三种代表性架构 —— CNN 的 **XYDeblur**、Transformer 的 **Restormer**、简化的 **NAFNet**；每种比较四个变体：
  1. 单图 baseline；
  2. 通道扩展（channel-expansion，单图增容）；
  3. 朴素立体拼接（stereo concatenation）；
  4. **+PECA（本文）**。
- **训练配置**：PyTorch，400K 迭代，batch size 8，AdamW + 余弦退火；学习率/权重衰减按骨干分别设为 XYDeblur（1e-4 / 1e-3）、Restormer（3e-4 / 1e-4）、NAFNet（5e-4 / 1e-3）；随机裁剪 128×128（XYDeblur、Restormer）与 256×256（NAFNet）；含 gamma 与 shot/read 噪声增强。
- **公平性控制**：为公平比较，所有骨干最深隐层特征固定为 **32×32**（NAFNet 配为三级结构，Restormer 去掉第四编码阶段前的下采样）；统一使用 $\tau = 0.01$、$D_{max} = 5$；MACs 在 720×1280 输入下测量。
- **消融实验**：
  - 注意力搜索空间对比：全局 2D / 全行 1D / PECA（三者仅搜索空间不同，投影层与相似度设置一致）。
  - 参数敏感性：$D_{max}$ 从 3 到 16 与 $\tau \in \{1.0, 0.1, 0.01, 0.001\}$ 的 PSNR/SSIM 热力图（XYDeblur 骨干）。
  - 补充材料：严重遮挡分析、top-3 注意力分布分析、额外定性结果。

## 4. 资源与算力

- 文中仅说明：**PyTorch 实现，在 NVIDIA GPU 上训练**，每个骨干训练 **400K 迭代、batch size 8**。
- **未明确给出** GPU 型号、数量、单卡/多卡配置、总训练时长、显存占用与总 GPU 小时数；也未报告推理时延等部署侧指标（仅以 MACs 与参数量衡量效率）。因此算力成本无法从论文中精确复原。

## 5. 实验数量与充分性

- **定量实验规模**：3 骨干 × 4 变体 = 12 组主要结果（PSNR/SSIM/Params/MACs）；消融 3 组搜索空间对比；1 组 $D_{max}$×$\tau$ 网格敏感性分析（14×4 个配置）；补充材料含遮挡与注意力分布分析。
- **定性实验**：HSD 配对样本对比（含大尺度模糊、透明塑料膜、细小文字三个放大区域）+ 真实手持序列对比（3 骨干 × 有/无 PECA）。
- **充分性评价**：
  - **较充分**：跨三种架构范式的验证有效支撑了"backbone-agnostic"主张；变体设置（通道扩展 vs 拼接 vs PECA）能较好地把增益归因于结构化跨视角检索而非单纯增容；搜索空间消融直接验证了物理约束的必要性。
  - **客观与公平性较好**：统一 latent 分辨率、统一超参、参数量尽量对齐、MACs 同分辨率测量。
  - **覆盖不足**：仅在一个自建数据集上定量评估，未在 GoPro/REDS/RealBlur/HIDE 或已有立体去模糊基准上交叉验证；真实手持场景只有定性、无定量；未与已有异构多摄方法（如 hybrid camera deblurring、asymmetric dual-lens video deblurring、NAFSSR/iPASSR 等）做直接数值对比，比较对象主要是自建变体。

## 6. 主要结论与发现

- 引入同步 wide/ultra-wide 参考在所有骨干上均优于单图 baseline（如 XYDeblur 拼接版 +1.20 dB），说明跨视角信息对非对称去模糊有效。
- **PECA 增益并非来自容量**：通道扩展模型参数更多、MACs 更高却仍逊于 PECA（Restormer 上 PECA 比通道扩展高 **+1.30 dB** 且计算更省）。
- 相比朴素立体拼接，PECA 持续更优（NAFNet 上 **+0.68 dB**），说明显式建模跨视角对应关系比简单特征融合更关键。
- 定量结果示例：XYDeblur 30.76→**32.22 dB**（SSIM 0.9444→0.9620）；Restormer 30.94→**32.47 dB**；NAFNet 32.16→**32.92 dB**（SSIM 0.9669）。
- **搜索空间消融**：全局 2D 注意力 30.72 dB（模块 852.2G MACs）；全行 1D 注意力 30.75 dB（7.6G MACs，仅 +0.03 dB）；PECA **32.22 dB**（2.9G MACs），相比全局提升 +1.50 dB、相比全行提升 +1.47 dB。原因：模糊削弱高频判别性、行内模式重复，导致全行搜索注意力弥散。
- **参数敏感性**：$\tau = 0.01$ 时，$D_{max}$ 从 3 到 16 均表现稳健，XYDeblur 上最佳为 $D_{max}=9$；小温度使注意力更尖锐、更能隔离可靠对应；大温度（如 1.0）导致权重弥散、性能下降，此时扩大窗口反而引入更多歧义候选。
- **定性**：PECA 在大尺度模糊、透明薄膜、细小文字等区域恢复出更锐利的边缘与纹理，避免过度平滑；在真实手持强模糊场景下同样保持结构清晰。

## 7. 优点

- **问题定位精准**：把"硬件异构导致的非对称模糊"从被忽略的工程现象提升为明确的复原目标，并配套真实设备流水线（原生校正输出）的数据构建协议。
- **物理先验嵌入注意力**：用最小对焦距离、基线、焦距推导视差上界 $D_{phys}$，再结合校正几何给出**单向 1D 极线窗口**，把"物理可行"与"计算高效"统一起来，而非依赖学习式的全局稠密匹配。
- **复杂度显著下降**：$O(HW D_{max})$，注意力模块 MACs 从 852.2G 降到 2.9G（约 294× 降幅），精度反而更高，工程可部署性强。
- **无需匹配与掩码的鲁棒性设计**：用注意力分布的尖锐/弥散隐式表达置信度，配合残差融合形成软门控，避免显式遮挡掩码带来的额外开销与误差敏感性。
- **架构无关**：在 CNN、Transformer、NAFNet 三类范式上一致有效，通用性论证较扎实。
- **公平性控制细致**：统一隐层分辨率、统一超参、参数量对齐，并设置通道扩展对照组以排除"增容即增益"的替代解释。
- **可复现性**：数据集与代码已开源（github.com/shinhoju/PECA）。

## 8. 不足与局限

- **模糊合成的真实性缺口**：超广角模糊由 11 帧时序积分合成，依赖拍摄时"稳定运动"假设；论文明确**未建模卷帘快门**，与真实曝光退化仍有差距，可能低估或简化真实退化分布。
- **分辨率与画质损失**：图像从 1080×1920 下采样至 720×1280 以控制噪声与复杂度，未验证在全分辨率下的有效性。
- **真实场景仅定性**：真实手持序列无 GT，只能做视觉对比，缺乏客观指标支撑其在实际

……部署环境中的鲁棒性与泛化性。

- **缺乏与既有异构/立体复原方法的直接数值对比**：对比对象主要是自建变体（单图、通道扩展、朴素拼接），未与已有异构多摄去模糊、非对称双镜头视频去模糊、立体超分类方法（如 NAFSSR/iPASSR 等）在同一基准上做横向数值比较，因而难以判断 PECA 相对现有技术路线的绝对优势幅度。
- **定量评估仅限单一自建基准**：未在 GoPro、REDS、RealBlur、HIDE 等通用去模糊数据集或已有立体去模糊基准上交叉验证，跨数据集泛化能力缺乏证据；HSD 本身由同一批 iPhone 机型采集，存在设备与 ISP 偏置，对其他品牌、其他焦距组合（如长焦-主摄、三摄系统）的迁移性未知。
- **视差上界的先验依赖较强**：$D_{phys}$ 需要基线 $B$、像素焦距 $f$、两相机最小对焦距离 $d_{min}$ 等参数，这些量依赖厂商元数据与设备标定口径；论文直接采用设备原生校正输出而未重新标定，若元数据缺失或有误差，物理上界的正确性会受影响。文中也未系统分析这些参数误差对 $D_{max}$ 设置与最终性能的敏感度。
- **超参设置与最佳值存在偏差**：所有实验统一固定 $D_{max}=5$，而敏感性分析显示 XYDeblur 上最佳为 $D_{max}=9$；说明统一设置是为公平性服务的折中，可能未充分释放 PECA 的潜力，也未报告按骨干分别调参后的上限。
- **遮挡与歧义处理仍是隐式的**：虽然以注意力权重弥散来隐式弱化不可靠对应，但论文未给出显式的遮挡判定或失败案例分析（仅在补充材料中做严重遮挡分析），在强遮挡、重复纹理、大面积无纹理区域的行为边界尚不清晰。
- **未利用时间维度**：数据源为立体视频，但方法在单帧对上工作，未探索时序一致性、多帧聚合或视频去模糊设定下的增益；这与"手机立体视频拍摄"的实际应用场景存在落差。
- **未建模卷帘快门与传感器差异**：论文已明确声明，但这意味着合成退化与真实退化之间存在系统性偏差，尤其在快速运动下会低估真实模糊的复杂性；两相机之间可能存在的曝光时间、增益、色彩响应差异也未纳入建模。
- **评测指标偏传统**：仅报告 PSNR/SSIM，未使用 LPIPS、DISTS 等感知指标，也未做用户主观研究；对于强调"锐利边缘与纹理恢复"的定性主张，感知层面缺乏量化支撑。
- **效率评估维度单一**：仅报告参数量与 MACs，未给出实际推理时延、显存占用与端侧部署可行性验证，而论文动机之一正是手机端应用。
- **算力与训练成本披露不足**：GPU 型号、卡数、总训练时长均未报告，影响复现成本估计与结果可比性。

## 9. 启示与可拓展方向

- **将物理上界推广到更一般的相机组合**：把 $D_{phys}$ 的推导从 wide/ultra-wide 对扩展到长焦-主摄、三摄乃至异构多摄阵列，并研究各对之间的窗口大小自适应分配。
- **参数不确定性下的鲁棒注意力**：可将 $d_{min}$、$B$、$f$ 的标称误差建模为窗口范围的软先验（如对 $D_{max}$ 施加可学习或概率化的膨胀），减少对元数据精度的硬依赖。
- **时序扩展**：在 PECA 基础上引入跨帧极线-时序联合注意力，利用视频中多帧 wide 参考提升超广角复原的稳定性，抑制闪烁。
- **显式置信度建模**：把注意力熵或 top-k 权重作为可监督信号，与遮挡/光度不一致检测联合训练，使隐式软门控获得更明确的语义。
- **更真实的退化合成**：纳入卷帘快门、双相机曝光/增益差异、镜头暗角与色差，缩小合成-真实域差，或采用域自适应/自监督方式在真实数据上微调。
- **多数据集与跨设备基准扩展**：在 HSD 上引入更多机型与焦距组合，并与其他去模糊基准做交叉评测，形成更具公信力的异构立体复原评测协议。

## 10. 总体评价

论文的核心贡献是**问题重构 + 轻量物理先验注意力 + 配套真实设备基准**三者的组合。它把"手机异构双摄带来的非对称模糊"从工程副作用提升为明确的研究对象，并在设备原生校正输出这一强约束下，用极线几何与视差物理上界把跨视角检索压缩到一条极线上的短窗口，从而在精度提升的同时将注意力模块计算量降低约两个数量级。搜索空间消融（全局 2D / 全行 1D / PECA）是全文最有说服力的证据：它清楚表明增益来自"正确约束下的对应搜索"，而非容量堆叠或全局注意力，这一点配合通道扩展对照组的设置，使结论具有较好的因果说服力。跨 CNN/Transformer/NAFNet 三种骨干的一致有效性，也支撑了其架构无关性主张。

同时，论文的边界也较清晰：验证集中在单一自建基准，真实场景仅定性，退化合成未含卷帘快门，视差上界依赖设备元数据，评测停留在 PSNR/SSIM，效率只以 MACs 衡量。因此其结论更应被理解为"在受控且贴近真实流水线的异构立体设定下，物理约束注意力是有效且高效的"，而非"在任意真实退化下均已超越现有方法"。对后续工作而言，最有价值的延伸方向是：把该物理约束框架推广到多摄与视频设定，补齐与现有方法的横向对比，并缩小合成-真实域差。

（完）
