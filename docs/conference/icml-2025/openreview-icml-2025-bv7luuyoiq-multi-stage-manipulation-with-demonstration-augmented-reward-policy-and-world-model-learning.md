---
title: "Multi-Stage Manipulation with Demonstration-Augmented Reward, Policy, and World Model Learning"
title_zh: 基于演示增强奖励、策略与世界模型的多阶段操作学习
authors: "Adrià López Escoriza, Nicklas Hansen, Stone Tao, Tongzhou Mu, Hao Su"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=Bv7LUUYOiq"
tags: ["query:vla"]
score: 7.0
evidence: 演示增强的多阶段操作学习
tldr: 针对长时序机器人操作任务中稠密奖励设计困难与状态空间探索难的问题，提出DEMO3框架。利用多阶段结构分解目标，融合多阶段稠密奖励学习、双阶段训练和世界模型，结合演示数据强化RL，显著提升复杂操作任务的学习效率。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1694, \"height\": 422, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 856, \"height\": 233, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1692, \"height\": 725, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 867, \"height\": 403, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1770, \"height\": 470, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1758, \"height\": 682, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 857, \"height\": 632, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 784, \"height\": 589, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 769, \"height\": 530, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1512, \"height\": 716, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1506, \"height\": 714, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1509, \"height\": 359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1459, \"height\": 764, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1354, \"height\": 927, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1566, \"height\": 1247, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1595, \"height\": 1329, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-bv7luuyoiq/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1678, \"height\": 992, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 876, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 500, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1625, \"height\": 486, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1152, \"height\": 1037, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1598, \"height\": 445, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1521, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 977, \"height\": 386, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1417, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1172, \"height\": 330, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-bv7luuyoiq/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 944, \"height\": 1960, \"label\": \"Table\"}]"
motivation: 长时序操作任务中稠密奖励设计困难、探索效率低。
method: 利用多阶段结构，融合稠密奖励学习、双阶段训练与世界模型。
result: 显著提升复杂操作任务学习效率。
conclusion: 为端到端机器人操作学习提供有效框架。
---

## Abstract
Long-horizon tasks in robotic manipulation present significant challenges in reinforcement learning (RL) due to the difficulty of designing dense reward functions and effectively exploring the expansive state-action space. However, despite a lack of dense rewards, these tasks often have a multi-stage structure, which can be leveraged to decompose the overall objective into manageable sub-goals. In this work, we propose DEMO³, a framework that exploits this structure for efficient learning from visual inputs. Specifically, our approach incorporates multi-stage dense reward learning, a bi-phasic training scheme, and world model learning into a carefully designed demonstration-augmented RL framework that strongly mitigates the challenge of exploration in long-horizon tasks. Our evaluations demonstrate that our method improves data-efficiency by an average of 40% and by 70% on particularly difficult tasks
compared to state-of-the-art approaches. We validate this across 16 sparse-reward tasks spanning four domains, including challenging humanoid visual control tasks using as few as five demonstrations.

---

## 论文详细总结（自动生成）

### 论文详细中文总结

#### 1. 核心问题与整体含义（研究动机和背景）
- **问题**：长时序（long-horizon）机器人操作任务在强化学习中面临两大挑战：一是稠密奖励函数设计极其困难，容易出现局部最优或意外捷径；二是稀疏奖励下状态-动作空间庞大，探索效率极低。
- **机遇**：这类任务通常具有天然的多阶段结构（如抓取→提升→放置），可将整体目标分解为若干子目标。利用阶段指示（stage indicators）可以轻松获取稀疏的阶段奖励。
- **目标**：在仅有少量演示（低至5个）和视觉输入的情况下，高效学习多阶段操作任务，弥合稀疏奖励与高效探索之间的鸿沟。

#### 2. 论文提出的方法论
- **核心思想**：提出 **DEMO³（Demonstration-Augmented Reward, Policy, and World Model Learning）**，一个用于多阶段操作的演示增强模型基强化学习（MBRL）框架。关键创新是**在线学习多阶段稠密奖励**，同时联合学习策略、世界模型和奖励函数。
- **关键技术细节**：
  - **多阶段稠密奖励学习**：为每个阶段 \( k \) 训练一个判别器 \( \delta_k \)，输入为世界模型编码的潜状态 \( z_t \)，输出该状态能成功过渡到下一阶段的概率。损失函数为 BCE（公式2）：
    \[
    L_{\delta_k} = \mathbb{E}_{(o_t, r_t=k, s_t) \sim \mathcal{B}} [\text{BCE}(1_{s_t > k}, \delta_k(h(o_t)))]
    \]
    其中 \( s_t \) 为轨迹从 t 时刻起能达到的最大阶段标签。
  - **稠密奖励生成**：将判别器输出映射到 \( [-\beta, \beta] \)（\(\beta \le 1/3\)），与稀疏阶段奖励相加（公式4）：
    \[
    \hat{r}_t^\delta = r_t + \beta \cdot \tanh(\delta_{r_t}(z_t))
    \]
    保证阶段间奖励不交叉。
  - **双阶段训练方案**：
    - **Phase 1（预训练）**：使用行为克隆（BC）预训练策略 \( \pi_{BC} \) 和编码器 \( h_{BC} \)，并用early stopping避免过拟合。
    - **Phase 2（交互学习）**：初始化策略和编码器为预训练版本；智能体通过学生模型（世界模型规划）和预训练策略混合采集数据，并采用演示采样过采样（初始50%）和退火策略逐步过渡到纯规划。整体损失（公式5）：
      \[
      \mathcal{L}_P = \mathcal{L}_R + \mathcal{L}_Q + \mathcal{L}_h + \mathcal{L}_\delta
      \]
      其中 \( \mathcal{L}_R \) 使用学习到的稠密奖励作为预测目标。
- **算法流程**：Algorithm 1 描述了每一轮交互-更新的过程，包括环境步、最大阶段标签计算、采样更新等。

#### 3. 实验设计
- **数据集/场景**：4个域共16个视觉稀疏奖励多阶段操作任务：
  - ManiSkill Manipulation（5个任务，如Peg Insertion、Stack Cube）
  - Meta-World（5个任务，如Assembly、Stick Push）
  - Robosuite（4个任务，如Lift、Door）
  - ManiSkill Humanoids（2个高维人形任务，如Place Apple）
- **基准对比方法**：
  - **MoDem**（演示增强MBRL基线）
  - **LaNE**（基于潜近邻探索的模型无关RL）
  - **TD-MPC2**（纯MBRL基线）
  - **BC**（行为克隆基线）
- **实验设置**：每个域给定不同的演示数量（5-100）和交互步数（100k-500k）；所有实验重复5个随机种子，报告平均成功率和95%置信区间。

#### 4. 资源与算力
- **硬件**：所有实验在**单个NVIDIA GeForce RTX 3090 GPU**和**32GB RAM**上完成。
- **时间成本**：平均每100k交互步约5.19小时（Robosuite域），低于MoDem（8.37h）和LaNE（20.40h），略高于TD-MPC2（4.84h），开销主要来自奖励学习。

#### 5. 实验数量与充分性
- **总体实验量**：16个任务 × 5个种子 × 多种对比方法 = 大量独立实验。此外还包括：
  - **消融实验**（图7）：去掉奖励学习、策略预训练、演示采样过采样等组件，验证各组件贡献。
  - **演示效率分析**（图8）：测试5~200个演示下的学习步数。
  - **奖励粒度分析**（图9）：比较1阶段、2阶段、3阶段和稠密奖励的效果。
  - **单任务结果**（Appendix A.1）：逐个展示所有任务的曲线。
- **充分性与公平性**：对比方法均使用官方实现和默认参数；baselines尽量适配视觉和多观测输入；实验结果稳定，置信区间合理；消融分析覆盖了关键设计。实验设计较为充分、客观、公平。

#### 6. 论文的主要结论与发现
- DEMO³在4个域上平均**数据效率提升40%**，在困难任务提升**70%**（如Peg Insertion、Stack Cube）。
- **奖励学习是关键组件**：去除奖励学习后性能显著下降；尤其在长时序高精度任务中，演示+世界模型仍难以探索，奖励学习提供关键指引。
- **双阶段训练和演示采样过采样贡献显著**：即使无奖励学习，预训练+过采样也能带来性能提升。
- **仅需2阶段奖励即可接近稠密奖励性能**，证明阶段指示+少量演示已足够引导学习。
- **低演示数量下优势明显**：仅5个演示，DEMO³是唯一能在交互预算内达成有意义成功率的算法。

#### 7. 优点
- **方法设计亮点**：
  - 将**在线稠密奖励学习**无缝集成到MBRL框架中，充分利用多阶段结构。
  - 双阶段训练有效解决早期探索问题，且预训练策略通过early stopping防止过拟合。
  - 对任何MBRL算法可即插即用（基于TD-MPC2实现，但框架通用）。
  - 对演示数量鲁棒，极少量演示（5个）即可工作。
- **实验设计亮点**：
  - 覆盖**16个任务**，4个不同域（含高维人形），任务难度跨度大。
  - 系统的消融和组件分析（奖励、预训练、粒度、演示数），结论可靠。
  - 与多个强基线（MoDem、LaNE、TD-MPC2）公平对比，并公开代码和演示数据。

#### 8. 不足与局限
- **局限**：
  - **仅在仿真中验证**，未部署到真实机器人；作者虽引用MoDem真实部署成功经验，但需进一步验证。
  - **演示来源单一**：所有演示由训练好的TD-MPC2（稠密奖励+状态观测）生成，未探索人类遥操作或其他多样性来源的影响。
  - **超参数固定**：演示采样比例（50%）和退火策略未自适应调整，可能不是最优。
  - **任务设定**：阶段指示需人工定义，部分任务不易自然分解。
- **潜在偏差**：实验任务可能偏向适合多阶段分解的场景，通用性需更多验证。
- **不足**：消融实验在部分域（如Robosuite）上未展示详细曲线；计算资源报告（单个GPU）虽足够，但未讨论大规模复现的扩展性。

（完）
