---
title: Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents
title_zh: 具身代理可泛化的视觉-语言预训练中的可证顺序性与连续性
authors: "Zhizhen Zhang, Lei Zhu, Zhen Fang, Zi Huang, Yadan Luo"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=3fDypdR4VN"
tags: ["query:vla"]
score: 8.0
evidence: 从人类动作视频进行视觉-语言预训练用于具身代理
tldr: 现有视觉-语言预训练过度强调未来帧对齐，导致错误关联。本文提出动作时间一致性学习（AcTOL），将视频视为连续序列而非目标导向，通过保持顺序和连续性约束学习更准确的表示。在具身代理任务上，AcTOL预训练的表征显著提升了指令跟随和泛化能力，减少了对专家演示的依赖。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1437, \"height\": 313, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1446, \"height\": 632, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1440, \"height\": 643, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 730, \"height\": 191, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1349, \"height\": 609, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 731, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1439, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 728, \"height\": 445, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1422, \"height\": 986, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-3fdypdr4vn/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1353, \"height\": 1956, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1446, \"height\": 363, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 725, \"height\": 149, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 726, \"height\": 212, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 583, \"height\": 138, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 603, \"height\": 426, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1031, \"height\": 423, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1455, \"height\": 1446, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1438, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1438, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1438, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1436, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1437, \"height\": 290, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-3fdypdr4vn/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1440, \"height\": 290, \"label\": \"Table\"}]"
motivation: 现有时序对比学习依赖目标启发式，可能产生错误的视觉-语言关联。
method: 提出AcTOL，通过保持时间顺序和连续性约束，无需严格目标边界地学习有序连续的视觉-语言表征。
result: 在多个具身环境上，AcTOL预训练的表征显著提升了下游任务的成功率和泛化性。
conclusion: 时间一致性学习可改善视觉-语言预训练质量，促进具身代理泛化。
---

## Abstract
Pre-training vision-language representations on human action videos has emerged
as a promising approach to reduce reliance on large-scale expert demonstrations
for training embodied agents. However, prior methods often employ time con-
trastive learning based on goal-reaching heuristics, progressively aligning language
instructions from the initial to the final frame. This overemphasis on future frames
can result in erroneous vision-language associations, as actions may terminate
early or include irrelevant moments in the end. To address this issue, we propose
Action Temporal Coherence Learning (AcTOL) to learn ordered and continuous
vision-language representations without rigid goal-based constraint. AcTOL treats
a video as a continuous trajectory where it (1) contrasts semantic differences be-
tween frames to reflect their natural ordering, and (2) imposes a local Brownian
bridge constraint to ensure smooth transitions across intermediate frames. Exten-
sive imitation learning experiments on both simulated and real robots show that the
pretrained features significantly enhance downstream manipulation tasks with high
robustness to different linguistic styles of instructions, offering a viable pathway
toward generalized embodied agents. Our project page is at https://actol-pretrain.github.io/.

---

## 论文详细总结（自动生成）

# 论文《Provable Ordering and Continuity in Vision-Language Pretraining for Generalizable Embodied Agents》中文总结

## 1. 核心问题与研究动机
- **背景**：从人类动作视频进行视觉-语言预训练是减少具身代理对大规模专家演示依赖的有效途径。现有方法（如 R3M、LIV、DecisionNCE）采用**目标达到启发式**的时间对比学习，将语言指令与未来帧对齐，假设动作序列逐渐逼近最终目标。
- **问题**：人类动作视频常包含噪声（动作提前结束、结尾包含无关帧），这种刚性假设导致错误的视觉-语言关联，影响下游策略学习。
- **目标**：提出一种更灵活、不依赖显式目标帧的预训练方法，学习**有序且连续**的视觉-语言表示，提升表示质量与泛化性。

## 2. 方法论细节
- **核心思想**：将视频视为连续轨迹，利用帧之间的**自然时间顺序**和**平滑过渡**，而非强制对齐到未来目标。
- **关键组件**：
  - **视觉-语言排序损失（VLO）**：对比任意帧对与语言描述的语义差异，使时间距离更近的帧语义差异更小，距离远的差异更大。损失函数为基于 NCE 的形式：
    \[
    R(v_i, v_j, l) = -\|\text{sim}(v_i, l) - \text{sim}(v_j, l)\|^2
    \]
    负样本定义为比参考帧对距离更远的帧。
  - **布朗桥连续性损失（BB）**：对采样的局部帧区间建模为布朗桥过程，强制中间帧嵌入接近线性插值期望，惩罚偏离，确保局部平滑：
    \[
    L_{\text{BB}} = \frac{1}{T} \sum_{t} \frac{1}{2\text{Var}[B(t)]} \|v_t - \mathbb{E}[B(t)]\|^2_2
    \]
  - **总损失**：\( \mathcal{L}_{\text{AcTOL}} = \mathcal{L}_{\text{VLO}} + \lambda \mathcal{L}_{\text{BB}} \)，\(\lambda\) 设为 0.1。
- **理论保证**：
  - VLO 损失达到下界时，表示满足**有序性**（时间距离与语义差异单调对应）。
  - BB 正则化与相似函数 Lipschitz 连续性共同保证**视觉-语言连续性**（帧嵌入接近→对齐分数接近）。
  - 语言嵌入的小扰动导致对齐分数变化有界（**语言鲁棒性**）。

## 3. 实验设计
- **预训练数据集**：EPIC-KITCHEN-100（人类第一人称厨房动作视频），初始化自 CLIP（ResNet-50）。
- **下游任务场景**：
  - **仿真**：Franka Kitchen（5 个任务：滑动柜门、开左门、开微波炉、开炉灶、开灯）和 Metaworld（5 个任务：锤钉子、按按钮、拣放、装配、开抽屉）。
  - **真实机器人**：Unitree D1 机械臂（3 个任务：捡杯子、打开指定抽屉、关闭指定抽屉）。
- **Baseline 方法**：CLIP、R3M、LIV、DecisionNCE，以及 AcTOL 去掉 BB 的消融变体（AcTOL w/o BB）。
- **实验设置**：
  - 仿真中，每种任务使用 5/15/25 条演示，2 个相机视角，3 个随机种子，报告成功率。
  - 真实机器人每个任务 10 次试验，60 条演示训练。
  - 额外实验包括：视觉偏移（5 种干扰：不同难度物体干扰、纹理变化）、语言扰动（4 种变体：口语化、同义词、复杂句）、人类-机器人域微调、语言条件奖励可视化。

## 4. 资源与算力
- **预训练**：2 块 NVIDIA A800 GPU，训练约 30 小时。
- **下游策略训练**（模拟）：使用 24 核 CPU 工作站，总计约 1944 小时（972 次实验 × 2 小时/次）。
- **真实机器人**：策略推理在 GeForce GTX 880M GPU 上运行。

## 5. 实验数量与充分性
- **覆盖面广**：
  - 仿真：5+5 任务 × 3 演示量 × 2 视角 × 3 种子 × 6 模型 = 540 轮+（实际报告中按任务和环境分组）。
  - 真实：3 任务 × 10 试验。
  - 消融：移除 BB、不同超参数（采样帧数、λ）敏感性（附录图 8）。
  - 鲁棒性：视觉偏移（5 种设置）、语言扰动（4 种变体 × 5 任务 = 20 条件）。
  - 奖励质量：使用 t-SNE 可视化特征连续性，EPIC-KITCHEN-100 和真实 robot 视频奖励曲线。
- **公平性**：与最相关基线（LIV、DecisionNCE）使用相同架构和预训练数据；报告标准差；多次随机种子平均。

## 6. 主要结论与发现
- AcTOL 在仿真和真实机器人上**显著超越所有基线**，尤其在**少样本**场景（5 或 15 条演示）下优势明显，相对提升 14%~49%。
- 去除 BB 损失导致性能下降，验证了连续性约束的重要性。
- 对视觉偏移和语言扰动具有**更强的鲁棒性**：在 5 种视觉偏移中 AcTOL 成功率均高于 DecisionNCE；语言扰动下成功率几乎不变，而基线下降 2.7%~11.9%。
- 奖励函数可准确识别动作边界，生成与指令对齐的密集奖励。
- 通过小规模机器人演示微调编码器（25 条），可进一步缩小人-机器人域差距，成功率从 61.8% 提升至 86.4%。

## 7. 方法的优点
- **理论扎实**：提供排序、连续性、语言鲁棒性的形式化证明，建立了预训练损失与表示性质之间的可证联系。
- **更自然的预训练范式**：避免刚性目标假设，充分利用视频内在时间动态，对噪声视频更鲁棒。
- **高效实用**：减少对专家演示的依赖，在低数据场景表现出色；奖励函数可直接用于 RL。
- **实验全面**：覆盖仿真和真实环境、多种干扰和语言变体，消融充分。

## 8. 不足与局限
- **适用范围**：假设动作呈有序单调进展，对**重复、循环或模糊行为**（如搅拌、循环切换）可能不适用，理论假设可能被违反。
- **实验覆盖**：
  - 真实机器人仅测试 3 个任务，且均属操作范畴，**未涉及移动、抓取-放置等更复杂场景**。
  - 预训练数据仅用 EPIC-KITCHEN-100（厨房场景），**领域偏差**可能限制向其他场景（如户外、工业）的迁移。
  - 与以大规模机器人数据预训练的方法（如 RT-X、OpenVLA）**未直接比较**，因此无法判断在机器人轨迹充足时是否仍具优势。
- **计算资源**：预训练 30 小时（2 卡 A800），对资源有限的团队可能有一定门槛；未报告在线推理速度或模型大小。
- **可重复性**：代码已提供，但论文未明确开源所有模型权重或训练完整配置，可能影响独立复现。

（完）
