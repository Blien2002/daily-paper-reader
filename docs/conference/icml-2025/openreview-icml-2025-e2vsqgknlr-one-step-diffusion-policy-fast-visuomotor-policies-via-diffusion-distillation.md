---
title: "One-Step Diffusion Policy: Fast Visuomotor Policies via Diffusion Distillation"
title_zh: 单步扩散策略：通过扩散蒸馏实现快速视觉运动策略
authors: "Zhendong Wang, Max Li, Ajay Mandlekar, Zhenjia Xu, Jiaojiao Fan, Yashraj Narang, Linxi Fan, Yuke Zhu, Yogesh Balaji, Mingyuan Zhou, Ming-Yu Liu, Yu Zeng"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=E2VsqgKNlr"
tags: ["query:vla"]
score: 7.0
evidence: 将扩散策略蒸馏为单步动作生成器，实现快速视觉运动控制
tldr: 针对扩散策略在机器人实时控制中的速度瓶颈，本文提出OneDP，通过知识蒸馏将预训练扩散策略压缩为单步动作生成器。该方法最小化KL散度以保持与原策略分布一致，在显著加速推理的同时保持了行为克隆性能。OneDP为端到端机器人操作的实时部署提供了高效方案。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1612, \"height\": 890, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1402, \"height\": 642, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1429, \"height\": 399, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1356, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1426, \"height\": 783, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 897, \"height\": 899, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1779, \"height\": 1292, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1767, \"height\": 2260, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1763, \"height\": 642, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1706, \"height\": 517, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-e2vsqgknlr/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1773, \"height\": 416, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1691, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1693, \"height\": 375, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1254, \"height\": 188, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1253, \"height\": 185, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 808, \"height\": 124, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 887, \"height\": 151, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-e2vsqgknlr/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 930, \"height\": 508, \"label\": \"Table\"}]"
motivation: 扩散策略迭代去噪过程速度慢，难以满足机器人实时控制需求。
method: 通过最小化KL散度，将预训练扩散策略蒸馏为单步动作生成器。
result: 显著加速了机器人控制任务的响应时间，同时保持与原始策略分布的对齐。
conclusion: 蒸馏方法有效平衡了扩散策略的质量与速度，适用于实时机器人操作。
---

## Abstract
Diffusion models, praised for their success in generative tasks, are increasingly being applied to robotics, demonstrating exceptional performance in behavior cloning. However, their slow generation process stemming from iterative denoising steps poses a challenge for real-time applications in resource-constrained robotics setups and dynamically changing environments.
In this paper, we introduce the One-Step Diffusion Policy (OneDP), a novel approach that distills knowledge from pre-trained diffusion policies into a single-step action generator, significantly accelerating response times for robotic control tasks. We ensure the distilled generator closely aligns with the original policy distribution by minimizing the Kullback-Leibler (KL) divergence along the diffusion chain, requiring only $2\%$-$10\%$ additional pre-training cost for convergence. We evaluated OneDP on 6 challenging simulation tasks as well as 4 self-designed real-world tasks using the Franka robot. The results demonstrate that OneDP not only achieves state-of-the-art success rates but also delivers an order-of-magnitude improvement in inference speed, boosting action prediction frequency from 1.5 Hz to 62 Hz, establishing its potential for dynamic and computationally constrained robotic applications. A video demo is provided at our project page, and the code will be publicly available.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：扩散模型在机器人行为克隆中表现出色（如 Diffusion Policy, Chi et al. 2023），但其生成过程需要数十到数百次迭代去噪，导致推理速度极慢（默认仅 1.49 Hz）。这在资源受限的机器人平台和动态变化环境中无法满足实时控制需求（如快速响应人为干扰）。
- **目标**：在不显著牺牲性能的前提下，将扩散策略加速到单步生成，使机器人能够快速反应并完成复杂任务。
- **整体含义**：提出 One-Step Diffusion Policy (OneDP)，通过知识蒸馏将预训练扩散策略压缩为单步动作生成器，推理速度提升约 42 倍（从 1.5 Hz 到 62 Hz），同时保持甚至超越原始策略的成功率，为扩散策略在实时机器人控制中的部署提供了高效方案。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：使用反向 KL 散度（Reverse KL Divergence）对齐预训练扩散策略分布 \(p_{\pi_\phi}\) 与单步生成器分布 \(p_{G_\theta}\)，通过最小化沿扩散链的期望 KL 散度进行蒸馏。
- **关键技术细节**：
  - **单步生成器**：定义 \(A_\theta = G_\theta(z, O)\)，其中 \(z\) 为高斯噪声，\(O\) 为观测图像。无需迭代去噪。
  - **蒸馏目标**：最小化 \(\mathbb{E}_{k\sim U}[D_{KL}(p_{G_\theta,k} \| p_{\pi_\phi,k})]\)，其梯度可转化为分数差损失：
    \[
    \nabla_\theta \mathbb{E} \left[ w(k) (s_{p_{G_\theta}}(A_k^\theta) - s_{p_{\pi_\phi}}(A_k^\theta)) \nabla_\theta A_k^\theta \right]
    \]
  - **两种变体**：
    - **OneDP-S（随机策略）**：引入辅助生成器评分网络 \(\pi_\psi\)，通过标准扩散训练更新 \(\psi\) 以估计 \(s_{p_{G_\theta}}\)，然后更新 \(\theta\)。
    - **OneDP-D（确定性策略）**：省略随机噪声 \(z\)，生成器变为 \(A_\theta = G_\theta(O)\)，此时 \(p_{G_\theta}\) 为 Dirac delta 函数，其显式分数可解析计算，无需辅助网络，简化训练。
  - **初始化**：生成器 \(G_\theta\) 和评分网络 \(\pi_\psi\) 均从预训练扩散策略复制权重，蒸馏只需额外 2%–10% 的训练代价即可收敛。
- **算法流程（文字说明）**：
  1. 预训练扩散策略 \(\pi_\phi\)。
  2. 初始化 \(G_\theta \leftarrow \pi_\phi\)，\(\pi_\psi \leftarrow \pi_\phi\)。
  3. 循环直到收敛：
     - 采样噪声 \(z\)，通过 \(G_\theta\) 生成动作样本 \(A_\theta\)。
     - 将 \(A_\theta\) 扩散到不同噪声水平 \(A_k^\theta\)。
     - 若为 OneDP-S，先按式 (6) 更新 \(\psi\)，再按式 (5) 更新 \(\theta\)；若为 OneDP-D，直接按式 (8) 更新 \(\theta\)。
  4. 推理时仅需单次前馈生成动作。

## 3. 实验设计：数据集、场景与对比方法

- **仿真实验**：使用 **Robomimic 基准**中的三个较难任务（Square、Transport、Tool Hang），每个任务包含两种人类演示变体（PH：熟练人类，MH：混合）。另加入 **PushT** 任务（推 T 形块到目标区域）。共 6 个任务。
- **真实世界实验**：使用 Franka Panda 机器人臂，设计四个任务：
  - **pnp-milk**：拾取牛奶盒放入固定盒子。
  - **pnp-anything**：拾取 11 种不同物体放入盒子。
  - **pnp-milk-move**：人为移动目标物体，测试动态响应。
  - **coffee**：操作咖啡机（拾取咖啡胶囊、放入支架、关闭盖子）。
- **对比方法**：
  - **Diffusion Policy (DP)**：使用 DDPM（100 步）和 DDIM（10 步、1 步）采样。
  - **Consistency Policy (CP)**：基于一致性轨迹模型（CTM），需 EDM 调度，训练 450 步。
- **评估指标**：成功率、任务完成时间、推理速度（NFE 和 wall-clock time）。

## 4. 资源与算力

- **硬件**：文中明确提到推理速度在本地 **NVIDIA V100 GPU** 上测量（表 5）。未说明训练使用的 GPU 数量和型号。
- **训练成本**：
  - 预训练 DP：1000 epochs。
  - 蒸馏 OneDP：仿真 20 epochs，真实世界 100 epochs，仅需 2%–10% 额外预训练成本。
  - 与 CP 相比，OneDP 收敛速度快约 20 倍（20 epoch vs 450 epoch）。
- **网络规模**：仿真实验中 DDPM 使用 256M 参数版本，EDM 使用 67M 参数版本（较小版本表现更好）；真实实验也采用 67M 参数。

## 5. 实验数量与充分性

- **仿真实验**：每个任务使用 **5 个训练种子** × **100 个不同初始条件** = 总计 500 次评估。报告平均成功率和标准差。实验覆盖 6 个难度递增的任务。
- **真实世界实验**：每个任务 **20 个预定初始位置**（pnp-milk-move 为 10 个轨迹）。每个算法使用最终 checkpoint（不挑选），分别评估成功率和完成时间。
- **消融实验**（附录 E）：探索生成器评分网络的学习率（网格搜索 1e-6 ~ 4e-5，最优 2e-5）和优化器设置（Adam β1=0 效果最佳）。
- **充分性判断**：实验设计较为全面，覆盖静态和动态环境、仿真和真实场景，与主流方法（DP、CP）公平对比，并报告多次重复的均值方差。但未涵盖长时域真实任务（如多阶段、长 horizon 操作），且缺少与更多蒸馏方法（如基于 GAN 的蒸馏）的对比。

## 6. 主要结论与发现

- **性能**：OneDP（尤其是随机版本 OneDP-S）在仿真 6 个任务上平均成功率达到 **0.843**，超过 DP（0.829）和 CP（0.672）；在真实世界 4 个任务上平均成功率 **0.98**，优于 DP 的 0.83。
- **速度**：推理速度从 DP 的 1.5 Hz 提升至 **62.5 Hz**，提升约 42 倍；任务完成时间缩短约 30%（例如 coffee 任务从 54.9 秒降至 29.8 秒）。
- **动态环境优势**：在人为干扰的 pnp-milk-move 任务中，OneDP 成功率 100%，而 DP 仅 80%（因推理慢导致滞后反应）。
- **蒸馏效率**：OneDP 仅需 20 epoch 蒸馏即可收敛，而 CP 需 450 epoch，且 OneDP 在 1 步生成下即达到或超过原 DP 性能。

## 7. 优点

- **原理简洁高效**：基于反向 KL 散度最小化，蒸馏过程自然且稳定。
- **单步生成无累积误差**：避免了迭代去噪中可能引入的累积错误，有时性能甚至微超原模型。
- **支持两种噪声调度**（DDPM 和 EDM）和两种策略变体（OneDP-S 和 OneDP-D），灵活适应不同需求。
- **训练代价低**：仅需 2%–10% 额外预训练成本，收敛速度远快于对比方法 CP。
- **真实场景验证充分**：在 Franka 机器人上设计 4 个真实任务，涵盖静态、多物体、动态干扰和精细操作，展示了实用性。

## 8. 不足与局限

- **长时域任务未覆盖**：论文明确指出未评估真实世界的长时域任务，限制了方法在复杂多阶段操作上的泛化性验证。
- **控制频率受限**：真实实验中为稳定将机器人操作频率限制在 20 Hz，未能完全发挥 OneDP 的 62 Hz 潜力，可能掩盖了其在更高频率下的优势或问题。
- **分布匹配方法非最优**：仅使用 KL 蒸馏，并未引入对抗性判别器或其他更先进的分布匹配技术（如 GAN 或 SiD），附录也承认“可能不是最优选择”。
- **对比方法局限性**：仅与 CP 和 DP 对比，未与更多蒸馏方法（如 progressive distillation、score distillation）或近期其他加速策略比较。
- **训练细节未完全披露**：未明确给出训练时的 GPU 数量、总 GPU 小时数等算力信息，可复现性稍弱。
- **消融实验较简略**：仅对学习率和优化器进行了消融，对于蒸馏损失函数设计、噪声调度选择等缺少深入分析。

（完）
