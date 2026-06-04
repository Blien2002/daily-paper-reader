---
title: "VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models"
title_zh: VLA-OS：视觉-语言-动作模型中规划表示与范式的结构化剖析
authors: "Chongkai Gao, Zixuan Liu, Zhenghao Chi, Junshan Huang, Xin Fei, Yiwen Hou, Yuxuan Zhang, Yudi Lin, Zhirui Fang, Lin Shao"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=PQYazNKEYo"
tags: ["query:vla"]
score: 9.0
evidence: 结构化剖析视觉-语言-动作模型中的规划表示
tldr: 当前VLA模型在规划范式、表示和训练数据上差异大，难以判断性能来源。本文通过系统分析法，隔离网络架构和数据的干扰，首次在不同规划范式和表示条件下对VLA模型进行深度剖析。实验揭示了不同组件的学习难度和性能增益来源。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1457, \"height\": 923, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1447, \"height\": 655, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1441, \"height\": 967, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1441, \"height\": 379, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 590, \"height\": 688, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 707, \"height\": 427, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 702, \"height\": 420, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1415, \"height\": 328, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pqyaznkeyo/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1434, \"height\": 1680, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1438, \"height\": 577, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 731, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 775, \"height\": 376, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1334, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1331, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 712, \"height\": 220, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pqyaznkeyo/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 582, \"height\": 220, \"label\": \"Table\"}]"
motivation: 现有VLA模型在规划上差异大，难以定位性能增益来源。
method: 系统性地隔离网络架构和数据，比较不同规划范式和表示。
result: 揭示了不同规划组件的学习难度和性能贡献。
conclusion: 为VLA模型设计提供了重要指导。
---

## Abstract
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and determine which component is more difficult to learn. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce \name, a unified VLA architecture suite capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior performance than other paradigms, albeit at the cost of slower training and inference speeds.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：视觉-语言-动作（VLA）模型在机器人操作任务中逐渐从端到端动作生成向“任务规划+动作生成”的流水线范式转变，在复杂长时任务上表现更优。然而，现有方法在网络架构、规划范式、规划表示形式、训练数据来源等方面差异巨大，导致研究者难以判断性能增益的具体来源，也无法明确哪个组件（规划 vs. 策略执行）更难学习。作者希望**系统性地隔离网络架构和训练数据的影响**，公平比较不同规划范式和表示形式的优劣，为社区提供实证指导。
- **核心问题**：包括五个关键问题：  
  1. **表示形式**：应采用哪种规划表示（语言、视觉、图像前瞻）？多表示是否更好还是相互冲突？  
  2. **范式**：使用单一模型联合规划与策略（Integrated-VLA）还是分层模型（Hierarchical-VLA）？  
  3. **瓶颈**：规划与策略执行哪个更困难？  
  4. **可扩展性与预训练**：引入规划后是否仍保持数据/模型可扩展性和预训练收益？  
  5. **性能**：带规划的VLA在泛化、持续学习上是否优于端到端VLA？

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：设计统一的VLA模型家族——**VLA-OS**，支持三种主流规划范式（ActionOnly-VLA、Integrated-VLA、Hierarchical-VLA），并配备可插拔的规划头（语言、视觉、图像前瞻），在所有对比中保持网络架构和训练数据一致，从而隔离无关变量。
- **关键技术细节**：
  - **VLA-OS-A（ActionOnly-VLA）**：基于Qwen2.5 LLM（0.5B/1.5B/3B/7B）和双视觉编码器（DINOV2+SigLIP），采用分块因果注意力动作头，支持动作块（chunk）预测。训练损失使用L1或流匹配（flow matching）损失。
  - **VLA-OS-I（Integrated-VLA）**：在VLA-OS-A基础上添加规划头（语言/视觉/图像前瞻）。支持显式规划（推理时先生成规划再动作）和隐式规划（规划头仅作为辅助损失，推理时不使用）。
    - 语言规划头：预测任务、子任务、移动指令等文本。
    - 视觉规划头：使用位置令牌（<loc_i>）表示边界框、末端执行器流、可操作区域。
    - 图像前瞻规划头：自回归生成未来帧图像（基于VAR+Bitwise Self-Correction）。
  - **VLA-OS-H（Hierarchical-VLA）**：将规划与策略分为两个独立网络。规划部分使用VLM+规划头，策略部分使用编码器-解码器动作头，可额外接收规划表示（经不同编码器处理后输入）。减少动作头层数以保持参数量相当。
  - **数据标注**：对LIBERO等数据集自动标注语言推理、视觉推理、图像前瞻三种规划标签，并经过一致性过滤和人工修正。

## 3. 实验设计：数据集、benchmark、对比方法

- **数据集与Benchmark**：
  - 仿真环境：LIBERO（4个子集：Spatial/Object/Goal/Long，共10任务各50条演示）、LIBERO-90（90任务）、The COLOSSEUM（20任务，含扰动泛化测试）、FurnitureBench（4任务）、DexArt（4任务）、PerAct2（5任务，双机械臂）。
  - 真实环境：3种可变形物体操作（展开牛仔裤、折叠手帕、拉直绳子）、5种刚体操作（见附录）。
- **对比方法**：
  - 基线：Diffusion Policy、OpenVLA、CoT-VLA、DiT Policy、π0-FAST、π0（SOTA）。
  - 主要对比：VLA-OS-A vs VLA-OS-I vs VLA-OS-H，以及不同规划表示（L、V、IF、组合）。
- **评估指标**：任务成功率（平均20轮次，取前3个检查点最高平均）、分解分数（DCS，规划正确率）、指令遵循分数（IFS，策略执行成功率）、泛化性能（COLOSSEUM全扰动设置）、持续学习指标（FWT/NBT/AUC）、训练/推理时间、数据/模型可扩展性曲线。

## 4. 资源与算力

- **训练设备**：8 × NVIDIA A100 80G GPU。
- **训练细节**：
  - VLM预训练：在LLaVa v1.5数据上预训练2个epoch，使用FSDP、BF16混合精度。
  - 下游任务训练：具体步数未统一说明，但提到LIBERO-LONG训练步数等参数（附录有详细超参数表如batch size 64、学习率2e-5等）。
  - 推理时间与训练成本在Fig.6b中展示（显式语言规划头最慢，视觉/图像前瞻更快）。
- **未明确说明**：总训练时长（小时或天数）未给出，但可以推算约需数天。

## 5. 实验数量与充分性

- **实验数量**：非常丰富，涵盖：
  - 6个仿真benchmark + 2个真实场景（刚体、可变形）+ 2种机械臂（夹爪、灵巧手）+ 2D/3D输入。
  - 规划表示对比：7种组合（L, V, IF, L+V, L+IF, V+IF, L+V+IF），分别在VLA-OS-I（显式/隐式）和VLA-OS-H上测试。
  - 范式对比：在5个benchmark上比较三种范式。
  - 泛化实验：COLOSSEUM全扰动测试。
  - 规划预训练实验：LIBERO-90预训练后微调。
  - 可扩展性实验：数据量（10%/40%/70%/100%）和模型规模（0.5B/1.5B/3B/7B）。
  - 持续学习实验：10任务顺序微调。
  - 消融：规划头种类、隐式/显式对比等。
- **充分性与公平性**：
  - 严格控制：所有对比使用相同VLM骨干、相同训练数据、相近参数量（规划头和动作头层数调整至约VLM 5%参数量）。
  - 统计方法：每个结果取前3个检查点平均20轮次，减少随机性。
  - 指标设计合理：单独评估规划（DCS）和策略（IFS）性能，客观定位瓶颈。
  - 不足：未探索所有可能的规划变体（如潜在动作、视频规划、场景流），且训练数据规模（<10k轨迹）较小，未在OXE等大规模数据集上验证。

## 6. 论文的主要结论与发现

- **发现1**：在目前的小规模数据下，模型架构和算法设计仍然重要，**并非模型越大越好**（VLA-OS-A 0.5B从零训练即可超越若干微调大模型）。
- **发现2**：**视觉锚定的规划表示（视觉推理和图像前瞻）显著优于语言规划表示**，且推理速度更快、训练成本更低。
- **发现3**：在Integrated-VLA中，**隐式规划（辅助损失）可带来正向增益**；**显式规划（推理时先规划）会导致严重性能下降**，主要由于规划误差累积。
- **发现4**：**Hierarchical-VLA整体表现最佳**：在任务成功率、泛化、数据可扩展性、持续学习、规划预训练收益上均优于或持平其他范式，但训练和推理更慢。
- **发现5**：**策略执行（policy learning）比任务规划更困难**（在所有表示中IFS均低于DCS），且视觉/图像前瞻表示更容易被低层策略遵循。
- **发现6**：所有范式均具有**数据可扩展性**；但在<5000条演示时，**LLM参数建议≤0.5B**（总模型<1B），否则过拟合。
- **发现7**：带规划的VLA在持续学习中**前向迁移更强，但遗忘更快**。

## 7. 优点：方法或实验设计上的亮点

- **系统性**：首次在同一架构套件内公平比较三种主流VLA范式与三种规划表示，隔离了网络架构、训练数据等混杂变量。
- **全面性**：覆盖2D/3D、刚体/可变形、仿真/真实、单臂/双臂/灵巧手等多种场景，共10+个benchmark。
- **创新指标**：提出分解分数（DCS）和指令遵循分数（IFS）分别评估规划与策略执行性能，精准定位瓶颈。
- **数据标注流程**：提出多层次推理标注（语言、视觉、图像），并经过一致性过滤和人工校正，保证数据质量。
- **开放贡献**：开源代码、标注数据集、模型检查点，方便复现和后续研究。
- **可插拔模块化设计**：VLA-OS支持不同LLM骨干和规划头，易于扩展。

## 8. 不足与局限

- **规划变体覆盖不全**：未包括潜在动作、视频生成规划、场景流等近期方法。
- **未涉及迁移学习**：未探索跨具身、sim2real、2D→3D迁移等问题。
- **数据规模有限**：训练数据集均小于10,000条轨迹，未在大规模数据集（如OXE）上验证，结论可能不适用于大规模预训练场景。
- **未深入解释根本原因**：例如为什么视觉表示优于语言、为什么隐式优于显式、梯度冲突的具体机制等仅作为未来方向提及，缺乏理论分析。
- **实际部署成本**：Hierarchical-VLA虽性能好，但训练和推理时间更长，在实时性要求高的场景中可能受限。
- **评估偏差风险**：主要依赖仿真环境（LIBERO等），真实世界实验仅包含3种可变形+5种刚体任务，且只报告成功率，未提供置信区间或误差棒。

（完）
