---
title: Scaffolding Dexterous Manipulation with Vision-Language Models
title_zh: 使用视觉语言模型辅助灵巧操作
authors: "Vincent de Bakker, Joey Hejna, Tyler Ga Wei Lum, Onur Celik, Aleksandar Taranovic, Denis Blessing, Gerhard Neumann, Jeannette Bohg, Dorsa Sadigh"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=PdRf0O7baQ"
tags: ["query:vla"]
score: 8.0
evidence: VLM辅助灵巧操作
tldr: 灵巧手操作面临演示数据稀缺和奖励设计繁琐的问题。本文提出利用视觉语言模型自动生成参考轨迹，为强化学习探索提供先验引导。该方法在多个灵巧操作基准上显著提升样本效率和任务成功率，展示了VLM在复杂操作学习中的巨大潜力。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1233, \"height\": 357, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1341, \"height\": 634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 501, \"height\": 829, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1456, \"height\": 242, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1330, \"height\": 229, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 725, \"height\": 311, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1449, \"height\": 228, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 654, \"height\": 616, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1456, \"height\": 247, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1437, \"height\": 239, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pdrf0o7baq/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 886, \"height\": 251, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-pdrf0o7baq/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 877, \"height\": 1009, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pdrf0o7baq/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 877, \"height\": 929, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pdrf0o7baq/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 767, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pdrf0o7baq/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1078, \"height\": 512, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pdrf0o7baq/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 474, \"height\": 410, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pdrf0o7baq/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1458, \"height\": 224, \"label\": \"Table\"}]"
motivation: 灵巧手操作数据稀缺，奖励设计困难。
method: 利用VLM生成参考轨迹引导RL探索。
result: 在多个灵巧操作任务上样本效率显著提升。
conclusion: VLM可作为操作学习的高效辅助。
---

## Abstract
Dexterous robotic hands are essential for performing complex manipulation tasks, yet remain difficult to train due to the challenges of demonstration collection and high-dimensional control. While reinforcement learning (RL) can alleviate the data bottleneck by generating experience in simulation, it typically relies on carefully designed, task-specific reward functions, which hinder scalability and generalization. Thus, contemporary works in dexterous manipulation have often bootstrapped from reference trajectories. These trajectories specify target hand poses that guide the exploration of RL policies and object poses that enable dense, task-agnostic rewards.
However, sourcing suitable trajectories---particularly for dexterous hands---remains a significant challenge. Yet, the precise details in explicit reference trajectories are often unnecessary, as RL ultimately refines the motion. Our key insight is that modern vision-language models (VLMs) already encode the commonsense spatial and semantic knowledge needed to specify tasks and guide exploration effectively. Given a task description (e.g., “open the cabinet”) and a visual scene, our method uses an off-the-shelf VLM to first identify task-relevant keypoints (e.g., handles, buttons) and then synthesize 3D trajectories for hand motion and object motion. Subsequently, we train a low-level residual RL policy in simulation to track these coarse trajectories or ``scaffolds'' with high fidelity. Across a number of simulated tasks involving articulated objects and semantic understanding, we demonstrate that our method is able to learn robust dexterous manipulation policies. Moreover, we showcase that our method transfers to real-world robotic hands without any human demonstrations or handcrafted rewards.

---

## 论文详细总结（自动生成）

以下是基于论文《Scaffolding Dexterous Manipulation with Vision-Language Models》的详细中文总结。

---

## 1. 核心问题与整体含义（研究动机和背景）

- **研究背景**：灵巧手（dexterous robotic hands）对于复杂操作任务至关重要，但其训练面临两大瓶颈：
  - **演示数据稀缺**：真实环境下采集高精度灵巧手演示数据困难且成本高昂。
  - **奖励设计复杂**：强化学习虽可在仿真中大规模生成经验，但通常需要精心设计任务特定的奖励函数，难以泛化。
- **现有方法局限**：
  - 模仿学习依赖大量高质量演示，数据瓶颈明显。
  - 基于强化学习的仿真训练需要手工奖励函数，且无引导时探索效率低。
  - 基于参考轨迹（如人类演示）的方法需要大量预存轨迹，且泛化能力有限。
- **核心动机**：作者认为，现代视觉语言模型（VLM）已经具备足够的常识性空间和语义知识，可以自动生成粗粒度的运动计划（称为“脚手架”），从而替代人工演示和奖励设计，引导强化学习策略的探索。

---

## 2. 方法论文：核心思想、关键技术细节

### 2.1 核心思想
利用 VLM 生成关于手部与物体的 3D 关键点轨迹（“脚手架”），然后通过低层残差强化学习（residual RL）在仿真中精确跟踪这些轨迹。高层规划由 VLM 完成，低层控制由 RL 策略完成，无需任何人类演示或手工奖励。

### 2.2 技术细节

#### （1）高层策略 \(\pi_h\)：VLM 生成轨迹
- **输入**：自然语言指令 \(L\) 和当前场景图像 \(I_1\)。
- **三阶段生成**：
  1. **语义关键点检测**：VLM 识别任务相关的 2D 关键点（如手柄、按钮），并利用深度图像投影到 3D 世界坐标。
  2. **轨迹生成**：VLM 基于初始 3D 关键点和手腕位姿，生成 \(n\) 个关键点序列和手腕轨迹 \(w\)（共 \(k+1\) 条轨迹）。
  3. **插值**：将 \(n\) 个粗略路点线性插值为长度为 \(T\) 的序列，形成完整计划 \(\tau\)。
- **可选 Few-shot 改进**：通过在上下文中提供之前成功的计划，进一步提高 VLM 生成质量。

#### （2）低层策略 \(\pi_l\)：残差强化学习
- **状态空间**：包括机器人本体感知（手腕位姿、手指关节位置与速度）以及当前和未来计划的关键点位置。
- **残差动作空间**：策略输出 \(\Delta w\)（手腕位姿残差）和手指目标位置 \(q_{targ}\)。最终动作 \(a_t = (\tilde{w}_t + \Delta w, q_{targ})\)。
- **奖励函数**（简单且任务无关）：
  \[
  r_t = \exp(-\beta \sum_i \|\hat{x}_t^{(i)} - \tilde{x}_t^{(i)}\|_2) + \exp(-1/(N_{contact} + \epsilon))
  \]
  - 第一项：鼓励跟踪关键点轨迹。
  - 第二项：鼓励手指与物体保持接触，促进稳定抓取。
- **结束条件**：关键点跟踪误差超过阈值 \(\delta\) 时提前终止，并采用课程学习（阈值从 \(\delta_{init}\) 线性减半）。
- **算法**：使用 PPO（Proximal Policy Optimization）训练，在大量并行的仿真环境中进行。

#### （3）全流程
- **训练**：从 VLM 采样多个计划，在不同的初始条件下训练低层策略，使其能够适应多样的计划。
- **测试**：给定新场景和指令，VLM 生成计划，冻结的低层策略闭环执行。

---

## 3. 实验设计

### 3.1 任务套件与 Benchmark
- 使用 **ManiSkill3** 仿真器和 **Allegro Hand** 模型。
- 设计了 **8 个任务**，分为四类：
  - 语义理解：Move Apple, Move Bottle
  - 非结构化运动：Hammer, Wipe with Sponge
  - 铰接物体操作：Open Drawer, Open Fridge
  - 精细操作：Close Scissors, Close Pliers
- 每个任务用自然语言指令指定（无奖励函数），需手动设计。

### 3.2 对比方法
- **Iterative Keypoint Rewards (IKER)**：用 VLM 生成代码指定奖励参数，同关键点设置。
- **Pre-recorded Trajectories**：使用训练集中预录轨迹在测试时重用。
- **Oracle Keypoints and Trajectories**：手动设定完美关键点和轨迹，作为上界。
- **Reduced Waypoints**：限制 VLM 生成较少路点（如 3 个）。
- **Additional Baselines**（附录）：
  - **RL (Simple Reward)**：无轨迹引导，仅用稀疏成功奖励和简单的关键点距离奖励。
  - **RL (Complex Reward)**：手工设计细致的奖励函数（距离、接触、成功信号等）。
  - **Diffusion Policy**（行为克隆）：使用 10/20/50 个完美演示训练。

### 3.3 评估方式
- 每个任务定义二值成功指标。
- 每个策略在 **100 个新颖初始条件**下测试，每个条件 **20 次**，总计 **2000 次评估**，取 3 个随机种子平均。

---

## 4. 资源与算力

- **仿真训练**在 **NVIDIA GPU**（A5000 到 L40）上进行，每任务训练时间 **1.5~6 小时**。
- **真实世界推理**使用 **2 块 RTX 4090 GPU**。
- 未提供总计算量估计，但提及使用 **2048 个并行环境**（PPO 训练），硬件资源中等。

---

## 5. 实验数量与充分性

- **仿真实验**：覆盖 8 个不同任务，每个任务 2000 次评估 × 3 种子，统计误差线。
- **消融实验**（见附录）：
  - 使用不同数量路点（3,5,10,20,40）
  - 替换 VLM 关键点或轨迹为 oracle
  - 添加高斯噪声到 VLM 输出
  - 开放 VLM 对比（Molmo vs Gemini）
  - 对比更多 RL/IL 基线（附录）
- **真实世界实验**：3 个任务，每个 20 次 rollout。
- **充分性**：实验设计较为全面，包括性能对比、失败分析、迭代改进、鲁棒性测试等。但主要依赖于仿真，真实世界任务数量有限（仅 3 个）。

---

## 6. 主要结论与发现

- **VLM 脚手架有效**：零样本 VLM 计划即可在 8 个任务上平均 72% 成功率，接近 Oracle（98%）。
- **Few-shot 迭代改进**：提供成功轨迹的上下文示例可显著提升性能（尤其开门任务，从 12%→64%）。
- **关键失败模式**：最主要失败来自低层策略不完全跟踪（26%），其次是关键点检测错误（5%）。
- **路点数量影响**：10 个路点即可饱和多数任务，但一些动态任务（如敲击）需要更多路点。
- **真实世界迁移可行**：三个任务成功率分别为：放置瓶子 90%、推盒子 85%、敲击三次 65%。

---

## 7. 优点

- **免手工奖励/演示**：完全依赖 VLM 的常识知识生成粗轨迹，自动提供密集奖励信号。
- **模块化设计**：高层 VLM 规划 + 低层 RL 跟踪，可独立优化。
- **较强的泛化能力**：在仿真中可以泛化到新初始条件；真实世界能零样本部署。
- **简单有效的奖励函数**：基于关键点误差和接触项，适用于多种任务。
- **系统性的消融与失败分析**：对各个组件和失败原因进行深入剖析，提供改进方向。
- **开放代码和视频网站**：促进可重复性。

---

## 8. 不足与局限

- **仅支持刚体**：方法假设刚体交互，无法处理可变形物体。
- **无法准确表示姿态**：对于小物体，难以从少量关键点推断完整 6D 姿态。
- **VLM 推理延迟**：当前推理需 1-2 分钟，无法满足实时响应。
- **闭环不足**：高层规划不与低层执行反馈耦合，遇到意外难以调整。
- **泛化局限**：对新任务类别或物体类别泛化能力有限，依赖 VLM 预训练知识。
- **Sim-to-real 仍具挑战**：真实世界任务仅三个，且敲击任务成功率偏低（65%），可能受限于仿真与真实之间动力学差异及感知噪声。
- **实验偏差风险**：VLM 使用 Gemini 2.5 Flash Thinking（收费模型），未充分评估开源模型替代性（仅测试 Molmo 并显示其在轨迹生成上失效）。可能限制了可重复性和公平性。

---

（完）
