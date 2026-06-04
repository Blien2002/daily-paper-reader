---
title: Action-Constrained Imitation Learning
title_zh: 动作约束下的模仿学习
authors: "Chia-Han Yeh, Tse-Sheng Nan, Risto Vuorio, Wei Hung, Hung Yen Wu, Shao-Hua Sun, Ping-Chun Hsieh"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=NYi9B34E1e"
tags: ["query:vla"]
score: 6.0
evidence: 面向机器人控制的带约束模仿学习
tldr: 在实际机器人控制中，动作约束常常导致模仿学习中的专家与学习者的状态分布不匹配。本文提出动作约束模仿学习（ACIL）问题，并设计DTWIL方法，通过轨迹对齐将专家示范转换成符合约束的替代数据集。该方法在多种机器人控制仿真任务中验证了有效性，为安全政策学习提供了新思路。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1679, \"height\": 430, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 855, \"height\": 586, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 792, \"height\": 401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 853, \"height\": 224, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 840, \"height\": 462, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1671, \"height\": 985, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-nyi9b34e1e/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1028, \"height\": 534, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 716, \"height\": 542, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1727, \"height\": 698, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 651, \"height\": 242, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 668, \"height\": 243, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1304, \"height\": 167, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 821, \"height\": 330, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 675, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 652, \"height\": 169, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1418, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 901, \"height\": 206, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1345, \"height\": 329, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-nyi9b34e1e/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 726, \"height\": 204, \"label\": \"Table\"}]"
motivation: 机器人常面临动作约束，导致模仿学习中学员与专家状态分布不匹配，影响策略性能。
method: 提出DTWIL，通过轨迹对齐将专家示范转化为符合动作约束的替代数据集，再用于行为克隆。
result: 在多个机器人控制环境中，DTWIL相比基线方法更有效地学习了符合约束的策略，并保持了较高性能。
conclusion: 该方法为解决动作约束下的模仿学习提供了有效框架，有助于安全机器人应用。
---

## Abstract
Policy learning under action constraints plays a central role in ensuring safe behaviors in various robot control and resource allocation applications.
In this paper, we study a new problem setting termed Action-Constrained Imitation Learning (ACIL), where an action-constrained imitator aims to learn from a demonstrative expert with larger action space.
The fundamental challenge of ACIL lies in the unavoidable mismatch of occupancy measure between the expert and the imitator caused by the action constraints. We tackle this mismatch through trajectory alignment and propose DTWIL, which replaces the original expert demonstrations with a surrogate dataset that follows similar state trajectories while adhering to the action constraints. Specifically, we recast trajectory alignment as a planning problem and solve it via Model Predictive Control, which aligns the surrogate trajectories with the expert trajectories based on the Dynamic Time Warping (DTW) distance. Through extensive experiments, we demonstrate that learning from the dataset generated by DTWIL significantly enhances performance across multiple robot control tasks and outperforms various benchmark imitation learning algorithms in terms of sample efficiency.

---

## 论文详细总结（自动生成）

# 论文《Action-Constrained Imitation Learning》详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：在机器人控制和资源分配等实际应用中，智能体往往面临**动作约束**（例如力矩上限、功率限制、运动学限制），而专家演示数据通常来自无约束或约束较弱的专家。传统模仿学习方法（如行为克隆、GAIL）假定专家与学习者动作空间一致，当学习者受到更紧的动作约束时，会产生**占用度度量失配**（occupancy measure distortion），导致策略性能严重下降。
- **研究动机**：现有工作主要关注无约束模仿学习或动作约束下的强化学习（ACRL），但**动作约束下的模仿学习（Action-Constrained Imitation Learning, ACIL）** 问题未被系统研究。直接套用ACRL中的投影层方法会导致轨迹偏移，无法解决状态分布失配。
- **整体含义**：ACIL旨在让受限学习者从无约束专家演示中学习，通过生成符合约束的替代轨迹来弥合能力差距，为安全、实用的机器人学习提供新范式。

## 2. 论文提出的方法论

### 核心思想
- 将ACIL分解为两个阶段：
  1. **轨迹对齐**：对每个无约束专家轨迹，生成一条**动作可行的替代轨迹**，使其状态序列与专家状态序列尽可能相似（允许不同长度）。
  2. **下游模仿学习**：在替代数据集上使用任意现成模仿学习算法（如行为克隆）训练策略，自然满足动作约束。

### 关键技术细节
- **模型预测控制（MPC）**：将轨迹对齐视为规划问题，使用MPC逐步生成替代动作。每步执行有限步规划，仅选取第一个动作作用于环境，从而自适应调整对齐进程。
- **动态时间规整（DTW）距离**：作为状态序列相似性度量，允许对齐不同长度的轨迹，解决受约束学习者需要更多时间步才能接近专家状态的问题。
  - 定义：`dDTW(σ, σ') = min_{A∈A} ⟨Δ, A⟩_F`，其中Δ为欧氏距离矩阵，A为允许右、下、右下移动的二进制对齐矩阵。
  - 递归计算：`dDTW(σ_{0:i}, σ'_{0:j}) = ‖σ_i - σ'_j‖₂ + min(...)`。
- **交叉熵方法（CEM）优化**：在MPC中迭代采样、评估、更新动作分布，生成候选轨迹。使用**拒绝采样**确保动作满足约束。
- **进展管理**：引入参数`tpg`，根据DTW规整路径判断当前对齐到专家轨迹的第几个状态，异步更新允许学习者以更慢速度前进。
- **专家正则化控制（ERC）**：在规划前几步混合采样动作与对应专家动作（加权平均），提升在精度要求高的环境（如Hopper）中的稳定性。

### 算法流程简化说明
1. 对每个专家轨迹，初始化动力学模型和替代轨迹。
2. MPC循环：每步由CEM采样可行动作序列，使用动力学模型滚动生成H步轨迹，计算其与专家片段`σ_{tpg:tpg+H}`的DTW距离，选取最优第一个动作执行，更新状态和`tpg`。
3. 将所有替代轨迹存入数据集`D_sur`。
4. 在`D_sur`上训练策略（如行为克隆）。

## 3. 实验设计

### 使用场景/环境
- **Maze2d-Medium-v1**（布局导航，2D动作空间）
- **HalfCheetah-v3**（猎豹跑步，6D动作空间）
- **Hopper-v2**（单腿跳跃，3D动作空间）
- **Table-Wiping**（Robosuite机械臂擦桌子，6D动作空间）

### 动作约束类型
- 盒子约束（Box）：如`|a_i|<0.1`（Maze2d）、`|a_i|<0.5`（HalfCheetah）
- 状态相关功率约束：如`∑|v_i a_i|≤0.5`（Maze2d）、`∑ max(w_i a_i,0)≤10`（Hopper）
- L2范数约束：如对Table-Wiping的不同关节组施加L2上限。

### 对比方法
- **LfD（状态-动作）**：BC, GAIL, CFIL-sa
- **LfO（仅状态）**：BCO, GAIfO, OPOLO, CFIL-s, SAIL, DIFO
- 所有基线方法的输出动作经投影层强制满足约束。

### 训练设置
- 在线方法（GAIL, OPOLO等）限制**50K环境步**，离线方法（BC, CFIL等）使用相同专家数据。每个实验3个随机种子。

## 4. 资源与算力

- **文中未明确说明具体GPU型号、数量或训练时长**。仅在致谢中感谢“National Center for High-performance Computing (NCHC) provided computational and storage resources”。因此无法量化算力开销。

## 5. 实验数量与充分性

- **主实验**：4个环境×2种约束（共8个任务）×10种方法，报告平均回报和DTW距离，含标准差，共240组数据点。
- **消融实验**包含：
  - 对齐准则比较：DTW vs L2（表3）
  - 与原生BC对比（表4）
  - CFIL使用DTWIL替代数据的效果（图5）
  - ERC的β和h_erc参数影响（表9）
  - 进展管理异步vs同步（表7）
  - MPc步数影响（表10）
  - 约束强度变化（表11）
  - 专家演示数量变化（表12）
- **公平性**：所有方法使用相同专家数据，在线方法步数一致，离线方法使用同等数据量。结果报告均值和标准差。实验覆盖了常见连续控制任务和多种约束类型，消融较全面。

**结论**：实验充分、客观、公平。

## 6. 论文的主要结论与发现

1. **ACIL问题具有独特挑战**：占用度量失配无法通过简单投影解决，需要专门的轨迹对齐方法。
2. **DTWIL显著优于所有基线**：在8个任务中，DTWIL（使用BC）在回报和DTW距离上均大幅领先；在线方法（GAIL, OPOLO等）在50K步内几乎无法有效学习。
3. **DTW距离比L2距离更适合对齐**：在HalfCheetah和Hopper上，DTW对齐产生的策略性能远高于L2对齐（表3）。
4. **替代数据集可提升其他IL方法**：将CFIL应用于DTWIL生成的替代数据，性能显著提升（图5）。
5. **样本效率高**：DTWIL仅需训练动力学模型，无需大量环境交互，适用于样本受限场景。

## 7. 优点

- **问题定义新颖**：首次正式提出动作约束模仿学习（ACIL），并识别出核心挑战——占用度量失配。
- **方法设计巧妙**：将约束满足与模仿学习解耦，通过MPC+DTW生成可行替代轨迹，下游可灵活选用任意IL算法。
- **技术合并合理**：DTW自然解决序列长度不匹配问题；MPC+CEM提供有效在线规划；ERC增强稳定性。
- **实验验证充分**：涵盖多种环境、约束类型，与多种LfD/LfO方法对比，消融实验深入。
- **代码开源**：提供了可复现的实验基线仓库。

## 8. 不足与局限

- **依赖动力学模型**：需要学习环境动力学模型，模型误差可能影响对齐质量，尤其在复杂高维环境。
- **计算成本**：MPC每步进行CEM采样和DTW计算，开销高于简单策略网络，可能限制实时应用。
- **ERC需要专家动作**：ERC混合专家动作有助于稳定，但在专家演示质量不佳或数量少时可能效果减弱。
- **仅验证连续动作空间**：未扩展到离散动作或混合动作空间任务。
- **未在真实机器人上验证**：实验全部在仿真环境，与实际硬件存在差距。
- **未讨论约束违反的硬安全性**：方法通过拒绝采样保证可行性，但未处理可能的状态约束或安全临界情况。
- **超参数较多**：MPC规划步数H、CEM迭代次数、ERC权重β和混合长度h_erc等需调节，对算法泛化性有一定影响。

（完）
