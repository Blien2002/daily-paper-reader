---
title: "DexScale: Automating Data Scaling for Sim2Real Generalizable Robot Control"
title_zh: DexScale：自动化数据扩展以实现Sim2Real可泛化机器人控制
authors: "Guiliang Liu, Yueci Deng, Runyi Zhao, Huayi Zhou, Jian Chen, Jietao Chen, Ruiyan Xu, Yunxin Tai, Kui Jia"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=AVVXX0erKT"
tags: ["query:vla"]
score: 6.0
evidence: 用于扩展模拟机器人技能的数据引擎，促进操作策略的Sim2Real泛化
tldr: 针对机器人操作策略数据稀缺问题，本文提出DexScale数据引擎，自动进行技能模拟与数据扩展，并集成可用性验证以弥合Sim2Real差距。该引擎能高效生成大规模、可部署的操作策略训练数据，为通用机器人控制提供了数据基础。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 805, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1604, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 852, \"height\": 294, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1757, \"height\": 624, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 681, \"height\": 504, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 847, \"height\": 1717, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1775, \"height\": 974, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1730, \"height\": 612, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1758, \"height\": 621, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1729, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-avvxx0erkt/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1730, \"height\": 610, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-avvxx0erkt/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 835, \"height\": 435, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-avvxx0erkt/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1068, \"height\": 421, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-avvxx0erkt/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1638, \"height\": 239, \"label\": \"Table\"}]"
motivation: 真实机器人数据昂贵，模拟数据存在Sim2Real鸿沟，需要自动化数据生成与扩展方法。
method: 提出DexScale数据引擎，自动模拟、记录并验证机器人技能，确保模拟数据的可用性。
result: 能高效生成大规模可用于实际部署的操作策略，促进Sim2Real泛化。
conclusion: 自动化的技能模拟与数据扩展是解决机器人数据瓶颈的有效途径。
---

## Abstract
A critical prerequisite for achieving generalizable robot control is the availability of a large-scale robot training dataset. Due to the expense of collecting realistic robotic data, recent studies explored simulating and recording robot skills in virtual environments. While simulated data can be generated at higher speeds, lower costs, and larger scales, the applicability of such simulated data remains questionable due to the gap between simulated and realistic environments. To advance the Sim2Real generalization, in this study, we present DexScale, a data engine designed to perform automatic skills simulation and scaling for learning deployable robot manipulation policies. Specifically, DexScale ensures the usability of simulated skills by integrating diverse forms of realistic data into the simulated environment, preserving semantic alignment with the target tasks. For each simulated skill in the environment, DexScale facilitates effective Sim2Real data scaling by automating the process of domain randomization and adaptation. Tuned by the scaled dataset, the control policy achieves zero-shot Sim2Real generalization across diverse tasks, multiple robot embodiments, and widely studied policy model architectures, highlighting its importance in advancing Sim2Real embodied intelligence.

---

## 论文详细总结（自动生成）

# DexScale 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：训练可泛化的机器人控制策略需要大规模数据集，但真实机器人数据采集成本高昂（设备、人力、标准化困难）。模拟数据生成速度快、成本低、规模大，但存在显著的 **Sim2Real 鸿沟**，包括语义不匹配（模拟环境与真实任务场景不一致）和模拟差异（物理、渲染等与现实不符），导致模拟训练的模型难以直接部署到真实世界。
- **研究动机**：需要一个自动化数据引擎，能够将真实场景信息（如人类演示视频）高效映射到模拟环境，并自动进行领域随机化与适应，生成可用于零样本 Sim2Real 迁移的大规模技能数据集，从而支撑通用机器人控制的训练。
- **整体含义**：DexScale 旨在解决机器人学习中的数据瓶颈，通过自动化数据生成与扩展，使模拟数据真正可用于真实环境部署，推动 Sim2Real 具身智能的发展。

## 2. 论文提出的方法论

- **核心思想**：构建一个自动化的数据引擎（DexScale），包含三个主要阶段：
    1. **异构数据投影（Heterogeneous Data Projection）**：将真实任务描述数据（如单视角或多视角 RGB 图像、人类演示视频）投影到模拟环境中，确保语义对齐。包括场景投影（通过“数字近亲”匹配、CAD 模型后处理、用户手动调整）和动作轨迹投影（从视频中检测人手/物体交互，重定位到机器人末端执行器，联合优化物体与手的 3D 位姿）。
    2. **环境模拟与技能生成（Environment Simulation）**：基于投影数据和任务描述，自动构建完整场景（利用 GPT-4 等大模型生成场景配置，从 Objaverse-XL 检索或生成物体），并生成动作轨迹（逆运动学、运动规划、用户提供奖励函数/RL）。
    3. **Sim2Real 数据扩展（Sim2Real Data Scaling）**：通过自动领域随机化（Action-Invariant DR 和 Semantic-Aware DR）生成多样化配置 Dξ，再用自适应（如面向对象的点云表示、姿态可供性表示）将观测映射到统一空间，最终得到可部署的数据集 DDR+AR。
- **关键技术细节**：
    - **自动领域随机化（AutoDR）**：利用大语言模型对 DR 特征排序，结合 ADR 算法（基于策略反馈）自动更新随机化参数分布。
    - **领域适应（DA）**：支持面向对象表示（去除背景，提取点云）和姿态可供性表示（只预测关键接触姿态），降低 Sim2Real 差异。
    - **零样本部署**：基于扩展后的数据集训练模仿策略（如 ACT、Diffusion Policy、RDT），直接在真实环境中执行，无需额外微调。
- **公式/算法流程**（文字说明）：  
    环境建模为 MDP M=(S,A,P_T,R,γ,ρ0)；  
    AI-DR 假设最优策略不变；  
    SA-DR 通过优化目标 J(Mξ′,π) − Div(π||π_θ0) 适应新环境；  
    最终策略通过模仿数据 D_DR+AR 训练。

## 3. 实验设计

- **数据集/场景**：
    - **泛化性实验（Generalizability）**：在模拟环境中人为引入10种 Sim2Real 差异（光照、物体纹理、桌面纹理、背景、干扰物、相机位置/朝向/视场角、物体姿态/形状），并对应在真实环境中进行10次试验评估。
    - **可扩展性实验（Scalability）**：四个任务——物体抓取（单一机械臂）、纸箱操作（打开四个盖子）、双臂桌面重排（摆放叉勺）、倒水（抓取瓶子倒水）。使用三种策略模型架构：Transformer-based policy（抓取）、Diffusion policy（开箱）、VLA model（桌面重排）。
- **Benchmark 与对比**：
    - **对比方法**：消融实验对比了“仅技能数据”、“技能+DR”、“技能+DA”以及完整的 DexScale 数据集。另外与人工选择 DR（按照 Xie et al. 2024 中 top-3 特征）进行了比较。
    - **无公开基准对比**：论文未直接与已有方法（如 MimicGen、GenAug）在相同场景下比较，而是聚焦于 DexScale 内部组件是否有效。
- **评价指标**：任务成功率（Sim 中100次，Real中10次）。

## 4. 资源与算力

- **明确说明的硬件配置**：
    - 抓取任务（Transformer）：4× NVIDIA A800 GPU，训练36小时；PyTorch 2.0.1。
    - 开箱任务（Diffusion Policy）：1× NVIDIA A100 GPU，训练48小时；PyTorch 2.0.1。
    - 桌面重排任务（RDT）：1× NVIDIA A100 GPU，训练时间未明确（40,000 iterations）；PyTorch 2.0.1。
- **其他资源**：未提及具体 CPU/内存、数据存储等。
- **总体评价**：算力信息比较具体，但仅涵盖三个主要实验，未提及泛化性实验中模型训练的资源消耗。

## 5. 实验数量与充分性

- **实验数量**：
    - 泛化性实验：10种领域差距 + 4种数据设置（仅技能、+DR、+DA、DexScale）= 40组条件，每组模拟100次、真实10次，合计约 1,600 次模拟试验和 400 次真实试验。但真实试验次数偏少（每条件仅10次）。
    - 可扩展性实验：4个任务 × 3种模型架构（但不同任务使用不同模型，并非所有排列）× 多机器人平台，提供了 Table 3（实际部署成功率）和可视化结果。
    - 消融实验：将 DR 和 DA 分别移除，证明了二者均有效。
- **充分性与公平性**：
    - **优势**：涵盖了多种典型 Sim2Real 差异，使用了多种策略架构和机器人平台，消融实验设计合理。
    - **不足**：
        - 真实环境试验次数仅10次，统计显著性较低。
        - 未与现有的其他 Sim2Real 系统（如 RoboGen、MimicGen）进行直接性能对比。
        - 未进行跨差别的综合分析（例如同时出现多种差异时的表现）。
        - 可扩展性实验中的成功率只在真实环境展示，未给出对应模拟环境的成功率，难以判断 Sim2Real 差距的具体大小。
    - 整体上实验设计考虑较全面，但统计量和对比范围有限。

## 6. 论文的主要结论与发现

- DexScale 能够显著桥接 Sim2Real 差距：在所有10种领域差异下，完整 DexScale 数据集训练的模型在模拟和真实环境中的成功率均高于仅有技能数据、仅+DR 或仅+DA 的消融设置。
- DR 与 DA 均对泛化有贡献：去除其中任何一个都会导致性能下降，尤其当差异涉及物体姿态/形状时，DA 的作用更为突出（成功率从 33%→42%→69%）。
- 与人工选择的 DR 相比，自动 DR 效果更好（成功率为 0.79 vs 0.56 在真实环境）。
- 该方法可扩展至不同任务、不同策略架构（Transformer、Diffusion、VLA）和不同机器人平台（单臂、双臂），并实现零样本部署。

## 7. 优点

- **自动化程度高**：设计了完整的数据生成→投影→扩展→训练的流水线，显著减少人工干预。
- **语义对齐**：通过投影真实场景/演示视频，确保模拟数据与目标任务一致，解决语义鸿沟。
- **模块化与可扩展**：架构支持多种模拟器后端、多种策略模型、多种机器人，易于集成已有工作。
- **消融实验充分**：系统性地分析 DR 和 DA 各自贡献，验证了方法的有效性。
- **成功案例直观**：提供了丰富的可视化（图4、5、7-10），展示从人类演示→数据扩展→真实部署的完整过程。

## 8. 不足与局限

- **真实实验统计量少**：每个 Setting 仅10次真实试验，结果容易受随机因素影响，置信度有限。
- **缺乏与外部方法的对比**：未与现有 Sim2Real 系统（如 Domain Randomization 基线、其他数据生成方法）进行定量对比，无法判断相对先进程度。
- **场景多样性有限**：虽然涵盖4种任务，但均为桌面操作；未涉及复杂接触、可变形物体、长时序任务等更困难的场景。
- **依赖渲染和物理模拟质量**：DexScale 的有效性高度依赖模拟器的逼真度，对于模拟难以准确建模的现象（如软体形变、流体）可能效果不佳。
- **失败案例未系统分析**：仅在项目页面提到四种常见失败原因，未在论文正文中给出定量或深入分析。
- **开放性**：代码与数据集未明确说明是否开源，可复现性存疑。

（完）
