---
title: "BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models"
title_zh: "BridgeVLA: 输入输出对齐的高效3D操作学习"
authors: "Peiyan Li, Yixiang Chen, Hongtao Wu, Xiao Ma, Xiangnan Wu, Yan Huang, Liang Wang, Tao Kong, Tieniu Tan"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ffBF6hYuQv"
tags: ["query:vla"]
score: 10.0
evidence: 直接用于3D操作的VLA模型
tldr: 现有视觉-语言-动作（VLA）模型未充分利用3D空间结构，导致数据效率低下。BridgeVLA提出一种新范式：先预训练VLM使其输出2D热图，再微调时对齐3D点云与动作空间。该方法在3D操作任务上以更少样本达到更高性能，为构建高效的3D VLA模型奠定了基础。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1404, \"height\": 797, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1388, \"height\": 542, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1359, \"height\": 733, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 679, \"height\": 555, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1435, \"height\": 1244, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1062, \"height\": 1919, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1454, \"height\": 1646, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1454, \"height\": 1461, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1287, \"height\": 1964, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1431, \"height\": 1082, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1432, \"height\": 1823, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1446, \"height\": 1205, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1238, \"height\": 1465, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ffbf6hyuqv/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1091, \"height\": 1853, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1442, \"height\": 804, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1442, \"height\": 396, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1398, \"height\": 302, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1442, \"height\": 437, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1453, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1438, \"height\": 654, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1435, \"height\": 734, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1443, \"height\": 656, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1442, \"height\": 743, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1438, \"height\": 775, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1438, \"height\": 578, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ffbf6hyuqv/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1155, \"height\": 667, \"label\": \"Table\"}]"
motivation: 现有VLA未充分利用3D空间结构，数据效率低。
method: 预训练VLM输出2D热图，微调时对齐点云与动作。
result: 在3D操作任务中以更少样本达到更高性能。
conclusion: 输入输出对齐是构建高效3D VLA的关键。
---

## Abstract
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low data efficiency. In this paper, we introduce a new paradigm for constructing 3D VLAs. Specifically, we first pre-train the VLM backbone to take 2D images as input and produce 2D heatmaps as output. Using this pre-trained VLM as the backbone, we then fine-tune the entire VLA model while maintaining alignment between inputs and outputs by: (1) projecting raw point cloud inputs into multi-view images, and (2) predicting heatmaps before generating the final action. Extensive experiments show that the resulting model, BridgeVLA, can learn 3D manipulation both efficiently and effectively. BridgeVLA outperforms state-of-the-art baselines across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4\% to 88.2\%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from  56.7\% to 64.0\%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32\% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 95.4\% on 10+ tasks with only 3 trajectories per task, while other VLA methods such as $\pi_{0}$ fail completely. Project Website: https://bridgevla.github.io/.

---

## 论文详细总结（自动生成）

## 详细中文总结

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有利用预训练视觉-语言模型（VLM）构建视觉-语言-动作（VLA）模型的方法在机器人操作学习中展现出潜力，但绝大多数方法仅使用2D图像输入，数据效率低；少数引入3D信号的方法未能充分利用3D数据的空间结构，导致样本效率不足。此外，微调阶段3D输入与VLM预训练时的2D图像之间存在分布偏移。
- **整体含义**：论文旨在构建一个统一的高效3D VLA模型，既融合VLM的广泛知识，又利用3D策略的空间结构先验，实现样本高效、鲁棒泛化的3D机器人操作学习。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：通过输入-输出对齐，将观察输入和动作输出统一到共享的2D图像空间中，从而利用VLM预训练知识和3D空间结构。
- **关键技术细节**：
  1. **2D热图预训练**：在VLM骨干（PaliGemma，含SigLIP视觉编码器+Gemma transformer）上增加一个凸上采样模块（convex upsampling block），预训练模型根据图像和文本描述输出2D热图，定位目标物体。损失函数为交叉熵。预训练数据集利用RoboPoint的120K物体检测子集，构造归一化的高斯热图作为真值。
  2. **3D动作微调**：
     - **输入对齐**：将RGB-D图像重建的点云从俯视、前视、右视三个正交投影视图渲染成2D图像，作为VLM骨干的输入（3张图片）。
     - **输出对齐**：模型对每个视图预测一个2D热图，热图分辨率与输入图像相同。通过反投影三个热图得到3D点网格的得分，选择最高点作为末端执行器平移。
     - **其余动作分量**：旋转（欧拉角离散化为72个bin，交叉熵损失）、夹爪状态、碰撞标志（二分类交叉熵损失）通过MLP从全局和局部特征池化后的tokens预测。
     - **粗到细策略**：第一次预测后，以预测平移为中心裁剪放大点云，进行第二次前向传播，执行第二次预测的动作。
  3. **保持预训练-微调对齐**：微调时不向VLM骨干注入额外3D位置信息（避免分布偏移），仅使用2D投影图像。

### 3. 实验设计：数据集、场景、Benchmark、对比方法

- **仿真实验**：
  - **RLBench**：18个任务，每任务100个演示，评估二元成功率（25次试次）。对比方法包括Image-BC (CNN/ViT)、C2F-ARM-BC、HiveFormer、PolarNet、PerAct、Act3D、RVT、3D Diffuser Actor、RVT-2等。
  - **COLOSSEUM**：20个任务，12种未见过扰动（纹理、颜色、大小、背景、灯光、干扰物、相机位姿等）及所有扰动组合。训练数据来自原始RLBench。对比方法包括R3M-MLP、MVP-MLP、PerAct、RVT、RVT-2。
  - **GemBench**：层级泛化基准（L1-L4），训练集16任务（31变体），测试集44任务（92变体）。对比方法包括HiveFormer、PolarNet、3D Diffuser Actor、RVT-2、3D-LOTUS、3D-LOTUS++。
- **真实机器人实验**：Franka Research 3机械臂+ZED 2i深度相机，13个任务，每任务10条轨迹训练（部分3条）。设置7种场景：Basic、Distractor、Lighting、Background、Height、Combination、Category。对比方法包括SpatialVLA、π0、ACT、RVT-2。
- **消融实验**：热图预测 vs 直接回归（BridgeVLA w/o heat）、添加3D位置输入（BridgeVLA w pos）、2D热图预训练 vs 无预训练（BridgeVLA w/o Pre-train）。

### 4. 资源与算力

- **预训练**：8块NVIDIA A100 GPU，3800步（约2小时）。
- **RLBench微调**：48块NVIDIA H100 GPU，83000步（约20小时）。
- **COLOSSEUM微调**：48块NVIDIA H100 GPU，83000步（约20小时）。
- **GemBench微调**：40块NVIDIA A100 GPU，50 epochs（约2.1小时）。
- **真实机器人微调**：8块NVIDIA A100 GPU，300 epochs（约1.5小时）。
- **推理**：单块NVIDIA RTX 4090，平均端到端0.21秒。

### 5. 实验数量与充分性

- **实验数量**：覆盖3个仿真基准（共约55+任务）、真实7个场景共13个任务，每组实验多次试次（仿真25次/任务，真实10次/任务），消融实验3组。
- **充分性与公平性**：
  - 多个基准上均与多个SOTA方法对比，采用标准评估协议（RLBench 25次，GemBench 5次随机种子，COLOSSEUM 3次测试重复）。
  - 真实实验手动对齐场景，确保公平比较。
  - 消融实验验证了核心组件（热图预测、无3D位置注入、预训练）的必要性。
  - 实验设计较为充分，统计误差（标准差/波动）被报告，结果可信。

### 6. 论文的主要结论与发现

- BridgeVLA在三个仿真基准中均达到新的SOTA：RLBench平均成功率88.2%（提升6.8%）、COLOSSEUM 64.0%（提升7.3%）、GemBench 50.0%。
- 真实世界实验中，BridgeVLA在Basic场景以10条轨迹取得96.9%成功率，仅需3条轨迹即可达95.4%，远超其他方法（SpatialVLA、π0、ACT完全失败）。
- 在视觉扰动（干扰物、光照、背景、高度）和语义泛化（新物体-技能组合、新类别）中，BridgeVLA显著优于RVT-2（均值高32%），尤其是光照和组合泛化。
- 消融实验证明热图预测、不引入3D位置特征、2D热图预训练均对性能至关重要。

### 7. 优点

- **输入-输出对齐设计**：将3D点云投影为2D图像并预测2D热图，巧妙地将VLM的2D预训练能力与3D空间结构统一，极大提升样本效率。
- **高效的热图预训练**：使VLM学会输出热图，避免从头训练，且可扩展至更多视觉任务。
- **粗到细策略**：通过两次前向传播提升平移精度。
- **极强的数据效率**：3条轨迹/任务即可达到95%+成功率，远优于现有VLA方法。
- **鲁棒泛化**：在多种未见视觉干扰和语义组合中保持高成功率。

### 8. 不足与局限

- **预训练-微调数据域差异**：预训练图像多为第三人称视角，与机器人正交投影图不同；预训练只学习物体定位，而操作需预测不直接对应物体的关键点（如放置点），导致类别泛化成功率偏低。
- **遮挡问题**：在Place Cups等任务中目标关键点被遮挡，性能受限（虽仍优于基线）。
- **长程任务表现弱**：在GemBench L4长程任务（需多步组合）中成功率为0，类似大多数基线，尚未引入语言模型进行任务分解。
- **未充分探索其他动作解码方法**（如扩散模型），未来可进一步改进。
- **实验仅使用单一真实机器人平台和一种VLM（PaliGemma）**，结论的跨平台、跨模型泛化性待验证。

（完）
