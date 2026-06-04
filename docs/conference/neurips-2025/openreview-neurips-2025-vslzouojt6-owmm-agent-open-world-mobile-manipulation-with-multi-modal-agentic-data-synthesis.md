---
title: "OWMM-Agent: Open World Mobile Manipulation With Multi-modal Agentic Data Synthesis"
title_zh: OWMM-Agent：基于多模态智能体数据合成的开放世界移动操纵
authors: "Junting Chen, Haotian Liang, Lingxiao Du, Weiyun Wang, Mengkang Hu, Yao Mu, Wenhai Wang, Jifeng Dai, Ping Luo, Wenqi Shao, Lin Shao"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=vSLzoUoJt6"
tags: ["query:vla"]
score: 8.0
evidence: 多模态智能体架构将大语言模型与机器人控制集成于开放世界移动操纵
tldr: 开放世界移动操纵需要泛化到开放式指令和环境，同时集成高层决策与低层控制。本文提出OWMM-Agent，一种多模态智能体架构，维护多视角场景帧和智能体状态，通过函数调用控制机器人。针对域迁移的幻觉问题，引入多模态代理数据合成增强性能。实验表明该方法在未见过的任务和环境中表现优异，展现了LLM在复杂操纵中的潜力。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1243, \"height\": 687, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1364, \"height\": 804, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1280, \"height\": 589, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1405, \"height\": 418, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 829, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1399, \"height\": 368, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1411, \"height\": 1655, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vslzouojt6/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1433, \"height\": 2047, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1455, \"height\": 885, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1426, \"height\": 369, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1459, \"height\": 413, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1405, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1455, \"height\": 797, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1535, \"height\": 392, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1463, \"height\": 377, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1508, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 906, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vslzouojt6/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 907, \"height\": 210, \"label\": \"Table\"}]"
motivation: 开放世界移动操纵面临指令和环境泛化难、高层决策与低层控制集成复杂的问题。
method: 设计多模态智能体架构，通过维护多视角场景状态和函数调用来实现端到端控制。
result: 在多个开放世界场景下实现高成功率，证明架构的有效性和泛化能力。
conclusion: OWMM-Agent为集成大语言模型的复杂机器人系统提供了有效范式。
---

## Abstract
The rapid progress of navigation, manipulation, and vision models has made mobile manipulators capable in many specialized tasks. 
However, the open-world mobile manipulation (OWMM) task remains a challenge due to the need for generalization to open-ended instructions and environments, as well as the systematic complexity to integrate high-level decision making with low-level robot control based on both global scene understanding and current agent state. To address this complexity, we propose a novel multi-modal agent architecture that maintains multi-view scene frames and agent states for decision-making and controls the robot by function calling.
A second challenge is the hallucination from domain shift. To enhance the agent performance, we further introduce an agentic data synthesis pipeline for the OWMM task to adapt the VLM model to our task domain with instruction fine-tuning. We highlight our fine-tuned OWMM-VLM as the first dedicated foundation model for mobile manipulators with global scene understanding, robot state tracking, and multi-modal action generation in a unified model. Through experiments, we demonstrate that our model achieves SOTA performance compared to other foundation models including GPT-4o and strong zero-shot generalization in real world.
The project page is at https://hhyhrhy.github.io/owmm-agent-project.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义

- **研究动机**：开放世界移动操纵（OWMM）要求机器人能理解开放式自然语言指令，并在未见过的非结构化环境中执行任务。现有方法依赖2D语义地图或3D语义场，受限于嵌入模型能力，难以处理复杂组合指令，且需要耗时的3D重建。
- **核心挑战**：
  - 全局场景理解与智能体状态跟踪的集成困难。
  - 预训练VLM存在域迁移导致的幻觉问题（如物体定位错误、多图像幻觉、长时序推理不足）。
- **整体含义**：提出一种统一的VLM智能体架构，通过多轮、多图像、多模态推理，将高层决策与低层坐标控制桥接，实现端到端的开放世界移动操纵。

## 2. 论文提出的方法论

- **核心思想**：不需要详细的几何环境表示，利用VLM的视觉语言基础能力，通过2D到3D反投影将推理结果转化为坐标控制。将OWMM任务建模为多轮、多图像、多模态的推理问题。
- **关键技术细节**：
  1. **多模态智能体架构（OWMM-Agent）**：
     - 输入：自然语言指令、预建图阶段的相机位姿图及其RGB图像、当前单目相机RGB-D图像。
     - 输出：高层动作（类型+位置）和智能体状态历史，由路径规划器（导航）和运动规划器（操作）转化为低层动作。
     - 动作类型：Posed image retrieval（场景图像检索）、Navigate to point、Pick、Place。
  2. **OWMM-VLM模型**：
     - 基于InternVL-2.5预训练模型，冻结ViT，训练MLP和LLM。
     - 设计结构化Chain-of-Thought（CoT）推理：任务理解→感知与定位→动作决策输出→历史总结。这有助于避免死循环和幻觉。
  3. **智能体数据合成流水线**：
     - 阶段1：使用PDDL生成符号任务计划。
     - 阶段2：在Habitat模拟器中执行并记录轨迹数据。
     - 阶段3：关键帧选择与过滤（导航时目标可见、操作时可触及）。
     - 阶段4：基于模板生成CoT标注，并用GPT-4o mini改写以增加语言多样性。
- **公式说明**：无公式，但定义了agent策略函数：at = Fagent(L, G, I, Ict, Dct, xt)，以及VLM的高层动作输出：At, Ht = Fvlm(L, G, I, Ict, Ht-1)，再经过规划器得到低层动作：at = At(xt, Dct)。

## 3. 实验设计

- **数据集与场景**：
  - 使用Habitat Synthetic Scenes Dataset (HSSD)的143个场景，结合YCB Objects和Google Scanned Objects（157个操作物体，1471个容器）。
  - 训练集：113个场景，137个物体；测试集：30个场景，20个未见物体。
  - 共生成21,046个有效episode，约572K标注，分为Pick (64.7K)、Place (68.9K)、导航 (59.6K)、场景搜索 (378.8K)。
- **基准测试**：单步评估（自我中心决策、图像检索、能力定位）和回合评估（完整任务成功率）。
- **对比方法**：
  - 通用VLM：GPT-4o、InternVL-2.5-8B。
  - 模块化方法：GPT-4o+PIVOT、GPT-4o+RoboPoint。
  - 单图像能力定位基线：RoboPoint、PIVOT的单图像版本。

## 4. 资源与算力

- 明确说明：
  - OWMM-VLM-8B：8×NVIDIA A100 GPU，训练约7小时（1个epoch）。
  - OWMM-VLM-38B：24×NVIDIA A100 GPU，训练约18小时（1个epoch）。
  - 测试时：8B在单A100-40G上运行，38B在4×A100-40G上并行推理。

## 5. 实验数量与充分性

- **实验组数**：
  - 单步评估（Table 2）：对比5种方法在5个指标上的性能。
  - 回合评估（Table 3）：两种阈值设置下，对比4种方法，并记录“死循环”次数。
  - 真实世界评估（Table 4）：10个测试样本，对比3种方法。
  - 数据多样性消融（Table 6）：不同数据量（0k/15k/45k/76k/152k）和不同多样性组合（场景/物体比例）。
  - 模型消融（Table 9）：接地格式、推理摘要去除、Beam search。
  - 计算效率分析（Table 10-11）：不同帧数下的时间和内存。
  - 失败模式分析（Appendix H）：100个失败episode的4类错误统计。
- **充分性评价**：实验覆盖模拟和真实场景，包含消融、数据规模、多样性、计算效率、失败分析，设计系统而全面。对比方法选择合理（通用VLM和专用能力模型），评估指标涵盖决策、检索、接地等多个维度，且设置严格/宽松阈值。整体实验充分、客观、公平。

## 6. 论文的主要结论与发现

- OWMM-VLM-38B在单步和回合评估中全面超越GPT-4o、InternVL-2.5等基线，实现SOTA性能。
- 在回合任务中，GPT-4o+PIVOT/RoboPoint出现大量死循环（195/308），而OWMM-Agent零死循环。
- 真实世界零样本泛化能力强（38B单步成功率90%）。
- 数据规模对性能提升显著，但边际收益递减；物体/场景多样性影响较小，表明模型能从足够的数据量中有效学习自我中心空间智能。
- 推理和摘要组件对保持任务连续性至关重要；Bounding box接地格式优于直接坐标输出。

## 7. 优点

- **方法创新**：将传统依赖3D重建的OWMM简化为基于2D图像的VLM推理，结合CoT和状态跟踪，避免死循环。
- **数据合成流水线**：全自动生成大规模高质量训练数据（572K），包含结构化的CoT标注，显著降低人工成本。
- **统一模型**：OWMM-VLM是首个专为移动操纵设计的统一基础模型，同时处理场景理解、状态跟踪和动作生成。
- **实验严谨**：包含模拟和真实世界的多维度评估，提供详尽的消融、数据规模、计算效率分析，并公开代码与数据。

## 8. 不足与局限

- **预建图依赖**：需要预先建立相机位姿图和2D占用地图，无法在完全未知环境中在线建图。
- **复杂操纵能力有限**：当前仅支持吸盘末端执行器，对灵巧手等复杂夹爪场景不适用。
- **跨本体泛化**：模型学习了特定机器人（Fetch）的运动学先验，迁移到不同机械臂时可能失败。
- **帧选择未自动化**：真实世界测试中，任务相关帧需要手动选取，未实现自主在线帧选择。
- **长程任务瓶颈**：回合评估中后期操作（Pick/Place）成功率低（38.56%），表明操作能力是当前主要短板，且错误会累积。

（完）
