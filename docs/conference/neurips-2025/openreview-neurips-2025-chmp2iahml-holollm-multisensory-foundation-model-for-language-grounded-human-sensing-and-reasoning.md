---
title: "HoloLLM: Multisensory Foundation Model for Language-Grounded Human Sensing and Reasoning"
title_zh: HoloLLM：用于语言接地人类感知与推理的多感官基础模型
authors: "Chuhao Zhou, Jianfei Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=cHMP2IAhML"
tags: ["query:vla"]
score: 4.0
evidence: 面向具身智能体的多感官基础模型
tldr: HoloLLM是一种多感官大语言模型，通过融合LiDAR、红外、毫米波雷达和WiFi等非视觉传感器，解决了智能家居中具身智能体在遮挡、弱光等环境下的鲁棒感知问题。方法利用对齐的文本数据和异构传感器融合，使得模型能在复杂环境中进行语言交互。实验表明其感知和推理能力优于纯视觉模型，为具身智能提供了更可靠的感知基础。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1349, \"height\": 643, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1451, \"height\": 560, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1419, \"height\": 507, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1452, \"height\": 363, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1448, \"height\": 282, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1452, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1436, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 455, \"height\": 300, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1400, \"height\": 664, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1410, \"height\": 464, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-chmp2iahml/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1298, \"height\": 1070, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1442, \"height\": 534, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1440, \"height\": 532, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1445, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 219, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1441, \"height\": 533, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1225, \"height\": 381, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1225, \"height\": 332, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-chmp2iahml/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 721, \"height\": 215, \"label\": \"Table\"}]"
motivation: 现有视觉语言模型在真实场景中因遮挡、光照等限制鲁棒性不足，需要更鲁棒的感知。
method: 提出HoloLLM，集成LiDAR、红外、毫米波雷达和WiFi等非视觉传感器到多模态大语言模型中。
result: 在异构环境下实现了优于纯视觉模型的感知和推理性能。
conclusion: 多感官融合显著提升了具身智能体在复杂环境中的鲁棒交互能力。
---

## Abstract
Embodied agents operating in smart homes must understand human behavior through diverse sensory inputs and communicate via natural language. While Vision-Language Models (VLMs) have enabled impressive language-grounded perception, their reliance on visual data limits robustness in real-world scenarios with occlusions, poor lighting, or privacy constraints. In this paper, we introduce HoloLLM, a Multimodal Large Language Model (MLLM) that integrates uncommon but powerful sensing modalities, such as LiDAR, infrared, mmWave radar, and WiFi, to enable seamless human perception and reasoning across heterogeneous environments. We address two key challenges: (1) the scarcity of aligned modality-text data for rare sensors, and (2) the heterogeneity of their physical signal representations. To overcome these, we design a Universal Modality-Injection Projector (UMIP) that enhances pre-aligned modality embeddings with fine-grained, text-aligned features from tailored encoders via coarse-to-fine cross-attention without introducing significant alignment overhead. We further introduce a human-VLM collaborative data curation pipeline to generate paired textual annotations for sensing datasets. Extensive experiments on two newly constructed benchmarks show that HoloLLM significantly outperforms existing MLLMs, improving language-grounded human sensing accuracy by up to 30\%. This work establishes a new foundation for real-world, language-informed multisensory embodied intelligence.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有视觉语言模型（VLM）在智能家居等真实场景中依赖视觉数据，在遮挡、弱光、隐私受限等条件下鲁棒性不足。需要整合LiDAR、红外、毫米波雷达、WiFi等非视觉传感器，但面临两大挑战：(1) 罕见传感器缺乏大规模模态-文本对齐数据；(2) 异构传感器信号表示差异大，难以利用统一编码器提取有效特征。
- **整体含义**：本文旨在构建首个将多种罕见传感模态与大型语言模型对齐的多模态基础模型，使具身智能体在复杂环境下仍能实现语言接地的人体感知与推理。

## 2. 论文提出的方法论
- **核心思想**：利用CLIP视觉编码器为每种模态生成预对齐的初始嵌入（不需额外训练），再通过定制编码器提取细粒度、模态特有的特征，最后用通用模态注入投影仪（UMIP）以粗到细的交叉注意力将细粒度特征逐步注入对齐嵌入，实现高效对齐。
- **关键技术细节**：
  - **UMIP结构**：输入Xm分别经过CLIP统一编码器得到粗粒度的预对齐嵌入Ym_CLIP，经平均池化形成查询Qm；同时经定制编码器（如ResNet18、PointNet、MetaFi等）+ MLP得到细粒度特征图Ym_T，展平为键值对Km/Vm。UMIP包含L=8个块，每个块内依次进行自注意力、交叉注意力（Q查询Km/Vm）、前馈网络，迭代更新查询，最后经MLP映射到LLM语义空间。
  - **两阶段训练**：阶段一用分类损失预训练定制编码器；阶段二冻结定制编码器，联合使用动作识别分类损失和自回归下一词预测损失微调UMIP和LLM。
- **公式/算法流程**（文字说明）：
  - 阶段一：L1 = CE(Classifier(E_T(Xm)), label)
  - 阶段二：L2 = CE(Classifier(LLM(Zm, Ztext)), label) + L_next_token

## 3. 实验设计
- **数据集**：MM-Fi（5种模态：视频、深度、LiDAR、毫米波、WiFi，27类动作，40人，4环境）和XRF55（5种模态：视频、深度、红外、RFID、WiFi，55类动作，19人，4环境）。
- **Benchmark**：构建了三种实验设置：随机拆分（Random）、跨主体（CrossSub）、跨环境（CrossEnv）。任务包括动作识别（Accuracy）、动作问答（Accuracy）、动作描述（METEOR）。
- **对比方法**：Tokenpacker、Honeybee、OneLLM（均为投影器方法）、ImageBind（编码器方法），均在同一数据集上微调进行公平比较。

## 4. 资源与算力
- **算力说明**：阶段一在单张A100 GPU上预训练120 epoch；阶段二在2张A100 GPU上微调5 epoch，有效batch size为64（MM-Fi）或48（XRF55），使用AdamW优化器，学习率2e-5，线性warmup 2000步。

## 5. 实验数量与充分性
- **实验组数**：共约8组主要实验，包括：
  - 主表1、2：动作QA和Caption在两种数据集、三种设置下，覆盖5种模态；
  - 图5：动作识别结果；
  - 表3：消融实验（基线、+定制编码器、+UMIP）在跨环境设置下；
  - 表6、7：多模态融合初步探索（朴素融合、加权求和、最大池化）；
  - 表8：泛化到新模态（Audio、UWB）的验证。
- **充分性评价**：实验较充分，覆盖了多种任务、多种设置、多种对比方法，消融实验验证了各组件的有效性。但未报告误差棒或多次运行统计，计算复杂度大可能限制了重复实验。对比方法较新，总体公平。

## 6. 论文的主要结论与发现
- HoloLLM在所有设置和大部分模态上显著优于现有MLLM，动作问答任务提升高达30%。
- UMIP和定制编码器有效解决了数据稀缺和异构性问题：定制编码器捕捉细粒度特征，UMIP在保持文本对齐的同时注入这些特征。
- 可视化（t-SNE）表明HoloLLM生成的多模态令牌按动作类别良好聚类，且与文本令牌对齐更紧密。

## 7. 优点
- **方法创新**：首次将多种罕见传感模态（LiDAR、毫米波、WiFi、RFID、红外）集成到MLLM中，UMIP设计巧妙，兼顾预对齐和细粒度特征，无需大量对齐数据。
- **数据管道**：提出人-VLM协作的数据标注流程，利用GPT-4o和LLaVA-Video生成问答和描述文本，解决了传感数据缺乏文本标注的问题。
- **性能领先**：在多个任务和设置下取得显著提升，验证了多感官融合对鲁棒感知的必要性。

## 8. 不足与局限
- **任务覆盖**：仅涵盖动作识别、问答和描述，未涉及更复杂的任务规划、具身动作生成等实际应用场景。
- **泛化性**：部分传感模态（如WiFi、RFID）在跨主体/跨环境设置下性能大幅下降，说明对主体和环境敏感，需要更大规模、更多样的数据。
- **算力成本**：使用7B LLM和多个编码器，训练资源需求较高。
- **偏差风险**：文本标注依赖GPT-4o和LLaVA-Video，可能引入语言模型的固有偏差或幻觉；动作类别有限（27/55类），真实场景更复杂。
- **统计完整性**：未提供多次重复实验的误差棒，结果可能存在随机性影响。

（完）
