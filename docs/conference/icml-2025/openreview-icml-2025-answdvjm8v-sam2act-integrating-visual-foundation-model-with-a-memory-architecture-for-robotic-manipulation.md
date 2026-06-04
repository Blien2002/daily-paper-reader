---
title: "SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation"
title_zh: SAM2Act：融合视觉基础模型与记忆架构的机器人操作策略
authors: "Haoquan Fang, Markus Grotz, Wilbert Pumacay, Yi Ru Wang, Dieter Fox, Ranjay Krishna, Jiafei Duan"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=anSWDvJm8v"
tags: ["query:vla"]
score: 9.0
evidence: 整合视觉基础模型用于机器人操作，多视图变换器策略，在RLBench上达到最先进水平
tldr: "本文针对机器人操作在多变环境中的泛化与记忆需求，提出了SAM2Act，一种结合视觉基础模型与记忆架构的多视图变换器策略。通过多分辨率上采样利用大规模视觉表示，SAM2Act在RLBench基准的18个任务上达到86.8%的平均成功率，展现了强大的泛化能力。该工作为构建多任务通用操作策略提供了有效方案。"
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-answdvjm8v/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1454, \"height\": 348, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-answdvjm8v/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1326, \"height\": 834, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-answdvjm8v/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1396, \"height\": 732, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-answdvjm8v/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1249, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-answdvjm8v/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1782, \"height\": 912, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 867, \"height\": 900, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1782, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1647, \"height\": 333, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 861, \"height\": 134, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 785, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 719, \"height\": 519, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1423, \"height\": 509, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1778, \"height\": 794, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1767, \"height\": 457, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1777, \"height\": 394, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1787, \"height\": 844, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-answdvjm8v/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1780, \"height\": 247, \"label\": \"Table\"}]"
motivation: 现有机器人操作方法在环境泛化和记忆依赖任务上表现不足，亟需提升多任务交互与泛化能力。
method: 提出多视图变换器策略，结合大规模视觉基础模型的多分辨率上采样与记忆架构以增强空间记忆。
result: "在RLBench基准的18个任务上达到86.8%的平均成功率，展现出优异的泛化性能。"
conclusion: SAM2Act有效提升了机器人操作的多任务能力与泛化性，为构建通用操作模型奠定基础。
---

## Abstract
Robotic manipulation systems operating in diverse, dynamic environments must exhibit three critical abilities: multitask interaction, generalization to unseen scenarios, and spatial memory. While significant progress has been made in robotic manipulation, existing approaches often fall short in generalization to complex environmental variations and addressing memory-dependent tasks. To bridge this gap, we introduce **SAM2Act**, a multi-view robotic transformer-based policy that leverages multi-resolution upsampling with visual representations from large-scale foundation model. SAM2Act achieves a state-of-the-art average success rate of **86.8% across 18 tasks** in the RLBench benchmark, and demonstrates robust generalization on *The Colosseum* benchmark, with only a **4.3% performance gap** under diverse environmental perturbations. Building on this foundation, we propose **SAM2Act+**, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to enhance spatial memory. To address the need for evaluating memory-dependent tasks, we introduce ***MemoryBench***, a novel benchmark designed to assess spatial memory and action recall in robotic manipulation. SAM2Act+ achieves an average success rate of **94.3% on memory-based tasks** in *MemoryBench*, significantly outperforming existing approaches and pushing the boundaries of memory-based robotic systems.
Project page: [sam2act.github.io](https://sam2act.github.io/).

---

## 论文详细总结（自动生成）

# 中文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有机器人操作策略在**多任务交互**、**泛化到未见场景**和**空间记忆**这三项关键能力上存在明显不足。尤其在复杂环境变化（光照、纹理、物体外观等）以及需要依赖历史信息（如记住先前打开过的抽屉）的记忆型任务上，传统方法表现弱。
- **整体含义**：该文旨在通过融合大规模视觉基础模型（SAM2）和显式记忆架构，构建一个既能高精度执行多任务又能泛化到环境扰动、且具备空间记忆能力的通用操作策略。这为迈向家庭服务机器人等现实应用提供了关键技术支撑。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：
  - **SAM2Act**：基于RVT-2的多视图变压器框架，引入**SAM2图像编码器**提取多分辨率视觉嵌入，并通过**级联的多分辨率凸上采样**模块将嵌入逐步融入翻译热图预测，从而提升动作定位精度。使用LoRA（rank=16）微调SAM2编码器以适应操控域。
  - **SAM2Act+**：在SAM2Act基础上，受SAM2视频跟踪机制启发，在粗分支中嵌入**记忆库（Memory Bank）**、**记忆编码器（Memory Encoder）**和**记忆注意力（Memory Attention）**。通过将历史预测热图编码为记忆特征，并与当前观测特征进行交叉注意力，使策略具备基于历史上下文推断当前动作的能力。
- **关键技术细节**：
  - 场景通过5个RGB-D相机重建点云，从三个正交虚拟相机渲染虚拟图像。RGB通道复制后输入SAM2编码器，与深度、3D坐标、语言指令拼接后送入多视图变压器。
  - 多分辨率上采样采用三级级联：每级先进行凸上采样（空间尺寸加倍、通道减半），然后与对应尺度的SAM2嵌入逐元素相加，再经层归一化。
  - SAM2Act+冻结预训练好的SAM2Act中SAM2编码器、多视图变压器和细分支，仅微调粗分支中的记忆组件和多分辨率上采样模块。训练时采样连续动作关键帧序列（窗口大小因任务而异），按顺序前向传播并更新记忆队列。
- **公式流程**（文字说明）：见论文Algorithm 1，描述了每个步骤视图独立的记忆读写过程：获取原始嵌入→检索历史记忆→记忆注意力生成条件嵌入→上采样预测热图→编码新记忆存入FIFO队列。

## 3. 实验设计：数据集、Benchmark、对比方法
- **仿真环境**：CoppeliaSim + PyRep，Franka Panda机器人，5个RGB-D相机（128×128）。
- **基准**：
  - **RLBench**：18个任务，249个变体（位置、颜色、大小、类别等），100个演示训练，25个未见演示测试，4次评估取平均值和标准差。
  - **The Colosseum**：20个任务，13种扰动（物体颜色/纹理/尺寸、光照、背景、相机位姿等），测试泛化能力，3次评估。
  - **MemoryBench**（本文新提出）：3个空间记忆任务（reopen drawer、put block back、rearrange block），每个任务含2-4个变体，故意违反马尔可夫性质，要求策略回忆历史动作。单任务训练，多epoch选取最佳模型。
- **真实机器人**：Franka Panda + Robotiq 2F-85 + RealSense D455，4个任务（turn on the lamp、push buttons in sequence、stack cubes、push the same button），每个任务10次分布内和10次分布外测试。
- **对比方法**：
  - 3D键帧行为克隆基线：PerAct, RVT, RVT-2, SAM-E, 3D Diffuser Actor, 3D-LOTUS, ARP+ 等（全表见附录C）。
  - 消融变体：替换SAM2编码器为SAM或DINOv2或Depth Anything V2，移除多分辨率输入，使用原始上采样等。

## 4. 资源与算力
- **明确说明**：所有模型在**32块NVIDIA H100/A100 GPU**上训练；部分实验使用16或8块GPU，但保持总batch size相同以保证公平性。
- **训练时长**：SAM2Act在RLBench上训练56.25K步（90 epoch），SAM2Act+在MemoryBench上额外训练12.5K步。未提供具体小时数。

## 5. 实验数量与充分性
- **充分性**：实验覆盖全面，包括：
   - 主实验：RLBench 18任务 + The Colosseum 20任务 + MemoryBench 3任务 + 真实4任务。
   - 消融实验：更换图像编码器（SAM/DINOv2/DepthAnything）、移除多分辨率输入/上采样、不同LoRA rank等。
   - 每个实验报告多次评估的均值和标准差，统计严谨。
- **客观性与公平性**：与多个SOTA方法在相同设定下对比，使用相同或兼容的训练配置（如总batch size一致）。MemoryBench采用单任务训练以避免多任务干扰，且对每个任务早停选取最佳epoch。真实实验也设置了分布内/分布外条件。

## 6. 论文的主要结论与发现
- SAM2Act在RLBench 18任务上达到**86.8%**平均成功率，领先此前最佳RVT-2（81.4%）**5.4%**，尤其在高精度任务（插入销钉提升44%，形状分拣提升29%）表现突出。
- 泛化方面，在The Colosseum上SAM2Act整体性能仅下降**-4.3%**，远优于RVT-2的-19.5%，对光照、纹理等环境扰动鲁棒。
- 记忆方面，SAM2Act+在MemoryBench上平均成功率**94.3%**，远超无记忆的SAM2Act（55.0%）和RVT-2（54.0%），证明显式记忆建模的必要性。
- 真实实验也验证了泛化和记忆能力，SAM2Act在高精度灯旋钮任务上成功率60% vs RVT-2的0%。

## 7. 优点：方法或实验设计上的亮点
- **方法创新**：
  - 有效结合视觉基础模型（SAM2）与机器人操控变压器，利用SAM2的多分辨率嵌入提升动作定位精度。
  - 将SAM2视频跟踪的“记忆-注意力”思想适配到动作预测中，开创性地用热图替代掩码作为记忆输入，赋予策略空间记忆能力。
  - 提出**MemoryBench**新基准，精心设计违反马尔可夫性质的任务，为后续记忆型操控研究提供标准评估工具。
- **实验设计**：
  - 多维度评估：标准泛化（The Colosseum）、记忆（MemoryBench）、真实世界。
  - 详尽的消融实验，隔离各组件贡献（编码器、上采样、记忆等）。
  - 代码和项目页面公开，结果可复现。

## 8. 不足与局限
- **记忆窗口固定**：SAM2Act+的FIFO大小需针对不同任务手动设定，无法自适应任务长度变化。
- **未扩展到灵巧操作与连续控制**：当前方法针对6-DoF键帧预测，不适用于如手部灵巧操作的连续动作空间。
- **计算开销**：SAM2编码器虽经LoRA微调，但多视图处理仍需较高算力（32块GPU）；记忆组件增加额外推理延迟。
- **真实实验规模有限**：仅4个任务，且每个任务仅10次测试，统计显著性有限；分布外扰动种类较少。
- **MemoryBench任务规模小**：仅3个模拟记忆任务，尚不能全面评估长程复杂记忆推理。
- **可能的内偏风险**：所有实验基于Franka Panda和CoppeliaSim仿真，结果向其他机器人/真实场景的迁移性未验证。

（完）
