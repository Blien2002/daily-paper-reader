---
title: "MENTOR: Mixture-of-Experts Network with Task-Oriented Perturbation for Visual Reinforcement Learning"
title_zh: MENTOR：面向视觉强化学习的混合专家网络与任务导向扰动
authors: "Suning Huang, Zheyu Aqa Zhang, Tianhai Liang, Yihan Xu, Zhehao Kou, Chenhao Lu, Guowei Xu, Zhengrong Xue, Huazhe Xu"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=t46uezeQH8"
tags: ["query:vla"]
score: 7.0
evidence: 基于视觉的强化学习结合混合专家网络用于机器人操作
tldr: "针对视觉深度强化学习样本效率低的问题MENTOR采用混合专家架构和任务导向扰动机制在三个仿真基准和真实机器人操作任务上取得83%成功率显著超过基线方法。"
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 850, \"height\": 283, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1554, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1610, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1370, \"height\": 529, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1574, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1609, \"height\": 985, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1595, \"height\": 770, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 620, \"height\": 558, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1743, \"height\": 475, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1311, \"height\": 544, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1427, \"height\": 334, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1216, \"height\": 630, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 591, \"height\": 597, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 566, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 764, \"height\": 548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-t46uezeqh8/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 836, \"height\": 209, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 853, \"height\": 717, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1352, \"height\": 299, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 860, \"height\": 783, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1478, \"height\": 237, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1470, \"height\": 1604, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 316, \"height\": 581, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 997, \"height\": 151, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-t46uezeqh8/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 604, \"height\": 239, \"label\": \"Table\"}]"
motivation: 视觉RL样本效率低限制实际机器人应用。
method: 将标准MLP替换为混合专家骨干并引入任务导向扰动。
result: "在仿真和真实操作任务上分别达到83%成功率显著优于现有方法。"
conclusion: 架构和优化改进能大幅提升视觉RL的效率和鲁棒性。
---

## Abstract
Visual deep reinforcement learning (RL) enables robots to acquire skills from visual input for unstructured tasks. However, current algorithms suffer from low sample efficiency, limiting their practical applicability. In this work, we present MENTOR, a method that improves both the *architecture* and *optimization* of RL agents. Specifically, MENTOR replaces the standard multi-layer perceptron (MLP) with a mixture-of-experts (MoE) backbone and introduces a task-oriented perturbation mechanism. MENTOR outperforms state-of-the-art methods across three simulation benchmarks and achieves an average of 83\% success rate on three challenging real-world robotic manipulation tasks, significantly surpassing the 32% success rate of the strongest existing model-free visual RL algorithm. These results underscore the importance of sample efficiency in advancing visual RL for real-world robotics. Experimental videos are available at https://suninghuang19.github.io/mentor_page/.

---

## 论文详细总结（自动生成）

## 1. 核心问题与研究动机
视觉深度强化学习（RL）在机器人控制任务中面临样本效率低下的瓶颈，导致大多数方法必须先在仿真环境中训练再部署到真实世界，存在“仿真-现实”差距（sim-to-real gap）。本文旨在通过改进智能体的**网络架构**和**优化方法**，从根本上提升视觉RL的样本效率，使其能够直接从真实世界的视觉输入中高效学习。

## 2. 方法论：MENTOR
MENTOR 包含两个关键改进：
- **混合专家（MoE）骨干网络**：将策略网络中的标准多层感知机（MLP）替换为 MoE 架构。MoE 由多个专家（前馈网络）和一个路由网络组成，对每个输入仅激活 top-k 个专家，并通过加权组合输出。这种稀疏激活机制允许梯度动态分配到不同专家，有效缓解了复杂任务（多阶段、多子目标）中的梯度冲突问题。论文通过多任务实验（图3a/b）和单任务多阶段实验（图4）验证了MoE在缓解梯度冲突和自动分工方面的优势。
- **任务导向扰动（Task-Oriented Perturbation）**：周期性用随机噪声扰动网络权重是逃离局部最优的常用手段。MENTOR 提出采样来自**历史高性能智能体权重分布**的扰动候选，而非固定高斯噪声。具体地，维护一个定长集合 \( S_{top} \)，存储训练过程中奖励最高的几个智能体参数；将其均值和标准差作为高斯分布 \( \Phi_{oriented} \)，从中采样扰动候选 \( \phi \)，然后按公式 \( \theta_t = \alpha \theta_{t-1} + (1-\alpha) \phi \) 更新当前权重（其中 \( \alpha \) 基于休眠比率动态调节）。该机制使得扰动候选包含任务相关信息，从而提供更有效的优化方向。

算法流程示意：在 MoE 骨干上执行标准 RL 更新（如 DrQ-v2），每隔一定步数进行一次任务导向扰动；同时 MoE 引入负载均衡损失（负熵）防止专家退化。

## 3. 实验设计
- **仿真 benchmark**：
  - **DeepMind Control Suite (DMC)**：Dog Stand、Dog Walk、Manipulator Bring Ball、Acrobot Swingup（Sparse）等，评价指标为 episode reward。
  - **Meta-World (MW)**：Assembly、Disassemble、Pick Place、Coffee Push（Sparse）、Soccer（Sparse）、Hammer（Sparse），评价指标为 success rate。
  - **Adroit**：Door、Hammer，评价指标为 success rate。
- **真实世界任务**（使用 Franka Panda 机械臂、RealSense D435 相机）：
  - 插销（三种形状）、线缆布线、桌面高尔夫。
- **对比方法**：DrM、DrQ-v2、ALIX、TACO，均为模型无关的视觉 RL 方法。实验中保持超参数一致，仅替换骨干网络与扰动机制。

## 4. 资源与算力
论文明确提到所有仿真和真实世界实验使用 **Nvidia RTX 3090 GPU**，但未给出具体 GPU 数量或总训练时长。在附录 E 中提供了不同方法在 Hopper Hop 任务上的 FPS 对比（MENTOR 约 37 FPS，DrM 约 55 FPS，DrQ-v2 约 78 FPS，ALIX 约 49 FPS，TACO 约 23 FPS），并指出真实世界任务中 MENTOR 由于更好的样本效率，实际训练时间更短（图14显示 DrM 需要更多小时才能达到相同性能）。

## 5. 实验数量与充分性
- **仿真实验**：在 12 个任务（DMC 4 个、MW 6 个、Adroit 2 个）上各进行 4 个随机种子实验，结果绘制均值与方差/范围。包含全任务对比（图6）。
- **消融实验**：
  - 仿真消融（图9）：在 Hopper Hop、Disassemble、Coffee Push、Hammer 上对比完整模型、移除任务导向扰动、移除 MoE、同时移除两者的版本，验证每个组件的贡献。
  - 真实世界消融（表1）：对比 MENTOR、MENTOR w/o MoE、DrM，以及使用预训练编码器的变体。
  - MoE 超参消融（图8）：专家数量与 top-k 的选择。
- **附加分析**：专家利用率热图（图15）、梯度冲突余弦相似度（图3、图13）、扰动候选性能（图5c）、抗干扰能力（附录 I）。
- **总体评价**：实验覆盖了多种任务类型（连续控制、稀疏奖励、多阶段、多任务）、多种评价维度（性能、样本效率、时间效率、鲁棒性），且消融设计合理，对比方法均为当前 SOTA，实验充分且客观。

## 6. 主要结论与发现
- MENTOR 在所有仿真任务和真实世界任务上均显著优于现有模型无关视觉 RL 方法。
- 在真实世界任务中，平均成功率达到 83%，而最强基线 DrM 仅 32%（同等训练时间内）。
- MoE 结构通过动态专家激活有效缓解了梯度冲突，尤其适用于多阶段或多子目标任务。
- 任务导向扰动相比随机噪声扰动能提供更具信息量的优化方向，加速收敛并保持更低的休眠比率。
- 充足的样本效率是缩小仿真-现实差距、实现真实世界从头训练 RL 的关键。

## 7. 优点
- **方法创新**：同时从架构（MoE）和优化（任务导向扰动）两个角度提升视觉 RL，二者互补，贡献清晰。
- **实验充分**：不仅覆盖多个仿真 benchmark，还完成了三个挑战性的真实世界任务，结果具有强说服力。
- **分析深入**：通过梯度冲突度量、专家利用率可视化、扰动候选性能分析等，提供了对方法内在机理的深入理解。
- **鲁棒性验证**：在真实世界实验和仿真中均展示了抗干扰能力（手动扰动或随机位置变化）。
- **代码与视频开源**：便于复现与后续研究。

## 8. 不足与局限
- **时间效率**：MoE 的朴素实现（所有专家计算）导致 FPS 低于部分基线（如 DrM），尽管样本效率优势弥补了部分差距，但仍有优化空间（如更高效的稀疏计算）。
- **任务与形态单一**：仅在单一机械臂（Franka Panda）上验证，且每个实验为单任务学习。论文指出未来工作可扩展到多任务或多机器人形态。
- **超参敏感性**：MoE 的专家数量、top-k 值、扰动相关超参（α_min、α_max、perturb interval）需要手动调优，虽然论文给出了推荐值，但未讨论泛化性。
- **真实世界任务奖励设计**：三个任务均有特定的手工奖励函数（如基于图像分类的线缆位置检测），限制了方法的即插即用程度。
- **缺乏与其他架构变体（如 Transformer 骨干）的对比**：仅对比了基于 CNN+MLP 的方法，未探讨 MoE 与其他先进骨干（如 ViT）的组合效果。

（完）
