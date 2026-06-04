---
title: "Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models"
title_zh: Hi Robot：基于层次化视觉-语言-动作模型的开放式指令跟随
authors: "Lucy Xiaoyang Shi, brian ichter, Michael Robert Equi, Liyiming Ke, Karl Pertsch, Quan Vuong, James Tanner, Anna Walling, Haohuan Wang, Niccolo Fusai, Adrian Li-Bell, Danny Driess, Lachy Groom, Sergey Levine, Chelsea Finn"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=lNVHg9npif"
tags: ["query:vla"]
score: 10.0
evidence: 用于开放式指令跟随的层次化视觉-语言-动作模型
tldr: 通用机器人需处理复杂指令和反馈。本文提出Hi Robot，一种层次化视觉-语言-动作模型系统，首先利用VLM推理复杂提示和用户反馈，确定最合适的下一步骤，然后执行具体动作。该系统在多种开放世界任务中展示了对复杂指令的理解和执行能力，代表了VLA模型在具身智能中的前沿进展。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1717, \"height\": 624, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 813, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 808, \"height\": 771, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1727, \"height\": 1829, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1730, \"height\": 446, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1733, \"height\": 594, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 816, \"height\": 537, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-lnvhg9npif/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 822, \"height\": 545, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-lnvhg9npif/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 617, \"height\": 285, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-lnvhg9npif/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 878, \"height\": 1392, \"label\": \"Table\"}]"
motivation: 机器人需理解复杂指令和用户反馈。
method: 构建层次化VLA系统，顶层推理任务计划，底层执行动作。
result: 成功执行多种开放世界指令，展现强大理解能力。
conclusion: 层次化结构有效处理复杂指令跟随。
---

## Abstract
Generalist robots that can perform a range of different tasks in open-world settings must be able to not only reason about the steps needed to accomplish their goals, but also process complex instructions, prompts, and even feedback during task execution. Intricate instructions (e.g., "Could you make me a vegetarian sandwich?" or "I don't like that one") require not just the ability to physically perform the individual steps, but the ability to situate complex commands and feedback in the physical world. In this work, we describe a system that uses vision-language models in a hierarchical structure, first reasoning over complex prompts and user feedback to deduce the most appropriate next step to fulfill the task, and then performing that step with low-level actions. In contrast to direct instruction following methods that can fulfill simple commands ("pick up the cup"), our system can reason through complex prompts and incorporate situated feedback during task execution ("that's not trash"). We evaluate our system across three robotic platforms, including single-arm, dual-arm, and dual-arm mobile robots, demonstrating its ability to handle tasks such as cleaning messy tables, making sandwiches, and grocery shopping.
Videos are available at https://www.pi.website/research/hirobot

---

## 论文详细总结（自动生成）

# 中文总结：Hi Robot：基于层次化视觉-语言-动作模型的开放式指令跟随

## 1. 论文的核心问题与整体含义（研究动机和背景）
- 通用机器人需要在开放世界环境中执行多样化任务，不仅要推理完成目标的步骤，还要处理复杂指令、提示和任务执行过程中的实时反馈。
- 现有指令跟随方法（如RT-2、π0等）通常限于简单原子指令（如“拿起杯子”），无法处理复杂多步指令（如“做一个素食三明治，不要西红柿”）或动态的用户反馈（如“这个不是垃圾”）。
- 类比Kahneman的“系统1”和“系统2”认知过程：系统1负责自动、快速的技能执行；系统2负责深思熟虑的高层推理。本文旨在构建一个结合两者能力的层次化系统。

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：采用层次化结构，将策略分解为高层推理和低层执行。
  - **高层策略（High-Level Policy）**：使用VLM（视觉-语言模型）处理复杂提示、用户反馈和当前图像观测，输出低层语言命令（如“拿起生菜”）和可选的机器人话语。
  - **低层策略（Low-Level Policy）**：使用VLA（视觉-语言-动作模型）接收高层输出的简单命令，结合图像和机器人状态，通过流匹配（flow matching）直接输出连续动作块。
- **推理流程**：高层推理以较低频率运行（每隔1秒或收到新用户输入时触发），将复杂任务分解为原子命令输出给低层策略执行。低层策略以高频（约10Hz）产生动作。
- **训练数据**：
  - 收集遥控操作演示数据，分割为短技能片段（持续1-3秒），并标注原子命令。
  - **合成数据生成**：利用一个强大的VLM（pgen）基于当前观测和技能标签，生成假设的用户提示和机器人回应。该过程包括场景分类（负面任务、情境纠正、特定约束等）和响应分类，确保多样性。
  - 高层策略在合成数据+真实标注数据上训练，使用交叉熵损失；低层策略在标注数据+演示数据上使用流匹配目标训练。
- **模型架构**：高低层策略均基于PaliGemma-3B VLM初始化；低层额外添加流匹配“动作专家”以输出连续动作。

## 3. 实验设计：数据集、场景、基准与对比方法
- **三个任务域**：
  - **餐桌清理（Table Bussing）**：清理餐桌，将餐具放入箱子、垃圾放入垃圾桶。评估复杂提示如“只清理垃圾不洗碗”、“清理所有黄色的东西”，以及实时纠正如“这不是垃圾”。
  - **做三明治（Sandwich Making）**：使用最多6种原料和面包制作三明治。评估提示如“做一个素三明治，我过敏腌菜”，以及实时纠正如“够了，不要了”。
  - **杂货购物（Grocery Shopping）**：从货架拿取指定物品放入篮子。评估提示如“给我拿些薯片”、“拿点甜的”、“再拿一个KitKat”。
- **对比方法**：
  - 专家人类高层（oracle）：人类代替高层模型输入最佳原子命令。
  - GPT-4o高层模型：使用GPT-4o API作为高层，低层为相同VLA，通过精心设计的系统提示选择原子命令。
  - 扁平VLA：直接使用π0低层，无高层。
  - 扁平VLA+合成数据：在低层训练中加入合成数据，无高层。
  - Hi Robot无合成数据：高层仅用真实标注数据训练。
- **评估指标**：
  - **指令准确性（Instruction Accuracy, IA）**：由盲评人员评估高层输出命令与用户意图和当前观测的一致性。
  - **任务进度（Task Progress, TP）**：量化对象被正确放置在正确位置的比例。
- 每个任务每种方法进行**20次试验**。

## 4. 资源与算力
- **训练硬件**：高层策略训练在8×H100 GPU上进行，约需**2小时**。
- 低层策略训练类似但耗时取决于数据集大小。
- **推理硬件**：使用1-2块NVIDIA GeForce RTX 4090消费级GPU即可实现实时推理（约10Hz控制率，通过动作分块可达50Hz）。
- 附录提供了详细的推理延迟数据（低层单步约73ms，高层单解码步约13-14ms）。

## 5. 实验数量与充分性
- 共在**三个不同机器人平台**（单臂UR5e、双臂ARX、移动双臂Mobile ARX）上评估，涵盖物理难度和语义复杂度各异的场景。
- 每个任务每个方法做**20次试验**，统计IA和TP，结果报告平均值（图中可见误差条）。对比实验包括4种主要基线+2种消融，覆盖了关键设计选择（合成数据、层次结构）。
- 消融实验验证了合成数据的重要性（图7）和层次结构优于扁平策略（图8）。
- 实验较为充分，对比了多个强基线（包括GPT-4o和oracle人类高层），公平性由盲评保障。但缺少其他层次化方法（如YAY Robot、OLAF）的直接量化比较，仅在相关工作中定性讨论。

## 6. 论文的主要结论与发现
- **Hi Robot在开放式指令跟随上显著优于GPT-4o和扁平VLA**，指令准确性平均高40%以上，任务进度也更高。
- 能够正确处理实时反馈（如“这不是垃圾”），而GPT-4o常丢失上下文或发出无意义命令。
- 在三个不同机器人平台上均有效，展示了良好的跨任务泛化性。
- 专家人类高层实验表明低层策略本身已足够强，瓶颈在于高层推理；Hi Robot很好地弥合了这一差距。
- 合成数据对处理多样化和全新提示至关重要；无合成数据时高层会忽略澄清或包含禁忌物品。
- 层次结构优于扁平策略，后者难以适应中途约束和局部指令。

## 7. 优点
- **创新性**：首次将VLM同时用于高层推理和低层执行，借助合成数据生成实现开放式指令跟随，无需大量人工标注交互数据。
- **实用性**：系统可在消费级GPU上实时运行，支持多平台（单臂、双臂、移动），具备实际部署潜力。
- **鲁棒性**：对复杂、多段指令和实时语言反馈有良好适应性，行为符合用户意图。
- **消融实验清晰**：分别验证了合成数据和层次结构的贡献，提供了有力的 ablation 证据。

## 8. 不足与局限
- **高层与低层训练解耦**：两者互相不了解对方的能力边界，可能产生高层输出低层无法执行的命令。未来可通过更紧密的耦合（如考虑低层成功率）改进。
- **提示工程依赖**：合成数据生成需要手动设计提示和场景分类，可能引入偏差；跨任务统一的高层策略尚未验证（当前每个任务单独训练）。
- **缺乏长期记忆**：系统无显式记忆，难以处理需要长上下文推理的指令（如“记住我过敏的东西”）。
- **失败模式**：低层策略有时会因训练偏差（如靠近物体时忽略指令）而出现错误导航；对象掉落等特殊情况恢复能力有限。
- **对比不完整**：未与同样处理实时反馈的方法（如OLAF、YAY Robot、RACER）进行直接定量比较，仅定性讨论。
- **泛化性局限**：仅在三个特定场景评估，未涵盖更广泛的开放世界任务（如家庭清洁、烹饪等），且每个场景的数据量未说明。

（完）
