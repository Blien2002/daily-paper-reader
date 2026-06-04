---
title: "From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots"
title_zh: 从专家到通才：面向人形机器人的通用全身控制
authors: "Yuxuan Wang, Ming Yang, Ziluo Ding, Yu Zhang, Weishuai Zeng, Xinrun Xu, Haobin Jiang, Zongqing Lu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ZBSkyMwdEB"
tags: ["query:vla"]
score: 6.0
evidence: 人形机器人全身控制的专家-通才学习框架
tldr: 人形机器人实现通用敏捷全身控制面临运动多样性和数据冲突的挑战。本文提出BumbleBee框架，通过自编码器聚类将相似运动分组训练专家策略，再结合仿真到真实迁移融合为通才策略。实验表明该方法能在多种复杂运动上达到高性能，推动了机器人全身控制通用化。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-zbskymwdeb/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1263, \"height\": 775, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zbskymwdeb/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1369, \"height\": 740, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zbskymwdeb/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 554, \"height\": 430, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zbskymwdeb/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1453, \"height\": 441, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zbskymwdeb/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1448, \"height\": 532, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zbskymwdeb/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1458, \"height\": 959, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1425, \"height\": 372, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1282, \"height\": 340, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 662, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 571, \"height\": 143, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 863, \"height\": 205, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 689, \"height\": 338, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 861, \"height\": 870, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 861, \"height\": 817, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 502, \"height\": 432, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 583, \"height\": 472, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 436, \"height\": 269, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zbskymwdeb/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1435, \"height\": 228, \"label\": \"Table\"}]"
motivation: 现有单运动专家策略难以泛化到多种行为，需要通用全身控制框架。
method: 提出BumbleBee框架，使用自编码器对运动特征和描述聚类，训练各簇专家策略并融合为通才策略。
result: 在多样化运动任务上实现了优于单任务专家的泛化能力，并经实物验证。
conclusion: 聚类与迁移学习结合可有效实现人形机器人全身控制的通用化。
---

## Abstract
Achieving general agile whole-body control on humanoid robots remains a major challenge due to diverse motion demands and data conflicts. While existing frameworks excel in training single motion-specific policies, they struggle to generalize across highly varied behaviors due to conflicting control requirements and mismatched data distributions. In this work, we propose BumbleBee (BB), an expert-generalist learning framework that combines motion clustering and sim-to-real adaptation to overcome these challenges. BB first leverages an autoencoder-based clustering method to group behaviorally similar motions using motion features and motion descriptions. Expert policies are then trained within each cluster and refined with real-world data through iterative delta action modeling to bridge the sim-to-real gap. Finally, these experts are distilled into a unified generalist controller that preserves agility and robustness across all motion types. Experiments on two simulations and a real humanoid robot demonstrate that BB achieves state-of-the-art general whole-body control, setting a new benchmark for agile, robust, and generalizable humanoid performance in the real world.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

人形机器人实现通用的敏捷全身控制面临两大挑战：一是不同运动（如跳跃、行走、原地站立）对控制的需求差异巨大（高扭矩 vs 平衡平稳），导致数据分布不匹配；二是直接训练统一策略时，任务间的梯度冲突会严重降低性能。现有方法（如OmniH2O、Exbody2、Hover）多为单运动专家策略，难以泛化到多种行为。本文提出**BumbleBee (BB) 框架**，通过“从专家到通才”的学习范式，结合运动聚类、专家策略训练和增量动作模型，最终蒸馏为一个统一的全身控制策略，在仿真和真实机器人上实现了更高敏捷性、鲁棒性和泛化能力。

### 2. 论文提出的方法论

- **核心思想**：先根据运动语义和动力学特征对异构数据进行聚类，在每类上训练专用专家策略（降低冲突），再用专家策略在真实世界收集数据、训练增量动作模型（弥补 sim-to-real 差距），最后通过知识蒸馏将多个专家融合为一个通用通才策略。

- **关键技术细节**：
  1. **数据集构建**：从 AMASS 数据集筛选出 8179 条高质量序列（SMPL 格式），并采用 PHC 过滤。
  2. **自编码器聚类**：
     - 输入：运动序列的关键帧特征（关节3D位置、根平移/速度、接触状态、脚部速度） + 文本描述（来自 HumanML3D）。
     - 编码器：Transformer（运动分支） + BERT+Transformer（文本分支），输出潜变量 \(z_m\) 和 \(z_l\)。
     - 解码器：重建关键关节（头、骨盆、手、脚）的特征。
     - 损失函数：`L_cluster = L_InfoNCE(z_l, z_m) + L2(z_l, z_m) + L_huber(M_hat_l, M) + L_huber(M_hat_m, M)`，实现运动与语义对齐。
     - 最终用 K-means 对 \(z_m\) 聚类，得到6个簇（Jump, Walk-slow, Walk-fast, Stand-up, Stand-mid, Stand-low）。
  3. **专家策略训练**：
     - 先训练一个通用跟踪策略（作为基座），然后在每个簇上微调得到专家策略（MLP，3层，隐藏层1024/1024/512）。
  4. **多阶段增量动作建模**：
     - 部署专家策略到真实机器人，收集各簇的运动轨迹（逐个动作执行多次，共上百条轨迹）。
     - 对每个簇训练独立的 delta 动作模型 \(\pi_\Delta(s_t, a_t)\)，输出补偿动作，使仿真状态转移逼近真实：\(s_{t+1} = f_{\text{sim}}(s_t, a_t + \pi_\Delta(s_t, a_t))\)。
     - 在修正后的仿真环境中继续微调专家策略，迭代多次（实验中迭代2轮）。
  5. **知识蒸馏为通才策略**：
     - 采用 DAgger 方法，用 KL 散度损失将各专家知识融合到统一策略（Transformer 架构，Gated Transformer-XL，序列长度10，6注意力头，隐藏大小128）。
     - 蒸馏时均衡各簇数据比例（1/6）。

### 3. 实验设计

- **数据集**：AMASS 数据集（过滤后 8179 条序列），HumanML3D 文本注释用于聚类。
- **仿真平台**：IsaacGym（训练）、MuJoCo（主要评估，因更接近真实物理）。
- **真实机器人**：Unitree G1（29 DoF，23 主动控制，排除腕关节）。
- **对比方法**：
  - OmniH2O、Exbody2、Hover（均为 SOTA 全身控制方法）。按照官方实现或作者重构，并适配 G1 机器人，使用相同训练数据集。
  - 消融基线：General Init（无专家直接训练通才）、Random（随机划分6个子集训练专家再蒸馏）。
- **评估指标**：
  - Success Rate (SR)：策略成功完成的轨迹比例。
  - Mean Per Joint Position Error (MPJPE)：关节角度误差（弧度）。
  - Mean Per Keypoint Position Error (MPKPE)：关键点位置误差（毫米）。
- **实验安排**：
  - 主实验：表1，在 IsaacGym 和 MuJoCo 上与三个 SOTA 方法对比。
  - 消融实验：表3（聚类 vs 随机 vs 无专家），表4（迭代 delta 微调效果），表5（通用 delta 模型 vs 专属 delta 模型）。
  - 专家 vs 通才对比：图4、图6，展示各簇上专家初始/最终、通才初始/最终的 SR。
  - 聚类分析：表2 给出6个簇的运动学统计（位移、速度、Z方向移动、关节变化等）。
  - 真实世界验证：图5展示迭代微调后足部稳定性提升。

### 4. 资源与算力

论文在附录 B.5（Training Resource）中说明：使用两台同样配置的台式计算机，每台配备 Intel i9-13900 CPU、NVIDIA RTX 4090 GPU、64 GB RAM。总训练算力为 2×RTX 4090。具体训练时长未明确给出，但提及每次迭代需在真实世界收集数据（每簇20个动作，每个动作约8秒，每个动作跑8次），在仿真中微调。算力信息比较清晰。

### 5. 实验数量与充分性

- **实验数量**：主实验 1 个表（两个仿真环境 vs 3 个基线）；消融实验 4 个表（表3、4、5、6）；专家/通才对比 2 个图（图4、6）；聚类分析 1 个表（表2）；真实世界定性展示 1 个图（图5）。实验组数较多，覆盖了聚类有效性、迭代微调效果、delta 模型专有性、专家与通才的关系等关键方面。
- **充分性与公平性**：对比方法均使用相同数据集和机器人模型，且为公平起见对 Hover 评估时使用未遮蔽观测。消融实验设计合理（随机划分无益，聚类有益；通用 delta 模型不如专属模型）。统计显著性表12给出了置信区间。但未在更多机器人（如 H1 等）上验证，泛化能力有待进一步测试。

### 6. 论文的主要结论与发现

1. **专家-通才框架有效**：BB 在 MuJoCo 上 SR 达 66.84%，显著高于 Exbody2 (50.19%) 和其他基线（<40%），在 IsaacGym 上亦最优。
2. **聚类至关重要**：随机划分专家无优势，而基于语义-运动学聚类显著提升性能。
3. **迭代 delta 微调提升显著**：专家 SR 从 Iter 0 的 51.49% 升至 Iter 2 的 70.37%，且真实世界中效果逐次改善。
4. **专属 delta 模型优于通用模型**：在跳跃等剧烈运动上差异明显（专属 68.92% vs 通用 50.71%）。
5. **最终通才有时优于单个专家**：对初始困难的动作（如跳跃、慢走），通才通过继承多专家稳定行为而表现更好。

### 7. 优点

- **创新性**：首次将“从专家到通才”思路用于人形机器人全身控制，巧妙融合运动聚类、增量动作模型和知识蒸馏。
- **方法完整**：从数据聚类到专家训练、sim-to-real 迁移、最终蒸馏，形成了闭环 pipeline，且每个模块都有明确动机和实验支撑。
- **实验充分**：在两种仿真 + 真实机器人上验证，包含多种消融，指标全面（SR + 精度），且提供了置信区间。
- **实用性强**：基于 AMASS 通用运动数据集，不依赖昂贵动捕系统（仅用里程计），在低成本机器人 G1 上实现，有部署价值。

### 8. 不足与局限

- **传感器限制**：目前未使用 GPS 或 VIO，缺少全局定位信息，可能引起参考轨迹对齐偏差。
- **管道复杂性**：整个 pipeline（聚类→专家训练→数据收集→delta 训练→迭代→蒸馏）步骤多，可扩展性受限，尤其在需要频繁真人参与收集数据时。
- **运动范围有限**：仅测试了 6 类运动，未涵盖更复杂的行为（如爬行、翻滚、操作物体等）。
- **硬件单一**：只在 Unitree G1 上验证，通用性未在其他机器人型号上证明。
- **实验未讨论超参数敏感性**：如聚类数 K（通过肘部法则选为6），但未验证 K 值变化的影响。

（完）
