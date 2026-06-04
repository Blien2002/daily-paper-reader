---
title: "PhysVLM-AVR: Active Visual Reasoning for Multimodal Large Language Models in Physical Environments"
title_zh: PhysVLM-AVR：多模态大语言模型在物理环境中的主动视觉推理
authors: "Weijie Zhou, Xuantang Xiong, Yi Peng, Manli Tao, Chaoyang Zhao, Honghui Dong, Ming Tang, Jinqiao Wang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=AYDMNzpJPv"
tags: ["query:vla"]
score: 6.0
evidence: 为多模态大语言模型提出主动视觉推理任务，用于具身物理环境
tldr: 多模态大语言模型在静态被动视觉推理中表现出色，但在真实物理环境中的部分可观测条件下效果有限。本文提出主动视觉推理任务，迫使智能体通过移动和操作主动收集信息。PhysVLM-AVR方法结合闭环感知-推理-动作，在模拟环境中取得了显著进步，推动了MLLM向具身智能应用发展。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1437, \"height\": 493, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1387, \"height\": 789, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1398, \"height\": 664, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1444, \"height\": 519, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1441, \"height\": 919, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1458, \"height\": 677, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1205, \"height\": 633, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1426, \"height\": 449, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1407, \"height\": 944, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1392, \"height\": 537, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 377, \"height\": 289, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1398, \"height\": 1402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1413, \"height\": 1660, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1419, \"height\": 1666, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-aydmnzpjpv/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1012, \"height\": 742, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-aydmnzpjpv/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 561, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-aydmnzpjpv/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 593, \"height\": 212, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-aydmnzpjpv/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1447, \"height\": 894, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-aydmnzpjpv/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1428, \"height\": 546, \"label\": \"Table\"}]"
motivation: 多模态大语言模型在被动静态推理中表现好，但缺乏在部分可观测物理环境中的主动探索能力。
method: 提出主动视觉推理任务，并设计闭环感知-推理-动作框架。
result: 在模拟物理环境中主动推理性能显著优于被动方法。
conclusion: 主动探索是提升MLLM在物理世界中推理能力的关键。
---

## Abstract
Visual reasoning in multimodal large language models (MLLMs) has primarily been studied in passive, static settings, limiting their effectiveness in real-world physical environments where an embodied agent must contend with incomplete information due to occlusion or a limited field of view. Humans, in contrast, leverage their embodiment to actively explore and interact with their environment—moving, examining, and manipulating objects—to gather information through a closed-loop process integrating perception, reasoning, and action. Inspired by this capability, we introduce the Active Visual Reasoning (AVR) task, extending visual reasoning to a paradigm of embodied interaction in partially observable environments. AVR necessitates embodied agents to: (1) actively acquire information via sequential physical actions, (2) integrate observations across multiple steps for coherent reasoning, and (3) dynamically adjust decisions based on evolving visual feedback. To rigorously evaluate AVR, we introduce CLEVR-AVR, a simulation benchmark featuring multi-round interactive environments designed to assess both reasoning correctness and information-gathering efficiency. We present AVR-152k, a large-scale dataset that offers rich Chain-of-Thought (CoT) annotations detailing iterative reasoning for uncertainty identification, action-conditioned information gain prediction, and information-maximizing action selection, crucial for training agents in a higher-order Markov Decision Process. Building on this, we develop PhysVLM-AVR, an embodied MLLM achieving state-of-the-art performance on CLEVR-AVR, embodied reasoning (OpenEQA, RoboVQA), and passive visual reasoning (GeoMath, Geometry30K). Our analysis also reveals that current embodied MLLMs, despite detecting information incompleteness, struggle to actively acquire and integrate new information through interaction, highlighting a fundamental gap in active reasoning capabilities.

---

## 论文详细总结（自动生成）

# 论文总结：PhysVLM-AVR：多模态大语言模型在物理环境中的主动视觉推理

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：多模态大语言模型（MLLMs）在被动、静态的视觉推理任务中表现优异，但在真实物理环境中，由于遮挡、视野有限等原因，信息往往部分可观测，导致模型的推理能力受限。当前方法缺乏主动探索和交互能力。
- **研究背景**：人类通过主动移动、操作物体来收集信息，形成“感知-推理-行动”闭环。受此启发，论文提出**主动视觉推理（Active Visual Reasoning, AVR）**任务，将视觉推理扩展到部分可观测的交互式环境，要求智能体主动获取信息、整合多步观测、动态决策。
- **整体含义**：AVR填补了静态视觉推理与具身智能之间的鸿沟，推动MLLM向更真实、更具自主性的物理世界理解前进。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
- 将AVR形式化为一个**高阶马尔可夫决策过程（Higher-order MDP）**，在每个时间步，智能体基于问题 \(Q\) 和历史观测 \(h_t\) 生成推理轨迹 \(Think_t\)，判断信息是否充足。若不充足，则选择信息增益最大的行动 \(a_t\) 执行，获取新观测，循环直至给出答案。

### 关键技术细节
- **问题形式化**：AVR定义为闭式循环，每步包括感知、推理、行动三步。行动选择以最大化关于真实答案 \(Y\) 的期望信息增益为目标（公式2）。
- **CLEVR-AVR基准**：基于Genesis物理仿真引擎，包含遮挡、堆叠、复合三种场景，提供多种动作（Pick、MoveObject、MoveViewer、RotateViewer），丰富的问答类型（计数、存在性、比较等），以及信息充分性判断、信息增益率、最终答案准确率三项评价指标。
- **AVR-152k数据集**：
  - **AVR-Caption（100k）**：室内场景密集标注（含边界框），用于基础视觉感知。
  - **AVR-Embodied Reasoning（50k）**：多图片序列+QA，用于时序视觉推理训练。
  - **AVR-Core（2k）**：核心部分，直接模拟高阶MDP，包含专家标注的Chain-of-Thought（CoT）注释，明确展示不确定性识别、行动信息增益预测、策略决策等步骤。
- **PhysVLM-AVR模型**：基于LLaVA架构，使用Qwen2.5-3B作为LLM解码器，SigLIP-400M作为视觉编码器，添加最大池化层将视觉token数减少3倍。训练分为四阶段：对齐→单图理解→综合视觉理解→通用推理+主动视觉推理（多数据集混合微调）。

## 3. 实验设计

### 数据集与场景
- **CLVER-AVR基准**：模拟环境中测试主动视觉推理能力（Occlusion, Stack, Composite三类场景）。
- **具身推理基准**：OpenEQA（物体识别、空间理解等7个子任务）、RoboVQA（BLEU评分）。
- **静态视觉推理基准**：GeoMath、Geometry3K。

### 对比方法
- 开源MLLM：Qwen2.5-VL-7B、LLaVA-OV-7B
- 推理型MLLM：R1-Onevision-7B、Reason-RFT-7B
- 具身型MLLM：Embodied-Reasoner-7B、RoboBrain-7B
- API型MLLM：GPT-4o、Gemini-2.0-flash
- 自己微调版本：AVR-Qwen2.5-VL-7B（在AVR-152K上微调）

### 评价指标
- CLEVR-AVR：信息充分性判断准确率（ACC_ISJ）、信息增益率（IGR）、最终答案准确率（ACC_FA）
- OpenEQA：LLM-score（GPT-4o评估）
- RoboVQA：BLEU1-4

## 4. 资源与算力
- 论文明确提到训练环境：Ubuntu服务器，配备**8块NVIDIA A800 GPU**，使用PyTorch 2.6.0、transformers 3.72.0、flash attention 2、DeepSpeed。
- 训练时长未明确说明，但给出了各阶段的batch size、学习率等超参数。

## 5. 实验数量与充分性
- **主要实验**：
  - CLEVR-AVR上对比了9种方法（含基线），报告了3类场景的平均指标。
  - 具身推理两个benchmark（OpenEQA、RoboVQA）和静态推理两个benchmark（GeoMath、Geometry3K）均给出了结果。
  - 消融实验：在CLEVR-AVR上对比“完整模型”、“去掉AVR-Core”、“去掉CoT注释”三种情况，验证了AVR-Core和CoT的重要性。
- **充分性评价**：
  - 实验覆盖了主动推理、具身推理、静态推理三大类，场景丰富，对比基线全面（从开源到API模型）。
  - 消融实验清晰，控制了关键变量。
  - 报告了多个种子（seed=42）下的平均结果，但未给出误差棒或统计显著性检验，略显不足。
  - 整体设计客观公平，但缺乏真实机器人平台实验，仅限仿真，可能不能完全推广到现实物理世界。

## 6. 主要结论与发现
- 现有MLLM（包括被动推理和具身推理模型）在主动视觉推理任务上表现极差（甚至接近零），说明被动能力无法迁移到主动环境。
- 具身模型（如Embodied-Reasoner-7B）虽能识别信息不完整，但无法有效进行信息获取和整合（最终准确率仅1.6%），存在根本性缺失。
- 本文提出的PhysVLM-AVR-3B在CLEVR-AVR上取得最高ACC_ISJ（90.5%），ACC_FA达到39.7%，显著优于其他开源模型，仅次于GPT-4o，验证了AVR框架的有效性。
- AVR-152k数据集（特别是AVR-Core及其CoT注释）对培养主动推理能力至关重要；去掉CoT或数据集会导致性能大幅下降。
- 主动推理训练还能提升模型在具身推理和静态推理任务上的泛化能力。

## 7. 优点
- **任务创新**：首次系统定义并形式化了主动视觉推理任务，填补了被动视觉与具身交互之间的空白。
- **基准与数据集全面**：CLEVR-AVR基准提供了多场景、多指标评价；AVR-152k数据集规模大（152k）且包含精细化的CoT人工注释，特别是AVR-Core直接建模MDP过程，为训练提供了结构化监督。
- **模型设计实用**：基于开源组件，采用多阶段混合训练策略，兼容多模态，同时保持一定效率（视觉token压缩）。
- **实验充分**：覆盖多个benchmark，与多个主流模型对比，消融实验清晰，结果有说服力。

## 8. 不足与局限
- **实验环境局限**：所有实验在仿真平台（Genesis）上进行，未在真实机器人环境中验证，真实世界中的噪声、控制误差等未考虑。
- **性能差距**：最终答案准确率（ACC_FA）仍与GPT-4o有差距（39.7% vs 45.7%），且远低于人类水平，说明最优动作选择和时序信息整合仍是瓶颈。
- **数据集规模较小**：AVR-Core仅2k样本，且由人工专家制作，可能难以覆盖多样化场景，且存在标注偏差风险。
- **模型规模有限**：模型参数量只有3B，可能限制了复杂推理能力，未来可探索更大模型。
- **未提供代码和数据的完全开放**：虽提及匿名链接，但未在论文中明确说明是否完全开源；附录仅给出提示示例，未给出完整数据集样本或模型权重。
- **缺乏统计显著性分析**：未给出多次重复实验的误差棒，结果稳定性有待验证。

（完）
