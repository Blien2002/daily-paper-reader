---
title: "Rethinking Latent Redundancy in Behavior Cloning: An Information Bottleneck Approach for Robot Manipulation"
title_zh: 重新思考行为克隆中的潜在冗余：面向机器人操作的信息瓶颈方法
authors: "Shuanghao Bai, Wanqi Zhou, Pengxiang Ding, Wei Zhao, Donglin Wang, Badong Chen"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=N2Dey442PJ"
tags: ["query:vla"]
score: 7.0
evidence: 信息瓶颈方法用于机器人操作的行为克隆
tldr: 针对行为克隆中潜在表示冗余且缺乏理论基础的问题引入互信息量化冗余并基于信息瓶颈原理指导学习。在机器人操作基准上该方法减少了表示冗余提升了策略泛化能力并提供了理论支撑。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 842, \"height\": 359, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1652, \"height\": 545, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 866, \"height\": 1045, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1750, \"height\": 680, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 856, \"height\": 513, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1783, \"height\": 506, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 830, \"height\": 514, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1752, \"height\": 444, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1760, \"height\": 490, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1745, \"height\": 672, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1290, \"height\": 833, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n2dey442pj/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 857, \"height\": 511, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1781, \"height\": 730, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1655, \"height\": 478, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 774, \"height\": 537, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 703, \"height\": 547, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 649, \"height\": 539, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1614, \"height\": 655, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1662, \"height\": 622, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1660, \"height\": 621, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n2dey442pj/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 443, \"height\": 197, \"label\": \"Table\"}]"
motivation: 行为克隆学到表示中存在冗余信息缺乏理论指导。
method: 利用互信息量化冗余结合信息瓶颈原理优化潜在表示。
result: 在机器人操作任务上降低了表示冗余提升了泛化性能。
conclusion: 信息瓶颈为行为克隆提供了一种理论驱动的表示学习框架。
---

## Abstract
Behavior Cloning (BC) is a widely adopted visual imitation learning method in robot manipulation. Current BC approaches often enhance generalization by leveraging large datasets and incorporating additional visual and textual modalities to capture more diverse information. However, these methods overlook whether the learned representations contain redundant information and lack a solid theoretical foundation to guide the learning process. To address these limitations, we adopt an information-theoretic perspective and introduce mutual information to quantify and mitigate redundancy in latent representations. Building on this, we incorporate the Information Bottleneck (IB) principle into BC, which extends the idea of reducing redundancy by providing a structured framework for compressing irrelevant information while preserving task-relevant features. This work presents the first comprehensive study on redundancy in latent representations across various methods, backbones, and experimental settings, while extending the generalizability of the IB to BC. Extensive experiments and analyses on the CortexBench and LIBERO benchmarks show consistent performance improvements with IB across various settings, underscoring the importance of reducing input data redundancy and highlighting its practical value for real-world applications.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **研究动机**：行为克隆（Behavior Cloning, BC）在机器人操作中依赖大规模数据和多模态输入（视觉、文本等）来提升泛化能力，但现有方法忽视了学习到的潜在表示中存在的**冗余信息**，且缺乏理论指导来规范化表示学习过程。
- **核心问题**：如何形式化地量化并减少输入或表示中的冗余，同时保持任务相关特征？
- **整体含义**：本文首次从信息论视角系统研究BC中的潜在冗余，引入互信息（Mutual Information）来量化冗余，并基于信息瓶颈（Information Bottleneck, IB）原理构建压缩-预测权衡框架，为BC提供理论驱动的表示学习范式。

## 2. 提出的方法论

### 2.1 核心思想

- 将BC的流程建模为信息流：输入多模态特征 \( X \) → 潜在表示 \( Z \) → 动作 \( A \)。
- 冗余量化为互信息 \( I(X; Z) \)，IB的目标是**最小化 \( I(X; Z) \)** 的同时**最大化 \( I(Z; A) \)**，即压缩无关信息、保留任务相关特征。
- 最终损失函数为：
  \[
  \mathcal{L}_{\text{BC-IB}} = \mathbb{E}_{(x_t, a_t) \sim \mathcal{D}_e} \left[ \beta I(x_t; z_t) + \|\pi(x_t) - a_t\|^2 \right]
  \]
  其中 \( \beta > 0 \) 控制压缩强度，\( \pi \) 为策略网络。

### 2.2 关键技术细节

- **互信息估计**：使用MINE（Mutual Information Neural Estimation）基于Donsker-Varadhan表示，通过神经网络判别器 \( T_\theta \) 估计 \( I(X; Z) \)。
- **模型架构分类**：根据特征融合方式分为**空间融合**（MLP/CNN/空间Transformer）和**时间融合**（RNN/LSTM/时间Transformer），分别适用于不同任务复杂度。
- **理论分析**：推导了泛化误差上界与 \( I(X; Z) \) 正相关（定理4.1、4.2），并证明对中间特征 \( X \) 压缩可有效控制 \( I(O; Z) \)（定理4.3），误差有界。

### 2.3 算法流程

1. 提取各模态特征（视觉编码器、本体感知编码器、语言编码器）并拼接为 \( X \)。
2. 通过融合模块（空间或时间）得到潜在表示 \( Z \)。
3. 策略头（MLP）输出动作 \( A \)。
4. 优化目标：BC回归损失 + β * MINE估计的互信息。

## 3. 实验设计

### 3.1 数据集与基准

- **CortexBench**：单任务基准，包含4个模拟器（Adroit、Meta-World、DMControl、TriFinger）共14个任务。每个任务使用25-100条专家轨迹。
- **LIBERO**：语言条件多任务基准，包含4套子集（LIBERO-Goal/ Object/ Spatial/ Long）共40个任务。每任务50条轨迹（常用45条训练、5条评估）。
- **真实世界实验**：UR5机械臂 + Robotiq 2F-85夹爪 + RealSense L515相机，设计Pick和Put（Pick-and-Place）任务，单任务25-50条演示，多任务800条演示（200条/任务）。

### 3.2 对比方法

- **全微调基线**：ResNet-18、ViT-S（从头训练）。
- **部分微调基线**：R3M、Voltron、VC-1、MPI（使用预训练编码器冻结）。
- **融合方式**：MLP（空间融合）、RNN/Transformer（时间融合）。
- 所有基线均与BC+IB版本对比，标记为“+IB”。

### 3.3 评估指标

- 成功率的平均值与标准差（3个随机种子）。

## 4. 资源与算力

- **模拟实验**：单张NVIDIA V100或A100 GPU（CUDA 11.8），12个CPU。
- **真实世界单任务**：单张V100 GPU + 12 CPU。
- **真实世界语言条件多任务**：8张A100 GPU训练，单张A100评估，100 CPU。
- 论文未详细报告训练时长（如每轮epoch的耗时），但基于典型配置可推测训练周期在数小时至数十小时范围内。

## 5. 实验数量与充分性

- **全面性**：覆盖14个单任务 + 40个多任务 + 真实世界2个任务，使用6种不同视觉编码器（ResNet, ViT, R3M, Voltron, VC-1, MPI）和多种融合方式，共进行了**数十组对比实验**。
- **消融与扩展**：
  - β参数敏感性分析（图5）。
  - 不同演示数量（1/5/10/20 few-shot）实验（图7、12）。
  - 注意力图可视化（图11）说明IB使模型聚焦任务相关区域。
  - LIBERO-Long上使用Diffusion Policy策略头验证可扩展性（表9）。
- **公平性**：所有基线使用相同超参数设置，仅添加IB相关模块（MINE+β），训练配置保持一致；模型选择策略明确（单任务选最高成功率，多任务选最终epoch）。
- **充分性评价**：实验设计较为充分，涵盖了多种任务复杂度、数据量、融合方式，并提供了理论分析支持。但未涉及大规模VLA模型（如RT-2、OpenVLA），且领域迁移鲁棒性测试不足。

## 6. 主要结论与发现

1. **IB一致提升性能**：在CortexBench和LIBERO所有任务上，BC+IB均优于或不低于原始BC，部分任务提升显著（如ResNet+IB在DMControl上+10.01%，VC-1+IB在Meta-World上+4.80%）。
2. **冗余存在性**：性能提升间接证明当前BC表示中存在大量冗余信息，压缩有益。
3. **融合方式适用性**：空间融合更适合简单单任务；时间融合（尤其Transformer）在复杂多任务（如LIBERO）中优势明显。
4. **IB有效性条件**：β在1e-4附近稳定提升；IB在少样本、小数据场景下同样有效。
5. **互信息下降**：IB方法使 \( I(X; Z) \) 显著降低（如LIBERO-Goal中降至原来的1/4），同时成功率提升。

## 7. 优点

- **理论创新**：首次将信息瓶颈系统引入机器人操作行为克隆，提供了泛化误差上界的理论证明，弥补了BC缺乏理论指导的空白。
- **方法通用性**：IB模块可即插即用于多种视觉编码器、融合方式和策略头，不依赖特定架构。
- **实验全面性**：涵盖模拟和真实世界、单任务和多任务、全微调和部分微调、不同数据量级（full-shot到few-shot），验证了方法的鲁棒性。
- **分析深入**：通过对注意力图、互信息值、β参数的可视化与敏感性分析，提供对模型行为的清晰理解。

## 8. 不足与局限

- **未验证大规模模型**：未评估IB在Vision-Language-Action（VLA）类架构（如RT-2、OpenVLA）中的效果，后者计算资源需求高，论文未涉及。
- **策略头种类有限**：仅使用MLP作为策略头，未探索Diffusion Policy、Transformer head或token化动作等设计（仅在附录中对LIBERO-Long实验补充了Diffusion Policy）。
- **领域迁移鲁棒性不足**：未系统测试环境、光照、背景、物体实例变化下的泛化能力，仅通过在真实世界中引入未见物体组合做了初步验证。
- **互信息估计误差**：使用MINE估计互信息可能存在估计偏差，且超参数（网络结构、学习率）需调优，可能影响IB效果。

---

（完）
