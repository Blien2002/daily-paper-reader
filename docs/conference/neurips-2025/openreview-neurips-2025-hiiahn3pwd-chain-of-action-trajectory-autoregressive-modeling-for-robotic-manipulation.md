---
title: "Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation"
title_zh: 动作链：机器人操作中的轨迹自回归建模
authors: "Wenbo Zhang, Tianrun Hu, Hanbo Zhang, Yanyuan Qiao, Yuchu Qin, Yang Li, Jiajun Liu, Tao Kong, Lingqiao Liu, Xiao Ma"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=hiiaHn3pWd"
tags: ["query:vla"]
score: 9.0
evidence: 端到端轨迹生成用于机器人操作
tldr: 传统的机器人操作策略仅前向预测下一步动作，缺乏全局规划能力。本文提出动作链（CoA），通过反向推理从任务关键帧开始自回归生成完整轨迹，实现全局到局部的动作约束。实验表明，CoA在多项复杂操作任务上显著优于现有方法，为端到端操作策略提供了新的思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 696, \"height\": 315, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1454, \"height\": 548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1154, \"height\": 570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1439, \"height\": 616, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1013, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 997, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1405, \"height\": 209, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 857, \"height\": 470, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hiiahn3pwd/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 506, \"height\": 471, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 649, \"height\": 593, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 615, \"height\": 502, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1452, \"height\": 663, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 338, \"height\": 214, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 313, \"height\": 193, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 735, \"height\": 647, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1356, \"height\": 677, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1450, \"height\": 190, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1312, \"height\": 2192, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 705, \"height\": 477, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 926, \"height\": 738, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 917, \"height\": 770, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 934, \"height\": 746, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1170, \"height\": 665, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hiiahn3pwd/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 500, \"height\": 554, \"label\": \"Table\"}]"
motivation: 现有操作策略仅前向预测，缺乏全局轨迹结构。
method: 提出CoA，利用反向推理从关键帧自回归生成完整轨迹。
result: 在多个操作任务上达到先进水平。
conclusion: 全局到局部结构有效提升了操作精度和长程规划能力。
---

## Abstract
We present Chain-of-Action (CoA), a novel visuomotor policy paradigm built upon Trajectory Autoregressive Modeling. Unlike conventional approaches that predict next step action(s) forward, CoA generates an entire trajectory by explicit backward reasoning with task-specific goals through an action-level Chain-of-Thought (CoT) process. This process is unified within a single autoregressive structure: (1) the first token corresponds to a stable keyframe action that encodes the task-specific goals;  and (2) subsequent action tokens are generated autoregressively, conditioned on the initial keyframe and previously predicted actions. This backward action reasoning enforces a global-to-local structure, allowing each local action to be tightly constrained by the final goal. To further realize the action reasoning structure, CoA incorporates four complementary designs: continuous action token representation; dynamic stopping for variable-length trajectory generation; reverse temporal ensemble; and multi-token prediction to balance action chunk modeling  with global structure. As a result, CoA gives strong spatial generalization capabilities while preserving the flexibility and simplicity of a visuomotor policy. Empirically, we observe that CoA outperforms representative imitation learning algorithms such as ACT and Diffusion Policy across 60 RLBench tasks and 8 real-world tasks.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：传统机器人操作策略（如 ACT、Diffusion Policy）采用**前向预测范式**，即基于当前观测逐帧预测下一步动作。这种模式缺乏对任务长期目标的全局引导，导致**累积误差**在长轨迹执行中不断放大，且模型在分布偏移（如物体位置变化）下泛化能力弱。
- **整体含义**：本文提出一种新的范式——**动作链（Chain-of-Action, CoA）**，通过**反向推理**从任务关键帧动作开始自回归生成整个轨迹，使每个局部动作都受最终目标约束，从而从根本上缓解前向预测的视野短浅问题，提升空间泛化和任务成功率。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：将轨迹生成视为一个反向自回归过程，首先预测一个稳定的**关键帧动作**（编码任务目标），然后在该关键帧条件上逆向生成之前的动作序列。公式表示为：
  - \( p(a_{1:T}|O) = p(a_T|O) \cdot p(a_{T-1}|a_T, O) \cdots p(a_1|a_{2:T}, O) \)
  - 其中 \( a_T \) 是关键帧动作，\( O \) 是观测（多视图RGB+机器人状态）。
- **关键技术细节**（四个必要设计）：
  1. **连续动作 token 表示**：避免离散化带来的分辨率损失，同时引入**潜在一致性损失**（\(\|\hat{x}_t - f_{\text{enc}}(a_t)\|\)）约束潜在空间的时序一致性。
  2. **局部动作建模（多 token 预测, MTP）**：在解码器最后 K 层使用多头预测，每个头预测未来一步动作，强制模型学习局部子轨迹的依赖关系，仅在训练时使用。
  3. **动态停止**：基于欧氏距离判断预测动作是否足够接近当前末端执行器状态，从而在连续动作空间中实现可变长度轨迹生成。
  4. **反向时序集成**：在推理时，对同一观测生成多个反向轨迹，以关键帧为锚点对齐并集成，提高预测稳定性。
- **训练流程**：采样子轨迹（从随机时间步到下一个关键帧），编码观察和动作，反向排列，通过 Transformer encoder-decoder 解码，优化动作回归损失和潜在一致性损失。
- **推理流程**：从 SOS token 开始自回归生成，直到满足动态停止条件，输出逆向动作序列，再正序执行。

## 3. 实验设计
- **数据集/场景**：
  - **仿真环境**：RLBench（基于 CoppeliaSim），使用 4 个 RGB 相机（128×128），7-DoF Franka Panda 机器人。
  - **真实世界**：Fetch 机器人（7-DoF 臂 + 移动基座），单 RGB 相机（640×480），PD 控制器执行，8 个厨房操作任务。
- **基准（Benchmark）**：
  - 主基准：自行构建的 **60 个 RLBench 任务**（RLBench-60）。
  - 对比基准：RLBench-10（用于 Octo）、RLBench-18（用于 3D 层次方法）。
- **对比方法**：
  1. 从零训练的模仿学习：ACT、Diffusion Policy (DP)。
  2. 微调通用策略：Octo。
  3. 3D 层次方法：PerAct、3D Diffuser Actor、RVT-2（仅作参考对比）。
- **评估协议**：每个任务 100 条演示训练，25 条测试，报告成功率。真实任务 10 次测试。

## 4. 资源与算力
- 文中明确说明：**所有模型每个任务使用单张 NVIDIA H100 GPU 训练**。
- 训练轮次：CoA 和 ACT 为 20,000 次迭代，DP 为 100,000 次，Octo 为 2,000 次。
- 未提及具体训练时长、GPU 内存消耗或总计算量。

## 5. 实验数量与充分性
- **实验数量**丰富：在 60 个 RLBench 任务上全面对比（同时提供 10 个任务和 18 个任务的子集结果），并在 8 个真实世界任务上验证。
- **消融实验**：在 10 个代表性任务上针对建模范式（反向/前向/混合）、MTP 头数、潜在一致性损失、集成策略等关键组件进行了系统消融。
- **充分性分析**：
  - 客观：所有方法采用相同训练设置（除 DP 更多迭代），ACT 和 CoA 架构基本一致，保证了公平性。
  - 不足：未报告**误差棒或统计显著性**（如置信区间），单个任务只评估 25 次，方差信息缺失。空间泛化分析（插值/外推、皮尔逊相关）提供了额外证据，但样本量有限。

## 6. 主要结论与发现
- CoA 在 RLBench-60 上平均成功率 **0.552**，显著优于 ACT（0.389）和 DP（0.326），提升幅度分别为 **16.3%** 和 **23.2%**。
- 在 81.7% 的任务上优于 ACT，80.0% 的任务上优于 DP，尤其是在物体位置变化大的任务中优势更明显。
- 空间泛化分析表明：CoA 在外推场景下性能下降远小于前向方法，且性能增益与空间方差呈正相关，说明反向建模更鲁棒。
- 真实场景中 CoA 平均成功率 0.613，比 ACT（0.463）高 15%。
- 注意力图显示：模型形成**全局-局部**的链式依赖，关键帧动作通过长程注意力引导后续动作生成。

## 7. 优点
- **范式创新**：首次将**反向自回归推理**引入机器人操作策略，从根本上解决累积误差。
- **设计简洁有效**：四个组件均为必要且实用，消融验证了各自贡献。
- **全面实验验证**：涵盖大规模仿真（60 任务）和真实场景（8 任务），并与多种基线公平对比。
- **空间泛化分析深入**：通过插值/外推、方差相关性、注意力可视化等多角度解释性能来源。
- **开源代码与项目页面**提供了可复现基础。

## 8. 不足与局限
- **依赖关键帧启发式**：当前使用基于 gripper 状态或速度的简单规则分割轨迹，可能不适用于更复杂或无极变速的任务，未来需探索无监督关键帧学习。
- **与 3D 层次方法的差距**：在 RLBench-18 上 CoA（37.33%）远低于 PerAct（48.7%）、RVT-2（81.4%），尽管输入模态不同，仍提示纯 RGB 策略在精密操作上的局限性。
- **统计可靠性不足**：缺少误差条和重复实验，单次运行 25 次测试可能存在偶然性。
- **计算资源信息不完整**：未提供训练时间、功耗等，不利于复现成本评估。
- **未讨论失败案例**：对于任务中成功率极低（如 straighten rope 0%）的原因缺乏分析。
- **社会影响未涉及**：论文未讨论技术潜在的负面用途（如自动化武器或岗位替代）。

（完）
