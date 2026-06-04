---
title: "ROVER: Recursive Reasoning Over Videos with Vision-Language Models for Embodied Tasks"
title_zh: ROVER：基于视觉语言模型的递归视频推理用于具身任务
authors: "Philip Schroeder, Ondrej Biza, Thomas Weng, Hongyin Luo, James R. Glass"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=NNiwGUY50Y"
tags: ["query:vla"]
score: 6.0
evidence: 使用VLM进行递归视频推理以支持具身任务
tldr: ROVER框架针对具身任务中长视频序列推理困难的问题，将长时间视频递归分解为短片段对应子任务，使得VLM能更聚焦地推理每个片段。该方法无需额外训练即可提升VLM在具身场景中的时序理解能力，实验表明在多个embodied benchmark上显著提升了任务成功率。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1443, \"height\": 899, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1162, \"height\": 580, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1452, \"height\": 604, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1086, \"height\": 367, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1452, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 805, \"height\": 334, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1451, \"height\": 293, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 835, \"height\": 417, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1175, \"height\": 644, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1177, \"height\": 600, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1295, \"height\": 351, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1295, \"height\": 350, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1296, \"height\": 389, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1369, \"height\": 1566, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1450, \"height\": 298, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1163, \"height\": 502, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1447, \"height\": 620, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1289, \"height\": 527, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1290, \"height\": 531, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 689, \"height\": 463, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 682, \"height\": 464, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 669, \"height\": 574, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 666, \"height\": 574, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 668, \"height\": 579, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 667, \"height\": 569, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 669, \"height\": 570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 667, \"height\": 568, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1422, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1427, \"height\": 406, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-nniwguy50y/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1428, \"height\": 404, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 735, \"height\": 436, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 968, \"height\": 348, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1140, \"height\": 1310, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1455, \"height\": 1922, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1406, \"height\": 1956, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 918, \"height\": 420, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1379, \"height\": 224, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1380, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 491, \"height\": 376, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 489, \"height\": 378, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1458, \"height\": 2200, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1462, \"height\": 2135, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 818, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-nniwguy50y/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1409, \"height\": 342, \"label\": \"Table\"}]"
motivation: VLM在处理长视频序列时推理能力不足，限制了其在具身场景中的使用。
method: 提出递归分解长视频轨迹为子任务段，使VLM对局部帧进行聚焦推理。
result: 在多个具身任务基准上提升了任务成功率。
conclusion: 递归分解能有效增强VLM在具身任务中的时序推理能力。
---

## Abstract
Vision-language models (VLMs) have exhibited impressive capabilities across diverse image understanding tasks, but still struggle in settings that require reasoning over extended sequences of camera frames from a video. This limits their utility in embodied settings, which require reasoning over long frame sequences from a continuous stream of visual input at each moment of a task attempt. To address this limitation, we propose ROVER (Reasoning Over VidEo Recursively), a framework that enables the model to recursively decompose long-horizon video trajectories into segments corresponding to shorter subtasks within the trajectory. In doing so, ROVER facilitates more focused and accurate reasoning over temporally localized frame sequences without losing global context. We evaluate ROVER, implemented using an in-context learning approach, on diverse OpenX Embodiment videos and on a new dataset derived from RoboCasa that consists of 543 videos showing both expert and perturbed non-expert trajectories across 27 manipulation tasks. ROVER outperforms strong baselines across three video reasoning tasks: task progress estimation, frame-level natural language reasoning, and video question answering. We observe that, by reducing the number of frames the model reasons over at each timestep, ROVER mitigates model hallucinations, especially during unexpected or non-optimal moments of a trajectory. In addition, by enabling the implementation of a subtask-specific sliding context window, ROVER's time complexity scales linearly with video length, an asymptotic improvement over baselines.

---

## 论文详细总结（自动生成）

# 论文总结：ROVER: Recursive Reasoning Over Videos with Vision-Language Models for Embodied Tasks

## 1. 核心问题与整体含义（研究动机和背景）

- **背景**：视觉语言模型（VLM）在图像理解任务上表现出色，但在处理长视频序列（尤其是来自机器人的连续摄像头流）时推理能力不足。在具身任务（embodied tasks）中，模型需要持续接收大量视频帧，并根据任务描述实时推理当前进度和下一步动作。
- **核心问题**：现有方法要么仅对少量帧进行局部推理（丢失全局上下文），要么将全部帧一次性拼接输入（计算成本高、模型易被冗余信息淹没、产生幻觉）。
- **研究动机**：希望在不牺牲效率或全局上下文的前提下，实现高精度的逐帧推理。
- **整体含义**：本文提出的 ROVER 框架通过递归分解长视频轨迹为子任务段，使 VLM 在每个时刻只需聚焦于局部帧序列，从而提升推理准确性和效率。

## 2. 方法论

### 核心思想
ROVER 是一个递归框架，将给定任务分解为多个子任务，并为每个子任务生成独立的推理线（reasoning line）。当子任务完成时，其推理线终止，并创建新的推理线处理下一子任务的视频输入。该方法允许模型在每个时刻保持紧凑的时序上下文（最多3帧），从而减少幻觉并提升效率。

### 关键技术细节

- **递归分解算法**：给定上下文 c（任务描述+初始帧）和已生成的令牌序列 Y，模型 Θ 逐令牌生成。当 Y 中包含“下一帧”标记时，附加下一帧的图像令牌。当 Y 指定新子任务时，递归调用 ROVER(ϕ(Y), []) 创建子进程，子进程返回后将其输出附加到父进程。当任务完成或视频结束时返回完整序列。
- **ϕ 和 ψ 函数**：ϕ 从父进程最新帧和子任务描述生成子进程的上下文；ψ 返回子进程的最终帧及对应文本描述。
- **特殊标记**：`[next-frame]` 表示获取下一帧；`The robot needs to: {new_subtask}` 用于指定新子任务。
- **滑动上下文窗口**：在每个子任务内，只保留该子任务第一帧、上一帧以及当前帧（共3帧），窗口随帧前进滑动。这使推理复杂度从 O(n²) 降至 O(n)，有效缓解长上下文幻觉。

### 算法流程（文字说明）
1. 初始输入：任务描述和第一帧图像。
2. 模型生成当前帧的描述和子任务进度预测。
3. 若需要，模型指定新子任务，递归调用自身。
4. 逐帧推进：生成 `[next-frame]`，附加下一帧，窗口保留三帧。
5. 子任务完成后返回父进程，继续下一子任务。
6. 直到所有子任务完成或视频结束。

## 3. 实验设计

### 数据集

- **RoboCasa 模拟环境**：生成 543 个视频，覆盖 27 个机器人操作任务，每个任务包含专家轨迹和通过插入随机扰动生成的非专家轨迹（分为不同水平等级）。视频来自机械臂腕部相机和第三视角。
- **OpenX Embodiment (OXE)**：50 个真实世界数据集，共 1000 个视频，用于评估任务进度预测。

### Benchmark 任务

1. **帧级任务进度估计**：预测每帧的任务完成百分比，与基于几何距离的 ground-truth 值比较，指标为 Pearson 相关系数和 L2 距离。
2. **帧级自然语言推理**：评估模型每帧生成的描述是否正确（错误率、成功率），通过 GPT-4.5 自动判断。
3. **视频问答 (QA)**：询问特定事件是否发生及发生时间，评估准确性、精确率、召回率和时间偏差。

### 对比方法

- **LIV**：基于对比学习的价值模型（微调）。
- **GVL (Generative Value Learning)**：随机打乱帧顺序的上下文学习方法。
- **TemporalConcat**：按时间顺序拼接所有帧。
- **LocalConcat**：仅保留最近三帧。
- 扩展基线：VideoLLaMA-3、Video-LLaVA、VideoGemini（所有帧拼接）。
- 主实验使用 Gemini-1.5-Pro，附录也测试了 Gemini-2.5-Pro-Preview、GPT-4o、Qwen-2.5-VL-32B。

## 4. 资源与算力

论文未明确说明训练资源（因为 ROVER 采用上下文学习，无需额外训练）。对于推理，他们使用了 Google Gemini API 和 OpenAI API，以及 Qwen-2.5-VL-32B（在 A6000 GPU 上运行）。未提及训练成本或总计算量。

## 5. 实验数量与充分性

- **实验数量**：在 RoboCasa 上进行了 543 个视频的 3 项任务评估；在 OXE 上进行了 1000 个视频的进度预测；还做了消融实验（窗口大小、递归组件）、不同骨干模型对比、不同帧率/视频长度、不同相机视角的鲁棒性测试、错误分析（手动审查 200 个视频）。
- **充分性**：实验覆盖了多种任务类型（原子任务和复合任务）、多种性能指标、多种 backbone，并进行了消融和误差分析。实验设计较为全面，对比方法包括最先进的 GVL 以及其他视频模型，公平性较好。但所有模拟实验均基于 RoboCasa，真实世界实验仅使用了 OXE 视频（无真实进度标签），泛化到其他真实场景的验证有限。

## 6. 主要结论与发现

- ROVER 在三个 benchmark 上均优于所有基线，尤其是在包含非专家行为（非最优轨迹）的视频上提升显著。
- ROVER 通过缩短每个时刻的推理帧数，有效减少了 VLM 的幻觉（perception errors），特别是在上下文帧数超过 10 帧时。
- ROVER 的时间复杂度为 O(n)（线性），而基线方法（如 TemporalConcat）为 O(n²)，因此推理效率更高。
- 在 OXE 数据集上，ROVER 与帧号的相关系数普遍高于 GVL，表明其进度预测更贴近实际进展。
- 错误分析表明，ROVER 的主要错误类型是子任务分解错误（约 7-9%），但总错误率远低于 GVL（23% vs 57-76%）。

## 7. 优点

- **创新性**：递归分解+滑动窗口的联合设计，同时解决了全局上下文丢失和计算成本过高的问题。
- **无需微调**：完全基于上下文学习，可直接利用现有 VLM，便于部署。
- **效率提升**：线性时间复杂度，理论上可扩展到更长的视频。
- **实验设计严谨**：生成了带 ground-truth 进度标签的非专家轨迹数据集，支持细粒度评估；进行了多维度消融和鲁棒性分析。
- **可复现性**：论文提供了代码和数据集链接。

## 8. 不足与局限

- **分解错误**：当子任务分解不正确时（如引入不必要或错误的子任务），推理可能变得碎片化或偏离实际任务。
- **仅验证了上下文学习方法**：未探索微调方法可能带来的进一步提升。
- **真实世界评估受限**：OXE 视频缺少真实进度标签，只能用帧号近似，可能不够准确。
- **场景限制**：模拟实验仅在 RoboCasa 厨房场景中进行，任务类型为机器人操作，泛化到其他具身场景（如移动机器人、复杂环境）有待验证。
- **滑动窗口大小固定为3帧**：虽然效果良好，但某些任务可能需要更多帧上下文才能准确捕捉事件（如快速动作）。
- **未与强化学习等具身系统集成**：论文仅评估了推理能力，未展示 ROVER 在端到端控制或奖励函数生成中的实际应用效果。

（完）
