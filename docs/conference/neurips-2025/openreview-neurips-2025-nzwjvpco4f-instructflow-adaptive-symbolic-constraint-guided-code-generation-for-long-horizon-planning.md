---
title: "InstructFlow: Adaptive Symbolic Constraint-Guided Code Generation for Long-Horizon Planning"
title_zh: InstructFlow：自适应符号约束引导的长期规划代码生成
authors: "Haotian Chi, Zeyu Feng, Yueming Lyu, Chengqi Zheng, Linbo Luo, Yew-Soon Ong, Ivor Tsang, Hechang Chen, Yi Chang, Haiyan Yin"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=nzwjvpCO4F"
tags: ["query:vla"]
score: 7.0
evidence: 基于大语言模型的代码生成用于机器人操作规划
tldr: InstructFlow针对机器人操作中长期规划中任务分解和约束满足困难的问题，提出多智能体框架，利用大语言模型构建层次化指令图分解目标，并生成满足空间、时间、物理约束的可执行代码。该框架支持自适应故障恢复，实验显示在复杂操作任务中成功率显著高于现有语言模型规划器。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
motivation: 语言模型规划器在长期操作任务中分解能力差且难以满足约束。
method: 建立符号驱动反馈流，通过层次指令图分解并用LLM生成约束代码。
result: 显著提高复杂操作任务的成功率并实现故障恢复。
conclusion: 符号约束和多智能体协作能有效提升LLM操作规划能力。
---

## Abstract
Long-horizon planning in robotic manipulation tasks requires translating underspecified, symbolic goals into executable control programs satisfying spatial, temporal, and physical constraints. However, language model-based planners often struggle with long-horizon task decomposition, robust constraint satisfaction, and adaptive failure recovery. We introduce InstructFlow, a multi-agent framework that establishes a symbolic, feedback-driven flow of information for code generation in robotic manipulation tasks. InstructFlow employs a InstructFlow Planner to construct and traverse a hierarchical instruction graph that decomposes goals into semantically meaningful subtasks, while a Code Generator generates executable code snippets conditioned on this graph. Crucially, when execution failures occur, a Constraint Generator analyzes feedback and induces symbolic constraints, which are propagated back into the instruction graph to guide targeted code refinement without regenerating from scratch. This dynamic, graph-guided flow enables structured, interpretable, and failure-resilient planning, significantly improving task success rates and robustness across diverse manipulation benchmarks, especially in constraint-sensitive and long-horizon scenarios.

---

## 论文详细总结（自动生成）

# InstructFlow 论文中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

论文聚焦于机器人操作中的**长期规划（long-horizon planning）**问题。这类任务需要将模糊的符号目标（如“把绿色方块放进绿色碗里”）转化为可执行的控制程序，且必须满足空间、时间、物理等多重约束。现有的基于大语言模型（LLM）的规划器虽然能够生成代码，但在以下方面存在根本性缺陷：

- **任务分解能力差**：难以将长期任务正确拆分为子步骤；
- **约束满足不鲁棒**：常生成语法正确但物理不可行的代码；
- **故障恢复能力弱**：当执行失败时，只能盲目重试或整体重新生成，缺乏结构化推理和针对性修复。

作者指出，其根本原因在于自然语言本身具有模糊性，难以物理地落地。现有方法（如PRoC3S）虽然引入了反馈驱动，但仅停留在表面失败响应层面，无法挖掘深层因果结构。为此，论文提出**InstructFlow**，建立一个**符号化、反馈驱动的信息流**，实现自适应任务规划与代码生成。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
InstructFlow是一个**多智能体（multi-agent）框架**，包含三个协作智能体：**InstructFlow Planner**、**Code Generator**和**Constraint Generator**。其核心在于构建一个**层次化指令图（hierarchical instruction graph）**作为任务分解与推理的骨架，并通过**符号约束归纳（symbolic constraint induction）**将执行失败抽象为可复用的逻辑约束，然后沿指令图向上传播，指导局部代码修复，避免全量重新生成。

### 关键技术细节

#### (1) 指令图（Instruction Graph）
- 节点分为两类：
  - **规划节点（planning nodes）**：可直接翻译为机器人可执行代码的子目标，如pick、place。
  - **推理节点（reasoning nodes）**：执行符号变换，提供任务相关抽象信息，如空间关系推断、目标选择、参数范围调整等。论文定义了五种推理模块：`T_spatial`、`T_density`、`T_select`、`T_plan`、`T_param`。
- 节点间边表示符号或时序依赖关系。
- 初始化时图仅含规划节点；当失败发生时，Planner在受影响的子目标前动态插入推理节点，形成符号堆栈。

#### (2) 符号约束归纳（Symbolic Constraint Induction）
- **四阶段诊断流程**：
  1. 失败相关实体检索：从失败trace和已执行代码中识别相关变量；
  2. 代码级推理：实例化变量并推理符号谓词；
  3. 诊断推理：计算几何/物理诊断指标（如碰撞距离、路径通畅性、放置稳定性）；
  4. 符号约束归纳：将诊断结果抽象为声明式符号约束。
- 约束形式化为合取式，包含关系约束（如`ClearOf(gripper, object)`）和物理约束（如`Dist ≥ δ_safe`）。
- 约束作为结构先验指导图更新和提示重构。

#### (3) 反馈驱动的图更新与代码生成
- 每个回合t，Planner根据任务目标、当前状态和约束生成更新后的指令图 `G_t`。
- Code Generator沿图结构组合提示，为每个规划节点生成代码段。只有受约束影响的子目标会被重新生成，无关部分保持不变。

#### (4) "Flow"的层次
- **图层面的符号流**：从推理节点流向规划节点。
- **提示层面的信息流**：从任务目标，经符号推理和反馈，流入结构化、自适应的提示。

### 公式与算法流程（文字说明）
- 形式化问题：给定任务描述和初始状态，LLM生成两个函数：`get_plan`（动作序列）和`get_domain`（参数范围）。
- 执行可行性由连续约束满足模块（CCSP）评估（运动学、碰撞、抓取、放置四类检查）。
- 约束生成器输出形如 `ϕ := ∧ c ∈ C (E,R,F,B) c` 的符号约束，其中`c`代表关系或物理条件。

## 3. 实验设计：数据集/场景、benchmark、对比方法

### 数据集/场景
所有实验在**Ravens仿真环境**中进行，使用**6-DOF UR5机械臂**和**Robotiq 2F-85夹爪**，物理引擎为PyBullet。包含三个模拟领域：
1. **Drawing（绘图）**：用draw_line原语在平面上绘制星形、箭头、字母等，并避开随机放置的障碍物。
2. **Arrange-Blocks（方块排列）**：堆叠和排列彩色方块与碗，形成金字塔、直线、包围等结构，测试稳定性、空间精度和遮挡处理。
3. **Arrange-YCB（YCB物体排列）**：操作YCB数据集中的复杂物体（如香蕉、肉罐）进行打包和堆叠，考验不规则几何下的抓取和放置。

### Benchmark
评估指标为**任务成功率（task success rate）**，并遵循PRoC3S[3]的评估协议（每个任务随机种子10次，最大采样数1000次，反馈迭代上限5次）。作者指出PRoC3S原始协议存在缺陷：某些物理上可行但语义上未满足目标的计划被错误归类为成功。因此引入了**VLM（GPT-4o）语义检查**作为补充评估层，确保真实目标达成。

### 对比方法
- **PRoC3S**：两阶段LLM规划器，分离计划生成与约束满足，带反馈。
- **LLM³**：LLM直接输出带连续参数的技能序列。
- **Code-as-Policies (CaP)**：用LLM合成完整Python程序，包含动作序列和连续参数。

所有方法均通过**OpenAI的GPT-4o**查询。

## 4. 资源与算力

论文未明确说明训练阶段使用的GPU型号、数量或训练时长。实验部分提到：
- 仿真在**CPU**上运行，配置**32GB RAM**。
- 所有基线实现集成到统一评估框架中。
- 每个任务用10个随机种子，最大采样数1000（Drawing任务为10000），反馈迭代最多5次。
- 未提及LLM推理的硬件（推断使用OpenAI API，不涉及本地计算资源）。

算力信息不完整，无法评估整体计算成本。

## 5. 实验数量与充分性

### 实验数量
- **主实验**：三个领域共10个子任务（Drawing: 3个，Arrange-Blocks: 5个，Arrange-YCB: 2个），每个均报告成功率。
- **消融实验**：对比完整InstructFlow与去掉Planner Agent、去掉Constraint Agent的变体。
- **鲁棒性实验**：
  - 感知噪声：注入高斯噪声（σ=0.005/0.01/0.02）测试6个任务。
  - 反馈噪声：测试错误对象引用和不完整trace两种情形。
- **效率分析**：对比PRoC3S的反馈查询次数和端到端延迟。
- **VLM辅助实验**：加入视觉输入的额外实验。

### 充分性与公平性
- **充分**：覆盖多个领域，包含组合消融和噪声测试，实验设计较全面。
- **公平**：统一采用GPT-4o、相同仿真环境、遵循PRoC3S协议并修正其评估缺陷（引入VLM验证），保证了对比的公平性。
- **局限**：仅限仿真，无真实机器人实验；每个任务10个种子，统计显著性未用置信区间展示（虽然后续效率表格带有标准差）。

## 6. 论文的主要结论与发现

1. **性能提升显著**：在Drawing（20-40%）、方块排列（20-40%）和YCB操作任务上，InstructFlow的成功率超越所有基线20-40个百分点。
2. **符号约束归纳有效**：消融实验表明，去掉Planner或Constraint Agent会导致成功率大幅下降（最高50%），证明结构化分解和反馈驱动修复缺一不可。
3. **鲁棒性强**：在感知噪声（σ=0.02）下平均成功率仅下降18.3%；在错误/不完全反馈下仅下降11-16%，显示出对现实不确定性的适应能力。
4. **效率更高**：相比PRoC3S，反馈查询次数减少约37%，端到端延迟降低约4.7%。

## 7. 优点：方法或实验设计上的亮点

- **结构化任务分解**：指令图将高层目标层次化分解为符号子目标，并为每个子目标注入推理节点，实现粗到细的规划，避免整体黑箱生成。
- **符号约束驱动的精准修复**：将失败抽象为可复用的逻辑谓词，仅局部修改受影响的子目标及其参数范围，避免了全量重新生成，提升了修复效率和可解释性。
- **多智能体协作**：三个智能体各司其职（规划、代码生成、约束生成），形成清晰的信息流，模块化设计便于维护和扩展。
- **实验协议修正**：发现并修复了PRoC3S评估中“语义成功判定缺失”的问题，引入VLM检查，使比较更加真实和公平。
- **鲁棒性测试**：主动模拟感知和反馈噪声，评估系统在非理想条件下的表现，为真实世界部署提供参考。

## 8. 不足与局限

- **缺乏真实机器人实验**：所有实验均在仿真中进行，尽管模拟了噪声，但真实环境的意外因素（如摩擦、形变、控制延迟）无法完全覆盖。
- **算力资源未透明**：未报告LLM推理的计算开销（API调用次数、延迟细节），影响了可复制性和成本评估。
- **统计严谨性不足**：主实验仅报告平均值，未提供置信区间或误差条，消融实验也未进行统计显著性检验。
- **任务规模有限**：评价的任务最多涉及几个物体，未测试大规模杂乱场景或更复杂的操作（如插入、装配）。
- **依赖LLM能力**：推理质量和约束归纳质量高度依赖底层LLM（GPT-4o），若模型能力不足或出现幻觉，框架可能退化。
- **符号约束人工定义依赖**：虽然约束是由LLM自动归纳的，但物理谓词和阈值的定义空间仍需要人工设计（如`δ_safe`），可能限制泛化到全新物理域。

（完）
