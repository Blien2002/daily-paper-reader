---
title: "NavBench: Probing Multimodal Large Language Models for Embodied Navigation"
title_zh: NavBench：探测多模态大语言模型的具身导航能力
authors: "Yanyuan Qiao, Haodong Hong, Wenqi Lyu, Dong An, Siqi Zhang, Yutong Xie, Xinyu Wang, Qi Wu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=nf8PKQKtl2"
tags: ["query:vla"]
score: 6.0
evidence: 多模态大语言模型具身导航能力基准
tldr: 现有工作缺乏对多模态大语言模型在具身环境中导航能力的系统评估。本文提出NavBench基准，包含导航理解（全局指令对齐、时间进度估计、局部观察-动作推理）和逐步执行两大组件，覆盖3200个问答对和432个室内场景。实验揭示了MLLMs在空间推理和动作执行方面的局限性，为未来具身导航研究提供评测标准。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1387, \"height\": 575, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1425, \"height\": 530, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1450, \"height\": 493, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1453, \"height\": 273, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 462, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 699, \"height\": 403, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 691, \"height\": 401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nf8pkqktl2/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 473, \"height\": 224, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-nf8pkqktl2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1450, \"height\": 743, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nf8pkqktl2/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 710, \"height\": 316, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nf8pkqktl2/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1445, \"height\": 284, \"label\": \"Table\"}]"
motivation: 多模态大语言模型在视觉-语言任务中表现优异，但其在具身环境中的导航能力尚未被充分探索。
method: 构建一个包含导航理解和逐步执行两部分的基准测试，涵盖多种认知任务和室内场景。
result: 实验发现MLLMs在全局指令对齐和局部观察-动作推理上存在不足，提出零样本设置下的导航能力评估结果。
conclusion: NavBench为多模态大语言模型的具身导航能力提供了系统评估框架，有助于推动相关研究。
---

## Abstract
Multimodal Large Language Models (MLLMs) have demonstrated strong generalization in vision-language tasks, yet their ability to understand and act within embodied environments remains underexplored. We present NavBench, a benchmark to evaluate the embodied navigation capabilities of MLLMs under zero-shot settings. NavBench consists of two components: (1) navigation comprehension, assessed through three cognitively grounded tasks including global instruction alignment, temporal progress estimation, and local observation-action reasoning, covering 3,200 question-answer pairs; and (2) step-by-step execution in 432 episodes across 72 indoor scenes, stratified by spatial, cognitive, and execution complexity. To support real-world deployment, we introduce a pipeline that converts MLLMs' outputs into robotic actions. We evaluate both proprietary and open-source models, finding that GPT-4o performs well across tasks, while lighter open-source models succeed in simpler cases. Results also show that models with higher comprehension scores tend to achieve better execution performance. Providing map-based context improves decision accuracy, especially in medium-difficulty scenarios. However, most models struggle with temporal understanding, particularly in estimating progress during navigation, which may pose a key challenge.

---

## 论文详细总结（自动生成）

# NavBench：探测多模态大语言模型的具身导航能力 —— 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：多模态大语言模型（MLLMs）在静态视觉-语言任务（如 VQA、视频理解）上表现优异，但其在**具身环境**中理解并执行物理动作的能力尚未被系统评估。现有具身导航基准（如 R2R、ObjectNav）多为任务特定监督，且仅通过最终成功率评估，无法揭示模型是否真正理解导航行为（如指令与轨迹的对齐、进度跟踪、动作推理），也无法区分不同难度层级。
- **核心问题**：MLLMs 是否能在零样本设置下具备**导航理解**（全局对齐、时间进度估计、局部观察-动作推理）和**逐步执行**（做出正确的下一步动作）的能力？不同模型在不同难度任务上的表现差异如何？
- **整体含义**：填补 MLLMs 在具身导航领域系统评估的空白，提供一个包含理解与执行、多难度分层的基准，并实现真实世界部署验证。

## 2. 论文提出的方法论

### 核心思想
将导航能力分解为**导航理解**（Comprehension）和**导航执行**（Execution）两个正交组件，分别用多项选择任务和逐步决策任务评估。同时引入**空间、认知、执行**三维难度分类，以分析不同复杂度下的表现。

### 关键技术细节
- **导航理解任务**（3,200 QA 对）：
  - **全局指令对齐**（1,200 例）：给定全景轨迹和 5 个候选指令（1 个正确 + 4 个干扰），选择正确指令。干扰项通过四种策略生成：基础随机、方向替换、物体替换、子指令打乱。
  - **时间进度估计**（1,000 例）：给定部分轨迹和子指令列表，预测最后完成的子指令索引。
  - **局部观察-动作推理**（1,000 例）：分为未来观察预测（当前视图 + 动作 → 选择正确结果视图）和未来动作预测（两个连续视图 → 选择导致转换的动作）。

- **导航执行任务**（432 个 episode，跨 72 个场景）：
  - 在 Matterport3D 模拟器中进行零样本逐步决策：模型接收当前全景图、指令和可选视点列表，选择下一个移动方向（视点选择，而非低层控制）。
  - 难度分类基于三个维度：
    - **空间复杂度**：路径长度 d、转角标准差 θ、垂直范围 z、2D 面积 A，公式：Φ_spatial = α1·log(1+d) + α2·log(1+θ) + α3·I(z>1.5) + α4·log(1+A)
    - **认知复杂度**：指令长度、动词数、空间词汇数、地标提及数、从句数，公式类似。
    - **执行复杂度**：步数、转弯数、楼层变化、决策点数量。
    - 各维度得分归一化到 1-9，划分为易(1-3)、中(4-6)、难(7-9)三级。人类标注验证分类。

- **真实世界部署管道**（图 5）：
  - 路点预测器（Waypoint Predictor）：从 RGB-D 输入生成候选路点热图。
  - MLLM 决策模块：选择最符合指令的路点（角度 + 距离）。
  - 低层控制器：将选定路点转换为机器人运动指令（API 控制）。

## 3. 实验设计

- **数据来源**：从 R2R、RxR、GEL-R2R、FGR2R 等已有导航基准中提取指令-轨迹对，并用 Matterport3D 模拟器渲染全景图和单视点 RGB 图像。
- **基准统计**：
  - 理解任务：3,200 QA（全局 1,200 + 进度 1,000 + 局部 1,000）
  - 执行任务：432 个 episode，来自 72 个场景（每个场景 6 个案例，平均分配难度）
- **对比模型**：
  - **闭源模型**：GPT-4o、GPT-4o-mini、Gemini-2.0-flash、o4-mini
  - **开源模型**：InternVL2.5-2B/8B、Qwen2.5-VL-3B/7B、LLaVA-OneVision-7B、LLaVA-Next-7B、Llama3.2-Vision-11B
- **度量指标**：
  - 理解任务：多项选择准确率
  - 执行任务：成功率（SR，目标在 3 米内可见）和 SPL（考虑路径效率）
- **基线**：随机猜测和人类表现（在 VLN-Bench tiny 子集上标注）
- **附加实验**：
  - 干扰类型分析（四种策略）
  - 局部观察-动作推理分项分析
  - 地图信息影响（MapGPT 方法，给 GPT-4o 添加拓扑地图文本）
  - 思维链（CoT）提示（“Let's think step by step”）
  - 错误类型手动分析（100 个失败案例）
  - 轨迹长度对时间推理的影响
  - 真实世界验证（各 10 个案例，GPT-4o 和 Qwen2.5-VL-7B）

## 4. 资源与算力

- **计算资源**：开源模型使用 **vLLM** 和 **lmdeploy** 部署在 **单个 NVIDIA A6000 GPU（48GB）** 上进行推理。闭源模型通过 API 调用。
- **训练成本**：论文采用零样本评估（zero-shot），**未进行模型训练**，因此没有训练时长和算力消耗。真实世界机器人实验使用双轮式移动底盘的室内机器人平台。
- 文中未详细报告每个实验的具体推理时间，但提到了使用的硬件型号。

## 5. 实验数量与充分性

- **实验数量**：
  - 理解任务：3,200 个多项选择样本，覆盖三个子任务。
  - 执行任务：432 个 episode，每个难度约 144 个（易/中/难各约 144）。
  - 额外分析：干扰类型对比（4 种）、局部推理分项、地图影响（2 条件）、CoT 对比（2 模型 × 2 条件）、错误分析（100 个案例）、轨迹长度分组（3 组）、真实世界验证（2 模型 × 10 案例）。
- **充分性与公平性**：
  - 覆盖了多个主流闭源和开源模型，包括不同参数量级（2B~11B）。
  - 零样本设置避免了任务特化训练带来的偏差。
  - 人类表现作为上限参考，随机基线作为下限。
  - 难度分类经自动评分+人工验证，具有合理性。
  - 但执行任务 432 个 episode 相对较少（但仍跨 72 场景），可能限制统计稳定性；真实世界验证仅有 20 个案例，属于小规模试点。
  - 消融实验（地图、CoT）设计合理，能揭示特定因素的影响。

## 6. 论文的主要结论与发现

1. **理解与执行能力高度相关**：在多数模型上，理解平均得分高的模型执行表现也更好（如 GPT-4o 均为最优之一）。
2. **时间推理是共同瓶颈**：进度估计任务得分普遍很低（除 GPT-4o 外均低于 40%），且全局对齐中“打乱子指令”干扰项导致性能急剧下降，表明模型缺乏对时间顺序的建模能力。
3. **轻量开源模型的潜力**：Qwen2.5-VL-7B 在简单任务上接近 GPT-4o-mini 性能，适合资源受限场景。
4. **地图信息改善中等难度场景**：提供拓扑地图文本后，GPT-4o 在中等难度提升约 4.5 个百分点，优于简单和困难场景。
5. **CoT 效果有限**：CoT 只明显提升全局指令对齐，对执行任务和其他推理任务无改善，推测因为执行任务已是逐步决策，简单 CoT 缺乏结构化多步推理。
6. **错误类型分布**：失败案例中，错误计划占 45%、动作未对齐占 20%、停止失败占 15%、幻觉移动占 20%。中长期轨迹（＞5 步）使时间推理错误率从 35% 升至 76%。
7. **真实世界验证**：GPT-4o 成功率达 60%，Qwen2.5-VL-7B 达 40%，趋势与模拟一致，验证了基准的有效性。

## 7. 优点

- **系统性分解**：将导航能力拆分为理解（全局/时间/局部）和执行，提供比最终成功率更丰富的诊断信息。
- **多维度难度分类**：基于空间、认知、执行三个正交维度，并融合人类审核，有助于细粒度分析模型的泛化能力。
- **干扰策略设计精巧**：四种干扰项（基本/方向/物体/打乱）能有效探测不同层面的语言理解缺陷，尤其是打乱顺序暴露了时间推理弱点。
- **真实世界部署管道**：不仅限于模拟评估，还提供了从路点预测到低层控制的完整流水线，增强了基准的实用性。
- **全面模型覆盖**：评估了闭源和开源共 10 个模型，覆盖不同参数量级，并进行了多种消融分析（地图、CoT、错误类型、轨迹长度），结论可靠。
- **错误分析深入**：手动分析 100 个失败案例并分类，为模型改进提供具体方向。

## 8. 不足与局限

- **执行场景规模有限**：432 个 episode 在 72 个场景中相对较少，可能不足以覆盖所有环境变化，且每个难度的案例数可能不足以保证统计显著性。
- **模拟与现实差距**：模拟器中使用视点选择抽象，忽略了连续控制（如精确转向、避障）的挑战；真实世界实验仅 20 个案例，代表性有限。
- **难度分类权重经验设定**：三个复杂度公式的权重 α、β、γ 是经验值，未说明调优过程，可能影响分类的客观性。
- **零样本限制**：仅评估零样本能力，未考虑模型是否可以通过微调或上下文学习提升性能，对于实际应用场景的指导性有限。
- **干扰策略中“打乱子指令”可能引入语法问题**：虽然论文声明保持了语法正确性，但打乱后的指令可能语义不连贯（如方向序列混乱），增加了区分难度。
- **缺乏对环境动态变化的测试**：所有实验基于静态 Matterport3D 数据，未考虑移动物体、光照变化等挑战。
- **未报告计算时间或推理效率**：对于真实部署，推理速度是重要指标，论文未提及。
- **未探讨不同多模态融合策略的影响**：仅评估模型整体表现，未深入分析视觉编码器或跨模态对齐的具体影响。

（完）
