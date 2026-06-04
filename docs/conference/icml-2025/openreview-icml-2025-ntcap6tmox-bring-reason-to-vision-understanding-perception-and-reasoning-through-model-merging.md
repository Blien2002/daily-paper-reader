---
title: "Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging"
title_zh: 为视觉引入推理：通过模型合并理解感知与推理
authors: "Shiqi Chen, Jinghan Zhang, Tongyao Zhu, Wei Liu, Siyang Gao, Miao Xiong, Manling Li, Junxian He"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=ntCAP6tMoX"
tags: ["query:vla"]
score: 7.0
evidence: VLM模型合并方法可迁移至VLA
tldr: 现有VLM在感知与推理结合上机制不清，本文提出跨模态模型合并方法，通过连接不同模型参数将LLM的推理能力迁移至VLM，无需额外训练。实验证明该方法成功提升了VLM的推理能力，为VLA模型中视觉语言部分的构建提供了高效路径。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1752, \"height\": 657, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 850, \"height\": 639, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 765, \"height\": 440, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1771, \"height\": 998, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1765, \"height\": 993, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1692, \"height\": 620, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1076, \"height\": 372, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 625, \"height\": 359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 779, \"height\": 790, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ntcap6tmox/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 799, \"height\": 588, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1772, \"height\": 530, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1771, \"height\": 423, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1770, \"height\": 477, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1773, \"height\": 641, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1083, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1777, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1775, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1122, \"height\": 838, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ntcap6tmox/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1610, \"height\": 335, \"label\": \"Table\"}]"
motivation: 当前VLM难以有效结合视觉感知与LLM推理能力，模型合并通常限于同类型模型。
method: 提出跨模态参数合并方法，将LLM的推理能力迁移到VLM中，无需训练。
result: 实验显示合并后的VLM在推理任务上表现显著提升。
conclusion: 模型合并是增强VLM推理能力的有效无训练方式，可推广至VLA。
---

## Abstract
Vision-Language Models (VLMs) combine visual perception with the general capabilities, such as reasoning, of Large Language Models (LLMs). However, the mechanisms by which these two abilities can be combined and contribute remain poorly understood.
In this work, we explore to compose perception and reasoning through model merging that connects parameters of different models.  
Unlike previous works that often focus on merging models of the same kind, we propose merging models **across modalities**, enabling the incorporation of the reasoning capabilities of LLMs into VLMs. 
Through extensive experiments, we demonstrate that model merging offers a successful pathway to transfer reasoning abilities from LLMs to VLMs in a **training-free** manner.
Moreover, we utilize the merged models to understand the internal mechanism of perception and reasoning and how merging affects it. We find that perception capabilities are predominantly encoded in the early layers of the model, whereas reasoning is largely facilitated by the middle-to-late layers. After merging, we observe that all layers begin to contribute to reasoning, whereas the distribution of perception abilities across layers remains largely unchanged. These observations shed light on the potential of model merging as a tool for multimodal integration and interpretation.

---

## 论文详细总结（自动生成）

# 论文《Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging》详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：视觉-语言模型（VLM）虽能结合视觉感知与语言能力，但在复杂多模态推理任务（如数学推理）上表现远逊于纯文本的大语言模型（LLM）。当前VLM的推理能力成为瓶颈，而LLM在推理方面进步显著。如何将LLM的推理能力迁移到VLM中，同时保持VLM的感知能力，且无需额外训练，是一个关键挑战。
- **研究背景**：VLM的感知与推理两大能力如何协同工作的机制尚不清晰。已有的模型合并工作多局限于同类型模型（如多个LLM合并），鲜有探讨跨模态模型合并。本文通过模型合并这一“训练免费”的工具，首次尝试将LLM的推理能力通过参数合并注入VLM，并借此理解VLM内部感知与推理能力的分布。

## 2. 方法论：核心思想、关键技术细节与公式

- **核心思想**：基于任务向量（task vector）的线性模型合并，将VLM的语言模型部分与一个擅长推理的LLM的参数进行加权平均，从而将推理能力迁移至VLM，而视觉塔（vision tower）和投影器（projector）保持不变。
- **关键技术细节**：
  - 定义基模型 \(\theta_{\text{base}}\)（VLM的原始语言模型初始化权重），VLM的语言模型参数 \(\theta_{\text{vlm}}\)，推理专用LLM参数 \(\theta_{\text{reason}}\)。
  - 任务向量：\(\tau_{\text{vlm}} = \theta_{\text{vlm}} - \theta_{\text{base}}\)，\(\tau_{\text{reason}} = \theta_{\text{reason}} - \theta_{\text{base}}\)。
  - 合并公式：\(\theta'_{\text{vlm}} = \theta_{\text{base}} + \lambda \tau_{\text{vlm}} + (1-\lambda) \tau_{\text{reason}}\)，其中 \(\lambda\) 控制VLM与推理LLM的平衡（主实验取0.9）。
  - 合并过程无需训练，仅需参数算术运算。
- **可解释性分析**：通过掩码（masking out）实验，逐层替换MLP或注意力层参数为均匀分布或另一模型参数，量化各层对感知和推理的贡献。

## 3. 实验设计

- **使用的VLM模型**：
  - LLaVA-Next-LLaMA3-8B（8B，LLaMA基座）
  - Idefics2-8B（8B，Mistral基座）
  - InternVL2-LLaMA3-76B（76B，LLaMA基座）
- **推理任务向量（源LLM）**：
  - 数学专精：Dart-Math（两个变体）、MAmmoTH-1、MAmmoTH-2、MetaMath、Magpie-v0.3、DeepSeek-R1-Distill
  - 逻辑推理：基于LogiCoT微调的LLaMA3-8B（附加实验）
- **基准测试（benchmarks）**：MathVista（含General和Math子集）、MathVerse（分6种感知难度模式，如Text-Dominant、Vision-Only）、MathVision、DynaMath、MMStar（含Math子集）、MM-Math（附加）
- **对比方法**：
  - 基线：原始VLM
  - 不同任务向量对比（5~7种）
  - 不同合并策略：线性合并（主要）、TIES、Dare-TIES、Dare-Linear、Layer Swapping
  - 消融：超参数λ调优（0.8,0.85,0.9）、逐层掩码分析、答案长度变化与性能关系

## 4. 资源与算力

- 论文**未明确说明**所使用的GPU型号、数量、训练时长等算力细节。仅提及代码已开源（GitHub链接）。实验均基于预训练模型的参数合并，无需额外训练，因此计算成本极低（仅需推理评估）。但可推测评估在单卡或少量GPU上即可完成。

## 5. 实验数量与充分性

- **实验数量**：涉及3个VLM × 至少5个任务向量 × 5~7个主基准，加上多种合并方法对比（至少4种）、消融实验（超参数敏感度、掩码分析、答案长度）、附加实验（逻辑推理、Qwen2-VL、MM-Math），总计超过30组结果表/图。
- **充分性**：
  - 覆盖了不同规模（8B~76B）、不同基座（LLaMA/Mistral）的VLM，验证了泛化性。
  - 同时在数学推理和一般感知任务上评估，避免了单一偏向。
  - 通过掩码分析深入解释了内部能力分布，增强了结论可信度。
  - 公平性：超参数λ在MathVista验证集上调优后统一用于所有基准；不同任务向量采用相同合并权重。
- **客观性**：实验结果一致性高，数学推理提升、视觉任务轻微下降，与理论预期相符。显著性检验标注了统计显著的结果。

## 6. 主要结论与发现

- **合并有效提升VLM推理能力**：将数学专精LLM（如Dart-Prop）合并入LLaVA，在MathVista数学子集上绝对提升3.6点，在MathVerse Text-Dominant模式上提升6点（相对30%），且在不同VLM上均观察到类似收益。
- **能力分布可分离**：通过掩码实验发现，感知能力主要位于模型早期层（前几层），而推理能力集中在中期到后期层（第五层起显著影响）。合并后，所有层对推理的贡献均增加，但感知层分布基本不变。
- **推理时间缩放能力迁移**：合并后模型在推理密集型任务上的答案长度显著增加（如几何推理超过250%），且长度增加与准确率提升呈近似线性关系，表明推理能力迁移成功。
- **对视觉主导任务影响有限或轻微下降**：如“视觉问答”、“图表问答”等任务性能可能下降，因为合并主要增强文本推理而非感知。
- **泛化至其他推理领域**：逻辑推理（LogiCoT）也可迁移至视觉数学推理，表明方法不限于数学。

## 7. 优点

- **训练免费**：无需任何额外训练，仅需简单参数算术操作，成本极低，易于推广。
- **跨模态迁移的创新**：首次系统研究将纯文本LLM的推理能力通过模型合并迁移至VLM，打破了同类型合并的局限。
- **深入的可解释性分析**：利用合并前后参数差异，通过掩码实验揭示感知与推理在VLM内部的层分布规律，为理解多模态模型内部机制提供了新视角。
- **广泛的实验验证**：涵盖多个VLM架构、不同推理任务向量、多种合并策略，结论稳健。
- **实用性强**：可直接提升现有VLM的数学推理性能，且代码开源。

## 8. 不足与局限

- **对已具备强推理能力的VLM提升有限**：如Qwen2-VL（预训练包含大量数学文本）合并后提升不明显，甚至部分基准下降，说明方法对已充分学习的模型收益递减。
- **视觉主导任务可能下降**：合并偏向推理，可能轻微损害感知能力，如“视觉问答”和“图表问答”任务性能下降。未探索如何弥补感知损失。
- **仅合并语言模型部分**：未尝试合并视觉塔或投影器，可能漏掉对感知能力的贡献。未涉及多模态联合合并。
- **未讨论计算开销细节**：缺少对合并后模型推理效率（如推理速度、显存占用）的分析。
- **合并超参数敏感度**：λ需要基于验证集调优，不同VLM或任务向量可能需要不同λ，限制了零样本直接使用。
- **可解释性分析依赖掩码假设**：掩码替换可能引入噪声，结论虽合理但需更多证据支持（如其他可解释方法）。

（完）
