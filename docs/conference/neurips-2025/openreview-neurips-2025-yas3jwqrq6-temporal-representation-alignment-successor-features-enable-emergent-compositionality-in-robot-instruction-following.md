---
title: "Temporal Representation Alignment: Successor Features Enable Emergent Compositionality in Robot Instruction Following"
title_zh: 时间表示对齐：后继特征实现机器人指令跟随中的突现组合性
authors: "Vivek Myers, Bill Zheng, Anca Dragan, Kuan Fang, Sergey Levine"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=yaS3JWQRQ6"
tags: ["query:vla"]
score: 7.0
evidence: 时间表示对齐用于机器人指令跟随
tldr: 机器人指令跟随需要任务表示的组合性，但自动学习此类表示困难。该工作通过时间对齐损失学习当前与未来状态的关联表示，使智能体无需显式子任务规划即可组合基本任务。在多种机器人操作实验中，该方法显著提升组合泛化能力，尤其适用于多步骤指令。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1309, \"height\": 600, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 723, \"height\": 427, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 564, \"height\": 455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 772, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 751, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1304, \"height\": 497, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1311, \"height\": 1103, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1137, \"height\": 647, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-yas3jwqrq6/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 941, \"height\": 632, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1412, \"height\": 352, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1455, \"height\": 623, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1265, \"height\": 416, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1455, \"height\": 609, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1450, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 974, \"height\": 427, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1455, \"height\": 644, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1452, \"height\": 306, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1454, \"height\": 633, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-yas3jwqrq6/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1452, \"height\": 308, \"label\": \"Table\"}]"
motivation: 机器人需要组合任务表示但缺乏有效的自动学习方法。
method: 利用时间对齐损失学习当前与未来状态表示关联，实现突现组合性。
result: 在多个操作任务中，该方法显著增强对复合指令的零样本泛化。
conclusion: 时间对齐是学习可组合任务表示的有效策略。
---

## Abstract
Effective task representations should facilitate compositionality, such
that after learning a variety of basic tasks, an agent can perform
compound tasks consisting of multiple steps simply by composing the
representations of the constituent steps together. While this is
conceptually simple and appealing, it is not clear how to automatically
learn representations that enable this sort of compositionality. We show
that learning to associate the representations of current and future
states with a temporal alignment loss can improve compositional
generalization, even in the absence of any explicit subtask planning or
reinforcement learning. We evaluate our approach across diverse robotic
manipulation tasks as well as in simulation, showing substantial
improvements for tasks specified with either language or goal images.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：机器人指令跟随需要任务表示的组合性——智能体在学习了多种基本任务后，应能通过组合这些基本任务的表示来执行多步骤复合任务。然而，如何自动学习能支持这种组合性的表示尚不明确。
- **核心问题**：传统的分层学习、显式子任务规划、基于动态规划的“缝合”等方法在实际机器人场景中往往不稳定或数据效率低，难以规模化。人类和动物能快速组合行为，其背后可能依赖后继表示、因果模型等结构化世界表征。因此，作者希望探索：在机器人学习中，能否通过简单的辅助学习目标来涌现组合行为，而无需显式规划或强化学习？

## 2. 方法论
- **核心思想**：Temporal Representation Alignment (TRA) 通过学习一个时间对比（time-contrastive）对齐损失，将当前状态表示与未来状态表示对齐，同时将目标图像/语言指令表示与状态表示对齐，从而构建一个结构化的共享表示空间。这种结构使得策略能够隐式地将长时任务分解为已知子步骤并顺序执行，无需显式规划或层次结构。
- **关键技术细节**：
  - 学习三个编码器：ϕ（编码当前状态）、ψ（编码未来目标状态/目标图像）、ξ（编码语言指令）。
  - 采用两个对比损失（InfoNCE）：
    1. 时间对齐损失：对齐 ϕ(s_t) 与 ψ(s_{t+k})，其中 k 服从几何分布，实现时间上的表示对齐。
    2. 任务对齐损失：对齐 ψ(goal_image) 与 ξ(language_instruction)，实现语言与视觉目标的对齐。
  - 同时训练一个行为克隆（BC）策略 π(a|s, φ)，条件可以是目标图像（ψ(g)）或语言指令（ξ(l)）。
  - 总损失函数 L_TRA = L_BC + L_NCE(时间) + L_NCE(任务)。
- **理论分析**：作者在假设策略通过推断路径点（waypoints）因式分解的条件下，给出了组合泛化误差的上界，表明TRA的结构化表示可以减少分布外复合任务的误差。

## 3. 实验设计
- **数据集与场景**：
  - **真实世界实验**：使用 BridgeData V2 数据集（增强版，包含5万+轨迹，7.2万语言标注），在 WidowX250 机械臂上进行评估。设计四个场景（难度递增）：
    - A（一步任务）：开抽屉等已见单步任务。
    - B（任务串联）：顺序执行多个同类型子任务（如扫多个物体）。
    - C（语义泛化）：操作同一类不同物体（如多种食物放入碗）。
    - D（依赖任务）：子任务间有依赖关系（如先从抽屉取出物体再放置）。
  - **仿真实验**：使用 OGBench 离线RL基准套件，包含7个环境（如 antmaze、humanoidmaze、cube stacking），其中5个使用“stitch”数据集（显式测试组合泛化），2个使用通用goal-reaching数据集。
- **对比方法**：
  - GRIF：仅使用目标-语言对齐，无时间对齐。
  - GCBC / LCBC：标准目标条件/语言条件行为克隆。
  - Octo：基于 Open-X 数据集的多模态Transformer。
  - AWR：离线RL方法，用优势加权回归，使用对比损失之差作为价值代理。
- **消融实验**：将TRA与“TRA + AWR”比较，验证额外RL目标是否带来提升。

## 4. 资源与算力
- 论文明确指出：训练TRA策略使用**一个Google V4-8 TPU VM实例**，训练**150,000步**，总时长**20小时**。使用**ResNet-34**架构，**学习率3e-4**，**ADAM优化器**，**2000步线性预热**，**MLP头3层256维**。仿真实验使用OGBench默认配置，未单独说明算力，但每个实验使用10个随机种子，计算量中等。

## 5. 实验数量与充分性
- **真实世界实验**：共13个任务（按场景分布：A 4个，B 4个，C 3个，D 2个），每个任务进行5~10次试验，报告成功率和标准误差（±1σ）。最终表格（Table 1）给出了所有方法与任务的成功率，并统计显著性（单侧t检验，p<0.05）。
- **仿真实验**：7个环境，每个方法使用10个种子，取最后3个评估周期的平均成功率作为结果。与多种基线对比（GCBC, CRL, GCIQL, GCIVL, QRL等）。
- **消融实验**：对比TRA与TRA+AWR，汇总所有场景的指令跟随和目标到达成功率（Fig. 4）。
- **理论分析**：提供了组合泛化误差界（Theorem 1, Corollary 1.1），并在附录中给出证明。
- **评价**：实验设计较为充分：覆盖了真实世界与仿真、多种难度场景、多种基线（包括离线RL和大型预训练策略），并进行了统计显著性检验。不过真实世界任务数量有限（13个），且每个任务仅5~10次试验，可能会带来一定方差。仿真的7个环境覆盖了不同复杂度，但缺乏更复杂的任务（如长时多物体操作）。

## 6. 主要结论与发现
- TRA在组合泛化任务上显著优于所有基线，在指令跟随任务上整体成功率提升超过40%，在目标到达任务上也有明显提升。
- TRA无需显式规划或分层结构，仅通过时间对比对齐就能涌现组合行为。
- TRA在仿真“stitch”数据集上也优于GCBC和其他非RL方法，在某些环境中甚至超过传统离线RL方法。
- 添加AWR（离线RL）作为额外损失并不能进一步提升TRA性能，提示TRA自身已足够实现良好的组合行为。
- 失败案例主要源于高斯策略无法处理多峰行为，以及深度理解不足（如早期抓取、延迟释放）。

## 7. 优点
- **方法简洁有效**：仅添加一个时间对比辅助损失，无需改变推理流程，即可显著提升组合泛化，具备实用性和可扩展性。
- **理论与实验结合**：提供了组合泛化误差的理论界，支撑了方法有效性的直觉。
- **泛化性强**：在真实世界的多种操作任务（物体搬运、抽屉操作、布料折叠等）和仿真环境（导航、操作）中均表现优异，适用于语言指令和目标图像两种任务设定。
- **公平比较**：与多个代表性基线（包括大型预训练策略Octo和离线RL方法AWR）在同一数据集和评估协议下进行对比，并做统计显著性检验。
- **开源代码**：提供了匿名代码仓库，便于复现。

## 8. 不足与局限
- **策略表达限制**：使用高斯策略，当存在多峰行为时容易失败（如早期抓取、延迟释放），可能需要更复杂的策略模型（扩散策略、Transformer）。
- **实验规模**：真实世界任务仅13个，每个任务试验次数较少（5~10次），可能受随机初始化影响较大。可扩展至更多样化的场景验证泛化性。
- **依赖大规模数据集**：TRA训练依赖 BridgeData 这种大规模专家演示数据，对于小样本或稀疏奖励场景的适用性未知。
- **安全与对齐**：作者指出未来工作应考虑任务泛化中的安全性，避免出现“突现失对齐”（emergent misalignment），但本文未涉及安全评估。
- **与最先进离线RL方法的差距**：在非stitch数据集（如 antmaze large navigate, cube single noisy）中，TRA虽然优于GCBC，但不及一些专门设计的离线RL方法（如GCIQL、QRL），说明TRA主要针对组合泛化场景，并非通用增强器。

（完）
