---
title: "UP-VLA:  A Unified Understanding and Prediction Model for Embodied Agent"
title_zh: UP-VLA：面向具身智能体的统一理解与预测模型
authors: "Jianke Zhang, Yanjiang Guo, Yucheng Hu, Xiaoyu Chen, Xiang Zhu, Jianyu Chen"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=V7JPraxi5j"
tags: ["query:vla"]
score: 9.0
evidence: 面向具身智能体的VLA模型
tldr: 现有VLA模型依赖预训练的视觉语言模型，但这类模型往往忽略低级空间特征和物理动态，不利于具身控制。本文提出UP-VLA，一种统一的理解与预测模型，通过联合训练视觉-语言理解和动作预测，增强了模型对空间信息和物理动态的捕捉能力。实验表明，UP-VLA在多个具身任务上取得了更好的泛化性能，为VLA模型的设计提供了新范式。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 855, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 862, \"height\": 589, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1727, \"height\": 632, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1718, \"height\": 687, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1734, \"height\": 568, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 848, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-v7jpraxi5j/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1753, \"height\": 635, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-v7jpraxi5j/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1763, \"height\": 628, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-v7jpraxi5j/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1628, \"height\": 306, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-v7jpraxi5j/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 872, \"height\": 348, \"label\": \"Table\"}]"
motivation: 现有多数VLA模型使用预训练的VLM，但VLM侧重高层语义而忽略低级空间与物理信息，限制了具身控制性能。
method: 提出UP-VLA统一模型，同时进行视觉语言理解和未来状态预测的训练，利用双向信息流增强低级特征学习。
result: 在多个机器人操作基准上，UP-VLA相比基线方法取得更高的任务成功率，尤其在需要空间理解的任务中提升显著。
conclusion: UP-VLA验证了在VLA中融合理解与预测任务的有效性，为构建更鲁棒的具身模型提供了新方向。
---

## Abstract
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities.
VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. 
However, prior research has shown that VLMs often focus on
high-level semantic content and neglect low-level features, 
limiting their ability to capture detailed spatial information and understand physical dynamics.
These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms.
In this paper, we investigate the training paradigm for VLAs, and 
introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33\% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有大多数VLA模型（如RT-2、OpenVLA）依赖预训练的视觉语言模型（VLM）作为骨干，VLM在视觉问答等任务上表现优异，提供了丰富的语义知识和推理能力。然而，近期研究表明，VLM普遍更关注高层语义内容，而忽略了低级视觉细节（如距离、尺寸、物体精确位置）以及物理动态理解能力。这些低级信息对于具身智能体（如机器人操控）中的精确控制和空间感知至关重要，但现有预训练范式未给予足够重视。
- **核心问题**：能否设计一种更好的预训练流水线，既能保留VLM的高层语义理解优势，又能强化低级视觉和空间特征，从而提升机器人在真实环境中的操控性能？
- **论文含义**：本文提出**UP-VLA**（Unified Understanding and Prediction Vision-Language-Action Model），通过统一的训练范式同时注入多模态理解（Multi-modal Understanding）和未来预测（Future Prediction）目标，使模型兼顾高层语义和低级细节。实验表明，该方法在CALVIN仿真基准上比之前最优方法提升33%，并在真实世界操控任务中取得显著改进。

### 2. 论文提出的方法论

- **核心思想**：利用自回归Transformer（基于Phi-1.5），通过灵活的注意力掩码机制，在同一模型中联合训练三种类型的数据：视觉-语言理解数据（如LLava-tuning）、视频/未来帧预测数据（如Bridge数据集）、以及机器人动作数据。这样，模型既能回答关于场景的问题（高层理解），又能预测未来的图像变化（低级动态），并据此生成动作。
- **关键技术细节**：
  - **模型架构**：采用Show-o（Xie et al., 2024）作为初始化骨干，LLM为Phi-1.5。对于理解任务，使用连续视觉编码器（CLIP-ViT + 投影层）将图像映射到语言嵌入空间；对于预测任务，使用离散图像编码器（VQ-GAN/MagVIT）将当前观测编码为离散token，然后自回归预测未来图像token。
  - **统一输入格式**：使用特殊标记（如`<MMU>`, `<T2I>`, `<PRE>`, `<ACT>`）区分任务类型，并设计两种attention mask：理解任务中图像token先于文本token且能相互注意；预测任务中图像token置于文本之后，能注意所有输入信息。
  - **动作学习增强**：在第二阶段微调时，模型不仅预测未来图像和动作序列，还利用自身生成的高层场景描述（通过理解任务得到）扩展语言指令，从而让动作生成同时依赖高层语义和低级视觉信息。
  - **训练流程**：
    1. 第一阶段（预训练）：在Bridge数据集（25k机器人演示）上进行未来预测，同时在LLava-tuning数据集（665k图像-文本对）上进行理解任务，共训练20k步。
    2. 第二阶段（动作微调）：在目标机器人数据集上联合训练未来预测和动作生成，同时继续混合理解数据以保持能力。
  - **损失函数**：语言建模损失（交叉熵）、图像预测损失（交叉熵）、动作损失（位置MSE + 末端执行器状态二分类交叉熵），加权求和。

### 3. 实验设计

- **数据集/场景**：
  - **仿真环境**：CALVIN基准（Mees et al., 2022），包含4个不同场景A、B、C、D，每个场景有多个语言指令任务。评估两种设置：**ABC→D**（在A、B、C上训练，在D上零样本测试泛化能力）和**ABCD→D**（在A、B、C、D上训练，在D上测试）。
  - **真实世界环境**：Franka-Emika Panda机器人，包含6种技能（抓取、放置、排线、按按钮、拉抽屉等），收集约2k条演示。训练在简单场景下进行，测试在更复杂的场景（更多干扰物、新物体、精确操作如抓取小球/笔）。
- **Benchmark**：CALVIN中长链条任务（最多5个子任务连续执行，衡量平均完成长度）；真实世界任务以成功率（20次尝试）评估，分为**seen**（训练见过的物体）、**unseen**（新物体）、**precise**（高精度操作）三类。
- **对比方法**：
  - **VLM-based VLA方法**：RT-2（复现为UP-VLA-RT-2）、Robo-Flamingo、3D-VLA。
  - **预测类方法**：Uni-Pi、SuSIE、GR-1、UP-VLA-phi-w/o-mmu（纯预测基础）。
  - **其他方法**：RT-1、Diffusion Policy、3D Diffuser Actor。
- **消融实验**：对比完整UP-VLA与去除MMU、去除Bridge预训练、去除未来预测、去除MMU条件增强共4种变体，在CALVIN ABC→D和真实世界任务上评估。

### 4. 资源与算力

- 论文**未明确说明**使用的GPU型号、数量、总训练时长。仅在附录中提及预训练阶段20k步（batch size=64），动作微调阶段batch size=64，但未给出具体硬件信息。这可能是论文的不足之一。

### 5. 实验数量与充分性

- **实验数量**：包含3个主要实验表格（Table 1、Table 2、Table 3）和1个真实世界结果图（Figure 6），涵盖了仿真零样本长序列评估、仿真在分布内评估、以及真实世界三个难度级别的任务。消融实验包含5种变体（包括完整模型）在2个场景下测试。
- **充分性与公平性**：
  - 仿真对比的基线数量较多（10+种），涵盖了不同流派（VLA、预测、多模态大模型），且对某些基线进行了复现以确保公平。
  - 真实世界实验中，所有方法使用相同的数据集和硬件，并标注了复现版本（如UP-VLA-RT-2、UP-VLA-phi-w/o-mmu），但某些基线（如RT-1、Diffusion Policy）使用的是开源代码，可能因实现差异略有偏差。
  - 消融实验设计合理，能够分别验证每个模块（理解、预测、预训练、条件增强）的贡献。
  - 主要局限：真实世界任务每个条件仅报告20次尝试，统计显著性可能不足；仿真任务仅报告5个任务的链式完成率，未报告方差；未见跨本体或多平台实验；计算资源细节缺失。

### 6. 论文的主要结论与发现

- **联合训练理解与预测的有效性**：UP-VLA在CALVIN ABC→D上达到4.08的平均完成长度，显著优于纯VLA方法（如UP-VLA-RT-2的1.44）和纯预测方法（如GR-1的3.06），验证了融合两种目标带来的互补增益。
- **未来预测提升低级视觉/空间理解**：去除未来预测后，性能从4.08骤降至1.44，说明预测任务对捕捉物理动态和空间细节至关重要。
- **多模态理解增强语义泛化**：在真实世界新物体任务上，UP-VLA（含MMU）比纯预测模型（UP-VLA-phi-w/o-mmu）表现更好；而在精确操作任务上，未来预测更关键，体现了两者的互补性。
- **CALVIN ABC→D 提升33%**：相比之前最优方法（3D Diffuser Actor的3.35），UP-VLA的4.08提升了约22%；若仅比较同类baseline，提升更显著。

### 7. 优点

- **创新性**：首次系统地在VLA训练中联合注入高层语义理解和低级视觉预测，并设计了统一的注意力掩码和提示格式，避免了额外模型或复杂级联。
- **实验充分**：在仿真和真实世界两个平台上，覆盖了泛化、精确控制、多任务学习等多个维度，基线选择全面且公平。
- **消融实验设计清晰**：能明确归因每个模块的贡献，验证了核心假设。
- **开源**：提供了代码仓库（GitHub），可复现性良好。
- **性能提升显著**：特别是在需要泛化的ABC→D场景，提升幅度大，且真实世界任务中所有三类任务均取得最优。

### 8. 不足与局限

- **计算资源不透明**：未报告训练所需的GPU型号、数量和时间，不利于其他研究者估算成本或进行公平对比。
- **预训练数据规模有限**：仅使用Bridge 25k演示和LLava-665k，相比RT-2等使用了更大规模数据的方法，模型规模（1.3B）和数据量可能限制了泛化潜力。
- **真实世界评估样本量小**：每个任务仅20次尝试，未提供置信区间，统计可靠性有待加强。
- **未来预测质量限制**：如文中提及，在CALVIN D场景下的预测图像背景颜色出现偏差（模型倾向于使用训练场景A/B/C的背景），说明视觉生成泛化能力不足。
- **动作输出空间未详细分析**：论文未讨论动作表示（连续/离散）对性能的影响，也未与纯扩散动作策略（如Diffusion Policy）进行更深入的比较。
- **未进行跨本体或跨平台验证**：仅使用Franka Panda机器人，结论的通用性需进一步验证。
- **未探讨推理效率**：自回归式生成未来图像和动作可能导致推理延迟，论文未分析实时性。

（完）
