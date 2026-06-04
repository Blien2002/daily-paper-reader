---
title: "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation"
title_zh: ForceVLA：通过力感知混合专家增强VLA模型用于接触丰富操作
authors: "Jiawen Yu, Hairuo Liu, Qiaojun Yu, Jieji Ren, Ce Hao, Haitong Ding, Guangyu Huang, Guofan Huang, Yan Song, Panpan Cai, Wenqiang Zhang, Cewu Lu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=2845H8Ua5D"
tags: ["query:vla"]
score: 9.0
evidence: 提出ForceVLA，将力传感作为第一模态融入VLA框架，面向接触丰富操作
tldr: 现有VLA模型在接触丰富操作中因缺乏力反馈而表现不佳。ForceVLA将外部力传感作为第一模态，通过力感知混合专家模块动态融合视觉语言与力信息，在视觉遮挡和动态不确定条件下实现细粒度控制。实验表明该方法在多种接触操作任务上显著优于基线。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1290, \"height\": 822, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 704, \"height\": 704, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1379, \"height\": 622, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1376, \"height\": 448, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1299, \"height\": 431, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1306, \"height\": 634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1369, \"height\": 659, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1222, \"height\": 503, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1341, \"height\": 739, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1432, \"height\": 1059, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1431, \"height\": 921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1430, \"height\": 822, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1429, \"height\": 765, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1429, \"height\": 765, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1427, \"height\": 762, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1430, \"height\": 809, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1428, \"height\": 762, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1430, \"height\": 824, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-2845h8ua5d/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1430, \"height\": 763, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-2845h8ua5d/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 705, \"height\": 265, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2845h8ua5d/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1205, \"height\": 342, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2845h8ua5d/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 579, \"height\": 305, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2845h8ua5d/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1413, \"height\": 722, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2845h8ua5d/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 970, \"height\": 339, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-2845h8ua5d/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1134, \"height\": 263, \"label\": \"Table\"}]"
motivation: VLA模型在接触丰富任务中因缺乏力反馈而难以进行细粒度控制。
method: 提出FVLMoE模块，将6轴力反馈与预训练视觉语言嵌入动态融合。
result: 在接触操作任务上显著提升成功率，尤其在视觉遮挡场景下。
conclusion: 力传感作为第一模态能有效增强VLA模型在复杂操作中的表现。
---

## Abstract
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose \textbf{ForceVLA}, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces \textbf{FVLMoE}, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2\% over strong $\pi_0$-based baselines, achieving up to 80\% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025/.

---

## 论文详细总结（自动生成）

# 论文总结：ForceVLA：通过力感知混合专家增强VLA模型用于接触丰富操作

## 1. 核心问题与整体含义
- **研究动机**：现有的Vision-Language-Action (VLA) 模型（如OpenVLA、π0）通过预训练的视觉语言表示实现了通用机器人操控，但在接触丰富（contact-rich）任务（如插入、装配、剥皮）中表现脆弱。这些任务要求精细的力控制和实时物理交互，而VLA模型主要依赖视觉和语言线索，缺乏对力感知（force sensing）的显式整合，导致在视觉遮挡或动态不确定性下容易失败。
- **整体含义**：论文认为应将外部力传感（6轴力/力矩）作为第一类模态（first-class modality）融入VLA系统，通过合理的多模态融合机制提升机器人对细微接触动态的适应能力，从而实现更鲁棒、更智能的物理交互操控。

## 2. 方法论
- **核心思想**：在π0框架基础上，增加一个力感知混合专家（Mixture-of-Experts, MoE）模块——FVLMoE，将视觉语言特征与实时6维力反馈进行动态深度融合，以产生接触感知的动作序列。
- **关键技术细节**：
  - **输入**：时刻t的观测包括：基础相机图像、手腕相机图像、本体状态（TCP位姿+夹爪宽度）、6维外部力/力矩（估计值）。结合语言指令。
  - **特征提取**：视觉/语言输入经预训练的PaliGemma VLM（基于SigLIP）编码为视觉语言嵌入。
  - **力特征投影**：6维力向量通过线性投影层映射为力token（维度2048），与视觉语言嵌入拼接形成多模态序列。
  - **FVLMoE模块**：
    - 先经一个自注意力+FFN的编码层进行共享精炼。
    - 再送入稀疏MoE层：4个专家（每个为独立MLP），门控网络对每个token选择top-1专家，输出加权求和，并通过残差连接。
    - 最后线性投影到动作头的维度。
  - **动作生成**：采用条件流匹配模型（flow matching），以FVLMoE输出的融合特征作为引导信号，与当前状态和噪声动作轨迹相加，迭代去噪生成H步动作块。
  - **融合位置**：力信息在VLM视觉语言编码之后、动作解码之前注入，避免破坏预训练表示。

## 3. 实验设计
- **数据集**：自采数据集**ForceVLA-Data**，包含5个接触丰富任务：瓶泵、插头插入、USB插入、擦白板、剥黄瓜。共244条轨迹，约14万同步时间步，含视觉（两个RGB-D相机）、本体、6轴力/力矩。使用Flexiv Rizon 7-DOF机械臂、大寰自适应夹爪、Quest3 VR遥操作采集。
- **基准模型**：基于π0架构的四个变体：
  - π0-base w/o F：标准π0，无力输入
  - π0-base w/ F：π0将力直接拼接至状态输入
  - π0-fast w/o F：更快的π0变体，无力
  - π0-fast w/ F：π0-fast带直接力拼接
- **评估场景**：
  - 主实验：5个任务上分别评估成功率（各任务试次数不同：插入/泵20次，擦白板10次，剥黄瓜15次）。
  - 泛化实验：5个设置（不同物体几何、高度变化、视觉遮挡、不稳定插座）。
  - 消融实验：比较力的不同注入阶段（VLM前、后）以及不同融合方式（线性/ MoE /拼接）。
  - 多任务联合训练评估（4个任务）。
  - 力输入掩码（masking）实验：比较有/无力输入时的性能。
  - 专家路由负载分析（路由器激活模式）。

## 4. 资源与算力
- **训练硬件**：8× NVIDIA RTX 4090 GPU（每卡24 GB显存），64物理CPU核心，251 GB系统内存。
- **训练细节**：
  - 优化器：Adam（β1=0.9, β2=0.95），峰值学习率2.5e-5，衰减至2.5e-6。
  - 多任务训练：数据并行2 GPU，全局batch size 16，有效2048（梯度累积），30,000步约12小时。
  - 单任务训练：1 GPU，10,000步约9小时。
  - 精度：bfloat16，梯度裁剪1.0。
- **说明**：论文明确提供了算力和训练时长，便于复现。

## 5. 实验数量与充分性
- **实验数量丰富**：涵盖5个主任务成功率比较、5个泛化设置、5种消融变体（力的注入位置和融合方式）、多任务联合训练、力掩码消融、以及专家路由可视化。总计约20+组对比实验。
- **充分性**：
  - 对比了强基线（π0系列），包括有无力输入的多种变体，消融设计合理，揭示了力的注入阶段和融合方式的关键性。
  - 泛化实验覆盖物体/高度/遮挡/动态扰动等，验证了鲁棒性。
  - 失败模式分析详细（附录E、F），补充了定性说明。
  - 多任务实验显示ForceVLA能同时学习多个技能。
- **公平性**：基线均基于同一代码框架（π0），力输入方式公平对比；评价指标统一为任务成功率，部分任务辅以剥皮长度/次数。客观性较好。

## 6. 主要结论与发现
- ForceVLA在所有5个接触丰富任务上平均成功率60.5%，比最强π0-base基线（37.3%）提升23.2%，个别任务达80%。
- 直接拼接力信号虽能小幅提升π0-base（+2.9%），但FVLMoE的深度融合带来更大增益（+23.2%），表明融合方式比单纯增加模态更重要。
- 力应于VLM编码之后注入，避免破坏预训练特征；MoE动态路由能实现任务阶段感知的专家选择。
- 泛化实验显示ForceVLA在视觉遮挡、物体变形、高度变化下保持高性能，而基线严重退化。
- 力掩码消融证实移除力输入后性能大幅下降，验证了力模态的不可或缺性。

## 7. 优点
- **创新性**：首次将6轴力作为第一类模态并采用MoE动态融合引入VLA框架，设计精巧（后编码融合+MoE路由）。
- **系统性**：提供了完整的端到端框架、自标注数据集、数据采集工具和消融分析，代码和数据承诺开源。
- **实验严谨**：涵盖多任务、多泛化场景、多消融、失败模式分析，结果充分支持结论。
- **实用性**：真实世界数据集（无仿真缝隙），直接面向物理部署；任务的选取覆盖典型接触类操作，具有代表性。
- **性能突出**：在多个任务上显著超越强基线，尤其对视觉遮挡和物理扰动鲁棒。

## 8. 不足与局限
- **力传感精度**：当前使用估计的外部力矩（estimated external wrench），并非直接高保真力传感器，可能限制极端精细场景的表现。
- **硬件成本**：依赖高成本力/力矩传感器和工业级机械臂，普及性受限。
- **无仿真数据**：仅真实世界数据采集和评估，未利用仿真大规模训练（作者承认是未来方向）。
- **任务多样性有限**：仅5个任务（插入、按压、擦拭、切削），未涵盖更复杂的装配或交互任务；物体种类和场景变化较少。
- **多任务联合训练**：联合训练时某些任务（如USB插入）仍低于20%，说明知识迁移仍有挑战。
- **专家路由分析**：虽然给出了路由器激活模式，但缺乏对专家功能可解释性的深入分析。
- **潜在偏差**：数据集仅由5位操作员遥操作采集，操作风格和多样性可能受限，存在数据偏差风险。
- **评估统计**：部分任务仅10-20次试验，未报告置信区间或标准差，虽进行了枚举但统计显著性未显式检验。

（完）
