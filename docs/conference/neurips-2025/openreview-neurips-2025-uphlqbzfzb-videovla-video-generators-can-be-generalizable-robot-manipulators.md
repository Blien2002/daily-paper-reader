---
title: "VideoVLA: Video Generators Can Be Generalizable Robot Manipulators"
title_zh: VideoVLA：视频生成器可成为通用机器人操纵器
authors: "Yichao Shen, Fangyun Wei, Zhiying Du, Yaobo Liang, Yan Lu, Jiaolong Yang, Nanning Zheng, Baining Guo"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=UPHlqbZFZB"
tags: ["query:vla"]
score: 10.0
evidence: 将视频生成模型转化为机器人视觉-语言-动作操纵器
tldr: 现有视觉-语言-动作（VLA）模型泛化能力有限。本文提出VideoVLA，利用多模态扩散变压器将视频生成模型改造为VLA操纵器，输入语言指令和图像即可预测动作序列及未来视觉结果。实验显示其在多种新任务、新物体上显著提升泛化性，为通用机器人操纵提供了新范式。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-uphlqbzfzb/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1419, \"height\": 452, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-uphlqbzfzb/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1430, \"height\": 565, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-uphlqbzfzb/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1315, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-uphlqbzfzb/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1447, \"height\": 564, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-uphlqbzfzb/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1419, \"height\": 921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-uphlqbzfzb/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1420, \"height\": 1851, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1438, \"height\": 483, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1430, \"height\": 331, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1428, \"height\": 349, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1454, \"height\": 336, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1443, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 789, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1460, \"height\": 331, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 625, \"height\": 240, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 921, \"height\": 169, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1454, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1157, \"height\": 675, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 457, \"height\": 311, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1253, \"height\": 180, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-uphlqbzfzb/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1282, \"height\": 257, \"label\": \"Table\"}]"
motivation: 现有VLA模型泛化能力有限，视频生成模型蕴含丰富的动态先验。
method: 基于多模态扩散变压器，联合建模视频、语言和动作模态，实现动作与未来视觉的联合预测。
result: 在多个机器人操纵基准上，对新任务、新物体的泛化性大幅超越此前VLA方法。
conclusion: 视频生成模型可作为VLA模型 backbone，提升机器人操纵的通用性。
---

## Abstract
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes.  Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy—forecasting both actions and their visual consequences—explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：机器人操纵的泛化能力是实现开放世界部署和通用人工智能的关键。现有的视觉-语言-动作（VLA）模型虽然利用大规模预训练的视觉-语言理解模型进行感知和指令理解，但在面对新任务、新物体和新环境时泛化能力仍然有限。
- **背景**：最近大型视频生成模型（如CogVideoX、OpenSora）在文本或图像条件上表现出惊人的泛化能力，生成的视频具有物理合理性，并隐含着对动态世界的理解。论文指出，视频生成器处理新颖文本/图像条件的能力与机器人操纵器处理未见指令/观测的能力自然对齐，因此提出一个问题：“能否将大型视频生成模型无缝改造为具有泛化能力的机器人操纵器？”
- **整体含义**：论文探索了一种新范式——利用预训练的视频生成模型（而非传统的理解型模型）作为VLA模型的主干，通过联合预测未来动作及其视觉结果来实现操纵任务，并展示出优异的域内性能和强大的泛化能力（跨本体技能迁移、操作未见物体）。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：**VideoVLA** 将视频生成模型（CogVideoX-5B）转化为一个端到端的视觉-语言-动作（VLA）操纵器，输入语言指令和当前观测图像，同时输出动作序列和对应的未来视频帧（视觉想象）。该方法采用**双预测策略**：同时预测动作和动作产生的视觉后果，利用视频生成模型预训练中获得的世界知识和物理先验来增强操纵的泛化性。
- **关键技术细节**：
  - **模型架构**：基于多模态扩散变压器（Diffusion Transformer, DiT）。将所有模态（语言、视频潜在表示、动作）拼接成一个统一序列，使用DDPM扩散损失进行去噪训练。
  - **数据预处理**：
    - 文本编码器：T5，将指令编码为固定长度（226个token）序列。
    - 视频编码器：使用CogVideoX的3D因果VAE编码器。将输入视频帧转换为潜在表示，其中第一个潜在表示对应于当前观测帧；训练时输入完整视频得到当前观测和未来帧的潜在表示。
  - **统一未来建模**：在DiT中，将语言token、当前观测潜在、未来帧潜在和动作向量（7维：三轴旋转+三轴平移+夹爪状态）拼接，对动作和未来帧潜在添加高斯噪声，模型学习去噪。动作和视频使用相同的扩散时间步（同步调度）。训练时DDPM损失监督。推理时使用DDIM采样（50步）。
  - **流程**：预测一个动作块（含K个动作）和N帧未来视频。执行前三个动作后获取新观测，重复直至任务完成。
- **初始化**：主干预训练权重来自CogVideoX-5B，并在OXE数据集上预训练，然后在下游真实数据集上微调。

## 3. 实验设计：数据集/场景、基准、对比方法

- **数据集**：
  - **预训练**：Open X-Embodiment (OXE) 数据集，包含超过100万条真实机器人轨迹，来自60个数据集、22种机器人形态。采用与Octo、OpenVLA、CogACT一致的子集（2250万帧）。
  - **真实世界微调**：使用Realman机器人（7自由度臂+夹爪）通过遥操作收集5824个样本，包含“捡拾”、“堆叠”、“放置”三类任务。
- **评估场景**：
  - **仿真环境**：SIMPLER模拟环境，用于Google Robot和WidowX Robot，包含Visual Matching (VM)和Variant Aggregation (VA)两种评估协议。
  - **真实世界**：使用Realman机器人在实验室环境下进行评估。
- **基准与对比方法**：总共对比了**8种**VLA模型：RT-1-X、RT-2-X、Octo-Base、Octo-Small、OpenVLA、SpatialVLA、π0、CogACT。所有基线模型均使用公开预训练权重并在相同条件下微调。

## 4. 资源与算力

- 论文明确说明：预训练使用 **32块 AMD MI300X GPU**，批大小256，训练 **100K 次迭代**；下游微调使用相同硬件，训练 **15K 次迭代**。
- 优化器：AdamW，学习率1e-5，权重衰减1e-4。
- 推理速度：在单块H100 GPU上，使用10步DDIM去噪，预测4个未来潜在（13帧视频）和6个动作（前3个执行）约需1.1秒，有效控制频率约3 Hz。

## 5. 实验数量与充分性

- **实验数量**：论文进行了大量实验，包括：
  - 仿真环境下的**域内评估**（4个WidowX任务 + 4个Google任务 × 两种协议 = 12个实验），每个任务多次试验（表11列出：Google VM任务300、240、216、108次；VA任务825、600、378、189次；WidowX任务各24次）。
  - **泛化到新物体**（Google机器人，10种未见物体，每种25次试验）。
  - **泛化到新技能**（Google机器人执行WidowX专有技能，8种技能，每种20次试验）。
  - **真实世界域内评估**（3种任务，共24+48+24=96次试验）。
  - **真实世界泛化-新物体**（12种未见物体，每种12次试验）。
  - **真实世界泛化-跨本体技能迁移**（6种新技能，每种16次试验）。
  - **消融实验**：共10组以上（backbone选择、预测帧数、双预测策略、因果掩码、扩散同步调度等）。
- **充分性与公平性**：
  - 实验覆盖仿真和真实两种场景，涵盖多种机器人形态（Google、WidowX、Realman）。
  - 所有基线模型在相同训练/微调/评估条件下进行，代码和开源计划确保可复现。
  - 每个任务均报告多次试验的平均成功率，并提供了试验次数细节。
  - 总体实验设计充分，对比公平，结论可靠。

## 6. 论文的主要结论与发现

- **主要发现**：高质量的未来视觉想象（生成视频）与可靠的动作预测及任务成功之间存在**强相关**；双预测策略显著提升泛化性能。
- **性能提升**：
  - 仿真域内：VideoVLA在Google机器人VM和VA平均上达到63.0%（所有12个任务平均），超过CogACT（62.6%）。
  - 新物体泛化：平均成功率65.2%，远超CogACT（42.4%）和SpatialVLA（50.8%）。
  - 新技能泛化：平均48.6%，超过CogACT（20.4%）两倍以上。
  - 真实世界：真实世界域内平均64.6%，新物体50.6%，新技能58.0%，均为最优。
- **消融结论**：
  - 视频生成模型预训练至关重要（从零训练成功率仅12.6%，使用预训练达80.4%）。
  - 更长的预测时间窗口（49帧优于25帧优于13帧）带来更好表现。
  - 移除视频损失或完全不预测视频会导致性能断崖式下降（如新物体泛化从65.2%跌至12.7%）。
  - 因果掩码不如双向注意力；同步扩散调度优于异步调度。
- **视觉想象与执行一致性**：通过SIFT关键点匹配和SAM-PT跟踪计算运动相似度，发现相似度越高任务成功率越高（图3），验证了双预测策略的有效性。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：
  - 首次系统性地探索将大规模视频生成模型（而非理解模型）直接改造为VLA操纵器，开辟新范式。
  - 双预测策略（动作+视觉想象）使模型隐式利用生成模型的世界知识和物理先验，增强泛化。
  - 统一的多模态DiT架构，视频、语言、动作端到端联合建模。
- **实验设计亮点**：
  - 仿真+真实双环境验证，涵盖多种机器人本体（Google、WidowX、Realman）。
  - 泛化评估设计全面：新物体、新技能（跨本体迁移）、真实场景干扰物等。
  - 消融实验系统（骨干网络、帧数、预测策略、注意力掩码、扩散调度），深入分析各组件贡献。
  - 提供“想象-执行一致性”量化分析（运动相似度与成功率关系），具有方法论价值。
  - 所有基线模型均在相同条件下复现或微调，确保公平对比。

## 8. 不足与局限

- **推理速度**：当前仅约3Hz，对于需要高频控制的动态任务可能不足。主要受限于大视频生成模型（5B参数）和多步DDIM采样。论文已提出未来方向（模型蒸馏、一步去噪、专用小模型）。
- **计算资源需求大**：预训练需要32块AMD MI300X，对一般研究团队门槛较高。
- **视频解码开销**：虽然推理时视频解码可选，但若需要显式可视化想象，额外解码会增加延迟。
- **动作空间局限性**：仅支持7自由度操作（6D姿态+夹爪），未包含更复杂灵巧操作或多指手。
- **数据集偏差**：预训练使用OXE数据集，其本身可能包含特定场景和物体分布，泛化到极端新颖场景（如完全没见过的物体类型或复杂环境）可能仍受限制。
- **未涉及长期规划**：论文采用短动作块（6步），未测试长周期任务（如多步组装、导航结合操作）。
- **伦理与安全**：论文在附录简要提到但未深入讨论失败案例的潜在风险（如错误想象导致碰撞或损坏物体）。

（完）
