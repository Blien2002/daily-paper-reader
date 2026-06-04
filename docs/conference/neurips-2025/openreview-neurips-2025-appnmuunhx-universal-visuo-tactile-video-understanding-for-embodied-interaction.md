---
title: Universal Visuo-Tactile Video Understanding for Embodied Interaction
title_zh: 面向具身交互的通用视觉-触觉视频理解
authors: "Yifan Xie, Mingyang Li, Shoujie Li, Xingting Li, Guangyu Chen, Fei Ma, Fei Yu, Wenbo Ding"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=aPPnmuuNhx"
tags: ["query:vla"]
score: 5.0
evidence: 用于具身交互中视觉-触觉理解的多模态大模型
tldr: 现有方法未能有效结合触觉信息进行物理理解。本文提出首个通用视觉-触觉视频理解多模态大语言模型VTV-LLM，并贡献了含150K帧的VTV150K数据集。模型能够理解跨传感器、跨模态的触觉视频内容，为具身智能提供了关键的触觉语言接口。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-appnmuunhx/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1438, \"height\": 969, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-appnmuunhx/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1436, \"height\": 1221, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-appnmuunhx/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1450, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-appnmuunhx/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1435, \"height\": 454, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-appnmuunhx/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1454, \"height\": 619, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-appnmuunhx/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1440, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-appnmuunhx/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 710, \"height\": 189, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-appnmuunhx/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 709, \"height\": 214, \"label\": \"Table\"}]"
motivation: 现有物理理解方法忽略触觉信息，缺乏跨传感器触觉语言模型。
method: 构建首个视觉-触觉视频多模态大语言模型及大规模数据集。
result: 实现了跨传感器、跨模态的触觉视频理解。
conclusion: 为具身智能提供了触觉感知与语言的桥梁。
---

## Abstract
Tactile perception is essential for embodied agents to understand the physical attributes of objects that cannot be determined through visual inspection alone. While existing methods have made progress in visual and language modalities for physical understanding, they fail to effectively incorporate tactile information that provides crucial haptic feedback for real-world interaction. In this paper, we present VTV-LLM, the first multi-modal large language model that enables universal Visuo-Tactile Video (VTV) understanding, bridging the gap between tactile perception and natural language. To address the challenges of cross-sensor and cross-modal integration, we contribute VTV150K, a comprehensive dataset comprising 150,000 video frames from 100 diverse objects captured across three different tactile sensors (GelSight Mini, DIGIT, and Tac3D), annotated with four fundamental tactile attributes (hardness, protrusion, elasticity, and friction). We develop a novel three-stage training paradigm that includes VTV enhancement for robust visuo-tactile representation, VTV-text alignment for cross-modal correspondence, and text prompt finetuning for natural language generation. Our framework enables sophisticated tactile reasoning capabilities including feature assessment, comparative analysis, and scenario-based decision-making. Extensive experimental evaluations demonstrate that VTV-LLM achieves superior performance in tactile reasoning tasks, establishing a foundation for more intuitive human-machine interaction in tactile domains.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **背景**：触觉感知对于具身智能体理解物体的物理属性（如硬度、纹理、柔顺性）至关重要，这些属性无法仅通过视觉推断得出。然而，现有的视觉-语言模型在处理物理交互时，因缺乏触觉信息而受到根本限制。
- **问题**：现有触觉学习方法要么只关注静态属性，要么未能有效将触觉感知与自然语言理解整合；同时，不同的触觉传感器（如 GelSight、DIGIT、Tac3D）产生的数据格式差异大，导致跨传感器迁移困难。此外，触觉交互的时间动态信息（按压、滑动、旋转）在现有工作中被忽视。
- **整体含义**：本文旨在构建首个能够实现通用视觉-触觉视频理解的大型多模态语言模型，将触觉感知作为跨模态推理问题，从而为更直观的人机物理交互奠定基础。

## 2. 方法论：核心思想、关键技术细节
### 核心思想
- 将触觉视频视为连续帧序列，通过三阶段训练范式，首先学习鲁棒的视觉-触觉表示，然后将其与文本描述对齐，最后优化自然语言生成，使模型能够执行复杂的触觉推理。

### 关键技术细节
- **数据集 VTV150K**：
  - 包含 100 个常见物体、3 种触觉传感器（GelSight Mini、DIGIT、Tac3D）采集的 150,000 帧视频（20FPS，320×320）。
  - 标注 4 个基本触觉属性（硬度、突出度、弹性、摩擦），每个分为 3 个等级。
  - 通过模板生成 10,000 个问答对，涵盖特征评估、比较分析、场景决策等任务。

- **模型架构**：
  - 采用 Qwen 2.5 系列 LLM 作为骨干，结合 VTV 编码器（基于 ViT-base，借鉴 VideoMAE 并改进）和两个投影器（V-Projector、T-Projector）。
  - 引入特殊 token `<video_start>`、`<video>`、`<video_end>` 表示视频的起止和内容。

- **三阶段训练框架**：
  1. **VTV 增强**：针对触觉视频动态特性，提出**光流引导掩码策略**：
     - 选取中间帧作为关键帧，使用高斯混合模型生成连续值掩码（而非二值化），保留空间结构。
     - 利用 RAFT 网络计算双向光流，指导时间一致性掩码生成。
     - 训练 VTV 编码器-解码器进行视频重建（MSE 损失），并附加属性分类器（交叉熵损失），联合优化。
  2. **VTV-文本对齐**：冻结 LLM，仅训练 V-Projector 和 T-Projector，利用 VTV150K 数据集建立跨模态对应。
  3. **文本提示微调**：使用 LoRA 微调 LLM 和投影器，使用独立生成的 10,000 个问答对进行监督训练，增强自然语言生成能力。

- **数学表示**：给出了从视频帧到特征提取、视觉嵌入、最终响应的公式化流程。

## 3. 实验设计
### 数据集与场景
- **训练集**：VTV150K 数据集（100 个物体，多传感器）。
- **测试集**：独立的 600 个问答对，来自训练中未见过的新物体，覆盖全部推理任务（特征评估、SFD、SOI、OSC、TSA）。
- **任务类型**：
  - 触觉特征评估（单属性和组合属性）
  - 表面特征区分（SFD）
  - 表面最优性识别（SOI）
  - 物体感觉关联（OSC）
  - 触觉场景分析（TSA，零样本任务）

### Benchmark 及对比方法
- 对比 7 个方法：
  - **闭源**：GPT-4o、Gemini-2.5-Pro-Exp
  - **开源**：LLaVA-OneVision-7B、LLaVA-Video-Qwen2-7B、InternVL2.5-VL-8B、VideoLLaMA3-7B、Qwen2.5-VL-7B
- 报告三次随机种子运行的平均结果，确保公平。

## 4. 资源与算力
- **硬件**：4 块 NVIDIA RTX 6000 Ada GPU。
- **训练时长**：论文未明确说明各阶段的具体训练时长，仅在实验设置中提及了 GPU 数量和模型参数规模（3B、7B、14B 三种）。
- **备注**：文中未提供详细的时间开销，但代码和数据集将在接受后公开。

## 5. 实验数量与充分性
- **主要对比实验**：表 1 展示了 VTV-LLM-7B 与全部基线在 6 个任务上的性能，覆盖单属性、组合属性、高级推理任务。
- **消融实验**：
  - **LLM 骨干规模对比**（图 5）：3B、7B、14B，验证模型性能与规模正相关。
  - **VTV 编码器设置**（表 2）：比较未训练 VideoMAE、训练后 VideoMAE、无分类器的方法、完整方法，共 4 种。
  - **三阶段训练范式**（表 3）：移除 stage2、移除 stage3、使用相同数据集在不同阶段、完整方法，共 4 种。
- **充分性评价**：实验设计全面，既对比了强闭源与开源模型，又进行了关键模块消融，测试集包含零样本任务，结果可信。但缺少真实机器人部署的实证评估。

## 6. 主要结论与发现
- VTV-LLM 在所有任务上大幅超越所有基线，尤其在组合属性推理上（35.6% vs 基线最高 4.3%），证明其跨模态对齐的有效性。
- 三阶段训练策略缺一不可：缺少对齐或微调阶段分别导致性能下降 8.2% 和 15.5%。
- 使用独立数据集进行不同阶段训练能避免过拟合，提升泛化能力。
- 更大模型（14B）在复杂推理任务（如 TSA）上改进更显著，但计算代价增加。
- 触觉场景分析（TSA）作为零样本任务达到 64% 准确率，表明模型具备一定的物理常识推理能力。

## 7. 优点
- **首创性**：第一个将视觉-触觉视频与大型语言模型结合的通用框架，填补了跨模态触觉推理的空白。
- **数据贡献**：VTV150K 数据集规模大、覆盖多传感器、标注细致，为后续研究提供基准。
- **方法创新**：
  - 针对触觉视频动态特性设计的光流引导掩码策略，优于传统 VideoMAE 的 tube masking。
  - 三阶段训练逻辑清晰，逐步提升表示、对齐和生成能力，且验证了各阶段必要性。
- **实验全面**：对比了多种主流模型，包含零样本任务，消融实验揭示关键组件贡献。
- **开放性**：代码与数据计划公开，有利于社区复现与扩展。

## 8. 不足与局限
- **局限性**：论文在正文中未设专门章节讨论局限性，仅在 NeurIPS Checklist 中提及已在补充材料中讨论。根据可获取信息，可推断以下不足：
  - 数据集仅包含 100 个物体，且为手工交互采集，可能存在标注主观性与一致性偏差。
  - 传感器类型仅为三种视觉触觉传感器，未覆盖其他触觉传感技术（如压阻、电容等）。
  - 所有实验均在实验室环境下进行，缺乏真实机器人操作任务验证。
  - 零样本任务（TSA）准确率仅 64%，仍有较大提升空间，表明模型对真实场景推理的泛化能力有限。
  - 模型参数量较大（7B/14B），推理效率在实时交互场景中可能受限。
- **偏差风险**：物体选取和属性标注可能带有采集者主观偏好，训练数据中属性分布不均衡（如“硬”物体占 39%，“无摩擦”占 32%），可能引入统计偏差。

（完）
