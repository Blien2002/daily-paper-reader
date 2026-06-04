---
title: Learning to Plan with Personalized Preferences
title_zh: 学习根据个性化偏好进行规划
authors: "Manjie Xu, Xinyi Yang, Wei Liang, Chi Zhang, Yixin Zhu"
date: 2025-01-21
pdf: "https://openreview.net/pdf?id=r53lwSSfcI"
tags: ["query:vla"]
score: 5.0
evidence: 具身智能中的个性化规划基准
tldr: 该论文聚焦具身智能中忽略个性化偏好的问题，提出PbP基准，要求智能体从少量演示中学习并泛化个人规划偏好。实验表明所提方法能有效捕捉偏好并在新场景中调整规划策略，促进了人机协作中的个性化适应。
source: ICML-2025-Rejected-Public
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1772, \"height\": 779, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1774, \"height\": 590, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 861, \"height\": 495, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1601, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 853, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1599, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-r53lwssfci/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 849, \"height\": 367, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-r53lwssfci/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1433, \"height\": 414, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-r53lwssfci/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1390, \"height\": 371, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-r53lwssfci/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 882, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-r53lwssfci/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 928, \"height\": 210, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-r53lwssfci/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1174, \"height\": 711, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-r53lwssfci/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1488, \"height\": 1175, \"label\": \"Table\"}]"
motivation: 现有具身智能方法通常采用通用规划策略，忽视用户个人偏好。
method: 提出从少量演示隐式学习偏好的方法，并构建PbP具身基准来评估个性化规划能力。
result: 所提方法能在多样规划场景中有效泛化个性化偏好。
conclusion: 个性化偏好学习对具身智能的人机协作至关重要。
---

## Abstract
Effective integration of AI agents into daily life requires them to understand and adapt to individual human preferences, particularly in collaborative roles. Although recent studies on embodied intelligence have advanced significantly, they typically adopt generalized approaches that overlook personal **preferences in planning**. We address this limitation by developing agents that not only learn preferences from few demonstrations but also learn to adapt their planning strategies based on these preferences. Our research leverages the observation that preferences, though implicitly expressed through minimal demonstrations, can generalize across diverse planning scenarios. To systematically evaluate this hypothesis, we introduce PbP benchmark, an embodied benchmark featuring hundreds of diverse preferences spanning from atomic actions to complex sequences. Our evaluation of SOTA methods reveals that while symbol-based approaches show promise in scalability, significant challenges remain in learning to generate and execute plans that satisfy personalized preferences. We further demonstrate that incorporating learned preferences as intermediate representations in planning significantly improves the agent's ability to construct personalized plans. These findings establish preferences as a valuable abstraction layer for adaptive planning, opening new directions for research in preference-guided plan generation and execution.

---

## 论文详细总结（自动生成）

# 论文《Learning to Plan with Personalized Preferences》详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **研究动机**：当前具身智能（Embodied AI）在协作式人机交互方面取得显著进展，但大多采用通用规划策略，忽略了用户个体的个性化偏好。例如，用户要求“帮我准备一个苹果”，机器人需要知道是否清洗、是否切块、放在哪里等细节，而这些因人而异。现有方法要么依赖详尽的自然语言指令（存在歧义），要么仅针对特定任务（如物体整理）学习偏好，缺乏泛化能力。
- **核心目标**：开发能通过**少量演示**（few-shot）隐式学习用户偏好，并将偏好作为**中间表示**来指导规划（planning）的智能体，使其能够在不同场景（物体、房间布局、任务组合）中自适应地生成个性化行动序列。
- **整体含义**：将偏好提升为一种有价值的抽象层，连接高层目标与底层动作，为人机协作中的个性化适应提供新范式。

## 2. 论文提出的方法论

### 核心思想
- **两阶段框架**：
  - **阶段一（偏好学习）**：从用户演示的观察序列（egocentric视频+动作序列）中推断出偏好表示（可为隐式向量或显式文本标签）。
  - **阶段二（偏好引导规划）**：利用学得的偏好表示，在当前状态和新场景下生成符合偏好的动作序列。
- **形式化**：给定观察集 O = {(S_i, A_i, M)}，学习偏好 p = f(O; θ_f)；然后优化目标 L = Σ ℓ(g(s_i, p; θ_g), a_i)，其中 g 为规划函数。

### 关键技术细节
- **基准建设**：基于 NVIDIA Omniverse 和 OmniGibson 构建 Preference-based Planning (PbP) 基准，包含 **50 个不同场景**、**290 种偏好**、**5000 个测试实例**。
- **偏好层次结构**：分为三层：
  - **动作层（Action Level）**：75种，控制原子动作的细节（如水量、切割方式）。
  - **选项层（Option Level）**：135种，编码子任务的不同实现方式（如水果放冰箱 vs 桌上）。
  - **序列层（Sequence Level）**：80种，定义任务间的时序逻辑（如先清洗后烹饪）。
- **数据生成**：使用规则规划器（A* 路径规划、IK 抓取、OMPL 高级规划）生成演示，每个演示包含 egocentric 视频、鸟瞰地图、帧级动作标注（含 Omniverse 物体 ID）。

### 算法流程（文字说明）
1. **输入**：用户执行任务的若干演示（egocentric 视频或符号化动作序列）。
2. **偏好学习**：模型通过 in-context learning 或显式分类，从演示中提取偏好标签（如“水果放床上”）。
3. **规划生成**：模型依据当前环境描述（新场景、新物体列表）以及学得的偏好，生成顺序动作序列（如“移动到葡萄，拿起葡萄，移动到床，放下葡萄”）。
4. **评估**：使用 Levenshtein 距离度量生成序列与真实序列的差异。

## 3. 实验设计

### 数据集/场景
- 使用自建的 **PbP 基准**：基于 OmniGibson 的 50 个不同室内场景（如 Beechwood、Rs、Merom 等），涵盖多样化物体和布局。
- 层次划分：动作层、选项层、序列层各含不同数量测试点（总共 5000 个测试点，另有 15000 条原始录制视频）。

### 对比方法
- **视频输入模型**：
  - ViViT（纯视频Transformer，无LLM）
  - LLaVA-NeXT（多模态VLM，7B）
  - EILEV（基于OPT-2.7B的ego-centric VLM）
  - GPT-4V（gpt-4-turbo-2024-04-09）
- **符号输入模型**（仅处理动作序列文本）：
  - DAG-Opt（基于NOTEARS的结构因果学习）
  - Llama3-8B-Instruct
  - GPT-4-Turbo

### 实验设置
- **端到端**：直接从演示+当前状态生成动作序列，不显式获取偏好标签。
- **两阶段**：先预测偏好标签（偏好分类准确率），再基于预测标签（或真实标签）进行规划（测量Levenshtein距离）。
- **消融**：
  - 去除演示（仅用测试序列预测偏好）。
  - 改变演示数量（1、2、3、5个）。
  - 控制场景和物体不变（direct） vs 随机变化（generalization）。

## 4. 资源与算力

- **文中明确说明**：所有实验在**一台配备 8 块 NVIDIA A100 GPU 的机器**上运行。
- **未明确说明**：具体训练时长、模型微调超参数（如ViViT训练30 epoch，但未给出总时间）；LLM 推理使用保守参数（temperature=0.05, top_p=0.05）；未报告显存占用或能源消耗。

## 5. 实验数量与充分性

### 实验组数
1. **端到端 Levenshtein 距离**（表1）：6个模型 × 2个层级（选项、序列） = 12组。
2. **两阶段 Levenshtein 距离**（表1）：同样12组，加真实偏好标签6组。
3. **偏好预测准确率**（表2）：包括 few-shot 和 ablative（无演示）共 6模型 × 2层级 × 2条件 = 24组。
4. **泛化测试**（表3）：4个模型在 direct 和 generalization 条件下预测准确率，共 4×4=16组。
5. **演示数量消融**（图7）：展示了5种模型（GPT-4、Llama3、EILEV等）在1/2/3/5个演示下的偏好预测准确率和Levenshtein距离变化。
6. **案例分析**（附录表A3）：4个模型在某个具体场景（Beechwood）的完整动作序列对比。

### 充分性评价
- **充分**：涵盖了不同输入模态（视频 vs 符号）、不同偏好层级（动作/选项/序列）、多种基线（纯视觉、LLM、结构学习）、消融（演示数量、场景不变性）。
- **公平客观**：视频模型使用相同的egocentric视频规格（分辨率512×512，8fps）；符号模型使用相同的动作序列文本提示；LLM推理参数一致；评价指标采用Levenshtein距离（无需人工评分）。
- **不足**：所有实验基于仿真环境（合成数据），缺乏真实世界验证；仅报告了单一指标（Levenshtein距离），未讨论任务成功率或执行时间等；消融研究仅对部分模型进行（如泛化实验只测试了4个最强模型）。

## 6. 主要结论与发现

1. **端到端方法在偏好学习上基本失败**：生成的序列与真实序列的Levenshtein距离接近平均长度，表明模型仅学到孤立动作而非隐含偏好。
2. **两阶段方法显著提升性能**：显式引入偏好标签作为中间表示后，规划质量大幅提升，尤其符号型模型（GPT-4）在选项层几乎达到零距离。
3. **符号模型优于视觉模型**：GPT-4符号版在偏好预测准确率（86.27% 选项层）和规划精度上大幅领先视觉模型（GPT-4V 48.48%）。
4. **视觉模型泛化性差**：当场景物体改变时，视觉模型准确率下降明显（如LLaVA选项层从33.25%→36.87%但序列层从33.12%→24.85%），而符号模型几乎不受影响。
5. **演示数量影响**：增加演示数量通常提升性能，但过多（如5个）有时反而有轻微下降。
6. **偏好作为抽象层有效**：分离偏好学习与规划分解了任务难度，且偏好能够跨场景、跨物体泛化。

## 7. 优点

- **基准新颖且系统**：首个覆盖多层级（动作/选项/序列）、大量偏好（290种）的具身规划基准，基于高质量仿真（NVIDIA Omniverse）。
- **框架简洁有效**：两阶段范式明确分离“学偏好”与“用偏好”的挑战，便于诊断模型瓶颈。
- **实验设计全面**：对比了视频和符号输入、端到端和两阶段、有无演示、不同演示数量等，结论可靠。
- **案例分析直观**：附录中给出了具体动作序列对比，易于理解模型行为差异。
- **注重公平性**：统一了视频规格、LLM参数、提示模板，减少了额外变量干扰。
- **开放早期沟通**：提供了完整的数据卡片（附录A），包含动机、组成、收集过程等，透明度高。

## 8. 不足与局限

- **完全基于合成数据**：尽管Omniverse渲染质量高，但无法模拟真实光照、物体物理、人类肌肉动作等复杂性，存在 sim-to-real gap。
- **偏好标签人工定义**：290种偏好未必能覆盖真实世界的多样性，且标注可能粗糙；未测试偏好间是否存在冲突或连续变化。
- **泛化实验不够深入**：只测试了场景/物体变化，未测试用户身份变化、噪声演示、偏好迁移等更复杂的泛化场景。
- **缺乏真实用户交互**：所有演示由规则生成器产生，没有人类实际行为数据，可能隐含系统偏差（如动作平滑度、一致性）。
- **算力细节不完整**：未报告训练总时长、模型参数量、推理延迟等重要指标，对可复现性和实用性评估不利。
- **评价指标单一**：仅使用 Levenshtein 距离，未考虑任务完成率、安全性、用户满意度等维度。
- **视觉模型可能过拟合**：论文自身指出模型倾向于记住视觉上下文而非真正理解偏好，这一危险未得到充分缓解策略讨论。
- **未探索连续或隐式偏好表示**：框架主要使用显式分类标签，未深入分析连续向量表示的效果与可比性。

（完）
