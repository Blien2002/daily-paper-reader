---
title: World Model Implanting for Test-time Adaptation of Embodied Agents
title_zh: 世界模型植入：具身智能体测试时自适应
authors: "Minjong Yoo, Jinwoo Jang, Sihyung Yoon, Honguk Woo"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=tpbtodnI1p"
tags: ["query:vla"]
score: 8.0
evidence: LLM与世界模型结合用于具身智能体适应
tldr: 具身智能体在新领域鲁棒适应需要大量数据或重训练。本文提出世界模型植入框架WorMI，在测试时将LLM的推理能力与独立学习的领域世界模型组合，通过原型检索和轨迹抽象匹配实现无缝植入和移除。实验表明智能体策略获得跨域适应性。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 852, \"height\": 544, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1631, \"height\": 664, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 832, \"height\": 959, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 832, \"height\": 373, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 829, \"height\": 628, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1760, \"height\": 319, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1590, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-tpbtodni1p/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1748, \"height\": 299, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1520, \"height\": 603, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1767, \"height\": 501, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 694, \"height\": 527, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 863, \"height\": 436, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 677, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 861, \"height\": 421, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 832, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1109, \"height\": 586, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 967, \"height\": 496, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1001, \"height\": 313, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1195, \"height\": 395, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1029, \"height\": 1011, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 610, \"height\": 172, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 756, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 487, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 579, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 704, \"height\": 174, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-tpbtodni1p/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 533, \"height\": 422, \"label\": \"Table\"}]"
motivation: 具身智能体难以鲁棒适应新领域，缺乏高效测试时适应方法。
method: 提出WorMI框架，测试时将LLM与领域世界模型组合，利用原型检索和轨迹匹配。
result: 智能体在跨域任务中适应能力显著提升。
conclusion: 世界模型植入是具身智能体测试时适应的有效范式。
---

## Abstract
In embodied AI, a persistent challenge is enabling agents to robustly adapt to novel domains without requiring extensive data collection or retraining. To address this, we present a world model implanting framework (WorMI) that combines the reasoning capabilities of large language models (LLMs) with independently learned, domain-specific world models through test-time composition. By allowing seamless implantation and removal of the world models, the embodied agent's policy achieves and maintains cross-domain adaptability. In the WorMI framework, we employ a prototype-based world model retrieval approach, utilizing efficient trajectory-based abstract representation matching, to incorporate relevant models into test-time composition. We also develop a world-wise compound attention method that not only integrates the knowledge from the retrieved world models but also aligns their intermediate representations with the reasoning model's representation within the agent's policy. This framework design effectively fuses domain-specific knowledge from multiple world models, ensuring robust adaptation to unseen domains. We evaluate our WorMI on the VirtualHome and ALFWorld benchmarks, demonstrating superior zero-shot and few-shot performance compared to several LLM-based approaches across a range of unseen domains. These results highlight the framework’s potential for scalable, real-world deployment in embodied agent scenarios where adaptability and data efficiency are essential.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **问题**：具身智能体在真实世界中面临多样且不断变化的环境，现有的策略通常针对特定领域训练，难以高效适应未见过的领域（unseen domains）。传统方法要么需要大量数据收集和重训练，要么缺乏灵活扩展知识的能力。
- **意义**：本文提出一种能够在测试时（test-time）动态组合多个领域世界模型与大语言模型（LLM）的框架，使智能体在不重训练主模型的情况下实现跨域适应，从而提升数据效率和鲁棒性。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- **WorMI（World Model Implanting）**：将多个预训练的领域特定世界模型（world models）通过可学习的复合注意力模块（compound attention）动态“植入”到固定的LLM推理策略中，在测试时实现领域知识的灵活融合与对齐。

### 关键技术细节
1. **原型驱动的世界模型检索（Prototype-based World Model Retrieval）**：
   - 每个世界模型对应的数据集通过物体级状态嵌入（object-wise embeddings）构建原型集（prototypes，使用k-center聚类选取约0.1%代表性嵌入）。
   - 给定当前观测，计算其嵌入集与各模型原型集的Wasserstein距离，检索Top-K最相关的世界模型，避免全量计算。

2. **世界级复合注意力（World-wise Compound Attention）**：
   - 线性投影层：将每个世界模型中间层表示投影到LLM的嵌入空间。
   - **世界级交叉注意力（World-level Cross-attention）**：以LLM的当前隐藏状态为查询，对检索到的多个世界模型表示进行加权融合。
   - **推理级交叉注意力（Reasoning-level Cross-attention）**：将融合后的表示与LLM表示对齐，最终输入到LLM下一层。
   - 该模块通过元学习（meta-learning）训练，使其能灵活适应任意组合的世界模型。

### 算法流程（文字说明）
- **训练阶段**（元学习）：
  1. 初始化复合注意力参数θ。
  2. 内循环：对每个世界模型子集Mj，复制θ为θj，在对应数据集上通过行为克隆损失更新θj（少量梯度步）。
  3. 外循环：将所有θj平均回传更新θ。
- **测试阶段**：
  1. 对当前观测，原型检索选出最相关的K个世界模型。
  2. 利用训练好的复合注意力将这些模型与固定LLM组合成策略πθ，执行动作。

## 3. 实验设计：数据集、基准、对比方法

- **环境与数据集**：
  - **VirtualHome**（3D模拟）：1,023个episode，覆盖78个任务（16个seen，62个unseen）和20个场景（6个seen，14个unseen）。
  - **ALFWorld**（文本模拟）：3,554个episode，按CL-ALFRED设置分为4种场景类型（3 seen，1 unseen）和6种任务类型（4 seen，2 unseen）。
- **基准（Benchmark）**：零样本（zero-shot）和少样本（few-shot，1/5/10 shots）跨域适应。
- **对比方法**：
  - **ZSP**（零样本预训练）
  - **LLM+FT**（领域微调）
  - **LLM-Planner**（基于上下文学习的规划）
  - **SayCanPay**（集成启发式代价最小化的SOTA方法）
- **评估指标**：成功率（SR）、待完成步数（PS，值越小越好）。

## 4. 资源与算力

- **文中明确说明**：
  - 使用固定LLM：Llama-3.2-3B作为推理模型（ZSP、LLM-Planner、SayCanPay的Say模型、WorMI的推理模型）。
  - 可训练模型：Llama-3.2-1B用于世界模型和微调基线。
  - 附录中报告了推理时间和内存占用（例如WorMI在K=3,N=6时385ms推理，33,445 MiB内存）。
- **未明确说明**：训练复合注意力模块所用的GPU型号、数量、总训练时长等信息缺失。

## 5. 实验数量与充分性

- **主要实验**：
  - 零样本（表1）和少样本（表2）各两个环境，涵盖seen/unseen tasks & scenes组合，共4个主要表格。
  - 消融实验（表3）：检索策略（全部/随机/原型）和融合策略（拼接/相加/复合注意力）。
  - LLM规模影响（表4）：1B、3B、11B。
  - 世界模型数量影响（表5）：1~6个。
  - 复杂指令场景（表6）：长时指令、多指令。
  - 持续模型植入实验（图5）。
  - 额外分析：世界级注意力可视化、多模态变体、鲁棒性测试（附录）。
- **充分性评估**：实验覆盖零样本/少样本、不同领域、不同模型规模、不同融合方式，设计较为全面。消融实验清晰验证各组件贡献。但缺乏真实机器人平台验证，且未与其他多模型集成方法（如MoE）直接对比。总体充分且客观。

## 6. 论文的主要结论与发现

- WorMI在所有设置下显著优于现有基线：
  - **VirtualHome零样本**：SR比SayCanPay高20.41%，PS降低3.87步。
  - **ALFWorld零样本**：SR高12.01%，PS降低3.68步。
  - **少样本平均**：SR提升26.58%（VirtualHome）和19.16%（ALFWorld）。
- 原型检索有效选择相关世界模型，复合注意力动态聚焦最相关的领域知识。
- 随着LLM规模增大，WorMI性能持续提升，而上下文学习方法依赖更大模型。
- 在2~4个世界模型时性能最佳，过多或过少均下降。
- 持续植入/移除世界模型可行，支持知识更新与遗忘。

## 7. 优点

- **方法创新**：首次提出测试时“植入”多个世界模型到LLM推理中的双阶段融合范式，兼具模型集成与上下文学习的优势。
- **高效检索**：原型驱动检索大幅降低计算开销（仅使用0.1%嵌入），且理论有界保证（Wasserstein距离上界）。
- **可扩展性**：世界模型可以独立替换或添加，无需重训策略，支持持续学习场景。
- **实验扎实**：在两个基准、多种设定下全面对比，消融和规模分析充分。
- **跨模型鲁棒**：在1B~11B不同LLM下均有效，且能利用更大LLM的推理能力。

## 8. 不足与局限

- **计算开销**：即使有检索优化，仍需要同时运行多个世界模型（每个约1B参数），在资源受限边缘设备上可能存在挑战。
- **依赖LLM能力**：硬编码LLM作为推理核心，如果LLM对特定领域推理不足，整体性能会受限制。
- **训练数据假设**：假设每个领域已有预训练世界模型和对应数据集，这在现实场景中不一定总能满足。
- **未充分说明训练算力**：缺少复合注意力元学习阶段的具体GPU配置和训练时间，不利于复现和评估成本。
- **缺乏真实物理环境验证**：仅在模拟器（VirtualHome/ALFWorld）上评估，未见真实机器人实验，泛化性有待验证。
- **与模型合并方法的对比有限**：虽然文中对比了CALM概念，但实验未直接与更多最新组合/融合方法（如Mixture of Experts）比较。

（完）
