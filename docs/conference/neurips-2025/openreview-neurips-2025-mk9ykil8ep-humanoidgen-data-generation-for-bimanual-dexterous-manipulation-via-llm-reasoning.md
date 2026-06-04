---
title: "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning"
title_zh: HumanoidGen：基于LLM推理的双臂灵巧操作数据生成
authors: "Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Mk9ykil8eP"
tags: ["query:vla"]
score: 7.0
evidence: 利用LLM推理生成双臂灵巧操作数据，支持机器人基础模型
tldr: 双臂灵巧操作的数据收集极为困难，现有数据集多针对单臂机器人。HumanoidGen利用原子灵巧操作和LLM推理自动创建任务并生成演示，为双臂人形机器人提供丰富训练数据。实验验证生成的数据能有效训练操作策略，填补了该领域的数据空白。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1448, \"height\": 617, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1455, \"height\": 339, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1295, \"height\": 1144, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1444, \"height\": 489, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1414, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 726, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1446, \"height\": 340, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1444, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1442, \"height\": 283, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1244, \"height\": 1197, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1445, \"height\": 346, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1435, \"height\": 451, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1402, \"height\": 802, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-mk9ykil8ep/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1388, \"height\": 2230, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 660, \"height\": 484, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1443, \"height\": 783, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1445, \"height\": 983, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1444, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1429, \"height\": 148, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1388, \"height\": 176, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1462, \"height\": 150, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1457, \"height\": 147, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1445, \"height\": 329, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1441, \"height\": 1863, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1444, \"height\": 267, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-mk9ykil8ep/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1443, \"height\": 578, \"label\": \"Table\"}]"
motivation: 双臂灵巧操作缺乏高质量仿真任务和演示数据。
method: 通过原子操作定义和LLM推理生成空间约束，自动创建任务并收集演示。
result: 生成的数据成功训练了双臂操作策略，填补了数据缺口。
conclusion: LLM推理可有效自动化生成复杂操作数据。
---

## Abstract
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究背景**：机器人操作领域，现有数据集和仿真基准主要针对单臂机械臂平台，对于配备双臂和灵巧手的人形机器人，高质量的仿真任务和演示数据严重匮乏。
- **核心问题**：双臂灵巧操作需要协调手臂运动和手部操作，复杂性高，传统方法依赖昂贵的遥操作（如VR、外骨骼设备）或强化学习收集数据，难以覆盖多样化场景，且效率低、成本高。
- **整体含义**：本文旨在提出一个自动化的任务创建和演示数据生成框架HumanoidGen，利用LLM推理和原子灵巧操作，自动为双臂人形机器人生成多样化的操作任务和高品质演示数据，推动人形机器人操作研究的发展。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
### 核心思想
- 利用预定义的**原子操作**（如捏、抓、按）和**空间标注**（关键点、关键轴），结合LLM推理生成任务分解和动作约束链，再通过轨迹优化器求解约束得到可执行的机器人动作，以此自动生成演示数据。

### 关键技术细节
1. **空间标注与场景生成**
   - **手部原子操作标注**：定义每种原子操作的关键点、接近轴、附着轴、平行轴等（如图2所示），如“捏”操作中，接近轴、附着轴（拇指尖到食指尖）、平行轴。
   - **资产固有信息标注**：资产自身功能相关的点和轴（如杯子有倾倒点和存储点）。
   - **资产操作标注**：定义资产上可用于原子操作的关键点和轴（不同操作可共用，同一操作可有不同关键点）。
   - **场景生成**：LLM根据任务描述、资产库和场景细节，生成环境设置代码（物体种类、数量、位姿）和成功判定条件。

2. **LLM任务规划**
   - **任务分解**：LLM将长时域任务分解为动作序列S = {S1, ..., Sn}，每步包含手部操作（从原子库选择）和手臂运动（定义目标约束C_goal和路径约束C_path）。
   - **关系动作约束**：引入动态坐标系Fact，表示手和物体的几何关系，通过点、轴的对齐、平行、正交等约束描述动作意图。
   - **碰撞避免**：
     - **主动碰撞避免**：LLM生成脚本时主动包含避开碰撞的行为（如移开为另一只手腾出空间）。
     - **动态碰撞管理**：LLM动态调整物体忽略列表，允许在接触式操作中忽略特定碰撞（如拉抽屉时忽略手与抽屉的碰撞），在自由运动时启用碰撞检测。

3. **MCTS增强推理**
   - 针对长时域任务或标注不足的物体，LLM缺乏可靠推理，引入**分段-截断-合并-恢复（STCR）机制**和MCTS树搜索。
   - **STCR**：将规划代码分段、在出错处截断、合并意图一致的原子操作、恢复节点状态。
   - **MCTS**：在搜索树中进行选择（根据QDUCB值）、扩展（LLM根据节点信息生成新代码）、反向传播（基于“有价值时刻”的内在奖励更新节点价值），直到找到可执行方案。

4. **场景缩放**：将桌面级任务扩展到房间级场景，通过坐标变换对齐原始和新场景中的物体位姿，增加数据多样性。

## 3. 实验设计：数据集、benchmark、对比方法
- **Benchmark**：构建**HGen-Bench**，包含20个桌面级双臂灵巧操作任务，使用Unitree H1-2人形机器人搭配Inspire灵巧手，SAPIEN仿真引擎。任务难度分级（简单/困难），涵盖单臂/双臂、短时域/长时域、简单/复杂碰撞场景。提供来自6个相机的RGB-D图像、关节状态和动作真值。
- **数据生成**：每个任务生成100个演示样本。
- **对比方法**：主要与RoboTwin对比（修改版以支持灵巧手），使用DeepSeek-R1作为LLM。此外，对比了不同大模型（DeepSeek-R1、DeepSeek-Chat-v3、GPT-4o等）作为规划器的效果。
- **策略评估**：训练2D扩散策略（Diffusion Policy, DP）和3D扩散策略（DP3），测试数据规模（20/50/100个演示）对策略成功率的影响。
- **MCTS评估**：在4个任务上（Block Stack Single, Blocks Stack Easy, Blocks Stack Hard, Pyramid Stack）比较MCTS与非MCTS的推理成功率和token消耗。

## 4. 资源与算力
- 论文未明确说明训练扩散策略所使用的GPU型号、数量或训练时长。仅在附录C.4中提供了各阶段平均计算和token消耗：场景生成12.64s，脚本生成18.31s，数据执行14.40s；LLM推理平均使用约3000-4000 tokens。未提及具体硬件配置。

## 5. 实验数量与充分性
- **实验组数量**：三大组实验——(1)演示生成和执行成功率评估（20个任务，对比RoboTwin）; (2) MCTS有效性评估（4个任务，多个N值设置）; (3) 数据集训练策略评估（14个任务，3种数据规模，DP和DP3各3个随机种子）。
- **充分性评价**：实验设计较为全面，覆盖不同难度、不同任务类型、不同数据规模。消融实验（MCTS vs 非MCTS, 不同LLM, 碰撞管理对比）较充分。但策略训练部分（表2）显示部分复杂任务（如块堆叠、手递手存储）策略成功率很低，说明数据集质量仍有提升空间，实验尚不能完全证明生成数据能解决所有难题。总体上实验客观公平，误差棒和多次运行均有报告。

## 6. 论文的主要结论与发现
1. **HumanoidGen框架有效性**：在20个任务上平均演示生成执行成功率超过50%，复杂任务上优于RoboTwin，尤其在长时域和复杂碰撞任务中表现显著提升。
2. **MCTS增强推理**：MCTS可显著提升LLM在标注不足和长时域任务中的推理成功率（例如Blocks Stack Hard从18.3%提升到98.3%），且token消耗增量不大（约20%），同时生成计划多样性更高。
3. **数据质量验证**：基于生成数据训练的DP和DP3策略，随着数据量增加性能持续提升（如Open Box Hard从20演示的11.1%上升到100演示的100%），证明数据集有效且可扩展。
4. **实际应用**：通过真实世界实验（抓瓶子、关笔记本）验证了数据收集成功率超85%，且少量真实数据结合仿真数据可达到优于单纯使用真实数据的效果。

## 7. 优点：方法或实验设计上的亮点
- **自动化程度高**：从场景生成、规划代码生成到演示执行完全自动，仅需初始资产标注（4-6秒/类），大幅降低人力成本。
- **空间推理能力**：通过关键点和关键轴标注，LLM能够生成精确的几何约束，结合动态碰撞管理，处理复杂的接触式操作和长时域任务。
- **MCTS融合**：创新性地将MCTS与LLM结合用于任务规划，通过内在探索奖励和STCR机制，有效提升了复杂任务的成功率和计划多样性。
- **数据规模可扩展**：支持房间级场景缩放和位姿随机化，可快速生成大量多样化数据。
- **benchmark设计**：HGen-Bench覆盖多种难度和类型，为双臂灵巧操作研究提供了标准评估平台。

## 8. 不足与局限
- **仍需要少量人工标注**：对于新资产类别，需要手动标注原子操作关键点/轴，尚未实现完全零样本自动化。
- **仿真引擎限制**：基于ManiSkill3物理引擎，无法处理可变形物体或流体操作任务。
- **低层控制依赖运动规划器**：对于需要连续状态调整的任务（如推T、布匹整理）难以处理，仅能处理目标姿态明确的任务。
- **长时域复杂任务策略学习困难**：实验显示，对于某些超长时域任务（如Handover and Storage、Pyramid Stack），DP和DP3几乎无法学到有效策略，说明生成数据虽能执行但策略学习仍有瓶颈。
- **算力资源细节缺失**：未提供训练扩散策略的GPU型号、数量及耗时，复现成本不明确。
- **bechmark规模有限**：当前20个任务，未来可扩展更多资产和场景以增强代表性。

（完）
