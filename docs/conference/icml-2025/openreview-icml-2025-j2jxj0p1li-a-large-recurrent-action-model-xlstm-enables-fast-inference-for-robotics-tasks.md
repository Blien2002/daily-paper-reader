---
title: "A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks"
title_zh: 大型循环动作模型：xLSTM实现机器人任务快速推理
authors: "Thomas Schmied, Thomas Adler, Vihang Prakash Patil, Maximilian Beck, Korbinian Pöppel, Johannes Brandstetter, Günter Klambauer, Razvan Pascanu, Sepp Hochreiter"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=J2JxJ0P1LI"
tags: ["query:vla"]
score: 8.0
evidence: 用于机器人的大型循环动作模型
tldr: 基于Transformer的大规模动作模型推理慢，不适用于机器人实时应用。本文研究现代循环架构（xLSTM、Mamba）用于动作模型，提出大型循环动作模型，在保持训练并行性的同时实现快速推理。实验表明在机器人任务中达到与Transformer相媲美的性能且推理更快。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1344, \"height\": 544, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1345, \"height\": 630, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1121, \"height\": 467, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 834, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 830, \"height\": 518, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1729, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 735, \"height\": 501, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1562, \"height\": 430, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1562, \"height\": 385, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 904, \"height\": 1647, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1127, \"height\": 1032, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 862, \"height\": 607, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1299, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 862, \"height\": 582, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1249, \"height\": 518, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1295, \"height\": 622, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1298, \"height\": 576, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1300, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1303, \"height\": 572, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1305, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1514, \"height\": 601, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 671, \"height\": 518, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1294, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1296, \"height\": 614, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1163, \"height\": 1039, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1299, \"height\": 617, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1158, \"height\": 553, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1298, \"height\": 619, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1297, \"height\": 618, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1300, \"height\": 656, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 1289, \"height\": 650, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-032.webp\", \"caption\": \"\", \"page\": 0, \"index\": 32, \"width\": 1296, \"height\": 627, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-033.webp\", \"caption\": \"\", \"page\": 0, \"index\": 33, \"width\": 1299, \"height\": 615, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j2jxj0p1li/fig-034.webp\", \"caption\": \"\", \"page\": 0, \"index\": 34, \"width\": 1642, \"height\": 651, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1445, \"height\": 425, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 950, \"height\": 1531, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1201, \"height\": 638, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1055, \"height\": 680, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 814, \"height\": 747, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 990, \"height\": 693, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1130, \"height\": 142, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1047, \"height\": 682, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1198, \"height\": 1962, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1402, \"height\": 1646, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1413, \"height\": 595, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 863, \"height\": 2155, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1386, \"height\": 2193, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1388, \"height\": 2204, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1395, \"height\": 2117, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j2jxj0p1li/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1394, \"height\": 1609, \"label\": \"Table\"}]"
motivation: Transformer大模型推理慢，不适合机器人实时控制。
method: 采用xLSTM等现代循环架构构建大型动作模型，利用训练并行性和快速推理。
result: 机器人任务中性能与Transformer相当，推理速度显著提升。
conclusion: 现代循环架构可替代Transformer用于机器人动作模型，兼顾效率与性能。
---

## Abstract
In recent years, there has been a trend in the field of Reinforcement Learning (RL) towards large action models trained offline on large-scale datasets via sequence modeling. Existing models are primarily based on the Transformer architecture, which results in powerful agents. However, due to slow inference times, Transformer-based approaches are impractical for real-time applications, such as robotics. Recently, modern recurrent architectures, such as xLSTM and Mamba, have been proposed that exhibit parallelization benefits during training similar to the Transformer architecture while offering fast inference. In this work, we study the aptitude of these modern recurrent architectures for large action models. Consequently, we propose a Large Recurrent Action Model (LRAM) with an xLSTM at its core that comes with linear-time inference complexity and natural sequence length extrapolation abilities. Experiments on 432 tasks from 6 domains show that LRAM compares favorably to Transformers in terms of performance and speed.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：现有基于Transformer的Large Action Models（LAMs）（如Decision Transformer）在机器人等实时应用中推理速度过慢（二次复杂度），无法满足100-1000Hz的控制器采样率需求。
- **整体含义**：该论文系统评估了现代循环架构（xLSTM、Mamba）作为LAMs骨干的潜力，提出LRAM（Large Recurrent Action Model），在保持训练并行性的同时实现了线性推理复杂度，从而兼顾性能与速度，为实时机器人控制提供了可行方案。

## 2. 论文提出的方法论

- **核心思想**：用现代循环架构（xLSTM、Mamba）替代Transformer作为决策序列模型的骨干，利用其训练阶段的并行化与推理阶段的线性复杂度。
- **关键技术细节**：
  - **输入表示**：状态（图像用CNN编码，低维用全连接）、Return-to-Go、奖励，去除动作预测中的前一动作（避免“复制猫问题”）。
  - **动作输出**：连续动作离散化为256个bin，使用共享动作头一次性预测全部动作维度（离散动作直接分类）。
  - **训练目标**：交叉熵损失，行为克隆范式（条件于RTG和奖励）。
  - **推理模式**：利用循环神经网络的隐状态进行线性时间推理，支持长序列（如多回合ICL）。
- **架构变体**：xLSTM有两种变体——mLSTM（完全可并行化）和sLSTM（支持状态跟踪），论文主要使用[7:1]和[1:0]比例。

## 3. 实验设计

- **数据集与场景**：收集了432个任务、6个领域共8.94亿个转换的大规模离线数据集：
  - Atari（41训练+5测试任务，图像观测，离散动作）
  - Composuite（240训练+16测试任务，连续状态/动作，机器人操作）
  - DMControl（11训练+5测试任务，连续状态/动作）
  - Meta-World（45训练+5测试任务，连续状态/动作）
  - Mimicgen（83训练+2测试任务，连续状态/动作，机器人）
  - Procgen（12训练+4测试任务，图像观测，离散动作）
- **Benchmark**：多任务离线序列建模；评估指标包括验证集困惑度、归一化分数（数据归一化或人类归一化）。
- **对比方法**：xLSTM[7:1]、xLSTM[1:0]、Mamba、GPT-2风格Transformer（DT）。四种模型规模：16M、48M、110M、206M参数。
- **额外实验**：微调（37个留出任务）、上下文学习（ICL，Dark-Room 10×10）、推理时间对比（延迟、吞吐量）、消融（去除动作、上下文长度、Dropout、mLSTM/sLSTM比例、返回条件、层数缩减等）、嵌入空间分析（UMAP）。

## 4. 资源与算力

- **训练硬件**：4块NVIDIA A100 GPU（40GB显存），使用分布式数据并行。
- **训练时长**：最小DT模型约5小时，最大Mamba模型约30小时（200K更新步，batch size 128×6梯度累积）。
- **评估**：并行化评估，使用4进程/GPU，全部432任务评估耗时18分钟（小模型）~2小时（大模型）。
- **推理测试**：A100上测试，使用torch.compile、FlashAttention（DT）、自定义xLSTM内核、Mamba官方内核。

## 5. 实验数量与充分性

- **实验数量**：非常充分。包括：
  - 4种模型规模 × 3个随机种子 × 4种架构 → 主要结果；
  - 每个领域和总体性能曲线；
  - 零样本、微调、ICL性能；
  - 推理时延和吞吐量对比（不同batch size、上下文长度）；
  - 多项消融：去除动作、上下文长度、Dropout、mLSTM/sLSTM比例、RTG条件、层数匹配等。
- **充分性与客观性**：采用标准离线RL评估协议（保留2.5%验证集，每50K评估，95%置信区间）；对比方法使用相同训练协议和数据集；推理对比控制参数和计算环境公平。局限：Mamba与torch.compile不兼容，可能使其推理稍慢。

## 6. 论文的主要结论与发现

- 在432个任务的评估中，xLSTM和Mamba的性能优于或匹配Transformer，且在更大模型规模下xLSTM优势更明显（206M参数）。
- 推理速度：对于长序列（≥25600时间步）和大批量（B≥16），xLSTM和Mamba延迟显著低于Transformer，且不会OOM；吞吐量更高。
- 去除动作输入和增加上下文长度都有利于提升性能（缓解复制猫问题）。
- xLSTM的sLSTM块（7:1比例）在需要状态跟踪的任务（如Dark-Room ICL）中表现出色，Mamba无法实现。
- 现代循环架构同样支持高效微调和ICL。

## 7. 优点

- **方法创新**：首次系统地将xLSTM等现代循环架构应用到大规模多任务决策模型中，解决了Transformer推理瓶颈。
- **实验全面**：覆盖6个领域、432个任务、多种模型规模；包含详尽的推理性能对比（延迟、吞吐量、内存）。
- **开源贡献**：释放数据集生成管道和所生成的存储数据，促进后续研究。
- **设计细节**：共享动作头、去除动作条件等实用技巧验证有效。

## 8. 不足与局限

- **真实机器人验证缺失**：所有实验均在仿真环境，未在真实机器人上测试。
- **微调仅限离线**：未探索在线RL微调（尽管循环架构更易适配）。
- **ICL场景单一**：仅在Dark-Room网格世界测试，未在更复杂环境验证。
- **潜在偏差**：Mamba可能因与torch.compile不兼容而在推理速度上处于劣势；xLSTM的sLSTM带来的提升仅在特定任务中体现。
- **数据质量**：数据集混合了专家和次优轨迹，且Mimicgen任务失败较多，可能限制泛化。
- **计算成本**：最大模型（408M）仅单次运行，未报告统计显著性。

（完）
