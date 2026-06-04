---
title: "ChatVLA-2: Vision-Language-Action Model with Open-World Reasoning"
title_zh: ChatVLA-2：具有开放世界推理能力的视觉-语言-行动模型
authors: "Zhongyi Zhou, Yichen Zhu, Xiaoyu Liu, Zhibin Tang, Junjie Wen, Yaxin Peng, Chaomin Shen, Yi Xu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=1lyKflUOhp"
tags: ["query:vla"]
score: 10.0
evidence: ChatVLA-2是一个具有开放世界推理能力的新型VLA模型
tldr: 现有端到端VLA模型在适应机器人任务时会丢失VLM的开放世界推理能力。ChatVLA-2通过保留VLM的核心能力并引入推理跟随机制，使机器人能处理未见过的物体和复杂指令。在多种操作环境中，该方法在保持泛化性的同时实现了高成功率，推动了VLA模型迈向通用机器人智能。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-1lykfluohp/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1426, \"height\": 353, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1lykfluohp/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1429, \"height\": 435, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1lykfluohp/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1307, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1lykfluohp/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1417, \"height\": 683, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-1lykfluohp/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1433, \"height\": 647, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1444, \"height\": 390, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 816, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1443, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 643, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1443, \"height\": 192, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 731, \"height\": 210, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-1lykfluohp/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 702, \"height\": 210, \"label\": \"Table\"}]"
motivation: 现有VLA模型在微调时丧失VLM的开放世界推理能力，限制泛化。
method: 提出ChatVLA-2架构，通过保留VLM核心知识并引入推理跟随模块实现动作生成。
result: 在多个机器人任务上，ChatVLA-2显著提升泛化性能，成功处理未见物体和指令。
conclusion: 保持VLM能力是构建通用VLA模型的关键。
---

## Abstract
Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) **Open-world reasoning** - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, capable of solving math problems, possessing visual-spatial intelligence, 2) **Reasoning following** – effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce **ChatVLA-2**, a novel mixture-of-expert VLA model coupled with a specialized three-stage training pipeline designed to preserve the VLM’s original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and $\pi_0$. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.

---

## 论文详细总结（自动生成）

# 论文《ChatVLA-2：具有开放世界推理能力的视觉-语言-行动模型》详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有端到端视觉-语言-行动（VLA）模型虽然利用了强大的预训练视觉-语言模型（VLM）作为主干，但在针对具体机器人任务微调时，会严重丢失VLM原有的开放世界推理、数学计算、OCR、空间理解等核心能力。这导致机器人无法处理训练数据中未出现过的场景（例如未见过的数学方程、新物体、新方向指令），限制了VLA模型向通用机器人基础模型发展的潜力。
- **整体含义**：要实现真正可泛化的机器人基础模型，必须保留并且主动利用VLM的预训练知识，同时确保机器人动作能够忠实跟随其内部推理结果。本文提出的ChatVLA-2正是朝这一目标迈进的重要尝试。

## 2. 论文提出的方法论

### 核心思想
- **保留VLM能力**：通过动态混合专家（Dynamic MoE）架构解耦多模态理解与机器人控制这两种任务的冲突特征空间，同时保留共享的互益特征（如空间推理）。
- **推理跟随**：引入推理跟随增强模块，使动作专家能够基于VLM高层生成的开放世界推理结果来调整动作生成，确保动作与推理一致。

### 关键技术细节

1. **动态混合专家（Dynamic MoE）模块**：
   - 在VLM（Qwen2-VL）的LLM部分引入MoE，共8个专家，推理时动态选择前2个专家激活。
   - 专家分为两类：任务专用专家（多模态理解、机器人控制）和共享专家（捕捉互益特征）。
   - 路由器根据输入特征自适应选择专家，避免静态专家或共享专家破坏原始VLM结构（Qwen2-VL没有原生MoE支持）。

2. **推理跟随增强模块**：
   - 用推理token（来自VLM输出）替换原始观测嵌入的一部分。
   - 推理token经MLP投影后，与当前时间步嵌入合并，用于生成动作专家中后一半层的尺度和偏移参数。
   - 仅在动作专家的后一半层注入推理信息，避免干扰前一半层的动作生成稳定性。

3. **两阶段训练策略**：
   - **阶段一（联合训练）**：同时训练图像-文本数据（COCO、TextVQA、GQA等）和机器人任务数据（数学匹配游戏600条轨迹、玩具放置300条轨迹），使VLA模型获得开放世界推理与理解能力。图像-文本数据与机器人数据比例1:3。训练50k步，初始学习率2e-5，前3k步预热，余弦退火至2e-6。
   - **阶段二（推理跟随训练）**：冻结整个VLM，仅训练动作专家。使模型学会将上层生成的推理结果转化为具体的机器人动作，增强对未见推理场景的适应能力。训练细节同阶段一。

## 3. 实验设计

### 数据集 / 场景
1. **数学匹配游戏（数学推理+OCR）**：
   - 白板上写有数学方程，机器人需从桌上的数字卡片中选出正确答案并放置到白板上。
   - 图像-文本数据：COCO（~32k）、TextVQA（~20k）、GQA（~54k），以及机器人相关的空间推理数据（RoboPoint ~2k、真实场景5k）。
   - 机器人数据：收集600条轨迹，含推理注释（采用π0.5和DexVLA类似的子推理模板，并用GPT-4o增强）。

2. **玩具放置任务（空间推理）**：
   - 指令：“拿起[物体]并放在[目标]的[方向]”，方向包括左、右、前、后、顶部、底部。
   - 训练集中物体和方向均可见，开放世界测试中使用全新物体和方向。
   - 机器人数据：300条轨迹。

### Benchmark
- 主要评估指标：
  - **数学匹配游戏**：OCR评分（4分制，含数字识别、符号识别、卡片位置等）、数学推理评分（2分制，含正确答案和正确选卡）、操作成功率。
  - **玩具放置**：物体识别得分、空间推理得分、操作成功率。
- 同时评估了12个多模态理解基准（TextVQA、DocVQA、ChartQA等）。

### 对比方法
- 基线方法：Octo、Diffusion Policy、OpenVLA、GR00T N1、DexVLA、ChatVLA、π0。
- 消融实验：动态MoE vs 静态MoE+动态MoE、共享MoE+动态MoE、3B/7B稠密模型；两阶段训练 vs 单阶段；专家数量与层注入位置等。

## 4. 资源与算力

- **GPU**：8块NVIDIA H800 GPU（每块80GB）。
- **训练时长**：总计340 GPU小时（阶段一约？文中未分列，总训练步数50k+？实际两阶段共约65k步？从文本看：阶段一50k步，阶段二50k步，但说明“总训练成本340 GPU小时”）。
- **优化器**：AdamW，混合精度FP16。

## 5. 实验数量与充分性

- **主要实验数量**：
  - 数学匹配游戏：开放世界与域内测试（共52次测试？）。
  - 玩具放置：域内67次测试，开放世界156次测试。
  - 多模态理解基准：12项基准评估。
  - 消融实验：MoE架构对比（5种配置）、两阶段训练对比（3种配置）、专家数量（3种）、推理注入层位置（3种）、动作专家设计等。
- **充分性与客观性**：实验覆盖了机器人操作、OCR、数学推理、空间推理、多模态理解等多个维度，对比了当前主流VLA和模仿学习方法，且消融实验设计合理。但实验仅在桌面上进行（Franka + ARX-R5双机械臂），未涉及移动操作或长时域任务；开放世界测试规模有限（如数学方程仅考虑加法减法等简单运算）。总体上实验较充分，但泛化到更复杂场景尚需验证。

## 6. 论文的主要结论与发现

1. **ChatVLA-2在开放世界场景下显著优于现有方法**：数学匹配游戏中OCR评分3.58/4、数学推理1.73/2、操作成功率82.7%；玩具放置中物体识别0.94/1、空间推理0.88/1、操作成功率81.4%。相比之下，其他方法（如DexVLA、ChatVLA）在开放世界下几乎完全失败。
2. **动态MoE是关键**：相比静态/共享MoE或稠密模型，动态MoE能有效保留VLM预训练知识并解耦冲突特征。稠密7B模型在未见方程上完全失败（OCR 0.08，数学0）。
3. **两阶段训练不可或缺**：缺少阶段二（推理跟随训练）时开放世界成功率降至23%；缺少阶段一（联合训练）时开放世界推理能力近乎为零。
4. **VLA模型可以内在地利用VLM预训练知识**，无需显式训练即可完成数学、OCR、空间推理等任务，实现从零到有效泛化的跨越。
5. 在多模态理解基准上（11/12项提升），ChatVLA-2保持了甚至增强了VLM的理解能力。

## 7. 优点

1. **创新性架构**：首次将动态MoE引入VLA模型，并设计推理跟随模块，有效保留VLM知识。
2. **巧妙的训练策略**：两阶段训练（先联合学习，后冻结VLM只训练动作专家）确保了知识保持与推理跟随。
3. **实验设计有挑战性**：直接测试开放世界新方程、新物体、新方向，结果令人信服。
4. **开源基础**：论文承诺开源模型与部分数据（受政策限制无法公开机器人数据，但架构和训练细节清晰）。
5. **跨领域验证**：不仅验证机器人操作，还在12个多模态理解基准上证明理解能力未下降。
6. **方法简洁有效**：没有引入复杂的显式规划器或外部模块，而是通过端到端模型自身实现泛化。

## 8. 不足与局限

1. **任务场景有限**：仅测试了桌面拾放任务（数学卡片、玩具放置），没有涉及移动操作、长时域任务、重操作或动态环境。
2. **开放世界测试规模偏小**：数学方程类型单一（加、减、乘、除），玩具放置中物体种类和方向组合有限。更多样化的测试（如复杂多步操作、自然语言复杂指令）有待验证。
3. **VLM知识保留不完整**：论文承认“无法完全保留VLM的预训练知识”，微调过程中仍会有能力损失。
4. **计算资源需求较高**：340 GPU小时训练成本可能限制中小实验室复现。
5. **依赖手工数据收集**：机器人数据（600+300条轨迹）通过遥操作收集，若扩展到大规模任务数据成本高。
6. **未讨论失败案例分析**：没有深入分析开放世界下为何部分任务失败（如数学推理得分未饱和）。
7. **缺乏与显式规划方法的对比**：未与“VLM+低层控制器”这种层次化方法比较，后者也可能有类似的开放世界能力。
8. **伦理与安全讨论缺失**：论文未涉及机器人安全、误操作风险等实际部署问题。

（完）
