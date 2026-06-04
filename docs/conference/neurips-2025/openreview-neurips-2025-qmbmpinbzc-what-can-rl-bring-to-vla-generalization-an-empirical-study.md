---
title: What Can RL Bring to VLA Generalization? An Empirical Study
title_zh: RL能为VLA泛化带来什么？一项实证研究
authors: "Jijia Liu, Feng Gao, Bingwen Wei, Xinlei Chen, Qingmin Liao, Yi Wu, Chao Yu, Yu Wang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=qmBMPInbZC"
tags: ["query:vla"]
score: 9.0
evidence: 关于RL微调对VLA泛化的实证研究
tldr: VLA模型通常使用SFT训练，在分布偏移下易累积误差。该研究建立系统基准，全面比较RL与SFT微调对VLA泛化的影响。实验表明RL微调尤其在视觉变化和语义新指令上大幅提升鲁棒性。该工作为VLA训练策略提供了关键指导，推动具身智能的泛化研究。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1436, \"height\": 1064, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 800, \"height\": 319, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1454, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 653, \"height\": 345, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1443, \"height\": 358, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 506, \"height\": 322, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1442, \"height\": 308, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1445, \"height\": 770, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 618, \"height\": 331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1151, \"height\": 1288, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 778, \"height\": 491, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 779, \"height\": 488, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1445, \"height\": 315, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1112, \"height\": 905, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qmbmpinbzc/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1450, \"height\": 426, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-qmbmpinbzc/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1454, \"height\": 839, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qmbmpinbzc/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 700, \"height\": 175, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qmbmpinbzc/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1453, \"height\": 838, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qmbmpinbzc/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1425, \"height\": 607, \"label\": \"Table\"}]"
motivation: SFT训练VLA模型泛化不足，RL的潜在优势缺乏系统对比。
method: 构建VLA泛化基准，在视觉/语义/执行维度下比较RL与SFT微调。
result: RL微调显著提升VLA在多种分布偏移下的任务成功率。
conclusion: RL是增强VLA泛化能力的有效训练范式。
---

## Abstract
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. 
However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. 
To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **背景**：视觉-语言-动作（VLA）模型通过监督微调（SFT）训练，在分布偏移（如新物体、新背景、新指令）下容易产生累积误差，限制其泛化能力。
- **动机**：强化学习（RL）通过试错直接优化任务目标，理论上可以克服SFT的缺陷，但缺乏对RL微调VLA泛化能力的系统理解。本文旨在回答：“相比SFT，RL能为VLA泛化带来哪些具体的优势？”
- **整体含义**：建立了一个针对VLA泛化的综合基准，并系统比较了RL与SFT在视觉、语义、执行三个维度上的泛化表现，揭示了RL在语义理解与执行鲁棒性上的显著优势。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：以OpenVLA模型为基座，使用RL（特别是PPO）进行微调，通过在线交互和奖励信号引导策略学习，从而提升在分布外（OOD）场景下的泛化能力。
- **关键技术细节**：
  - **模型架构**：基于OpenVLA（视觉编码器SigLIP+DINOv2 + Llama-2 7B语言骨干），采用LoRA（秩r=32）微调所有线性层。
  - **RL算法选择**：比较PPO、GRPO、DPO。PPO表现最佳，GRPO受POMDP非平稳性影响，DPO受稀疏奖励和分布偏移影响。
  - **高效PPO配方**：
    - **共享actor-critic骨干**：在动作预测后的第一个token位置添加一个轻量级3层MLP价值头，与actor共享Transformer骨干（减少35%时间，83%显存）。
    - **VLA warm-up**：先使用140条运动规划器生成的演示轨迹进行SFT热启动，可减少约50%的环境交互步骤。
    - **最小PPO epoch**：设置epoch=1，避免过拟合和额外计算开销。
- **算法流程**：
  - SFT：最小化演示数据上的交叉熵/回归损失（行为克隆）。
  - RL（PPO）：在线收集轨迹，使用广义优势估计（GAE）计算优势，通过剪切重要性采样更新策略，同时最小化价值函数MSE损失。

### 3. 实验设计：数据集/场景、benchmark、对比方法
- **任务**：基于ManiSkill模拟器的拾取放置任务（Pick-and-Place），机器人使用8-DoF WidowX-250S臂，输入640×480 RGB图像和自然语言指令，输出末端执行器delta和夹爪信号。奖励稀疏（抓取0.1，持续抓取0.1，放置成功1.0）。
- **泛化维度**：
  - **视觉**：未见表面、动态纹理/噪声（弱/强）。
  - **语义**：未见物体/容器、新指令短语、多物体区分、干扰容器等。
  - **执行**：物体/容器位置偏移、机器人初始姿态变化、任务中物体位置重摆。
- **数据集**：SFT使用运动规划器（MPLib）自动生成的16k轨迹（约1.26M步），并过滤掉静止动作（约1/3被移除）。RL在模拟环境中在线交互。
- **对比方法**：
  - SFT基线：用不同规模（0.5k~64k）演示数据训练至收敛，选择16k作为最强SFT基线。
  - RL方法：PPO（含ORZ变体）、GRPO、DPO（TPO版本）。最终主要对比16k SFT vs PPO。
  - 消融：PPO的warm-up、epoch数量、LoRA秩、温度等。
- **额外实验**：对开合铰接物体任务（使用Franka Panda臂）进行扩展验证；初步的sim-to-real真实机器人实验。

### 4. 资源与算力
- 文中明确指出：**单张NVIDIA A100 GPU**上训练约**42小时**可收敛（RL PPO微调）。SFT训练也使用相同GPU。
- 具体硬件细节（如CPU、内存等）未详细说明。

### 5. 实验数量与充分性
- **实验数量**：大量实验涵盖：
  - 三个泛化维度共**超过14种OOD场景**（每种重复3个随机种子）。
  - 主实验（Fig. 6-7）包括训练曲线、成功率和性能下降率。
  - 消融实验：warm-up、epoch、LoRA秩、温度、critic设计、算法比较（PPO/GRPO/DPO）。
  - 扩展任务（铰接物体）和sim-to-real初步验证（30个真实试次）。
- **充分性与公平性**：
  - 所有方法使用相同LoRA配置，SFT基线也进行充分训练至收敛。
  - 报告了均值和标准差，使用相同种子控制随机性。
  - 对比方法（DPO、GRPO）进行了公平调参，但未达到PPO的性能。
  - 局限性：仅在仿真环境中的拾取放置任务为主，其他任务作为补充。

### 6. 论文的主要结论与发现
- **RL（PPO）在语义和执行维度上显著优于SFT**：平均OOD成功率提升约42.6%（在未见物体/表上），性能下降率更低。
- **视觉维度两者相当**：RL和SFT在视觉噪声/纹理变化上表现相似，均未超过训练中随机化的程度。
- **PPO比DPO和GRPO更适合VLA微调**：DPO受稀疏奖励和分布偏移困扰，GRPO因POMDP非平稳性而不稳定。
- **高效PPO配方有效**：共享actor-critic、warm-up、单epoch训练可在42小时内收敛。
- **RL在sim-to-real中优于SFT**：初步真实实验（Franka Panda）显示RL抓取成功率0.43 vs SFT 0.10。

### 7. 优点：方法或实验设计上的亮点
- **系统性**：首次对VLA泛化的三个关键维度（视觉、语义、执行）进行系统比较，定义清晰的OOD场景。
- **实用配方**：提出高效的PPO微调方法（共享骨干、warm-up、单epoch），便于复现和部署。
- **公平对比**：控制LoRA、数据量等变量，同时测试多种RL算法（PPO、DPO、GRPO），结论可靠。
- **扩展验证**：在开合铰接物体任务和真实机器人上验证了结论的迁移性。
- **开源**：提供项目页和代码，促进后续研究。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制
- **任务局限**：主要实验仅针对拾取放置任务，虽然扩展了铰接物体任务，但整体动作空间和任务复杂度有限。
- **数据偏差**：SFT演示由运动规划器生成，行为模式相对单一，可能不能完全代表人类演示的多样性。
- **仿真环境**：所有主要实验在ManiSkill模拟中进行，sim-to-real仅在初步尝试，未做大量的域随机化或实际部署验证。
- **算法局限**：仅测试了三种RL算法，更多离线/在线方法（如SAC、DQfD）未涉及；PPO的参数量敏感（LoRA秩32是固定值）。
- **计算资源**：仅使用单卡A100，未探索多卡分布式训练对效率的影响。
- **奖励设计**：使用稀疏奖励，未尝试更密集的奖励信号，可能影响RL收敛速度。
- **泛化边界**：仅测试了有限数量的OOD分布（如16个物体，9个未见），实际世界中泛化能力可能仍受限于训练分布。

（完）
