---
title: "OpenHOI: Open-World Hand-Object Interaction Synthesis with Multimodal Large Language Model"
title_zh: OpenHOI：基于多模态大语言模型的开放世界手物交互合成
authors: "Zhenhao Zhang, Ye Shi, Lingxiao Yang, Suting Ni, Qi Ye, Jingya Wang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=0biUwyjKkm"
tags: ["query:vla"]
score: 7.0
evidence: OpenHOI利用MLLM进行开放世界手物交互合成，与机器人操作相关
tldr: 现有手物交互方法局限于封闭集物体和预定义任务。OpenHOI通过微调3D多模态大语言模型，实现对新物体的开放式操作序列生成。该方法能够理解自由形式语言指令，自动定位交互区域并分解任务。在多种物体上展示了零样本泛化能力，为机器人灵巧操作提供了新范式。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1421, \"height\": 711, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1415, \"height\": 815, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1435, \"height\": 200, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1428, \"height\": 250, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1368, \"height\": 704, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1421, \"height\": 785, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-0biuwyjkkm/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1369, \"height\": 692, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1439, \"height\": 214, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1432, \"height\": 576, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1433, \"height\": 574, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1474, \"height\": 576, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1473, \"height\": 578, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1453, \"height\": 575, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 696, \"height\": 360, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 910, \"height\": 361, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 681, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1409, \"height\": 573, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1413, \"height\": 574, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1317, \"height\": 359, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 767, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 770, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 896, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-0biuwyjkkm/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1250, \"height\": 518, \"label\": \"Table\"}]"
motivation: 现有方法无法泛化到未见物体和新指令，限制机器人操作应用。
method: 提出OpenHOI框架，微调3D MLLM实现抓取定位和语义任务分解。
result: 在零样本条件下成功生成多种未见物体的长程操作序列。
conclusion: MLLM驱动的开放世界交互合成可提升机器人操作泛化性。
---

## Abstract
Understanding and synthesizing realistic 3D hand-object interactions (HOI) is critical for applications ranging from immersive AR/VR to dexterous robotics. Existing methods struggle with generalization, performing well on closed-set objects and predefined tasks but failing to handle unseen objects or open-vocabulary instructions. We introduce OpenHOI, the first framework for open-world HOI synthesis, capable of generating long-horizon manipulation sequences for novel objects guided by free-form language commands. Our approach integrates a 3D Multimodal Large Language Model (MLLM) fine-tuned for joint affordance grounding and semantic task decomposition, enabling precise localization of interaction regions (e.g., handles, buttons) and breakdown of complex instructions (e.g., “Find a water bottle and take a sip”) into executable sub-tasks. To synthesize physically plausible interactions, we propose an affordance-driven diffusion model paired with a training-free physics refinement stage that minimizes penetration and optimizes affordance alignment.
Evaluations across diverse scenarios demonstrate OpenHOI’s superiority over state-of-the-art methods in generalizing to novel object categories, multi-stage tasks, and complex language instructions.

---

## 论文详细总结（自动生成）

# 中文总结：OpenHOI: 开放世界手物交互合成框架

## 1. 核心问题与整体含义

- **研究动机**：逼真的3D手物交互（HOI）合成对于AR/VR、灵巧机器人等应用至关重要。现有方法仅在封闭集物体和预定义任务上表现良好，无法泛化到未见物体或开放词汇指令。
- **整体贡献**：首次提出**开放世界HOI合成框架OpenHOI**，能够根据自由形式的自然语言指令，为**未见物体**生成长时序操作序列。通过整合3D多模态大语言模型（MLLM）与扩散模型，实现了对复杂指令的语义分解和对物体交互区域的细粒度定位，显著超越现有SOTA方法。

## 2. 方法论

### 核心思想
利用3D MLLM（基于ShapeLLM-7B）联合建模**几何抓取先验**与**语义任务分解**，再通过抓取驱动的扩散模型和**无需训练的物理精炼**生成物理合理、时序连贯的HOI序列。

### 关键技术细节
- **3D MLLM 的抓取推理与任务分解**：
  - 输入：物体点云 + 高层次指令文本。
  - 输出：空间抓取图（标识交互区域）+ 时序子任务序列（如“用双手打开瓶盖→用右手喝水”）。
  - 采用**<AFF> token**扩展MLLM词汇表，从最后一层隐藏状态解码出抓取区域；使用**粗到细的两阶段微调**：先在粗粒度静态抓取数据集上训练，再在细粒度动态HOI数据集上微调。
- **抓取驱动HOI扩散模型**：
  - 训练时，以抓取图、子任务嵌入、物体点云为条件，训练Transformer网络预测去噪后的HOI序列。
  - 采用**无分类器引导（CFG）**增强条件对齐（训练时随机屏蔽10%条件）。
  - 损失包含重建损失、距离图损失、相对方向损失。
- **训练后物理精炼（无需训练）**：
  - 在扩散采样过程中引入三个可微损失：**抓取对齐损失**（保证手部关节靠近抓取区域）、**穿透损失**（防止手穿透物体）、**运动插值损失**（平滑子任务间过渡）。
  - 使用**DSG（球形高斯约束）**方法在保持原始分布的同时进行梯度下降，避免分布偏移。

## 3. 实验设计

### 数据集与场景
- **GRAB**（51种物体，全身抓取）
- **ARCTIC**（双灵巧手操作可活动物体）
- **H2O**（仅用于极端泛化测试：训练于GRAB/ARCTIC，测试于H2O，完全未见物体）
- 所有数据集按80%/20%划分seen/unseen，并利用MLLM将低层描述转化为开放词汇意图指令。

### 对比方法
- MDM、TM2T、MotionGPT、Text2HOI（均为文本到运动生成方法）。

### 评估指标
- **运动准确性**：MPJPE（关节位置误差）、FOL（物体最终位置误差）
- **生成真实性**：FID（特征空间分布距离）
- **多样性与多模态性**：Diversity（跨提示方差）、MModality（同提示内方差）

### 主要结果
- 在主实验（GRAB & ARCTIC）的seen/unseen设置下，OpenHOI在所有指标上均**大幅超越**所有基线（例如GRAB unseen下MPJPE 51.34 vs Text2HOI 60.67, FID 28.29 vs 36.96）。
- 在极端测试H2O上同样保持领先（例如GRAB→H2O下MPJPE 75.78 vs Text2HOI 80.25）。
- 消融实验验证了affordance、CFG、penetration loss、affordance loss各组件的重要性。
- 敏感性分析显示guidance rate 2.5为最佳。
- 物理现实性评估（穿透率等）也优于Text2HOI。

## 4. 资源与算力

- 文中仅提到“Our experiments were conducted on NVIDIA A100 GPU”，未明确说明使用多少张GPU、训练时长、具体算力开销。
- 附录A提供实现细节：MLLM阶段使用AdamW优化器，学习率2e-4（第一阶段）和5e-4（第二阶段），训练7+3个epoch；扩散模型使用T=1000步余弦噪声调度。
- **总结**：算力描述不充分，缺少具体GPU数量和总训练时间。

## 5. 实验数量与充分性

- **实验组数丰富**：
  - 主实验：2个数据集 × 2种设置（seen/unseen） × 5种方法（含Ours） → 共20个条件。
  - 消融实验：2个数据集 × 2种设置 × 5种消融（w/o Affordance, w/o CFG, w/o l_penetration, w/o l_aff, Ours） → 20个条件。
  - 敏感性分析（guidance rate在0.5~5.0范围内测试）。
  - 极端测试（H2O：两个训练来源 × 5方法）。
  - 物理现实性对比、运动插值指标（SmoothRate）消融。
- **充分性判断**：实验设计全面，覆盖seen/unseen、组件消融、超参数敏感性、极端泛化，且报告了误差线（±标准差），统计显著性检验（t-test，附录C.9）支持结论。因此**实验充分、客观、公平**。

## 6. 主要结论与发现

1. OpenHOI首次实现了**开放世界HOI合成**，能从未见物体和开放指令生成长时间序列。
2. 3D MLLM的抓取推理与任务分解是泛化能力的核心，粗到细微调策略有效。
3. 基于抓取的扩散模型结合无需训练的物理精炼可生成高质量、物理合理的交互。
4. 通用化能力优于现有闭集方法（在GRAB/ARCTIC上MPJPE降低约10-20mm，FID降低约10-30%）。
5. 但面对**精确指代（如“第二个橱柜”）**和**超长序列（超过3个子任务）**时性能下降。

## 7. 优点

- **首创性**：首次提出开放世界HOI合成，突破闭集限制。
- **方法创新**：融合3D MLLM（抓取感知+语义分解）与扩散模型（抓取引导+物理精炼），形成完整流水线。
- **训练后精炼无需额外训练**：通过DSG实现在采样时直接优化物理约束，避免分布偏移。
- **实验充分**：多数据集、多基线、消融、敏感性、极端测试，结果稳健。
- **开源性承诺**：代码将公开（GitHub: OpenHOI），促进可复现性。

## 8. 不足与局限

- **算力信息缺失**：未明确GPU数量和训练耗时，影响可复现性评估。
- **场景覆盖有限**：仅在GRAB、ARCTIC、H2O上验证，缺少真实世界复杂场景（如杂乱环境、多物体交互）。
- **精细动力学处理不足**：对流体、可变形物体等精细物理模拟（如倒水）效果有限。
- **长序列和复杂指令限制**：超过3个子任务时误差累积，且无法精确区分同类物体（如“第二个橱柜”），依赖MLLM的逻辑推理能力提升。
- **应用限制**：当前方法为离线生成，实时性未考虑；机器人部署需额外逆运动学和重定向步骤。
- **潜在偏差**：训练数据来自实验室采集，可能不覆盖全部真实交互模式和物体类别。

（完）
