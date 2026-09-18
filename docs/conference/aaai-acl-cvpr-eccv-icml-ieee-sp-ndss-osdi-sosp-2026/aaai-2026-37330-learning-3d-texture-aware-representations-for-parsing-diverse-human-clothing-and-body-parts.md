---
title: Learning 3D Texture-Aware Representations for Parsing Diverse Human Clothing and Body Parts
title_zh: 学习面向多样人体服饰与身体部位解析的3D纹理感知表征
authors: "Kiran Chhatre, Christopher E. Peters, Srikrishna Karanam"
date: 2026
publication_date: 2026
publication_date_precision: year
publication_date_source: conference year only; exact release date unverified
publication_date_kind: unknown
pdf: "https://ojs.aaai.org/index.php/AAAI/article/download/37330/41292"
tags: ["query:seg"]
score: 6.0
evidence: 开放词汇分割与部位级像素解析
tldr: 现有人体解析方法常采用固定且宽泛的掩码类别，难以区分多样的服饰类型，而开放词汇分割又通常把整个人归为单一的人类别。为此作者提出统一网络Spectrum，借助预训练文生图扩散特征，同时完成部位级像素解析与实例级分组。实验表明该网络能对服饰和身体部位做细粒度区分，并保持较强的零样本迁移能力。该工作推动了细粒度人体解析与开放词汇分割的结合。
source: AAAI-2026-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37330/fig-001.webp\", \"caption\": \"\", \"page\": 4, \"index\": 1, \"width\": 662, \"height\": 279}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37330/fig-002.webp\", \"caption\": \"\", \"page\": 5, \"index\": 2, \"width\": 662, \"height\": 898}, {\"url\": \"assets/figures/aaai-2026-accepted/aaai-2026-37330/fig-003.webp\", \"caption\": \"\", \"page\": 6, \"index\": 3, \"width\": 1399, \"height\": 615}]"
motivation: 现有人体解析使用固定粗粒度类别，开放词汇分割又常把整个人归为单一类别。
method: 提出统一网络Spectrum，结合文生图扩散特征实现部位级像素解析与实例级分组。
result: 在人体解析上实现服饰与身体部位的细粒度区分，并保持零样本迁移能力。
conclusion: 为细粒度人体部位与服饰解析提供了可迁移的统一框架。
---

## Abstract
Existing methods for human parsing into body parts and clothing often use fixed mask categories with broad labels that obscure fine-grained clothing types. Recent open-vocabulary segmentation approaches leverage pretrained text-to-image (T2I) diffusion model features for strong zero-shot transfer, but typically group entire humans into a single person category, failing to distinguish diverse clothing or detailed body parts. To address this, we propose Spectrum, a unified network for part-level pixel parsing (body parts and clothing) and instance-level grouping. While diffusion-based open-vocabulary models generalize well across tasks, their internal representations are not specialized for detailed human parsing. We observe that, unlike diffusion models with broad representations, image-driven 3D texture generators maintain faithful correspondence to input images, enabling stronger representations for parsing diverse clothing and body parts. Spectrum introduces a novel repurposing of an Image-to-Texture (I2Tx) diffusion model—obtained by fine-tuning a T2I model on 3D human texture maps—for improved alignment with body parts and clothing. From an input image, we extract human-part internal features via the I2Tx diffusion model and generate semantically valid masks aligned to diverse clothing categories through prompt-guided grounding. Once trained, Spectrum produces semantic segmentation maps for every visible body part and clothing category, ignoring standalone garments or irrelevant objects, for any number of humans in the scene. We conduct extensive cross-dataset experiments—separately assessing body parts, clothing parts, unseen clothing categories, and full-body masks—and demonstrate that Spectrum consistently outperforms baseline methods in prompt-based segmentation.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义

- **研究动机**：现有人体解析方法通常使用固定的、宽泛的掩码类别，例如把躯干服饰统一标为 `upper clothes`，难以区分细粒度服饰类型；而开放词汇分割方法虽借助 T2I 扩散模型获得较强零样本迁移能力，却常把整个人归为单一 `person` 类别，无法区分多样服饰和详细身体部位。
- **核心
