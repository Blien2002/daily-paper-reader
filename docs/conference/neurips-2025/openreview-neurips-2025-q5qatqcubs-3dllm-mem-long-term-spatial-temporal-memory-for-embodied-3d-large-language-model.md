---
title: "3DLLM-Mem: Long-Term Spatial-Temporal Memory for Embodied 3D Large Language Model"
title_zh: 3DLLM-Mem：面向具身3D大语言模型的长期时空记忆
authors: "Wenbo Hu, Yining Hong, Yanjun Wang, Leison Gao, Zibu Wei, Xingcheng Yao, Nanyun Peng, Yonatan Bitton, Idan Szpektor, Kai-Wei Chang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=q5QaTQcUbS"
tags: ["query:vla"]
score: 7.0
evidence: 为具身3D大语言模型引入长期时空记忆
tldr: 人类擅长利用长期记忆完成复杂任务，但当前大语言模型在动态多房间3D环境中规划行动时缺乏适当的空间-时间记忆建模。本文首先提出3DMem-Bench基准，包含大量轨迹和具身任务。然后提出3DLLM-Mem，一种动态记忆管理与融合模型，使LLM能够存储和检索长期空间-时间经验，从而提升规划与行动能力。实验证明该方法在多种具身任务上显著优于无记忆基线。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-q5qatqcubs/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1429, \"height\": 629, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-q5qatqcubs/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1446, \"height\": 1154, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-q5qatqcubs/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1437, \"height\": 648, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-q5qatqcubs/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1440, \"height\": 436, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-q5qatqcubs/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1156, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-q5qatqcubs/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1404, \"height\": 1496, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-q5qatqcubs/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-q5qatqcubs/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1440, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-q5qatqcubs/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1440, \"height\": 336, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-q5qatqcubs/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1443, \"height\": 219, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-q5qatqcubs/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1226, \"height\": 1781, \"label\": \"Table\"}]"
motivation: 大语言模型在具身3D环境中缺乏长期时空记忆，难以有效规划和行动。
method: 提出动态记忆管理与融合模型3DLLM-Mem，为LLM提供长期空间-时间经验的存储与检索能力。
result: 在3DMem-Bench基准测试中，3DLLM-Mem在问答和任务规划上均超越现有模型。
conclusion: 3DLLM-Mem有效弥补了LLM在具身环境中记忆建模的缺失，推动了具身智能的发展。
---

## Abstract
Humans excel at performing complex tasks by leveraging long-term memory across temporal and spatial experiences. In contrast, current Large Language Models (LLMs) struggle to effectively plan and act in dynamic, multi-room 3D environments. 
We posit that part of this limitation is due to the lack of proper 3D spatial-temporal memory modeling in LLMs. 
To address this, we first introduce 3DMem-Bench, a comprehensive benchmark comprising over 26,000 trajectories and 2,892 embodied tasks, question-answering and captioning, designed to evaluate an agent's ability to reason over long-term memory in 3D environments.
Second, we propose 3DLLM-Mem, a novel dynamic memory management and fusion model for embodied spatial-temporal reasoning and actions in LLMs. 
Our model uses working memory tokens, which represents current observations, as queries to selectively attend to and fuse the most useful spatial and temporal features from episodic memory, which stores past observations and interactions. Our approach allows the agent to focus on task-relevant information while maintaining memory efficiency in complex, long-horizon environments.
Experimental results demonstrate that 3DLLM-Mem achieves state-of-the-art performance across various tasks, outperforming the strongest baselines by 16.5\% in success rate on 3DMem-Bench's  most challenging in-the-wild embodied tasks.

---

## 论文详细总结（自动生成）

## 论文深度总结：3DLLM-Mem：面向具身3D大语言模型的长期时空记忆

### 1. 核心问题与整体含义（研究动机与背景）

*   **研究动机**：人类能够通过整合跨时间和空间的长期记忆来执行复杂任务，但当前的大语言模型（LLM）在动态、多房间3D环境中进行规划和行动时表现不佳。作者认为，这一局限性的重要原因在于LLM中缺乏适当的3D空间-时间记忆建模。
*   **总体目标**：解决具身智能体在长期、多房间任务中无法有效存储、检索和利用空间-时间记忆的根本性挑战，弥合人类认知能力与AI系统之间的差距。

### 2. 方法论：核心思想与关键技术细节

*   **核心思想**：受人类认知结构（工作记忆与情景记忆）启发，为3D LLM设计一个动态记忆管理与融合模块，使其能够以任务相关的方式选择性利用历史空间-时间信息，同时保持记忆效率。
*   **关键模型：3DLLM-Mem**
    *   **基础架构**：基于LLaVA-3D（2D视觉特征+3D位置编码），扩展上下文窗口至8192 tokens。
    *   **双记忆系统**：
        *   **工作记忆（Working Memory）**：当前时刻的3D观察表示（点云特征），保留在上下文窗口中作为查询。
        *   **情景记忆（Episodic Memory）**：存储过去所有时间步的3D观察特征，使用多层感知机（MLP）投影至共享记忆空间，并加入时间步的正弦位置编码。
    *   **记忆融合机制（Memory Fusion）**：
        *   **查询生成**：将工作记忆特征作为查询（\( f_{Q}^{t} \)）。
        *   **注意力检索**：计算查询与情景记忆中所有键（\( f_{K} \)）的注意力权重，从值（\( f_{V} \)）中聚合相关信息，得到融合特征 \( f_{Q}^{\text{fuse}} \)。
        *   **融合输出**：将融合特征与原始工作记忆特征拼接，作为最终的记忆增强表示 \( f_{M} \)。
    *   **记忆更新**：工作记忆动态更新；当智能体进入新环境时，之前的工作记忆转入情景记忆；若环境中已有条目且被修改，则更新该条目，保持记忆反映最新环境状态。

### 3. 实验设计：数据集、基准与对比方法

*   **数据集与场景**
    *   **3D场景来源**：基于Habitat-Matterport 3D（HM3D）语义数据集（182个3D空间，2602个房间），额外添加来自Objaverse的交互式物体，使任务支持拾取、放置等操作。
    *   **Trajectory生成**：使用Gemini模型（通过box-demonstration-instruction提示）自动生成带标注轨迹，经过自动化验证和人工审核（4位学生专家）。
*   **新提出的基准：3DMem-Bench**
    *   **规模**：超过26,000条轨迹，1,860个细粒度长期记忆具身任务（分为简单/中等/困难三级，对应3、5、10个多房间场景），865个问答任务（EQA），167个描述任务。
    *   **任务类型**：包括具身操作、长期记忆EQA（空间推理、导航、比较、布局、计数）及描述任务；同时设有“in-the-wild”泛化评估集。
*   **对比方法**
    *   **无记忆/简单记忆基线**：Everything in Context（所有观察放上下文）、Most Recent Memory（仅最近观察）、Retrieval-Augmented Memory（RAG，检索最相关存储）。
    *   **现有3D模型**：3D-LLM（微调版）、3D-Mem（基于Gemini/GPT-4o的记忆框架，但无动作执行）。
    *   **自对比模型**：3DLLM-Mem（本文方法）。

### 4. 资源与算力

*   **训练资源**：8块Google Cloud TPU v5p核心，批量大小256，训练约1000步（约1天）。使用Adam优化器，学习率2e-5，线性预热后余弦衰减。
*   **模型初始化**：从LLaVA-3D预训练权重开始，微调整个记忆模块及LLM解码器。
*   **评估算力**：未明确说明，但所有基线均在同一硬件环境复现。

### 5. 实验数量与充分性

*   **实验组数**：
    *   具身任务：在简单、中等、困难三个难度级别上，分别评估in-domain和in-the-wild的表现，记录成功率和子成功率。
    *   EQA任务：覆盖5个子类别（空间关系、导航、比较、布局、计数），使用LLM-as-judge（Gemini）评分。
    *   描述任务：报告BLEU-1/4、METEOR指标。
    *   消融实验：针对记忆融合查询初始化方式的3种变体（工作记忆vs.最近情景记忆vs.可学习零参数）。
    *   共约数十项主要结果比较。
*   **充分性**：实验覆盖了不同任务、不同难度、不同记忆策略、不同模型架构，并包含消融和泛化测试。对比基线均为当前主流方法，实验设置公平（所有基线在同一数据拆分和评估流程下测试）。统计上未报告误差棒（如多次重复运行），但考虑到计算成本较高，属于可接受范围。

### 6. 主要结论与发现

*   3DLLM-Mem在所有任务上大幅超越所有基线。
    *   在最具挑战性的in-the-wild具身任务中，平均成功率比最强基线（Retrieval-Augmented Memory）高出16.5个百分点（32.1% vs 15.6%）。
    *   尤其在困难级别的in-the-wild任务中，基线成功率仅约5%，而3DLLM-Mem仍保持27.8%的成功率，证明了其长期记忆管理的可扩展性和有效性。
    *   在EQA和描述任务上也全面领先，显示了融合型内存对空间-时间推理的促进作用。
*   消融实验证实，使用工作记忆作为融合查询是最优设计，优于使用最近情景记忆或可学习零参数初始化。

### 7. 优点（方法与实验设计亮点）

*   **方法创新性**：首次将稠密3D点云表示作为情景记忆，并设计基于注意力机制的动态融合模块，兼顾了信息丰富度和计算效率。
*   **基准全面性**：构建的3DMem-Bench不仅规模大，而且引入了多难度、in-the-wild、长期记忆推理（EQA/captioning）等新颖评估维度，填补了现有基准的空白。
*   **实验设计严谨**：对比了多种记忆管理基线（全上下文、最近记忆、检索增强），并进行了消融分析，验证了每个设计选择的必要性。
*   **泛化能力强**：方法在未见过的场景和任务上表现稳健，具有实际应用潜力。

### 8. 不足与局限

*   **低级控制缺失**：当前模型依赖模拟器中预定义的高级动作策略，未集成低级导航和控制策略。虽然作者认为这一方面与核心贡献正交，但限制了实际机器人部署的完整性。
*   **计算资源要求高**：训练需要8个TPU v5p（或等效算力），且上下文窗口扩展至8192 token，对资源有限的研究组复现可能困难。
*   **偏差与幻觉风险**：模型基于LLaVA-3D和LLaMA/Vicuna，继承了其潜在的偏见、准确性问题和幻觉倾向，可能影响关键任务的可信度。
*   **实验统计性**：未在多次运行中报告误差棒，单次运行结果可能存在随机波动，降低结论的统计稳健性。
*   **场景真实性**：环境基于HM3D合成+虚拟物体，与真实世界（如光照变化、物体变形等）仍有差距，泛化至真实环境需要进一步验证。
*   **记忆更新策略**：当前记忆更新仅基于环境是否已存在，未涉及更细粒度的记忆重叠/冲突处理，可能在高动态场景下不够鲁棒。

（完）
