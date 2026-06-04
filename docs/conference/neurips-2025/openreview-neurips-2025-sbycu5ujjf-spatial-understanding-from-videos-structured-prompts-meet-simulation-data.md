---
title: "Spatial Understanding from Videos: Structured Prompts Meet Simulation Data"
title_zh: 视频空间理解：结构化提示遇见仿真数据
authors: "Haoyu Zhang, Meng Liu, Zaijing Li, Haokun Wen, Weili Guan, Yaowei Wang, Liqiang Nie"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=SBYCu5uJJf"
tags: ["query:vla"]
score: 5.0
evidence: 提升预训练视觉语言模型的3D空间推理能力以支持具身交互
tldr: 视觉空间理解对于具身导航和交互至关重要，但现有方法受限于空间不确定性和数据匮乏。本文提出统一框架，结合结构化提示策略SpatialMind和可扩展问答数据集ScanForgeQA，在不修改模型架构的情况下增强预训练视觉语言模型的3D空间推理能力。实验表明该方法在多个推理任务上取得显著提升，有望支撑下游具身应用。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1441, \"height\": 597, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1445, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 698, \"height\": 570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 678, \"height\": 504, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 703, \"height\": 562, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1443, \"height\": 736, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1307, \"height\": 862, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 997, \"height\": 613, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-sbycu5ujjf/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1447, \"height\": 488, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1458, \"height\": 259, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1427, \"height\": 1189, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 867, \"height\": 449, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 571, \"height\": 451, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1468, \"height\": 448, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1435, \"height\": 2003, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-sbycu5ujjf/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1452, \"height\": 1614, \"label\": \"Table\"}]"
motivation: 现有视觉语言模型的3D空间推理能力受限于空间不确定性和数据稀疏。
method: 提出SpatialMind结构化提示策略和ScanForgeQA仿真数据集，无需修改架构即可增强空间推理。
result: 在多个空间推理任务上取得性能提升，验证了框架的有效性。
conclusion: 该框架为增强预训练视觉语言模型的3D空间推理能力提供了一种高效、通用的方法。
---

## Abstract
Visual-spatial understanding, the ability to infer object relationships and layouts from visual input, is fundamental to downstream tasks such as robotic navigation and embodied interaction. However, existing methods face spatial uncertainty and data scarcity, limiting the 3D spatial reasoning capability of pre-trained vision-language models (VLMs). To address these challenges, we present a unified framework for enhancing 3D spatial reasoning in pre-trained VLMs without modifying their architecture. This framework combines SpatialMind, a structured prompting strategy that decomposes complex scenes and questions into interpretable reasoning steps, with ScanForgeQA, a scalable question-answering dataset built from diverse 3D simulation scenes through an automated construction process designed for fine-tuning. Extensive experiments across multiple benchmarks demonstrate the individual and combined effectiveness of our prompting and fine-tuning strategies, and yield insights that may inspire future research on visual-spatial understanding.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：视觉语言模型（VLM）在3D空间推理方面能力不足，主要表现为两个关键挑战：**空间不确定性**（从2D视频推断3D结构时存在遮挡、透视变形和纹理歧义）和**数据稀缺**（现有空间推理数据集规模小、多样性低，且大多依赖真实场景扫描，可扩展性差）。
- **整体含义**：本文致力于在不修改模型架构的前提下，提升预训练VLM的3D空间推理能力。这直接关系到机器人导航、具身交互、增强现实等下游应用，具有重要实际价值。

## 2. 方法论：核心思想、关键技术细节

### 2.1 核心思想
提出一种**双管齐下**的方法：
- **SpatialMind**：一种结构化思维链（CoT）提示策略，将复杂场景和问题分解为可解释的推理步骤。
- **ScanForgeQA**：一个大规模合成问答数据集，通过自动化管道从3D仿真场景构建，用于微调VLM以获取空间常识。

### 2.2 SpatialMind 提示策略
由**场景分解**和**问题分解**两部分组成：

- **场景分解**：
  1. **局部建模**：逐帧识别候选物体，并以随机参考物体为原点估计局部3D坐标。
  2. **坐标映射**：通过VLM推断相邻帧间的相对旋转和平移，累积变换矩阵，将所有局部坐标转换到统一全局坐标系。合并重复检测，得到全局3D地图。
  3. **认知生成**：将全局3D地图转化为**2D网格**和**自然语言描述**（物体相对于参考点的空间语句），供VLM理解。

- **问题分解**：
  1. 将问题分类（如物体大小、相对距离、相对方向）。
  2. 为每类设计固定的推理步骤（如“识别物体→估计坐标→计算距离→选择答案”），通过GPT-4o生成并人工验证。
  3. 推理时，根据问题类型选取对应步骤，结合场景表示输入VLM。

### 2.3 ScanForgeQA 数据集构建
三步流水线：
1. **场景构建**：
   - **分离**：从3D-FRONT（6813个多房间场景）中拆分为34,116个单房间场景（六类常见房间）。
   - **合成**：利用HoloDeck框架（LLM驱动）生成额外8类房间（增加办公室、商店），共160个场景。
2. **扫描创建**：使用Unity引擎模拟两种扫描策略：
   - **轨道扫描**：圆形轨迹，每5度一帧，共72帧。
   - **导航扫描**：基于NavMesh的路径扫描，起点和终点随机选择，共72帧（含起点/终点360度旋转）。
3. **QA生成**：定义三类问题：
   - **属性估计**（物体数量、大小、房间尺寸、类型），答案直接从标注获取。
   - **空间推理**（相对/绝对距离、方向、接触关系），基于3D坐标计算（欧氏距离、方向扇区等）。
   - **假设分析**（操作可行性，如放置或嵌入），比较物体尺寸。
   - 最终得到**34,276个场景、103K段视频、925K个QA对**。

## 3. 实验设计

### 3.1 数据集与基准
- **训练数据**：ScanForgeQA（93%用于训练，7%验证）。
- **评估基准**：
  - **VSI-Bench**（>5000个QA，288个室内场景，8种任务）。
  - **OpenEQA**（EM-EQA子集，1600+个QA，180+场景）。
  - **ScanQA**（9353个QA，71个场景）。
  - **SQA3D**（3261个QA，65个场景）。
- 对比方法包括：
  - **闭源模型**：Gemini-1.5/2.0 Pro、GPT-4o。
  - **开源模型**：InternVL2 (8B/40B)、InternVL2.5 (8B/38B)、LLaVA-NeXT-Video (7B/72B)、VideoLLaMA3 (7B)、Qwen2-VL (7B)、Qwen2.5-VL (7B/72B)。
- 指标：Accuracy、BLEU-1、EM-1 等。

### 3.2 资源与算力
论文明确说明：**所有实验在8张NVIDIA H20 GPU上完成**。未给出具体训练时长，对于闭源模型则通过API调用。

### 3.3 实验数量与充分性
- **主实验**：在VSI-Bench、OpenEQA、ScanQA、SQA3D四个基准上进行，涵盖8种任务类型。
- **消融实验**：
  - 不同场景表示（3D地图、2D网格、文本描述 → 文本描述最优）。
  - 对比SpatialMind与ScanForgeQA单独及联合效果。
  - 对比SpatialMind内部组件（仅问题CoT、仅场景描述、完整版）。
  - 对比不同微调数据（SQA3D、ScanQA、ScanForgeQA）。
  - 不同帧数和分辨率对性能的影响。
  - 混合微调（加入ShareGPT4Video数据）对通用视频任务的影响（MVBench、Video-MME）。
- **定性分析**：给出2个具体案例对比基线模型和增强模型。
- **全面性与公平性**：实验覆盖了从7B到72B的多种开源模型以及主流闭源模型，结果一致显示提升；对超参数（帧数、分辨率）进行鲁棒性检验；对比了现有空间数据集，证明合成数据的优势。实验设计较为充分、客观、公平。

## 4. 主要结论与发现
1. **SpatialMind和ScanForgeQA均能一致提升VLM的视觉空间推理能力**，闭源模型（Gemini-1.5 Pro、GPT-4o）和开源模型均有显著增益。
2. **两者互补**：联合使用（“+Both”）在几乎所有任务上取得最大提升。
3. **模型规模影响效益**：大模型（72B）从提示策略获益更多，小模型（7B）从微调数据获益更多。
4. **文本描述是最优场景表示**，优于3D地图和2D网格，说明当前VLM更擅长处理一维文本。
5. ScanForgeQA微调在保持通用视频理解能力的同时，还能提升空间推理相关任务（如MVBench），但会在纯事件理解任务（Video-MME）上造成轻微下降，可通过混合微调缓解。
6. **人工与VLM对比**：人类在定性任务（如外观顺序）完美，但在定量估计（如物体大小）上较差；VLM在定量任务上反而超人类，显示互补潜力。

## 5. 优点
- **无需修改模型架构**：通过提示+微调即可增强已有VLM，适用范围广。
- **可扩展的数据生成流水线**：合成场景避免了真实数据采集的高成本和隐私问题，且能控制多样性。
- **结构化提示设计**：显式分解场景和问题，增强了推理的可解释性和鲁棒性。
- **实验全面性**：覆盖多个基准、多种模型规模和多种消融设置，结论可靠。
- **开源计划**：代码、数据、模型权重将在论文发表后公开，促进可重复研究。

## 6. 不足与局限
- **场景单室为主**：虽然OpenEQA包含多房间场景并取得良好表现，但论文明确说明“we primarily focus on basic single-room 3D scene”，对于大型室内布局和室外环境探索不足。
- **对文本描述过度依赖**：实验显示VLM更善于理解文本描述，但文本可能无法直观捕捉空间语义，限制性能上限。
- **通用能力轻微下降**：在Video-MME上出现margin drop，虽可通过混合微调缓解，但并非完美无代价。
- **计算开销**：SpatialMind需要多次调用VLM进行推理（逐帧检测、坐标估计等），隐式计算成本未详细讨论。
- **数据集偏差**：合成场景可能与真实场景分布有差异，泛化到真实世界仍需验证。
- **公平性与偏见**：预训练模型的潜在偏见可能被继承，且空间准确性评估仍具挑战。

（完）
