---
title: "URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model"
title_zh: URDF-Anything：利用3D多模态语言模型构建铰接物体
authors: "Zhe Li, Xiang Bai, Jieyu Zhang, Zhuangzhe Wu, Che Xu, Ying Li, Chengkai Hou, Shanghang Zhang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=g3EF5XsapH"
tags: ["query:vla"]
score: 7.0
evidence: 利用3D多模态大语言模型端到端重建铰接物体用于机器人仿真
tldr: "构建铰接物体数字孪生对于机器人仿真训练至关重要，但传统方法需要大量人工。本文提出URDF-Anything，一个基于3D多模态大语言模型的端到端自动重建框架。它通过点云与文本的多模态输入，利用自回归预测和专用[SEG]令牌机制联合优化几何分割与运动学参数，无需多阶段流水线。实验表明该方法在多种物体上实现高精度重建，为具身AI仿真提供关键支撑。"
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1402, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1432, \"height\": 536, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1384, \"height\": 1247, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1420, \"height\": 775, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1432, \"height\": 909, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1427, \"height\": 643, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1386, \"height\": 837, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1377, \"height\": 1918, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-g3ef5xsaph/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1277, \"height\": 556, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1453, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1460, \"height\": 290, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1115, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1482, \"height\": 319, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1406, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 785, \"height\": 243, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 655, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1204, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1290, \"height\": 242, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1453, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1111, \"height\": 183, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-g3ef5xsaph/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1086, \"height\": 183, \"label\": \"Table\"}]"
motivation: 手动构建铰接物体数字孪生耗时且繁琐，缺乏自动化的端到端解决方案。
method: "基于3D多模态大语言模型，采用自回归预测和[SEG]令牌机制联合优化几何分割与运动学参数。"
result: 在多个铰接物体类别上实现精确的几何和运动学重建，优于现有方法。
conclusion: URDF-Anything大幅简化了机器人仿真场景的构建流程，有利于具身智能研究。
---

## Abstract
Constructing accurate digital twins of articulated objects is essential for robotic simulation training and embodied AI world model building, yet historically requires painstaking manual modeling or multi-stage pipelines. In this work, we propose \textbf{URDF-Anything}, an end-to-end automatic reconstruction framework based on a 3D multimodal large language model (MLLM). URDF-Anything utilizes an autoregressive prediction framework based on point-cloud and text multimodal input to jointly optimize geometric segmentation and kinematic parameter prediction. It implements a specialized [SEG] token mechanism that interacts directly with point cloud features, enabling fine-grained part-level segmentation while maintaining consistency with the kinematic parameter predictions.
Experiments on both simulated and real-world datasets demonstrate that our method significantly outperforms existing approaches regarding geometric segmentation (mIoU 17\% improvement), kinematic parameter prediction (average error reduction of 29\%), and physical executability (surpassing baselines by 50\%). Notably, our method exhibits excellent generalization ability, performing well even on objects outside the training set. This work provides an efficient solution for constructing digital twins for robotic simulation, significantly enhancing the sim-to-real transfer capability.

---

## 论文详细总结（自动生成）

# 论文《URDF-Anything: Constructing Articulated Objects with 3D Multimodal Language Model》详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：在机器人仿真训练与具身AI世界模型构建中，需要高保真的铰接物体数字孪生（如带门、抽屉的家具）。传统方法依赖人工手动建模或多阶段流水线，耗时且缺乏自动化。
- **核心问题**：如何从视觉观测（单/多视图图像）自动、端到端地生成可用于物理仿真的完整URDF模型（包含几何分割 + 运动学参数）。
- **整体意义**：提出首个基于3D多模态大语言模型（MLLM）的端到端重建框架，显著降低构建数字孪生的人力成本，提升仿真到真实迁移的鲁棒性。

## 2. 方法论

- **核心思想**：利用3D MLLM（ShapeLLM）同时处理点云几何特征与文本指令，通过自回归方式联合预测运动学参数（关节类型、原点、轴、父子关系）和部件级分割掩码，输出的[SEG] token经交叉注意力机制直接与点云特征交互，实现一致的几何-运动学预测。
- **关键技术细节**：
  - **输入表示**：多视图时使用DUSt3R生成密集点云；单视图时先用扩散模型合成多视图，再用LGM重建点云。
  - **3D MLLM骨干**：采用ShapeLLM-7B（Uni3D编码器 + LLaMA），通过LoRA微调。
  - **[SEG] token机制**：扩展LLM词表，使模型在生成JSON输出时对每个部件附加[SEG] token；其隐藏状态与部件类别token融合，作为查询与点云特征进行交叉注意力，输出每点得分 → 二值掩码。
  - **公式**：总体损失 \(L = \lambda_{\text{text}} L_{\text{text}} + \lambda_{\text{seg}} \sum_{i} L_{i,\text{seg}}\)，其中 \(L_{\text{seg}}\) 为BCE + Dice损失。
  - **最终输出**：分段点云转换为网格（点→网格算法），连同JSON解析的运动学参数组装成URDF文件。

## 3. 实验设计

- **数据集**：PartNet-Mobility。分为**In-Distribution（ID）**：5类（Laptop, Box, Refrigerator, StorageFurniture, Table）和**Out-of-Distribution（OOD）**：其余41类，用于测试泛化性。通过SAPIENS模拟器渲染多视图图像，生成点云作为输入。
- **Benchmark**：几何分割（mIoU、Count Accuracy）、运动学参数预测（Type Error、Axis Error、Origin Error）、物理可执行性（成功率）。
- **对比方法**：
  - 分割基线：Uni3D w/o text（仅几何）、Uni3D w/ text（文本引导分割）。
  - 完整重建基线：Articulate-Anything（迭代细化+网格检索）、Real2Code（OBB+LLM参数预测）、URDFormer（流水线）。
  - 消融：输入模态（2D图像、OBB、纯点云、点云+文本）、联合预测 vs 独立预测（Kinematics-Only、Segmentation-Only）。

## 4. 资源与算力

- **GPU**：单张NVIDIA A800 80GB GPU。
- **训练时长**：2.5小时。
- **微调方法**：LoRA（秩=8），优化器AdamW（lr=0.0003，weight decay=0），余弦学习率调度，batch size=2，梯度累积步数=10。

## 5. 实验数量与充分性

- **实验数量**：包含三大类主要实验（分割、运动学、物理可执行性），多组消融（输入模态、联合预测重要性、上下文融合机制）、零样本仿真-真实泛化测试、故障案例分析、形状重建质量（Chamfer距离）对比。
- **充分性与公平性**：
  - 分割实验：对比了两种Uni3D变体，报告了均值 ± 标准差。
  - 运动学实验：对比了三个基线（Real2Code Oracle、URDFormer Oracle、Articulate-Anything），均基于相同数据划分。
  - 物理可执行性：在MuJoCo/Sapiens模拟器中测试。
  - 消融：系统验证了关键设计选择（3D输入必要性、联合预测互益），确保客观。
  - 局限性：未报告统计显著性检验（如误差条），但多次运行给出了方差，基本公平。

## 6. 主要结论与发现

- URDF-Anything在**几何分割**（mIoU 0.63 vs 最佳基线0.54，提升16.7%）、**运动学参数预测**（Type Error 0.008 vs 0.025，降低68%；Axis Error 0.132 vs 0.145，降低9%；Origin Error 0.164 vs 0.207，降低21%）、**物理可执行性**（78% vs 52%，提升50%）上均显著超越现有方法。
- 在**OOD类别**上表现尤为突出，展现强泛化能力。
- **消融证实**：点云+文本模态最佳；联合几何与运动学预测比独立预测效果更好（几何正则化互益）。
- 零样本仿真→真实测试（PARIS真实数据集）达到可接受的精度，证明其实际应用潜力。

## 7. 优点

- **端到端统一框架**：首次将3D MLLM用于铰接物体重建，避免多阶段流水线误差累积。
- **[SEG] token创新**：将语言生成与密集预测紧密耦合，实现几何-运动学一致性。
- **泛化性强**：在未见类别上仍保持高准确率。
- **计算高效**：单GPU 2.5小时完成训练，推理约13秒，适合实际部署。
- **输入灵活**：支持多视图和单视图输入，适配不同应用场景。

## 8. 不足与局限

- **无法生成惯性与质量属性**：受限于训练数据和基础模型，未输出质量、惯性张量等动力学参数。
- **非完全端到端**：依赖外部点云→网格转换模块（如Ball-Pivoting），可能引入误差。
- **数值精度受限**：基于token生成方式，输出为离散文本，导致连续参数精度有限（如原点、轴小数位）。
- **数据集偏小**：PartNet-Mobility中部分类别样本有限，可能影响极稀有类别的表现。
- **实验缺失**：未提供统计显著性检验（如置信区间），仅报告均值±标准差；消融实验数量较少（缺少对[SEG] token位置、不同点云密度等的全面探索）。

（完）
