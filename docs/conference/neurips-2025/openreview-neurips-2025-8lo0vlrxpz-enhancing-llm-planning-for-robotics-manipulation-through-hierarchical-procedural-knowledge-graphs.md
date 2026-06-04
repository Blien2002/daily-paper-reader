---
title: Enhancing LLM Planning for Robotics Manipulation through Hierarchical Procedural Knowledge Graphs
title_zh: 通过层次化程序知识图谱增强机器人操纵中的LLM规划
authors: "Jiacong Zhou, Jiaxu Miao, Xianyun Wang, Jun Yu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=8LO0vLRXpz"
tags: ["query:vla"]
score: 7.0
evidence: 利用知识图谱增强LLM的机器人操纵规划
tldr: 大型语言模型在机器人操纵规划中表现优秀，但难以处理复杂任务且模型规模过大。本文提出层次化程序知识图谱（HP-KG），通过结构化先验知识增强LLM的规划能力，同时显著降低对LLM规模的需求。实验证明在复杂操纵任务上效果显著提升。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1303, \"height\": 478, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 646, \"height\": 353, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1431, \"height\": 633, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 599, \"height\": 442, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1418, \"height\": 535, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1433, \"height\": 484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1367, \"height\": 674, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 620, \"height\": 465, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1437, \"height\": 340, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 746, \"height\": 298, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1358, \"height\": 733, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1333, \"height\": 641, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8lo0vlrxpz/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1313, \"height\": 716, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1442, \"height\": 206, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 541, \"height\": 259, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 848, \"height\": 351, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 648, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 663, \"height\": 181, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1164, \"height\": 249, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1445, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1387, \"height\": 285, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1310, \"height\": 182, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1221, \"height\": 203, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 801, \"height\": 196, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8lo0vlrxpz/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1600, \"height\": 654, \"label\": \"Table\"}]"
motivation: 现有LLM驱动规划难以处理复杂操纵任务且模型过大。
method: 构建层次化程序知识图谱来增强LLM的规划能力，降低模型规模需求。
result: 在复杂操纵任务上提升了规划准确性和效率。
conclusion: HP-KG有效促进了LLM在机器人操纵中的实用化。
---

## Abstract
Large Language Models (LLMs) have shown the promising planning capabilities for robotic manipulation, which advances the development of embodied intelligence significantly. However, existing LLM-driven robotic manipulation approaches excel at simple pick-and-place tasks but are insufficient for complex manipulation tasks due to inaccurate procedural knowledge. Besides, for embodied intelligence, equipping a large scale LLM is energy-consuming and inefficient, which affects its real-world application.
To address the above problems, we propose Hierarchical Procedural Knowledge Graphs (\textbf{HP-KG}) to enhance LLMs for complex robotic planning while significantly reducing the demand for LLM scale in robotic manipulation. 
Considering that the complex real-world tasks require multiple steps, and each step is composed of robotic-understandable atomic actions, we design a hierarchical knowledge graph structure to model the relationships between tasks, steps, and actions. This design bridges the gap between human instructions and robotic manipulation actions. To construct HP-KG, we develop an automatic knowledge graph construction framework powered by LLM-based multi-agents, which eliminates costly manual efforts while maintaining high-quality graph structures. 
The resulting HP-KG encompasses over 40k activity steps across more than 6k household tasks, spanning diverse everyday scenarios. Extensive experiments demonstrate that small scale LLMs (7B) enhanced by our HP-KG significantly improve the planning capabilities, which are stronger than 72B LLMs only. Encouragingly, our approach remains effective on the most powerful GPT-4o model.

---

## 论文详细总结（自动生成）

# 基于层次化程序知识图谱增强LLM机器人操纵规划能力——论文核心总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：大型语言模型（LLMs）在机器人操纵规划中展现出强大潜力，但现有方法主要擅长简单取放任务，在复杂操纵任务中因缺乏精确的程序常识而生成不切实际或逻辑不一致的步骤（如忽略物理约束或必要的预备动作）。同时，为获得足够规划能力，LLM规划器往往需要超大模型（如PaLM-E 562B参数），这在能量和效率上对实体机器人不可行。
- **核心问题**：如何在不依赖超级LLM规模的前提下，提升LLM对复杂机器人操纵任务的规划能力，使其具备准确的程序性常识。
- **论文目标**：构建一个可自动生成的大规模层次化程序知识图谱（HP-KG），作为外部知识增强LLM规划，显著降低对LLM参数规模的依赖，同时提升规划准确性和鲁棒性。

## 2. 论文提出的方法论

- **核心思想**：利用层次化知识图谱组织程序知识，将复杂人类指令逐步分解为机器人可理解的原子动作。通过检索相关子图作为上下文，注入LLM，使其能依赖结构化先验知识进行规划。
- **关键技术细节**：
  - **HP-KG结构设计**：分为三层——**任务（Task）**、**步骤（Step）**、**动作（Action）**。任务通过HasStep边链接步骤，步骤通过HasAction边链接动作；步骤间/动作间通过NextStep/NextAction边表示时序关系。每个节点附带名称、描述和Tips属性，包含安全提示。
  - **自动构造框架**：包含四个阶段：
    1. 数据源清理与处理（WikiHow + BEHAVIOR-1K，过滤家务类条目，去重）。
    2. 程序生成与完成（用LLM提取任务-步骤-属性，再补充原子动作）。
    3. 规则引导的迭代验证与精炼（Verifier使用多个规则检查模型和嵌入模型评估，Refiner根据反馈修改，迭代至分数达标）。
    4. 层次聚类与摘要（Summary Agent按层次对相似程序聚类和合并，减少冗余）。
  - **检索增强规划算法**：对输入指令用LLM提取查询，编码后检索top-k1相似节点；进行K-hop广度优先扩展，过滤目标层级节点，重排序选出top-k2；提取关联子图转换为文本上下文，供LLM规划使用。
- **公式/算法流程**（文字说明）：
  - 节点嵌入：`z_n = Encoder(x_n)`。
  - 查询嵌入：`z_q = Encoder(x_q)`。
  - 初始检索：`V_k1 = TopK_{n in V} sim(z_q, z_n)`。
  - 扩展：`V'_k1 = union_{n in V_k1} {n' | dist(n', n) ≤ K}`。
  - 过滤层级：`V_target = {n in V'_k1 | Level(n) = L_target}`。
  - 重排序选top-k2：`V_k2 = TopK_{n in V_target} sim(z_q, z_n)`。
  - 最后将每个节点及其子图转换成文本，拼接后作为LLM上下文。

## 3. 实验设计

- **数据集/场景**：
  - **RLBench**：6个复杂操纵任务（开酒瓶、取秤、取伞、滑方块、玩叠叠乐等），每任务20次试验。
  - **Blocks Arrange**：5个方框排列任务（如堆叠成三座塔）。
  - **ActPlan-1K**：多模态家务规划基准，共237个实例，输入任务描述+环境图像，要求生成步骤规划。
  - **VLABench**：含常识、复杂、M&T、物理规则四个类别，每类5-8任务，每任务50次试验。
  - **Kitchen World**：长时域规划任务（做鸡汤），使用默认TAMP方法执行子目标。
- **基准方法**：
  - RLBench：VoxPoser、MA（Manipulate-Anything）、RVT（动作执行器）；与Chain of Thought (COT) 比较。
  - Blocks Arrange：SayCan、GPT-4o w/ COT。
  - ActPlan-1K：多种MLLM（GPT-4o、Gemini-2.0-Flash、Qwen2-VL-7B/72B、InternVL-2.5-26B、Llama-3.2-90B-Vision-Instruct）有无HP-KG增强对比。
  - VLABench：Intern3-VL-8B。
- **评价指标**：成功率（SR）、最长公共子序列（LCS）、混合LCS（Mix LCS）。

## 4. 资源与算力

- 论文明确提到：实验使用NVIDIA A6000 GPU（48GB VRAM），CUDA Toolkit 11.8。7B和72B模型部署使用vLLM推理框架，72B采用AWQ量化以适配显存。训练/推理时间：各模型的inference time在实验中被记录（如Qwen2-VL-7B约0.44s，72B约1.28s）。未提及知识图谱构造的具体训练算力消耗（但框架使用LLM API，有效计算开销在论文附录中有部分量化）。

## 5. 实验数量与充分性

- **实验数量**：核心实验包含6张表（表1-6）及多个附录表格（表7-13），涵盖：
  - RLBench：2组基线比较（表1、表2）+ 开源模型比较（表10）。
  - Blocks Arrange：1组（表3）。
  - ActPlan-1K：主表（表4）+ 附加模型（表8）+ 消融实验（表5、6、9）。
  - VLABench：1组（表12）。
  - Kitchen World：1组（表13）。
  - 图4、8含效率对比；图5、9为定性案例。
- **消融实验**：
  - 图结构消融（表5）：对比无结构文档、粗粒度图、层次图。
  - 构造框架阶段消融（表6、9）：对比有无初步生成、迭代验证、摘要合并。
- **充分性**：实验覆盖多个领域（操作、规划、长时域、常识推理），模型规模从7B到GPT-4o，基线包括经典方法和SoTA，总体充分。但所有任务均限于实验室仿真环境（未提及真实机器人），且RLBench任务数较少。

## 6. 论文的主要结论与发现

- 小规模LLM（7B）增强HP-KG后，规划能力超越无增强的72B模型，且推理时间减少约50%（图4）。
- 在所有测试的模型（7B/72B/闭源）上，HP-KG均带来显著提升：Qwen2-VL-7B提升17.64%，Qwen2-VL-72B提升11.74%，GPT-4o提升3.99%。
- 在机器人操纵任务（RLBench）上，HP-KG提升VoxPoser成功率10%，提升MA成功率11%；在Benchmarks Arrange上也优于SayCan和COT。
- 在长时域规划（Kitchen World）中，HP-KG使GPT-4o的任务完成百分比从77.4%提升至86.9%。
- 层次化图结构和多阶段自动构造框架均被验证有效。

## 7. 优点

- **结构设计创新**：层次化任务-步骤-动作结构直接对齐人类指令与机器人原子动作，填补了常识鸿沟。
- **自动化构建**：无需人工标注，利用LLM多智能体自动抽取、验证、去重和合并，可扩展至其他领域。
- **即插即用**：HP-KG作为外部知识，可无缝集成多种LLM/VLM规划方法，显著提升性能。
- **成本效益**：降低对超大模型依赖，推理更快，适合实际机器人部署。

## 8. 不足与局限

- **领域限制**：HP-KG当前仅覆盖家务活动（WikiHow+BEHAVIOR-1K），缺乏工业、医疗等通用场景泛化性。
- **实验覆盖**：RLBench仅测试6个任务，部分任务未提升（如Play_jenga始终0%），可能因底层操纵能力瓶颈；未在真实机器人上验证。
- **潜在偏差**：知识图谱质量受限于LLM生成准确性，虽经迭代验证但仍可能包含错误或过度泛化。构造时使用GPT-4o作为主要LLM，成本较高。
- **上下文长度敏感**：小模型在Top-K增大时性能下降（图4），说明长上下文理解能力有限。
- **可重复性**：承诺公开代码和数据，但目前为匿名链接，需验证最终可用性。

（完）
