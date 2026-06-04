---
title: "Tru-POMDP: Task Planning Under Uncertainty via Tree of Hypotheses and Open-Ended POMDPs"
title_zh: Tru-POMDP：基于假设树和开放式POMDP的不确定性任务规划
authors: "Wenjing Tang, Xinyu He, Yongxi Huang, Yunxiao Xiao, Cewu Lu, Panpan Cai"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=1GIQOV3NAj"
tags: ["query:vla"]
score: 5.0
evidence: Tru-POMDP结合LLM与POMDP进行机器人任务规划
tldr: 家庭服务机器人面临模糊指令和未知物体位置等开放不确定性。Tru-POMDP通过层次化假设树利用LLM生成高质量粒子信念，并建立开放世界POMDP模型。在多个真实家庭场景的实验中，该方法有效应对了开放式不确定性，实现了鲁棒的长时间任务规划。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1456, \"height\": 794, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1438, \"height\": 431, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 526, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1438, \"height\": 434, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 529, \"height\": 397, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1368, \"height\": 862, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1giqov3naj/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1426, \"height\": 842, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-1giqov3naj/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1454, \"height\": 500, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1giqov3naj/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1453, \"height\": 679, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1giqov3naj/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1455, \"height\": 572, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1giqov3naj/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1455, \"height\": 607, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1giqov3naj/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1455, \"height\": 749, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1giqov3naj/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1453, \"height\": 414, \"label\": \"Table\"}]"
motivation: 家庭机器人面临开放的不确定性，传统规划器难以处理。
method: 提出Tru-POMDP，结合LLM层次化假设树生成信念，用POMDP进行推理。
result: 在模拟和真实家庭任务中，Tru-POMDP显著提升规划鲁棒性和效率。
conclusion: LLM与POMDP的结合为开放式机器人规划提供了有效方案。
---

## Abstract
Task planning under uncertainty is essential for home-service robots operating in the real world. Tasks involve ambiguous human instructions, hidden or unknown object locations, and open-vocabulary object types, leading to significant open-ended uncertainty and a boundlessly large planning space. To address these challenges, we propose Tru-POMDP, a planner that combines structured belief generation using Large Language Models (LLMs) with principled POMDP planning. Tru-POMDP introduces a hierarchical Tree of Hypotheses (TOH), which systematically queries an LLM to construct high-quality particle beliefs over possible world states and human goals. We further formulate an open-ended POMDP model that enables rigorous Bayesian belief tracking and efficient belief-space planning over these LLM-generated hypotheses. Experiments on complex object rearrangement tasks across diverse kitchen environments show that Tru-POMDP significantly outperforms state-of-the-art LLM-based and LLM-tree-search hybrid planners, achieving higher success rates with significantly better plans, stronger robustness to ambiguity and occlusion, and greater planning efficiency.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义

家庭服务机器人在真实场景中执行任务（如准备派对、整理厨房）时，面临**开放世界中的不确定性**：

- **人类指令模糊**：例如“准备好厨房”未指定具体物品和位置。
- **物体位置隐藏**：许多物品在柜子、抽屉等封闭区域，无法直接观察。
- **物体类型开放**：任务可能涉及未预先定义的任意物体，状态空间和动作空间无法提前固定。

传统POMDP规划需要预定义所有状态、动作和观测，无法处理这种开放性。因此，论文提出**Tru-POMDP**，将大语言模型（LLM）的常识推理与原则性POMDP规划相结合，首次在**开放式POMDP**框架下解决这类任务。

## 2. 方法论

### 核心思想
利用LLM生成**层次化假设树（Tree of Hypotheses, TOH）**，构建对世界状态和人类目标的**显式粒子信念**；然后通过**混合信念更新（Hybrid Belief Update）** 维持信念一致性；最后使用**在线信念树搜索**（基于DESPOT）进行最优动作规划。

### 关键技术细节
1. **Tree of Hypotheses (TOH)**
   - **Level 1**：LLM推断可能的目标物体组合（C1个），每个带置信度。
   - **Level 2**：对每个物体组合推断其目标放置区域（形成完整放置目标）。
   - **Level 3**：对每个尚未可见的目标物体，推断其可能初始位置（C2个候选区域）。
   - 每条从根到叶的路径构成一个粒子，权重为各步置信度乘积的归一化值，形成初始信念 \( b_{LLM} \)。

2. **Hybrid Belief Update**
   - 每步执行**贝叶斯滤波**：预测（按确定性转移模型推进场景图）→ 剔除（与观测不一致的粒子）。
   - 若剩余总权重低于阈值 \( 1-\epsilon \)（如0.7），则调用LLM重新生成新信念，与滤波后信念加权合并：\( b_t' = b_{BF} + (1 - w_{BF}) \cdot b_{LLM} \)。
   - 目的：重用可靠信息，减少LLM调用频率。

3. **Online POMDP Planning**
   - **动态动作空间**：从当前信念的粒子中提取相关实体（目标物体、开放式区域、封闭容器），组装成紧凑有效动作集。
   - **信念树搜索**：基于DESPOT，递归模拟未来动作-观测序列，并用Bellman原理更新节点价值。
   - **LLM生成Rollout策略**：预先生成一个C++函数（由LLM编写），在搜索叶子节点时作为默认策略估计累积奖励，避免频繁LLM调用。

## 3. 实验设计

### 数据集/场景
- 使用**RoboCasa**中的5种厨房环境：One Wall、One Wall with Island、L-Shaped、L-Shaped with Island、Galley。
- 每个场景包含最多40个区域（其中29个初始封闭），有语义丰富的名称。
- 任务由LLM辅助生成，分三个难度级别：Easy（2个目标物体）、Medium（3个）、Hard（4~8个）。每个级别100个任务，共300个任务。

### 对比方法
- **ReAct**：纯LLM闭环规划。
- **Reflexion**：ReAct+反思模块。
- **ReAct*** / **Reflexion***：上述方法的增强版，增加结构化任务描述。
- **LLM-MCTS**：LLM结合蒙特卡洛树搜索的POMDP规划（已知物体集，闭合领域）。

### 评估指标
- 累计奖励（基于POMDP奖励函数，最终完成得1000分）
- 成功率（在步数和时间限制内完成）
- 步数（失败时计为最大允许步数）
- 规划时间（总耗时代价）
- LLM token使用量

## 4. 资源与算力

- **硬件**：本地机器，12th Gen Intel Core i7-12700KF CPU（20线程），**无GPU加速**。
- **LLM**：所有方法一致使用GPT-4.1 API调用。
- **未提及**：无模型训练，只有推理；未提供GPU型号、训练时长等信息（因为本文不涉及训练）。

## 5. 实验数量与充分性

- **综合对比**：在300个任务上（每个难度100个）对5种基线进行对比，报告均值与标准误差。
- **消融实验**：设计6个变体：
  - w/o Belief（仅用最可能假设）
  - w/o HBU（每步重新生成整信念，无贝叶斯滤波）
  - w/o TOH（单次flat信念生成）
  - w/o LRP（随机rollout策略）
  - w/o BTS（直接LLM输出动作）
- 每个变体也在不同难度上评估，提供误差线。
- **充分性**：实验覆盖不同难度、不同组件，统计显著，可复现。对照组设计合理，不公平：所有方法共享相同LLM和相同任务集，运行条件一致。

## 6. 主要结论与发现

1. **信念空间规划至关重要**：Tru-POMDP显著优于纯LLM规划器（ReAct/Reflexion），在中等/困难任务上成功率提升数倍。
2. **混合信念更新提升效率**：相比无HBU变体，规划时间降低约3倍，成功率提高。
3. **层次化假设树优于扁平生成**：无TOH变体性能下降甚至低于单假设，说明结构化查询减少幻觉。
4. **LLM生成的rollout策略有效引导搜索**：无LRP变体性能大幅下降。
5. **整体框架高效**：Tru-POMDP以最低的LLM token消耗实现最高成功率。
6. 开放世界POMDP模型搭配动态动作空间是解决开放式不确定性可行范式。

## 7. 优点

- **创新性**：首次将POMDP与LLM结构化推理结合，提出开放式POMDP框架，填补了传统POMDP无法处理未知状态空间的空白。
- **方法论完备**：三层假设树生成多元化信念，贝叶斯滤波与LLM生成互补，动态动作空间实用，rollout策略预编译降低在线开销。
- **实验充分**：任务生成、环境多样性、基线选择、消融设计均严密，报告误差线。
- **可解释性**：显式信念表示和树搜索过程可追溯，有利于调试和验证。
- **实用性**：算法在无GPU的CPU上运行即可，且LLM token消耗低，便于实际部署。

## 8. 不足与局限

- **计算开销**：TOH每次调用LLM多次（尤其Level 3并行），存在延迟，可通过微调本地模型缓解。
- **独立性假设**：文中假设不同物体的放置位置条件独立，当存在更复杂依赖关系（如多个物体必须放在同一区域）时，需要系统化的信念分解。
- **理想化感知**：当前假设无噪声感知和确定性动作；虽然框架在理论上可扩展，但实验未验证噪声情况。
- **任务范围有限**：仅评估物体重排任务，未扩展至更复杂动作（如操作电器）、更多属性推理（如物体颜色、状态）。
- **实验场景**：仅使用模拟环境RoboCasa，未在真实机器人上部署，可能存在Sim-to-Real差距。
- **未讨论负社会影响**：虽然对机器人规划研究进展有益，但未探讨可能的误用或隐私问题。

（完）
