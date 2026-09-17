---
title: "Any to Full: Prompting Depth Anything for Depth Completion in One Stage"
title_zh: Any to Full：以提示方式驱动 Depth Anything 的单阶段深度补全
authors: "Zhiyuan Zhou, Ruofeng Liu, TAICHI LIU, Weijian Zuo, Shanshan Wang, Zhiqing Hong, Desheng Zhang"
date: 2026-09-08
pdf: "https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/3196.pdf"
tags: ["query:mono-depth"]
score: 8.0
evidence: 提示 Depth Anything 完成单阶段深度补全
tldr: 机器人感知需要稠密深度，但廉价传感器常给出稀疏或不完整的测量，现有 RGBD 融合补全方法泛化性差，而借助单目深度估计模型的两阶段方案又需要显式相对到度量对齐，带来额外计算与结构性失真。Any2Full 提出单阶段、域通用且与稀疏模式无关的框架，直接提示 Depth Anything 完成深度补全。实验表明该方法在多种深度模式下具备更强的域泛化与鲁棒性，为深度补全提供了简洁高效的新范式。
source: ECCV-2026-Accepted-Program
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-001.webp\", \"caption\": \"\", \"page\": 2, \"index\": 1, \"width\": 551, \"height\": 495}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-002.webp\", \"caption\": \"\", \"page\": 2, \"index\": 2, \"width\": 622, \"height\": 339}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-003.webp\", \"caption\": \"\", \"page\": 2, \"index\": 3, \"width\": 1811, \"height\": 1113}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-004.webp\", \"caption\": \"\", \"page\": 2, \"index\": 4, \"width\": 904, \"height\": 332}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-005.webp\", \"caption\": \"\", \"page\": 2, \"index\": 5, \"width\": 568, \"height\": 494}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-006.webp\", \"caption\": \"\", \"page\": 6, \"index\": 6, \"width\": 1456, \"height\": 578}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-007.webp\", \"caption\": \"\", \"page\": 6, \"index\": 7, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-008.webp\", \"caption\": \"\", \"page\": 6, \"index\": 8, \"width\": 642, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-009.webp\", \"caption\": \"\", \"page\": 6, \"index\": 9, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-010.webp\", \"caption\": \"\", \"page\": 6, \"index\": 10, \"width\": 913, \"height\": 550}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-011.webp\", \"caption\": \"\", \"page\": 6, \"index\": 11, \"width\": 914, \"height\": 549}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-012.webp\", \"caption\": \"\", \"page\": 6, \"index\": 12, \"width\": 480, \"height\": 548}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-013.webp\", \"caption\": \"\", \"page\": 6, \"index\": 13, \"width\": 1468, \"height\": 255}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-014.webp\", \"caption\": \"\", \"page\": 6, \"index\": 14, \"width\": 1832, \"height\": 261}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-015.webp\", \"caption\": \"\", \"page\": 12, \"index\": 15, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-016.webp\", \"caption\": \"\", \"page\": 12, \"index\": 16, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-017.webp\", \"caption\": \"\", \"page\": 12, \"index\": 17, \"width\": 642, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-018.webp\", \"caption\": \"\", \"page\": 12, \"index\": 18, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-019.webp\", \"caption\": \"\", \"page\": 12, \"index\": 19, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-020.webp\", \"caption\": \"\", \"page\": 12, \"index\": 20, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-021.webp\", \"caption\": \"\", \"page\": 12, \"index\": 21, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-022.webp\", \"caption\": \"\", \"page\": 12, \"index\": 22, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-023.webp\", \"caption\": \"\", \"page\": 12, \"index\": 23, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-024.webp\", \"caption\": \"\", \"page\": 12, \"index\": 24, \"width\": 1216, \"height\": 352}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-025.webp\", \"caption\": \"\", \"page\": 12, \"index\": 25, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-026.webp\", \"caption\": \"\", \"page\": 12, \"index\": 26, \"width\": 640, \"height\": 480}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-027.webp\", \"caption\": \"\", \"page\": 12, \"index\": 27, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-028.webp\", \"caption\": \"\", \"page\": 12, \"index\": 28, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-029.webp\", \"caption\": \"\", \"page\": 12, \"index\": 29, \"width\": 1448, \"height\": 1048}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-030.webp\", \"caption\": \"\", \"page\": 12, \"index\": 30, \"width\": 612, \"height\": 443}, {\"url\": \"assets/figures/eccv-2026-accepted-program/eccv-2026-d2b8e884d3bbba294e576d79/fig-031.webp\", \"caption\": \"\", \"page\": 12, \"index\": 31, \"width\": 640, \"height\": 480}]"
motivation: 廉价传感器深度稀疏不完整，现有补全方法泛化差，两阶段单目先验方案引入额外计算与失真。
method: 提出单阶段、域通用且与稀疏模式无关的 Any2Full 框架，直接提示 Depth Anything 完成深度补全。
result: 在多种深度模式下展现更强的域泛化与鲁棒性，避免结构性失真。
conclusion: 为深度补全提供了简洁高效的集成范式。
---

## Abstract
Accurate, dense depth estimation is crucial for robotic per-ception, but commodity sensors often yield sparse or incomplete measure-ments due to hardware limitations. Existing RGBD-fused depth comple-tion methods learn priors jointly conditioned on training RGB distri-bution and specific depth patterns, limiting domain generalization androbustness to various depth patterns. Recent efforts leverage monoculardepth estimation (MDE) models to introduce domain-general geomet-ric priors, but current two-stage integration strategies relying on explicitrelative-to-metric alignment incur additional computation and introducestructured distortions. To this end, we present Any2Full, a one-stage,domain-general, and pattern-agnostic framework that reformulates com-pletion as a scale-prompting adaptation of a pretrained MDE model.To address varying depth sparsity levels and irregular spatial distribu-tions, we design a Scale-Aware Prompt Encoder. It distills scale cuesfrom sparse inputs into unified scale prompts, guiding the MDE modeltoward globally scale-consistent predictions while preserving its geomet-ric priors. Extensive experiments demonstrate that Any2Full achievessuperior robustness and efficiency. It outperforms OMNI-DC by 32.2%in average AbsREL and delivers a 1.4× speedup over PriorDA with thesame MDE backbone, establishing a new paradigm for universal depthcompletion. Codes and checkpoints are available at https://github.com/zhiyuandaily/Any2Full.

---

## 论文详细总结（自动生成）

# Any2Full 论文总结

## 1. 核心问题与整体含义

- **研究动机**：机器人感知需要精确稠密的深度信息，但商品化深度传感器（LiDAR、ToF、结构光相机）受分辨率、量程、光线反射/吸收等硬件限制，常输出稀疏或不完整的深度图，因此**深度补全**（从稀疏深度与 RGB 恢复稠密度量深度）成为基础任务。
- **现有方法的局限**：
  - **传统 RGBD 融合方法**（如 CompFormer）联合基于训练 RGB 分布与特定深度模式学习先验，导致两类问题：①**域特定性**——光照、纹理、场景变化时性能骤降；②**深度模式敏感性**——面对不同传感器导致的密度变化、缺失区域、量程限制时鲁棒性差。
  - **引入 MDE 的两阶段方案**（如 PriorDA）：先预测粗深度，再精修。但显式的"相对深度→度量深度"对齐存在**尺度不一致**（相对深度存在非线性畸变，需要空间变化的尺度因子），会引入**结构性失真与模式特定偏差**，且带来额外计算开销。
  - **测试时自适应方法**（如 Marigold-DC、TestPromptDC）虽精度高，但推理代价大，难以实时应用。
- **核心问题**：如何绕过中间粗深度生成，在**单阶段**内无缝集成 MDE 的几何先验，实现**域通用且模式无关**的深度补全？
- **整体含义**：论文提出 Any2Full，将深度补全重新表述为对预训练 MDE 模型的**尺度提示（scale-prompting）自适应**，为通用深度补全建立新范式。

## 2. 方法论

- **核心思想**：冻结预训练 MDE 骨干（Depth Anything v2），从稀疏深度中蒸馏**尺度线索（点间尺度比）**，形成统一的尺度提示去调制 MDE 特征，使其输出**尺度一致的相对深度**（即整幅场景可用单一全局尺度与偏置对齐到度量深度），再通过非参数最小二乘拟合恢复稠密度量深度。
- **一阶段定义**：单次前向推理，无中间深度预测或辅助精修网络；最终度量深度由闭式对齐获得，不引入额外可学习模块。
- **关键挑战**：稀疏输入不仅密度多变，且空间分布不规则（随机缺失区域），导致训练不稳定与模式特定过拟合。
- **尺度感知提示编码器（SAPE）**，两个层级模块：
  - **局部增强模块（Local Enrichment）**：将 patch 级深度特征 $f_{dep,i}$ 与对应的 MDE 几何特征 $f_{mde,i}$ 通过广义 **FiLM** 机制耦合，锚定尺度线索到 MDE 隐空间：
    $$f_{loc,i} = \gamma(f_{dep,i}, f_{mde,i}) \odot f_{mde,i} + \beta(f_{dep,i}, f_{mde,i})$$
    其中 $\gamma,\beta$ 由轻量 MLP 预测。此设计对稀疏度变化鲁棒。
  - **全局传播模块（Global Propagation）**：以 $F_{loc}$ 为初始状态，通过 $L$ 个几何引导的 Transformer 块扩散，层数与 MDE 编码器组对应。**关键设计**：注意力权重（Q、K）完全来自 MDE 几何特征 $F_{mde}$，仅将 $F_{glo}$ 作为 Value，使尺度线索沿 RGB 几何结构扩散，而非受稀疏采样模式偏置。首个 Transformer 块采用掩码注意力，约束尺度信息从有效深度位置向几何一致区域传播。
  - **尺度提示融合（Scale Prompt Fusion）**：将多层级尺度提示 $\{F^1_{glo},...,F^L_{glo}\}$ 通过分层 FiLM 注入 MDE 解码器：
    $$F'^{\phi(l)}_{mde} = \gamma_l(F^l_{glo}) F^{\phi(l)}_{mde} + \beta_l(F^l_{glo}, F^{\phi(l)}_{mde})$$
    在多个语义层级注入，既提升尺度一致性，又最小化对原始 MDE 表示的改动以保留域通用先验。
- **效率设计**：传播块数量与 MDE 解码器层级对齐；在最低层编码器-解码器层省略传播与提示（该层主要捕捉局部纹理而非结构几何）。
- **训练**：
  - 数据：高质量合成数据集（Hypersim 60K 室内、VKITTI2 10K 室外、TartanAir 15K），采用**随机采样**与**孔洞采样**两种策略随机选择，保证模式多样性。
  - 损失：尺度与平移不变损失 $L_{ssi}$（全局一致性）、梯度匹配损失 $L_{gm}$（边缘保持）、有效深度锚点上的 $L_{anchor}$（稀疏输入对齐）、相对结构 SSIM 损失 $L_{r\text{-}ssim}$，加权求和。
  - 训练细节：冻结 MDE 骨干，仅训练 SAPE；224K 步，10K 预热，余弦调度器；batch size 16；Adam，学习率 5e-5。

## 3. 实验设计

- **数据集/场景**（零样本评估，无数据集特定微调）：
  - **NYU-Depth V2**：室内 Kinect，654 测试样本，304×228。
  - **iBims-1**：室内激光扫描，高精度几何，量程达 50m，100 张，640×480。
  - **KITTI DC**：室外驾驶，稀疏 LiDAR，1216×352，1000 验证样本。
  - **DIODE**：室内外大规模 FARO 激光扫描，量程达 350m，771 样本。
  - **ETH3D**：多视图立体，高分辨率室内外，High-res DSLR 集（11 场景，390 图）。
  - **VOID**：Intel RealSense D435i 室内序列，含运动模糊与低纹理，800 测试样本，三种稀疏协议（1500/500/150）。
  - **Logistic-Black（自采集真实数据）**：机器人仓库场景，Vzense DS77C Pro ToF 相机，114 对 RGB-D，1448×1048，黑色包裹吸收红外光导致缺失区域。
- **深度模式**：Hole（孔洞）、Range（量程截断，仅保留 20–80% 有效深度）、Sparse-Random、Sparse-LiDAR（64 线）、Sparse-SfM（COLMAP 投影）、Mixed（真实数据集）。
- **对比方法**：
  - 域特定深度补全：CompFormer、DepthPrompt；
  - 域通用 MDE：Depth Anything v2、Marigold；
  - 域通用方法：PromptDA（深度超分）、Marigold-DC、TestPromptDC、PriorDA、OMNI-DC。
- **评价指标**：AbsREL、RMSE（米），在有效像素上计算。

## 4. 资源与算力

- 论文明确提到训练使用 **4 块 NPU**（表述为"相当于高端 GPU 集群"），batch size 16，训练 224K 步，含 10K 预热。
- 效率对比实验的推理延迟在**单块 NVIDIA RTX P40 GPU** 上测得（100 张 640×480 图像）。
- **未明确说明**：具体 NPU/GPU 型号、总训练时长（小时/天）、显存占用等细节。文中只给出"四个 NPU"这一模糊表述，算力信息不够充分。

## 5. 实验数量与充分性

- **实验规模较大**：覆盖 6 个公开基准 + 1 个自采集真实数据集，跨室内外、多种传感器与 6 种深度模式。
- **主要实验组**：
  - 主对比（Tab. 1）：跨 7 个数据集的完整 AbsREL/RMSE 对比，含平均排名。
  - 效率对比（Tab. 2）：参数量、延迟、精度。
  - 跨骨干泛化（Tab. 3）：MoGe-2-Base 验证 SAPE 不依赖特定 MDE 架构。
  - 稀疏鲁棒性（Tab. 4）：VOID 1500/500/150 与 KITTI 64/16/4 线。
  - 量程鲁棒性（Fig. 4）：NYU 与 KITTI 不同深度区间。
  - 消融实验（Tab. 5）：SP/LE/GP 逐项去除，覆盖多模式与多稀疏度。
  - 真实部署：仓库抓取成功率从 28% 提升至 91.6%。
- **充分性与公平性**：
  - 消融覆盖了核心模块，跨骨干与跨稀疏度/量程验证较全面，真实场景部署增强了实用说服力。
  - 所有方法统一零样本评估，DA 系列统一使用 DA-v2-Large 骨干，对比相对公平。
  - 但**未报告多次运行的方差或置信区间**；部分结论（如"DA-L 不一定优于 DA-B"）归因于真值粗糙，属推测，缺乏直接验证。

## 6. 主要结论与发现

- Any2Full 在平均 AbsREL 上**超越 OMNI-DC 32.2%**；在相同 MDE 骨干下相比 PriorDA 实现 **1.4× 加速**（0.49s vs 0.68s）且精度更高。
- 在全部评估场景中取得**最低平均排名（2.3）**，在每个数据集上均居前列。
- 最小变体（DA-S）仍超越所有先前深度补全方法，推理仅 0.09s，约比 PriorDA 快 7×、比 TestPromptDC 快约 1000×。
- 对未见过的 Range 模式、极端稀疏（VOID-150）、4 线 LiDAR 等均表现出强鲁棒性；PriorDA/OMNI-DC 在 Range 模式出现明显伪影（如 IBims-Range 的噪点、KITTI-Range 的深度环）。
- SAPE 可无缝迁移到 MoGe-2 骨干，验证方法的通用性。
- 真实部署中，黑色包裹抓取成功率从 28% 提升至 91.6% 且无损伤。

## 7. 优点

- **范式创新**：将深度补全重新表述为 MDE 的尺度提示自适应，避免中间粗深度与显式相对-度量对齐，从根源上规避结构性失真。
- **设计精巧**：局部增强（FiLM 耦合）+ 全局传播（Q/K 来自 MDE 几何、仅用 Fglo 作 Value）+ 分层 FiLM 融合，有效解耦尺度线索与特定深度模式。
- **高效轻量**：仅增加 <20% 参数（60.6M vs 335.3M），单阶段推理，延迟接近原始 MDE。
- **泛化性强**：跨域、跨深度模式、跨 MDE 骨干、跨稀疏度与量程均表现稳定。
- **实用验证**：真实仓库部署与抓取成功率数据，证明了工业价值。
- **对比公平**：统一零样本协议、统一骨干，指标与排名透明。

## 8. 不足与局限

- **训练数据依赖**：需要高质量合成 RGB-D 对与精确度量真值，真实数据难以直接用于训练。
- **冻结骨干的潜在上限**：MDE 骨干被冻结，可能限制模型在特定域上的进一步提升；论文也观察到 DA-L 并不必然优于 DA-B，归因于真值粗糙

，缺乏直接验证；建议补充多骨干、多真值精度的对照实验以澄清。
  - **尺度提示的表达能力有限**：方法本质假设场景可用**单一全局尺度+偏置**对齐到度量深度。对于存在强烈非线性畸变或分段尺度变化的场景（如超大量程、多传感器拼接），该假设可能不成立，论文未对此类极端情形做压力测试。
  - **自采集数据的可复现性**：Logistic-Black 数据集为自采集，未公开或未详细说明采集/标注流程，外部难以复现其抓取成功率结论。
  - **推理延迟对比口径**：效率实验仅在单块 RTX P40 上以 640×480 测 100 张图，未报告不同分辨率、不同 batch 或 FP16/INT8 量化下的表现，硬件与精度设置单一。
  - **训练成本描述模糊**：仅称"4 块 NPU"，未给出型号、时长、显存、能耗，削弱了效率主张的完整性。
  - **消融粒度**：Tab. 5 主要做模块级去除，缺少对超参（传播层数 $L$、FiLM 维度、各损失权重）的敏感性分析。
  - **失败案例分析不足**：论文报告了 PriorDA/OMNI-DC 在 Range 模式的伪影，但未系统展示 Any2Full 自身的失败案例（如极端反射、透明/镜面材质、动态物体）。

## 9. 启示与展望

- **范式层面的启示**：把"深度补全"从"补洞/超分"重新解释为"对基础模型的尺度条件化"，提示了一条通用路径——**用低维、物理可解释的提示（尺度、位姿、内参）去调制大规模预训练几何模型**，而非在任务数据上重训专用网络。该思路可迁移到法向估计、光流、点云上采样等相关任务。
- **设计层面的启示**：将注意力机制的 Q/K 绑定到冻结骨干的几何特征、仅以任务线索作 Value，是"如何让任务特定信息沿通用几何结构传播而不污染先验"的有效工程范式，值得在其他条件生成任务中借鉴。
- **训练层面的启示**：随机采样与孔洞采样结合的稀疏模式增广，是缓解"模式特定过拟合"的简单而有效手段，说明**数据侧的分布覆盖**往往比架构侧的复杂度更关键。
- **未来方向**：
  - 突破全局单一尺度的假设，探索**空间变化尺度场**或分段尺度的提示形式，以覆盖超大量程与多模态拼接场景。
  - 在保持单阶段的前提下，探索**轻量在线自适应**（如少量测试时统计量更新），兼顾域通用与实时性。
  - 将 SAPE 扩展至**视频/时序**输入，利用时间一致性进一步提升稀疏与遮挡场景的稳定性。
  - 与下游任务（抓取、导航、SLAM）做端到端联合优化，验证尺度提示是否可被任务损失直接监督。
  - 补充公开自采集数据集与完整算力报告，提升可复现性与工业可信度。

## 10. 总体评价

Any2Full 是一篇**问题定位清晰、方法简洁优雅、验证较为扎实**的工作。其核心贡献不在于堆叠模块，而在于一个观念转变：**与其让补全网络去学"如何补洞"，不如让预训练 MDE 去回答"这个洞在哪一尺度上"**。通过 SAPE 的局部 FiLM 耦合、几何引导的全局传播与分层尺度提示融合，方法在保持 MDE 域通用先验的同时注入了稀疏深度的度量线索，从而在跨域、跨模式、跨骨干的评测中稳定领先，并在真实机器人抓取任务上取得了 28%→91.6% 的显著提升。

其主要短板集中在**实验报告的完备性**（算力细节、方差、失败案例、超参敏感性）与**方法假设的边界**（单一全局尺度）上，这些并不动摇核心结论，但限制了结论的外推强度。总体而言，该工作在"基础模型 + 轻量提示"这一趋势下提供了一个干净且具说服力的范例，对通用深度补全及更广泛的几何基础模型适配研究具有较高的参考价值。

（完）
