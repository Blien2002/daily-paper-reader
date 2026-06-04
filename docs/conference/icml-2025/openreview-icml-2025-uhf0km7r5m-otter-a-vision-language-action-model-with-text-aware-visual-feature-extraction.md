---
title: "OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction"
title_zh: OTTER：具有文本感知视觉特征提取的视觉-语言-动作模型
authors: "Huang Huang, Fangchen Liu, Letian Fu, Tingfan Wu, Mustafa Mukadam, Jitendra Malik, Ken Goldberg, Pieter Abbeel"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=UHF0km7R5M"
tags: ["query:vla"]
score: 9.0
evidence: 文本感知的视觉特征提取VLA架构
tldr: 现有VLA模型通常需要微调整个预训练的视觉语言模型，导致语义对齐被破坏。OTTER通过显式的文本感知视觉特征提取，只将与语言指令语义对齐的视觉特征传递给策略网络，从而保持预训练编码器冻结。这一设计减少了计算开销并保留了原有的语义对齐，在多个机器人操作任务上取得了更优的零样本泛化性能。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 836, \"height\": 670, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 798, \"height\": 700, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 808, \"height\": 611, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 828, \"height\": 315, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 773, \"height\": 570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1603, \"height\": 920, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-uhf0km7r5m/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1751, \"height\": 492, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 862, \"height\": 513, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1412, \"height\": 474, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1582, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 881, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1106, \"height\": 536, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1414, \"height\": 935, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 998, \"height\": 836, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 695, \"height\": 665, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-uhf0km7r5m/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1087, \"height\": 147, \"label\": \"Table\"}]"
motivation: 现有VLA微调整个预训练VLM会破坏原始的语义对齐，且计算成本高。
method: 提出文本感知视觉特征提取模块，仅提取与语言指令对齐的视觉特征，保持视觉语言编码器冻结。
result: 在多个机器人操作环境中，OTTER取得了更高的任务成功率，并展现出更强的零样本泛化能力。
conclusion: OTTER表明保留预训练语义对齐可以有效提升VLA模型的效率与泛化性能。
---

## Abstract
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained vision-language models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zero-shot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有的视觉-语言-动作（VLA）模型通常需要对整个预训练的视觉-语言模型（VLM）进行微调，将视觉和语言特征独立地输入到下游策略网络中。这种做法会破坏预训练阶段建立的语义对齐，导致模型在未见过的物体或环境上泛化能力显著下降。同时，机器人数据集远不如视觉-语言数据集语义丰富，微调容易过拟合。
- **研究动机**：探索是否可以通过保留预训练VLM的冻结状态，并利用其已有的文本-视觉对齐能力，来更有效地提取任务相关的视觉特征，从而在不牺牲泛化能力的前提下实现机器人操作任务。
- **整体含义**：提出一种新的VLA架构——OTTER，通过显式的**文本感知视觉特征提取**，只将与语言指令语义对齐的视觉特征传递给策略网络，保持预训练的视觉语言编码器完全冻结，从而保留并利用大规模预训练获得的丰富语义理解，实现强大的零样本泛化。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- **保留预训练VLM冻结，避免微调破坏语义对齐**。利用CLIP等模型的文本-视觉相似度，从视觉特征中**选择**与任务指令最相关的区域，将结果作为策略网络的输入，而不是将所有视觉特征都输入。

### 关键技术细节
1. **文本感知视觉特征提取**（图3）：
   - 使用预训练的CLIP（ViT架构）。从语言编码器获取文本token特征 \( f_l \)（m个token）。
   - 从视觉编码器的**最后一个自注意力层的注意力输出** \( X_{attn} \)（而非最终的输出特征 \( X_{out} \)）获取视觉patch特征 \( f_v \)（n个patch token）。理由：\( X_{attn} \)包含更干净的语义信息（受ClearCLIP启发）。
   - 对语言和视觉特征分别进行归一化和投影，然后计算余弦相似度，并通过softmax（带可学习温度参数 \( \tau \)）得到每个文本token对视觉patch的注意力权重。
   - 将加权后的视觉patch特征加上2D正弦余弦位置编码，得到文本感知的视觉特征 \( f_{vl} \in \mathbb{R}^{m \times d} \)。整个CLIP模型**完全冻结**，仅温度 \( \tau \) 可学习。

2. **模型架构**（图2）：
   - **输入压缩**：对每个摄像头的 \( f_{vl} \) 使用可学习的交叉注意力池化（4个查询），得到单个特征 \( f'_{vl} \)；对文本特征 \( f_l \) 也做类似池化得到 \( f'_l \)。
   - **本体感知编码**：通过MLP将机器人的10维本体状态（平移、旋转、夹爪状态）编码为 \( f_e \)。
   - 将 \( f'_l, f'_{vl}, f_e \) 拼接成一个token \( f_t \)，作为策略Transformer的输入。
   - **策略网络**：4层、8头、隐藏维度512的因果Transformer，上下文窗口长度为12步。每个时间步预测未来12个动作（delta end-effector姿态+夹爪开合），采用时序集成和滚动时域控制。

3. **动作和本体表示**：使用10维表示（3维平移 + 6维旋转向量 + 1维夹爪开度），动作使用相对于当前末端执行器姿态的delta变换。

## 3. 实验设计：数据集/场景、基准、对比方法

### 数据集/场景
- **仿真环境**：LIBERO benchmark（LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-90）。共30个训练任务，并构造10个未见过的任务（修改物体颜色/类型）。
- **真实机器人环境**：使用Franka机械臂，收集4种操作基元的数据：
  - **拾取与放置（Pick and Place）**：10个任务，724条演示，记为DS-PnP。
  - **倒水（Pouring）、抽屉（Drawer）、戳（Poking）**：共1,185条演示，记为DS-ALL。
  - 评估场景：19个训练任务（in-distribution）和15个未见任务（out-of-distribution），每个任务10次试验，随机改变目标位置和2-3个干扰物。

### 对比方法
- **Octo**：从零开始在Open X-Embodiment（800K轨迹）上训练的Transformer策略。
- **OpenVLA**：微调Prismatic-7B VLM的VLA模型。
- **π0-Fast-Droid**：使用PaliGemma和Fast action tokenizer的VLA，预训练于OXE和Droid数据集。
- **DFP-OTTER**：OTTER的变体，直接将所有视觉和语言token分别池化后拼接（无文本感知特征提取）。
- **其他消融变体**：去掉本体特征（w.o. \( f_e \)）、去掉文本token（w.o. \( f'_l \)）、去掉预训练CLIP（w.o. CLIP vision）、微调CLIP（Finetune CLIP）等。

## 4. 资源与算力
- **文中明确说明**：所有模型在4块NVIDIA A100 80GB GPU上训练。训练超参数：学习率3e-4，批大小64，总梯度步数40,000（对DS-PnP）或60,000（对OXE预训练）。使用AdamW优化器，余弦学习率衰减。
- **未说明**：具体训练时长（小时数）未提及。但提到使用ViT-L/14 CLIP的OTTER在单块NVIDIA 3090Ti上推理速度达50Hz（实时控制）。

## 5. 实验数量与充分性
- **实验数量**：
  - 真实环境：单基元（拾取与放置）100次训练试验 + 70次未见试验；多基元（4种基元）共150次未见试验（每种基元分别报告）。
  - 仿真环境：LIBERO各子集（Spatial/Object/Goal）各50次试验×30个任务 = 4,500次？以及未见任务10个×50次 = 500次。
  - 消融实验：在真实和仿真环境下均进行了多种消融（移除本体、移除文本、移除CLIP、微调CLIP等），并测试了不同CLIP规模（ViT-B/32, ViT-B/16, ViT-L/14）。
- **充分性与公平性**：
  - 与Octo、OpenVLA等SOTA方法进行了公平比较（相同训练步数、相同评估设置）。
  - 在仿真中直接引用OpenVLA论文报告的数值（带*标注），其余自己复现，但未提及是否完全复现其训练细节。
  - 消融实验设计较为全面，覆盖了架构关键组件，验证了文本感知提取和冻结编码器的重要性。
  - 实验覆盖了多种基元、多种场景，结论具有较好的一般性。但未测试长时域任务或更复杂场景。

## 6. 论文的主要结论与发现
1. **OTTER显著优于现有VLA方法**：在真实和仿真环境中，OTTER在训练和未见任务上的成功率均高于Octo、OpenVLA、π0-Fast-Droid等基线，尤其零样本泛化能力突出（例如多基元未见任务平均成功率67%-77%，而基线普遍低于10%或直接失败）。
2. **冻结预训练VLM + 文本感知特征提取是关键**：微调CLIP会破坏泛化能力（OTTER Finetune CLIP在未见任务上仅15%），而冻结CLIP并直接传递所有视觉特征（DFP-OTTER）仅4%，说明两者缺一不可。
3. **性能随规模提升**：更大的CLIP编码器（ViT-L/14优于ViT-B/32）、更大的策略网络（OTTER-L优于OTTER）、以及预训练于更大机器人数据集（OTTER-OXE优于从零训练OTTER）均能带来性能提升。
4. **文本感知视觉特征提取提供了更好的视觉-语言关联**，使策略网络能够聚焦于任务相关区域，减少背景干扰。

## 7. 优点
- **方法创新**：首次在VLA中提出使用冻结CLIP的注意力输出（而非最终输出）进行文本感知特征提取，既保留了预训练语义对齐，又避免了微调带来的灾难性遗忘。
- **高效性与实用性**：通过缓存CLIP特征实现50Hz实时推理，适合实际机器人控制。
- **全面的实验验证**：在仿真和真实场景、多基元、多任务设置下进行广泛评估，消融实验设计完整。
- **开源与可复现**：提供代码、检查点和数据集链接。

## 8. 不足与局限
- **形态多样性不足**：当前仅适用于可用SE(3)变换参数化的机器人（如单臂操作），对多指手等复杂形态支持有限。
- **长时域任务未探索**：实验仅涉及较短时间跨度的操作（如拾取、放置、倒水等），未评估在长时域任务（如多步骤组装）上的表现。
- **数据集规模相对较小**：真实机器人演示仅1,185条，虽然OTTER展现出较好的数据效率，但更大规模的机器人训练数据是否能持续提升尚需验证。
- **未见任务构造相对有限**：主要变化为物体类型/颜色/位置，未涉及场景结构大幅变化、光照变化或传感器噪声等更复杂的域迁移。
- **未讨论失败案例分析**：论文未详细分析哪些场景下OTTER失败以及失败模式，可能隐藏偏差（如对某些物体或背景的偏好）。
- **对CLIP的依赖**：性能受限于CLIP的预训练质量，若CLIP对某些细粒度指令理解不足，OTTER可能也受限。

（完）
