---
title: Closed-Loop Long-Horizon Robotic Planning via Equilibrium Sequence Modeling
title_zh: 通过均衡序列建模实现闭环长时域机器人规划
authors: "Jinghan Li, Zhicheng Sun, Yadong MU"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=MCqlamfhAy"
tags: ["query:vla"]
score: 6.0
evidence: 闭环长时域机器人规划采用自优化方案
tldr: 针对语言模型在机器人规划中容易出错且无法提前计划的问题提出闭环自优化方案通过迭代优化计划直至平衡且无需额外验证器。实验证明了该方法在长时域规划任务中的有效性。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1658, \"height\": 490, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1694, \"height\": 692, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1697, \"height\": 432, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1774, \"height\": 963, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 870, \"height\": 350, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1758, \"height\": 1037, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1574, \"height\": 623, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1786, \"height\": 1944, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1784, \"height\": 1868, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 575, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 577, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 573, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 575, \"height\": 329, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mcqlamfhay/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1382, \"height\": 1253, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1767, \"height\": 620, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1767, \"height\": 585, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1766, \"height\": 309, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 859, \"height\": 297, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 859, \"height\": 296, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1766, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1760, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1764, \"height\": 415, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 904, \"height\": 190, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1784, \"height\": 1868, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 580, \"height\": 2055, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 580, \"height\": 1264, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mcqlamfhay/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 590, \"height\": 1928, \"label\": \"Table\"}]"
motivation: 语言模型代理在规划中容易出错提前计划能力有限。
method: 提出自我优化方案迭代优化草稿计划直到达到均衡以有监督方式训练。
result: 在模拟机器人规划任务中优于现有方法实现了更长的有效规划。
conclusion: 均衡序列建模为机器人规划提供了一种简便有效的闭环方案。
---

## Abstract
In the endeavor to make autonomous robots take actions, task planning is a major challenge that requires translating high-level task descriptions to long-horizon action sequences. Despite recent advances in language model agents, they remain prone to planning errors and limited in their ability to plan ahead. To address these limitations in robotic planning, we advocate a self-refining scheme that iteratively refines a draft plan until an equilibrium is reached. Remarkably, this process can be optimized end-to-end from an analytical perspective without the need to curate additional verifiers or reward models, allowing us to train self-refining planners in a simple supervised learning fashion. Meanwhile, a nested equilibrium sequence modeling procedure is devised for efficient closed-loop planning that incorporates useful feedback from the environment (or an internal world model). Our method is evaluated on the VirtualHome-Env benchmark, showing advanced performance with improved scaling w.r.t. inference-time computation. Code is available at https://github.com/anonymous-icml-2025/equilibrium-planner.

---

## 论文详细总结（自动生成）

# 中文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：大型语言模型（LLM）在机器人任务规划中虽然展现潜力，但存在固有局限：①单向依赖性导致无法提前规划（不能关注未来token）；②缺乏对已有输出的纠错能力，除非依赖繁重的系统2；③固定的前向过程难以通过增加推理计算来提升规划性能。这些缺陷阻碍了闭环长时域规划的实现。
- **核心问题**：如何让LLM规划器具备自我修正能力，同时保持训练简单（无需额外的验证器或奖励模型），并能有效融合环境反馈进行闭环规划。
- **整体含义**：本文提出一种基于均衡序列建模（Equilibrium Sequence Modeling）的自我优化方案，将规划过程视为一个固定点问题，通过迭代细化直至均衡，实现端到端的监督训练，无需强化学习或复杂的系统2。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 2.1 核心思想：自我优化作为均衡模型
- 将自我优化过程形式化为固定点问题：\( x_{t+1} = f_\theta(x_t, c) \)，其中 \( x_t \) 是规划草稿，\( c \) 是上下文（如环境反馈），最终理想规划 \( x^* \) 满足 \( x^* = f_\theta(x^*, c) \)。
- 利用深度均衡模型（Deep Equilibrium Model）框架：训练时通过隐函数定理直接计算梯度，无需反向传播通过所有优化步骤。
- 梯度简化：采用雅可比自由近似（Jacobian-free approximation），将逆雅可比项近似为单位矩阵，使得训练退化为简单的监督学习形式：
  \[
  \min_\theta L(f_\theta(x^*, c), y)
  \]
  其中 \( x^* \) 是解出的均衡点，\( y \) 是真实规划。

### 2.2 关键技术细节
- **两阶段交替训练流程**：
  1. **推理阶段**：固定点迭代求解均衡点 \( x^* \)（多次调用LLM基于上一次输出生成新规划，直至收敛）。
  2. **训练阶段**：将均衡点 \( x^* \) 与真实规划 \( y \) 配对，用标准监督损失训练，使模型学会从次优均衡点向更优规划自我优化。
- **嵌套均衡求解（Nested Equilibrium Solving）**：为了高效整合环境反馈，设计内循环和外循环：
  - **内循环**：在固定反馈 \( c_t \) 下通过固定点迭代求解均衡规划 \( x^*_t \)。
  - **外循环**：与环境交互（或调用世界模型）获取新反馈 \( c_{t+1} \)。
- **均衡解复用（Reusing Equilibrium Solution）**：将上一轮外循环的均衡解作为下一轮内循环的初始点，加速收敛。
- **经验管理记忆**：缓存所有历史均衡点和对应反馈，用于训练时采样（更频繁采样最近均衡点以减少分布偏移）。
- **世界模型（World Model）**：额外训练一个LLM，以环境上下文、任务指令和当前规划为输入，预测反馈类型，在无法与环境交互时提供内部反馈，提升效率。

### 2.3 算法流程（文字说明）
1. 初始化规划草稿 \( x_0 \) 和反馈 \( c_0 \)。
2. 对于每个外循环迭代 \( i \in [0,N] \)：
   - 执行内循环固定点迭代直至收敛，得到当前反馈下的均衡规划 \( x^*_i \)。
   - 与环境（或世界模型）交互，获得新反馈 \( c_{i+1} \)（包括当前规划的执行结果和错误信息）。
   - 复用均衡解作为下一内循环初始点。
3. 输出最终均衡规划。

## 3. 实验设计

- **基准环境**：VirtualHome-Env 模拟环境（基于VirtualHome），包含1360个长时域任务（平均动作长度10.8），提供场景图和可交互反馈。
- **数据集划分**：50%训练、50%测试，测试集分为三个子集：新场景集、新任务集、新场景和任务集。
- **评价指标**：
  - 可执行性（Exec.）：计划能否在环境中执行。
  - 成功率（SR）：目标是否完成。
  - 目标条件召回率（GCR）：目标达成比例。
  - 推理时计算量（TFLOPS）。
- **对比基线**：
  - API调用方法（GPT-3.5）：Zero-shot Planner、ProgPrompt、Iterative-Planner、Tree-Planner。
  - 基于Llama 3 8B微调的方法：监督微调（supervised）、Tree-Planner（N=25/50）、SELF-REFINE、Ours（本文）。
- **实验设置**：两个测试场景——无纠错（no correction）和最多10次纠错（with up to 10 corrections，允许基于环境反馈自我修正）。

## 4. 资源与算力

- 文中未明确说明使用的GPU型号、数量及具体算力资源。
- 提供了训练时长信息：本文方法训练比基线慢（36小时 vs 12小时），其中24小时用于均衡求解生成训练数据；推理评估耗时16小时（Tree-Planner需24小时）。
- 未提及硬件配置细节。

## 5. 实验数量与充分性

- **主要实验组**：包括无纠错场景（表1）和有纠错场景（表2）在两个子集上的对比，涵盖Exec./SR/GCR指标。
- **消融实验**：
  - 不同反馈类型（内部世界模型 vs 外部环境）的组合效果（表3）。
  - 推理计算与成功率的关系（图5a）。
  - 规划长度与成功率的关系（图5b）。
  - 均衡解复用对收敛速度的影响（图6a）。
  - 固定点收敛分析（表4）。
  - 对噪声反馈的鲁棒性测试（表5）。
  - 零样本泛化到ALFRED基准（表7）。
- **可视化**：多个自修正过程案例（图4、10-14）。
- **充分性评估**：实验覆盖了主要性能指标、多个消融维度、计算效率、鲁棒性、泛化性，对比了多种基线（包括GPT-3.5和微调Llama方法），较为充分。但仅在单一基准（VirtualHome-Env）上验证，缺乏更多真实机器人或多样性场景的评估，存在一定局限性。

## 6. 论文的主要结论与发现

1. **均衡序列建模有效**：所提方法能够以简单的监督训练实现自我优化，无需强化学习或验证器，在VirtualHome-Env上取得最优或接近最优的成功率和目标条件召回率。
2. **闭环规划能力提升**：融合环境反馈后，性能提升显著（所有指标提升11%~19%），且优于基于提示或树搜索的自我修正方法（如SELF-REFINE提升>11%，Tree-Planner提升>12%）。
3. **推理计算可扩展**：随着推理计算量增加，成功率持续提升（图5a），领先于Tree-Planner和SELF-REFINE；特别在长规划（>20步）场景中成功率超出基线两倍以上（图5b）。
4. **计算效率优势**：通过嵌套均衡求解和解复用设计，推理速度比Tree-Planner更快（16h vs 24h），且动态分配计算量（复杂任务需要更多固定点迭代）。
5. **鲁棒性与泛化性**：在10%噪声下性能稳定（表5）；零样本迁移到ALFRED基准时，任务分类准确率54%（监督微调仅11%），动作-对象召回率27.08%（0.50%）。

## 7. 优点

- **训练简化**：无需强化学习或过程监督，仅用标准监督损失即可训练自我优化模型，极具实用性。
- **灵活整合反馈**：通过嵌套均衡求解，能高效利用环境或世界模型反馈，且支持内部/外部反馈组合。
- **推理计算可缩放**：固定点迭代次数可随问题复杂度动态调整，实现更好的计算-性能权衡。
- **长时域规划能力强**：在长规划序列任务上优势明显，表明方法有效克服了LLM的规划前瞻性局限。
- **高效的工程实现**：KV cache加速、均衡解复用等设计降低推理开销。

## 8. 不足与局限

- **单一基准验证**：仅在VirtualHome-Env上评估，缺乏在其他机器人任务或真实环境中的测试，泛化性未充分证明。
- **依赖环境反馈**：无纠错场景下性能不及Tree-Planner（因为后者通过多候选采样获得优势），需结合反馈才能超越。
- **训练效率较低**：由于需要固定点迭代生成训练数据，训练总时长高于基线（36h vs 12h）。
- **世界模型准确性有限**：世界模型提供的反馈不如真实环境有效，仍有改进空间。
- **无隐式推理步骤**：目前仅考虑显式输出规划，未结合思维链等推理过程，可能限制复杂规划能力。
- **仅限文本输入**：缺乏视觉输入，无法处理真实世界多模态感知任务。
- **收敛分析未充分讨论**：虽然固定点收敛快，但理论上的收缩性条件未严格验证，实际中依赖贪婪采样降低随机性。

（完）
