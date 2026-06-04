---
title: "DexFlyWheel: A Scalable and Self-improving Data Generation Framework for Dexterous Manipulation"
title_zh: DexFlyWheel：面向灵巧操纵的可扩展自改进数据生成框架
authors: "Kefei Zhu, Fengshuo Bai, YuanHao Xiang, Yishuai Cai, Xinglin Chen, Ruochong Li, Xingtao Wang, Hao Dong, Yaodong Yang, Xiaopeng Fan, Yuanpei Chen"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=a49F7EAm6l"
tags: ["query:vla"]
score: 6.0
evidence: 用于灵巧操纵的可扩展自改进数据生成框架
tldr: 灵巧操纵依赖多样化的高质量数据，但现有数据收集方法可扩展性差。本文提出DexFlyWheel，一个自改进的数据生成框架，通过模仿学习和残差强化学习的闭环迭代不断丰富数据多样性。从少量种子演示出发，每轮循环扩充数据集并提升策略性能。实验表明生成的数据可用于训练泛化性强的灵巧操纵策略，缓解数据稀缺问题。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1431, \"height\": 830, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1374, \"height\": 924, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1435, \"height\": 463, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 705, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 711, \"height\": 404, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 872, \"height\": 651, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 869, \"height\": 574, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 870, \"height\": 561, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-a49f7eam6l/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 864, \"height\": 716, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 649, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1440, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1447, \"height\": 168, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1453, \"height\": 205, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1145, \"height\": 1150, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1132, \"height\": 1028, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1456, \"height\": 209, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 805, \"height\": 304, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1451, \"height\": 263, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1449, \"height\": 301, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-a49f7eam6l/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1455, \"height\": 495, \"label\": \"Table\"}]"
motivation: 灵巧操纵数据集稀缺且多样性不足，人工收集成本高。
method: 提出自改进循环框架，结合模仿学习和残差强化学习迭代生成多样化数据。
result: 生成的数据集有效提升了灵巧操纵策略的成功率和泛化能力，尤其在未见物体上。
conclusion: DexFlyWheel为灵巧操纵提供了一种高效、可扩展的数据生成方案，有助于降低对人工数据的依赖。
---

## Abstract
Dexterous manipulation is critical for advancing robot capabilities in real-world applications, yet diverse and high-quality datasets remain scarce. Existing data collection methods either rely on human teleoperation or require significant human engineering, or generate data with limited diversity, which restricts their scalability and generalization. In this paper, we introduce DexFlyWheel, a scalable data generation framework that employs a self-improving cycle to continuously enrich data diversity. Starting from efficient seed demonstrations warmup, DexFlyWheel expands the dataset through iterative cycles. Each cycle follows a closed-loop pipeline that integrates Imitation Learning (IL), residual Reinforcement Learning (RL), rollout trajectory collection, and data augmentation. Specifically, IL extracts human-like behaviors from demonstrations, and residual RL enhances policy generalization. The learned policy is then used to generate trajectories in simulation, which are further augmented across diverse environments and spatial configurations before being fed back into the next cycle. Over successive iterations, a self-improving data flywheel effect emerges, producing datasets that cover diverse scenarios and thereby scaling policy performance. Experimental results demonstrate that DexFlyWheel generates over 2,000 diverse demonstrations across four challenging tasks. Policies trained on our dataset achieve an average success rate of 81.9\% on the challenge test sets and successfully transfer to the real world through digital twin, achieving a 78.3\% success rate on dual-arm lift tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

灵巧操纵（dexterous manipulation）对于机器人在现实世界中执行复杂任务至关重要，但高质量且多样化的数据集非常稀缺。现有数据收集方法存在显著瓶颈：人工遥操作需要大量人力且局限于实验室环境；基于仿真的方法（如纯强化学习、规划方法或重放机制）往往难以处理灵巧手的高维动作空间和复杂接触动力学，生成的数据多样性不足或质量较低。这限制了可泛化灵巧操纵策略的训练。因此，论文旨在提出一种可扩展、自改进的数据生成框架，以缓解灵巧操纵数据稀缺问题，为训练通用化策略奠定基础。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- 提出 **DexFlyWheel**，一个两阶段的自改进数据生成框架。
- 关键洞察：操纵不同物体通常只需对轨迹进行微小调整，因此可将人类演示视为强行为先验，而非简单的重放数据。
- 通过“模仿学习（IL）+ 残差强化学习（residual RL）”结合数据增强，形成迭代飞轮，不断扩展数据多样性并提升策略泛化能力。

### 关键技术细节
1. **预热阶段（Warm-up Stage）**：
   - 使用 VR 遥操作（Apple Vision Pro）收集每个任务仅一个种子演示 \( d_{\text{seed}} \)。
   - 通过多维度数据增强模块 \( \mathcal{A}_{\text{EP}} \)（基于 MimicGen 扩展）对种子演示进行环境、空间变化增强，生成初始数据集 \( D_1 \)。

2. **自改进数据飞轮阶段（Self-improving Data FlyWheel Stage）**：
   - 迭代进行 \( i = 1, 2, \ldots, n-1 \) 轮，每轮包括四个步骤：
     - **(1) 基策略训练**：在数据集 \( D_i \) 上训练扩散策略（diffusion-based policy）作为基策略 \( \pi_{\text{base}}^i \)，学习人类行为。
     - **(2) 残差策略训练**：在冻结的基策略之上，使用 SAC 算法训练残差策略 \( \pi_{\text{res}}^i \)，输出动作修正 \( \Delta a \)，并通过渐进式混合策略 \( \pi_{\text{combined}}^i = \pi_{\text{base}}^i + \alpha \cdot \pi_{\text{res}}^i \) 实现泛化。
     - **(3) 展开轨迹收集**：在仿真中部署组合策略，在随机物体配置下执行 rollout，并筛选成功轨迹得到 \( D_i^O \)。
     - **(4) 数据增强**：对 \( D_i^O \) 再次应用 \( \mathcal{A}_{\text{EP}} \) 进行环境和空间增强，得到下一轮数据集 \( D_{i+1} \)。

3. **动作空间**：动作包括末端执行器 6D 位姿和手部目标关节角；状态包括视觉、物体状态和机器人本体感知。

## 3. 实验设计

### 数据集/场景
- **仿真平台**：OmniGibson，提供真实渲染。
- **任务**：四个灵巧操纵任务：
  - 单臂：Grasp（抓取并提升 >0.2m）、Pour（倾倒物体到容器）
  - 双臂：Lift（协作提升 >0.15m）、Handover（手递手传递）
- **机器人**：单臂使用 Franka Panda + Inspire 灵巧手；双臂使用 RealMan RM75-6F + PsiBot G0-R 手。
- **场景多样性**：共 80 个不同物体（逐步扩展：从 1 个到 20+），12 种环境（光照、桌面外观变化），空间位姿变化。
- **迭代轮次**：\( i = 1,2,3 \)，分别生成 20、100、500 条轨迹。
- **测试集**：
  - 多因素泛化测试集 \( T_{\text{OEP}} \)：包含 40 个未见过的场景配置（物体、环境、空间同时变化）。
  - 物体泛化测试集 \( T_O(i) \)：评估在特定物体上的成功率。

### Benchmark 和对比方法
对比方法包括：
- **Human Demo (Default)**：固定场景下 20 条人类演示。
- **Human Demo (Enhanced)**：多样场景下 20 条演示。
- **DexMimicGen (Default)**：基于重放和编辑的代表性数据生成方法，与 DexFlyWheel 同种子数据。
- **DexMimicGen (Enhanced)**：给予 10 条多样人类演示（10×数据优势）。
- **w/o Res**：移除残差策略的消融模型。
- **w/o AEP**：移除数据增强模块的消融模型。
- **w/o Res + w/o AEP**：仅基策略的最小配置。

### 评估指标
- **数据多样性**：物体数（O）、环境数（E）、位姿数（P）、总场景配置数、轨迹数。
- **泛化性能**：成功率（SR），报告 5 次独立运行的平均值 ± 标准差。

## 4. 资源与算力

论文明确说明了：
- **基策略训练**：8 块 NVIDIA A100 GPU。
- **残差策略训练**：单块 NVIDIA RTX 4090 GPU。
- **训练时长**：
  - 基策略（IL）：每次迭代约 5 小时 40 分钟。
  - 残差策略（RL）：每次迭代约 6 小时 30 分钟。
  - 三轮迭代总训练时间约 30 小时。
- **数据生成时间**：每轨迹 15 秒；收集 500 条成功轨迹约 2.4 小时（单 RTX 4090）。

## 5. 实验数量与充分性

- **任务覆盖**：4 个灵巧操纵任务（单臂和双臂），涵盖抓取、倾倒、协同提升、传递。
- **迭代轮次**：默认 3 轮，并提供第 4、5 轮的扩展实验（表 7）。
- **消融实验**：分别移除残差策略、数据增强模块，进行完整消融分析（图 4）。
- **与基线对比**：与 4 种基线方法（人类演示、DexMimicGen 等）在相同测试集上比较成功率。
- **泛化性验证**：测试了物体数量（从 1 到 20+）、环境数量（1 到 12）、位姿数量（1 到 10+），以及多因素同时变化。
- **真实世界部署**：在双臂真实机器人上评估 Lift 和 Handover 任务（各 20 条轨迹 × 3 轮）。
- **统计严谨性**：所有成功率报告均基于 5 次独立运行的平均值和标准差。

总体而言，实验设计较为充分、客观，覆盖了数据集多样性、策略泛化、消融、真实迁移等维度，且对比基线合理。

## 6. 论文的主要结论与发现

1. **数据飞轮效应成立**：随迭代进行，数据集多样性显著提升（物体数从 1 增加到 20，场景配置从 9.5 增加到 2040），策略成功率从 16.5% 提升至 81.9%（多因素泛化测试）。
2. **残差策略有效提升泛化**：在物体泛化测试上，残差策略平均提升成功率 32.1%。
3. **优于基线方法**：DexFlyWheel 在四个任务上的平均成功率（81.9%）远高于人类演示（13.4%）和 DexMimicGen（45.2%），且数据生成时间更短（2.4h vs 4.4h/12.5h）。
4. **真实世界可迁移**：通过数字孪生，双臂 Lift 任务真实成功率达 78.3%，Handover 达 63.3%。
5. **高效率**：仅需单条种子演示即可生成 500+ 条成功轨迹，人力成本极低。

## 7. 优点

- **新颖的数据飞轮设计**：将 IL 与残差 RL 结合，实现自改进的数据生成，解决了传统重放方法无法探索新策略的局限。
- **极高的数据生成效率**：仅需单条人类演示，迭代后可生成 2000+ 条覆盖多场景的轨迹，人力成本极低。
- **优秀的泛化能力**：在物体、环境、空间三维度上均展现强泛化，尤其能处理几何形状差异大的物体。
- **仿真到真实迁移成功**：通过数字孪生实现 zero-shot 迁移，展示了实用价值。
- **全面的消融实验**：明确验证了残差策略和数据增强两个模块的贡献。
- **代码与数据开源**：提供了可复现性保障。

## 8. 不足与局限

- **依赖手工奖励函数**：残差 RL 阶段仍需要为每个任务手工设计奖励函数，限制了框架的自动化程度。
- **缺乏触觉反馈**：当前仿真和策略均未使用触觉传感器，对于需要精细接触力控制的任务可能受限。
- **物体泛化范围有限**：论文承认，对于需要完全不同操纵策略的任务（如布料折叠、打结、精密装配），“微小调整”假设可能不成立，泛化能力有待验证。
- **扩展迭代收益递减**：实验显示从第 3 轮后性能提升趋于平缓（如 Grasp 从 90.0% 到 93.2%），可能存在边际效应，需考虑计算成本与收益的平衡。
- **仅测试了四类任务**：缺乏对更复杂长时域或接触密集型任务的验证。
- **仿真与真实之间的差距**：真实世界成功率（78.3%/63.3%）低于仿真（79.4%/72.5%），仍存在 sim-to-real gap。

（完）
