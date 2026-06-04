---
title: Self-Improving Embodied Foundation Models
title_zh: 自改进的具身基础模型
authors: "Seyed Kamyar Seyed Ghasemipour, Ayzaan Wahid, Jonathan Tompson, Pannag R Sanketi, Igor Mordatch"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=KXMIIVUB9U"
tags: ["query:vla"]
score: 8.0
evidence: 自改进的具身基础模型采用两阶段后训练
tldr: 具身基础模型多限于行为克隆，难以自主提升。该工作提出两阶段后训练：先通过行为克隆和步骤预测进行SFT，然后利用步骤预测提取奖励函数和成功检测器，使机器人以最小人类监督自主练习下游任务。真实世界实验显示该方法持续提升任务性能，接近强化学习效果但更易扩展。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1994, \"height\": 743, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1736, \"height\": 429, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1873, \"height\": 456, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 725, \"height\": 429, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 620, \"height\": 428, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1882, \"height\": 354, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1447, \"height\": 580, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 732, \"height\": 426, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1692, \"height\": 1021, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1452, \"height\": 591, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 728, \"height\": 588, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1278, \"height\": 521, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 455, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kxmiivub9u/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1449, \"height\": 822, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-kxmiivub9u/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1371, \"height\": 739, \"label\": \"Table\"}]"
motivation: 现有具身基础模型局限于行为克隆，缺乏自主提升能力。
method: 提出两阶段后训练：SFT后利用步骤预测奖励进行自改进。
result: 在真实机器人上，该方法显著提升多种操作任务的成功率，接近RL效果。
conclusion: 奖励预测可实现有效的自监督后训练，拓展基础模型潜力。
---

## Abstract
Foundation models trained on web-scale data have revolutionized robotics, but their application to low-level control remains largely limited to behavioral cloning. Drawing inspiration from the success of the reinforcement learning stage in fine-tuning large language models, we propose a two-stage post-training approach for robotics. The first stage, Supervised Fine-Tuning (SFT), fine-tunes pretrained foundation models using both: a) behavioral cloning, and b) steps-to-go prediction objectives. In the second stage, Self-Improvement, steps-to-go prediction enables the extraction of a well-shaped reward function and a robust success detector, enabling a fleet of robots to autonomously practice downstream tasks with minimal human supervision. Through extensive experiments on real-world and simulated robot embodiments, our novel post-training recipe unveils significant results on Embodied Foundation Models. First, we demonstrate that the combination of SFT and Self-Improvement is significantly more sample-efficient than scaling imitation data collection for supervised learning, and that it leads to policies with significantly higher success rates. Further ablations highlight that the combination of web-scale pretraining and Self-Improvement is the key to this sample-efficiency. Next, we demonstrate that our proposed combination uniquely unlocks a capability that current methods cannot achieve: autonomously practicing and acquiring novel skills that generalize far beyond the behaviors observed in the imitation learning datasets used during training. These findings highlight the transformative potential of combining pretrained foundation models with online Self-Improvement to enable autonomous skill acquisition in robotics.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：当前具身基础模型（Embodied Foundation Models, EFMs）在低层控制中的应用主要局限于行为克隆（Behavioral Cloning, BC），即纯监督学习。这种范式缺乏自主提升能力，且需要大量人工采集的示教数据。受大语言模型（LLM）后训练中强化学习（RL）阶段成功的启发，作者提出将类似的“监督微调（SFT）+ 强化学习”两阶段后训练框架引入机器人领域。
- **核心问题**：如何在无需人工设计奖励函数和大量人工监督的情况下，让机器人自主练习下游任务并快速提升性能，甚至习得远超示教数据分布的崭新技能。
- **整体意义**：证明了结合网络规模预训练的基础模型与在线自改进（Self-Improvement）能够带来样本效率的显著提升，并解锁了传统行为克隆无法实现的行为泛化能力，为机器人自主技能获取开辟了新路径。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：两阶段后训练框架。
  - **第一阶段：监督微调（SFT）** ：在预训练的多模态基础模型（本文使用 PaLI-3B）上，利用机器人示教数据集同时进行两个目标的监督学习：
    1. 目标条件行为克隆（Goal-conditioned Behavioral Cloning）
    2. **“步骤到完成”预测（Steps-to-go Prediction）**：学习从当前观察和给定目标预测还需多少时间步才能完成任务。
  - **第二阶段：自改进（Self-Improvement）** ：利用第一阶段训练好的模型（冻结）作为奖励函数和成功检测器，在线收集机器人自主交互数据，并使用 REINFORCE 算法进行策略更新。

- **关键技术细节**：
  - **奖励函数定义**：
    \[
    d(o, g) = \mathbb{E}_{p_{\text{EFM}}^{\text{steps-to-go}}}[\text{steps-to-go} \mid o, g]
    \]
    \[
    r(o_t, a_t, o_{t+1}, g) = d(o_t, g) - d(o_{t+1}, g)
    \]
    即预测的“步骤数”减少量作为即时奖励，反映策略离目标更近的程度。
  - **成功检测器**：
    \[
    \text{success}(o, g) = \mathbb{1}[d(o, g) \le s]
    \]
    其中 \(s\) 是一个很小的阈值。这样避免了显式训练二分类成功检测器。
  - **算法流程（Algorithm 1）** ：
    1. 初始化策略网络为第一阶段 checkpoint；冻结另一个用于奖励和成功检测的 checkpoint。
    2. 循环：
       - 收集一批轨迹：采样指令 \(g\)，执行当前策略，直到成功检测器触发、达到最大长度或人工终止。
       - 计算每条轨迹的蒙特卡洛回报 \(R_t = \sum_{i=t}^T \gamma^{i-t} r(o_i, a_i, o_{i+1}, g)\)。
       - 将 \((o_t, a_t, g, R_t)\) 放入回放缓冲区。
       - 当缓冲区大小达到 \(N \times B\) 后，执行 \(N\) 次 REINFORCE 策略更新：
         \[
         \mathcal{L} = -c \cdot R_t \cdot \log p_{\text{EFM}}^{\text{action}}(a_t | o_t, g)
         \]
       - 清空缓冲区，进入下一轮。
  - **关键设计选择**：使用 on-policy REINFORCE（无数据复用、无自举），避免死亡三合问题；奖励函数天然带有基线项（\(V^\mu(o_t, g)\)），降低方差；成功检测通过阈值化步骤预测实现。

## 3. 实验设计：数据集/场景、基准方法、对比方法

- **实验场景**：
  - **LanguageTable**：2D 平面推块任务，具备真实世界和模拟两种环境。示教数据集包含 181,020 条人机轨迹，78,623 条独特指令。
  - **Aloha**：双臂插入任务（左臂抓取插座，右臂抓取插头并插入）。模拟环境，70 维动作空间。示教数据集通过扩散策略生成，规模为 5K、10K、15K 条成功轨迹。
  - **BananaTable**：LanguageTable 的变体，用单根香蕉代替方块，要求将香蕉推到指定位置（需要学习新的推香蕉策略，因为数据集不含香蕉）。
- **基准方法**：
  - 所有基线均基于 RT-2（使用 PaLI-3B 的 VLM），即第一阶段 SFT 后的行为克隆策略。
  - 对比方法包括不同数据量（10%、20%、80% 示教数据）下的 SFT 性能，以及不同预训练模型初始化（随机初始化 Scratch、仅单模态预训练 Uni-PaLI）的消融。
- **主要实验类型**：
  - 模拟 LanguageTable 上不同数据量下 SFT vs SFT+Self-Improvement
  - 真实 LanguageTable 上（使用 4 台机器人）的 Self-Improvement 效果
  - 模拟 Aloha 插入任务上的 Self-Improvement
  - 预训练重要性消融（Scratch、Uni-PaLI vs 完整 PaLI）
  - 域迁移（Real2Sim：用真实数据训练 Stage1，在模拟中 Self-Improve）
  - 强泛化实验（BananaTable：全新任务，只依赖基础模型的泛化能力）

## 4. 资源与算力

- **第一阶段 SFT**：使用 64 块 TPUv4（2×4×4）或 128 块 TPUv3。
- **第二阶段 Self-Improvement**：
  - 学习者（learner）：SFT 一半资源（因使用半批次大小）
  - 奖励模型：4 块 TPUv4（2×2×1）
  - 成功检测器：4 块 TPUv4（2×2×1）
- 未明确给出总训练时长，但真实世界 LanguageTable 实验大约运行 20 小时（4小时/天×5天）；BananaTable 约 8 小时；模拟实验中每个种子需要多轮迭代，但未提供具体时间。

## 5. 实验数量与充分性

- **实验数量**：
  - 模拟 LanguageTable：3 个数据量（10%、20%、80%），每个 3 个随机种子。
  - 真实 LanguageTable：两个数据量（20%、80%），其中 20% 实验重复两次（3 台和 4 台机器人），80% 一次。
  - 模拟 Aloha：两个数据量（5K、10K），每个 3 个随机种子。
  - 消融实验：Scratch、Uni-PaLI 在 10%、20%、80% 数据量上各 3 个种子。
  - Real2Sim：80% 真实数据训练，在模拟中 Self-Improve，比较 PaLI vs Uni-PaLI 奖励模型。
  - BananaTable：一次真实实验（2 台机器人，约 8 小时），无多次种子。
- **充分性评价**：
  - **充分**：模拟实验均包含多个随机种子，统计显著性有保障；消融实验系统；真实世界实验也有重复（20% 两次）。唯一不足是 BananaTable 实验仅一次，但作为强泛化演示仍具说服力。
  - **客观公平**：基线采用 RT-2 等价模型；对比方法在相同设置下比较；实验结果清晰展示了 Self-Improvement 的优势。

## 6. 论文的主要结论与发现

1. **Self-Improvement 显著提升下游任务成功率**：在所有测试场景中，经过 Self-Improvement 的策略成功率均远高于纯行为克隆（1.5× 以上提升）。
2. **样本效率极高**：例如在 LanguageTable 上，仅需额外 3% 的自改进经验（相对示教集），成功率从 45% 提升到 75%；而将示教数据量增加 8 倍只能从 45% 提升到 60%。
3. **预训练是自改进成功的关键**：使用完整 PaLI 预训练模型时 Self-Improvement 效果最好；Uni-PaLI 次之；随机初始化基本无效。差距在小数据场景下更明显。
4. **可实现域迁移**：Real2Sim 实验证明，在模拟环境中自改进可有效提升策略（从 22% 到 59%），且预训练模型优势仍然存在。
5. **解锁强泛化能力**：BananaTable 实验表明，仅通过自改进就能让策略学会如何推香蕉（全新行为），成功率从 63% 提升到 85%，且策略行为可观察地优化。
6. **自改进过程鲁棒**：真实世界实验中，单个人即可监控多台机器人自动运行约 20 小时，无需额外人工标签。

## 7. 优点

- **方法简洁且通用**：无需手工设计奖励函数，无需真实成功检测器，仅依赖步骤预测的差值即可构造稠密奖励，且支持多机器人并行。
- **样本效率突出**：相比增加示教数据量，自改进能以少得多的额外交互实现更大性能提升。
- **强大的泛化能力**：不仅支持语义泛化（类似 RT-2 的新物体），还能习得完全新的行为（行为泛化），这是纯监督学习无法实现的。
- **工程实现友好**：使用 on-policy REINFORCE 和简单的成功阈值，避免了复杂的 off-policy 和自举带来的训练不稳定；奖励函数自带基线降低方差。
- **充分的消融实验**：通过多种预训练初始化、域迁移等实验，系统证明了预训练和自改进的协同作用。

## 8. 不足与局限

- **实验覆盖**：
  - 只使用了 PaLI-3B 作为基础模型，未验证其他架构（如扩散模型、flow matching 等）的兼容性。
  - 真实世界实验仅在 LanguageTable 和 Aloha 两种平台上进行，Aloha 仅模拟实验且仅一个任务，真实 Aloha 实验未完成。
  - BananaTable 实验仅一次，未提供随机种子重复。
  - 仅测试了单任务自改进（Block2Block 或插入），未充分探索多任务联合自改进（虽提及但未完成实验）。
- **算法局限性**：
  - 使用 on-policy REINFORCE 无数据复用，样本效率仍有提升空间；未探索 off-policy 方法。
  - 奖励模型依赖于示教数据的覆盖度，对于完全未见过的失败状态可能给出不准确信号（分布外问题）。
  - 成功阈值 \(s\) 和折扣因子 \(\gamma\) 等超参数需要调整。
  - 自改进可能导致策略过优化（过拟合奖励信号），需要适当的停止准则或正则化。
- **应用限制**：
  - 需要访问冻结的步骤预测模型（第一阶段的 checkpoint），这部分算力需求不低。
  - 对于长时域任务，需要进一步研究技能链式组合（skill-chaining）。
  - 机器人硬件带来的约束（如 Aloha 10Hz 控制频率需要本地推理而非远程推理）。
- **公平性/偏差**：未讨论不同任务类别的公平性或潜在的负社会影响（如自动化导致失业）的具体缓解措施。

（完）
