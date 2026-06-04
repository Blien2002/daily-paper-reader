---
title: "NBDI: A Simple and Effective Termination Condition for Skill Extraction from Task-Agnostic Demonstrations"
title_zh: NBDI：一种简单有效的技能提取终止条件
authors: "Myunsoo Kim, Hayeong Lee, Seong-Woong Shim, JunHo Seo, Byung-Jun Lee"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=8ino4CdB6w"
tags: ["query:vla"]
score: 4.0
evidence: 从任务无关演示中提取技能用于智能体决策
tldr: 针对技能学习中固定长度技能可能错过决策点的问题提出基于新颖性的决策点识别方法（NBDI）利用智能体经验数据学习终止条件。实验表明NBDI在多个机器人任务中优于先前方法有效促进了探索和策略学习。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1594, \"height\": 467, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1723, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 858, \"height\": 264, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1744, \"height\": 772, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1756, \"height\": 510, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1565, \"height\": 418, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 865, \"height\": 319, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 670, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1782, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 373, \"height\": 374, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1783, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1488, \"height\": 1026, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1647, \"height\": 885, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1701, \"height\": 1912, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1770, \"height\": 1014, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 878, \"height\": 645, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-8ino4cdb6w/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1573, \"height\": 2098, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-8ino4cdb6w/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 722, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-8ino4cdb6w/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 857, \"height\": 143, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-8ino4cdb6w/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1014, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-8ino4cdb6w/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1401, \"height\": 916, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-8ino4cdb6w/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1763, \"height\": 598, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-8ino4cdb6w/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1212, \"height\": 1069, \"label\": \"Table\"}]"
motivation: 固定长度技能会跳过有价值决策点限制探索和策略学习。
method: 提出基于状态-动作新颖性的决策点识别模块来学习技能终止条件。
result: 在多个机器人任务中优于先前方法收敛速度更快。
conclusion: NBDI提供了一种简单有效的技能分割方法有助于层次化强化学习。
---

## Abstract
Intelligent agents are able to make decisions based on different levels of granularity and duration. Recent advances in skill learning enabled the agent to solve complex, long-horizon tasks by effectively guiding the agent in choosing appropriate skills. However, the practice of using fixed-length skills can easily result in skipping valuable decision points, which ultimately limits the potential for further exploration and faster policy learning.
In this work, we propose to learn a simple and effective termination condition that identifies decision points through a state-action novelty module that leverages agent experience data.
Our approach, Novelty-based Decision Point Identification (NBDI), outperforms previous baselines in complex, long-horizon tasks, and remains effective even in the presence of significant variations in the environment configurations of downstream tasks, highlighting the importance of decision point identification in skill learning.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究背景**：在强化学习中，时间抽象（temporal abstraction）通过将低级动作组合成技能（skill）来简化长期任务决策。现有技能学习方法（如SPiRL）通常使用固定长度技能，这会导致智能体在关键决策点（如十字路口、子任务完成点）错过切换时机，从而限制探索效率和策略学习速度。
- **核心问题**：如何在任务无关的演示数据中自动识别关键决策点，并据此学习可变的技能终止条件，使得技能能够在恰当的位置终止，以促进下游任务学习。
- **整体含义**：技能终止条件的好坏直接影响层次化RL的性能。NBDI提出一种简单、有效且鲁棒的终止条件识别方法，显著提升在复杂长期任务中的表现。

## 2. 论文提出的方法论

- **核心思想**：利用状态-动作对的新颖性（novelty）来识别决策点。新颖性越高，表示该状态-动作对在数据中越罕见或在该状态下有多种可能动作（条件动作新颖性高），这些点往往是子任务完成点或岔路口。
- **关键技术细节**：
  - 使用**内在好奇心模块（ICM）**作为新颖性估计器，预训练于任务无关的演示数据。ICM通过预测下一状态的特征表示，计算预测误差作为状态-动作新颖性χ(s,a)。
  - 将新颖性分解为状态新颖性χ(s)与条件动作新颖性χ(a|s)：χ(s,a) = 1/N(s,a) ∝ χ(s) · χ(a|s)。
  - 基于预训练的新颖性值设定阈值（通常为数据集内新颖性分布的约97百分位），将超过阈值的时刻标记为终止点β=1。
  - 联合训练一个深度潜变量模型（LSTM编码器+解码器），同时学习**技能嵌入z**、**终止分布p(β|s,a)** 和**技能先验p(z|s)**。目标函数包括重构损失（动作序列和终止点）、KL正则化以及先验匹配损失。
- **算法流程**（文字说明）：
  1. **新颖性学习与技能提取**：在任务无关演示集上预训练ICM得到每个(s,a)的新颖性值；然后使用这些新颖性值作为监督信号，训练潜变量模型，使得技能能够在预测的终止点结束。
  2. **下游强化学习**：将预训练的低级策略π(a|z,s)和终止分布p(β|s,a)固定。在SMDP框架下，高级策略μ(z|s)输出技能嵌入，执行直到采样到β=1或达到最大长度H，累积折扣奖励˜r，然后更新高级策略（使用SAC算法并加入KL正则化）。

## 3. 实验设计

- **环境/场景**：
  - **迷宫导航**（30×30和40×40）：任务无关演示来自随机布局，下游任务使用全新布局（大小、结构不同）。
  - **稀疏块堆叠**：演示环境有5个块，下游任务有11个块随机位置，奖励仅由堆叠高度决定（稀疏）。
  - **厨房环境**（D4RL Kitchen）：7个可操作物体，下游任务需要按特定顺序完成4个子任务。
- **基准方法**：
  - 平坦RL：SAC、SAC+Novelty（将新颖性作为内在奖励）
  - 平坦离线预训练+微调：BC+SAC、IQL+SAC
  - 固定长度技能：SPiRL
  - 其他变长度技能方法：LOVE（基于最小描述长度）、Relative Novelty（相对新颖性，基于伪计数）
- **对比类别**：主要比较NBDI与上述方法在下游任务上的成功率或完成子任务数。

## 4. 资源与算力

- 论文在附录I.5中明确说明：
  - 每个实验使用单颗CPU（Intel Xeon Gold 6330）、256GB RAM、单颗GPU（NVIDIA RTX 3090）。
  - 每次训练约36小时（12小时先验学习 + 24小时下游RL），占用约30% RAM和25% GPU显存。
  - 所有算法使用PyTorch 1.3，Ubuntu 22.04.04 LTS。
- 这是具体的信息，可以如实总结。

## 5. 实验数量与充分性

- **实验数量**：
  - 主要结果在四个环境（两个迷宫、块堆叠、厨房）上报告，每个环境5个随机种子，给出95%置信区间。
  - 消融实验：
    - 对比不同新颖性成分（状态新颖性NBDI-χ(s) vs 条件动作新颖性NBDI-χ(a|s) vs 联合NBDI）。
    - 对比不同阈值（附录A.1：0.1, 0.3, 0.5）。
    - 对比不预训练终止分布（NBDI-NoTermDistr） vs 使用累积和（NBDI-CumulativeSum）。
    - 对比固定平均长度的SPiRL（附录A.4）。
  - 与变长度方法（LOVE、Relative Novelty）对比（图6b）。
  - 子优数据实验（表1：使用随机高斯噪声的BC策略生成质量较低的数据）。
  - 模型容量和数据集大小的影响（图8）。
  - 迁移到元强化学习（SiMPL+NBDI，图9和表2）。
- **充分性与公平性**：
  - 所有对比方法使用相同的任务无关演示和计算资源。
  - 本文还额外做了可视化（图7决策点分布、图2预测误差热力图）来支撑直觉。
  - 实验覆盖了导航、操作等不同领域，且在下游配置显著变化时仍有效，增强了结论的泛化性。
  - 局限性：仅在子优数据实验中指出性能下降（见不足），但整体实验设计较为全面客观。

## 6. 论文的主要结论与发现

- NBDI在四个环境上均显著优于所有基线，尤其是在迷宫40×40上，成功率比SPiRL提升约177.78%；在厨房中完成4个子任务（SPiRL只能完成3.0个）。
- 状态-动作新颖性联合使用比单独使用状态新颖性或条件动作新颖性效果更好（消融实验证实）。
- 终止条件的预训练（与技能嵌入联合优化）至关重要：若不预训练终止分布，性能会下降（图10b）。
- NBDI对阈值选择敏感，需要根据数据集新颖性分布设定合适阈值（约97百分位）。
- 在子优数据场景下，NBDI仍能学到一定决策点（优于SPiRL完全失败），但更强随机性会削弱检测能力（附录C）。
- 将NBDI集成到元强化学习框架SiMPL中，可显著提升样本效率和最终成功率。

## 7. 优点

- **创新性**：首次将状态-动作新颖性用于深度RL中的技能终止条件学习，并给出理论解释（终止改进定理的启发）。
- **简单实用**：仅需任务无关演示数据，无需奖励或任务标签，可直接使用ICM等通用新颖性估计器。
- **鲁棒性**：在下游环境配置发生显著变化（迷宫布局、块数、物体位置）时仍有效，优于LOVE等端到端方法。
- **充分消融**：对各新颖性成分、阈值、终止分布学习必要性、模型容量等进行了详尽分析，验证了设计选择。
- **可扩展性**：在元RL场景中也展示了良好的兼容性。

## 8. 不足与局限

- **数据质量敏感**：当演示数据由高随机性策略生成时（如随机游走），ICM无法识别有意义的决策点，导致性能下降（附录C、图16注释）。
- **阈值手工设定**：目前需要根据经验选择阈值（约97百分位），虽然提供了指南但缺乏自适应机制。
- **最大技能长度H固定**：虽然技能可提前终止，但依然设定了上限H=30，可能在某些场景下不够灵活。
- **实验环境类型有限**：主要涉及导航和机器人操作，未在更复杂或可视化的基准（如Atari、Meta-World）上验证。
- **与部分baseline比较不完全公平**：如LOVE原本针对离散动作，作者进行了适配修改，可能影响其原本性能。
- **计算成本**：预训练ICM和潜变量模型需要离线演示，且下游RL训练时间较长（36小时/种子），但相对于其他层次化方法尚可接受。

（完）
