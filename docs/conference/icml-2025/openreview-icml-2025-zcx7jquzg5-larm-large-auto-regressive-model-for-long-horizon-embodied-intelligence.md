---
title: "LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence"
title_zh: LARM：用于长时程具身智能的大自回归模型
authors: "Zhuoling Li, Xiaogang Xu, Zhenhua Xu, Ser-Nam Lim, Hengshuang Zhao"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=zcx7jqUZg5"
tags: ["query:vla"]
score: 10.0
evidence: 大自回归模型直接输出动作用于具身智能
tldr: 现有具身代理要么是效率高但任务少的RL，要么是参数超千亿但通用性强的LLM。本文提出LARM，基于轻量级LLM直接输出动作而非文本，并引入裁判强化学习解决长时程探索中反馈消失问题。实验表明，LARM在多种长时程具身任务中实现了高效率和强泛化性，为集成LLM与机器人动作空间提供了高效新范式。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-zcx7jquzg5/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1762, \"height\": 772, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-zcx7jquzg5/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1760, \"height\": 904, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-zcx7jquzg5/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1762, \"height\": 1023, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-zcx7jquzg5/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1505, \"height\": 598, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-zcx7jquzg5/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 856, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-zcx7jquzg5/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 771, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-zcx7jquzg5/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 814, \"height\": 187, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-zcx7jquzg5/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 821, \"height\": 246, \"label\": \"Table\"}]"
motivation: RL代理任务少，大LLM代理资源消耗巨大。
method: 构建轻量级大自回归模型直接输出动作，并设计裁判强化学习。
result: 在长时程具身任务中实现高效且泛化。
conclusion: 轻量级LLM直接输出动作结合裁判RL可兼顾效率和泛化。
---

## Abstract
Recent embodied agents are primarily built based on reinforcement learning (RL) or large language models (LLMs). Among them, RL agents are efficient for deployment but only perform very few tasks. By contrast, giant LLM agents (often more than 1000B parameters) present strong generalization while demanding enormous computing resources. In this work, we combine their advantages while avoiding the drawbacks by conducting the proposed referee RL on our developed large auto-regressive model (LARM). Specifically, LARM is built upon a lightweight LLM (fewer than 5B parameters) and directly outputs the next action to execute rather than text. We mathematically reveal that classic RL feedbacks vanish in long-horizon embodied exploration and introduce a giant LLM based referee to handle this reward vanishment during training LARM. In this way, LARM learns to complete diverse open-world tasks without human intervention. Especially, LARM successfully harvests enchanted diamond equipment in Minecraft, which demands significantly longer decision-making chains than the highest achievements of prior best methods.

---

## 论文详细总结（自动生成）

# 论文总结：LARM: Large Auto-Regressive Model for Long-Horizon Embodied Intelligence

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：现有具身智能代理主要基于强化学习（RL）或大语言模型（LLM）。RL代理轻量高效，但通常只能完成少数特定任务；超千亿参数的大LLM代理（如GPT-4）泛化能力强，但部署计算资源需求巨大。如何结合两者优势、避免各自缺陷，是核心挑战。
- **背景**：Minecraft被广泛作为开放世界、长时程决策的基准平台。早期RL方法需要精细奖励工程，只能完成简单任务；LLM方法（如Voyager）虽然泛化好，但依赖远程大规模集群，推理速度慢。
- **整体含义**：本文旨在构建一个轻量级（<5B参数）、能直接输出动作、且具备良好泛化能力的具身代理，兼顾效率与通用性。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
### 核心思想
- 提出**大型自回归模型（LARM）**：基于轻量级LLM（TinyLLaVA-3.1B）构建，直接输出下一个动作（技能）而非文本，实现快速响应。
- 提出**裁判强化学习（Referee RL）**：通过一个巨量LLM（GPT-4）作为裁判，为每一步动作提供即时辅助奖励，解决长时程探索中环境奖励稀疏导致的反馈消失问题。

### 关键技术细节
- **LARM模型结构**：
  - 主体为TinyLLaVA-3.1B的decoder部分，冻结参数，使用可训练的LoRA模块进行领域适配。
  - 输入包括任务描述、文本观察（如库存、周围方块）、视觉观察（实时图像）以及一个可学习的技能令牌。
  - 经decoder后，技能令牌分别进入动作头（actor head）和评论家头（critic head），输出下一个技能和状态值。
- **裁判RL算法（Algorithm 1）**：
  1. 在每一步，代理根据观测选取动作 `at`，执行后得到新状态 `st+1` 和环境奖励 `rt`。
  2. 裁判 `πp`（GPT-4）基于任务 ι、状态 sk、动作 ak、新状态 sk+1 输出辅助奖励 `brk`，分为四类：
     - (a) 动作正确且带来正面结果：`ra`
     - (b) 动作正确但无正面结果：`rb`
     - (c) 动作错误但无负面结果：`rc`
     - (d) 动作错误且带来负面结果：`rd`，其中 `ra > rb > 0 > rc > rd`。
  3. 总奖励 = 环境奖励 + 辅助奖励，用PPO算法更新actor和critic。
- **数学推导**：证明经典RL在长时程任务中（如式(5)）由于奖励稀疏，GAE值趋近于零（式(6)），导致优化失效；引入裁判RL后，每一步都有非零反馈，克服问题。

### 预训练
- LARM先在34GB的Minecraft相关网页数据（来自Wiki）上进行预训练，以增强领域知识。

## 3. 实验设计
### 数据集/场景
- **MineDojo**：包含数千个自然语言指定的任务，如采集、合成、战斗等。使用RL技能（原子动作）。
- **Mineflayer**：提供API级技能（如砍树、找石头），更聚焦高层决策。测试从无工具开始，完成从木剑到附魔钻石剑的五个等级任务。

### 基准与对比方法
- **MineDojo**：对比MineAgent、Plan4MC、LLaMA-Rider（Base和完整版）、RL-GPT。
- **Mineflayer**：对比AutoGPT、Voyager、STEVE。
- LARM在两种环境中均使用单个模型完成所有任务，而对比方法大多为每个任务训练独立模型。

### 评估指标
- 成功率（每个任务测试30次）。

## 4. 资源与算力
- **训练时间**：完成最具挑战性的任务（合成附魔钻石工具）约需**42小时**单卡RTX 4090上的探索。
- **推理速度**：RTX 4090上每次推理0.58秒，满足在线高层动作调度速度要求。
- 文中未明确说明使用多少张GPU或训练总轮数等细节，仅提及单卡RTX 4090。

## 5. 实验数量与充分性
- **主要实验**：在MineDojo上对比了14个任务（表1）；在Mineflayer上对比5个等级任务（表2）。
- **消融实验**：
  - 奖励设计（表3）：环境奖励 vs 加LLaVA-7B奖励 vs 加GPT-4二分类奖励 vs 四分类奖励。
  - LLM基座选择（表4）：TinyLLaVA-0.5B vs 3.1B，以及是否进行网页预训练。
  - 噪声奖励分析（表5）：10%、30%、50%的错误裁判奖励影响。
- **案例研究**（图3）：展示探索村庄、进入下界、多智能体战斗等额外行为。
- **充分性**：实验覆盖了不同难度、不同环境、多种消融变量，对比方法均为领域最新。但仅基于Minecraft，未在机器人等真实场景验证。消融实验均在同一设置下进行，结果客观公平。

## 6. 论文的主要结论与发现
- **LARM在MineDojo所有测试任务上成功率均优于对比方法**，尤其是在长时程任务（如铁剑、铁镐）上提升明显。
- **在Mineflayer上，LARM首次成功合成附魔钻石剑（16/30）**，而所有先前方法均未实现。
- **裁判RL有效解决长时程探索中奖励消失问题**，且巨型LLM（GPT-4）裁判远优于轻量级LLM（LLaVA-7B）。（表3、LLM能力对比示例）
- **预训练对知识增强有帮助**：网页数据预训练使TinyLLaVA-3.1B正确理解合成配方。
- **在噪声裁判下性能急剧下降**：超过10%的错误奖励即导致明显衰退。

## 7. 优点
- **方法创新性强**：首次将轻量LLM直接输出动作（而非文本），并设计裁判RL实现端到端在线优化，无需人类监督。
- **效率与泛化兼顾**：单模型高效完成多种任务，推理速度快（0.58s/步）。
- **理论贡献**：数学证明经典RL在长时程任务中反馈消失，并给出解决方案。
- **实验全面**：两种环境、多种任务、多组消融，结果清晰支撑论点。
- **可复现性**：提供网站（lizhuoling.github.io/LARM_webpage/）。

## 8. 不足与局限
- **环境单一**：所有实验仅在Minecraft中完成，未验证到真实机器人或其他物理仿真环境，泛化到现实世界需进一步研究。
- **依赖GPT-4作为裁判**：裁判RL有效性高度依赖巨大LLM的质量，在GPT-4不可用或收费高昂时难以复现；且对噪声敏感（>10%误差即显著下降）。
- **轻量LLM基座限制**：仅使用3.1B模型，未尝试更大轻量模型（如7B），可能性能仍有提升空间。
- **训练资源**：单卡RTX 4090需42小时，对于无强大GPU的研究者门槛仍较高；且未说明总探索步数或交互量。
- **技能生成依赖外部库**：Mineflayer API需要预先定义；MineDojo技能执行成功率未单独报告。
- **缺少与LLM类方法在相同轻量级模型上的直接比较**：如使用GPT-2或更小模型微调的基准。

（完）
