---
title: Latent Diffusion Planning for Imitation Learning
title_zh: 面向模仿学习的潜在扩散规划
authors: "Amber Xie, Oleh Rybkin, Dorsa Sadigh, Chelsea Finn"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=vhACnRfuYh"
tags: ["query:vla"]
score: 7.0
evidence: 用于视动任务的潜在扩散规划
tldr: 模仿学习通常需要大量专家演示。LDP提出潜在扩散规划框架，将规划与逆动力学模型分离，在潜在空间中操作。该规划器可利用无动作演示，逆动力学模型可利用次优数据，从而降低对专家数据的依赖。在多个复杂机器人操作任务上，LDP在数据效率方面显著优于现有方法，为数据高效的模仿学习提供了新思路。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-vhacnrfuyh/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1778, \"height\": 645, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vhacnrfuyh/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 860, \"height\": 939, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vhacnrfuyh/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 861, \"height\": 206, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vhacnrfuyh/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 415, \"height\": 348, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vhacnrfuyh/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 860, \"height\": 831, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1491, \"height\": 445, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1490, \"height\": 529, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 594, \"height\": 277, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 865, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1518, \"height\": 213, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 995, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 993, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1259, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1199, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vhacnrfuyh/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 876, \"height\": 498, \"label\": \"Table\"}]"
motivation: 现有模仿学习方法通常需要大量专家演示，数据效率低。
method: 在VAE学习的潜在空间上，分别训练扩散规划器和逆动力学模型，前者可无动作演示学习，后者可利用次优数据。
result: 在多个机器人操作基准上，LDP以更少专家演示达到或超越基线方法的性能。
conclusion: LDP验证了潜在扩散规划在提高模仿学习数据效率方面的有效性。
---

## Abstract
Recent progress in imitation learning has been enabled by policy architectures that scale to complex visuomotor tasks, multimodal distributions, and large datasets. However, these methods often rely on learning from large amount of expert demonstrations.
To address these shortcomings, we propose Latent Diffusion Planning (LDP), a modular approach consisting of a planner which can leverage action-free demonstrations, and an inverse dynamics model which can leverage suboptimal data, that both operate over a learned latent space. First, we learn a compact latent space through a variational autoencoder, enabling effective forecasting of future states in image-based domains. Then, we train a planner and an inverse dynamics model with diffusion objectives. By separating planning from action prediction, LDP can benefit from the denser supervision signals of suboptimal and action-free data.
On simulated visual robotic manipulation tasks, LDP outperforms state-of-the-art imitation learning approaches, as they cannot leverage such additional data.

---

## 论文详细总结（自动生成）

# 论文总结：Latent Diffusion Planning for Imitation Learning

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：当前模仿学习（Imitation Learning）方法，如 Diffusion Policy，严重依赖大量专家演示数据。然而，收集高质量专家演示耗时且昂贵，而次优数据（如失败轨迹）和无动作数据（如人类视频）更容易获取，但现有方法无法有效利用这些数据。
- **动机**：希望通过分离规划（预测未来状态）与动作预测，使模型能够从不同来源的数据中获益，从而降低对专家演示数量和质量的要求，提升数据效率。
- **整体含义**：本文提出了一种模块化框架——潜在扩散规划（LDP），该框架在学习的紧凑潜在空间上进行规划与动作推断，可同时利用无动作演示和次优数据，在少专家演示场景下显著优于现有模仿学习方法。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：将模仿学习分解为两个独立模块：（1）**规划器**：基于当前潜在状态预测未来一段时间的潜在状态序列；（2）**逆动力学模型（IDM）**：根据相邻潜在状态对预测动作。两者均使用扩散模型（DDPM），并在VAE学习的潜在空间（latent space）上操作。
- **关键技术细节**：
  - **潜在空间学习**：使用β-VAE对图像进行编码，得到紧凑的潜在表示（例如16维），规划器和IDM均在此空间上工作。
  - **规划器**：采用基于条件U-Net的扩散模型，以当前潜在状态（图像潜在+本体感知）为条件，生成未来H个时间步的潜在状态序列。训练目标为标准扩散噪声预测损失。
  - **逆动力学模型**：使用轻量级MLPResNet架构的扩散模型，以相邻两个潜在状态为条件，预测对应的动作。训练目标同样为噪声预测损失。
  - **推理流程**：在每一控制周期，规划器进行DDPM采样得到未来潜在状态序列；然后对每对相邻状态，使用IDM采样得到动作；执行前H_a个动作，然后重规划（receding horizon control）。
  - **数据利用**：规划器可仅使用状态序列（无动作）进行训练；IDM可使用次优状态-动作对进行训练（无需专家标签）。两者结合可同时利用所有类型的数据。

## 3. 实验设计

- **数据集/场景**：
  - **模拟任务**：Robomimic的Lift、Can、Square，以及ALOHA模拟的Transfer Cube。均使用图像输入（64×64）。
  - **真实世界任务**：Franka Panda机器人拾取红色方块（Franka Lift），使用DROID设置和Oculus Quest 2遥操作。
- **基准水平**：在低专家演示数量条件下测试（例如Lift仅3个演示，Can/Square为100个，ALOHA Cube为25个），并提供次优数据（500条失败轨迹）和无动作数据（另外数十条演示中去除动作）。
- **对比方法**：
  - **行为克隆基线**：Diffusion Policy (DP)
  - **利用次优数据的基线**：Reward-Conditioned DP (RC-DP)、DP with Representation Learning (DP+Repr)、DP Pretrain+Finetune (DP PT+FT)
  - **利用无动作数据的基线**：DP with Video PreTraining (DP-VPT)（使用IDM标注无动作数据）
  - **视频规划基线**：UniPi (Open-Loop和Closed-Loop变体，即UniPi-OL和UniPi-CL)
  - **消融变体**：LDP层次化版本（LDP Hierarchical）、使用DINOv2嵌入的LDP等。

## 4. 资源与算力

- 原文未明确说明训练所用的GPU型号、数量及训练时长。仅在附录中给出了batch size、梯度步数等超参数（如规划器和IDM训练500k步，VAE训练300k步），但未提及硬件配置。

## 5. 实验数量与充分性

- **模拟实验**：在4个任务上评估，每个任务至少2个种子，报告成功率（成功/50轮）及其标准差。每个任务比较了10余种方法变体，包含主对比（表1和表2）和消融实验（表4、附录表5-7）。
- **真实世界实验**：在Franka Lift上进行了45次评估（3×3网格×5次），3个种子，较为充分。
- **消融实验**：包括层次化规划消融（LDP Hierarchical vs LDP）、使用DINOv2预训练嵌入消融、从预训练权重微调UniPi的消融等。
- **公平性**：所有方法均在相同的数据集划分、评估设置下比较，并报告了均值和方差。DP基线使用与原文一致的实现（Jax复现，验证与官方结果一致）。
- **结论**：实验设计较为全面，覆盖了不同任务、不同类型数据组合，对比充分，消融实验严谨，客观性良好。

## 6. 主要结论与发现

- LDP能够有效利用无动作数据和次优数据，在低专家演示场景下显著优于不能利用这些数据的最佳基线（如DP）。
- 当同时使用无动作数据和次优数据时，LDP在所有模拟任务上的成功率接近完美（平均0.95），而DP平均仅0.51。
- LDP优于基于视频规划的UniPi方法（包括闭环变体），原因在于：潜在空间规划效率高、支持密集预测和快速重规划，避免了视频生成的不稳定性和耗时问题。
- 层次化规划（稀疏预测）不如密集预测有效，说明密集潜在状态预测是LDP性能的关键。
- 在真实世界Franka Lift任务上，LDP同样优于DP，且通过添加无动作数据进一步提升。

## 7. 优点

- **模块化设计**：将规划与动作预测解耦，使每个模块可独立利用不同标签类型的数据，极大拓展了数据源的可用性。
- **潜在空间规划**：避免了对高维图像的直接生成，计算开销远低于视频生成方法，同时支持闭环控制与快速推理。
- **扩散模型的应用**：利用扩散模型的表达能力和多模态拟合能力，使得规划器和IDM均能捕捉复杂分布。
- **实验验证充分**：涵盖仿真和真实场景，与多种代表性基线进行对比，并做了多组消融分析，结果稳健。
- **易于扩展**：未来可进一步结合更先进的扩散模型架构或表示学习目标。

## 8. 不足与局限

- **潜在空间学习纯依赖重建**：VAE可能未学到对控制最有利的特征，未来可探索更优的表示学习目标（如任务相关、对比学习等）。
- **计算开销**：由于需要对状态进行扩散采样（而非仅动作），推理速度慢于直接动作预测方法。作者认为硬件进步可缓解。
- **未探索更先进扩散模型**：如DiT（Transformer-based）、流匹配等，在大数据场景下可能进一步提升性能。
- **实验未覆盖极大规模数据**：仅涉及单任务有限数据集（几百条轨迹），未见在多个任务联合训练或大规模真实数据集上的评估。
- **UniPi基线使用从零训练的视频模型**，可能限制了其表现；附录中尝试了预训练权重的微调，但效果改善有限。未来可考虑使用更强的视频生成模型。
- **未详细讨论真实世界数据收集成本**：虽然无动作数据收集更简便，但文中未量化实际收集代价。

（完）
