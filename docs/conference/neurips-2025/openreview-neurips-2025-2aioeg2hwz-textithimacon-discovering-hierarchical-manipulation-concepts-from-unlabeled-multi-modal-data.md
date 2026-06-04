---
title: "$\\textit{HiMaCon:}$ Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data"
title_zh: HiMaCon：从无标签多模态数据中发现层次化操作概念
authors: "Ruizhe Liu, Pei Zhou, Qian Luo, Li Sun, Jun CEN, Yibing Song, Yanchao Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=2aIoEG2Hwz"
tags: ["query:vla"]
score: 7.0
evidence: 从无标签多模态数据中学习层次化操作概念，支持机器人基础模型
tldr: 机器人操作需要捕获跨环境和任务的交互模式，但手工标注昂贵。HiMaCon利用自监督跨模态相关网络和多时间尺度预测器，从无标签多模态数据中学习层次化操作概念。这些概念使策略能够关注可迁移的关系模式，在多个操作泛化基准上取得改进。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1421, \"height\": 763, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1450, \"height\": 690, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1440, \"height\": 831, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 681, \"height\": 420, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1453, \"height\": 357, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1461, \"height\": 1171, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1395, \"height\": 338, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1359, \"height\": 814, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1184, \"height\": 2083, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1325, \"height\": 676, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2aioeg2hwz/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 989, \"height\": 764, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1441, \"height\": 859, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1342, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 559, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 818, \"height\": 240, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 977, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 979, \"height\": 204, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1080, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 691, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 926, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 867, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 879, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 778, \"height\": 140, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2aioeg2hwz/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 916, \"height\": 197, \"label\": \"Table\"}]"
motivation: 机器人操作泛化需要不变交互模式，但标注成本高。
method: 结合跨模态相关网络和多时间尺度预测器，自监督学习层次化操作概念。
result: 学到的概念提升了策略在多个操作泛化任务上的表现。
conclusion: 层次化操作概念能够有效编码可迁移的交互模式。
---

## Abstract
Effective generalization in robotic manipulation requires representations that capture invariant patterns of interaction across environments and tasks.
We present a self-supervised framework for learning hierarchical manipulation concepts that encode these invariant patterns through cross-modal sensory correlations and multi-level temporal abstractions without requiring human annotation.
Our approach combines a cross-modal correlation network that identifies persistent patterns across sensory modalities with a multi-horizon predictor that organizes representations hierarchically across temporal scales. Manipulation concepts learned through this dual structure enable policies to focus on transferable relational patterns while maintaining awareness of both immediate actions and longer-term goals.
Empirical evaluation across simulated benchmarks and real-world deployments demonstrates significant performance improvements with our concept-enhanced policies. 
Analysis reveals that the learned concepts resemble human-interpretable manipulation primitives despite receiving no semantic supervision. This work advances both the understanding of representation learning for manipulation and provides a practical approach to enhancing robotic performance in complex scenarios.

---

## 论文详细总结（自动生成）

# HiMaCon：从无标签多模态数据中发现层次化操作概念——详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：机器人操作在多样、非结构化环境中的泛化仍面临根本挑战。现有策略遇到意外变化或新场景时容易失败（例如放置杯子时遇到障碍物），存在关键的泛化缺口。
- **核心问题**：如何使机器人从无标签的演示数据中自动学习可迁移的**操作概念**（manipulation concepts），这些概念应编码跨环境和任务的**不变交互模式**，并以层次化方式组织（从低层动作到高层目标），从而提升策略在未见场景中的鲁棒性。
- **整体含义**：提出一种自监督框架，无需人工标注即可从多模态传感器数据中提取层次化操作概念，这些概念能捕捉跨模态相关性（视觉、 proprioception）和不同时间尺度的子目标，使策略关注可迁移的关系模式（如“物体放入容器”），而非表面特征（如颜色、形状），显著提升泛化能力。

## 2. 论文提出的方法论

### 核心思想
通过两个互补的自监督目标学习层次化操作概念：
1. **跨模态相关性学习**：利用 mask-and-predict 策略最大化不同模态观测间的条件互信息，使概念编码跨模态的持久模式。
2. **多时间尺度子目标组织**：通过概念潜变量在簇内的球形距离定义子过程，并训练预测器根据当前观测和概念预测不同时间尺度的终端观测，从而使概念自然形成层次结构。

### 关键技术细节
- **操作概念编码器 E**：使用 Transformer 将多模态观测序列（agentview 视觉、眼在手视觉、本体感知状态）映射为连续的潜变量序列 \(z_t\)（维度 256）。
- **跨模态相关网络 C**：随机 mask 部分模态，然后由概念 \(z_t\) 和未 mask 的观测重构所有模态，通过最小化重构损失最大化条件互信息（公式 3）。
- **多时间尺度未来预测器 F**：基于当前观测 \(o_t\)、概念 \(z_t\) 和随机采样的阈值 \(\epsilon\)，预测子过程的终端观测。子过程由球形距离 \(dist(z, u) < \epsilon\) 定义（公式 4、6）。通过最小化预测损失（公式 7）迫使概念编码多时间尺度的子目标信息。
- **联合优化**：结合两个损失（公式 8）：\(\mathcal{L}_z = \lambda_{mm}\mathcal{L}_{mm} + \lambda_{mh}\mathcal{L}_{mh}\)。
- **策略增强**：通过联合预测动作和概念（公式 9）将学到的概念集成到现有策略（ACT、扩散策略）中，概念预测正则化动作生成，使策略隐含地利用概念信息。

### 算法流程
- **阶段1（概念发现）**：对批量演示，编码器 E 输出概念序列 → 随机 mask 模态，C 重构 → 随机采样 \(\epsilon\)，推导子过程，F 预测终端观测 → 联合更新 E、C、F。
- **阶段2（策略增强）**：使用编码器 E 为所有演示标注概念，然后训练策略网络同时预测动作和概念，\(\pi_h\) 输出共享表示，\(\pi_z\) 预测概念，\(\pi_a\) 预测动作，损失包含动作误差和概念误差。

## 3. 实验设计

### 数据集与场景
- **LIBERO 基准**（基于 Robosuite）：  
  - **LIBERO-90**：90 个操作任务，作为主要训练域（概念发现和初始策略学习）。每个任务 50 条专家演示。  
  - **LIBERO-LONG**：10 个新长时序任务（每个由两个 LIBERO-90 任务组合），用于测试向复杂结构的迁移。  
  - **LIBERO-GOAL**：10 个全新环境中的任务，用于测试对全新背景的泛化。  
- **多模态观测**：agentview 视觉（128×128 RGB）、眼在手视觉、9 维本体感知状态。
- **真实世界验证**：使用 Mobile ALOHA 机器人执行“清理杯子”任务，训练数据仅含简单容器布置和固定颜色配对，测试 6 种挑战性变体（新布局、新颜色、新物体、障碍物、内部隔板、双手同时抓取）。

### 对比方法
- **概念发现基线**：InfoCon、XSkill、DecisionNCE（两个变体：用任务指令/用动作标签）、RPT、All（本文消融版）、Next（预测相邻时刻）、CLIP、DINOv2。
- **策略基线**：Plain（无概念的标准模仿学习）。  
- **策略架构**：ACT（transformer-based CVAE）和 Diffusion Policy（1D UNet）。所有概念增强通过联合预测实现。

### Benchmark
- 主要指标：任务成功率（%），报告 4 个随机种子的均值和标准差。

## 4. 资源与算力

- 训练在 A800 GPU 上进行（文中提到 GeForce RTX 3090 或 4090 也兼容，但使用 A800 提升效率）。  
- 概念发现训练：200,000 次迭代，batch size 512，每迭代使用长度为 60 的演示片段。完成时间约 1.5 天（单卡 A800）。  
- 策略增强训练的具体算力未单独说明，但基于现有 ACT/DP 框架，开销相似。  
- 注意：未明确给出所有实验的总 GPU 小时数，但指出使用单张 A800 完成概念发现阶段。

## 5. 实验数量与充分性

- **覆盖范围**：  
  - 在 LIBERO-90 上进行概念发现和策略训练（Table 1 的 L90-90 部分）。  
  - 跨任务迁移：LIBERO-90 → LIBERO-LONG（长时序组合）和 LIBERO-90 → LIBERO-GOAL（新环境）。  
  - 消融实验：  
    - 模态消融（Table 2）：移除不同模态组合的效果。  
    - 方法组件消融（Table 8）：仅跨模态 / 仅多时间尺度 / 全方法。  
    - 采样策略消融（Table 7）：均匀 vs 稀疏 vs 偏置采样。  
    - 距离度量消融（Table 10）：球面距离 vs 余弦距离。  
    - 子过程约束消融（Table 11）：序列约束 vs 端点约束。  
    - 未来预测策略消融（Table 12）：本文方法 vs Next-n vs Next-random。  
    - 概念使用方式消融（Table 13）：直接条件 vs 联合预测。  
    - 数据量消融（Table 9）：不同演示数量下的表现。  
  - 真实世界实验（Table 4）：6 种变体场景，各 15 次评估。  
  - 初步 VLA 集成（Fig. 8）：使用 50% 数据微调 OpenVLA-OFT。
- **充分性与公平性**：  
  - 对比了多个主流概念发现和视觉表示方法，覆盖生成式、对比式、掩码自编码器等。  
  - 所有基线在相同数据上训练/测试，超参数尽量一致。  
  - 报告 4 个种子，有标准差，但未提供统计显著性检验。  
  - 消融实验系统，验证了每个设计选择。  
  - 真实实验样本量较小（每个场景 15 次），但展示了趋势。

## 6. 论文的主要结论与发现

- 本文的自监督概念发现方法显著提升了策略在原始任务、长时序组合和新环境中的成功率，优于所有基线（Table 1）。  
- 学到的概念具有以下性质：  
  - **跨模态相关性增强**：条件互信息高于消融版（Table 3）。  
  - **语义对齐**：概念簇与人类定义的子目标高度一致（Fig. 4, Fig. 9）。  
  - **层次化结构**：通过调整阈值 \(\epsilon\) 可自然产生从细粒度到粗粒度的子过程划分（Fig. 3）。  
  - **可迁移性**：在全新环境（LIBERO-GOAL）和真实场景中保持优势。  
- 概念增强策略在真实世界中表现出更好的故障恢复（如重试抓取）和关系焦点（关注“物体-容器”关系而非表面视觉特征）。  
- 多时间尺度预测显示概念能编码不同时间范围的子目标（Fig. 7）。

## 7. 优点

- **自监督、免标注**：完全依靠多模态演示数据内部的统计规律，无需人工标注子目标或语义概念。  
- **层次化表示**：通过时间尺度阈值自然形成树状子目标结构，使策略同时推理短期动作和长期目标。  
- **架构无关性**：概念集成采用联合预测方式，可轻松适配 ACT、DP 等不同策略架构，甚至 VLA 模型。  
- **泛化能力强**：学到的概念聚焦于关系模式（如“放入”），对视觉外观、物体类型变化鲁棒，优于基于语言或固定时间窗口的方法。  
- **分析充分**：提供了互信息分析、语义对齐热图、t-SNE 可视化、多层级结构展示、运动捕获分析等，全面揭示了概念的内在性质。  
- **真实验证**：在 Mobile ALOHA 上进行了 6 种复杂变体测试，展示了实际可用性。

## 8. 不足与局限

- **层次化结构推导的简化**：基于球形距离的阈值切分虽有效，但未显式建模子目标之间的树状关系（如子目标嵌套），且对不同 \(\epsilon\) 之间的关系挖掘不足。  
- **计算资源消耗较大**：概念发现阶段需要 1.5 天单卡 A800，且需要为每个新任务域重新训练概念编码器（尽管可迁移到相关任务）。  
- **多模态依赖**：所有模态必须可用；若某些模态缺失（如无本体感知），性能会显著下降（Table 2）。  
- **真实实验规模有限**：仅一个任务（清理杯子），每个场景 15 次评估，缺乏统计显著性检验和更多机器人平台验证。  
- **公平性考虑**：对比基线（CLIP、DINOv2）仅使用视觉，而本文使用多模态，但已通过消融（Table 2）表明多模态贡献。DecisionNCE 使用了语言，本文方法完全无语言，但仍有优势。  
- **可扩展性未充分验证**：未在大规模异质数据集（如 Open X-Embedding）上测试，也未深度集成到 VLA 模型（仅初步尝试）。  
- **潜在偏差风险**：概念发现依赖演示数据中的模式，若演示存在偏差（如固定物体位置），所学概念可能无法泛化到极端分布外的情况。

（完）
