---
title: Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models
title_zh: 基于核的无监督嵌入对齐以增强视觉语言模型的视觉表征
authors: "Shizhan Gong, Yankai Jiang, Qi Dou, Farzan Farnia"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=0fLoGPTLo1"
tags: ["query:vla"]
score: 4.0
evidence: 增强视觉语言模型中的视觉表征，可助力VLA模型
tldr: 针对CLIP模型细粒度感知能力不足的问题，提出基于核的无监督嵌入对齐方法，将CLIP视觉表征与DINOv2对齐，在保持与文本嵌入兼容的同时提升视觉细节捕捉能力。实验表明该方法能增强下游多模态大模型性能，为VLA模型的视觉编码提供潜在改进。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-0flogptlo1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1737, \"height\": 501, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-0flogptlo1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 807, \"height\": 443, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-0flogptlo1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1736, \"height\": 349, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-0flogptlo1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 857, \"height\": 529, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-0flogptlo1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1736, \"height\": 350, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1773, \"height\": 784, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1776, \"height\": 487, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 885, \"height\": 583, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 627, \"height\": 364, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1769, \"height\": 536, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1562, \"height\": 330, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 926, \"height\": 550, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1773, \"height\": 530, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1775, \"height\": 431, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1616, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 844, \"height\": 147, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1773, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1770, \"height\": 307, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-0flogptlo1/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1773, \"height\": 420, \"label\": \"Table\"}]"
motivation: CLIP细粒度感知不足导致下游多模态大模型失败。
method: 提出基于核的方法对齐CLIP与DINOv2的视觉嵌入。
result: 对齐后保持文本嵌入兼容性同时提升视觉细节。
conclusion: 该方法可增强VLM视觉表征，助力VLA模型。
---

## Abstract
Vision-language models, such as CLIP, have achieved significant success in aligning visual and textual representations, becoming essential components of many multi-modal large language models (MLLMs) like LLaVA and OpenFlamingo. However, numerous studies have identified CLIP's limited fine-grained perception as a critical drawback, leading to substantial failures in downstream MLLMs. In contrast, vision-centric foundation models like DINOv2 demonstrate remarkable capabilities in capturing fine details from images. In this work, we propose a novel kernel-based method to align CLIP's visual representation with that of DINOv2, ensuring that the resulting embeddings maintain compatibility with text embeddings while enhancing perceptual capabilities. Our alignment objective is designed for efficient stochastic optimization. Following this image-only alignment fine-tuning, the visual encoder retains compatibility with the frozen text encoder and exhibits significant improvements in zero-shot object recognition, fine-grained spatial reasoning, and localization. By integrating the aligned visual encoder, downstream MLLMs also demonstrate enhanced performance. The code and models are available at https://github.com/peterant330/KUEA.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：CLIP 等视觉-语言模型（VLM）虽然成功对齐了图像和文本表示，但其视觉编码器在细粒度感知（如颜色、空间关系、计数）方面存在严重不足，导致下游多模态大语言模型（MLLM）在这些任务上性能受限。
- **研究动机**：DINOv2 等纯视觉自监督模型擅长捕捉图像细节，但其特征空间与 CLIP 不兼容，难以直接替换。现有增强 CLIP 的方法要么破坏与文本编码器的对齐，要么需要重新训练下游模型，成本过高。
- **整体含义**：提出一种轻量级、图像仅微调的方法，在不破坏 CLIP 与文本编码器兼容性的前提下，将 DINOv2 的细粒度感知能力迁移到 CLIP 视觉编码器中，从而提升 CLIP 及依赖它的 MLLM 的性能。

### 2. 论文提出的方法论

- **核心思想**：通过核函数度量样本间的相似性，使 CLIP 的核矩阵（基于 CLIP 嵌入）向 DINOv2 的核矩阵（基于 DINOv2 嵌入）对齐，从而在不剧烈改变原始特征空间结构的前提下，增强 CLIP 对视觉细节的区分能力。
- **关键技术细节**：
  - 使用**归一化多项式核**（degree 3）计算两两样本间的相似性，形成核矩阵。
  - 优化目标同时包含两项：
    1. **对齐项**：最小化 CLIP 核与 DINOv2 核之间的均方误差（MSE）。
    2. **正则项**：L2 距离惩罚，防止微调后的 CLIP 视觉嵌入偏离原始嵌入，以保持与冻结文本编码器的对齐。
  - 利用随机优化（mini-batch gradient descent）高效求解，理论保证梯度估计的收敛性。
- **算法流程**（文字说明）：
  1. 固定 CLIP 文本编码器和 DINOv2 视觉编码器。
  2. 从训练集（如 ImageNet-1K）中随机采样图像对。
  3. 分别用 CLIP（参数θ）和 DINOv2 提取特征，计算核函数值。
  4. 计算对齐损失 + 正则损失，对 CLIP 视觉编码器参数θ进行梯度更新。
  5. 经过少量 epoch 微调后，得到对齐后的 CLIP 视觉编码器。

### 3. 实验设计

- **数据集与场景**：
  - 训练集：ImageNet-1K（约128万张图像）。
  - 零样本分类：12个基准，包括 ImageNet、CIFAR-10/100、CalTech101、OxfordPets、DTD、EuroSAT、PCAM、ImageNet-Sketch、ImageNet-O 等，覆盖通用物体、细粒度、遥感、医疗、OOD 等场景。
  - 检索：Flickr30K、MSCOCO（图像-文本双向检索）。
  - 细粒度能力：SVHN、GTSRB、CLEVR Distance/Counts。
  - 定位能力：COCO 上的局部/全局探针测试。
  - 下游 MLLM：LLaVA-1.5-7B、OpenFlamingo-3B，评估 VQA（VQAv2、TextVQA、OK-VQA、VizWiz）、指代理解（RefCOCO/+ /g）、视觉空间推理（VSR、TallyQA、POPE、AI2D）等，以及 GPT-aided 评测。
- **Benchmark**：CLIP-Benchmark（LAION-AI）、ProbE（Covert et al. 2025）、MMVP-VLM 等。
- **对比方法**：
  - 简单基线：线性投影法（将 DINOv2 特征映射到 CLIP 空间）、特征直接对齐（L2）。
  - 相关方法：DIVA（利用扩散模型增强 CLIP）、AM-RADIO（多教师蒸馏）、Additive-MoF（简单融合 CLIP 和 DINOv2 特征）。
  - 自身消融：不同训练 epoch、正则系数、核函数类型、训练数据量。

### 4. 资源与算力

- **硬件**：最多4块 NVIDIA GeForce RTX 4090 GPU（不同模型配置不同，ViT-L-14 使用2块，ViT-L-14-336 使用4块）。
- **时间**：对齐微调 ViT-L-14 约需30小时。
- **备注**：文中明确说明了 GPU 型号和数量，但未给出具体能耗或显存占用细节。

### 5. 实验数量与充分性

- **实验数量**：非常充分。
  - 零样本分类：在12个数据集上测试了3种 CLIP 骨干（ViT-B-16, ViT-L-14, ViT-L-14-336），并扩展到 SigLIP、DFN、MetaCLIP。
  - 检索：2个数据集 × 2个方向。
  - 细粒度任务：4个数据集（SVHN, GTSRB, CLEVR 两个子集）。
  - 定位：1个数据集（COCO）的局部/全局探针。
  - MLLM：LLaVA 在12个 benchmark 上评测，OpenFlamingo 在7个数据集上3种 shot 设置。
  - 消融：5组（epoch、正则系数、核函数、训练数据比例、特征 vs 核对齐），以及附加 baseline 对比（AM-RADIO, Additive-MoF）。
- **充分性评估**：实验设计全面，覆盖了视觉任务、语言-视觉任务、细粒度能力、定位和下游 MLLM 性能，且控制变量合理。对比方法包括简单基线、先进方法和正交方法，结果客观。消融实验深入分析了设计选择。

### 6. 论文的主要结论与发现

- **主要结论**：提出的核对齐方法能有效将 DINOv2 的细粒度感知能力迁移到 CLIP 视觉编码器中，同时保持与文本编码器的兼容性。
- **具体发现**：
  - 零样本分类平均提升0.8%~1.3%，尤其在低分辨率或小物体数据集上提升显著。
  - 图像-文本检索性能没有下降甚至略有提升。
  - 计数、空间推理、文字识别等困难任务提升明显（如线性探针上 ViT-L-14 平均提升5.5%）。
  - 定位能力（局部/全局探针）提升，注意力图更锐利。
  - 下游 MLLM（LLaVA、OpenFlamingo）替换对齐后的视觉编码器后，在保留图文对齐的同时获得显著性能提升，尤其是指代理解和细粒度 VQA 任务。
  - 方法泛化性强：可应用于不同 CLIP 变体（SigLIP、DFN、MetaCLIP）和不同目标模型（MLCD）。

### 7. 优点

- **创新性**：首次利用核矩阵对齐来迁移视觉中心模型的细粒度表示，避免了直接特征对齐导致的语义漂移。
- **轻量化**：仅需少量图像数据（ImageNet-1K）和少量 epoch 微调，计算资源要求低（30小时，2~4块4090）。
- **兼容性强**：对齐后 CLIP 视觉编码器可直接替换下游 MLLM 中的原始编码器，无需重新训练图文对齐层或 LLM。
- **实验充分**：覆盖多种骨干、多种下游任务、多种对比方法，结果可靠。
- **理论支撑**：提供了优化目标的可随机优化定理，以及对齐保持定理（Proposition 3.2 说明正则项如何保护图文对齐）。

### 8. 不足与局限

- **实验规模有限**：仅在较小规模数据集（ImageNet-1K）上微调，未在更大规模（如 DataComp-1B）上验证。作者也承认可能限制了泛化性。
- **模型规模局限**：仅测试了7B/3B 的 MLLM，未验证在 70B 级别模型上的效果。
- **目标模型单一**：主要聚焦 CLIP↔DINOv2，虽然文中也尝试了 MLCD 和其他 VLM，但对不同视觉中心模型的系统性对比不足。
- **下游任务覆盖**：尽管实验丰富，但缺少对视频、医学图像、三维场景等更复杂场景的验证。
- **潜在偏差**：微调数据来自 ImageNet-1K，可能在领域分布上引入偏差，影响某些专业领域（如医疗、遥感）的泛化性。
- **应用限制**：要求目标模型（如 DINOv2）和 VLM（CLIP 系列）均已存在，对齐过程不改变这两个模型的架构，是一种后处理补救，而非根本性解决 CLIP 早期设计缺陷。

（完）
