---
title: "MMInference: Accelerating Pre-filling for Long-Context Visual Language Models via Modality-Aware Permutation Sparse Attention"
title_zh: MMInference：通过模态感知置换稀疏注意力加速长上下文视觉语言模型的预填充
authors: "Yucheng Li, Huiqiang Jiang, Chengruidong Zhang, Qianhui Wu, Xufang Luo, Surin Ahn, Amir H. Abdi, Dongsheng Li, Jianfeng Gao, Yuqing Yang, Lili Qiu"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=me6PfbATWM"
tags: ["query:vla"]
score: 5.0
evidence: VLM推理加速方法
tldr: 长上下文VLM在预填充阶段面临二次注意力复杂度，部署困难。本文提出MMInference动态稀疏注意力，利用视频输入的时空局部性和不同模态的稀疏分布模式加速预填充。实验证明在大幅降低计算量的同时保持模型质量，有益于VLA中的视觉语言处理。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 657, \"height\": 774, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1711, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1729, \"height\": 1269, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1347, \"height\": 839, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 858, \"height\": 390, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 859, \"height\": 434, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 865, \"height\": 395, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 868, \"height\": 454, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1653, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 859, \"height\": 413, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 821, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1083, \"height\": 592, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1349, \"height\": 1024, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1375, \"height\": 501, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1373, \"height\": 504, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 895, \"height\": 462, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 799, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 901, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 893, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 889, \"height\": 454, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 895, \"height\": 458, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 895, \"height\": 449, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1154, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 894, \"height\": 463, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 880, \"height\": 454, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1042, \"height\": 629, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1686, \"height\": 1799, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-me6pfbatwm/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1690, \"height\": 887, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-me6pfbatwm/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1756, \"height\": 986, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-me6pfbatwm/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 747, \"height\": 853, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-me6pfbatwm/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1597, \"height\": 217, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-me6pfbatwm/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1323, \"height\": 351, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-me6pfbatwm/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 906, \"height\": 1180, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-me6pfbatwm/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1711, \"height\": 1232, \"label\": \"Table\"}]"
motivation: 长上下文VLM预填充阶段注意力复杂度高，阻碍实际部署。
method: 分析视频输入的Grid稀疏模式，提出动态稀疏注意力方法加速预填充。
result: 显著减少预填充时间而性能损失极小。
conclusion: MMInference有效加速VLM推理，可支撑VLA系统的高效运行。
---

## Abstract
The integration of long-context capabilities with visual understanding unlocks unprecedented potential for Vision Language Models (VLMs). However, the quadratic attention complexity during the pre-filling phase remains a significant obstacle to real-world deployment. To overcome this limitation, we introduce MMInference (Multimodality Million tokens Inference), a dynamic sparse attention method that accelerates the prefilling stage for long-context multi-modal inputs. First, our analysis reveals that the temporal and spatial locality of video input leads to a unique sparse pattern, the Grid pattern. Simultaneously, VLMs exhibit markedly different sparse distributions across different modalities. We introduce a permutation-based method to leverage the unique Grid pattern and handle modality boundary issues. By offline search the optimal sparse patterns for each head, MMInference constructs the sparse distribution dynamically based on the input. We also provide optimized GPU kernels for efficient sparse computations. Notably, MMInference integrates seamlessly into existing VLM pipelines without any model modifications or fine-tuning. Experiments on multi-modal benchmarks-including Video QA, Captioning, VisionNIAH, and Mixed-Modality NIAH-with state-of-the-art long-context VLMs (LongVila, LlavaVideo, VideoChat-Flash, Qwen2.5-VL) show that MMInference accelerates the pre-filling stage by up to 8.3x at 1M tokens while maintaining accuracy. Our code is available at https://ama.ms/MMInference.

---

## 论文详细总结（自动生成）

# 论文《MMInference：通过模态感知置换稀疏注意力加速长上下文视觉语言模型的预填充》详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **问题**：长上下文视觉语言模型（VLM）在预填充（pre-filling）阶段，由于自注意力机制的二次复杂度，处理大量多模态输入（如长视频+文本）时延迟极高（可达数分钟），严重阻碍了实际部署（如机器人、自动驾驶、医疗等场景）。
- **背景**：现有稀疏注意力方法（如Sparse Transformer、StreamingLLM、MInference）主要针对纯文本LLM设计，未能有效利用多模态输入中视频特有的时空局部性，也无法处理不同模态之间的注意力边界问题，导致在VLM上性能下降或效率不足。
- **整体含义**：提出一种能够感知多模态稀疏模式的动态稀疏注意力方法，在不修改模型结构或微调的前提下，大幅降低预填充阶段计算量，同时保持准确性，从而推动长上下文VLM在实时或近实时场景的应用。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
利用VLM中视频输入的**时空局部性**（形成独特的Grid模式）以及**模态边界**（不同模态注意力分布差异大）的特点，通过**置换**（permutation）操作将非连续的稀疏块重排为连续块，再结合**动态稀疏估计**与**优化的GPU内核**，实现高效动态稀疏注意力计算。

### 关键技术细节
- **稀疏模式分析**：
  - **Grid模式**：视频帧的时空局部性使得注意力图中出现均匀间隔的水平和垂直条纹（类似于网格）。
  - **Q-Boundary**：Query维度上存在模态边界，不同模态（视→文、文→视）的稀疏模式被截断。
  - **2D-Boundary**：Query和Key维度上均存在模态边界，注意力分为多个独立块。
- **置换方法**：
  - 对Grid模式：通过行列置换将分散的网格块聚集为连续区块，便于硬件高效加载。
  - 对Q-Boundary：按模态对Q进行置换，使同一模态的query连续，然后对每个模态内部应用稀疏模式。
  - 对2D-Boundary：同时对Q、K、V按模态置换，然后对每个模态对（如视→文、文→视）分别应用稀疏注意力并构建对应mask。
- **Offline搜索**：对每个注意力头，在预定义的稀疏模式空间（Grid、A-shape、Vertical-Slash等）中离线搜索最优模式及超参数（如步长、窗口大小），最大化注意力召回率。
- **Online动态稀疏索引构建**：利用最后一段query估计近似注意力矩阵，动态确定稀疏索引（如网格步长、相位、竖线/斜线位置）。
- **GPU内核优化**：基于Triton和FlashAttention实现稀疏加载+密集计算的块稀疏内核，支持Grid、Q-Boundary、2D-Boundary模式的高效执行。
- **无需模型修改或微调**：直接插入现有VLM的预填充阶段，兼容性强。

## 3. 实验设计：数据集、基准与对比方法

### 数据集与场景
- **视频理解任务**（长视频QA、描述）：
  - ActNet-QA, EgoSchema, Next-QA, PerceptionTest, VideoDC, VideoMME。
- **Video Needle in a Haystack (V-NIAH)**：检索插入视频中的目标图像，token数最高达1.1M（约6000帧）。
- **Mixed-Modality Needle in a Haystack (MM-NIAH)**：论文新引入的混合模态检索任务，在视频中混入25%文本段落，token数最高达1.1M。

### 基准方法（对比方法）
- FlashAttention-2（作为全注意力的高效实现基准）
- 静态稀疏：SparseTransformer (Fixed/Strided)、A-shape、Tri-shape
- 动态稀疏：MInference（基于Vertical-Slash模式）
- 视觉token压缩：VisionZip

### 使用的模型
- LongVILA-7B-1M, Llava-Video-7B, VideoChat-Flash, Qwen2.5-VL-7B

### 评估指标
- 准确率（Accuracy/Recall），延迟（端到端及内核级），FLOPs占比。

## 4. 资源与算力

- **文中明确说明**：所有延迟实验在**单张NVIDIA A100 GPU**上运行，使用**bfloat16**精度，采用贪心解码。
- **离线搜索耗时**：约为15分钟（单张A100），使用一个校准样本（来自egoschema任务，token数≤25K）。
- **未提及**：训练相关算力（因为方法无需训练），未说明训练VLM模型本身的算力消耗。

## 5. 实验数量与充分性

### 实验数量
- **视频理解**：在6个主流benchmark上测试，覆盖Llava-Video（10项指标）、LongVILA（7项指标）、Qwen2.5-VL（7项指标），总计21个任务×方法结果。
- **V-NIAH**：在300~6000帧范围内测试全注意力与MMInference，并展示了与A-shape、Tri-shape、SF-fixed、SF-strided、MInference的对比（附录图）。
- **MM-NIAH**：在300~4500帧范围内测试全注意力与MMInference，以及与A-shape、Tri-shape、MInference、不带跨模态置换的消融对比。
- **消融分析**：
  - Grid vs. Vertical-Slash模式的延迟对比。
  - 稀疏索引跨模态泛化能力分析（图8）。
  - 与VideoChat-Flash（结合token压缩）的集成实验（表2）。
- **延迟测试**：在300/120K, 900/360K, 1800/720K, 2700/1M token下的端到端与内核级别延迟。

### 实验充分性评价
- **充分**：覆盖了多种任务类型（QA、描述、检索）、多种上下文长度（从20K到1M token）、多种模型架构。
- **客观公平**：与其他稀疏方法对比时，尽量对齐FLOPs（例如调节局部窗口大小），并使用官方评估指标；引入混合模态新任务以凸显跨模态特殊性。
- **不足**：仅在7B参数量级模型上验证，未在更大模型（如13B/34B）上测试；未在纯图像输入或语音/音频模态上验证（但在附录中提及Audio LMs也有类似模态边界现象）。

## 6. 论文的主要结论与发现

- **效率提升**：MMInference在1M token下实现**8.3×端到端加速**（对比FlashAttention-2），比MInference快1.7×，同时内核级加速达12×，仅保留约30%~50%的FLOPs。
- **准确率保留**：在视频理解任务中与全注意力几乎无差距（平均差异<1%）；在V-NIAH上召回率97.7%（全注意力98.3%）；在MM-NIAH上召回率91.3%（全注意力90.9%）。
- **Grid模式有效性**：相比MInference的Vertical-Slash模式，Grid模式在保持精度的同时显著降低延迟（因网格块重叠更少，稀疏度更高）。
- **模态置换的必要性**：消除Q-Boundary与2D-Boundary后，跨模态注意力仍可保持连续，否则性能明显下降。
- **稀疏模式可迁移性**：同一模态内构建的稀疏索引可跨模态边界泛化到同模态其他区域。

## 7. 优点

- **系统-算法协同设计**：联合考虑数学等价约束（稀疏加载+密集计算）和注意力模式的时空局部性，实现硬件高效。
- **首创性分析**：首次系统识别VLM中的Grid模式及四类模态边界模式，并针对性设计置换策略。
- **无需训练/微调**：直接应用于预训练模型，实用性强。
- **兼容性强**：可与视觉token压缩方法（如VideoChat-Flash）无缝集成，进一步提升效率。
- **实验覆盖全面**：包含视频理解、纯视频检索、混合模态检索三类基准，并引入MM-NIAH新任务，暴露了现有方法在混合输入下的局限性。
- **代码开源**：提供了完整实现，可重复性强。

## 8. 不足与局限

- **模型规模有限**：仅在7B参数模型上验证，未在更大VLM（如34B/72B）上测试，稀疏模式是否随规模变化？未探讨。
- **模态覆盖不全**：未测试音频或图片+文字混合输入（论文仅提及“音频LM也存在模态边界现象”，但未在实验中体现）。
- **离线搜索成本**：虽仅需15分钟，但需要针对每个模型单独搜索，且依赖于一个校准样本；如果模型或输入分布变化较大，可能需重新搜索。
- **动态索引近似依赖**：使用最后64个query近似整个注意力矩阵，对于某些极端长序列或特殊头可能存在偏差（论文已分析召回率，但未与更复杂的近似方法对比）。
- **稀疏核优化细节未完全公开**：虽提供算法伪代码，但实际性能严重依赖Triton内核实现细节（如块大小、并行策略），复现难度较高。
- **伦理/社会影响**：论文提及伦理声明“无特殊影响”，但若加速后VLM被用于敏感决策（如自动驾驶），其可靠性仍待进一步验证。

（完）
