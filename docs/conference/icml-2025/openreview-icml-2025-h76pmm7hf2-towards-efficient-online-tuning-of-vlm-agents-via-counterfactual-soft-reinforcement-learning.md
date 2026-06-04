---
title: Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning
title_zh: 通过反事实软强化学习实现VLM代理的高效在线微调
authors: "Lang Feng, Weihao Tan, Zhiyi Lyu, Longtao Zheng, Haiyang Xu, Ming Yan, Fei Huang, Bo An"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=H76PMm7hf2"
tags: ["query:vla"]
score: 8.0
evidence: 使用反事实软强化学习在线微调VLM代理以实现高效探索
tldr: 在线微调VLM代理面临动作空间爆炸等挑战。本文提出反事实软强化学习(CoSo)，利用反事实推理动态评估每个token的因果影响，从而更有效地进行在线探索。实验证明，CoSo在多个VLM代理任务中提升了探索效率和任务性能，为整合VLM与决策空间提供了可行方法。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1664, \"height\": 538, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 846, \"height\": 376, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1711, \"height\": 1199, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 833, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 800, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1592, \"height\": 364, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1592, \"height\": 456, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 894, \"height\": 339, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 543, \"height\": 83, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 293, \"height\": 293, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 294, \"height\": 293, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-h76pmm7hf2/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 293, \"height\": 290, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-h76pmm7hf2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 858, \"height\": 782, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-h76pmm7hf2/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1644, \"height\": 584, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-h76pmm7hf2/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1726, \"height\": 485, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-h76pmm7hf2/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1236, \"height\": 186, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-h76pmm7hf2/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1560, \"height\": 275, \"label\": \"Table\"}]"
motivation: VLM代理在线微调中探索空间过大。
method: 基于反事实推理评估token因果影响进行软强化学习。
result: 提升了VLM代理的探索效率和任务性能。
conclusion: 反事实推理可有效优化VLM代理的在线微调。
---

## Abstract
Online fine-tuning vision-language model (VLM) agents with reinforcement learning (RL) has shown promise for equipping agents with multi-step, goal-oriented capabilities in dynamic environments. However, their open-ended textual action space and non-end-to-end nature of action generation present significant challenges to effective online exploration in RL, e.g., explosion of the exploration space. We propose a novel online fine-tuning method, Counterfactual Soft Reinforcement Learning (CoSo), better suited to the textual output space of VLM agents. Compared to prior methods that assign uniform uncertainty to all tokens, CoSo leverages counterfactual reasoning to dynamically assess the causal influence of individual tokens on post-processed actions. By prioritizing the exploration of action-critical tokens while reducing the impact of semantically redundant or low-impact tokens, CoSo enables a more targeted and efficient online rollout process. We provide theoretical analysis proving CoSo's convergence and policy improvement guarantees, and extensive empirical evaluations supporting CoSo's effectiveness. Our results across a diverse set of agent tasks, including Android device control, card gaming, and embodied AI, highlight its remarkable ability to enhance exploration efficiency and deliver consistent performance gains. The code is available at https://github.com/langfengQ/CoSo.

---

## 论文详细总结（自动生成）

# 论文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：在线微调视觉-语言模型（VLM）代理时，强化学习（RL）面临严重的探索效率问题。原因是：
  - VLM 的文本动作空间是开放式的，词汇量和序列长度导致指数级搜索空间。
  - 动作生成并非端到端：模型输出自然语言语句（utterance），需通过解析函数转换为可执行动作。许多 token（如固定格式、语义冗余）对最终动作无实质影响。
- **现有方法不足**：传统 RL 及其熵正则化对所有 token 分配均匀的不确定性，导致大量无效探索，难以带来有意义的动作变化。
- **本文目标**：提出一种更高效的在线微调方法，通过识别并优先探索对动作有因果影响的 token，缩小探索空间，提升 RL 训练效率。

## 2. 方法论

- **核心思想**：利用反事实推理计算每个 token 对解析动作的因果权重，将加权熵正则化引入软 RL 目标，实现定向探索。
- **关键技术细节**：
  - **Token-to-Action 因果结构**：将解析函数建模为 `a = f_parse(B ⊙ y)`，其中 `B` 为权重向量。
  - **反事实推理**：用一个轻量级 SCM（结构因果模型，BERT 网络，0.01B 参数）近似 `P(a|y, ε)`。对每个 token `y_i`，将其替换为 null 值，计算动作似然的变化作为因果权重：`B_i = P(a|y) - P(a|y_{-i} ∪ y_i^null)`。
  - **因果加权熵正则化**：在软 RL 目标中，将熵项替换为因果加权和：`H_B(π|s) = Σ_i B_i · H(y_i | y_{1:i-1})`。这样，高权重 token（少于 10%）得到更多探索，低权重 token（超 80%）被抑制。
- **算法流程**（Algorithm 1）：
  1. 离线阶段：用 SFT 初始化 VLM 策略。
  2. 在线阶段每轮：
     - Rollout：VLM 与环境交互，收集数据。
     - 反事实推理：为每个 token 计算因果权重。
     - 模型更新：更新 SCM（交叉熵损失），用 CoSo 目标更新 VLM。
- **理论保证**：Lemma 4.2 证明策略评估的收敛性；Lemma 4.3 证明策略改进；Proposition 4.4 保证策略迭代收敛到最优。

## 3. 实验设计

- **数据集/场景**：
  - **Android-in-the-Wild（AitW）**：General 和 WebShopping 任务，涉及 GUI 操作。
  - **Gym Cards**：NumberLine、EZPoints、Points24、Blackjack 四个数字推理任务。
  - **ALFWorld**：Pick&Place、ExamineInLight、Clean&Place、Heat&Place、Cool&Place、PickTwo&Place 六种具身任务。
  - **附录扩展**：纯文本 ALFWorld 环境（AlfredTWEnv）测试 LLM 代理。
- **Benchmark 与对比方法**：
  - Prompting 方法：Gemini 1.5 Pro、GPT-4V、AppAgent。
  - 学习类方法：CogAgent、AutoUI+SFT、Online Filtered BC、DigiRL（AitW 基线）、CNN+RL、LLaVA-1.6+SFT、RL4VLM（Gym Cards/ALFWorld 基线）。
  - CoSo 实现：基于 DigiRL（AitW）和 RL4VLM（Gym Cards/ALFWorld）。
- **消融实验**：在 WebShopping 和 NumberLine 上比较标准 RL、RL+均匀熵、CoSo（RL+HB）。
- **探索效率定性分析**：重复采样对比（Figure 3 下）展示不同方法在错误恢复时的动作分布。

## 4. 资源与算力（附录 D）

- **GPU 型号**：NVIDIA H100。
- **参数规模**：VLM 7.96B，SCM 0.01B，总计 7.97B。
- **GPU 内存**：VLM 37.0 GB，SCM 0.7 GB，总计 37.7 GB。
- **训练时间**（H100 GPU 小时）：
  - 基线 RL：13.9
  - RL + 均匀熵：14.0
  - CoSo：14.5
- **说明**：CoSo 引入的额外开销较小（<4% 时间，<2% 内存），主要来自因果权重计算。

## 5. 实验数量与充分性

- **实验总量**：覆盖 3 个主要场景，含 2 个子集（AitW）、4 个任务（Gym Cards）、6 个子任务（ALFWorld），共约 12 个实验设置。
- **每个实验**均报告 3 个随机种子的平均成功率及标准差。
- **消融实验**：1 组（WebShopping + NumberLine），直接验证因果权重的作用。
- **定性实验**：重复采样对比（Figure 3 下），可视化因果权重分布（Figure E.1、E.2）。
- **扩展验证**：LLM 代理实验（AlfredTWEnv，Table C.1）证明方法泛化性。
- **充分性评价**：实验设计较为全面，对比了多种主流基线（包括强 prompt 方法、SFT 方法、现有 RL 方法），覆盖不同难度的任务类型，统计方式规范。但缺少在更多 VLM 架构（如 GPT-4V 微调）上的扩展验证。

## 6. 主要结论与发现

- CoSo 在三个场景中均一致优于现有 RL 微调方法：
  - AitW：平均成功率 72.9%，比 DigiRL 提升 12.3%。
  - Gym Cards：平均 49.3%，比 RL4VLM 提升 9.3%。
  - ALFWorld：平均 26.5%，比 RL4VLM 提升 16.7%。
- 消融实验证明：均匀熵仅有微小改进，而因果加权熵带来显著加速和最终性能提升。
- 反事实推理能有效识别行动关键 token（<10%），将探索聚焦在有效区域。
- 理论分析保证了 CoSo 的收敛性和策略单调改进。

## 7. 优点

- **方法创新**：将因果反事实推理引入 VLM 代理的在线 RL 微调，解决探索空间爆炸问题。
- **通用性**：提供统一的因果加权熵形式，可灵活适配多种 RL 目标（如 AWR、PPO），并支持 LLM 代理。
- **理论扎实**：给出了收敛性和策略改进的数学证明。
- **实验规范**：多任务、多基线、多次重复实验，结果可靠；提供代码开源。
- **效率可控**：额外计算开销很小（<4% 训练时间），适合实际应用。

## 8. 不足与局限

- **长序列限制**：实验中最大序列长度小于 300 token，未验证超长思维链（CoT）下的效果。作者将其列为未来方向。
- **SCM 依赖**：因果权重计算依赖一个额外的 SCM 模型（BERT），其质量可能影响性能；虽然 SCM 较小，但训练和推理仍增加复杂度。
- **实验覆盖有限**：仅测试了基于 AutoUI 和 LLaVA-1.6 的 VLM 架构，未在更大规模或不同架构（如 Qwen-VL、Gemini 等）上验证；且仅包含三个环境，可能无法完全代表真实世界任务多样性。
- **未讨论偏差风险**：因果权重可能放大某些 token 的偏见，论文未分析公平性或鲁棒性。
- **定性分析欠缺**：探索效率的定性分析（Figure 3）虽直观，但缺少量化指标（如探索到达新状态的数量、动作多样性等）。

（完）
