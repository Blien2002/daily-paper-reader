---
title: "WorldSimBench: Towards Video Generation Models as World Simulators"
title_zh: WorldSimBench：迈向将视频生成模型视为世界模拟器
authors: "Yiran Qin, Zhelun Shi, Jiwen Yu, Xijun Wang, Enshen Zhou, Lijun Li, Zhenfei Yin, Xihui Liu, Lu Sheng, Jing Shao, LEI BAI, Ruimao Zhang"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=j9pVnmulQm"
tags: ["query:vla"]
score: 5.0
evidence: 从具身视角评估世界模拟器的基准
tldr: 该论文针对现有预测模型缺乏层次分类且缺少从具身角度评估的问题，提出世界模拟器基准WorldSimBench，包含显式感知和隐式操纵双重评估。该框架通过人类偏好评估，为衡量高能力具身预测模型提供了新标准。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1757, \"height\": 584, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1770, \"height\": 826, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1738, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1585, \"height\": 509, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1576, \"height\": 777, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1773, \"height\": 902, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1766, \"height\": 869, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1766, \"height\": 1008, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-j9pvnmulqm/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1769, \"height\": 750, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1646, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1770, \"height\": 448, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1775, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1769, \"height\": 228, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1139, \"height\": 185, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1771, \"height\": 160, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1195, \"height\": 1015, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1076, \"height\": 401, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 996, \"height\": 402, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1139, \"height\": 401, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 502, \"height\": 480, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1777, \"height\": 474, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1333, \"height\": 232, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1057, \"height\": 252, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-j9pvnmulqm/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1056, \"height\": 339, \"label\": \"Table\"}]"
motivation: 当前缺乏从具身视角对预测模型（如世界模拟器）进行系统评估的标准。
method: 提出层次化功能分类，并设计双评估框架WorldSimBench，包括显式感知评估和隐式操纵评估。
result: WorldSimBench能够有效区分不同能力等级的世界模拟器。
conclusion: 该基准推动了世界模拟器在具身智能中的评估与发展。
---

## Abstract
Recent advancements in predictive models have demonstrated exceptional capabilities in predicting the future state of objects and scenes. However, the lack of categorization based on inherent characteristics continues to hinder the progress of predictive model development. Additionally, existing benchmarks are unable to effectively evaluate higher-capability, highly embodied predictive models from an embodied perspective. In this work, we classify the functionalities of predictive models into a hierarchy and take the first step in evaluating World Simulators by proposing a dual evaluation framework called WorldSimBench. WorldSimBench includes Explicit Perceptual Evaluation and Implicit Manipulative Evaluation, encompassing human preference assessments from the visual perspective and action-level evaluations in embodied tasks, covering three representative embodied scenarios: Open-Ended Embodied Environment, Autonomous, Driving, and Robot Manipulation. In the Explicit Perceptual Evaluation, we introduce the HF-Embodied Dataset, a video assessment dataset based on fine-grained human feedback, which we use to train a Human Preference Evaluator that aligns with human perception and explicitly assesses the visual fidelity of World Simulater. In the Implicit Manipulative Evaluation, we assess the video-action consistency of World Simulators by evaluating whether the generated situation-aware video can be accurately translated into the correct control signals in dynamic environments. Our comprehensive evaluation offers key insights that can drive further innovation in video generation models, positioning World Simulators as a pivotal advancement toward embodied artificial intelligence.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：现有预测模型（Predictive Models）种类繁多，但缺乏基于输出模态的层次化分类，且已有评估基准（如AgentBench、VBench等）仅关注文本任务规划或视觉美观性，无法从具身智能（embodied AI）的视角评估高能力模型（即“世界模拟器”World Simulators）的物理规则遵循、3D场景理解和动作可执行性。
- **整体含义**：为了推动世界模拟器的发展，需要建立一套能够同时评估视觉质量和动作控制能力的双维评估框架。论文提出WorldSimBench，旨在填补这一空白，为视频生成模型迈向世界模拟器提供系统化评测标准。

## 2. 方法论：核心思想与关键技术细节

### 2.1 核心思想
- 将预测模型按输出模态分为四个层次：
  - **S0**：文本预测（如LLM规划）
  - **S1**：图像预测（如Lego）
  - **S2**：视频预测（如VBench评估）
  - **S3**：可执行视频预测——**世界模拟器**，需兼顾物理规则与动作可译性。
- 针对S3模型，提出**双评估框架**：
  - **显式感知评估**：通过人类偏好评估视频的视觉质量、条件一致性和具身维度（如轨迹、交互、速度等）。
  - **隐式操纵评估**：将生成视频输入预训练的视频到动作模型，在闭环仿真环境中评估任务完成度。

### 2.2 关键技术细节
- **显式感知评估**：
  - 构建**HF-Embodied数据集**，包含35,701个（视频、指令、多维度评分、细粒度原因）元组，覆盖开放世界、自动驾驶、机器人操作三个场景。
  - 基于Flash-VStream（视频LLM）训练**Human Preference Evaluator**，输入视频和评估维度说明，输出1~5分（开放世界为1-2分）。仅训练LoRA参数。
  - 评估维度包括：视觉质量（美学、前景/背景一致性）、条件一致性（指令对齐、场景对齐）、具身属性（轨迹、交互、速度、视角、关键元素、安全性等）。
- **隐式操纵评估**：
  - 使用三个仿真平台：**MineRL**（开放世界）、**CARLA**（自动驾驶）、**CALVIN**（机器人操作）。
  - 预训练视频到动作模型：开放世界用Steve-1（目标基策略），自动驾驶用LMDrive，机器人操作用Susie。
  - 评估流程：当前观测+文本指令 → 世界模拟器生成未来视频 → 视频到动作模型输出控制信号 → 闭环执行固定步长后刷新预测，重复直至任务结束。指标包括任务成功率、路线完成率、违规次数等。

## 3. 实验设计

### 3.1 数据集与场景
- **开放世界**：利用VPT数据集（Minecraft人类玩家数据）扩展，并采集额外探索轨迹。评估任务：收集木头、泥土、种子，探索距离，垂直挖掘深度。
- **自动驾驶**：使用nuScenes训练集，参考Vista采样25帧。评估指标：路线完成率（RC）、违规得分（IS）、驾驶得分（DS）、各类碰撞和违章。
- **机器人操作**：使用RH20T-P（原始级机器人操作数据集）以及CALVIN数据集（ABC→D零样本评估）。评估指标：连续完成1-5个任务的成功率及平均长度。

### 3.2 对比方法
- 评估了8个主流视频生成模型：**Open-Sora-Plan (T2V/TI2V)、Lavie、ModelScope、OpenSora、AnimateDiff、DynamiCrafter、EasyAnimate**。所有模型在对应场景数据上进行了微调（fine-tune），以生成具身视频。

### 3.3 Benchmark
- 自身提出的WorldSimBench，包含显式感知（通过Human Preference Evaluator评分）和隐式操纵（闭环任务表现）两个维度。

## 4. 资源与算力
- **显式感知评估**中，Human Preference Evaluator基于Flash-VStream训练，使用**4张A100 80GB GPU**，训练4个epoch，学习率2e-5，warmup比例0.03，LoRA设置与Flash-VStream一致。
- **隐式操纵评估**中，视频生成模型的微调未明确给出具体GPU数量和时间，但提及遵循各模型官方实现，采用短视频（约20帧）和长视频（约60帧）两种设置（见表6）。视频到动作模型如Steve-1、LMDrive、Susie使用预训练权重，部分进行了额外微调（如LMDrive用任意指令重新训练）。
- **HF-Embodied数据集构建**：使用多种视频生成模型（如Open-Sora-Plan等）生成视频，然后进行人工标注，未提及具体算力消耗。

## 5. 实验数量与充分性
- **显式感知评估**：每个维度从指令池中选取5条指令，每条指令生成5个视频，由Human Preference Evaluator打分。共测试3个场景，每个场景包含6-7个维度。此外，与GPT-4o进行了对比（表3、表7），包含零样本（跨模型）泛化实验，证明HPE的优越性。
- **隐式操纵评估**：
  - 开放世界：5个任务，每个任务运行10个种子（trails），每轮3000帧（2.5分钟）。
  - 自动驾驶：LangAuto-Tiny基准（路线<150m），多环境组合（7种天气×3种日照），但未给出具体种子数。
  - 机器人操作：CALVIN协议（ABC训练→D测试），运行20条轨迹（main）和100条轨迹（附录表15），验证稳定性。
- **消融实验**：未专门设计消融实验，但通过DPO训练（附录表5）展示了HF-Embodied数据集可用于提升模型属性（如指令对齐提升0.6）。
- **充分性**：实验覆盖三个关键具身场景，对比了多个模型（包括condition类型差异），零样本泛化验证了评估器的鲁棒性。但隐式操纵评估中部分场景（如AD）的种子数未明确，可能影响统计显著性。

## 6. 主要结论与发现
- **显式感知评估**：
  - 开放世界：大多数模型在“具身交互”维度表现差（如物体变形不合理）；速度维度得分高是因为动态对象少。
  - 自动驾驶：模型间差异小，高表现模型在各维度均优；指令对齐得分高但3D深度（视角）和关键元素生成弱。
  - 机器人操作：静态场景（前景/背景一致性）表现好，但指令对齐差，常生成无目的动作；轨迹得分虚高（因无碰撞）。
- **隐式操纵评估**：
  - 开放世界：带图像条件的模型（TI2V）成功率显著低于纯文本条件模型，表明模型难以处理多条件输入且物理规律生成差。
  - 自动驾驶：Open-Sora-Plan在轨迹生成上表现最佳，DynamiCrafter和EasyAnimate在复杂动态场景下性能下降。
  - 机器人操作：DynamiCrafter在首任务上成功率高但长序列衰退快，Open-Sora-Plan平均任务长度最高（2.95/5）。
- **整体结论**：当前视频生成模型尚不能可靠地作为世界模拟器，尤其在物理规律一致性、指令对齐和长程任务执行上仍需重大改进。显式与隐式评估结果总体一致，但部分场景存在差异（如开放世界轨迹维度显式好但隐式差），说明双重评估的必要性。

## 7. 优点
- **层次化分类**：首次将预测模型按输出模态划分为S0-S3，明确世界模拟器的定位，为后续研究提供清晰框架。
- **双评估框架**：结合人类主观感知和闭环客观任务，全面评估视频质量与动作可执行性，弥补了现有基准的不足。
- **HF-Embodied数据集**：包含细粒度人类反馈（评分+原因），覆盖20个维度、3个场景，不仅可用于评估，还可用于偏好对齐训练（如DPO），具有扩展价值。
- **Human Preference Evaluator性能强**：基于Flash-VStream微调，在零样本泛化中显著优于GPT-4o（尤其在复杂维度如轨迹、交互），表明其可用作自动评估工具。
- **跨场景覆盖**：开放世界、自动驾驶、机器人操作三个代表性具身场景，增强了评估的普适性。

## 8. 不足与局限
- **实验覆盖有限**：仅评估了8个开源视频生成模型，未涉及商业模型（如Sora）或更先进的world model（如UniPi、Dreamer等），结论普遍性受限。
- **隐式操纵评估随机性**：部分场景（如AD）未报告多种子结果，未能展示统计误差；OE和RM的种子数相对较小（10/20），可能受环境随机性影响。
- **物理规则评估简化**：显式评估中“物理规则”通过人类评分间接反映，缺乏定量物理指标（如碰撞检测、动量守恒）。
- **视频到动作模型依赖**：隐式评估结果受限于视频到动作模型的质量，若该模型本身不准，可能低估世界模拟器的能力。
- **指令多样性不平衡**：AD场景仅5条指令（前进、后退、左转、右转、停止），过于简单；OE和RM指令虽有变化，但未评估语义复杂度对模型的影响。
- **计算资源未详尽说明**：大部分模型微调和推理的算力消耗未给出，影响复现性。
- **局限声明**：作者自己也指出，世界模拟器可应用于更多场景（如室内服务），当前框架未覆盖；其他物理表示（如流体、可变形物体）也未涉及。

（完）
