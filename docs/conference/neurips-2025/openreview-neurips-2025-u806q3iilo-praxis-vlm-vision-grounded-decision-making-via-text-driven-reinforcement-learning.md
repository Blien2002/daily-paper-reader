---
title: "Praxis-VLM: Vision-Grounded Decision Making via Text-Driven Reinforcement Learning"
title_zh: Praxis-VLM：通过文本驱动强化学习实现视觉接地决策
authors: "Zhe Hu, Jing Li, Zhongzhu Pu, Hou Pong Chan, Yu Yin"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=U806q3iILo"
tags: ["query:vla"]
score: 6.0
evidence: 通过文本驱动强化学习增强VLM的视觉接地决策能力
tldr: Praxis-VLM观察到VLM在纯文本场景下已有强推理能力，因此提出在文本描述场景上使用GRPO算法训练VLM推理动作后果，再迁移到多模态场景。实验证明该方法显著提升了VLM在视觉决策任务上的准确率，为将LLM推理能力用于具身智能提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1435, \"height\": 734, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 633, \"height\": 365, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1440, \"height\": 395, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 672, \"height\": 387, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 602, \"height\": 389, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1451, \"height\": 409, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1351, \"height\": 291, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1442, \"height\": 370, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1444, \"height\": 815, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 349, \"height\": 204, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 339, \"height\": 263, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-u806q3iilo/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 752, \"height\": 130, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-u806q3iilo/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1296, \"height\": 519, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-u806q3iilo/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1472, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-u806q3iilo/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 375, \"height\": 289, \"label\": \"Table\"}]"
motivation: VLM在复杂决策中缺乏情景推理能力，但文本场景推理表现出色。
method: 在纯文本场景上使用GRPO强化学习训练VLM推理能力，再迁移到视觉场景。
result: 在视觉决策任务上取得显著提升。
conclusion: 文本推理可有效迁移至多模态场景，提升VLM决策能力。
---

## Abstract
Vision Language Models exhibit impressive performance for various tasks, yet they often lack the sophisticated situational reasoning required for complex decision-making. This paper shows that VLMs can achieve surprisingly strong decision-making performance when visual scenes are replaced by textual descriptions, suggesting foundational reasoning can be effectively learned from language. Motivated by this insight, we propose Praxis-VLM, a reasoning VLM for vision-grounded decision-making. Praxis-VLM employs the GRPO algorithm on textual scenarios to instill robust reasoning capabilities, where models learn to evaluate actions and their consequences. These reasoning skills, acquired purely from text, successfully transfer to multimodal inference with visual inputs, significantly reducing reliance on scarce paired image-text training data. Experiments across diverse decision-making benchmarks demonstrate that Praxis-VLM substantially outperforms standard supervised fine-tuning, exhibiting superior performance and generalizability. Further analysis confirms that our models engage in explicit and effective reasoning, underpinning their enhanced performance and adaptability.

---

## 论文详细总结（自动生成）

# 论文总结：Praxis-VLM：通过文本驱动强化学习实现视觉接地决策

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：Vision Language Models (VLMs) 在复杂视觉情景决策中缺乏显式的推理能力，难以进行“先思考再决策”的类人推理过程。现有提升VLM推理的方法依赖大量配对的图像-文本训练数据，成本高昂且难以扩展。
- **关键发现**：作者发现，当视觉场景被替换为纯文本描述时，VLMs在视觉决策任务上的表现竟然相当甚至更好，这表明基础决策推理能力可以从语言中有效学习，而不必依赖多模态数据。
- **整体含义**：提出一种数据高效的路径：通过文本驱动的强化学习赋予VLM可迁移的推理能力，然后在多模态推理阶段将这种能力应用于真实视觉输入，从而显著降低对配对图像-文本数据的依赖。

## 2. 论文提出的方法论

- **核心思想**：决策推理能力可以与视觉感知解耦，优先通过纯文本情景学习，再通过推理时的视觉输入进行接地。类比人类的心智模型理论——人在推理时使用内部语言表征。
- **关键技术**：
    - **文本训练数据构建**：使用GPT-4o自动生成10K训练样本和1K验证样本，每个样本包括文本情景描述、多项选择决策问题和正确答案。无需人工筛选或昂贵标注。
    - **GRPO (Group Relative Policy Optimization) 强化学习**：在文本数据上优化VLM策略，鼓励模型生成显式推理链（`<think>...</think><answer>...</answer>`），通过规则奖励（格式、准确率、推理长度）进行训练。
    - **多阶段自适应奖励训练**：
        - **Stage 1（冷启动）**：使用几何数学数据（Geometry3K）训练，强制模型学习输出格式和基本逻辑推理。
        - **Stage 2（文本决策RL）**：使用文本决策数据集，奖励函数包括格式、决策准确率和推理长度（`R_len`），鼓励更长的推理链以进行更全面的情景分析。
    - **训练时只更新语言模型组件**，推理时使用完整的VLM架构（包括视觉编码器），实现文本学到的推理能力向视觉场景迁移。
- **公式/算法流程**：GRPO目标函数包含裁剪的policy ratio、优势估计（组内归一化）和KL散度惩罚项；推理长度奖励`R_len = min(word_count / 250, 1.0)`。

## 3. 实验设计

- **使用的数据集/场景**：
    - **VIVA**（1240样本）：以人为中心的情景决策，需根据图像理解社会情境预测合适行为。
    - **PCA-Bench**（317样本）：具身智能体任务，包括机器人、自动驾驶和交互游戏，使用开放测试集。
    - **EgoNormia**（1743样本）：第一人称视频理解，需从自我中心视角预测行为，作为**域外（out-of-domain）基准**。
- **Benchmark形式**：所有任务均为多选视觉问答，评价指标为准确率（Accuracy）。
- **对比方法**：
    - 基线：Qwen2.5-VL（3B和7B）原始版本（vanilla）。
    - 监督微调（SFT）两种变体：直接预测答案的 `w/ SFT`；先生成推理链再输出答案的 `w/ Reason SFT`。
    - 消融：单阶段GRPO（无数学冷启动）的 `w/ one-stage GRPO`。
- **实现细节**：使用EasyRL库实现GRPO，rollout N=5，KL系数0.01，lr=1e-6；SFT使用HuggingFace TRL，3个epoch，lr=2e-5。全部使用BF16全参数微调。

## 4. 资源与算力

- 论文明确提到：“All models are trained on four NVIDIA A100 and H100 GPUs.” 未提供具体训练时长（如训练epoch数或wall-clock时间）。对于SFT和GRPO训练的具体时间未给出，但GRPO训练使用了rollout和多次采样，计算消耗应高于SFT。
- 推理使用VLLM库，greedy decoding。

## 5. 实验数量与充分性

- **实验数量**：
    - 主实验：在3个基准上对比了3种模型（3B/7B）的5个变体（vanilla, SFT, Reason SFT, Praxis-VLM, one-stage GRPO），共约30组结果（表1）。
    - 推理长度分析（图4）：按长度分5个bin计算准确率。
    - 多样化采样实验（表2）：每个样本采样8次，报告Majority Vote和Pass@8。
    - 推理维度聚类分析（图5）：GPT-4o生成关键词并聚类为4类。
    - 错误分析（图6）：列举3类常见错误。
- **充分性与客观性**：
    - 实验覆盖了同域（VIVA, PCA-Bench）和域外（EgoNormia）任务，对比了SFT和原始模型，并且有单阶段消融。
    - 结果使用贪婪解码，未报告置信区间或多次运行均值，但多样采样实验部分弥补了统计稳健性。
    - 训练数据生成使用GPT-4o，可能引入噪声，但作者指出无需人工过滤，是一种低成本扩展。
    - 总体上实验设计较为全面，消融合理，结论有支撑。

## 6. 论文的主要结论与发现

- **文本驱动的GRPO训练可以成功迁移至多模态推理**：Praxis-VLM在所有基准上一致优于原始VLM和SFT变体。
- **泛化能力显著更强**：尤其在域外EgoNormia上，Praxis-VLM保持高准确率，而SFT变体性能大幅下降，说明RL学到了更普适的决策技能，而非简单的模式匹配。
- **数学冷启动进一步提升泛化能力**：两阶段Praxis-VLM在域外任务上优于单阶段变体，表明基础逻辑推理训练促进了跨域适应。
- **推理长度与样本难度相关**：模型在困难样本上自动生成更长推理，但仍保持比基线更高的准确率。
- **推理过程呈现多维结构**：模型在推理中体现了情景分析、行动后果评估、安全风险管理和规则规范遵循四大维度。
- **错误类型包括**：情景误解、安全优先级错误、社会规范偏差。

## 7. 优点

- **数据高效性**：完全使用文本数据训练推理能力，无需昂贵的配对图像-文本数据，大幅降低数据获取成本。
- **方法简洁且具有普适性**：GRPO+规则奖励，无需训练额外奖励模型或依赖人工标注推理链，易于复现。
- **推理可解释性与可迁移性**：模型生成显式推理链，有助于分析决策过程，且学到的能力可跨域迁移。
- **性能提升显著**：在7B模型上，PCA-Bench提升约14个百分点（46.37→60.25），EgoNormia提升约8个百分点，效果突出。
- **实验分析深入**：包括推理长度、多样采样、推理维度聚类和错误分析，为后续研究提供了洞见。

## 8. 不足与局限

- **实验统计稳健性不足**：主实验仅使用单次贪婪解码结果，未提供误差条或多次运行统计，可能受随机波动影响。
- **算力报告不完整**：未提供具体训练时长、GPU小时数，难以评估计算成本。
- **文本数据依赖GPT-4o**：自动生成的质量和多样性可能有限，且可能引入偏见或噪声，未进行人工校验或对抗性筛选。
- **推理长度奖励的副作用**：最长推理bin中准确率下降，存在“过度思考”或输出截断问题，表明一味鼓励长链推理并非总是有益。
- **错误分析显示模型仍存在深层理解缺陷**：如对交通信号灯颜色误解、优先考虑非最安全措施等，表明推理鲁棒性仍有提升空间。
- **未探讨更大模型规模（如72B等）**：仅使用3B和7B，结论的缩放规律不明。
- **多模态接地能力未专门优化**：文本推理到视觉的迁移依赖视觉编码器本身的质量，未对视觉特征与推理结构做联合训练，可能限制最终效果。

（完）
