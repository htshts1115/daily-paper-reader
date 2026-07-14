<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-07-05 ~ 2026-07-14
- 运行时间：2026-07-14 06:50:35 UTC
- 运行状态：成功
- 本次总论文数：30
- 精读区：13
- 速读区：17

### 今日简报（AI）
今日精读两篇深度估计前沿，并速读水下匹配、视觉预训练及开放场景理解等方向。

最值得关注零样本轻量单目深度方案ZipDepth，以及稀疏锚点深度标定的鲁棒校准方法。

建议普通读者优先了解零样本深度估计的实用化进展，后续可关注水下或开放场景理解等新应用。
- 详情：[/20260705-20260714/README](/20260705-20260714/README)

### 精读区论文标签
1. [ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device](/20260705-20260714/2607.08771v1-zipdepth-bringing-lightweight-zero-shot-monocular-depth-anywhere-on-any-device)  
   标签：评分：10.0/10、query:mono-depth
   evidence：面向移动设备的轻量零样本单目深度模型
2. [The Multipath Blind Spot: $K$-Agnostic Robust Calibration for Sparse-Anchor Metric Depth from Frozen Foundations](/20260705-20260714/2607.04101v1-the-multipath-blind-spot-k-agnostic-robust-calibration-for-sparse-anchor-metric-depth-from-frozen-foundations)  
   标签：评分：9.0/10、query:mono-depth
   evidence：从冻结基础模型进行鲁棒度量深度标定
3. [Repurposing CLIP to Localize at Pixel Level](/20260705-20260714/2607.05253v2-repurposing-clip-to-localize-at-pixel-level)  
   标签：评分：9.0/10、query:seg
   evidence：将CLIP重用于像素级开放词汇分割
4. [Realistic Compound-Lens Defocus Blur Synthesis](/20260705-20260714/2607.05837v1-realistic-compound-lens-defocus-blur-synthesis)  
   标签：评分：9.0/10、query:cv-render
   evidence：波光学PSF计算、深度感知散焦渲染、遮挡处理用于模糊合成
5. [From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with Text-to-Image Models](/20260705-20260714/2607.06553v1-from-rgb-generation-to-dense-field-readout-pixel-space-dense-prediction-with-text-to-image-models)  
   标签：评分：9.0/10、query:vfm
   evidence：利用预训练文生图模型进行像素级密集预测（深度、法线、蒙版、抠图）
6. [URS-Stereo: Uncertainty-Guided Residual Search for Real-Time Stereo Matching](/20260705-20260714/2607.06779v1-urs-stereo-uncertainty-guided-residual-search-for-real-time-stereo-matching)  
   标签：评分：9.0/10、query:stereo-depth
   evidence：基于不确定性引导残差搜索的实时粗到细立体匹配
7. [SAM-MT: Real-Time Interactive Multi-Target Video Segmentation](/20260705-20260714/2607.08688v1-sam-mt-real-time-interactive-multi-target-video-segmentation)  
   标签：评分：9.0/10、query:seg
   evidence：开放词汇实时多目标视频分割
8. [REBASE: Reference-Background Subspace Elimination for Training-Free In-Context Segmentation](/20260705-20260714/2607.09082v1-rebase-reference-background-subspace-elimination-for-training-free-in-context-segmentation)  
   标签：评分：9.0/10、query:seg
   evidence：无训练上下文分割，支持新类别
9. [Rethinking Monocular Depth Embedding for Generalized Stereo Matching](/20260705-20260714/2607.09284v1-rethinking-monocular-depth-embedding-for-generalized-stereo-matching)  
   标签：评分：9.0/10、query:mono-depth
   evidence：重新思考单目深度嵌入以提升深度估计鲁棒性
10. [Self-supervised Automatic Matting](/20260705-20260714/2607.10395v1-self-supervised-automatic-matting)  
   标签：评分：9.0/10、query:matting
   evidence：无三才图的自监督自动抠图
11. [GHOST: Geometry-Guided Hallucination of Opaque Surface Textures](/20260705-20260714/2607.11118v1-ghost-geometry-guided-hallucination-of-opaque-surface-textures)  
   标签：评分：9.0/10、query:mono-depth
   evidence：针对透明物体的几何引导预处理，改善单目深度估计
12. [Parallax Portrait Matting](/20260705-20260714/2607.11205v1-parallax-portrait-matting)  
   标签：评分：9.0/10、query:matting
   evidence：利用视差双帧进行人像抠图，无需三分图
13. [FoundationGeo: Learning Spatial Pixel-Wise Fields for Monocular Metric Geometry](/20260705-20260714/2607.11588v1-foundationgeo-learning-spatial-pixel-wise-fields-for-monocular-metric-geometry)  
   标签：评分：9.0/10、query:mono-depth
   evidence：单目度量深度估计，采用空间像素级校准场

### 速读区论文标签
1. [AquaStereo: Enabling Underwater Stereo Matching via Depth-Conditioned Diffusion and Geometry Self-Distillation](/20260705-20260714/2607.04303v1-aquastereo-enabling-underwater-stereo-matching-via-depth-conditioned-diffusion-and-geometry-self-distillation)  
   标签：评分：8.0/10、query:stereo-depth
   evidence：水下双目匹配，使用深度条件扩散和自蒸馏进行数据模拟
2. [Vision Pretraining for Dense Spatial Perception](/20260705-20260714/2607.05247v1-vision-pretraining-for-dense-spatial-perception)  
   标签：评分：8.0/10、query:depth-refine
   evidence：以边界为中心的预训练，适用于边缘感知深度精修
3. [Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis](/20260705-20260714/2607.05348v1-beyond-isolated-objects-relationship-aware-open-vocabulary-scene-understanding-via-3d-scene-graph-analysis)  
   标签：评分：8.0/10、query:seg
   evidence：基于关系场景图的开放词汇3D场景理解
4. [Vision as Unified Multimodal Generation](/20260705-20260714/2607.06560v1-vision-as-unified-multimodal-generation)  
   标签：评分：8.0/10、query:vfm
   evidence：统一多模态生成用于包括深度和分割的密集空间预测
5. [Time-to-Collision Based Dynamic Obstacle Avoidance Using Pretrained Vision Models for Robots in Unstructured Environments](/20260705-20260714/2607.07885v1-time-to-collision-based-dynamic-obstacle-avoidance-using-pretrained-vision-models-for-robots-in-unstructured-environments)  
   标签：评分：8.0/10、query:mono-depth
   evidence：利用预训练单目深度模型UniDepth
6. [Attribute Retrieving for Open-Vocabulary Endoscopic Compositional Referring Segmentation](/20260705-20260714/2607.08397v1-attribute-retrieving-for-open-vocabulary-endoscopic-compositional-referring-segmentation)  
   标签：评分：8.0/10、query:seg
   evidence：内窥镜图像的开放词汇分割
7. [VocaDet: Sample-Driven Open-Vocabulary Object Detection and Segmentation via Visual Tokenization and Vector Database Retrieval](/20260705-20260714/2607.08541v1-vocadet-sample-driven-open-vocabulary-object-detection-and-segmentation-via-visual-tokenization-and-vector-database-retrieval)  
   标签：评分：8.0/10、query:seg
   evidence：样本驱动的开放词汇目标检测与分割
8. [Revisiting Matching Response and Swept Feature Volumes for Wide-baseline Omnidirectional Stereo](/20260705-20260714/2607.11097v1-revisiting-matching-response-and-swept-feature-volumes-for-wide-baseline-omnidirectional-stereo)  
   标签：评分：8.0/10、query:stereo-depth
   evidence：面向宽基线全向相机的立体深度估计与置信度评估
9. [LoCA: Spatially-Aware Low-Rank Convolutional Adaptation of Vision Foundation Models](/20260705-20260714/2607.06918v1-loca-spatially-aware-low-rank-convolutional-adaptation-of-vision-foundation-models)  
   标签：评分：7.0/10、query:vfm
   evidence：空间感知低秩卷积适应视觉基础模型，支持向密集预测任务迁移
10. [`Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object Segmentation](/20260705-20260714/2607.07230v1-attention-guided-cross-temporal-clustering-for-self-supervised-video-object-segmentation)  
   标签：评分：7.0/10、query:seg
   evidence：自监督视频目标分割，跨时间聚类
11. [DGSfM: Depth-Guided Scale-Aware Global Structure-from-Motion](/20260705-20260714/2607.09507v1-dgsfm-depth-guided-scale-aware-global-structure-from-motion)  
   标签：评分：7.0/10、query:mono-depth
   evidence：利用单目深度图作为SfM的可扩展先验
12. [Geometric Reciprocity: Unlocking Self-Supervision for Stereoscopic Video Generation](/20260705-20260714/2607.05354v1-geometric-reciprocity-unlocking-self-supervision-for-stereoscopic-video-generation)  
   标签：评分：6.0/10、query:stereo-depth
   evidence：使用几何互易定理的自监督单目到立体转换，涉及深度图像渲染
13. [Harnessing Generative Image Models for Training-Free Primitive Shape Abstraction](/20260705-20260714/2607.05568v1-harnessing-generative-image-models-for-training-free-primitive-shape-abstraction)  
   标签：评分：6.0/10、query:vfm
   evidence：利用生成图像模型进行无训练的部分分割和体素抽象
14. [TRIG: Trajectory-Rig Decoupled Metric Geometry Learning](/20260705-20260714/2607.05801v1-trig-trajectory-rig-decoupled-metric-geometry-learning)  
   标签：评分：6.0/10、query:mono-depth
   evidence：提出用于多相机驾驶系统的度量深度预测方法
15. [Smart Scissor: Coupling Spatial Redundancy Reduction and CNN Compression for Embedded Hardware](/20260705-20260714/2607.06915v1-smart-scissor-coupling-spatial-redundancy-reduction-and-cnn-compression-for-embedded-hardware)  
   标签：评分：6.0/10、query:lite-vision
   evidence：轻量级前景预测器和CNN压缩用于嵌入式硬件
16. [Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](/20260705-20260714/2607.08769v1-geometry-and-gradient-based-partitioning-for-panoramic-outdoor-reconstruction)  
   标签：评分：6.0/10、query:depth-refine
   evidence：两阶段粗到细框架，使用单目深度监督
17. [GeoGS-SLAM: Online Monocular Reconstruction Using Gaussian Splatting with Geometric Priors](/20260705-20260714/2607.11184v1-geogs-slam-online-monocular-reconstruction-using-gaussian-splatting-with-geometric-priors)  
   标签：评分：6.0/10、query:mono-depth
   evidence：利用预训练视觉几何模型进行单目深度估计


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
