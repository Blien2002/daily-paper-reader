---
title: "ReinboT: Amplifying Robot Visual-Language Manipulation with Reinforcement Learning"
title_zh: ReinboT：利用强化学习增强机器人视觉-语言操作
authors: "Hongyin Zhang, Zifeng Zhuang, Han Zhao, Pengxiang Ding, Hongchao Lu, Donglin Wang"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=Mzz4BhdIFb"
tags: ["query:vla"]
score: 10.0
evidence: 端到端VLA模型结合离线强化学习，名为ReinboT，实现稳健决策
tldr: 针对视觉-语言-动作（VLA）模型受限于训练数据质量问题，本文提出ReinboT，一种端到端VLA模型，通过预测密集回报将强化学习原理融入模仿学习。该模型能够从混合质量数据中学习稳健策略，在操作任务中表现出更优的决策能力。ReinboT展示了RL增强VLA的有效性。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1413, \"height\": 644, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 804, \"height\": 778, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 882, \"height\": 642, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1421, \"height\": 238, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 575, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 828, \"height\": 560, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 869, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1244, \"height\": 417, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1614, \"height\": 1120, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1249, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1613, \"height\": 1121, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1249, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1611, \"height\": 1116, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1249, \"height\": 417, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1609, \"height\": 1114, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-mzz4bhdifb/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1577, \"height\": 952, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-mzz4bhdifb/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1237, \"height\": 631, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mzz4bhdifb/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1210, \"height\": 379, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mzz4bhdifb/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1234, \"height\": 561, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-mzz4bhdifb/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1270, \"height\": 561, \"label\": \"Table\"}]"
motivation: VLA模型依赖模仿学习，但训练数据质量参差不齐限制了其性能，离线强化学习可从中学习稳健策略。
method: 提出端到端VLA模型ReinboT，通过预测密集回报将强化学习最大化累积奖励原则集成到模型中。
result: ReinboT实现了对数据质量分布的深层理解，生成更鲁棒的机器人决策动作。
conclusion: 融合强化学习原则能有效提升VLA模型在复杂操作任务中的性能。
---

## Abstract
Vision-Language-Action (VLA) models have shown great potential in general robotic decision-making tasks via imitation learning. However, the variable quality of training data often constrains the performance of these models. On the other hand, offline Reinforcement Learning (RL) excels at learning robust policy models from mixed-quality data. In this paper, we introduce Reinforced robot GPT (ReinboT), a novel end-to-end VLA model that integrates the RL principle of maximizing cumulative reward. ReinboT achieves a deeper understanding of the data quality distribution by predicting dense returns that capture the nuances of manipulation tasks. The dense return prediction capability enables the robot to generate more robust decision-making actions, oriented towards maximizing future benefits. Extensive experiments show that ReinboT achieves state-of-the-art performance on the CALVIN mixed-quality dataset and exhibits superior few-shot learning and out-of-distribution generalization capabilities in real-world tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
视觉-语言-动作（VLA）模型通过模仿学习在机器人通用决策任务中展现出巨大潜力，但其性能受限于训练数据质量的参差不齐：即使来自成功示范的数据，质量也往往不均衡。模仿学习难以区分混合质量数据并充分利用，而离线强化学习（RL）擅长从混合质量数据中学习稳健策略。论文旨在将RL的“最大化累积奖励”原则内化到VLA模型中，使其能够基于对数据质量的深度理解生成更鲁棒的决策动作，从而提升机器人长时域操作能力。

## 2. 论文提出的方法论

### 核心思想
将离线RL中的最大回报序列建模（如Decision Transformer中的ReturnToGo）作为新模态数据，通过**expectile回归**（一种分位数回归的变体）预测**当前状态下可达到的最大回报**（而非轨迹的真实回报），并将其与动作解码器耦合，引导模型输出倾向于最大化未来收益的动作。

### 关键技术细节
- **密集奖励设计**：自动将长时域任务轨迹分割为单子目标片段，并设计包含四个分量的密集奖励：
  - `r1`（子目标达成）：通过MSE、SSIM、ORB特征匹配衡量图像与关节状态与子目标的相似度。
  - `r2`（任务进展）：根据当前所在的子目标序列位置给予奖励，越接近最终目标奖励越大。
  - `r3`（行为平滑）：抑制关节速度、加速度和动作变化率，惩罚不连贯运动。
  - `r4`（任务完成）：轨迹成功时为1，否则为0。
  最终总奖励为四个分量的加权和。
- **网络架构**：基于GPT-style Transformer，输入语言指令（CLIP编码）、图像状态（ViT + Perceiver Resampler）、本体感受（MLP）。引入三个预测token：`[RTG]`、`[ACTION]`、`[IMAGE]`，分别对应回报、动作和未来图像预测。回报解码器的最后一层隐藏特征与动作特征拼接后输入动作解码器。
- **训练损失**：`L = λ L_RTG + L_arm + 0.01 L_gripper + 0.1 L_image`，其中`L_RTG`采用expectile回归损失，参数`m > 0.5`时倾向于预测高于真实回报的值，实现回报最大化。
- **推理流程**：无需手动设置初始ReturnToGo，无需环境提供奖励，单次前向即可得到动作（见Algorithm 1）。

### 公式与算法说明（文字描述）
- ReturnToGo损失：`L_RTG = E_t[ |τ - 1(Δg < 0)| · (Δg)^2 ]`，其中`Δg = g_t - 预测回报`，`τ`为expectile参数（`m`）。
- 动作预测公式：`ˆa_t = P_ω( h_action, ˆg_hidden )`，其中`ˆg_hidden`来自RTG解码器最后一层隐藏特征。

## 3. 实验设计

### 数据集与场景
- **模拟环境**：CALVIN（长时域操作基准）。构造混合质量数据集：包含ABC区约50条/任务的带语言标注轨迹，以及D区大量无标注自主数据（含失败数据和不同噪声水平），共约3万条轨迹。
- **真实世界**：UR5机械臂，抓取放置任务（杯子、碗、毛绒玩具），共约530条成功轨迹。少数样本微调（每个任务30条）和OOD泛化（新指令、背景、干扰物、物体）。

### Benchmark
- **模拟**：CALVIN D环境上的链式指令成功率（1～5个指令）和平均完成长度（AL）。
- **真实**：few-shot学习成功率、OOD泛化成功率。

### 对比方法
- **模仿学习类**：RoboFlamingo、GR-1、PIDM、GR-MG。
- **离线RL类**：RWR（Reward-Weighted Regression）。
- **奖励设计变体**：稀疏奖励、子目标稀疏奖励、本文提出的密集奖励（单维/全分量）。
- **消融**：去除ReturnToGo、去除各奖励分量、不同超参数λ和m。

## 4. 资源与算力
论文未明确提及所使用的GPU型号、数量或训练时长。仅在附录中给出训练超参数：Epoch=50，Batch size=32，Learning rate=0.001，使用Adam优化器。未公开硬件配置。

## 5. 实验数量与充分性
- **主实验**（Table 1）：在CALVIN混合质量数据上对比5种基线及多种奖励变体，共约12个配置。
- **消融实验**（Table 2）：围绕密集奖励的四个分量及有无ReturnToGo，共6组。
- **超参数分析**（Figure 2）：λ（0.0~0.1）和m（0.5~0.99）的影响，共约12组。
- **回报性质分析**（Figure 3）：不同m下预测回报分布对比。
- **真实世界实验**（Figure 6）：few-shot（3个任务）和OOD（4个场景）对比，共约7个条件。
- **补充**：附录中展示了子目标分割和奖励可视化样例。

总体来看，实验覆盖了模拟和真实场景，对比了多种代表性方法，消融充分，超参数分析细致。但**未报告多次运行的标准差或置信区间**，可能削弱统计显著性。实验设计客观公平。

## 6. 论文的主要结论与发现
- ReinboT在CALVIN混合质量数据集上达到SOTA，平均完成长度（AL=2.26）显著优于模仿学习方法（PIDM为1.73）和RWR（1.82）。
- 密集回报的各个分量对性能均有贡献，其中任务进展（r2）和子目标达成（r1）最为关键。
- expectile参数m=0.9时最佳，过大（如0.99）会导致过乐观估计和性能下降。
- 预测的最大回报分布高，表明模型能识别高质量数据并引导动作朝向高回报。
- 真实世界中，ReinboT在少数样本微调和OOD泛化上均优于GR-1和RWR。

## 7. 优点
- **方法创新**：将离线RL的回报最大化思想以监督学习范式无缝集成到VLA中，无需引入Q函数或额外RL损失，降低了训练难度。
- **密集奖励设计通用性强**：基于子目标、行为平滑、任务进展等通用因素，不依赖特定任务知识，易于迁移。
- **推理高效**：单次前向即可得到动作，无需手动设置RTG初始值，适合实际部署。
- **实验全面**：覆盖模拟和真实、混合质量数据和少量数据场景，消融充分。
- **可视化分析**：通过回报分布对比直观展示了回报最大化的效果。

## 8. 不足与局限
- **算力资源未公开**：缺少GPU型号、数量、训练时长等信息，影响可复现性判断。
- **实验统计未报告方差**：多次运行的标准差或置信区间缺失，无法评估结果稳定性。
- **真实世界任务规模有限**：仅约530条成功轨迹，且任务类型为简单抓取放置，未验证更复杂或更多样化的操作。
- **子目标分割依赖启发式**：需要基于关节速度和夹爪状态变化检测关键点，可能不适用于所有任务（如连续精细操作）。
- **对失败数据的利用有限**：混合质量数据包含失败轨迹，但奖励设计主要面向成功轨迹，失败轨迹的奖励可能较低，模型如何有效利用其信息未深入分析。
- **可扩展性未验证**：仅使用GPT-2规模网络，未探讨更大模型或数据量下的表现。

（完）
