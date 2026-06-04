---
title: "FOUNDER: Grounding Foundation Models in World Models for Open-Ended Embodied Decision Making"
title_zh: FOUNDER：将基础模型嵌入世界模型以实现开放式具身决策
authors: "Yucen Wang, Rui Yu, Shenghua Wan, Le Gan, De-Chuan Zhan"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=UTT5OTyIWm"
tags: ["query:vla"]
score: 8.0
evidence: 结合基础模型与世界模型的具身决策
tldr: 基础模型擅长泛化但缺乏动态建模，世界模型擅长模拟但泛化性有限。FOUNDER框架将两者结合，通过学习映射函数将基础模型表示对齐到世界模型状态空间，使智能体能够在想象中进行目标导向的策略学习。该方法无需外部奖励信号，在多个具身环境中的开放任务上展现了更强的适应性和任务完成能力。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1758, \"height\": 488, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1774, \"height\": 509, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 858, \"height\": 457, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1771, \"height\": 464, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1774, \"height\": 342, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1382, \"height\": 545, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1753, \"height\": 366, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-utt5otyiwm/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1753, \"height\": 419, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1583, \"height\": 915, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 915, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1783, \"height\": 1231, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1193, \"height\": 1074, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1247, \"height\": 453, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1786, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1603, \"height\": 364, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-utt5otyiwm/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 922, \"height\": 1858, \"label\": \"Table\"}]"
motivation: 基础模型具备广泛知识但缺少环境动态建模能力，世界模型擅长模拟但泛化性弱，两者互补。
method: 学习从外部观测到世界模型状态空间的映射，使得能够通过想象实现目标条件策略学习，无需奖励信号。
result: 在多个具身环境中的开放任务上，FOUNDER取得了更高的成功率和更快的适应速度。
conclusion: 该工作验证了基础模型与世界模型有效融合的可行性，为开放式具身智能体设计提供了新范式。
---

## Abstract
Foundation Models (FMs) and World Models (WMs) offer complementary strengths in task generalization at different levels. In this work, we propose FOUNDER, a framework that integrates the generalizable knowledge embedded in FMs with the dynamic modeling capabilities of WMs to enable open-ended task solving in embodied environments in a reward-free manner. We learn a mapping function that grounds FM representations in the WM state space, effectively inferring the agent's physical states in the world simulator from external observations. This mapping enables the learning of a goal-conditioned policy through imagination during behavior learning, with the mapped task serving as the goal state. Our method leverages the predicted temporal distance to the goal state as an informative reward signal. FOUNDER demonstrates superior performance on various multi-task offline visual control benchmarks, excelling in capturing the deep-level semantics of tasks specified by text or videos, particularly in scenarios involving complex observations or domain gaps where prior methods struggle. The consistency of our learned reward function with the ground-truth reward is also empirically validated. Our project website is https://sites.google.com/view/founder-rl.

---

## 论文详细总结（自动生成）

## 论文中文总结

### 1. 核心问题与整体含义（研究动机和背景）
- **问题**：基础模型（FM）如视觉语言模型具备丰富的先验知识和任务泛化能力，但缺乏对具体环境动态的建模能力；世界模型（WM）擅长学习环境动态和生成可控轨迹，但缺乏高层语义理解，且通常需要自定义奖励函数才能用于具体任务。如何将两者的互补优势（FM的高层泛化知识与WM的低层动态建模）结合，以实现在无外在奖励信号下解决开放式、多模态指定的具身任务，是一个尚未充分探索的问题。
- **整体含义**：论文提出 FOUNDER 框架，通过将 FM 生成的任务表示（文本或视频）映射为 WM 中的可操作目标状态，使智能体能够在想象中执行模型-based 的目标条件强化学习（GCRL），从而无需手动设计奖励即可完成多样化任务。这为开放式具身决策提供了一个通用范式。

### 2. 方法论
- **核心思想**：利用一个可学习的映射函数，将 FM 表示（来自文本或视频嵌入）对齐到 WM 的潜在状态空间，然后将该映射状态作为目标，通过预测时间距离（Temporal Distance）作为奖励信号，在 WM 中进行目标条件策略学习。
- **关键技术细节**：
  - **世界模型学习**：基于 DreamerV3 的 RSSM 结构，从离线数据集学习图像观测和动作的潜在动力学（编码器、转移模型、解码器），不含奖励模型。
  - **映射函数学习**：
    - 使用离线轨迹中的连续观测序列（例如 8 帧）通过 VLM（InternVideo2）生成嵌入 \( e_t \)，同时通过已训练的 WM 编码得到对应时间步的潜在状态 \( z_t \)，形成配对数据。
    - 学习映射函数 \( Q_\psi \)，最小化 \( Q_\psi(e_t) \) 与 \( z_t \) 之间的 KL 散度，并加入自编码器重构损失（从映射状态重构 \( e_t \)），使得映射结果能保留环境动态信息。
    - 对于新任务，将提示嵌入 \( e_g \) 通过 \( Q_\psi \) 映射为目标状态 \( z_g \)。
  - **行为学习**（目标条件策略学习）：
    - 训练时间距离预测器 \( D_\theta \)，预测两个 WM 状态之间的时间步数（轨迹内正样本预测归一化距离，跨轨迹负样本预测最大距离 1）。
    - 在 WM 中想象轨迹，每个时间步的奖励 \( r_D(z_t, z_g) = -D_\theta(z_t, z_g) \)。
    - 使用 Dreamer-style Actor-Critic 学习目标条件策略 \( \pi(a_t \mid z_t, z_g) \) 和值函数。
- **算法流程**（文字说明）：
  1. 预训练：离线数据 → 训练 WM → 编码得到状态 → 训练映射函数（KL + 重构） → 训练时间距离预测器。
  2. 行为学习：给定任务提示 → VLM 编码 → 映射为目标状态 → 在 WM 中想象轨迹 → 用时间距离奖励训练策略。

### 3. 实验设计
- **数据集/场景**：
  - **DeepMind Control Suite (DMC)**：Cheetah, Walker, Quadruped, Stickman 四种体型的运动任务（Stand, Walk, Run, Flip）。
  - **Franka Kitchen**：操作任务（light, slide, microwave, burner, kettle）。
  - **Minecraft**（Minedojo 基准）：Hunt Cow, Shear Sheep, Chop Trees, Milk Cow, Hunt Sheep 等 5 个任务。
- **基准与比较方法**：
  - 主要对比：GenRL（序列匹配）、WM-CLIP（反向映射+FM空间相似度奖励）、GenRL-TempD（在 GenRL 中改用时间距离）、FOUNDER w/o TempD（使用余弦相似度奖励的 FOUNDER 变体）。
  - 额外对比：IQL, TD3+BC, HILP 等模型免费方法；在 Minecraft 中还包括 MineCLIP-IQL（使用预训练 MineCLIP 作为奖励的 IQL）。
- **设置**：所有方法使用同一个 VLM（InternVideo2），离线数据集不包含奖励，行为学习阶段限制 50K 步更新（小步数适应）。

### 4. 资源与算力
- 文中明确说明：所有实验在**单张 RTX 3090 GPU** 上完成。
- 预训练时间：
  - FOUNDER（WM + 映射 + 时序预测器）：约 3 天（72 小时）。
  - GenRL（MFWM）：约 5 天（120 小时）。
  - HILP：约 30 小时。
- 下游任务微调（50K 步）：每任务不足 5 小时。
- 模型免费方法如 TD3 从头训练约 7 小时。
- 未提及 GPU 数量（仅单卡），也未提供总算力（如 GPU-hours）的完整汇总。

### 5. 实验数量与充分性
- **实验数量**：
  - 语言任务：DMC + Kitchen 共 19 个任务（表1）。
  - 跨体视频任务：12 个（6 种体对组合 × 2 种动作）。
  - 跨视角视频任务：4 个 Kitchen 视角 + 5 个 DMC 视角（图2-4）。
  - 奖励函数评估：7 个任务上的 6 项指标（表2）。
  - Minecraft：5 个任务（图5）。
  - 消融：FOUNDER w/o TempD, GenRL-TempD, 以及多种基线的对比。
- **充分性与公平性**：
  - 实验设计较全面，覆盖了同域语言、跨域视频、真实世界视频、奖励一致性、更复杂的 Minecraft 环境。
  - 所有对比方法使用相同 VLM，相同离线数据，相同训练步数。
  - 消融实验明确展示了时间距离、映射方式、基线各部件的贡献。
  - 限于算力未做大规模超参数扫描，但关键结果均有多次 seed 重复（4-6 seed）。

### 6. 主要结论与发现
- FOUNDER 在大多数任务上取得最佳或并列最佳性能，尤其在**跨体（Cheetah与Walker/Stickman转换）和跨视角**任务中显著优于 GenRL 等基线，表明其能够捕捉深层任务语义而非仅视觉特征。
- 时间距离奖励信号有效避免了奖励破解问题（如 FOUNDER w/o TempD 在动态任务中模拟视觉外观但无法推进）。
- 奖励函数评估中，FOUNDER 的伪奖励与真实奖励具有最高相关性（Corr=0.54）和最低遗憾（Regret=0.07），且具有完美精度（1.0），说明其可靠性。
- 在 Minecraft 中，FOUNDER 在 3/5 任务上超越或匹配 MineCLIP-IQL（使用互联网预训练奖励模型的 oracle 基线），证明其有效利用有限环境数据泛化。

### 7. 优点
- **方法创新性**：首次将 FM 表示以物理状态对齐的方式嵌入 WM，通过时间距离实现无奖励 GCRL，避免了 GenRL 中耗时的序列到序列匹配和视觉风格传输。
- **实验全面**：涵盖多种形态、多个域、多种任务类型（语言、视频、跨域）、奖励一致性验证，以及复杂 Minecraft 环境，充分展示通用性。
- **高效性**：相比 GenRL，预训练时间减少约 40%，下游微调时间相当但性能更高。
- **开源与可复现**：提供项目网站和代码，便于后续研究。

### 8. 不足与局限
- **对离线数据的依赖**：映射函数和 WM 仅基于目标环境的离线数据，如果任务提示中的语义（如特定对象或行为）未在数据中充分出现，映射可能失败。性能受限于离线数据的质量和覆盖度。
- **短时任务为主**：实验主要涉及短齐次任务（数十步），未充分评估长序列任务（如需要子任务分解的场景）。
- **未处理跨域视频中的复杂视觉差异**：虽然跨体/跨视角实验表现好，但论文仅使用了 8 帧视频（受 VLM 限制），对于更复杂的动作可能信息不足。
- **计算资源细节不完整**：仅报告单卡 RTX 3090 的训练时间，但未给出总 GPU-hours、显存占用等，不利于精确复现与比较。
- **应用限制**：当前方法需要预训练 VLM，且映射函数仅针对特定环境训练；迁移到全新环境可能需要重新收集数据和训练。未来应结合更多数据采集策略或融入真实视频训练。

（完）
