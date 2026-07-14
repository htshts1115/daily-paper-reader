<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-07-14
- 运行时间：2026-07-14 22:18:13 UTC
- 运行状态：成功
- 本次总论文数：18
- 精读区：4
- 速读区：14

### 今日简报（AI）
今日18篇论文深度解析，重点关注从RGB生成到密集场读取的像素空间预测、以及实时立体匹配中的不确定性引导残差搜索技术。最值得深入阅读的两篇高分精读分别为《From RGB Generation to Dense Field Readout》和《URS-Stereo》，前者革新了文本到图像模型的像素级预测范式，后者在实时立体匹配中引入不确定性引导机制。建议普通读者优先关注这些可直接提升视觉任务精度的技术，并留意速读中《Segmentation before Answering》等视觉推理方向的应用潜力。
- 详情：[/202607/14/README](/202607/14/README)

### 精读区论文标签
1. [From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with Text-to-Image Models](/202607/14/2607.06553v1-from-rgb-generation-to-dense-field-readout-pixel-space-dense-prediction-with-text-to-image-models)  
   标签：评分：9.0/10、query:vfm
   evidence：利用文生图模型进行密集预测（深度、法线、alpha抠图、掩码）
2. [URS-Stereo: Uncertainty-Guided Residual Search for Real-Time Stereo Matching](/202607/14/2607.06779v1-urs-stereo-uncertainty-guided-residual-search-for-real-time-stereo-matching)  
   标签：评分：8.0/10、query:stereo-depth
   evidence：面向手机双摄的实时粗到细立体匹配
3. [TMI: Text-to-Image Meets Image-to-Image for Complementary Data Synthesis to Boost Long-Tailed Instance Segmentation](/202607/14/2607.08201v1-tmi-text-to-image-meets-image-to-image-for-complementary-data-synthesis-to-boost-long-tailed-instance-segmentation)  
   标签：评分：8.0/10、query:seg
   evidence：长尾实例分割数据合成
4. [TSR-Ego: Temporally Guided Stereo Refinement Framework for Egocentric 3D Human Pose Estimation](/202607/14/2607.09169v1-tsr-ego-temporally-guided-stereo-refinement-framework-for-egocentric-3d-human-pose-estimation)  
   标签：评分：8.0/10、query:stereo-depth
   evidence：面向第一人称视角3D人体姿态估计的时序引导立体深度精化

### 速读区论文标签
1. [Segmentation before Answering: Pixel Grounding for MLLM Visual Reasoning](/202607/14/2607.05798v1-segmentation-before-answering-pixel-grounding-for-mllm-visual-reasoning)  
   标签：评分：7.0/10、query:seg
   evidence：像素级分割定位用于视觉推理
2. [Smart Scissor: Coupling Spatial Redundancy Reduction and CNN Compression for Embedded Hardware](/202607/14/2607.06915v1-smart-scissor-coupling-spatial-redundancy-reduction-and-cnn-compression-for-embedded-hardware)  
   标签：评分：7.0/10、query:seg
   evidence：面向嵌入式硬件的轻量级前景预测器实现动态图像裁剪
3. [LoCA: Spatially-Aware Low-Rank Convolutional Adaptation of Vision Foundation Models](/202607/14/2607.06918v1-loca-spatially-aware-low-rank-convolutional-adaptation-of-vision-foundation-models)  
   标签：评分：7.0/10、query:vfm
   evidence：视觉基础模型的参数高效微调用于密集预测
4. [Sparse Attention for Dense Open-Vocabulary Prediction in CLIP](/202607/14/2607.07135v2-sparse-attention-for-dense-open-vocabulary-prediction-in-clip)  
   标签：评分：7.0/10、query:seg
   evidence：通过稀疏注意力改进CLIP用于密集开放词汇预测
5. [Weaving Light and Time: Unified Harmonic-Geometric Representation Learning for Dense RGB-Event Parsing](/202607/14/2607.09143v1-weaving-light-and-time-unified-harmonic-geometric-representation-learning-for-dense-rgb-event-parsing)  
   标签：评分：7.0/10、query:seg
   evidence：统一骨干网络用于稠密RGB-事件语义分割
6. [CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation](/202607/14/2607.09362v1-ctrlvton-controllable-virtual-try-on-via-visual-instance-prompt-segmentation)  
   标签：评分：7.0/10、query:seg
   evidence：视觉实例提示分割用于服装实例级分割；与实例分割直接相关
7. [Slot-RAE: Streamlining Object-Centric Learning via Direct Representation Auto-Encoders](/202607/14/2607.11196v1-slot-rae-streamlining-object-centric-learning-via-direct-representation-auto-encoders)  
   标签：评分：7.0/10、query:vfm
   evidence：使用DINOv3特征空间和扩散进行对象中心学习，可迁移至密集预测任务
8. [3DMPE: 3D Multi-Perspective Embedding](/202607/14/2607.04898v1-3dmpe-3d-multi-perspective-embedding)  
   标签：评分：6.0/10、query:stereo-depth
   evidence：基于优化的多视图3D重建方法，包含点对应和投影估计，与双目深度估计技术相关
9. [GUSH3R: Everyone Everywhere All at Once as Gaussians](/202607/14/2607.05243v1-gush3r-everyone-everywhere-all-at-once-as-gaussians)  
   标签：评分：6.0/10、query:mono-depth
   evidence：从单目视频重建动态人体和场景，与用于人像虚化的单目深度估计相关
10. [Harnessing Generative Image Models for Training-Free Primitive Shape Abstraction](/202607/14/2607.05568v1-harnessing-generative-image-models-for-training-free-primitive-shape-abstraction)  
   标签：评分：6.0/10、query:seg
   evidence：利用生成图像模型和视觉语言模型实现免训练的部件分割
11. [Enhancing In-context Panoramic Generation via Geometric-aware Pretraining](/202607/14/2607.08765v2-enhancing-in-context-panoramic-generation-via-geometric-aware-pretraining)  
   标签：评分：6.0/10、query:mono-depth
   evidence：在全景生成框架中使用并行深度生成
12. [DETRAM: End-to-end DEtection, Tracking and Recovery of HumAn Meshes](/202607/14/2607.09089v1-detram-end-to-end-detection-tracking-and-recovery-of-human-meshes)  
   标签：评分：6.0/10、query:seg
   evidence：端到端人体网格恢复与追踪，利用检测变压器隐式分割视频中的人体
13. [SigLIP-HD by Fine-to-Coarse Supervision](/202607/14/2607.09488v1-siglip-hd-by-fine-to-coarse-supervision)  
   标签：评分：6.0/10、query:vfm
   evidence：精细到粗糙监督改进视觉编码器，适用于密集预测任务
14. [CUST: Clustered Unit-level Similarity Transformer for Lightweight Image Super-Resolution](/202607/14/2607.11088v1-cust-clustered-unit-level-similarity-transformer-for-lightweight-image-super-resolution)  
   标签：评分：6.0/10、query:lite-vision
   evidence：轻量级ViT超分辨率方法，可迁移至密集预测任务


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
