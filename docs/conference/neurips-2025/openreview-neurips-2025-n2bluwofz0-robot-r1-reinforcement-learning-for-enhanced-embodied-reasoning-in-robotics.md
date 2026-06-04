---
title: "Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics"
title_zh: Robot-R1：强化学习增强机器人具身推理
authors: "Dongyoung Kim, Sumin Park, Huiwon Jang, Jinwoo Shin, Jaehyung Kim, Younggyo Seo"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=N2bLuwofZ0"
tags: ["query:vla"]
score: 7.0
evidence: 使用强化学习增强基于LVLMs的具身推理，用于机器人控制
tldr: 监督微调在机器人具身推理中面临灾难性遗忘和泛化不足。Robot-R1提出使用强化学习优化LVLM的推理能力，使其更好地预测任务完成的下一关键点状态。实验表明该方法在多个机器人控制任务上优于监督微调基线，且泛化性更强。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1429, \"height\": 683, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1303, \"height\": 590, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 237, \"height\": 241, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 616, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1331, \"height\": 208, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 233, \"height\": 233, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 673, \"height\": 449, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n2bluwofz0/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 683, \"height\": 445, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1159, \"height\": 723, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 566, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1455, \"height\": 398, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1451, \"height\": 467, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1457, \"height\": 143, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 737, \"height\": 142, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1435, \"height\": 324, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1455, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1453, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1450, \"height\": 259, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1454, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1453, \"height\": 180, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n2bluwofz0/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1446, \"height\": 182, \"label\": \"Table\"}]"
motivation: 监督微调在机器人具身推理中导致灾难性遗忘和泛化降低。
method: 采用强化学习训练LVLM预测下一关键点状态，直接优化机器人控制目标。
result: 在多个机器人控制任务上超越监督微调方法，泛化性提高。
conclusion: 强化学习能更有效对齐LVLM的推理与机器人控制需求。
---

## Abstract
Large Vision-Language Models (LVLMs) have recently shown great promise in advancing robotics by combining embodied reasoning with robot control. A common approach involves training on embodied reasoning tasks related to robot control using Supervised Fine-Tuning (SFT). However, SFT datasets are often heuristically constructed and not explicitly optimized for improving robot control. Furthermore, SFT often leads to issues such as catastrophic forgetting and reduced generalization performance. To address these limitations, we introduce Robot-R1, a novel framework that leverages reinforcement learning to enhance embodied reasoning specifically for robot control. Robot-R1 learns to predict the next keypoint state required for task completion, conditioned on the current scene image and environment metadata derived from expert demonstrations. Inspired by the DeepSeek-R1 learning approach, Robot-R1 samples reasoning-based responses and reinforces those that lead to more accurate predictions. Our experiments show that models trained with Robot-R1 outperform SFT methods on embodied reasoning tasks. Despite having only 7B parameters, Robot-R1 even surpasses GPT-4o on reasoning tasks related to low-level action control, such as spatial and movement reasoning.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：大型视觉语言模型（LVLMs）在机器人控制中通过结合具身推理与动作生成展现出潜力。常用方法是使用监督微调（SFT）在问答数据集上训练模型进行推理，但SFT存在两个关键缺陷：
  - SFT数据集往往是启发式构建的，并未针对优化机器人控制进行明确设计；
  - SFT容易导致灾难性遗忘（catastrophic forgetting）和泛化性能下降。
- **动机**：受DeepSeek-R1强化学习（RL）方法的启发，作者希望利用RL来激励和强化LVLM的推理路径，从而克服SFT的局限，更有效地将推理能力与机器人控制对齐。
- **整体含义**：提出Robot-R1框架，通过强化学习训练LVLM预测下一个关键点（keypoint）状态，使模型学会执行与机器人控制直接相关的具身推理，提升低层动作控制的准确性。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：使用RL来训练LVLM生成推理过程（reasoning trace），并基于预测准确性奖励来优化，使得模型能够从经验示范中学习预测任务完成所需的下一步状态。
- **关键技术细节**：
  1. **问题重新公式化**：将连续空间的下一状态预测转化为**多项选择问答（MCQA）**问题，缩小动作空间，提高探索效率。
  2. **数据生成**：从专家示范中提取元数据（参考点、坐标系、对象尺寸等），构建三类QA任务：
     - 路点预测QA（主任务）：预测下一关键点的状态（x,y,z）；
     - 当前状态预测QA（辅助任务）：从图像推断当前状态；
     - 运动预测QA（辅助任务）：基于状态变化预测规则化的语言描述（如“move up”）。
  3. **训练算法**：采用**组相对策略优化（GRPO）**，对每个查询生成G个响应，计算优势函数并最大化带KL惩罚的目标函数。
  4. **奖励设计**：包含格式奖励（确保输出结构）和答案正确性奖励（基于MCQA选项匹配）。
  5. **推理生成**：模型被要求将思考过程封装在`<think>...</think>`标签中，最终答案在`<answer>...</answer>`中。
  6. **基座模型**：使用Qwen2.5-7B-VL-Instruct（7B参数）。

## 3. 实验设计

- **数据集与场景**：
  - 训练数据来自RLBench的5个任务（pick_up_cup, push_button, put_rubbish_in_bin, phone_on_base, take_lid_off_saucepan），每个任务50个示范，提取路点，生成约7.5K个QA对。
  - 提出的新基准**Robot-R1 Bench**：包含50张图像（来自RLBench的10个任务），共215个开放式问题，覆盖四种推理类型（规划、高层动作、运动、空间推理），使用GPT-4o作为评判器（LLM-as-judge）评分[0,3]。
- **对比方法**：
  - 商用模型：GPT-4o、GPT-4o-mini、Claude系列（3-Opus, 3.5-Haiku, 3.5-Sonnet-v2, 3.7-Sonnet）、Gemini系列（1.5-Flash, 1.5-Pro, 2.0-Flash）、Qwen2.5-VL-7B-Ins。
  - 基线方法：直接SFT（直接预测下一状态）、CoT SFT（使用人工设计的链式推理路径）。
- **外部基准**：
  - **EmbodiedBench Manipulation**：基于RLBench的视觉驱动智能体评估，包含4个任务（Pick & Place, Stack Objects, Shape Sorter, Table Wiping），按指令复杂性分5类。
  - **SpatialRGPT-Bench**：测试3D空间理解（定量和定性）。
- **消融实验**：不同RL算法（GRPO vs RLOO vs REINFORCE++）、不同随机种子、不同辅助任务组合、不同问题格式（MCQA vs 开放生成）。
- **额外评估**：真实机器人（BridgeV2数据集）、VLABench、LIBERO模拟、真实机器人Pick-and-Place。

## 4. 资源与算力

- 论文明确说明：所有实验在**单个节点配备4张A100 80GB GPU**上运行。
- 训练Robot-R1需要约**12小时**完成5个epoch（使用7.5K提示词）。
- SFT基线使用相同的批大小但学习率不同，未单独说明训练时长。

## 5. 实验数量与充分性

- **实验数量**：核心实验覆盖了6个主要基准（Robot-R1 Bench、EmbodiedBench、SpatialRGPT-Bench、Bridge Bench、VLABench、LIBERO、真实机器人），加上多种消融（算法、种子、任务组件、问题格式、冷启动等），共约15组以上的比较实验。
- **充分性判断**：
  - **优势**：涵盖模拟和真实场景，对比多个商用模型和SFT基线，消融实验全面，验证了RL算法选择、种子稳定性、辅助任务贡献等。
  - **局限性**：
    - 所有基准测试中仅使用一个随机种子（除种子消融外），未报告误差棒或置信区间；
    - Robot-R1 Bench的LLM-as-judge与人类评分的相关性较高（除规划任务外），但整体评估依赖GPT-4o，可能存在偏差；
    - 训练数据仅来自RLBench的5个任务，且仅使用XYZ位置（忽略旋转和夹爪），可能限制泛化性；
    - 在复杂逻辑/物理规律任务（如VLABench的Physical Law）上性能下降，表明学到的是与空间和运动相关的推理，而非通用推理。

## 6. 主要结论与发现

- **核心结论**：Robot-R1框架通过强化学习训练LVLM生成推理路径，显著提升了在低层动作控制相关的具身推理能力（如运动推理、空间推理），优于SFT基线和多个商用大模型（如GPT-4o）。
- **关键发现**：
  - 仅训练7B参数模型即可在Robot-R1 Bench的低层控制任务上超越GPT-4o；
  - 在EmbodiedBench上获得约31%的性能提升，而SFT方法完全失败；
  - 在SpatialRGPT-Bench上定量任务提升约40%，定性任务提升约60%；
  - 推理长度在训练过程中逐渐缩短，从概括性格式转向更聚焦的叙事格式；
  - 辅助任务（当前状态预测、运动预测）有助于提升整体性能；MCQA格式优于开放生成格式。

## 7. 优点

- **方法创新**：将连续空间预测转化为离散MCQA问题，显著降低RL探索难度；结合辅助任务提升状态理解和运动推理。
- **实验设计**：提出专门评估具身推理的Robot-R1 Bench，涵盖多种推理类型且使用LLM-as-judge自动化评估，操作性强。
- **泛化验证**：不仅评估模拟环境，还扩展到真实机器人数据（BridgeV2）和多种下游任务（LIBERO、VLABench、真实Pick-and-Place），展示了转移能力。
- **资源效率**：仅用4×A100和12小时训练时间，参数7B，即可达到甚至超越商用大模型，具有实际部署潜力。
- **对比公平**：与多种最新版本的商用模型（GPT-4o, Claude 3.7, Gemini 2.0等）比较，结果具有说服力。

## 8. 不足与局限

- **状态维度限制**：仅使用XYZ位置，忽略旋转（roll, pitch, yaw）和夹爪状态，因此无法推理需要精细旋转或夹爪动作的任务。
- **训练数据局限性**：仅基于RLBench模拟的5个任务，场景多样性和物体种类有限，可能导致在客观类别（如LIBERO Goal）上表现提升但Objective类别略有下降。
- **评估偏差风险**：Robot-R1 Bench依赖GPT-4o作为评判，尽管与人类评分的相关性较高，但仍存在自动评估的偏差风险；规划任务相关性较低（0.33），说明该任务评分不够可靠。
- **未报告统计显著性**：除种子消融外，其他实验未提供误差棒或置信区间，部分结论的稳健性有待进一步证实。
- **开放生成格式效果差**：MCQA格式效果更好，但实际应用中机器人控制往往需要连续输出，MCQA的离散化可能限制了直接部署的灵活性。
- **社会影响**：论文提到RL训练可能导致机器人执行意外动作以达到目标，但未提出详细缓解措施。

（完）
