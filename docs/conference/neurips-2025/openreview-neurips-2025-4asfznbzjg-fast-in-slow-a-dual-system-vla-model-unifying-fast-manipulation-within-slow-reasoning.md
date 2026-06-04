---
title: "Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning"
title_zh: 快慢合一：统一快速操纵与慢速推理的双系统VLA模型
authors: "Hao Chen, Jiaming Liu, Chenyang Gu, Zhuoyang Liu, Renrui Zhang, Xiaoqi Li, Xiao He, Yandong Guo, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=4asFznbzJg"
tags: ["query:vla"]
score: 9.0
evidence: 统一快速操纵与慢速推理的双系统VLA模型
tldr: 机器人操纵面临泛化性和执行效率的双重挑战。现有双系统方法将VLM与动作模块分离，限制了知识共享。本文提出Fast-in-Slow（FiS），一种统一的双系统VLA模型，将慢速推理与快速动作生成融合在单一框架中，使动作模块充分共享VLM预训练知识，在提升泛化性的同时保持实时控制。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1432, \"height\": 486, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1440, \"height\": 619, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1450, \"height\": 307, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1433, \"height\": 386, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1360, \"height\": 328, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1403, \"height\": 178, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1432, \"height\": 559, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1423, \"height\": 401, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1403, \"height\": 1859, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1406, \"height\": 1866, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1443, \"height\": 894, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1441, \"height\": 905, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-4asfznbzjg/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1431, \"height\": 932, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1451, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1445, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1360, \"height\": 328, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 722, \"height\": 1560, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1070, \"height\": 419, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1437, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1440, \"height\": 152, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1449, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1448, \"height\": 204, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1446, \"height\": 203, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1446, \"height\": 202, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-4asfznbzjg/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1448, \"height\": 203, \"label\": \"Table\"}]"
motivation: 现有双系统VLA模型分离VLM与动作模块，无法充分利用预训练知识。
method: 提出统一双系统框架，将推理与动作生成融合，共享参数。
result: 同时提升泛化性和执行效率，实现实时控制。
conclusion: 统一双系统设计有效解决了泛化与效率的矛盾。
---

## Abstract
Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation. While recent foundation policies benefit from the common-sense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency. To mitigate this dilemma, dual-system approaches have been proposed to leverage a VLM-based System 2 module for handling high-level decision-making, and a separate System 1 action module for ensuring real-time control. However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2. In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing parameters. This innovative paradigm not only enables high-frequency execution in System 1, but also facilitates coordination between multimodal reasoning and execution components within a single foundation model of System 2. Given their fundamentally distinct roles within FiS-VLA, we design the two systems to incorporate heterogeneous modality inputs alongside asynchronous operating frequencies, enabling both fast and precise manipulation. To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2’s contextual understanding to provide stable latent conditions for System 1. For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in real-world tasks in terms of average success rate, while achieving a 117.7 Hz control frequency with action chunk set to eight. Project web page: https://fast-in-slow.github.io.

---

## 论文详细总结（自动生成）

# Fast-in-Slow：统一快速操纵与慢速推理的双系统VLA模型 —— 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：机器人操纵学习面临两个关键挑战：**泛化策略**（能否适应新物体、新场景）和**执行效率**（能否满足实时闭环控制）。现有的视觉-语言-动作（VLA）模型利用互联网规模的预训练视觉-语言模型（VLM）获得了常识推理能力，但受限于亿级参数和自回归动作生成，运行频率低（通常<10 Hz），难以用于实时控制。
- **已有解决方案的不足**：受卡尼曼双系统理论启发，一些工作将VLM作为System 2（慢速、逻辑推理）处理高层决策，另加一个轻量级的System 1（快速、直觉执行）模块保证实时控制。但这些方法将两个系统保持为分离模型，System 1仅依赖System 2提取的特征，无法充分利用VLM中丰富的预训练知识，导致性能受限。
- **论文核心思想**：提出“快在慢中”（Fast-in-Slow, FiS）的统一双系统VLA模型，将System 1执行模块**嵌入到**System 2的VLM内部（通过共享最后几层Transformer块），从而既保持System 2的推理能力，又使System 1继承VLM的预训练知识，同时支持高频执行。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 2.1 核心架构
- **整体框架**：FiS-VLA基于Prismatic VLM（SigLIP + DINOv2作为视觉编码器，LLaMA2-7B作为语言模型）。保留完整的32层LLM模块用于System 2推理，将最后若干（默认2层）Transformer块**重用**为System 1高频执行模块。System 1不额外插入独立策略网络，而是继承System 2的参数和知识。
- **异构模态输入**：
  - System 2（低频率）接收2D图像和语言指令，进行高层语义理解。
  - System 1（高频率）接收实时2D图像、机器人状态（proprioception）、3D点云（通过快速3D tokenizer + 共享视觉编码器处理），以及System 2周期性更新的潜在特征，用于生成动作。
- **异步频率设计**：System 2与System 1的工作频率比为1:n（默认1:4）。System 2每隔n步输出一次潜在条件，System 1每步执行动作。通过训练时的异步采样实现。

### 2.2 训练策略
- **双感知协同训练（Dual-aware Co-training Strategy）**：
  - **System 1**：采用扩散模型（Diffusion）学习连续动作生成。损失函数为去噪均方误差（式1）：$\mathcal{L}_{\text{fast}} = \mathbb{E}[\|\eta - \pi_{\theta_f}(\tilde{a}_\tau, c, \tau)\|^2]$，其中$\tilde{a}_\tau$是加噪动作，c为条件（包含System 2潜在特征和System 1高频输入）。
  - **System 2**：保持自回归下一个词预测损失（式2）：$\mathcal{L}_{\text{slow}} = -\sum_i \log P(\hat{a}_i|\text{context},\theta)$，可使用离散动作或语言计划作为监督信号。
  - 总损失：$\mathcal{L}_{\text{FiS-VLA}} = \mathcal{L}_{\text{fast}} + \mathcal{L}_{\text{slow}}$，联合优化整个模型。
- **预训练与微调**：先在包含86万+轨迹的跨具身数据集（Open X-Embodiment, DROID, ROBOMIND等）上预训练5个epoch（仅使用单视图图像）；然后在特定任务数据（RLBench 100条/任务，自采集真实数据100条/任务）上微调。

## 3. 实验设计

### 3.1 模拟实验（Simulation Experiment）
- **平台**：CoppeliaSim + RLBench benchmark，Franka Panda机器人，单臂7-DoF末端执行器控制。
- **任务**：10种操纵任务（Close box, Close laptop, Toilet seat down, Sweep to dustpan, Close fridge, Phone on base, Take umbrella out, Frame off hanger, Wine at rack, Water plants）。
- **对比方法**：ManipLLM, OpenVLA, π0, CogACT（均为SOTA VLA模型）。其中π0和CogACT是双系统方法但频率同步。
- **评价指标**：每个任务20次rollout，重复3次，报告平均成功率及方差。
- **结果**：FiS-VLA平均成功率69%，超过CogACT（61%）和π0（55%）；控制频率21.9 Hz（action chunk=1），远超CogACT（9.8 Hz）和π0（13.8 Hz）。在8/10个任务上最优。

### 3.2 真实世界实验（Real-World Experiment）
- **机器人平台**：
  - **Agilex**双臂机器人（6-DoF/臂），使用末端执行器位姿控制，三视图（外部+左右手腕）。
  - **AlphaBot**双臂机器人（7-DoF/臂），使用关节位置控制，三视图。
- **任务**：每个平台4个任务（共8个）。Agilex：Pick and place, Lift ball, Place bottles at rack, Wipe blackboard。AlphaBot：Pick bowl and place object, Handover object and place, Pour water and move cup, Fold towel and place in bucket。
- **对比方法**：仅与π0对比（因为SOTA双系统模型为π0，且CogACT未提供真实世界权重）。
- **结果**：FiS-VLA在Agilex上平均68% vs π0 59%，在AlphaBot上平均74% vs π0 61%。在复杂任务（如Place bottles, Fold towel）上提升明显。

### 3.3 泛化实验（Generalization Experiment）
- **测试场景**：操纵未见物体、复杂背景、光照变化。
- **任务**：Place bottles at rack（Agilex）和Pick bowl and place object（AlphaBot）。
- **结果**：FiS-VLA性能下降幅度（-19%~-31%）显著小于π0（-27%~-46%），表明嵌入System 1到VLM中增强了泛化鲁棒性。

### 3.4 消融实验（Ablation Study）
在RLBench的10个任务上进行：
1. System 1共享块数量：1→2→4→8块，2块最佳（69% vs 49%～66%）。
2. System 1输入模态：全模态（图像+点云+状态）最优69%；去除点云降至61%；去除图像和状态降至44%；仅用潜在特征降至22%。
3. 频率比：1:4最佳（69%），1:1（60%）、1:2（63%）、1:8（61%）。
4. 训练策略：去除$\mathcal{L}_{\text{slow}}$降至62%；加入语言计划监督可升至73%。
5. 动作块大小（action chunk）：1到8，成功率稳定（69%左右），控制频率可达117.7 Hz（chunk=8）。
6. 输入变体（不同模态分配）：原设计最优（69%），其他变体略低（61%~68%）。
7. 参数共享有效性：对比复制最后几层作为独立System 1，本设计更优（69% vs 61%/59%）。
8. 小规模LLM（2.7B Phi-2）：平均成功率62%（7B版本69%），证明方法的通用性。

## 4. 资源与算力
- **预训练**：使用8张NVIDIA A800 GPU，混合精度训练，在860K轨迹数据上训练5个epoch。
- **微调**：模拟实验（RLBench 10任务×100轨迹）训练300 epoch，8张A800 GPU。
- **真实世界实验**：自采集数据（100演示/任务），训练设置与模拟类似。
- **推理**：单个NVIDIA 4090 GPU上，action chunk=1时21.9 Hz，chunk=8时117.7 Hz。

## 5. 实验数量与充分性
- **模拟**：10个任务，每任务20 rollout × 3次，方差报告充分。
- **真实**：8个任务（2个平台各4个），每任务20 rollout。
- **消融**：涵盖架构（块数、模态、频率比、训练策略、动作块大小、输入变体）共约6组消融，每组都在10个任务上测试。
- **泛化**：3种场景（物体、背景、光照），2个平台。
- **对比**：模拟对比4个SOTA，真实对比1个SOTA（π0）。对比方法均使用官方预训练权重并全微调，设置公平。
- **充分性**：实验覆盖全面，既有模拟又有真实，包含泛化测试和多组消融。但真实世界仅对比了π0，缺乏与CogACT等方法的直接对比（因未提供真实权重），可能存在偏差。另外，所有方法均采用20 rollout制，方差报告，可靠性较好。

## 6. 论文的主要结论与发现
1. 将System 1执行模块直接嵌入System 2的VLM内部（共享参数）比分离式双系统能更好利用预训练知识，提升成功率。
2. 异步频率设计（如1:4）在保证推理质量的同时大幅提升控制频率（可达117.7 Hz）。
3. System 1接收多模态输入（尤其3D点云）显著提升空间操纵精度。
4. 双感知协同训练（扩散+自回归）既维持System 2的推理能力又保证System 1的生成质量。
5. FiS-VLA在模拟和真实实验中均达到SOTA，并在泛化任务上表现稳健。

## 7. 优点
- **创新性**：提出了“Fast-in-Slow”的架构范式，将快速执行模块无缝融入慢速推理大模型中，而非额外附加，概念简洁且有效。
- **性能提升显著**：模拟+8%，真实+11%平均成功率，同时控制频率远超现有方法。
- **充分消融**：对各种设计维度（共享块数、模态、频率、损失函数、动作块）进行了系统分析，验证了每个组件的贡献。
- **真实世界验证**：在两种不同机器人（不同自由度、控制模式）上做了8个任务，涵盖双臂协调、精细操作、变形物体等挑战。
- **泛化实验**：从物体、背景、光照三个维度验证了模型的鲁棒性，并量化了性能下降幅度。
- **代码与模型开源**：提供了项目网页，公开了预训练和微调细节。

## 8. 不足与局限
- **静态配置**：System 1共享块数量、两系统频率比是静态设定的，未实现根据任务复杂度动态调整。论文承认这是未来工作方向。
- **真实对比不够全面**：真实世界仅与π0对比，缺乏与CogACT、ManipLLM等在同一硬件上的直接比较，可能是因为这些方法未提供真实部署权重。
- **任务覆盖有限**：模拟10个任务，真实8个任务，虽然多样但属于桌面级操控，未涉及移动操作、复杂装配或高动态场景。
- **点云产生方式**：点云从单视角深度图生成，可能存在遮挡和噪声，对空间理解的鲁棒性有待进一步评估。
- **失败案例分析**：附录中展示了真实场景的四种失败模式（双臂碰撞、操作高度/位置误差、旋转误差），提示在双臂协调、变形物体操控方面仍有改进空间。
- **社会影响**：论文附录提及高速闭环控制存在安全隐患，需在部署中加入安全约束，但未提供具体措施。
- **算力需求**：7B模型预训练需要8张A800 GPU，微调也需要较多资源，对研究社区复现有一定门槛。

（完）
