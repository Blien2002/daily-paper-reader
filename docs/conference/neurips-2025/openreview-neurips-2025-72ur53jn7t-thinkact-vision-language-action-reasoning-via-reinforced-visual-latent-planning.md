---
title: "ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning"
title_zh: ThinkAct：通过强化视觉隐式规划实现视觉-语言-动作推理
authors: "Chi-Pin Huang, Yueh-Hua Wu, Min-Hung Chen, Yu-Chiang Frank Wang, Fu-En Yang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=72UR53jN7T"
tags: ["query:vla"]
score: 9.0
evidence: 提出双系统VLA推理框架，结合强化视觉隐式规划
tldr: 现有VLA模型直接端到端映射输入到动作，缺乏显式推理，难以应对长程复杂任务。ThinkAct提出双系统框架：多模态LLM生成推理计划，再通过强化视觉隐式规划指导底层执行。实验表明该方法在多个VLA推理基准上超越端到端基线，尤其擅长多步规划任务。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1447, \"height\": 510, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1442, \"height\": 637, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1436, \"height\": 748, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1448, \"height\": 869, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 642, \"height\": 439, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1362, \"height\": 242, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-72ur53jn7t/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1369, \"height\": 239, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-72ur53jn7t/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 582, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-72ur53jn7t/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1442, \"height\": 594, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-72ur53jn7t/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 757, \"height\": 275, \"label\": \"Table\"}]"
motivation: 现有VLA模型端到端训练缺乏显式推理，难以进行多步规划和适应复杂任务。
method: 构建双系统框架，训练LLM生成推理计划，并用强化学习优化视觉隐式规划。
result: 在VLA推理任务上超越端到端方法，长程规划表现突出。
conclusion: 显式推理与强化规划结合能显著提升VLA模型的规划能力。
---

## Abstract
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与研究动机
现有视觉-语言-动作（VLA）模型大多采用端到端训练方式，直接将视觉和语言输入映射为动作，缺乏显式的推理过程。这导致模型在多步规划、适应复杂任务变化以及处理长程目标时表现受限。尤其是面对动态环境和复杂指令时，模型难以生成结构化的中间推理步骤，容易过拟合于特定场景或推理模式。为此，论文提出 **ThinkAct** 框架，旨在通过强化视觉隐式规划将高层推理与低层动作执行有机结合，提升VLA模型在具身推理和机器人操作中的能力。

## 2. 方法论：核心思想与关键技术
- **双系统架构**：分为推理多模态大语言模型（Reasoning MLLM）和动作模型（Action Model）两部分。前者负责生成高层推理计划（包括链式推理和视觉轨迹），后者负责将推理计划转化为具体的执行动作。
- **视觉隐式规划（Visual Latent Planning）**：模型将推理步骤压缩为紧凑的视觉轨迹隐变量（visual plan latent），该隐变量捕获了时空意图，并作为条件输入下游动作模型。
- **强化学习引导推理**：采用 Group Relative Policy Optimization (GRPO) 优化推理过程。关键创新在于设计了**动作对齐的视觉奖励**，包括：
  - **目标完成奖励（Goal Reward）**：比较预测轨迹的起始/终点与真实轨迹对应点的距离（使用动态时间规整DTW距离）。
  - **轨迹分布匹配奖励（Trajectory Reward）**：衡量预测轨迹与示范轨迹的整体分布一致性（同样基于DTW）。
  - 综合奖励公式：\( r = 0.9(\omega_{\text{goal}} r_{\text{goal}} + \omega_{\text{traj}} r_{\text{traj}}) + 0.1 r_{\text{format}} \)，其中 \( r_{\text{format}} \) 是格式正确性奖励。
- **动作适应阶段**：冻结推理MLLM，仅更新动作模型（基于扩散策略DiT）和状态编码器/隐投影器，通过模仿学习使动作模型在目标环境中利用推理隐变量执行动作。
- **异步执行**：推理与动作执行可异步运行，每个推理隐变量对应多个动作步（慢思考、快控制）。

## 3. 实验设计
- **数据集**：
  - 训练：Open X-Embodiment (OXE) 子集、Something-Something v2 人类视频、RoboVQA、EgoPlan-IT、Video-R1-CoT、Reflect 等。
  - 评估：机器人操作基准 **SimplerEnv**（含Google-VM、Google-VA、Bridge-VM）和 **LIBERO**（空间、物体、目标、长程四个子任务）；具身推理基准 **EgoPlan-Bench2**、**RoboVQA**、**OpenEQA**。
- **对比方法**：
  - 操作任务：Octo-Base、RT1-X、OpenVLA、DiT-Policy、TraceVLA、CoT-VLA、Magma 等。
  - 推理任务：GPT-4V、LLaVA-Video、InternVL2.5/3、NVILA、Qwen2.5-VL、Magma 等。
- **评估指标**：任务成功率（SimplerEnv、LIBERO）、准确率（EgoPlan-Bench2）、BLEU分数（RoboVQA）、LLM评分（OpenEQA）。

## 4. 资源与算力
- **硬件**：使用 16 块 NVIDIA A100 GPU（80GB 显存）。
- **训练阶段**：
  - 冷启动（SFT）：20K 迭代，batch size 32，learning rate 1e-5，DeepSpeed ZeRO-3。
  - 强化学习（GRPO）：6K 迭代，batch size 64，learning rate 1e-6，rollout size 5。
  - 动作模型适应：在 100K OXE 数据上训练 120K 迭代，batch size 256，learning rate 2e-5；LIBERO 额外 75K 迭代，batch size 128。
- **模型规模**：推理MLLM 为 Qwen2.5-VL 7B；动作模型为 DiT-based，432M 参数。

## 5. 实验数量与充分性
- **主要实验**：共 3 张核心表格（表1机器人操作、表2推理、表3消融），以及多个定性分析和额外实验（如少样本适应、自纠错、推理速度）。
- **消融实验**：对比了添加/移除目标奖励、轨迹奖励的效果，以及仅用QA奖励、无RL的基线，验证了各组件贡献。
- **公平性**：在同一基准下与多种已发表方法（包括端到端和推理增强方法）比较，使用了标准评估协议（如500 trials per task in LIBERO）。但未报告误差棒或置信区间，可能削弱统计显著性。此外，未对比所有最新方法（如某些2025年工作可能未涵盖）。

## 6. 主要结论与发现
- ThinkAct 在机器人操作任务上全面超越现有方法，尤其在长程和变体场景中（SimplerEnv 综合高出 15%+，LIBERO-Long 达 70.9%）。
- 在具身推理基准上，ThinkAct 刷新了多项记录（EgoPlan-Bench2 48.2%，RoboVQA 59.8 BLEU，OpenEQA 56.2），展现了强规划与场景理解能力。
- 少样本适应实验（10个示范）表明推理能力显著提升动作模型的泛化性，优于Magma等方法。
- 模型展现出自我纠错能力：通过观察执行历史视频片段，可识别失败并重新规划。
- 推理速度比端到端 OpenVLA 慢约17%，但性能提升更大，属于合理的测试时扩展。

## 7. 优点
- **创新性**：首次将强化学习（GRPO）与动作对齐的视觉奖励结合，引导MLLM生成具身推理，克服了传统监督式CoT对标注的依赖。
- **双系统架构**：实现了推理与执行的解耦，支持异步模式，兼顾慢思考与快控制。
- **奖励设计**：基于视觉轨迹的目标完成与分布匹配奖励，无需真实动作标签即可评估推理质量，易于扩展到新任务。
- **实验全面**：覆盖了操作与推理两大类别，多个基准，并提供了定性示例（含自纠错演示）。
- **开源导向**：论文承诺在接收后发布代码，便于复现。

## 8. 不足与局限
- **推理继承性缺陷**：MLLM 本身存在视觉/空间幻觉，可能导致生成的规划包含错误属性或空间关系，尽管通过隐规划有所缓解。
- **奖励仅基于2D轨迹**：未纳入接触力等物理信号，不能充分反映精细操作任务（如插拔）中的关键信息。
- **统计报告不充分**：未提供误差棒/置信区间，实验结果的稳定性不清晰。
- **计算成本较高**：需要16块A100进行多阶段训练，对资源要求较高。
- **推理速度有延迟**：虽被合理化为“测试时扩展”，但在实时性要求高的场景中可能受限。
- **未在真实机器人上验证**：所有实验均在模拟器（SimplerEnv、LIBERO）中进行，真实世界的泛化能力有待验证。
- **评估偏差风险**：在Summarizer指标（如BLEU、LLM评分）上可能存在度量偏差，且部分基准（如OpenEQA）使用自动评分，可能不完全反映人类判断。

（完）
