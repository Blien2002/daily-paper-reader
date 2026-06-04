---
title: Active Fine-Tuning of Multi-Task Policies
title_zh: 多任务策略的主动微调
authors: "Marco Bagatella, Jonas Hübotter, Georg Martius, Andreas Krause"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=hlyBdwHBeC"
tags: ["query:vla"]
score: 7.0
evidence: 主动选择演示数据用于机器人多任务策略微调
tldr: 针对机器人多任务学习中的演示预算有限问题，本文提出AMF算法，通过交互式框架自适应选择需要演示的任务。AMF基于预期策略改进的信息增益进行任务选择，在有限的演示次数下最大化多任务策略性能。该方法为高效微调通用机器人模型提供了实用策略。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 834, \"height\": 248, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1779, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 322, \"height\": 318, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1738, \"height\": 1009, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 672, \"height\": 465, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 981, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1773, \"height\": 2301, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1768, \"height\": 629, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1412, \"height\": 626, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 867, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1412, \"height\": 515, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 765, \"height\": 536, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1765, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1752, \"height\": 655, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1439, \"height\": 1001, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1438, \"height\": 1002, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1783, \"height\": 1004, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1787, \"height\": 1005, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1732, \"height\": 448, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1754, \"height\": 934, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-hlybdwhbec/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 878, \"height\": 1127, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-hlybdwhbec/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 851, \"height\": 503, \"label\": \"Table\"}]"
motivation: 多任务策略微调需要决定哪些任务需要演示以及频率，但通常缺乏系统方法。
method: 提出AMF算法，基于信息增益主动选择能最大程度提升策略性能的任务进行演示。
result: 在有限演示预算下显著提升了多任务策略的性能。
conclusion: 主动任务选择策略能有效提高多任务机器人学习的样本效率。
---

## Abstract
Pre-trained generalist policies are rapidly gaining relevance in robot learning due to their promise of fast adaptation to novel, in-domain tasks.
This adaptation often relies on collecting new demonstrations for a specific task of interest and applying imitation learning algorithms, such as behavioral cloning.
However, as soon as several tasks need to be learned, we must decide *which tasks should be demonstrated and how often?*
We study this multi-task problem and explore an interactive framework in which the agent *adaptively* selects the tasks to be demonstrated.
We propose AMF (Active Multi-task Fine-tuning), an algorithm to maximize multi-task policy performance under a limited demonstration budget by collecting demonstrations yielding the largest information gain on the expert policy.
We derive performance guarantees for AMF under regularity assumptions and demonstrate its empirical effectiveness to efficiently fine-tune neural policies in complex and high-dimensional environments.

---

## 论文详细总结（自动生成）

## 论文总结：Active Fine-Tuning of Multi-Task Policies

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：随着大规模预训练通用策略（generalist policies）在机器人学习中的兴起，如何高效地微调这些策略以适应多个新任务成为一个关键挑战。传统微调依赖为每个任务收集新的专家演示，但多任务场景下需要决定“哪些任务应该被演示，以及演示多少次”，以避免资源浪费。
- **核心问题**：在有限演示预算下，如何自适应地选择任务以最大化多任务策略的整体性能？
- **整体含义**：本文提出主动多任务微调（AMF）框架，通过交互式机制让智能体主动请求最有信息量的演示，从而高效提升多任务策略性能，并提供了理论收敛保证与实证验证。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：基于贝叶斯信息论，选择能最大化专家策略后验信息增益的任务进行演示，即选择使策略熵下降最快的任务。
- **关键技术细节**：
  - **信息增益准则**：每个回合选择任务`c'`使得预期互信息最大：  
    `c_n = argmax_{c'} E[ Σ_t I(π(s_t,c); τ(c') | 历史数据) ]`
  - **理论保证**：在马尔可夫决策过程（MDP）满足利普希茨光滑、策略属于再生核希尔伯特空间等正则性假设下，AMF策略与专家策略的差距以 `O(γ(Hn)/√n)` 速率收敛（高概率），其中γ(Hn)为最大信息增益（对常见核为次线性）。
  - **实际算法（AMF-NN）**：
    1. 当策略为神经网络时，利用损失梯度嵌入（loss gradient embeddings）将网络近似为高斯过程（GP），从而高效估计条件熵。
    2. 通过重要性采样估计未来任务的轨迹分布（利用已收集轨迹的似然比）。
    3. 提出“自适应先验（Adaptive Prior）”机制缓解灾难性遗忘：将微调策略与冻结的预训练策略按任务自适应的权重混合，权重通过带保守惩罚的BC损失训练。
  - **算法流程**（Algorithm 1）：初始化空数据集，每轮选择最优任务`c_n`，收集演示，每B轮后更新策略。

### 3. 实验设计：数据集/场景、基准、对比方法
- **实验场景**：
  - **GP环境**：2D积分器（点质点到目标点任务，连续任务空间）。
  - **高维任务**：FrankaKitchen（5个操作任务）、Metaworld（4个机器人操作任务）、Robomimic（4个长时程精密操作任务，人类演示）、WidowX（使用Octo预训练模型）。
- **基准方法**：均匀随机任务采样（Uniform）、带自适应先验的均匀采样（Uniform with adaptive prior）、重平衡（Rebalancing，可访问预训练分布的特权基线）。
- **对比方法**：不同不确定性估计方案（最后层梯度、Dropout）、不同遗忘缓解技术（L2正则、EWC）。

### 4. 资源与算力
- 论文未明确说明使用的GPU型号、数量或总训练时长。仅在附录M.4中提到“每个AMF-NN实验在GPU加速下最多5小时，数据选择每轮<1秒；AMF-GP实验10分钟内可在CPU上复现”。未提供具体硬件配置。

### 5. 实验数量与充分性
- **实验数量**：
  - GP环境：覆盖12种预训练分布（从1/12到12/12任务演示），每种10个随机种子。
  - 高维场景：FrankaKitchen和Metaworld各在状态输入和视觉输入下，评估不匹配与匹配两种预训练情况；额外进行不同预训练分配（共数十种子）。
  - 消融实验：不确定性估计对比（3种方法）、遗忘缓解对比（3种方法+自适应先验）、重平衡对比。
  - 其他：Robomimic（扩散策略）、WidowX（Octo通用策略）各一组实验。
- **充分性与公平性**：实验覆盖了多种任务复杂度、预训练偏移程度和策略架构，指标（成功率、回报）均报告均值和90%自助法置信区间（10个种子），对比方法均有公平设置。主要结论（AMF在分布不匹配时优势显著，在匹配时不低于随机）有充分支持。但缺少在大规模通用策略（如RT-2）上的全量微调评估，数据点相对有限。

### 6. 论文的主要结论与发现
- AMF算法在理论上有收敛保证，在实践中能显著加速多任务策略微调，尤其当预训练分布与目标分布不匹配时。
- AMF通过自动“重平衡”演示分配（优先选择预训练未充分覆盖的任务），接近甚至超过知悉预训练分布的特权基线。
- 提出的“自适应先验”有效缓解灾难性遗忘，使策略保留预训练技能。
- 当预训练覆盖均匀时，AMF性能与均匀采样相当；但从不低于均匀采样。
- AMF可应用于多种策略类（GP、MLP、扩散策略）和任务形式（状态、视觉输入），具有良好通用性。

### 7. 优点
- **理论创新**：首次为主动多任务行为克隆提供性能收敛保证，将信息论主动学习拓展到动态系统。
- **实践实用**：方法对预训练数据不可见、不使用rehearsal，适用于实际部署；自适应先进一步址了微调中的灾难性遗忘。
- **实验全面**：覆盖多种环境、多种预训练偏移、多种策略架构，消融实验分析各组件贡献。
- **可复现**：开源代码，附录提供实现细节和超参数。

### 8. 不足与局限
- **规模限制**：未在超大规模通用策略（如RT-2、Octo全参数微调）上验证，仅测试了小型到中等模型。
- **不确定性估计依赖**：AMF-NN依赖损失梯度嵌入近似GP，该方法在深度网络上的准确性可能有限，且不适用于无法求梯度的策略（如扩散策略在确定性模式下需特殊处理）。
- **实验种子数**：仅10个种子，对于高维任务可能不足以保证统计稳定性；某些置信区间重叠较大。
- **任务空间假设**：在无限/连续任务空间时，需依赖离散化或采样优化，可能降低效率。
- **性能增益局限**：当预训练已均匀覆盖所有任务时，AMF增益不大，符合预期但不惊艳。
- **假设前提**：理论证明依赖利普希茨光滑、RKHS等较强假设，实际环境可能不满足。

（完）
