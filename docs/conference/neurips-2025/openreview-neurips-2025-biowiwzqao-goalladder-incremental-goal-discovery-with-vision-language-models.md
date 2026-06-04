---
title: "GoalLadder: Incremental Goal Discovery with Vision-Language Models"
title_zh: "GoalLadder: 使用视觉语言模型进行增量式目标发现"
authors: "Alexey Zakharov, Shimon Whiteson"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=BiowiwzQaO"
tags: ["query:vla"]
score: 7.0
evidence: VLM与RL动作空间的集成
tldr: 在视觉环境中从语言指令学习奖励函数是一大挑战。GoalLadder方法利用预训练视觉语言模型，逐步发现并分解子目标，从而为强化学习提供逐步的奖励信号。实验证明，该方法只需单条语言指令即可在复杂视觉任务中高效训练机器人策略，提升了学习的可解释性和效率。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-biowiwzqao/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 686, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-biowiwzqao/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1409, \"height\": 520, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-biowiwzqao/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 576, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-biowiwzqao/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1443, \"height\": 1080, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-biowiwzqao/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1452, \"height\": 486, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1464, \"height\": 748, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1444, \"height\": 413, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1442, \"height\": 375, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 570, \"height\": 184, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1452, \"height\": 295, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 712, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-biowiwzqao/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1216, \"height\": 298, \"label\": \"Table\"}]"
motivation: 从语言指令提取奖励在视觉环境中存在困难。
method: 使用VLM逐步发现子目标，生成奖励函数。
result: 在视觉任务中从单条指令高效学习。
conclusion: 提供了可解释的逐步奖励机制。
---

## Abstract
Natural language can offer a concise and human-interpretable means of specifying reinforcement learning (RL) tasks. The ability to extract rewards from a language instruction can enable the development of robotic systems that can learn from human guidance; however, it remains a challenging problem, especially in visual environments. Existing approaches that employ large, pretrained language models either rely on non‑visual environment representations, require prohibitively large amounts of feedback, or generate noisy, ill‑shaped reward functions. In this paper, we propose a novel method, GoalLadder, that leverages vision-language models (VLMs) to train RL agents from a single language instruction in visual environments. GoalLadder works by incrementally discovering states that bring the agent closer to completing a task specified in natural language. To do so, it queries a VLM to identify states that represent an improvement in agent's task progress and to rank them using pairwise comparisons. Unlike prior work, GoalLadder does not trust VLM's feedback completely; instead, it uses it to rank potential goal states using an ELO-based rating system, thus reducing the detrimental effects of noisy VLM feedback. Over the course of training, the agent is tasked with minimising the distance to the top-ranked goal in a learned embedding space, which is trained on unlabelled visual data. This key feature allows us to bypass the need for abundant and accurate feedback typically required to train a well-shaped reward function. We demonstrate that GoalLadder outperforms existing related methods on classic control and robotic manipulation environments with the average final success rate of $\sim$95\% compared to only $\sim$45\% of the best competitor.

---

## 论文详细总结（自动生成）

# 论文总结：GoalLadder: Incremental Goal Discovery with Vision-Language Models

## 1. 核心问题与整体含义（研究动机与背景）

- **研究动机**：强化学习（RL）依赖精心设计的奖励函数，但手工设计成本高、需要领域知识。自然语言提供了一种简洁、人类可解释的任务描述方式。如何从单条语言指令中自动提取有效的奖励函数，尤其是在视觉环境中（如机器人操纵），是一个关键挑战。
- **现有方法的不足**：
  - **基于嵌入的方法**（如使用CLIP）因训练数据与测试环境不匹配，导致奖励函数噪声大。
  - **基于偏好的方法**（如RL-VLM-F）虽能生成更相关奖励，但VLM的比较错误会产生噪声标签，且需要大量查询才能训练出泛化能力强的奖励函数。
- **核心问题**：如何在利用VLM强大理解能力的同时，克服其反馈噪声和查询效率低下的问题，从而在视觉环境中仅凭一条语言指令训练RL智能体。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：GoalLadder 不使用VLM直接定义奖励或训练偏好模型，而是利用VLM**增量式发现**并**排序**视觉状态，将其中评价最高的状态作为“子目标”；智能体通过最小化在**无监督学习嵌入空间**中与该目标的距离来获得奖励。VLM的噪声通过**ELO评级系统**逐步吸收，而非全盘信任单次比较结果。
- **关键技术细节**：
  1. **候选目标发现**：在每个训练周期中，从最新轨迹中采样状态图像，通过VLM与当前最高评级目标比较，若被判定更接近任务目标（由语言指令定义），则将其加入候选目标缓冲区。
  2. **ELO评级系统**：对缓冲区中的候选目标两两比较，使用ELO公式更新评分：
     - 期望得分：\( E_i = 1 / (1 + 10^{(e_j - e_i)/C}) \)，其中 \(C=400\)（控制敏感度）。
     - 评级更新：\( e_i \leftarrow e_i + T (S_i - E_i) \)，其中 \(T=32\)（更新速度），\(S_i \in \{-1,0,1\}\) 表示输、平、赢。
     - 新加入的候选目标初始评级为当前缓冲区的平均评级。
  3. **奖励函数定义**：
     - 使用变分自编码器（VAE）在无标签的智能体观测数据上训练一个视觉编码器 \(\psi\)，将图像映射到低维潜在空间（维度16）。
     - 奖励 \(R(s_{t-1}, a_{t-1}) = - \| \psi(o_t) - \psi(o^*) \|_2\)，其中 \(o^*\) 为当前最高评级目标图像。
     - 奖励经 min-max 归一化到 \([0,1]\) 并施加非线性变换（指数γ=20），以稳定训练。
  4. **周期性更新**：每 \(L=5000\) 环境步更新最高目标并重标签经验回放缓冲区的所有奖励（应对奖励非平稳性）。
- **算法流程（伪代码）**：
  1. 初始化候选目标缓冲区 \(B_g\)（包含随机观测）。
  2. 智能体执行当前SAC策略，收集轨迹并存入经验回放缓冲区 \(D\)。
  3. 每 \(K\) 步（对Gym环境2000步，对Metaworld 500步）执行：
     - 从最新轨迹采样 \(M=5\) 个观测，每个与当前最高评级目标用VLM比较，若优于则加入 \(B_g\)。
     - 从 \(B_g\) 中采样 \(M\) 对候选目标，用VLM两两比较并更新ELO评级。
     - 移除最低评级的候选目标，保持缓冲区大小 \(\leq 10\)。
  4. 每 \(L=5000\) 步：选择最高评级目标 \(g^*\)，更新所有经验回放的奖励（基于VAE嵌入距离）。
  5. 每步：更新SAC策略和VAE（从 \(D\) 中采样小批量）。

## 3. 实验设计

- **任务场景**：共7个连续控制环境。
  - 经典控制：OpenAI Gym 的 CartPole、MountainCar。
  - 机器人操纵：Metaworld 的 Drawer Close、Drawer Open、Sweep Into、Window Open、Button Press。
  - 不使用任何特殊环境修改（如去除机器人图像）。
- **基准方法（Baselines）**：
  - **Oracle**：使用环境真实奖励，作为性能上限。
  - **VLM-RM**：使用CLIP嵌入计算图像与文本相似度作为奖励。
  - **RoboCLIP**：使用预训练视频-语言模型S3D，基于文本描述计算视频轨迹的相似度。
  - **RL-VLM-F**：使用VLM提供偏好标签训练奖励函数（同原论文设置，使用相同VLM骨干）。
- **评价指标**：最终成功率（多个种子的均值±标准差）。

## 4. 资源与算力

- **硬件**：
  - GPU：1× Tesla V100 16GB。
  - CPU：2× Intel Xeon E5-2698 v4（共40核80线程）。
- **训练时间**：单个GoalLadder智能体训练约 **45小时**。
- **其他**：VLM使用 Gemini 2.0 Flash API（需网络访问，费用未报告）。

## 5. 实验数量与充分性

- **主要实验**：
  - 在7个环境各运行3个随机种子（图中阴影表示标准差）。
  - 每个环境训练步数：OpenAI Gym环境约10万步，Metaworld约100万步。
- **消融实验**：
  - **ELO评级系统消融**（Table 5）：对比有/无ELO（贪婪替换目标）在Drawer Open任务上，有ELO成功率0.97±0.11，无ELO仅0.20±0.35，证明ELO至关重要。
  - **缓冲区大小消融**（Table 6）：测试大小1,5,25,50,10000，确认过大或过小都不好，10为默认。
  - **视觉编码器消融**（Table 7）：对比VAE、DINOv2、CLIP，VAE最好（最大成功率1.00），DINOv2 0.25，CLIP 0.38。
- **可视化分析**：
  - 展示目标缓冲区中图像随时间演进（Figure 2、5）。
  - 展示ELO评级变化曲线（Figure 3）。
- **充分性评价**：实验覆盖了从简单到复杂的不同任务，进行了充分消融和可视化分析，对比方法设置公平（相同反馈频率、相同VLM骨干）。结果置信区间合理。

## 6. 主要结论与发现

- **性能**：GoalLadder在所有7个任务上平均最终成功率达 **~95%**，最佳竞争者RL-VLM-F仅 **~45%**。甚至在Drawer Open任务上超越了Oracle（Oracle可能因奖励设计不当而未能学会拉开手柄）。
- **鲁棒性**：ELO评级系统有效抑制了VLM噪声，使最佳候选目标稳定升至顶部。
- **查询效率**：相比RL-VLM-F（需学习奖励函数），GoalLadder仅需约4500次VLM查询（Metaworld平均），而PEBBLE（使用真值偏好）需约15000个标签。
- **泛化能力**：基于无监督VAE嵌入的奖励定义，无需为每个新状态查询VLM，自然泛化到未见过的观测。

## 7. 优点

- **创新性**：将VLM用于增量目标发现而非直接定义奖励或训练偏好模型，结合ELO评级系统处理噪声，是新颖有效的方法。
- **实用性**：仅需一条语言指令，无需手工设计奖励、无需大量人类反馈、无需环境代码或状态表示，具有很强的通用性。
- **鲁棒性**：对VLM的误判有天然抵抗力，评级系统逐步纠正错误。
- **效率**：VLM查询次数显著少于现有偏好学习方法，且奖励通过嵌入空间泛化，无需为每个状态查询。
- **实验严谨**：进行了多项消融，证明ELO、缓冲区大小、视觉编码器选择的合理性，并展示了目标发现的动态可视化。

## 8. 不足与局限

- **任务假设**：假设任务目标可以通过单帧图像识别（静态目标），不适用于需要时间动态或连续动作的任务（如“推动物体到目标”可能需要多帧）。
- **视觉相似性限制**：奖励基于视觉嵌入的欧氏距离，可能无法反映真正的状态相似性或任务进度（例如外观相似但语义不同的状态）。
- **VLM成本**：虽然查询次数少，但每次查询使用大型闭源模型（Gemini 2.0 Flash）仍有经济成本和延迟，未在论文中详细分析。
- **环境范围**：仅测试了7个模拟环境，未在真实机器人或更复杂场景（如多物体交互、部分可观测）中验证。
- **可扩展性**：候选缓冲区大小固定为10，虽然经消融确认合理，但任务复杂度上升时可能需要更大缓冲区或更复杂的评级机制。
- **未与最新方法对比**：如使用LLM生成奖励函数的方法（Eureka等）未被直接比较，但作者指出这些方法需要环境代码或可解释状态表示。

（完）
