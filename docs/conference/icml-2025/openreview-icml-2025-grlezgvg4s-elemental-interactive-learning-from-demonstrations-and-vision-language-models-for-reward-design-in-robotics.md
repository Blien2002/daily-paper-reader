---
title: "ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics"
title_zh: ELEMENTAL：基于演示与视觉语言模型的交互式机器人奖励设计
authors: "Letian Chen, Nina Marie Moorman, Matthew Craig Gombolay"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=grlezgVg4s"
tags: ["query:vla"]
score: 8.0
evidence: 结合演示与VLM的交互式机器人奖励设计
tldr: 针对LLM在机器人奖励设计中难以平衡特征重要性且泛化差的问题，提出ELEMENTAL框架，融合自然语言引导与视觉演示来对齐机器人行为。利用VLM理解多模态信号，自动生成稠密奖励函数，在多样化机器人任务中提升学习效率与用户对齐度。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1590, \"height\": 806, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1776, \"height\": 867, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 842, \"height\": 595, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 773, \"height\": 1021, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 798, \"height\": 658, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 799, \"height\": 658, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-grlezgvg4s/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1740, \"height\": 303, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 814, \"height\": 691, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1799, \"height\": 690, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1708, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1391, \"height\": 204, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1714, \"height\": 594, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1747, \"height\": 1155, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1785, \"height\": 403, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1712, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1466, \"height\": 239, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1354, \"height\": 167, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1693, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1710, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-grlezgvg4s/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1579, \"height\": 337, \"label\": \"Table\"}]"
motivation: LLM难以平衡特征重要性且泛化差。
method: 融合自然语言引导与视觉演示，利用VLM生成奖励。
result: 在多种机器人任务中提升学习效率与用户对齐度。
conclusion: 为VLM与机器人动作空间集成提供有效框架。
---

## Abstract
Reinforcement learning (RL) has demonstrated compelling performance in robotic tasks, but its success often hinges on the design of complex, ad hoc reward functions. Researchers have explored how Large Language Models (LLMs) could enable non-expert users to specify reward functions more easily. However, LLMs struggle to balance the importance of different features, generalize poorly to out-of-distribution robotic tasks, and cannot represent the problem properly with only text-based descriptions. To address these challenges, we propose ELEMENTAL (intEractive LEarning froM dEmoNstraTion And Language), a novel framework that combines natural language guidance with visual user demonstrations to align robot behavior with user intentions better. By incorporating visual inputs, ELEMENTAL overcomes the limitations of text-only task specifications, while leveraging inverse reinforcement learning (IRL) to balance feature weights and match the demonstrated behaviors optimally. ELEMENTAL also introduces an iterative feedback-loop through self-reflection to improve feature, reward, and policy learning. Our experiment results demonstrate that ELEMENTAL outperforms prior work by 42.3% on task success, and achieves 41.3% better generalization in out-of-distribution tasks, highlighting its robustness in LfD.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：强化学习（RL）在机器人任务中依赖精心设计的奖励函数，而手动设计奖励函数复杂且易出错。现有利用大语言模型（LLM）自动生成奖励函数的方法（如EUREKA）存在以下不足：（1）仅依靠文本描述难以精确表达用户意图，忽略了用户潜在偏好；（2）LLM无法合理平衡多个奖励分量的重要性；（3）生成的奖励函数在分布外任务上泛化能力差。
- **整体含义**：为了克服上述局限，论文提出 **ELEMENTAL** 框架，将**视觉语言模型（VLM）** 与**逆强化学习（IRL）** 相结合，利用人类提供的**视觉演示**（而非仅文本）来推断任务特征，并通过迭代自反思机制不断优化特征函数、奖励函数和策略。目标是让机器人更准确、鲁棒地学习用户意图，同时提升对未见任务的泛化能力。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：融合 VLM 的语义理解能力与 IRL 的演示匹配能力，通过视觉演示补充文本描述的模糊性，利用 IRL 自动确定特征权重，并引入自反思循环闭环改进。
- **技术细节与流程**（三个阶段）：
  1. **Phase 1：初始提示**  
     - 输入：MDP环境代码、任务文本描述、**视觉演示**（对于运动任务使用叠加图像，对于操作任务使用关键帧）。  
     - VLM（GPT-4o）生成**特征函数** \(\phi(s): S \to \mathbb{R}^n\)，以Python代码形式输出。若代码不可执行则重试至多3次。
  2. **Phase 2：学习（近似MaxEnt-IRL）**  
     - 假设奖励函数为特征的线性组合：\(R_\theta(s)=\theta^T\phi(s)\)。  
     - 采用**近似最大熵逆强化学习（Approximate MaxEnt-IRL）**，利用策略\(\pi_\psi\)近似专家策略，梯度为：
       \[
       \nabla_\theta \approx \mathbb{E}_{\tau\sim\mathcal{D}}\left[\sum_{s\in\tau}\phi(s)\right] - \mathbb{E}_{\tau\sim\pi_\psi}\left[\sum_{s\in\tau}\phi(s)\right]
       \]
     - 对梯度进行L1范数归一化（Eq.5），更新θ后对θ进行L1归一化（Eq.6），确保稳定性。  
     - 算法流程：初始化θ为均匀权重，交替优化策略π_ψ（使用PPO）和更新θ（梯度上升），迭代m=5次。
  3. **Phase 3：自反思**  
     - 计算当前策略生成的轨迹与演示轨迹的**特征计数**向量（Eq.7）。  
     - 将特征计数差异反馈给VLM，VLM据此**修改特征函数**，例如调整特征尺度、重写或丢弃特征。  
     - 重复Phase 2和3直至性能收敛（默认3次迭代）。

### 3. 实验设计：数据集/场景、Benchmark、对比方法
- **模拟环境**：**IsaacGym** 中的9个高难度机器人任务，涵盖运动控制（Cartpole、BallBalance、Quadcopter、Ant、Humanoid、Anymal）和操作任务（FrankaCabinet、AllegroHand、ShadowHand）。每个任务使用5条由RL训练策略生成的演示。
- **基准方法**：
  - 行为克隆（BC）
  - 传统IRL（不带VLM特征）
  - **EUREKA**（SOTA LLM奖励设计方法，仅文本）
  - 随机策略（下界）
  - 真实奖励（GT，上界）
  - ELEMENTAL的**6个消融变体**：无自反思、无梯度归一化、无权重归一化、无视觉输入、用文本代替演示、用随机视觉演示。
- **泛化实验**：在Ant任务上设计4种变体：原始Ant、状态向量反转、更轻重力、反向跑步任务。
- **真实用户研究**：12名参与者使用Kinova JACO机械臂进行沙拉混合任务，教授3个技能（抓蘑菇、放至碗中、搅拌），对比ELEMENTAL与EUREKA，使用7点Likert量表评估任务表现和策略对齐。
- **统计检验**：采用独立t检验或Mann-Whitney U检验（5个种子），报告p值。

### 4. 资源与算力（文中说明）
- 论文未明确列出整体训练使用的GPU型号、数量及总时长。但提及：
  - 模拟实验使用**GPU加速训练**（IsaacGym支持GPU）。
  - 真实用户研究中，每个学习轮次在**NVIDIA A40 GPU**的远程服务器上完成，耗时**少于4分钟**。
  - ELEMENTAL平均运行时间168.36分钟（9个任务），EUREKA平均68.21分钟，增加的原因是IRL需要环境rollout。
- 评价：算力描述不够详细，但提供了相对时间和真实世界部署信息。

### 5. 实验数量与充分性
- **模拟实验**：9个任务×多种基线+6个消融，共约9×(1(BC)+1(IRL)+1(EUREKA)+1(Random)+1(GT)+6(消融))=99组实验（每个种子一次），部分报告了5个种子的均值和标准差。外加4个泛化任务。
- **消融实验**覆盖了关键组件：自反思、归一化、视觉模态、演示质量，系统性地验证了各部分贡献。
- **真实用户研究**：12名参与者的受试者内设计，两个指标各4题，共24个评分，统计显著。
- **充分性评价**：实验数量较多，覆盖模拟、泛化、真实场景，统计检验合理，但缺少更多随机种子（仅报告3或5个种子）和更多泛化域（仅Ant变体）。总体较为充分、客观、公平。

### 6. 论文的主要结论与发现
1. ELEMENTAL在IsaacGym 9个任务上平均任务成功率比EUREKA**高出42.3%**，在8个任务上占优。
2. 在分布外泛化任务上，ELEMENTAL比EUREKA**提升41.3%**，表明VLM+IRL结合能更好地适应环境变化和任务迁移。
3. **消融实验**证实：自反思、归一化步骤、视觉输入均为关键组件；去除任一组件性能显著下降。
4. 特征函数代码执行率：ELEMENTAL首次迭代约**80%**，显著高于EUREKA的不足50%（p=0.030），说明VLM更适合生成特征提取代码而非完整奖励函数。
5. 真实用户评价：ELEMENTAL在任务表现和策略对齐上均显著优于EUREKA（p<0.001），用户反馈其能容忍不完美演示。
6. 奖励函数与真实奖励的相关性：ELEMENTAL在大部分任务中更高，表明学习到的奖励更准确。

### 7. 优点：方法或实验设计上的亮点
- **方法创新**：
  - 首次将**视觉演示**直接输入VLM用于奖励设计，有效缓解文本模糊性。
  - 将特征设计（VLM擅长）与特征加权（IRL擅长）解耦，各取其长。
  - 自反思循环使系统能自动修正特征错误，无需额外人工干预。
- **实验设计亮点**：
  - 不仅评测标准任务，还设计了**分布外泛化**（改变物理参数、任务目标），检验模型鲁棒性。
  - 包含**真实用户研究**，验证了实际交互中的有效性。
  - 消融实验全面，证明了每个技术点的必要性。
- **实用价值**：框架通用，提示词无需针对具体环境定制，可批处理高维机器人任务。

### 8. 不足与局限
- **实验覆盖局限**：
  - 模拟环境仅为IsaacGym，未包含更复杂的真实物理仿真或动态环境。
  - 泛化实验仅针对Ant任务，其他任务和更极端的变化未测试。
- **资源与可扩展性**：
  - ELEMENTAL运行时间约为EUREKA的2.5倍，依赖环境rollout，计算开销大。
  - 依赖VLM的代码生成能力，若VLM生成不可执行代码需重试，增加延迟。
- **演示质量假设**：
  - 虽然用户研究表明能容忍一定噪声，但极度随机或低质量演示仍会导致性能下降（消融实验显示）。
  - 演示由RL策略生成，非真实人类演示（除用户研究外），可能无法完全反映非专家行为。
- **潜在偏差**：
  - 使用GPT-4o作为VLM，可能产生幻觉或过拟合语言先验。
  - 自反思可能引入累积错误，VLM生成的改进特征可能在某些任务上不稳定。
- **应用限制**：需要视觉输入和IRL训练基础设施，对低成本机器人部署不够友好；未讨论多任务或任务序列的泛化。

（完）
