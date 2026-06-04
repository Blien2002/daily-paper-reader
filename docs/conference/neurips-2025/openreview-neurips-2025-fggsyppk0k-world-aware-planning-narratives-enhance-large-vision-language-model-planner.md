---
title: World-aware Planning Narratives Enhance Large Vision-Language Model Planner
title_zh: 世界感知规划叙事增强大型视觉-语言模型规划器
authors: "Junhao Shi, Zhaoye Fei, Siyin Wang, Qipeng Guo, Jingjing Gong, Xipeng Qiu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=fggSyPPk0K"
tags: ["query:vla"]
score: 7.0
evidence: 通过世界感知叙事增强LVLM在具身规划中的能力
tldr: 大型视觉-语言模型在复杂多步具身规划任务中表现不佳，主要缺乏环境理解。本文提出世界感知规划叙事增强（WAP）框架，通过注入视觉外观、空间推理、功能抽象和语法基础四种认知能力，使LVLM能基于真实环境上下文进行规划。实验表明WAP在长周期任务中的成功率显著提升，且能更好地处理上下文相关指令。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-fggsyppk0k/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1402, \"height\": 553, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fggsyppk0k/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1416, \"height\": 1082, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1474, \"height\": 1420, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1410, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1260, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1477, \"height\": 319, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1454, \"height\": 299, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 989, \"height\": 227, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fggsyppk0k/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1223, \"height\": 185, \"label\": \"Table\"}]"
motivation: LVLM在复杂环境中的长程规划常忽略环境上下文。
method: 提出WAP框架，通过四种认知能力（外观、空间、功能、语法）将环境知识注入LVLM。
result: 在多个具身规划基准上，WAP显著提升了长周期任务的成功率。
conclusion: 注入世界感知知识可有效增强LVLM的具身规划能力。
---

## Abstract
Large Vision-Language Models (LVLMs) show promise for embodied planning tasks but struggle with complex scenarios involving unfamiliar environments and multi-step goals. 
Current approaches rely on environment-agnostic imitation learning that disconnects instructions from environmental contexts, causing models to struggle with context-sensitive instructions and rely on supplementary cues rather than visual reasoning during long-horizon interactions.
In this work, we propose World-Aware Planning Narrative Enhancement (WAP), a framework that infuses LVLMs with comprehensive environmental understanding through four cognitive capabilities (visual appearance modeling, spatial reasoning, functional abstraction, and syntactic grounding) while developing and evaluating models using only raw visual observations through curriculum learning.
Evaluations on the EB-ALFRED benchmark demonstrate substantial improvements, with Qwen2.5-VL achieving a 60.7 absolute improvement in task success rates—particularly in commonsense reasoning (+60.0) and long-horizon planning (+70.0). Notably, our enhanced open-source models outperform proprietary systems like GPT-4o and Claude-3.5-Sonnet by a large margin.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有大型视觉-语言模型（LVLM）在具身规划任务中，采用“环境无关的模仿学习”范式，将指令与环境上下文割裂。这导致模型在面对不熟悉环境、上下文敏感的指令、多步长周期任务时，泛化能力差、推理不一致，且倾向于依赖动作反馈等辅助线索而非纯视觉推理。
- **整体含义**：为了弥补LVLM在复杂真实场景中的规划缺陷，需要注入环境理解能力，使模型能从视觉观察中自主建立指令与环境的关联，实现闭环、无特权反馈的规划。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：提出 **世界感知规划叙事增强（WAP）** 框架，通过多维认知增强（视觉外观建模、空间关系推理、功能抽象学习、语法基础解析）将环境知识注入LVLM，并采用课程学习逐步提升模型能力。
- **关键技术细节**：
    - **指令增强**：利用高性能LVLM（Qwen2.5-VL-72B-Instruct）根据原始指令和轨迹生成四类增强指令（视觉、空间、功能、语法），并经过语义一致性校验确保任务等价。
    - **逐步推理生成**：为每个动作生成显式推理过程（包括环境状态、对象关系、动作前提等），作为中间监督信号。
    - **课程学习框架**：分三阶段训练：
        1. 基础阶段（原始指令-轨迹对）
        2. 环境理解阶段（加入视觉和空间增强）
        3. 概念推理阶段（加入功能和语法增强）
    - **闭环设置**：仅依赖原始视觉观测和自然语言指令，不依赖动作成功信号等特权反馈，模拟真实部署条件。

### 3. 实验设计

- **数据集与场景**：基于ALFRED轨迹构建增强语料（80,875条指令-轨迹对，源自16,145条原始轨迹），在**EB-ALFRED**（EmbodiedBench子集）上评估。
- **Benchmark**：EB-ALFRED，包含6类任务（Base、Common、Complex、Visual、Spatial、Long），采用成功率（SR）和标准差（STD）衡量平衡性。
- **对比方法**：
    - 专有模型：GPT-4o、Claude-3.5-Sonnet、Gemini系列等（在原始开环和更难的闭环设置下）
    - 开源模型：InternVL系列、Qwen2.5-VL系列、Llama-3.2-Vision等
    - 消融变体：是否使用WAP增强、逐步推理、课程学习等

### 4. 资源与算力

- **数据增强**：4×H100 GPU，共220 GPU小时（指令增强20小时，推理增强200小时）。
- **模型微调**：8×H100 GPU，共100 GPU小时（训练）。
- **总计算量**：约800 A100 GPU-hours（附录提到完整实验包括消融和超参调优共800 A100 GPU小时）。
- **硬件规格**：8×A100-80GB节点，采用张量并行、Flash Attention v2、BF16混合精度。

### 5. 实验数量与充分性

- **主要实验结果**：表1报告了多组模型在EB-ALFRED上的成功率，包含2种开源模型（Qwen2.5-VL-7B、InternVL3-8B）的多个变体，以及专有模型对比。
- **消融实验**：表5从完整框架逐步去除课程学习、逐步推理（首步/后续步）、WAP指令增强，共6种配置。
- **泛化实验**：表3在VOTA-Bench未见环境上测试WAP与GPT-4o对比。
- **敏感性分析**：表4探究教师模型大小（7B/32B/72B）的影响。
- **自导向增强对比**：表2比较显式课程与自导向策略。
- **充分性评价**：实验覆盖性能、消融、泛化、敏感性、成本-效果分析（表7），全面且客观；但未报告误差棒（遵循EmbodiedBench规范），统计显著性未明确说明。

### 6. 论文的主要结论与发现

- WAP框架在仅依赖原始视觉观测的闭环设置下，显著提升了LVLM的规划能力：Qwen2.5-VL-7B平均成功率从4.7%提升至62.7%（提升60.7%），在常识推理（+60.0）和长周期规划（+70.0）上尤为突出。
- 增强后的开源模型（Qwen2.5-VL-7B、InternVL3-8B）甚至超越GPT-4o和Claude-3.5-Sonnet等专有模型。
- 课程学习、逐步推理链、WAP指令增强三部分均不可或缺，首步推理对稳定性至关重要，后续推理保证空间和常识连贯性。
- 模型在未见环境和对象配置上展现出强泛化能力（VOTA-Bench上比GPT-4o高44%）。

### 7. 优点

- **方法创新**：首次系统地将四种认知能力注入具身规划，并通过课程学习渐进训练，符合认知发展理论。
- **实验完备**：多种基线、消融、泛化、敏感性分析，验证了各模块的有效性。
- **实用性强**：仅使用原始视觉观测，无特权反馈，更贴近真实部署场景。
- **开源且超越专有模型**：展示了开源模型在复杂任务上超越闭源系统的潜力。

### 8. 不足与局限

- **符号层抽象**：只规划高级符号动作（如“拿起刀”），未建模连续控制参数（如力度、轨迹），需后续与低层控制器结合。
- **场景局限**：仅在ALFRED家庭环境验证，未测试工业或户外动态场景。
- **无在线纠错**：训练时未设计执行中错误修正机制，模型缺乏动态调整能力。
- **计算成本**：推理时使用完整历史观测，计算量增加（单观测约1.6 GPU小时 vs 完整历史4.2 GPU小时），可能限制资源受限设备部署。
- **统计显著性未报告**：未提供误差棒或置信区间。

（完）
