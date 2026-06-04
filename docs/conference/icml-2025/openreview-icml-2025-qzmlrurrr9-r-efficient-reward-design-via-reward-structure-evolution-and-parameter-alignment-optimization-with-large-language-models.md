---
title: "R*: Efficient Reward Design via Reward Structure Evolution and Parameter Alignment Optimization with Large Language Models"
title_zh: "R*：通过奖励结构演化与参数对齐优化实现高效奖励设计"
authors: "Pengyi Li, Jianye HAO, Hongyao Tang, Yifu Yuan, Jinbin Qiao, Zibin Dong, YAN ZHENG"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=qZMLrURRr9"
tags: ["query:vla"]
score: 6.0
evidence: 基于LLM的奖励设计用于策略学习
tldr: "奖励函数对策略学习至关重要，但代码型奖励设计空间大、优化效率低。本文提出R*框架，将奖励设计分解为结构演化与参数对齐优化，利用LLM维护奖励函数种群并模块化组件。实验表明R*高效生成高质量奖励，可用于机器人的强化学习任务。"
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1761, \"height\": 984, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1745, \"height\": 670, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 814, \"height\": 633, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 832, \"height\": 418, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 828, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 828, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 760, \"height\": 337, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1699, \"height\": 1171, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1689, \"height\": 1631, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1692, \"height\": 1208, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-qzmlrurrr9/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1671, \"height\": 2083, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-qzmlrurrr9/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1770, \"height\": 129, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-qzmlrurrr9/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1346, \"height\": 188, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-qzmlrurrr9/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1675, \"height\": 1227, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-qzmlrurrr9/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1695, \"height\": 1367, \"label\": \"Table\"}]"
motivation: 代码型奖励函数设计空间大且优化效率低，需要自动化方法。
method: 将奖励设计分解为结构演化和参数对齐两部分，利用LLM维护奖励函数种群并模块化。
result: "R*在多项任务中生成有效奖励函数，提升策略学习效率。"
conclusion: "R*为自动化奖励设计提供高效方案，可支持具身智能体学习。"
---

## Abstract
Reward functions are crucial for policy learning. Large Language Models (LLMs), with strong coding capabilities and valuable domain knowledge, provide an automated solution for high-quality reward design. 
However, 
code-based reward functions require precise guiding logic and parameter configurations within a vast design space, leading to low optimization efficiency.
To address the challenges,
we propose an efficient automated reward design framework, called R*,
which decomposes reward design into two parts: reward structure evolution and parameter alignment optimization. To design high-quality reward structures, R* maintains a reward function population and modularizes the functional components. LLMs are employed as the mutation operator, and module-level crossover is proposed to facilitate efficient exploration and exploitation.
To design more efficient reward parameters, R* first leverages LLMs to generate multiple critic functions for trajectory comparison and annotation. Based on these critics, a voting mechanism is employed to collect the trajectory segments with high-confidence labels.
These labeled segments are then used to refine the reward function parameters through preference learning.
Experiments on diverse robotic control tasks demonstrate that R* outperforms strong baselines in both reward design efficiency and quality, surpassing human-designed reward functions.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题概述**：深度强化学习（DRL）在机器人控制等领域表现出色，但学习过程常因奖励信号质量低（稀疏、欺骗性）而不稳定，导致策略次优甚至崩溃。手工设计高质量奖励函数需要大量领域知识，成本高昂且难以保证有效性。
- **现有方法局限**：逆强化学习依赖专家演示；人类反馈强化学习（RLHF）需持续人类参与；利用大语言模型（LLM）直接生成代码型奖励函数虽然自动化，但面临巨大设计空间和参数配置次优的问题。已有工作Eureka结合进化算法和LLM，但存在贪婪开发（仅依赖最优个体）和参数分配次优（LLM直接设定参数）两大缺陷。
- **本文目标**：提出一种高效的LLM驱动的自动奖励设计框架**R***，将奖励设计解耦为**结构演化**和**参数对齐优化**两个子问题，提高奖励设计的效率和质量，使其能指导策略学习超越手工设计的奖励。

## 2. 方法论：核心思想与关键技术细节

### 2.1 整体框架
R* 分为两个阶段：**初始化阶段**和**进化改进阶段**（迭代进行）。
- **初始化阶段**：利用LLM根据任务描述和环境代码生成**奖励函数种群**（模块化结构）和**批评函数种群**（用于轨迹比较标注）。
- **进化改进阶段**：包括三个核心步骤：种群评估、进化（模块级交叉+LLM反思）、参数对齐优化。

### 2.2 奖励结构演化
- **模块化奖励函数**：每个奖励函数由多个模块（如距离奖励、速度奖励）组成，每个模块负责不同目标。
- **LLM作为变异算子**：通过LLM反思机制执行三种操作：模块内改进、删除模块、添加模块。
- **模块级交叉**：维护一个奖励函数存档，基于适应度（策略成功率）选择两个父代，将其中一个父代的模块插入另一个，生成新个体。交叉操作能充分利用已发现的高质量奖励函数，促进设计空间探索。
- **适应度定义**：奖励函数引导的策略的成功率作为适应度。

### 2.3 参数对齐优化
- **动机**：LLM直接设定的参数（如权重、系数）往往次优，需进一步优化。
- **自动轨迹标注**：使用批评函数种群进行逐步骤比较。批评函数为规则式代码函数，能比较两段轨迹对应状态的质量，输出标签（1、0、-1）。仅当所有指标严格优/劣时赋予非零标签，并通过种群投票（至少半数批评者一致）增强可靠性。将连续相同标签的步骤分组为片段（长度>5）加入标注缓存。
- **偏好学习**：基于Bradley-Terry模型，使用交叉熵损失优化奖励函数参数（模块内参数和模块间权重）。数据70%训练，30%验证，选择验证集准确率最高的参数。

### 2.4 伪代码流程（文字说明）
1. 输入任务描述L、环境代码C、提示词，LLM生成奖励种群（大小n）和批评种群（大小c）。
2. 每轮迭代：
   - 从存档采样两个父代，执行模块级交叉生成nc个新个体，加入种群。
   - 采样轨迹，用批评种群标注并缓存。
   - 对种群中的奖励函数进行参数对齐优化（偏好损失）。
   - 并行PPO训练评估每个奖励函数，更新存档，获得最优个体。
   - 利用LLM反思机制基于最优个体和改进提示改进种群。
3. 迭代K轮后返回最优奖励函数。

## 3. 实验设计

### 3.1 任务与场景
- **测试环境**：基于Isaac Gym和Bidextrous Manipulation (Dexterity)基准的**8个机器人操作任务**：FrankaCabinet、Shadow-Hand-Swing-Cup、Shadow-Hand-Over、Shadow-Hand-Scissors、Allegro-Hand、Shadow-Hand-Door-Open-Outward、Shadow-Hand-Kettle、Shadow-Hand-Pen。
- **覆盖范围**：涉及单臂操作、单只灵巧手操作、双手灵巧操作（如传递物体、旋转杯子等）。

### 3.2 Benchmark与对比方法
- **Eureka**：最强LLM驱动奖励设计基线，维护奖励种群并通过LLM反思改进。
- **Oracle**：人类专家手工设计的奖励函数。
- **Sparse**：稀疏奖励（仅成功时给1，其余0）。
- 所有方法均使用GPT-4o作为LLM骨干。

### 3.3 实验设置
- 种群大小：奖励函数16个（12个由LLM生成/改进，4个由交叉生成）；批评函数5个。
- 进化迭代次数：5轮。
- 并行环境数因任务而异（见表1，从128到4096不等，为保证40GB GPU内存预算而减小）。
- 超参数与Eureka一致，RL训练使用PPO，配置相同。

## 4. 资源与算力
- 论文明确说明：所有实验在**40 GB GPU内存预算**内进行（例如使用两块NVIDIA 3090或4090 GPU）。
- 为了适应内存限制，部分任务减少了并行环境实例数（增加了学习难度），具体数量见表1。
- **未说明**：总训练时长、GPU小时数、API调用次数等详细算力消耗。

## 5. 实验数量与充分性
- **主实验**：8个任务上对比R*与Eureka、Oracle、Sparse，每个任务报告5次独立运行的平均值与95%置信区间（图2）。
- **进化效率分析**：4个任务上比较每代最优策略成功率（图3）。
- **交叉贡献分析**：统计8个任务中最佳策略来源于交叉的概率（图4），并比较不同交叉个体数量（4 vs 8）的影响（图5，2个任务）。
- **消融实验**：2个任务上移除交叉（w/o Cross）和移除对齐优化（w/o Align）（图6）。
- **标注方法精度比较**：2个任务上对比Ours、LLM、VLM三种标注方法的准确率（图7）。
- **额外实验**：在原始大环境设置下（与原Eureka一致）对比6个任务的成功率（表2）。
- **充分性评价**：实验覆盖了多种任务类型，进行了消融、组件分析、标注精度验证和跨设置对比。消融实验较少（仅2个任务），但主实验8个任务已能说明整体效果。实验设计公平（与Eureka共享超参数和LLM），结果客观。

## 6. 主要结论与发现
1. **性能优势**：R*在所有8个任务上的奖励函数引导的策略成功率显著优于Eureka，且学习更稳定（Eureka在某些任务出现策略崩溃）。在多数任务上R*超越了人类专家设计的奖励（Oracle）。
2. **进化效率**：R*在更少的进化代数内达到更高成功率，表明结构演化与参数优化的联合设计加速了高质量奖励的发现。
3. **模块级交叉有效**：尽管交叉生成的个体仅占种群1/4，但最佳策略来源于交叉的概率超过50%（大多数任务），证明交叉能高效利用已有高质量奖励函数。
4. **参数对齐优化必要**：移除对齐优化后性能显著下降，表明LLM直接参数设定次优，偏好学习有效改善了参数配置。
5. **标注方法可靠**：基于批评种群的投票标注达到100%准确率，优于直接使用LLM或VLM，能提供高质量训练数据。

## 7. 优点
- **创新分解**：将奖励设计解耦为结构搜索与参数精调，分别利用LLM的生成能力和偏好学习的优化能力，解决了两大瓶颈（盲目搜索和参数不匹配）。
- **模块级交叉**：简单有效的结构探索机制，无需额外LLM调用，充分利用存档中的高质量候选。
- **批评种群与投票机制**：提供自动、高置信度的轨迹标注，克服了LLM幻觉和VLM能力不足的问题。
- **全面实验**：在8个多样化人型机器人操作任务上验证，并对比了强基线和人类专家设计，消融实验和组件分析支撑了方法的有效性。
- **效率与性能平衡**：通过减少并行环境数，在有限GPU内存下仍取得超越基线结果。

## 8. 不足与局限
- **实验覆盖有限**：仅在仿真环境中的机器人操作任务上测试，未涉及真实机器人、视觉观测任务或非接触式场景。论文承认当前方法依赖低层信息（状态变量），对仅提供图像的任务不适用。
- **缺少泛化性分析**：未讨论在更复杂任务（如长时序、高维观察）或不同RL算法下的表现。
- **算力报告不充分**：未详细说明总训练时间、API调用次数等，不利于复现和资源估计。
- **交叉个体数量敏感**：增加交叉个体（从4到8）反而导致性能下降，表明需要平衡LLM探索与交叉利用，文中未深入分析最优比例。
- **批评函数依赖手工提示**：批评函数由LLM生成但需特定格式提示（见附录），可能在不同任务中需要调整，泛化性存疑。
- **潜在偏差**：标注质量依赖于批评种群的质量，若批评函数存在系统性偏差（如过于强调距离指标），可能引入偏好偏差。
- **应用限制**：对于无法提取关键低层信息的任务（如纯视觉控制），需要额外检测模型提取特征，增加了系统复杂度。

（完）
