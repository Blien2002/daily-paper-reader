---
title: Efficient Robotic Policy Learning via Latent Space Backward Planning
title_zh: 通过潜在空间反向规划实现高效机器人策略学习
authors: "Dongxiu Liu, Haoyi Niu, Zhihao Wang, Jinliang Zheng, Yinan Zheng, Zhonghong Ou, Jianming HU, Jianxiong Li, Xianyuan Zhan"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=DJiouYdH19"
tags: ["query:vla"]
score: 5.0
evidence: 潜在空间反向规划实现高效机器人策略学习
tldr: 针对前向规划在长时域任务中计算量大且误差累积的问题提出在潜在空间进行反向规划生成子目标引导策略。实验证明该方法在多种机器人任务中实现高效准确的规划适合实时控制。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-djiouydh19/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 888, \"height\": 811, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-djiouydh19/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 907, \"height\": 529, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-djiouydh19/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1758, \"height\": 506, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-djiouydh19/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1759, \"height\": 467, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-djiouydh19/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1773, \"height\": 472, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-djiouydh19/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1776, \"height\": 477, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1768, \"height\": 525, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 823, \"height\": 499, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 822, \"height\": 292, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1433, \"height\": 884, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1759, \"height\": 334, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1561, \"height\": 765, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 861, \"height\": 316, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 859, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1045, \"height\": 319, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1416, \"height\": 316, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-djiouydh19/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1607, \"height\": 317, \"label\": \"Table\"}]"
motivation: 前向规划计算成本高且误差累积影响实时性和任务成功率。
method: 在潜在空间中从目标反推规划子目标避免全像素预测。
result: 在机器人规划任务中降低了计算开销提高了长期任务成功率。
conclusion: 潜在空间反向规划为长时域机器人控制提供了高效准确的新范式。
---

## Abstract
Current robotic planning methods often rely on predicting multi-frame images with full pixel details. While this fine-grained approach can serve as a generic world model, it introduces two significant challenges for downstream policy learning: substantial computational costs that hinder real-time deployment, and accumulated inaccuracies that can mislead action extraction. Planning with coarse-grained subgoals partially alleviates efficiency issues. However, their forward planning schemes can still result in off-task predictions due to accumulation errors, leading to misalignment with long-term goals. This raises a critical question: Can robotic planning be both efficient and accurate enough for real-time control in long-horizon, multi-stage tasks?
To address this, we propose a **B**ackward **P**lanning scheme in **L**atent space (**LBP**), which begins by grounding the task into final latent goals, followed by recursively predicting intermediate subgoals closer to the current state. The grounded final goal enables backward subgoal planning to always remain aware of task completion, facilitating on-task prediction along the entire planning horizon. The subgoal-conditioned policy incorporates a learnable token to summarize the subgoal sequences and determines how each subgoal guides action extraction.
Through extensive simulation and real-robot long-horizon experiments, we show that LBP outperforms existing fine-grained and forward planning methods, achieving SOTA performance. Project Page: [https://lbp-authors.github.io](https://lbp-authors.github.io).

---

## 论文详细总结（自动生成）

# 论文中文总结：通过潜在空间反向规划实现高效机器人策略学习

## 1. 核心问题与整体含义（研究动机和背景）
- **现有方法的困境**：当前机器人规划方法主要分为两类：细粒度视频预测（如逐帧预测）和粗粒度子目标规划。前者计算成本高、误差累积严重，难以实时部署；后者虽然效率较高，但前向规划的固有缺陷导致子目标容易偏离最终任务目标，出现“离题”行为（off-task）。
- **核心矛盾**：机器人规划面临效率、长时域一致性和预测精度三者之间的“三元悖论”（trilemma）。如何在长时域、多阶段任务中同时实现高效、准确且与目标对齐的规划，是亟需解决的关键问题。
- **本文思路**：借鉴人类规划方式——先设想最终目标，再逐步分解为更接近当前状态的子目标，提出**潜在空间反向规划（LBP）**，从最终目标反向递归预测子目标，从而在保证任务对齐的同时提升计算效率。

## 2. 方法论：核心思想、关键技术细节、算法流程
- **核心思想**：在潜在空间（latent space）中进行反向子目标规划。首先将语言指令和当前状态映射为最终潜在目标（final latent goal），然后递归地预测越来越接近当前状态的中间子目标，形成从粗到细（coarse-to-fine）的子目标序列。最终，子目标序列与语言特征共同输入策略网络，通过可学习的“目标融合注意力”（Goal-Fusion Attention）模块自适应地整合不同距离的子目标信息。
- **关键技术细节**：
  - **目标预测器（Goal Predictor, fg）**：由2层MLP构成，输入当前潜在状态zt和语言指令特征ϕ_l，输出最终潜在目标zg。优化目标见公式(2)。
  - **统一子目标预测器（Subgoal Predictor, fw）**：同样由2层MLP实现，输入当前状态zt、上一级子目标wi-1（或最终目标zg作为w0）和语言特征ϕ_l，输出当前子目标wi。训练时采用双层优化：第一层使用真实子目标z_λi进行监督，第二层使用自身前一次预测的ẑ_λi-1作为输入，保证递归预测的一致性。优化目标见公式(5)。
  - **递归规划系数λ**：控制子目标的时间密度，λ=0.5表示子目标位于当前状态与目标之间的中点，λ=0.75则更靠近目标。默认使用3步规划（1个最终目标+2个中间子目标），λ=0.5。
  - **策略网络**：采用共享ResNet-34提取多视角图像特征，通过FiLM注入语言嵌入，再与目标融合特征拼接，经残差MLP输出动作。使用扩散损失（denoising step=25）建模动作分布，动作分块长度=6。
  - **目标融合模块**：基于Perceiver-style交叉注意力，用可学习的潜在向量作为查询，从所有子目标和最终目标中压缩出低维上下文嵌入zc，实现自适应信息提取。
- **算法流程**（测试阶段）：
  1. 将当前观测It和语言指令l通过编码器（如DecisionNCE）得到潜在状态zt和语言特征ϕ_l。
  2. 目标预测器fg生成最终潜在目标zg。
  3. 子目标预测器fw递归生成子目标序列wn, ..., w1（w0=zg）。
  4. 所有预测的（子）目标与语言特征一起作为上下文c，输入策略网络π(a|It, c)输出动作。

## 3. 实验设计
- **模拟环境**：**LIBERO-LONG**基准（Liu et al., 2024），包含10个不同的长时域机器人操作任务（如放置物品、打开微波炉等），每个任务提供50条专家演示。图像分辨率256×256。
- **真实机器人环境**：使用6自由度AIRBOT机械臂，搭配三个Logitech C922PRO摄像头（顶视、前视、腕视）。设计了4个长时域任务：堆叠3个杯子、移动杯子、堆叠4个杯子、移位杯子。每个任务包含2~5个阶段。数据集规模：Move cups和Shift cups各200条演示，Stack 3/4 cups共200条演示（有数据增强）。
- **对比方法**：
  - LIBERO-LONG：MTACT、MVP、MPI、OpenVLA、Seer、SuSIE（论文复现，加入腕视角）。
  - 真实实验：LCBC（仅语言条件行为克隆）、GLCBC（语言+固定目标图像条件）、SuSIE（图像编辑子目标规划）。
- **评估指标**：模拟实验采用平均成功率（Avg. Success），每个任务的top-3 checkpoint各评估10次rollout取平均。真实实验采用阶段级评分（0/25/50/75/100），只有当前阶段获得100分才能进入下一阶段，最终给出各阶段平均分。

## 4. 资源与算力
- 文中明确提及：SuSIE的高层图像编辑扩散模型使用4张A6000 GPU进行训练。但**LBP自身的训练算力细节未明确说明**。仅提到高层规划器（MLP）训练100k steps，低层策略在LIBERO-LONG训练200k steps（batch size=64），在真实实验训练400k steps（batch size=128）。未说明使用的GPU型号、数量及具体训练时间。

## 5. 实验数量与充分性
- **实验数量**：在LIBERO-LONG上进行了10个任务的对比实验，每个方法取top-3 checkpoints × 10次评估；在真实机器人上进行了4个任务各10次rollout评估。此外还包含多组消融实验：
  - 规划步数消融（0/1/2/3个子目标）
  - 递归系数λ消融（0.5 vs. 0.75）
  - 有无规划器对比（w/o planner为LCBC）
  - 目标融合策略消融（平均池化 vs. 交叉注意力）
  - 前向与反向规划误差对比（MSE可视化）
- **充分性与公平性**：模拟实验使用与Seer论文相同的评估设置，保证公平；真实实验采用严格阶段递进规则，指标客观。消融实验覆盖了关键超参数和架构组件，分析合理。但缺乏在更多变体（如不同编码器、更大规模任务）上的验证，以及与其他子目标规划方法（如GCSL）的直接对比。

## 6. 主要结论与发现
- LBP在LIBERO-LONG上达到平均成功率88.6%（DecisionNCE latent），显著优于所有基线（Seer: 78.6%, SuSIE: 76.3%）。在10个任务中的9个上取得最高成功率。
- 真实机器人实验中，LBP在所有任务的各个阶段均优于其他方法，尤其在后期阶段优势明显（如Shift cups最终阶段得分26.6 vs. LCBC的0.0）。
- 与前向规划对比，反向规划的MSE误差显著更低且稳定，不随规划时长增长。
- 消融实验表明：最终视觉目标zg提供6%的增益；子目标w进一步带来3%的提升；但过多子目标（如4个）反而下降；目标融合模块优于平均池化（+9.6%）；λ取值0.5和0.75均稳健。

## 7. 优点
- **创新性**：首次将反向规划引入潜在空间子目标生成，从根本上缓解前向规划的误差累积问题，同时保持计算高效。
- **效率**：利用轻量MLP实现规划，避免像素级生成模型的高开销，可实时部署。
- **灵活性**：子目标序列提供从粗到细的多尺度指导，目标融合模块自适应利用不同距离信息，适应不同任务阶段需求。
- **实验全面**：包含模拟和真实机器人、多任务、多阶段评估，消融实验设计合理，对比公平。
- **泛化性**：在真实环境中添加干扰物、更换背景等情况下仍保持较好性能（见表11）。

## 8. 不足与局限
- **算力信息缺失**：未明确说明LBP本身的训练GPU型号、数量及训练时间，影响可复现性和资源需求评估。
- **任务覆盖有限**：模拟环境仅10个任务，真实任务均为桌面操作（pick-and-place），未涉及移动操作、多机协作等复杂场景；物体种类和操作模式较单一。
- **子目标数量敏感**：虽然默认3步最优，但增加子目标（4步）时性能下降，说明递归预测存在一定容量限制，需要自动选择关键帧（作者也指出这是未来方向）。
- **潜在空间依赖**：性能依赖编码器（如DecisionNCE），不同编码器差异（SigLIP vs. DecisionNCE）导致约3.6%的差距，可能限制了在其他视觉表示上的泛化。
- **未与其他子目标学习方法（如GCSL、HiQL）对比**：论文仅对比了视频规划（Seer）和图像编辑规划（SuSIE），缺少与同类子目标规划的纵向比较。
- **实验偏差风险**：真实机器人演示由研究者收集，可能隐含一定分布内假设；对抗性干扰场景测试不够系统（仅简单干扰物和背景变化）。
- **应用限制**：方法假设任务可通过语言指定最终目标，对于无法用语言描述的隐性目标（如康复训练）不适用。

（完）
