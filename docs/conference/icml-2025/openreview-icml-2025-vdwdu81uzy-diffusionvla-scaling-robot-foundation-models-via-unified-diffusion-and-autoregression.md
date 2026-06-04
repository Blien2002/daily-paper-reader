---
title: "DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression"
title_zh: DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型
authors: "Junjie Wen, Yichen Zhu, Minjie Zhu, Zhibin Tang, Jinming Li, Zhongyi Zhou, Xiaoyu Liu, Chaomin Shen, Yaxin Peng, Feifei Feng"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=VdwdU81Uzy"
tags: ["query:vla"]
score: 10.0
evidence: 直接提出扩散与自回归结合的VLA框架面向机器人基础模型
tldr: 针对现有自回归VLA模型动作生成不精确扩散策略缺乏推理能力的问题提出DiffusionVLA框架。该方法利用预训练VLM进行任务分解和解释并通过推理注入模块将自生成推理短语嵌入扩散策略。实验表明该框架在多个机器人操作基准上实现了高成功率高鲁棒性和可扩展性为机器人基础模型提供新思路。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1597, \"height\": 1235, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1754, \"height\": 780, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1569, \"height\": 563, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 769, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 861, \"height\": 343, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 858, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 853, \"height\": 451, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 844, \"height\": 224, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 858, \"height\": 507, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1747, \"height\": 897, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1759, \"height\": 890, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vdwdu81uzy/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 860, \"height\": 375, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1779, \"height\": 290, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 724, \"height\": 160, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 815, \"height\": 204, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1778, \"height\": 798, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 865, \"height\": 126, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 727, \"height\": 138, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 810, \"height\": 128, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 809, \"height\": 163, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 861, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 838, \"height\": 182, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vdwdu81uzy/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 894, \"height\": 561, \"label\": \"Table\"}]"
motivation: 自回归VLA模型动作生成不精确扩散策略缺乏推理能力。
method: 集成预训练VLM的自回归推理作为扩散策略的引导通过推理注入模块耦合两者。
result: 在多个机器人操作任务中实现了精确且鲁棒的动作生成显著优于单独方法。
conclusion: 统一扩散与自回归是构建可扩展机器人基础模型的可行方向。
---

## Abstract
In this paper, we present DiffusionVLA, a novel framework that integrates autoregressive reasoning with diffusion policies to address the limitations of existing methods: while autoregressive Vision-Language-Action (VLA) models lack precise and robust action generation, diffusion-based policies inherently lack reasoning capabilities. Central to our approach is autoregressive reasoning — a task decomposition and explanation process enabled by a pre-trained VLM — to guide diffusion-based action policies. To tightly couple reasoning with action generation, we introduce a reasoning injection module that directly embeds self-generated reasoning phrases into the policy learning process. The framework is simple, flexible, and efficient, enabling seamless deployment across diverse robotic platforms.

We conduct extensive experiments using multiple real robots to validate the effectiveness of DiVLA. Our tests include a challenging factory sorting task, where DiVLA successfully categorizes objects, including those not seen during training. The reasoning injection module enhances interpretability, enabling explicit failure diagnosis by visualizing the model’s decision process. Additionally, we test DiVLA on a zero-shot bin-picking task, achieving \textbf{63.7\% accuracy on 102 previously unseen objects}. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiVLA can follow novel instructions and retain conversational ability. Notably, DiVLA is data-efficient and fast at inference; our smallest DiVLA-2B runs 82Hz on a single A6000 GPU. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

现有机器人基础模型主要分为两类：一是基于自回归（Next-Token Prediction, NTP）的视觉-语言-动作（VLA）模型（如 RT-2、OpenVLA），它们将连续动作离散为 token 进行预测，但存在动作精度不足、推理速度慢的问题；二是基于扩散策略（Diffusion Policy）的模型，它们通过噪声-去噪过程生成动作序列，擅长处理多模态分布且生成速度快，但缺乏语言推理能力。本文的核心动机是：**能否将自回归模型的推理能力与扩散策略的动作生成鲁棒性统一到单一框架中**，从而构建兼具“推理”与“精准动作”的机器人基础模型。

## 2. 方法论

### 核心思想
提出 **DiffusionVLA（DiVLA）**，将预训练视觉语言模型（VLM）的自回归推理作为扩散策略的“引导信号”，通过**推理注入模块**将自生成的自然语言推理短语直接嵌入到扩散策略的学习过程中，使动作生成能够利用语义推理信息。

### 关键技术细节
- **整体架构**：
  - 视觉编码器：SigLIP 处理多视角图像，输出视觉 token。
  - 语言模型：Qwen2-VL（2B/8B/72B 参数），保持自回归能力。
  - 扩散策略：采用标准 Diffusion Policy (Chi et al., 2023) 设计，输出动作序列。
  - 投影层：将 VLM 输出的 action tokens 通过两层 MLP + LayerNorm 映射到扩散模型维度。
- **推理注入模块**：
  - 将 VLM 推理阶段生成的“推理 token”的最终嵌入，通过 **Feature-wise Linear Modulation (FiLM)** 注入到扩散策略网络的各层中，实现“条件化”动作生成。
  - 该模块仅作为辅助增强，不主导主决策流，保持效率。
- **训练目标**：
  - 联合损失：\( L = L_{\text{diff}} + \alpha L_{\text{ntp}} \)，其中 \( \alpha = 10 \) 以平衡扩散损失与自回归推理损失的量级。
- **预训练数据**：
  - DiVLA-2B/7B：使用 Droid 数据集（仅含动作和观测，缺乏语言推理）。
  - 使用 GPT-4o 自动为 Droid 数据生成“推理文本”（如“我要抓蓝色玩具车”），使数据包含推理信号。
  - DiVLA-72B：额外使用 OXE 数据集（25 倍于 Droid）联合预训练。
- **微调**：使用 LoRA 微调 VLM 部分，冻结视觉编码器，学习率 2e-5。

## 3. 实验设计

### 数据集与场景
- **预训练**：Droid 数据集（约 39K 轨迹）、OXE 数据集（约 970K 轨迹）。
- **微调任务**（全部真实机器人）：
  - **多任务学习**（Franka 机器人）：5 个任务（物体选择、翻转锅、将方块放入盒子、将杯子放在盘子上、将方块放入指定颜色盒子），总计 580 条轨迹。
  - **工厂分拣**（Franka 机器人）：将玩具车、针织手套、毛绒玩具、内六角扳手四类物品分拣到对应区域，500 条轨迹。评估设置包括：仅见过物体、混合见过+未见物体、杂乱场景。
  - **零样本拣货**（Franka 机器人）：102 个完全未见过物体，无训练数据，指令“将右侧面板上的任意物体移动到左侧篮子里”。
  - **双机械臂擦桌子**（AgileX 双机械臂）：将餐具放到左侧托盘，垃圾投入右侧垃圾箱，400 条轨迹，评估见过和未见物体。
  - **视角泛化**：工厂分拣任务中改变相机位置。
  - **新颖指令跟随**：执行未见过指令如“先捡西瓜，再捡蓝色纸垃圾”。

### 对比方法
- Diffusion Policy (DP)
- TinyVLA
- Octo
- OpenVLA-7B
- （部分实验还包括 π0 的类似设置）

### 评估指标
- 成功次数 / 成功率。
- 平均成功率（多任务或多场景）。

## 4. 资源与算力
论文中明确提到：
- 模型尺寸：2B、7B、72B 参数（对应 Qwen2-VL 的三种规模）。
- 训练：使用 LoRA 微调，学习率 2e-5，训练 20 个 epoch（针对 OpenVLA）。
- 推理硬件：单张 A6000 GPU。
- 推理速度：DiVLA-2B 达 82Hz，DiVLA-7B 达 42Hz，OpenVLA-7B 仅 5Hz。
- 未明确说明训练所需的 GPU 数量与训练时长，但提及预训练使用 Droid 和 OXE 数据，较大模型需更多数据。

## 5. 实验数量与充分性

### 实验组数
- 多任务学习：5 个任务，共 77 次试次（in-distribution）+ 45 次试次（视觉泛化）。
- 工厂分拣：4 个场景（简单/混合/杂乱/杂乱混合），每个 65~80 次试次。
- 零样本拣货：102 个物体，每个物体一次试次。
- 双机械臂擦桌子：2 个场景各 48 次试次。
- 视角泛化：5 次试次。
- 新颖指令：4 条指令，各 3 次试次。
- 消融实验：推理注入模块去除（多任务 5 任务）。
- 模型缩放实验：2B/7B/72B 在分拣和零样本任务上对比。

### 充分性评价
- **充分**：覆盖多种机器人平台（Franka 单臂、AgileX 双臂）、多种任务难度（简单/杂乱/零样本/新颖指令）、多种泛化维度（视觉变化、视角、新物体、新指令、新形态）。
- **客观公平**：对比了当前 SOTA 方法（DP、Octo、OpenVLA、TinyVLA），且使用相同训练设置（如扩展 OpenVLA 到三视角以公平比较）。消融研究验证了推理注入模块的必要性。
- **局限性**：工厂分拣任务中仅测试 4 类物品；零样本任务中物体数量有限（102 个）；未包含仿真实验对比；未与其他扩散+推理框架（如 HybridVLA）直接对比（当时可能未发表）。

## 6. 主要结论与发现

1. **统一框架有效**：结合自回归推理与扩散动作生成，在多个真实机器人任务上超越纯自回归或纯扩散方法。
2. **推理注入提升泛化**：推理模块使模型能类比新物体（如螺丝刀被归为内六角扳手），提升零样本场景成功率（63.7% vs 第二名 OpenVLA 28.4%）。
3. **可解释性**：可输出自然语言推理短语解释机器人的决策过程，有助于故障诊断。
4. **速度快**：DiVLA-2B 在 A6000 上达 82Hz，满足实时性要求；DiVLA-7B 42Hz，比同尺寸 OpenVLA 快 8 倍。
5. **可扩展性**：模型从 2B 到 72B，性能持续提升（分拣成功率 66.2% → 74.9% → 82.4%；零样本拣货 63.7% → 66.7% → 75.9%）。
6. **鲁棒性**：对视觉干扰（背景变化、杂乱、光照）具有较强抵抗力，且能适应新机器人形态（双机械臂）。
7. **保留对话能力**：即使未专门训练，仍可完成 VQA 任务。

## 7. 优点

- **方法论创新**：首次将自回归推理与扩散策略**紧密耦合**，而非简单拼接；推理注入模块（FiLM）设计简单有效。
- **数据高效**：仅使用 39K 轨迹（Droid）预训练即可达到超越 OpenVLA（970K 轨迹）的性能，微调数据量也较小。
- **推理速度极快**：通过 vLLM 框架优化，实现在单卡上 82Hz 的控制频率，适合真实机器人部署。
- **泛化能力突出**：零样本超过 60% 成功率，且对未见物体、新视角、新指令、新形态均表现良好。
- **可解释性强**：生成的推理文本可揭示模型内部决策过程，有助于调试和理解。
- **开源友好**：计划开放代码和数据（open-source）。

## 8. 不足与局限

- **实验覆盖有限**：未进行仿真实验，完全依赖真实机器人，难以大规模重复；任务数量相对较少（5 个多任务 + 分拣 + 擦桌子）。
- **零样本任务定义不严格**：零样本拣货的指令是“移动任意物体”，并非严格的任务泛化（如按类别分拣未见物体）。
- **缺乏与其他扩散-推理联合方法的对比**：论文发表时可能尚无同类方法，但后续可能已有 HybridVLA 等，本文未讨论。
- **推理模块的额外开销未量化**：文中未测量注入模块带来的计算增量，虽然速度已经很快，但消融实验仅显示性能提升。
- **预训练数据中推理文本来自 GPT-4o**：可能引入噪声或偏差，且该过程依赖外部大模型，可复现性需进一步验证。
- **模型缩放实验不完整**：仅测试了 2B/7B/72B 三个点，未给出完整 scaling law 曲线。
- **对低精度量化的敏感性**：文中提到 8-bit/4-bit 量化时性能下降显著，说明当前 VLA 模型对量化不够鲁棒。
- **新颖指令实验规模小**：仅 4 条指令，每指令 3 次试次，统计显著性不足。

（完）
