---
title: "AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning"
title_zh: AutoVLA：一种用于端到端自动驾驶的具有自适应推理和强化微调的视觉-语言-动作模型
authors: "Zewei Zhou, Tianhui Cai, Seth Z. Zhao, Yun Zhang, Zhiyu Huang, Bolei Zhou, Jiaqi Ma"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=28qUA2bSe5"
tags: ["query:vla"]
score: 8.0
evidence: 用于端到端自动驾驶的视觉-语言-动作模型
tldr: 现有VLA模型在自动驾驶中存在动作不可行、结构复杂等问题。本文提出AutoVLA，将推理与动作生成统一在单个自回归模型中，直接从视觉和语言指令进行语义推理和轨迹规划，通过将连续轨迹离散化为可行动作实现端到端驾驶。实验表明该方法能有效提升动作合理性并简化模型结构。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1421, \"height\": 756, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1424, \"height\": 491, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 841, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1434, \"height\": 676, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 714, \"height\": 709, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1450, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1437, \"height\": 439, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1439, \"height\": 777, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1432, \"height\": 1577, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1402, \"height\": 997, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1423, \"height\": 683, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1444, \"height\": 1039, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1427, \"height\": 1445, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1429, \"height\": 688, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1429, \"height\": 1926, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-28qua2bse5/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1447, \"height\": 423, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1397, \"height\": 444, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 731, \"height\": 184, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1307, \"height\": 373, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1456, \"height\": 315, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 723, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 734, \"height\": 183, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1114, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1429, \"height\": 453, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1441, \"height\": 757, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-28qua2bse5/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1087, \"height\": 370, \"label\": \"Table\"}]"
motivation: 现有VLA模型在自动驾驶中输出不可行动作、结构复杂或推理冗长，需要更统一的解决方案。
method: 提出单一自回归模型统一推理和动作生成，将连续轨迹离散化为可行动作。
result: 通过离散化动作和强化微调，提升了动作可行性和效率。
conclusion: AutoVLA为自动驾驶提供了一种简化的端到端VLA方案。
---

## Abstract
Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有用于自动驾驶的视觉-语言-动作（VLA）模型常存在**物理不可行的动作输出**、**复杂的模型结构**或**不必要的冗长推理**，限制了端到端驾驶的实用性和效率。
- **研究动机**：传统模块化架构存在误差累积和缺乏联合优化；纯模仿学习的端到端方法缺乏世界知识和推理能力。VLM/VLA 虽有潜力，但直接输出文本式动作不保证物理可行性，引入中间表示又破坏端到端优化或增加复杂度。此外，现有方法采用固定推理策略，无法适应场景复杂度。
- **整体含义**：论文旨在提出一种**统一的自回归 VLA 模型**，将语义推理与物理轨迹生成无缝集成，并实现根据场景自适应切换快/慢思考，从而提高规划性能与运行效率。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将连续轨迹离散化为有限个物理可行动作 token，整合到预训练的 VLM（Qwen2.5-VL-3B）中，实现单一自回归模型直接输出推理和动作序列。
- **关键技术细节**：
  - **动作 Token 化**：使用 K-disk 聚类从真实轨迹（WOMD）中构建包含 2048 个 token 的动作码本，每个 token 表示 0.5 秒的短时运动（Δx, Δy, Δθ）。模型输出 10 个动作 token，解码后形成 5 秒轨迹。
  - **模型输入**：多视角（前、前左、前右）连续 4 帧摄像头图像、导航指令（如“直行”）、当前车辆速度、加速度和历史动作。
  - **双思维模式**：通过 SFT 同时学习“快思考”（仅输出轨迹）和“慢思考”（链式推理 + 轨迹），由系统提示控制模式。
  - **训练阶段**：
    - **SFT**：使用真实轨迹和大 VLM（Qwen2.5-VL-72B）蒸馏的 CoT 推理数据。损失函数结合语言建模损失和额外的动作损失，并对含有 CoT 的样本加权（λ_cot=40）。
    - **RFT**：基于 GRPO 算法，以驾驶奖励（如 PDMS、ADE）为主，加入 CoT 长度惩罚，鼓励模型在简单场景减少推理，提升效率。
  - **公式**：LLM = −(1/N) Σ log pθ(xi | x<i, C, I, S)；Laction = −(1/T) Σ log pθ(xi | x<i, C, I, S)（仅对动作位置）；LSFT = w_i · (LLM + λ_a Laction)；GRPO 目标函数涉及组相对优势 A_i 和 KL 散度约束。

### 3. 实验设计：数据集、Benchmark、对比方法

| 项目              | 说明                                                                                                                                 |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **数据集**        | nuPlan（166k 训练，45.6k 推理标注），nuScenes（19k 训练，2.9k 推理标注），Waymo E2E（23.8k 训练，7.2k 推理标注），CARLA Garage（274.5k 训练，53.2k 推理标注），DriveLM 数据被重新格式化为 CoT 格式。 |
| **Benchmark**     | 开环：NAVSIM（nuPlan）、nuScenes 规划基准、Waymo E2E（RFS 评分）。闭环：CARLA Bench2Drive（驾驶分数、成功率等）。                             |
| **对比方法**      | 包括 TransFuser、Hydra-MDP、Centaur、TrajHF、UniAD、VAD、TCP-traj、DriveAdapter、Orion、EMMA、OpenEMMA、OpenDriveVLA-3B 等。       |
| **评估指标**      | nuPlan: PDMS（含碰撞、舒适、进度等）；nuScenes: L2 距离与碰撞率；Waymo: RFS 与 ADE；CARLA: 驾驶分数、成功率、效率、舒适度。                      |

### 4. 资源与算力

- **SFT**：使用 8 块 NVIDIA L40S GPU，每 GPU batch size=1，梯度累积 4 步，有效 batch size=32，训练 5 个 epoch。学习率 1e-5，FSDP 策略，BF16 混合精度。
- **RFT**：使用 LoRA 适配器（rank=8），学习率 3e-5，KL 权重 β=0.04，训练 6000 步。未明确给出总训练时长，但基于常用经验，训练成本适中。
- **推理**：快思考平均 1.072 秒/样本，慢思考平均 10.518 秒/样本，表明慢推理性价比较高，RFT 可减少慢思考次数。

### 5. 实验数量与充分性

- **实验数量**：涉及四大数据集/场景，至少包含：主表（Table 1, 3, S2, S3 等）、数据缩放实验（Fig.4）、RFT 性能与消融（Fig.5, Table 2, 5, 6）、动作分词方式对比（Table 4, 6）、Waymo 消融（Table S4）、以及多个定性示例。
- **充分性与公平性**：
  - 对比了多个 SOTA 方法，且结果表格与官方排行榜（Waymo 挑战赛）吻合。
  - 消融实验覆盖了文本输出 vs 动作 token、不同码本大小（256~4096）、不同分词方法（RT-1、FAST、K-disk）、RFT 前后对比、有无 CoT 训练、多摄像头 vs 单摄像头等。
  - 缺失误差条统计（仅单次运行），但符合该领域惯例。数据来源多样，避免单一偏差。

### 6. 论文的主要结论与发现

- **统一框架有效**：AutoVLA 在开环和闭环测试中均达到或超越现有 SOTA，证明了将推理与动作生成统一在一个自回归模型中的可行性。
- **RFT 提升性能与效率**：RFT 使 PDMS 提升 10.6%，推理运行时间减少 66.8%，且自适应减少了简单场景中不必要的推理。
- **动作 token 化优于文本输出**：物理尺度的离散动作 token 明显优于直接输出文本轨迹（PDMS 高 9 分、L2 低 0.19m、运行时间减半）。
- **数据缩放具有正收益**：增加训练数据量（10k→185k）持续改善规划指标，且 CoT 推理数据在数据量足够时（>50k）优势更明显。
- **模型具有强推理能力**：能在复杂场景（施工区、行人、遮挡等）提供合理的 CoT 推理并生成安全轨迹。

### 7. 优点（方法或实验设计亮点）

- **方法创新**：纯自回归统一框架简化了系统结构；动作 token 保证物理可行性；GRPO 驱动自适应推理，避免冗余计算。
- **实验设计**：覆盖多种真实世界与仿真数据集、开环与闭环评估，消融实验系统全面。特别在 Waymo 挑战赛取得 RFS Spotlight 最高分。
- **实用性**：快慢思考两种模式可部署时按需切换；RFT 可使用常规指标（如 ADE、PDMS）而无需人工标注偏好，更易扩展。
- **可复现性**：论文提供详细超参数、代码和数据集计划开源，附录包含完整算法流程和提示示例。

### 8. 不足与局限

- **实时性瓶颈**：当前推理频率约 1 Hz（慢思考更高），未达到实际系统要求的 10 Hz 以上，依赖 GPU 大显存，尚需模型量化或蒸馏优化。
- **实验偏差风险**：CoT 推理数据来自单一模型（Qwen2.5-VL-72B）蒸馏，可能继承了其错误或偏差；仅采用单次运行结果，缺乏统计误差；部分数据集（如 Waymo E2E）规模较小，可能限制泛化能力。
- **场景覆盖有限**：主要聚焦驾驶轨迹预测，缺乏对罕见事件（如事故、失控）的专门评估；闭环实验仅在 CARLA 仿真，与真实世界差距未知。
- **对比公平性**：部分基线（如 Orion）使用了更多传感器或计算资源，AutoVLA 使用的输入相对简化（三视角），但未详细讨论控制变量。
- **安全性与可解释性**：虽提供 CoT，但推理可能出错或过度自信，缺少对不安全案例的深入分析。

（完）
