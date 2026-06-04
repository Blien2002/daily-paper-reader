---
title: Enhancing Rating-Based Reinforcement Learning to Effectively Leverage Feedback from Large Vision-Language Models
title_zh: 增强基于评分强化学习以有效利用大视觉语言模型反馈
authors: "Tung Minh Luu, Younghwan Lee, Donghoon Lee, Sunho Kim, Min Jun Kim, Chang D. Yoo"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=k77bq8AJVy"
tags: ["query:vla"]
score: 6.0
evidence: 利用大视觉语言模型反馈进行奖励学习可应用于机器人学习
tldr: 针对手工设计奖励困难的问题提出ERL-VLM方法通过从大视觉语言模型的评分反馈中学习奖励函数避免人工标注。实验表明该框架在连续控制任务中有效为自动化奖励学习提供新途径。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1419, \"height\": 672, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 848, \"height\": 731, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1769, \"height\": 269, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1774, \"height\": 708, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1679, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1680, \"height\": 478, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1087, \"height\": 427, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1754, \"height\": 156, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1277, \"height\": 654, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1282, \"height\": 640, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1281, \"height\": 641, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1626, \"height\": 413, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1777, \"height\": 342, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1477, \"height\": 378, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1771, \"height\": 352, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1479, \"height\": 378, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 200, \"height\": 201, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 200, \"height\": 202, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 199, \"height\": 203, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 199, \"height\": 197, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 199, \"height\": 201, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 199, \"height\": 204, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 200, \"height\": 199, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1663, \"height\": 237, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1666, \"height\": 152, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1036, \"height\": 164, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1670, \"height\": 137, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1658, \"height\": 213, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1219, \"height\": 171, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1546, \"height\": 132, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 1545, \"height\": 123, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 1130, \"height\": 130, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-033.webp\", \"caption\": \"\", \"page\": 0, \"index\": 33, \"width\": 1783, \"height\": 2019, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-k77bq8ajvy/fig-034.webp\", \"caption\": \"\", \"page\": 0, \"index\": 34, \"width\": 1615, \"height\": 2285, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 874, \"height\": 239, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1771, \"height\": 1012, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 780, \"height\": 756, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 957, \"height\": 887, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 797, \"height\": 495, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1748, \"height\": 268, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1749, \"height\": 269, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1750, \"height\": 269, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1749, \"height\": 267, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-k77bq8ajvy/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1749, \"height\": 268, \"label\": \"Table\"}]"
motivation: 手工设计奖励函数耗时且依赖领域知识人类反馈成本高。
method: 使用VLM提供评分反馈学习奖励函数替代人工偏好比较。
result: 在MuJoCo连续控制任务中取得与人类反馈相当的性能。
conclusion: VLM反馈可有效替代部分人类监督扩展强化学习应用。
---

## Abstract
Designing effective reward functions remains a fundamental challenge in reinforcement learning (RL), as it often requires extensive human effort and domain expertise. While RL from human feedback has been successful in aligning agents with human intent, acquiring high-quality feedback is costly and labor-intensive, limiting its scalability. Recent advancements in foundation models present a promising alternative--leveraging AI-generated feedback to reduce reliance on human supervision in reward learning. Building on this paradigm, we introduce ERL-VLM, an enhanced rating-based RL method that effectively learns reward functions from AI feedback. Unlike prior methods that rely on pairwise comparisons, ERL-VLM queries large vision-language models (VLMs) for absolute ratings of individual trajectories, enabling more expressive feedback and improved sample efficiency. Additionally, we propose key enhancements to rating-based RL, addressing instability issues caused by data imbalance and noisy labels. Through extensive experiments across both low-level and high-level control tasks, we demonstrate that ERL-VLM significantly outperforms existing VLM-based reward generation methods. Our results demonstrate the potential of AI feedback for scaling RL with minimal human intervention, paving the way for more autonomous and efficient reward learning.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：在强化学习（RL）中，手工设计奖励函数耗时且依赖领域专家知识；从人类反馈中学习奖励（RLHF）虽然有效，但获取高质量人类反馈成本高、劳动密集，难以规模化。
- **整体含义**：本文提出利用大视觉语言模型（VLM）的自动反馈替代人类监督，以降低奖励学习的成本，实现更自主、高效的奖励学习。特别是，针对现有基于偏好（pairwise comparison）的方法存在样本效率低、查询成本高、对相似轨迹存在模糊性等问题，本文转向**绝对评分**（rating）方式，并引入增强机制来稳定学习。

## 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：ERL-VLM 通过查询 VLM（如 Gemini-1.5-Pro）获取绝对评分反馈（如“很坏/坏/一般/好/很好”），而非对比偏好。评分反馈更富表达力，且单个样本即可提供全局信息，提高样本效率。
- **关键技术细节**：
  1. **评分生成**：设计两阶段提示——先让 VLM 分析轨迹（含多帧图像和动作），再基于分析给出分级评分（n 类）。
  2. **奖励模型**：从评分数据中学习奖励函数 $\hat{r}_\psi$，使用基于评分的概率模型（参考 White et al., 2024）将预测回报映射为评分分布。
  3. **增强策略**：
     - **分层采样（Stratified Sampling）**：每个训练 batch 确保包含所有评分类别的样本，缓解数据不平衡。
     - **加权损失**：根据类别频率加权。
     - **MAE 损失**：用平均绝对误差替代交叉熵，对 VLM 产生的噪声标签更鲁棒。
  4. **训练流程**：每 K 步查询 VLM 获取 N 个评分，存入评分数据集；更新奖励模型后，回放缓冲区的奖励被重标记；策略使用 SAC 或 IQL 学习。
- **算法流程**（文字描述）：
  - 初始化策略 $\pi_\theta$、奖励函数 $\hat{r}_\psi$、回放缓冲区 $\mathcal{B}$、评分数据集 $\mathcal{D}$、查询频率 K、每次查询数 N。
  - 每个迭代循环：
    - **数据收集**：执行策略 T 步，将经验 $(s, a, s')$ 存入 $\mathcal{B}$。
    - **评分与奖励学习**（每 K 步执行一次）：
      - 从 $\mathcal{B}$ 采样 N 个轨迹段，查询 VLM 获得评分标签 $\tilde{y}$，加入 $\mathcal{D}$。
      - 采用分层采样从 $\mathcal{D}$ 中取 minibatch，用 MAE 损失更新 $\hat{r}_\psi$。
      - 用新奖励函数重标定整个 $\mathcal{B}$ 中经验的奖励。
    - **策略学习**：从 $\mathcal{B}$ 中采样，用任意 off-policy RL 算法（本文用 SAC 或 IQL）更新 $\pi_\theta$。

## 3. 实验设计

- **使用场景/数据集**：
  - **MetaWorld**（低层连续控制）：Sweep Into、Drawer Open、Soccer 三个任务。
  - **ALFRED**（高层视觉语言导航）：20 个任务，分为 PickupObject、PutObject、CoolObject、CleanObject 四类，使用 10 个厨房场景。
  - **真实机器人**（7-DOF Rethink Sawyer）：Sweep Bowl、Drawer Open、Pickup Banana 三个任务。
- **基准方法（Baselines）**：
  - **CLIP Score**：用 CLIP 嵌入相似度作为奖励。
  - **RoboCLIP Score**：用 S3D 视频嵌入相似度。
  - **RL-VLM-F**：用 VLM 偏好反馈学习奖励（pairwise comparison）。
  - **Environment Reward**：使用环境自带奖励（MetaWorld 为密集奖励，ALFRED 为稀疏奖励）。
  - 真实机器人实验中额外对比 **Behavior Cloning (BC)** 和 **IQL with Sparse Rewards**。
- **评价指标**：成功率（Success Rate），每个配置运行 3 个随机种子，报告均值和标准差。

## 4. 资源与算力

- 论文**未明确说明 GPU 型号、数量或训练时长**。仅提到代码开源，未披露具体计算资源。

## 5. 实验数量与充分性

- **实验数量**：
  - 主实验：7 个模拟任务（3 MetaWorld + 4 类 ALFRED）+ 3 个真实机器人任务，对比 4/5 种基线。
  - 消融实验：在 MetaWorld 上对每个增强组件（分层采样、MAE 损失、原始 RbRL）进行了 3 组消融。
  - 额外分析：不同评分类别数（n=2,3,4）、标签平滑 vs MAE、MAE 在偏好学习中的效果、评分一致性测试（10 次重复）、奖励可视化等。
- **充分性与公平性**：
  - 实验覆盖了从低层到高层、模拟到真实的任务，多样性较好。
  - 所有方法使用相同超参数和查询预算（MetaWorld 10000 次查询，ALFRED 1500 次），公平性较高。
  - 消融实验系统分析了各组件贡献。
  - 但样本量偏小（3 个随机种子），且真实机器人任务仅有 50 条演示，可能限制统计显著性。

## 6. 主要结论与发现

- ERL-VLM 在 6/7 个模拟任务中显著优于所有基线，在 ALFRED 上甚至超过环境的稀疏奖励。
- 绝对评分比偏好比较更高效：相同查询预算下，ERL-VLM 提供更丰富的信号，而 RL-VLM-F 在 ALFRED (仅 75 次偏好/任务) 几乎失败。
- 增强组件（分层采样、加权损失、MAE 损失）对稳定学习均不可或缺，其中 MAE 损失贡献最大。
- 评分类别数 n=2 或 3 效果最好，n=4 因歧义增加而性能下降；最优数量与任务本身清晰度相关。

## 7. 优点

- **方法创新**：将绝对评分引入 VLM 反馈的奖励学习，并设计针对数据不平衡和噪声标签的实用增强策略，简洁有效。
- **实验全面**：覆盖模拟（低层/高层）和真实机器人，对比多种基线（包括相似度方法和偏好方法）。
- **实用性强**：仅需语言任务描述和图像观测，不依赖特权状态或环境代码，可推广到新任务。
- **代码开源**：促进可复现性。

## 8. 不足与局限

- **计算资源未报告**：无法评估方法的实际成本。
- **实验规模**：真实机器人任务仅各 50 条演示，模拟任务每个设置仅 3 个随机种子，结果稳定性有待更多种子验证。
- **VLM 偏差风险**：依赖 Gemini-1.5-Pro，可能继承模型偏见；仅在单一 VLM 上测试，泛化性未知。
- **评分一致性**：VLM 评分存在随机噪声（即使温度为 0），方法虽用 MAE 缓解，但仍可能影响精细任务。
- **任务限制**：仅评估了可基于单帧或多帧图像判断的任务，对于需要长期时空推理的任务可能不够。
- **未讨论安全性**：AI 反馈可能产生不安全奖励，文中未涉及安全对齐。

（完）
