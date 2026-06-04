---
title: Enhancing Tactile-based Reinforcement Learning for Robotic Control
title_zh: 增强基于触觉的强化学习以实现机器人控制
authors: "Elle Miller, Trevor McInroe, David Abel, Oisin Mac Aodha, Sethu Vijayakumar"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Toy96yYopR"
tags: ["query:vla"]
score: 4.0
evidence: 基于触觉的强化学习机器人控制
tldr: 触觉感知对于机器人操纵至关重要，但强化学习中的触觉利用效果不稳定。本文通过自监督学习方法更有效地利用稀疏二进制触觉信号，结合本体感觉，在解耦的机器人-物体运动中实现超人的灵巧操作。实验证明稀疏触觉对灵巧交互至关重要。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1397, \"height\": 796, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1413, \"height\": 791, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 407, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1433, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1433, \"height\": 409, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1233, \"height\": 292, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1434, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1446, \"height\": 409, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1014, \"height\": 505, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 709, \"height\": 524, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 711, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 728, \"height\": 572, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 707, \"height\": 520, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 699, \"height\": 519, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 659, \"height\": 520, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 659, \"height\": 519, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 666, \"height\": 587, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 660, \"height\": 519, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 657, \"height\": 520, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 660, \"height\": 587, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 490, \"height\": 140, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1313, \"height\": 1523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 492, \"height\": 141, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1304, \"height\": 1507, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 590, \"height\": 439, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1445, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 659, \"height\": 497, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1425, \"height\": 2072, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1429, \"height\": 2053, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-toy96yyopr/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1428, \"height\": 2016, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-toy96yyopr/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1019, \"height\": 392, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-toy96yyopr/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1433, \"height\": 263, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-toy96yyopr/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 951, \"height\": 427, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-toy96yyopr/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1448, \"height\": 737, \"label\": \"Table\"}]"
motivation: 触觉在机器人强化学习中效果不稳定，需要更好的学习方法。
method: 开发自监督学习方法，利用稀疏二进制触觉信号和本体感觉。
result: 在解耦机器人-物体运动中达到超人灵巧度。
conclusion: 稀疏二进制触觉对灵巧操纵至关重要。
---

## Abstract
Achieving safe, reliable real-world robotic manipulation requires agents to evolve beyond vision and incorporate tactile sensing to overcome sensory deficits and reliance on idealised state information. Despite its potential, the efficacy of tactile sensing in reinforcement learning (RL) remains inconsistent. We address this by developing self-supervised learning (SSL) methodologies to more effectively harness tactile observations, focusing on a scalable setup of proprioception and sparse binary contacts. We empirically demonstrate that sparse binary tactile signals are critical for dexterity, particularly for interactions that proprioceptive control errors do not register, such as decoupled robot-object motions. Our agents achieve superhuman dexterity in complex contact tasks (ball bouncing and Baoding ball rotation). Furthermore, we find that decoupling the SSL memory from the on-policy memory can improve performance. We release the Robot Tactile Olympiad ($\texttt{RoTO}$) benchmark to standardise and promote future research in tactile-based manipulation. Project page: https://elle-miller.github.io/tactile_rl.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：机器人操作需要超越视觉感知，融入触觉以克服对理想化状态信息的依赖。然而，触觉在强化学习（RL）中的效果一直不稳定：部分研究报告触觉信息带来的性能提升有限，甚至无提升；另一些则认为二进制接触信息已隐含在本体感觉历史中。
- **核心问题**：触觉数据的特性（稀疏、非平滑）导致深度RL难以从中提取有效表征，容易过早收敛到依赖连续本体感觉信号的次优策略。本文旨在开发通用的自监督学习（SSL）方法，以更有效地利用触觉观测，提高RL在机器人操作中的表现。
- **整体含义**：证明了在仅有本体感觉和稀疏二进制接触（无视觉、无特权信息）的设置下，代理可以在复杂接触任务中达到超人灵巧度，挑战了“二进制接触信息已隐含在本体感觉中”的观点，为触觉驱动的机器人操作提供了更实用的路线。

## 2. 提出的方法论

### 核心思想
- 采用部分可观测马尔可夫决策过程（POMDP）框架，代理接收一个包含 \(k\) 步历史的本体感觉和触觉的复合观测。
- 代理包含三个MLP：观测编码器 \(e\)、策略 \(\pi\)、价值函数 \(v\)。使用PPO训练，并联合一个自监督辅助损失 \(\mathcal{L}_{\text{aux}}\) 进行表征学习。
- 本文提出四种自监督辅助目标，以及一种分离辅助记忆的策略。

### 关键技术细节
- **观测编码器**：3层MLP，维度：\(o_t \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow z_t\)，使用层归一化和ELU激活。
- **策略网络**：3层MLP：\(z_t \rightarrow 128 \rightarrow 64 \rightarrow a_t\)，输出层tanh激活。
- **价值网络**：3层MLP：\(z_t \rightarrow 128 \rightarrow 64 \rightarrow 1\)。
- **PPO更新**：对编码器、策略、价值函数使用共享学习率 \(lr\)，梯度裁剪1.0；辅助损失使用单独优化器和单独学习率 \(lr_{\text{aux}}\)，无梯度裁剪。

### 四种自监督目标

1. **触觉重建（Tactile Reconstruction, TR）**  
   - 从表征 \(z_t\) 解码触觉观测 \(\hat{o}_t^{\text{tact}}\)，使用带正权重 \(p_c = 10\) 的二元交叉熵损失，惩罚漏报。
   - 公式：\(\mathcal{L}_{\text{TR}} = \text{BCE}(\hat{o}_t^{\text{tact}}, o_t^{\text{tact}})\)

2. **全重建（Full Reconstruction, FR）**  
   - 同时重建触觉和本体感觉，损失为 \(\mathcal{L}_{\text{TR}} + \text{MSE}(\hat{o}_t^{\text{prop}}, o_t^{\text{prop}})\)。

3. **前向动力学（Forward Dynamics, FD）**  
   - 通过前向模型 \(f\) 预测未来潜状态：\(\hat{z}_{t+i} = f(\hat{z}_{t+i-1}, a_{t+i-1})\)。
   - 损失对 \(n\) 步预测（除去当前步）计算投影 \(p(\hat{z}_{t+i})\) 与目标编码器 \(e^T\)（EMA更新）产生的目标潜状态 \(z_{t+i}^T\) 之间的MSE：  
     \(\mathcal{L}_{\text{FD}} = \sum_{i=1}^{n-1} \text{MSE}\big(p(\hat{z}_{t+i}), z_{t+i}^T\big)\)

4. **触觉前向动力学（Tactile Forward Dynamics, TFD）**  
   - 在FD基础上，对预测的潜状态解码出触觉观测并加入触觉重建损失：  
     \(\mathcal{L}_{\text{TFD}} = \mathcal{L}_{\text{FD}} + \sum_{i=1}^{n-1} \text{BCE}(\hat{o}_{t+i}^{\text{tact}}, o_{t+i}^{\text{tact}})\)

### 分离辅助记忆（Separated Auxiliary Memory）
- 默认SSL与on-policy数据同一批更新，导致损失尖峰。本文将辅助数据存入更大独立缓冲区（大小为 \(N_{\text{rollouts}}\) 倍 on-policy 内存），以稳定训练、扩大数据分布。

## 3. 实验设计

### 数据集/场景
- 使用自建的 **Robot Tactile Olympiad (RoTO)** 基准，包含三个Isaac Lab环境：
  - **Find**：Franka机器人寻找平面上的固定球（300步）。
  - **Bounce**：Shadow Hand弹跳一个30g球（600步/10秒）。
  - **Baoding**：Shadow Hand旋转两个55g球（600步/10秒）。
- 机器人采用关节位置控制，物理仿真120Hz，控制策略60Hz。

### 对比方法
- RL-only基线：仅本体感觉、本体感觉+触觉、仅本体感觉（无上一动作）。
- SSL方法对比：FR、TR、FD、TFD，以及FD+分离记忆（FD+\(N_{\text{rollouts}}\)）。

### Benchmark特性
- 每个环境独立超参数搜索（TPE采样，20次试验），对PPO超参数、SSL超参数、序列长度 \(n\)、分离记忆大小等进行单独优化。
- 每个实验跑5个随机种子，绘制均值±1标准差。

## 4. 资源与算力

- **计算资源**：GPU集群，8× NVIDIA RTX A4500，仿真环境需16GB VRAM、32GB RAM、8 CPU核。
- **单实验时间**：约60小时（超参数搜索~50小时 + 5种子运行~10小时）。
- **总算力**：7个实验 × 3个任务 = 21次运行，累计约1,260小时（文中提到7×3×60=1,260 hours）。

## 5. 实验数量与充分性

- **实验数量**：21组完整实验（3环境 × 7方法），每组含超参数搜索及5种子重复。另有附加分析：互信息估计、物理指标统计、潜轨迹可视化、未来触觉预测分类指标等。
- **充分性与公平性**：
  - 对每种方法都进行了独立的超参数搜索，遵循RL研究最佳实践，确保不同方法间可比。
  - 报告了均值±1标准差，并给出了物理指标（找到时间、弹跳次数、旋转次数）和互信息分析，从多角度验证。
  - 消融实验覆盖了四种SSL目标、分离记忆、不同传感器组合，实验设计较为系统。
  - 但所有实验均在仿真中完成，未在真实机器人上验证，是主要局限性。

## 6. 主要结论与发现

1. **二进制触觉的关键作用**：在解耦物体-机器人动力学、低惯性物体、接触空间模糊、多接触解析等场景下，显式触觉信息不可或缺，不能仅靠本体感觉历史。
2. **SSL提升表征质量**：触觉重建和前向动力学优于RL-only；前向动力学总体最佳，能有效编码物体位置和速度。
3. **分离辅助记忆的增益**：在复杂任务（Baoding）中显著提升性能，推测因任务需要更长时序推理。
4. **超人类性能**：最佳代理在Bounce达88次弹跳/10秒（人类吉尼斯纪录~59次），在Baoding达25次旋转/10秒（人类最快~13次）。
5. **互信息分析**：前向动力学代理的潜表征与真实状态互信息最高，成功编码关键状态变量。

## 7. 优点

- **系统性**：提出并比较了四种针对触觉的SSL目标，并引入分离记忆，方法清晰，对比全面。
- **新颖基准**：发布了RoTO基准，包含三种不同接触模式的任务，促进该领域标准化研究。
- **超人体表现**：在仅有稀疏二进制触觉和本体感觉的设定下达到超越人类的速度，展示触觉的巨大潜力。
- **深入分析**：通过互信息、潜轨迹可视化、未来触觉预测分类指标等手段揭示SSL为何有效。
- **实用建议**：给出了具体的实践推荐（优先使用触觉重建或前向动力学+分离记忆），简化触觉表示以避免复杂增益。

## 8. 不足与局限

- **未进行真实机器人验证**：所有实验在仿真中完成，尽管作者声称二进制接触降低了sim-to-real难度，但仍需实际硬件验证。
- **计算代价高**：SSL增加训练时间，尤其前向动力学中的长序列预测；分离记忆也增加内存开销。
- **训练稳定性问题**：触觉动力学损失中的正权重固定，未随数据分布动态调整；某些实验（如TFD在Bounce上表现最差）显示辅助损失可能引入干扰。
- **环境多样性有限**：仅三个任务，且均为单手操作，未测试双手机器人或多物体交互场景。
- **泛化性能未探索**：未验证方法在其他模态（如视觉）或不同触觉传感器类型下的效果。
- **偏见风险**：性能提升可能部分源于超参数过度优化（对每个实验单独搜索），但在研究性工作中可接受。

（完）
