---
title: Elevating Visual Perception in Multimodal LLMs with Visual Embedding Distillation
title_zh: 通过视觉嵌入蒸馏提升多模态大语言模型的视觉感知
authors: "Jitesh Jain, Zhengyuan Yang, Humphrey Shi, Jianfeng Gao, Jianwei Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=AZ1iyo58F8"
tags: ["query:vla"]
score: 6.0
evidence: 增强多模态大语言模型视觉感知以提升具身空间推理
tldr: VisPer-LM发现多模态大语言模型在纯语言监督下倾向于忽略视觉细节，限制了具身空间推理。该方法通过蒸馏专家视觉编码器的感知知识到LLM隐藏表示，在不增加推理代价下显著提升视觉定位和关系理解。实验表明在具身空间推理任务上准确率大幅提升，为VLA模型提供了更好的视觉基础。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1429, \"height\": 443, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 757, \"height\": 592, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1428, \"height\": 816, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1359, \"height\": 837, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 869, \"height\": 301, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 875, \"height\": 342, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1431, \"height\": 680, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1442, \"height\": 1209, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1397, \"height\": 716, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1444, \"height\": 964, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1412, \"height\": 691, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1424, \"height\": 741, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1450, \"height\": 735, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1411, \"height\": 685, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1449, \"height\": 778, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-az1iyo58f8/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1452, \"height\": 417, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1448, \"height\": 501, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1017, \"height\": 147, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1017, \"height\": 188, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1146, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1151, \"height\": 207, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 867, \"height\": 194, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1150, \"height\": 163, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 998, \"height\": 110, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1014, \"height\": 154, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1443, \"height\": 165, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1012, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1149, \"height\": 171, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1013, \"height\": 424, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1154, \"height\": 410, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1155, \"height\": 347, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1010, \"height\": 156, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1438, \"height\": 239, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1443, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1434, \"height\": 182, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-az1iyo58f8/table-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1156, \"height\": 206, \"label\": \"Table\"}]"
motivation: 标准MLLM训练偏向语言理解，忽略视觉细节，不利于具身空间推理。
method: 将专家视觉编码器的感知知识蒸馏注入LLM隐藏表示层。
result: 在不增加推理成本下，显著提升空间推理和视觉理解性能。
conclusion: 视觉感知蒸馏是低成本增强MLLM具身推理能力的有效方法。
---

## Abstract
In recent times, the standard practice for developing MLLMs is to feed features from vision encoder(s) into the LLM and train with natural language supervision. This approach often causes models to lean towards language comprehension and undermine the rich visual perception signals present in the data, which are critical for tasks involving spatial reasoning in the domain of embodied AI and robotics. Is it possible to optimize both at the same time? In this work, we propose VisPer-LM, the first approach that infuses visual perception knowledge from expert vision encoders into the LLM's (of an MLLM) hidden representations. We start by investigating MLLMs trained solely with natural language supervision and identify a positive correlation between the quality of visual representations within these models and their downstream performance. Given this insight, we formulate the objective during the pretraining stage in MLLMs as a coupled optimization of predictive visual embedding and next (text) token prediction.  Moreover, through extensive probing, we observe improved visual representation quality due to embedding optimization, underscoring the effectiveness of our probing setup. We demonstrate that our VisPer-LM outperforms the single and multi-encoder baselines, proving our approach's superiority over explicitly feeding the corresponding features to the LLM. In particular, VisPer-LM boosts performance by an average margin of up to 2.5% on various benchmarks, with a notable improvement of 8.7% on the Depth task in CV-Bench.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前多模态大语言模型（MLLM）的主流训练方式是使用视觉编码器提取特征后送入LLM，并以自然语言监督（下一个词预测）进行训练。这种方式导致模型偏向语言理解，而忽视了丰富的视觉感知信号，尤其在具身AI和机器人所需的空间推理（如深度估计、距离判断、关系理解）等任务中性能不足。
- **整体含义**：论文旨在**同时优化语言理解与视觉感知能力**，在不增加推理阶段成本的前提下，提升MLLM在视觉感知任务上的表现。作者发现LLM内部视觉表示的质量与下游VQA性能正相关，因此提出通过**视觉嵌入蒸馏**将专家视觉编码器的感知知识注入LLM的隐藏表示中，从而在预训练阶段强化视觉感知能力。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：在预训练（PT）阶段，除了常规的下一个词预测（NTP）损失外，额外引入**预测性视觉嵌入优化**损失，将来自多个专家视觉编码器（深度、分割、生成）的输出特征蒸馏到LLM的中间层表示中。推理时仅使用单个基础视觉编码器，不增加额外推理开销。
- **关键技术细节**：
  - **目标编码器**：选择三个专家编码器——深度估计（DINOv2-L from Depth Anything v2）、语义分割（Swin-L from OneFormer）、图像生成（CLIP-ViT-L from unCLIP-SD-2.1）。
  - **嵌入预测器**：对于每个目标编码器，在LLM的特定层上使用**单层Perceiver Resampler**作为嵌入预测器，接收可学习查询和该层隐藏状态（系统提示、图像、特殊令牌、文本查询）作为输入，输出与目标特征维度匹配的预测。
  - **特殊令牌**：为每个目标任务引入一组可学习的特殊令牌`⟨t⟩`（深度`⟨d⟩`、分割`⟨s⟩`、生成`⟨g⟩`），插入到图像令牌之后，形成隐式的视觉思维链。
  - **蒸馏损失**：嵌入损失`L_emb`由平滑L1损失和对比损失（InfoNCE）加权组合构成，作用于选定的层集`D, S, G`。总预训练损失为`L_PT = L_NTP + λ_depth L_D_emb + λ_seg L_S_emb + λ_gen L_G_emb`。
  - **训练阶段**：在PT阶段训练MLP投影器、嵌入预测器和特殊令牌；在IFT（指令微调）阶段仅使用NTP损失，冻结视觉编码器和特殊令牌。
- **公式/算法流程**（文字说明）：
  - 输入图像经基础视觉编码器 → MLP投影器 → LLM；同时，三个专家编码器提取目标特征。
  - 在PT阶段，对于每个专家任务，从LLM特定层取隐藏状态，输入对应的嵌入预测器，得到预测嵌入。
  - 计算预测嵌入与目标特征之间的平滑L1损失和对比损失，反向传播更新投影器、预测器和特殊令牌。
  - 联合优化NTP损失和蒸馏损失，完成后进入IFT阶段。

### 3. 实验设计：使用了哪些数据集/场景，benchmark，对比了哪些方法

- **数据集**：
  - 预训练（PT）：LLaVA-558K（558K图像-文本对）。
  - 指令微调（IFT）：LLaVA-665K。
  - 额外视觉预训练（VPT）：ALLaVA-Caption-663K（用于扩规模实验）。
  - 探测数据集：COCO-train2017（118K图像，用于训练探针）、COCO-val2017（5K图像，用于评估探测余弦相似度）。
- **Benchmark**：
  - **主要评估视觉感知能力**：CV-Bench（包含2D计数、2D关系、3D深度、3D距离四个子任务）。
  - **通用视觉推理**：MMStar、RWQA、OK-VQA，以及POPE、GQA、MMMU、VizWiz等。
  - **感知任务**：BLINK benchmark（空间关系、相对深度、计数等）。
- **对比方法**：
  - 单编码器基线：LLaVA-1.5（使用CLIP-ViT-L或CLIP-ConvNeXT-XXL作为基础编码器）。
  - 多编码器基线：特征拼接（feat concat.）和令牌拼接（token concat.），使用相同专家编码器。
  - 其他方法：Cambrian-1、RADIO-ViT-L-based LLaVA-1.5，以及无编码器的Chameleon-7B、EVE-7B。

### 4. 资源与算力

- **GPU型号与数量**：16块 **AMD 192G-MI300X GPU**。
- **批量大小**：PT阶段256，IFT和VPT阶段128。
- **训练时长**：未明确给出总时长，但提及每阶段训练一个epoch。基于经验，PT+IFT需数小时至一天（16卡大容量GPU）。文中未详细报告时间。

### 5. 实验数量与充分性

- **实验数量**：
  - **主实验**：在多种编码器（CLIP-ViT-L、CLIP-ConvNeXT-XXL、SigLIP-ViT-SO400M）和LLM（Phi3-4k-mini、Llama3-8B）组合下对比，约6组。
  - **消融实验**（附录及正文）：
    - 层集选择（D、S、G不同组合）
    - 损失组件（平滑L1、对比损失及其组合）
    - 特殊令牌数量N（0,8,16,24）
    - 训练阶段（仅PT、仅IFT、PT+IFT）
    - 特殊令牌冻结与否
    - 嵌入预测器输入令牌类型
    - 蒸馏目标组合（仅depth、仅seg、仅gen等）
    - 损失权重
    - 特殊令牌顺序
  - **扩展实验**：加入VPT数据后的性能对比。
  - **探测实验**：对多模型进行层间探测，分析表示质量与下游性能的相关性（深度探针相关系数0.98）。
  - **下游任务评估**：在BLINK、POPE、GQA等上额外验证。
- **充分性与公平性**：
  - 消融全面，覆盖关键设计维度。
  - 对比方法包括单/多编码器基线、最新方法（Cambrian-1、RADIO），且使用相同数据量（部分数据受限设置）。
  - 报告了推理吞吐量（表8），证明VisPer-LM与单编码器基线相近，远优于多编码器。
  - 不足之处：未在大规模LLM（如70B）上验证，但已明确说明受资源限制。

### 6. 论文的主要结论与发现

- 通过探测实验，论文首次揭示了**MLLM内部视觉表示质量与下游感知任务性能正相关**（深度探针与CV-Bench相关系数0.98）。
- **VisPer-LM**在预训练中引入视觉嵌入蒸馏，显著提升了视觉表示质量，并带来下游任务收益：平均提升2.5%，在CV-Bench深度任务上提升8.7%。
- **与多编码器基线相比**，VisPer-LM在多数任务上更好，且推理时无需多个编码器，效率更高（吞吐量约9.86 samples/sec vs 5.32）。
- **与单编码器基线（LLaVA-1.5）相比**，VisPer-LM在几乎所有基准上一致提升，且不受基础编码器和LLM选择影响。
- **融合特殊令牌**能进一步增强视觉推理能力（隐式视觉思维链），且冻结特殊令牌在IFT中更佳。
- 论文证实了**“在PT阶段优化LLM内部表示”**是一种低成本、高效率的视觉增强策略。

### 7. 优点

- **创新性**：首次将视觉嵌入蒸馏应用于MLLM的LLM内部表示，而非仅用于视觉编码器。提出联合优化NTP与预测性视觉嵌入损失。
- **高效性**：推理阶段仅使用单编码器，无额外计算开销，推理吞吐量远高于多编码器方案。
- **分析深入**：通过系统的探测实验，建立了视觉表示质量与下游性能的因果关系，为后续研究提供了分析工具。
- **实验严谨**：消融实验覆盖几乎所有设计因素，确保结论可靠。对比方法包括强基线（Cambrian-1、RADIO），且使用相同数据量，公平性较好。
- **通用性**：在不同基础编码器（CLIP-ViT-L、ConvNeXT、SigLIP）和LLM（Phi3、Llama3）上均有效，证明了方法的可迁移性。

### 8. 不足与局限

- **感知任务局限**：主要聚焦深度、空间关系等感知任务，未改善通用视觉推理（如OK-VQA、MMStar上提升较小），文中也承认这是“目标”而非“全面”提升。
- **教师编码器选择**：仅使用了深度、分割、生成三个专家编码器，未尝试更通用的教师（如InternViT），可能受限。
- **模态限制**：仅处理图像，未扩展到视频或低层信息（如运动控制、时序推理）。
- **规模不足**：受资源限制，仅在8B级LLM上验证，未在更大模型（如Llama3-70B、Qwen2-72B）上实验，因此无法确认方法在超大规模下的效果。
- **代码与模型未公开**（论文提交时声称将在camera-ready版本开放），影响可复现性。

（完）
