---
title: "CogVLA: Cognition-Aligned Vision-Language-Action Models via Instruction-Driven Routing & Sparsification"
title_zh: CogVLA：通过指令驱动路由与稀疏化实现认知对齐的视觉-语言-动作模型
authors: "Wei Li, Renshan Zhang, Rui Shao, Jie He, Liqiang Nie"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=Fg9HufTI0K"
tags: ["query:vla"]
score: 8.0
evidence: 通过指令驱动的路由与稀疏化实现高效VLA模型
tldr: 现有VLA模型基于预训练VLM，后训练计算开销大，部署受限。本文提出CogVLA，通过指令驱动的模块路由和动态稀疏化，在保持语义耦合的前提下裁剪冗余计算。实验表明CogVLA在不牺牲性能的情况下显著降低推理成本，为VLA模型的轻量化部署提供了可行方案。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1432, \"height\": 838, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1448, \"height\": 584, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1443, \"height\": 768, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1443, \"height\": 952, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1445, \"height\": 1034, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1447, \"height\": 646, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1446, \"height\": 1445, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fg9hufti0k/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1446, \"height\": 2146, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1428, \"height\": 594, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1461, \"height\": 345, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1446, \"height\": 327, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 813, \"height\": 490, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 596, \"height\": 264, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 595, \"height\": 129, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1356, \"height\": 309, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1356, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fg9hufti0k/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 851, \"height\": 260, \"label\": \"Table\"}]"
motivation: VLA模型计算开销大，现有稀疏化策略忽略跨模态耦合。
method: 提出指令驱动的路由和稀疏化机制，根据指令动态选择任务相关子网络，并保持端到端连贯性。
result: "在多个操纵任务上，CogVLA在同等性能下计算量减少约40%。"
conclusion: 指令驱动的稀疏化可高效压缩VLA模型，促进实际部署。
---

## Abstract
Recent Vision-Language-Action (VLA) models built on pre-trained Vision-Language Models (VLMs) require extensive post-training, resulting in high computational overhead that limits scalability and deployment. Existing sparsification strategies—such as Mixture-of-Depths, layer skipping, and early exit—fall short by neglecting the semantic coupling across vision-language-action modalities, and focusing narrowly on intra-LLM computation while overlooking end-to-end coherence from perception to control. To address these challenges, we propose **CogVLA**, a Cognition-Aligned Vision-Language-Action framework that leverages instruction-driven routing and sparsification to improve both efficiency and performance. CogVLA draws inspiration from human multimodal coordination and introduces a 3-stage progressive architecture. 1) **Encoder-FiLM based Aggregation Routing (EFA-Routing)** injects instruction information into the vision encoder to selectively aggregate and compress dual-stream visual tokens, forming a instruction-aware latent representation. 2) Building upon this compact visual encoding, **LLM-FiLM based Pruning Routing (LFP-Routing)** introduces action intent into the language model by pruning instruction-irrelevant visually grounded tokens, thereby achieving token-level sparsity. 3) To ensure that compressed perception inputs can still support accurate and coherent action generation, we introduce **V‑L‑A Coupled Attention (CAtten)**, which combines causal vision-language attention with bidirectional action parallel decoding.
Extensive experiments on the LIBERO benchmark and real-world robotic tasks demonstrate that CogVLA achieves state-of-the-art performance with success rates of 97.4\% and 70.0\%, respectively, while reducing training costs by 2.5$\times$ and decreasing inference latency by 2.8$\times$ compared to OpenVLA.

---

## 论文详细总结（自动生成）

## 一、论文的核心问题与整体含义（研究动机和背景）

- **问题**：现有的 Vision-Language-Action (VLA) 模型（如 OpenVLA、π0 等）基于大规模预训练视觉语言模型（VLM），在微调时计算开销极大（例如在 LIBERO 单任务上微调 7B 模型需超过 600 GPU 小时）。现有的稀疏化策略（如 Mixture-of-Depths、层级跳过、早停等）主要关注语言模型内部的运算优化，忽略了视觉、语言、动作模态间的语义耦合，导致端到端的语义退化：视觉压缩丢失任务相关细节、LLM 内 Token 跳过破坏引用所需的上下文连贯性、动作生成缺乏多模态状态转换的因果推理。
- **核心目标**：提出一个认知对齐的 VLA 框架，通过指令驱动的路由与稀疏化，在保持跨模态语义一致性的同时大幅降低计算成本，实现高效且高性能的机器人操控。

## 二、方法论：核心思想、关键技术细节

- **核心思想**：受人类多模态协同机制的启发（视觉注意力系统 VAS、辅助运动区 SMA、前运动皮层 PMC），设计三阶段渐进式架构，实现“感知聚焦→语义过滤→动作规划”的仿生流程。
- **关键技术细节**：
  1. **Encoder-FiLM 聚合路由 (EFA-Routing)**：
     - 对应人类 VAS，在视觉编码器中利用 FiLM（Feature-wise Linear Modulation）根据指令动态调制视觉特征，进行帧内聚合（将图像 Token 缩至原始 25%），并通过指令条件路由门控融合两个异构编码器（SigLIP 和 DINOv2）的输出，得到任务感知的紧凑视觉表示。
     - 公式：`v_agg = α * v_SigLIP_agg + (1-α) * v_DINOv2_agg`，其中 α 由指令经 MLP 预测。
  2. **LLM-FiLM 剪枝路由 (LFP-Routing)**：
     - 对应人类 SMA，在大语言模型层前引入指令条件 FiLM，对视觉 Token 进行语义相关性评分，根据移位余弦调度动态保留比例（约 50% 剪枝），丢弃指令不相关的 Token，实现 Token 级稀疏。
     - 公式：`R_j^l = MLP(Z_j^l)`，仅保留权重超过 β 百分位阈值的 Token。
  3. **V-L-A 耦合注意力 (CAtten)**：
     - 对应人类 PMC，设计统一混合注意力掩码，在视觉-语言段采用因果注意力保持时序推理，在动作段采用双向注意力实现并行解码（一个前向过程同时生成 K 步动作），确保压缩后的多模态表示仍能产生准确且连贯的动作序列。
     - 掩码矩阵：上半部分为因果 VL 注意，下半部分为双向动作注意，VL 与动作间为掩码隔绝依赖。

## 三、实验设计

- **模拟基准**：LIBERO benchmark，包含四个任务套件（Spatial、Object、Goal、Long），每套 10 个任务，各有 50 个人类遥操作演示。指令平均长度 10.48 词，强调语言理解与多步推理。
- **真实世界实验**：Cobot Agilex ALOHA 平台，三个长时程任务（物体放置、抽屉操作、T 恤折叠），共 120 次演示，引入空间与语义变化。
- **对比方法**：Diffusion Policy、Octo、OpenVLA、π0、π0-Fast、π0.5-KI、OpenVLA-OFT、SpatialVLA、PD-VLA、STAR、Dita、CoT-VLA 等 10+ 个方法（具体见表 1、表 2 等）。
- **评估指标**：任务成功率（SR）、推理时间、吞吐量、FLOPs、训练成本。

## 四、资源与算力

- **硬件**：4 块 NVIDIA A800 GPU（80GB）。
- **训练设置**：
  - LIBERO 微调：使用 LoRA（rank=32，α=64），batch size 64，学习率 5e-4，共 60K 步。
  - 真实世界微调：chunk size K=25，batch size 32，共 80K 步。
- **效率对比**：CogVLA 训练成本为 4.7 小时 / 10K 步，相比 OpenVLA 的 11.7 小时 / 10K 步减少约 2.5 倍；推理时间 0.091 秒（比 OpenVLA 快 2.8 倍），FLOPs 2.72T（减少 3.1 倍）。

## 五、实验数量与充分性

- **实验组别**：
  - 主实验：4 个 LIBERO 套件 × 10 任务（表 1）、3 个真实世界任务 × 10 次/任务（表 2）、效率对比（表 3）。
  - 消融实验：模块组件消融（表 4）、稀疏率分配（表 5）、与其他压缩方法对比（表 6）、多种子稳定性（附录表 7）、扩展真实任务（附录表 8）、额外稀疏配置（附录表 9）。
  - 定性分析：注意力图可视化（图 4、7）、操作流程可视化（图 5、6、8）。
- **充分性与公平性**：
  - 与 10+ 个方法在相同设置下对比，包括开源复现结果（标记†）。
  - 多种子（3 种子）的标准差报告（表 7），显示稳定性。
  - 消融设计针对每个模块及稀疏比例，系统分析了不同配置对性能-效率平衡的影响。
  - 实验覆盖模拟和真实场景，且包含长时程、多属性、空间推理等多种挑战任务。整体实验设计充分、客观、公平。

## 六、论文的主要结论与发现

- CogVLA 在 LIBERO 上达到 97.4% 平均成功率，排名第一；在真实世界任务上达到 70.0% 成功率，均显著优于现有方法。
- 在保持甚至提升性能的同时，训练成本降低 2.5 倍、推理延迟降低 2.8 倍、FLOPs 减少 3.1 倍。
- 三阶段渐进式设计（EFA-Routing → LFP-Routing → CAtten）协同工作，缺一不可（消融实验验证）。
- 指令驱动稀疏化比固定式压缩（如 FastV、SliME）更有效（表 6）。
- 不对称稀疏率分配（Stage1 更激进，Stage2 更精细）能获得最佳性能-效率权衡（表 5）。

## 七、优点

- **仿生设计**：借鉴人类 VAS、SMA、PMC 的协同机制，三阶段架构具有认知可解释性。
- **指令驱动的联合稀疏化**：首次在视觉编码器和 LLM 内同时根据指令进行动态 Token 压缩与剪枝，保持跨模态语义一致性。
- **高效的 V-L-A 耦合注意力**：结合因果与双向注意，实现动作并行解码，同时确保视觉-语言时序推理。
- **性能与效率双优**：在多种任务上达到 SOTA，同时大幅降低计算与时间开销，有利于实际部署。
- **广泛实验验证**：覆盖模拟与真实场景，包括多步、软体、双/单臂任务，消融全面，结果稳健。

## 八、不足与局限

- **固定稀疏策略**：当前使用预定义的稀疏比例（余弦调度），未实现任务自适应调节，可能不适用于指令复杂度剧烈变化的场景。
- **OOD 泛化未充分验证**：仅限于 LIBERO 和 ALOHA 环境，对未见过的指令类型或全新操控类别的泛化能力尚不明确。
- **缺乏多模态反馈**：仅利用视觉和语言信息，未集成触觉、力觉等反馈，限制了精细操控的应用。
- **训练数据规模有限**：真实世界数据量较小（每个任务约 30–45 条演示），可能影响鲁棒性。
- **潜在风险**：模型可能误读模糊指令或在复杂环境中产生不安全行为，且训练数据偏差可能导致歧视性行为，需配合安全防护机制。

（完）
