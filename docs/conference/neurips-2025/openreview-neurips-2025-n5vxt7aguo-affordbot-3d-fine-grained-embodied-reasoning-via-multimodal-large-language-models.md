---
title: "AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models"
title_zh: AffordBot：基于多模态大语言模型的3D细粒度具身推理
authors: "Xinyi Wang, Xun Yang, Yanlong Xu, Yuchen Wu, Zhen Li, Na Zhao"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=N5vXT7AGuo"
tags: ["query:vla"]
score: 7.0
evidence: 利用多模态大语言模型进行细粒度3D具身推理
tldr: 有效的人-智能体协作需要理解在何处、如何行动，但现有方法仅处理对象级推理。本文提出细粒度3D具身推理任务，要求预测每个功能要素的空间位置、运动类型和运动轴。提出的AffordBot框架集成多模态大语言模型，从任务指令和3D场景中推理出结构化的三元组。实验证明该方法在细粒度动作理解上显著优于基线，为具身智能提供更精细的交互基础。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-n5vxt7aguo/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1433, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n5vxt7aguo/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1433, \"height\": 531, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n5vxt7aguo/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1401, \"height\": 327, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n5vxt7aguo/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1432, \"height\": 532, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n5vxt7aguo/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1429, \"height\": 1122, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1272, \"height\": 411, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 782, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 613, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 714, \"height\": 209, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1434, \"height\": 148, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 870, \"height\": 209, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n5vxt7aguo/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 654, \"height\": 247, \"label\": \"Table\"}]"
motivation: 现有具身推理方法缺乏对可操作元素的细粒度、指令驱动的理解。
method: 定义细粒度3D具身推理任务，并利用多模态大语言模型预测功能要素的位置、运动类型和轴。
result: 在合成的复杂场景数据集上，AffordBot在预测准确性上大幅超越现有方法。
conclusion: AffordBot推动了从对象级到元素级具身推理的进步，有助于人机协作。
---

## Abstract
Effective human-agent collaboration in physical environments requires understanding not only what to act upon, but also where the actionable elements are and how to interact with them. Existing approaches often operate at the object level or disjointedly handle fine-grained affordance reasoning, lacking coherent, instruction-driven grounding and reasoning. In this work, we introduce a new task: Fine-grained 3D Embodied Reasoning, which requires an agent to predict, for each referenced affordance element in a 3D scene, a structured triplet comprising its spatial location, motion type, and motion axis, based on a task instruction. To solve this task, we propose AffordBot, a novel framework that integrates Multimodal Large Language Models (MLLMs) with a tailored chain-of-thought (CoT) reasoning paradigm. To bridge the gap between 3D input and 2D-compatible MLLMs, we render surround-view images of the scene and project 3D element candidates into these views, forming a rich visual representation aligned with the scene geometry. Our CoT pipeline begins with an active perception stage, prompting the MLLM to select the most informative viewpoint based on the instruction, before proceeding with step-by-step reasoning to localize affordance elements and infer plausible interaction motions. Evaluated on the SceneFun3D dataset, AffordBot achieves state-of-the-art performance, demonstrating strong generalization and physically grounded reasoning with only 3D point cloud input and MLLMs. Our code is available at [https://github.com/hannahwxy/AffordBot](https://github.com/hannahwxy/AffordBot).

---

## 论文详细总结（自动生成）

# AffordBot：基于多模态大语言模型的3D细粒度具身推理 — 详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有具身推理方法大多停留在**对象级**理解（如识别“电视”），缺乏对可操作**元素级**（如电视遥控器上的按钮、抽屉把手）的细粒度、指令驱动的理解。同时，功能定位（affordance grounding）与运动估计（motion estimation）常被孤立处理，无法形成连贯的推理。
- **研究动机**：为了使人-智能体在真实3D环境中有效协作，智能体不仅要知道“做什么”，还要知道“在哪里做”以及“如何做”。例如，执行“拔掉圣诞树灯”指令时，需要精准定位插头（而非整棵树），并推断出“向外平移”的运动。
- **全新任务定义**：提出**细粒度3D具身推理**（Fine-grained 3D Embodied Reasoning），要求智能体根据自然语言指令，为场景中每个被引用的功能元素预测一个结构化三元组：**3D掩膜（空间位置）、运动类型（平移/旋转）、运动轴方向**。

## 2. 论文提出的方法论

### 2.1 核心思想
- 利用**多模态大语言模型（MLLM）** 的强大推理能力，结合**链式思考（Chain-of-Thought，CoT）** 范式，将3D场景信息转换为MLLM可理解的2D表示，实现从“观察”到“推理”的逐步执行。
- 关键在于**桥接3D点云与2D MLLM之间的模态鸿沟**：通过生成环绕视图、提取几何-语义描述符并建立3D-2D关联，构造丰富的多模态表示。

### 2.2 关键技术细节

#### 2.2.1 全局多模态表示构建（Holistic Multimodal Representation）
- **丰富视觉合成（Enriched Visual Synthesis）**：对场景中心点进行360°水平全景扫描，生成N个候选视图（N为超参数），克服传统视频帧视角有限、冗余度高的问题。
- **几何-语义描述符（Geometry-Semantic Descriptors）**：使用实例分割模型（Mask3D）提取功能元素，并为每个元素j构建几何描述符Gj（包含3D位置Cj和尺寸Σj）以及语义描述符Sj（功能类型）。训练时结合Dice损失和交叉熵损失：  
  `L_total = λ1·L_Dice + λ2·L_CE`  
  并采用**粗到细的课程学习策略**，通过逐步扩张真实掩膜δ_t来处理小目标。
- **3D-2D关联**：将3D元素投影到每个环绕视图上，得到2D边界框及其唯一ID和功能类型标签。采用**自适应标签精炼（Adaptive Label Refinement）** 避免标签重叠和遮挡。

#### 2.2.2 链式思考推理（Chain-of-Thought Reasoning）
- **步骤1：主动视图选择（Active View Selection）**  
  MLLM在获得多个标注视图后，根据指令自主选择信息量最丰富的视图（“观察”阶段），减少冗余输入并聚焦相关视觉线索。
- **步骤2：功能定位（Affordance Grounding）**  
  基于选定视图、指令和元素描述符，MLLM定位被引用的功能元素，输出其唯一ID。
- **步骤3：运动估计（Motion Estimation）**  
  MLLM结合指令与上一步定位信息，推断运动类型（平移/旋转）和运动轴方向（例如“水平向外”）。运动方向通过离散化为可解释的类别（水平/垂直、向内/向外等）以适应MLLM输出。

## 3. 实验设计

- **数据集**：**SceneFun3D**（唯一提供3D室内场景细粒度功能定位与运动估计标注的数据集）。共230个场景（200训练，30验证），含点云、元素级功能掩膜、运动类型与轴方向。
- **Benchmark**：采用标准指标：mIoU、mAP、AP@IoU=0.5/0.25（对掩膜），并扩展约束：+T（正确运动类型）、+TD（类型+轴方向）。
- **对比方法**：OpenMask3D、LERF、OpenIns3D、Fun3DU、Fun3DU (+motion)。其中Fun3DU(+motion)为作者复现的扩展基线（用Molmo推断运动）。
- **实现细节**：MLLM使用**Qwen2.5-VL-72B**；实例分割基于**Mask3D**在ScanNet200上微调，学习率0.0001，batch size 2，2cm体素化，训练1000 epochs。

## 4. 资源与算力

- MLLM推理：**4块NVIDIA A800 GPU**（本地部署Qwen2.5-VL-72B）。
- 分割模型训练：**1块NVIDIA A800 GPU**，1000 epochs。
- 训练时长未明确说明，但根据硬件推断约为数天量级。论文未报告整体推理耗时或GPU使用时间。

## 5. 实验数量与充分性

- **实验组数**：  
  - **主定量对比**（表1）：1组，包含6种方法，2个任务（功能定位、运动估计）共4个指标。  
  - **消融实验**（表2、3、4）：3组，分别针对关键组件、视角选择、瓶颈分析。  
  - **MLLM对比**（表5）：4种模型（LLaVA-v1.6-34B, Qwen2.5-VL-72B, GPT-4o, GPT-o1）。  
  - **性能变化分析**（表6、7）：按功能类型、目标数量分解。
- **定性展示**（图5）：4个示例场景。
- **充分性评价**：  
  - **优点**：消融实验设计合理，逐步揭示各模块贡献；瓶颈分析通过替换GT掩膜和视图明确主要限制；视角选择对比了多种策略（BEV、视频帧、查询对齐、动态选择）。  
  - **不足**：未报告误差棒或置信区间，单次运行缺乏统计显著性检验；缺少对运动估计单独（不依赖定位）的消融；未在更多数据集上验证泛化性（仅SceneFun3D）。

## 6. 论文的主要结论与发现

1. **性能领先**：AffordBot在功能定位（AP=15.5, AP50=20.0, AP25=23.3）和运动估计（+T=18.3, +TD=10.8）上均显著优于所有基线方法，验证了统一任务建模与MLLM结合的有效性。
2. **主要瓶颈**：实例分割噪声是限制整体性能的首要因素（替换为GT掩膜后AP25提升22.1%），主动视图选择虽有效但非根本。
3. **MLLM能力影响**：更强大的MLLM（GPT-o1）可显著提升性能（AP25从23.3%→33.4%），表明模型推理能力提升空间。
4. **不同类型/数量差异**：不同功能类型表现差异大（如“脚踏”100% vs “旋转”0%），部分因数据集不平衡和分割困难；多目标任务比单一目标任务表现更好（因单一目标多为小物体）。

## 7. 优点

- **任务定义创新**：首次将功能定位与运动估计统一为指令驱动的结构化三元组预测，更贴近真实机器人操纵需求。
- **方法设计巧妙**：巧妙利用MLLM的推理优势，通过环绕视图+CoT实现3D场景的2D兼容，避免传统视频处理的高冗余与视角局限。
- **消融实验深入**：对每个组件（自适应标签、视觉合成、视图选择）定量分析贡献；通过替换GT掩膜和视图精准定位瓶颈。
- **定性结果清晰**：可视化对比显示AffordBot在复杂场景（多目标、小目标）中定位更准确。

## 8. 不足与局限

- **实验覆盖有限**：仅使用单一数据集（SceneFun3D），且该数据集专注于室内场景，未在室外或更多样化场景下验证。
- **过度依赖分割质量**：瓶颈分析表明实例分割是主要误差来源，但论文未提出有效的分割改进方案（仅用Mask3D）。
- **缺乏统计严谨性**：所有实验无误差棒、无多次运行统计；结果可能受随机性影响。
- **运动离散化损失**：将连续运动轴方向离散化为有限类别（如“水平向外”），可能丢失精细运动信息，不利于精确机器人控制。
- **MLLM推理成本高**：使用72B级模型部署需多块高端GPU，实际应用时推理延迟和成本可能过高。
- **罕见类别表现差**：如“旋转”类型AP50为0%，数据集类别严重不平衡，模型难以学习。
- **视角选择未完全自动化**：虽为自主选择，但依赖预生成的固定角度视图，未考虑动态调整。

（完）
