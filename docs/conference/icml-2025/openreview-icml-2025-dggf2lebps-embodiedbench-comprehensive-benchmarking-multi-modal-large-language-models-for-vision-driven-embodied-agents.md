---
title: "EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents"
title_zh: EmbodiedBench：多模态大语言模型用于视觉驱动具身代理的综合基准
authors: "Rui Yang, Hanyang Chen, Junyu Zhang, Mark Zhao, Cheng Qian, Kangrui Wang, Qineng Wang, Teja Venkat Koripella, Marziyeh Movahedi, Manling Li, Heng Ji, Huan Zhang, Tong Zhang"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=DgGF2LEBPS"
tags: ["query:vla"]
score: 9.0
evidence: 基于多模态大模型的视觉驱动具身代理基准
tldr: 多模态大模型驱动的具身代理研究缺乏全面评估。本文提出EmbodiedBench，包含四个环境中1128个测试任务，涵盖高层语义任务（如家务）和底层原子动作（如导航和操作），并设六个精心策划的子集。该基准系统评估MLLM基于具身代理的能力，为VLA模型在具身智能中的应用提供了标准化评估平台。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1680, \"height\": 907, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1705, \"height\": 986, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1744, \"height\": 451, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 842, \"height\": 284, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 847, \"height\": 647, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 823, \"height\": 454, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1769, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1774, \"height\": 403, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1157, \"height\": 546, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1333, \"height\": 510, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1333, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1246, \"height\": 412, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1740, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1244, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 343, \"height\": 344, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 344, \"height\": 344, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 343, \"height\": 345, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 346, \"height\": 347, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1247, \"height\": 414, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 744, \"height\": 716, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1379, \"height\": 1102, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1574, \"height\": 976, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1264, \"height\": 223, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1256, \"height\": 226, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1534, \"height\": 224, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1012, \"height\": 226, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1409, \"height\": 546, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1326, \"height\": 228, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1335, \"height\": 229, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1331, \"height\": 227, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-dggf2lebps/fig-031.webp\", \"caption\": \"\", \"page\": 0, \"index\": 31, \"width\": 1390, \"height\": 1181, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1769, \"height\": 526, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1765, \"height\": 1125, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1682, \"height\": 1321, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1329, \"height\": 1142, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1661, \"height\": 2124, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1768, \"height\": 759, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1594, \"height\": 651, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1592, \"height\": 647, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 878, \"height\": 188, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1240, \"height\": 1306, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1654, \"height\": 854, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 900, \"height\": 624, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1537, \"height\": 1642, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-dggf2lebps/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1547, \"height\": 740, \"label\": \"Table\"}]"
motivation: 现有缺乏评估MLLM驱动具身代理的全面框架。
method: 构建包含1128个任务和六个子集的基准，覆盖多种环境。
result: 提供了评估具身代理能力的标准化平台。
conclusion: 该基准可推动MLLM在具身智能中的研究。
---

## Abstract
Leveraging Multi-modal Large Language Models (MLLMs) to create embodied agents offers a promising avenue for tackling real-world tasks. While language-centric embodied agents have garnered substantial attention, MLLM-based embodied agents remain underexplored due to the lack of comprehensive evaluation frameworks. To bridge this gap, we introduce EmbodiedBench, an extensive benchmark designed to evaluate vision-driven embodied agents.
EmbodiedBench features: (1) a diverse set of 1,128 testing tasks across four environments, ranging from high-level semantic tasks (e.g., household) to low-level tasks involving atomic actions (e.g., navigation and manipulation); and (2) six meticulously curated subsets evaluating essential agent capabilities like commonsense reasoning, complex instruction understanding, spatial awareness, visual perception, and long-term planning.
Through extensive experiments, we evaluated 24 leading proprietary and open-source MLLMs within EmbodiedBench. Our findings reveal that: MLLMs excel at high-level tasks but struggle with low-level manipulation, with the best model, GPT-4o, scoring only $28.9\\%$ on average. EmbodiedBench provides a multifaceted standardized evaluation platform that not only highlights existing challenges but also offers valuable insights to advance MLLM-based embodied agents. Our code and dataset are available at [https://embodiedbench.github.io](https://embodiedbench.github.io).

---

## 论文详细总结（自动生成）

## 论文中文总结

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：当前多模态大语言模型（MLLM）在驱动具身代理方面展现出巨大潜力，但缺乏全面、标准化的评估框架。已有的语言中心式具身代理评估工作较多，而针对MLLM的评估仍不充分，特别是对视觉驱动、低层动作控制（如导航、操作）的能力评估几乎空白。
- **整体含义**：本文旨在填补这一空白，通过构建一个涵盖高层语义任务与低层原子动作、具备细粒度能力评估的基准——EmbodiedBench，系统性地衡量和揭示当前MLLM在具身智能场景中的实际表现与瓶颈。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：构建多环境、多任务、多能力维度的综合评估平台，并设计统一的可扩展代理框架，允许MLLM以“视觉感知+语言推理+多步规划”的方式与模拟环境交互。
- **关键技术细节**：
  - **任务分层**：将动作分为高层动作（如找物体、拾取、放置）和低层动作（如平移、旋转、夹爪控制），涵盖四个具体环境：
    - EB-ALFRED（高层家务，动作空间171-298个高层面）
    - EB-Habitat（高层家居，70个技能）
    - EB-Navigation（底层导航，8个低层动作）
    - EB-Manipulation（底层操作，7维离散化动作向量）
  - **能力子集**：每个环境包含6个能力子集（Base、Common Sense、Complex Instruction、Spatial Awareness、Visual Appearance、Long Horizon），通过指令增强或人工标注构建。
  - **统一代理框架**：基于MLLM的任务规划器，接收当前视觉图像（可含检测框）、任务指令、历史交互反馈、少量上下文示例，输出JSON格式的视觉描述、推理、语言计划和可执行动作序列。采用多步规划（一次输出多个动作）以减少API调用。
  - **离散化与辅助信息**：对于底层操作，将连续动作空间离散化为整数（位置100 bin，姿态120 bin），并提供YOLO检测框与物体3D位置估计，降低MLLM输出精度要求。
- **公式/算法流程**：问题形式化为带语言指令的POMDP，策略π(at|L, ht)生成动作，目标最大化任务成功率。具体步骤为：视觉描述→反思+推理→语言计划→可执行计划→执行→反馈→下一轮规划。

### 3. 实验设计：数据集/场景、benchmark、对比方法
- **数据集/场景**：
  - 四个仿真环境：AI2-THOR（ALFRED、Navigation）、Habitat 2.0（Habitat）、CoppeliaSim（Manipulation）。
  - 总测试任务：1128个（EB-ALFRED 300、EB-Habitat 300、EB-Navigation 300、EB-Manipulation 228）。
- **Benchmark**：EmbodiedBench自身即为评估基准，包含每个环境的多个子集。
- **对比方法**：
  - 8个闭源MLLM：GPT-4o、GPT-4o-mini、Claude-3.5-Sonnet、Claude-3.7-Sonnet、Gemini Pro/Flash、Qwen-VL-Max。
  - 16个开源MLLM（7B-90B）：InternVL2.5/3、Qwen2-VL/2.5-VL、Llama-3.2-Vision、Gemma-3、Ovis2等。
  - 还包括“仅语言”对照（去掉视觉输入）。

### 4. 资源与算力
- 论文未明确说明训练所用算力（GPU型号、数量、训练时长等）。仅提到通过API调用闭源模型，以及使用lmdeploy和vllm本地部署开源模型。未提及分布式训练或微调细节。

### 5. 实验数量与充分性
- **实验数量**：
  - 主实验：24个模型在4个环境、6个子集上测试，报告任务成功率（表2、表3）。
  - 附加指标：子目标成功率（表6）、平均步数（表7、表8）。
  - 消融实验：
    - 语言相关消融：环境反馈、in-context示例数量（图4）。
    - 视觉相关消融：分辨率（5(a)）、检测框（5(b)）、多步图像（5(c)）、视觉ICL（5(d)）、多视角图像（图14）。
    - 另外在附录中进行了更多消融（分辨率、检测框策略、多步/多视角、视觉ICL）及错误分析（图6、图17）。
  - 错误分析：对失败轨迹按感知、推理、规划三类编码（图6）。
- **充分性与公平性**：
  - 覆盖模型多样性好（闭源+开源，不同规模）。
  - 实验设置统一（温度0，最大token 2048，图像500×500）。
  - 但存在一定偏差：仅使用模拟环境，未进行真实世界测试；部分子集数量不均衡（Manipulation的Visual子集仅36例）；未控制闭源模型API版本变化。

### 6. 论文的主要结论与发现
- **MLLM在高层次任务上表现良好，但在低层操作上严重不足**：最佳模型GPT-4o在低层操作平均成功率仅28.9%。
- **长期规划是最具挑战性的子集**：几乎所有模型在长程任务上都出现大幅性能下降。
- **视觉输入对低层任务至关重要，对高层任务影响小**：移除视觉后，导航成功率从57.7%降至17.4%，而高层任务甚至可能轻微提升。
- **视觉ICL显著提升低层操作性能**：如Claude-3.5-Sonnet提升16.7%。
- **当前MLLM难以有效利用多步或多视角图像**，反而引起混淆。
- **规划错误（尤其是缺失步骤、无效动作、不准确动作）是主要失败类型**，感知错误在低层任务中占比更高（33%）。

### 7. 优点：方法或实验设计上的亮点
- **全面性**：同时覆盖高层语义任务和底层原子动作，弥补了现有基准的空白。
- **细粒度能力评估**：设计6个能力子集，可诊断模型在常识、空间理解、视觉感知等维度的具体缺陷。
- **统一且可复现的评估框架**：明确提供代码、数据集和标准化协议。
- **多步规划策略**：减少API调用，提升效率，且与人类决策更一致。
- **丰富的消融实验**：系统研究了分辨率、检测框、多步/多视角图像、视觉ICL等因素的影响。
- **错误编码**：细分为感知、推理、规划三类12种子错误，有助于指导后续改进。

### 8. 不足与局限
- **仅在仿真环境中评估**：未涉及真实机器人部署，模拟与现实之间可能存在差距。
- **数据集规模有限**：每个子集仅36-60例，部分能力子集数据较少，可能影响统计显著性。
- **部分环境不支持所有子集**：导航缺少空间意识子集，操作缺少长程子集，导致能力评估不完整。
- **动作空间简化**：操作任务采用离散化动作，可能丢失连续控制的精度信息；导航任务假设平面移动，未考虑复杂地形。
- **闭源模型版本依赖**：API可能随时间更新，结果可能不可完全复现。
- **未深入分析模型规模与性能的关系**：虽然提到开源模型有规模趋势，但未给出具体相关性分析。
- **缺乏与VLA（视觉-语言-动作）模型（如RT-2、Octo）的直接对比**：仅评估了MLLM作为通用规划器，未对比端到端专用模型。

（完）
