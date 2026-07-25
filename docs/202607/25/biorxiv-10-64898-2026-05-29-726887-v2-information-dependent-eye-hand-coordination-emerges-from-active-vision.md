---
title: Information-dependent eye-hand coordination emerges from active vision
title_zh: 基于信息依赖的眼手协调：来自主动视觉的涌现
authors: "Zhao, J., VERDEL, D., Tan, Y., Burdet, E."
date: 2026-07-17
pdf: "https://www.biorxiv.org/content/10.64898/2026.05.29.726887v2.full.pdf"
tags: ["query:vla"]
score: 6.0
evidence: 主动视觉驱动眼手协调的具身智能原理
tldr: 人类在日常活动中通过眼动提取视觉信息来协调手部运动，行为研究揭示了扫视-追踪模式但缺乏统一原理。本文提出双随机模型预测控制框架，将眼动建模为连续优化过程以最小化任务不确定性并构建手部运动内部模型。模型自然涌现扫视-追踪模式，并准确预测了实验中眼手运动特征，同时眼动模式随信息上下文自适应。该工作为理解眼手协调的实时调节提供了计算原则，对机器人辅助和主动感知有重要启示。
source: biorxiv
selection_source: fresh_fetch
figures_json: "[{\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1286, \"height\": 731, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1399, \"height\": 1076, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1248, \"height\": 1106, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1169, \"height\": 1563, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1175, \"height\": 1138, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 687, \"height\": 341, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1472, \"height\": 560, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1828, \"height\": 802, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1833, \"height\": 799, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1829, \"height\": 800, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1831, \"height\": 801, \"label\": \"Figure\"}, {\"url\": \"assets/figures/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1832, \"height\": 803, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/biorxiv/biorxiv-10-64898-2026-05-29-726887-v2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1568, \"height\": 2216, \"label\": \"Table\"}]"
motivation: 现有眼手协调研究缺乏统一计算原理，无法解释连续任务中扫视-追踪模式的涌现机制。
method: 提出主动视觉的双随机模型预测控制，通过优化眼动减少任务不确定性并构建手部规划模型。
result: 模型自然产生扫视-追踪模式，准确预测实验眼手特征；眼动模式自适应信息密度和难度。
conclusion: 提供了理解连续眼手协调的计算框架，为机器人辅助和主动感知应用开辟新视角。
---

## 摘要
在日常活动中，人类依赖视觉信息来规划手部运动，因此通过眼睛注视提取任务相关信息成为运动控制的关键。行为学研究表明，存在特征性的扫视-追踪模式，这些模式可能受共享神经回路调控，能够有效降低任务相关的不确定性。

然而，目前仍缺乏一个统一的计算原理解释这些模式如何在连续任务（如阅读或驾驶）中涌现。本文提出了一种主动视觉的双随机模型预测控制框架，其中眼睛运动被连续控制以最小化任务相关的不确定性，并构建用于手部运动规划的内部模型。通过操控未来视觉信息的数量、密度和难度，我们展示了眼睛运动模式如何适应信息上下文，同时保持不变的提取视界。该模型自然地涌现出扫视-追踪模式，并准确预测了实验观察到的眼动和手部运动特征。这些结果为理解人类眼动的连续调节提供了原理性框架，并为机器人辅助和主动感知应用开辟了新视角。

## Abstract
In daily activities, humans rely on visual information to plan hand movements, making the extraction of task-relevant information through eye gaze a key aspect of motor control. Behavioral studies have revealed characteristic saccade-pursuit patterns, likely governed by shared neural circuits, which enable an efficient reduction of task-related uncertainty.

However, a unifying computational principle explaining the emergence of these patterns in continuous tasks such as reading or driving is still lacking. Here we propose a dual stochastic model predictive control formulation of active vision, in which eye movements are continuously controlled to minimize task-relevant uncertainty and build an internal model used for hand movement planning. Through experiments manipulating the amount, density, and difficulty of future visual information, we show how eye movement patterns adapt to the information context while maintaining an invariant extraction horizon. A saccade-pursuit pattern naturally emerges from the model, which accurately predicts both eye and hand movement features observed in experiments. These results provide a principled framework for understanding the continuous regulation of human eye movements and open new perspectives for applications in robotic assistance and active perception.