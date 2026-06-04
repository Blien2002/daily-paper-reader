---
title: "$\\textit{Hyper-GoalNet}$: Goal-Conditioned Manipulation Policy Learning with HyperNetworks"
title_zh: Hyper-GoalNet：基于超网络的目标条件操纵策略学习
authors: "Pei Zhou, Wanting Yao, Qian Luo, Xunzhe Zhou, Yanchao Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=aWWRPyGMie"
tags: ["query:vla"]
score: 5.0
evidence: 基于超网络的目标条件操纵策略学习
tldr: 目标条件策略学习在多样目标下保持性能困难。本文提出Hyper-GoalNet，利用超网络从目标描述生成策略网络参数，分离目标解释与状态处理，并引入正向动力学和正则化约束增强表示质量。实验表明在多个操纵任务上取得了更好的泛化性能。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1331, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1440, \"height\": 411, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 686, \"height\": 335, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1444, \"height\": 881, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1361, \"height\": 789, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1397, \"height\": 304, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1393, \"height\": 792, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1449, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1411, \"height\": 1772, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-awwrpygmie/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1415, \"height\": 1766, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 689, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1446, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 692, \"height\": 265, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 749, \"height\": 262, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 750, \"height\": 265, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 734, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1447, \"height\": 283, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1010, \"height\": 375, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1067, \"height\": 178, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1273, \"height\": 139, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-awwrpygmie/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 837, \"height\": 206, \"label\": \"Table\"}]"
motivation: 目标条件策略难以在多样目标和环境中保持性能。
method: 使用超网络从目标规范生成任务特定策略参数，并添加约束。
result: 在多种操纵任务上取得了更好的泛化性能。
conclusion: 超网络生成参数的方法有效提升了操纵策略的适应性。
---

## Abstract
Goal-conditioned policy learning for robotic manipulation presents significant challenges in maintaining performance across diverse objectives and environments. We introduce *Hyper-GoalNet*, a framework that generates task-specific policy network parameters from goal specifications using hypernetworks. Unlike conventional methods that simply condition fixed networks on goal-state pairs, our approach separates goal interpretation from state processing -- the former determines network parameters while the latter applies these parameters to current observations. To enhance representation quality for effective policy generation, we implement two complementary constraints on the latent space: (1) a forward dynamics model that promotes state transition predictability, and (2) a distance-based constraint ensuring monotonic progression toward goal states. We evaluate our method on a comprehensive suite of manipulation tasks with varying environmental randomization. 
Results demonstrate significant performance improvements over state-of-the-art methods, particularly in high-variability conditions. Real-world robotic experiments further validate our method's robustness to sensor noise and physical uncertainties. Our code and trained models will be made publicly available.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

目标条件（goal-conditioned）策略学习旨在让机器人根据当前状态观测和指定目标调整动作，但面临**在多样目标和环境中保持高性能**的重大挑战。传统方法通常将目标观测与当前状态拼接后输入固定参数的策略网络，这种做法将“处理什么”（当前状态）与“如何处理”（目标依赖的策略）混在一起，导致网络难以泛化到新目标，尤其是在接触丰富的复杂操纵任务中。本文提出 *Hyper-GoalNet*，**将目标视为确定策略网络参数（即处理方式）的规范**，而非额外的输入特征，从而在更根本的层面实现任务自适应。

## 2. 论文提出的方法论

### 核心思想
利用超网络（hypernetwork）**从目标规范动态生成策略网络参数**，实现“目标解释”与“状态处理”的分离：超网络读入当前与目标观测，输出任务特定的策略权重；生成的轻量级策略网络仅负责将当前观测映射为动作，不再需要重新访问目标信息。

### 关键技术细节
- **超网络架构**：采用优化启发式架构（类似 HyPoGen），通过 K 次迭代逐步优化策略参数。每次迭代模拟梯度下降步骤，其中步长和“梯度”均由可学习模块根据当前与目标观测的嵌入产生：
  \[
  \theta_k = \theta_{k-1} + \lambda_k(\theta_{k-1}, \alpha) \psi_k(\theta_{k-1}, \alpha), \quad \alpha = \phi(o_c, o_g)
  \]
- **训练目标**：行为克隆（BC），最小化预测动作与专家动作的均方误差：
  \[
  \mathcal{L}_{\text{policy}} = \mathbb{E}_{\tau \sim \mathcal{D}} \left[ \ell(a_t, \hat{a}_t) \right], \quad \hat{a}_t = \pi(o_{t-L:t}; H(o_t, o_{t'}))
  \]
- **潜在空间塑造（Latent Space Shaping）**：为提升超网络生成有效参数的能力，对图像编码器输出的潜在表示施加两项约束：
  1. **前向动力学模型**：预测下一时刻的潜在表示，使潜在空间保持状态转移的可预测性；
  2. **距离约束**：确保沿成功轨迹，当前状态与目标状态之间的欧氏距离单调递减（margin β=0）。
  
  总损失：
  \[
  \mathcal{L} = \mathcal{L}_{\text{policy}} + \lambda_{\text{pred}} \mathcal{L}_{\text{pred}} + \lambda_{\text{dist}} \mathcal{L}_{\text{dist}}
  \]
- **测试流程（Algorithm 1）**：每步利用当前和目标观测生成参数 → 策略采样动作 → 环境交互 → 若潜在距离小于阈值则判定成功。该机制可自然检测任务完成。

## 3. 实验设计

- **仿真环境**：使用 Robosuite 和 MimicGen 数据集，包含 **7 种操纵任务**（咖啡操作、穿线、杯子清理、螺母组装、三件组装、咖啡准备、厨房操作），每种任务设有 **3 个难度等级**（d0, d1, d2），对应不同的物体位姿随机化程度。
- **训练数据**：每任务 950 条示范轨迹，使用单张前视 RGB 图像（128×128）和 proprioception（9 维）作为观测。
- **对比方法**：
  - **GCBC**（Goal-Conditioned Behavioral Cloning）
  - **Play-LMP**
  - **MimicPlay**（包括原版和修改版）
  - **C-BeT**（Conditional Behavior Transformer）
  - 另有增强版基线（MimicPlay-O 和 MimicPlay-M）拥有额外腕部摄像头或更长观测序列。
- **评价指标**：**成功率**（50 次独立 rollout，环境提供的终止信号）。

## 4. 资源与算力

- 训练在 **单个 NVIDIA RTX 3090 或 RTX 4090 GPU** 上完成。
- 使用 Adam 优化器，初始学习率 5×10⁻⁴，余弦退火调度；batch size 256，训练 500 epochs。
- 每 epoch 训练时间约 90–104 秒（取决于编码器是否解冻），总训练时长未明确给出，但可估算约 12–14 小时。
- **注意**：论文未明确说明 GPU 数量（文中提到单卡），也未报告所有实验的总 GPU 时长。

## 5. 实验数量与充分性

- **模拟实验**：在 7 类任务 × 多个难度等级上评估，每个设置 50 次 rollout（共 > 30 个条件）。主实验结果（Table 1 & 2）覆盖 5 个短时任务和 2 个长时任务。
- **消融实验**：
  - 潜在空间塑造（有/无）
  - 距离度量选择（余弦 vs 欧氏）
  - 距离计算对象（当前→目标 vs 当前→起始）
  - 编码器解冻时机（epoch 0 vs epoch 20）
  - 超网络架构对比（HyperZero + 特殊初始化 vs 标准初始化）
  - 塑造方法应用于基线 C-BeT
  - 目标完成检测准确率评估（Table 5）
- **真实机器人实验**：4 个任务（拾取放置、拉抽屉、堆叠、扫地），每任务 15 次试验，对比 GCBC、Play-LMP、C-BeT。
- **充分性与公平性**：实验覆盖了多种场景和难度，对比基线采用相同观测设置（但在公平性上，MimicPlay-O 使用了额外腕部相机和更长序列，属于优势基线）。消融实验全面验证各组件贡献。**但未报告标准差或置信区间**，降低了统计显著性表达。

## 6. 论文的主要结论与发现

1. **参数自适应策略显著优于固定参数方法**：Hyper-GoalNet 在全部任务上超过所有基线，尤其在高变异性环境（d1/d2）中维持较高成功率，而基线几乎完全失效。
2. **潜在空间塑造是关键**：去除“去目标距离单调递减”约束后，性能严重下降；使用合适的距离度量（欧氏）比余弦距离更优。
3. **架构选择重要**：优化迭代式超网络（本文架构）远优于直接映射式 HyperZero，即使后者加上特殊初始化。
4. **目标完成可自动检测**：基于潜在距离的判定与真实环境信号高度吻合（平均准确率 86.6%，召回率 94.3%），验证了单调递减空间的有效性。
5. **真实世界鲁棒性**：在物理实验中对传感器噪声和环境变化保持稳健，成功率远高于对比方法。

## 7. 优点

- **创新性**：将目标视为参数生成器而非输入特征，从根本上改变目标条件策略的设计范式。
- **潜在空间塑造**：前向动力学 + 单调距离约束为超网络提供了清晰的结构化信号，同时赋予系统自动检测任务完成的能力。
- **实验完整性**：模拟任务种类多、难度分层合理；真实机器人实验验证了迁移可行性；消融实验系统且深入。
- **实用性**：仅需单张目标图像和 2 帧历史观测，部署简单，且动作生成速度快（Hyper-GoalNet(G) 仅 1.46 ms/步）。

## 8. 不足与局限

- **数据依赖**：演示数据必须包含清晰的“向目标递进”过程，否则难以形成良好结构的潜在空间；对于复杂长时任务，单张目标图像可能不足。
- **分布外泛化风险**：离线训练，对未见过目标可能生成不合理策略，且缺乏安全保证。
- **计算开销**：相较于简单拼接的基线，超网络增加了一些训练和推理负担（参数量、显存占用）。
- **实验细节缺失**：未报告多次运行的标准差或置信区间，影响了结果统计可靠性；未充分讨论失败案例分析。
- **任务覆盖**：虽然多样，但均限于桌面操纵；未验证在动态或非结构化环境（如移动操作）中的表现。

（完）
