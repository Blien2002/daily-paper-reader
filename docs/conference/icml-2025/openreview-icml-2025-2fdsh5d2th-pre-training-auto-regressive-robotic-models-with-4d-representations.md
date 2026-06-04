---
title: Pre-training Auto-regressive Robotic Models with 4D Representations
title_zh: ARM4R：基于4D表示的预训练自回归机器人模型
authors: "Dantong Niu, Yuvan Sharma, Haoru Xue, Giscard Biamby, Junyi Zhang, Ziteng Ji, Trevor Darrell, Roei Herzig"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=2FDsh5D2Th"
tags: ["query:vla"]
score: 7.0
evidence: 利用4D表示预训练机器人基础模型
tldr: 机器人基础模型的预训练常受限于昂贵的标注数据或缺乏有效物理表示。ARM4R利用从人类视频中学习的3D点跟踪表示，再将其提升到4D空间，从而获得更丰富的时空信息。以此预训练自回归机器人模型，在多个操作任务上展现出更强的泛化能力和数据效率，为机器人预训练提供了低成本高效益的途径。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1767, \"height\": 908, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1608, \"height\": 903, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1747, \"height\": 584, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1715, \"height\": 1151, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1762, \"height\": 1914, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 859, \"height\": 650, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1758, \"height\": 756, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-2fdsh5d2th/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 857, \"height\": 649, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1659, \"height\": 415, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1721, \"height\": 609, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 866, \"height\": 373, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 864, \"height\": 251, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 881, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 871, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-2fdsh5d2th/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 857, \"height\": 247, \"label\": \"Table\"}]"
motivation: 现有机器人预训练依赖昂贵标注或缺乏有效物理表示，泛化能力有限。
method: 从人类视频中学习3D点跟踪表示，并提升到4D时空表示，用于预训练自回归机器人模型。
result: 在多个机器人操作任务上，ARM4R比基线预训练方法取得了更高的成功率，且所需的机器人数据更少。
conclusion: 该工作表明基于4D表示的预训练能有效提升机器人模型泛化性，降低对机器人数据的依赖。
---

## Abstract
Foundation models pre-trained on massive unlabeled datasets have revolutionized natural language and computer vision, exhibiting remarkable generalization capabilities, thus highlighting the importance of pre-training. Yet, efforts in robotics have struggled to achieve similar success, limited by either the need for costly robotic annotations or the lack of representations that effectively model the physical world. In this paper, we introduce ARM4R, an **A**uto-regressive **R**obotic **M**odel that leverages low-level **4**D **R**epresentations learned from human video data to yield a better pre-trained robotic model. Specifically, we focus on utilizing 3D point tracking representations from videos derived by lifting 2D representations into 3D space via monocular depth estimation across time. These 4D representations maintain a shared geometric structure between the points and robot state representations up to a linear transformation, enabling efficient transfer learning from human video data to low-level robotic control. Our experiments show that ARM4R can transfer efficiently from human video data to robotics and consistently improves performance on tasks across various robot environments and configurations.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：机器人领域的预训练面临两大瓶颈：一是缺乏大规模、多样化的机器人数据（相较于文本和图像的丰富资源），二是现有方法（如Vision-Language-Action模型）的高层次预训练目标（如视觉问答、图像描述）与机器人所需的低层次动作预测之间存在显著偏差，导致泛化能力不足。
- **研究背景**：尽管基础模型在语言和视觉领域取得了巨大成功，但机器人模型难以复制这种成功。先前尝试利用人类视频数据进行表示学习（如MVP、RPT）或使用预训练组件（如VLM）的方法，均未能有效解决物理世界理解与底层控制之间的鸿沟。
- **本文动机**：探索利用从人类视频中学习的低层次4D表示（3D点跨时间跟踪）来预训练机器人模型，实现从人类数据到机器人控制的高效迁移，降低对昂贵机器人标注数据的依赖。

## 2. 方法论：核心思想与关键技术细节

- **核心思想**：ARM4R（Auto-regressive Robotic Model with 4D Representations）通过从人类视频中学习3D点跟踪任务（4D表示），获得对物理世界空间动态的理解，然后通过三阶段训练迁移到机器人控制。
- **关键技术细节**：
  - **4D表示生成**：使用单目深度估计将2D图像提升到3D空间，并随时间跟踪3D点（采用SpatialTracker获得伪标签）。3D点云与机器人状态（如末端执行器位姿）之间存在线性变换关系，便于迁移。
  - **架构**：
    - 输入：语言指令（冻结CLIP文本编码器+可学习线性投影）、图像（冻结的ViT-Base，使用CrossMAE预训练于ImageNet+OpenX）、当前3D点坐标（2层MLP编码）。
    - 融合：点特征与图像特征通过注意力池化得到观测token；语言token、观测token、预测token（下一时刻3D点坐标）拼接后送入因果Transformer（随机初始化ViT-Base）。
    - 输出：预测的下一时刻3D点坐标，损失采用L1距离。
    - 控制微调阶段：将输入/输出的3D点替换为机器人状态（如7-DoF关节位置+夹爪状态），保留相同架构和损失函数。
  - **三阶段训练流程**：
    1. **Stage 1（人类视频预训练）**：在76K Epic-Kitchens100视频上训练3D点跟踪任务，学习通用空间动态。
    2. **Stage 2（机器人视频微调）**：在少量（≈5-10% of Stage 1数据量）目标机器人场景视频上进行相同点跟踪任务微调，适应分布差异（相机视角、本体结构等）。
    3. **Stage 3（机器人控制微调）**：在少量目标任务演示数据（每个任务190个episode）上，将预测目标从3D点切换为机器人状态，训练动作预测策略。

## 3. 实验设计

- **仿真环境**：RLBench（Franka Emika Panda），12个操作任务（如开抽屉、关罐子、堆叠方块等）。使用前rgb和手腕rgb视图。
- **真实机器人**：
  - **Kinova Gen3**（7-DoF，Robotiq夹爪）：13个任务，分为5大类（pick, destack, stack, pick&place, push）。两个Logitech BRIO 4K摄像头。
  - **Franka Emika Panda**（7-DoF）：3个立方体任务（pick, stack, destack），用于跨机器人泛化实验。两个摄像头。
- **对比基线**：
  - 仿真：Image-BC (ViT)、C2FARM-BC、ManiGaussian、LLARVA、PerAct。
  - 真实：ATM（2D点跟踪）、LLARVA、π0-FAST、OpenVLA（均使用相同或更多演示数据微调）。
- **评估指标**：成功率（%），每个任务25个episode，多个随机种子（仿真5种子，真实3种子）取平均。
- **消融实验**：分别去除Stage 1（人类预训练）和Stage 2（机器人视频微调）的影响；不同预训练策略对比（MVP, RPT, Octo等）；动态干扰实验（物体移动、光照变化、背景干扰等）。

## 4. 资源与算力

- **训练资源**：4块NVIDIA A6000 GPU（48GB显存）用于训练，1块NVIDIA A6000 GPU用于推理。
- **训练时长**：论文未明确报告各阶段具体训练时间，仅提及Stage 3训练至损失收敛（epoch数可变，约50个epoch）。
- **备注**：算力消耗相对较小，但属于高端消费级GPU；训练数据规模（76K人类视频）远小于主流VLM预训练数据量。

## 5. 实验数量与充分性评估

- **实验数量**：共计超过20组主要实验，包括：
  - 仿真12个任务对比（表1）。
  - 真实Kinova 13个任务对比（表2），含3种子。
  - 3种任务的消融实验（图3）。
  - 跨机器人泛化实验（表4）。
  - 动态环境与鲁棒性测试（表5、6）。
  - 不同预训练方法对比（表3）。
- **充分性评估**：
  - 对比基线涵盖主流方法（2D/3D表示、VLM、层次化策略），比较公平且全面。
  - 消融实验明确验证了每个阶段的贡献。
  - 跨机器人实验（Kinova→Franka）展示了泛化能力。
  - 鲁棒性测试覆盖了常见干扰（物体移动、光照、背景及桌面干扰）。
  - **客观性**：指标统一为成功率，符合领域惯例；多次重复降低方差。
  - **不足**：仿真实验结果未报告方差（仅平均值），可能降低说服力；真实实验仅3个种子，样本量偏小；部分任务（如screw bulb）表现较差但未深入分析失败模式；未在更多真实机器人平台（如不同构型）上验证。

## 6. 主要结论与发现

- **核心结论**：ARM4R通过从人类视频数据中预训练低层次4D表示（3D点跟踪），显著优于仅用机器人数据或高层次语言预训练的方法。
- **关键发现**：
  - 人类视频预训练（Stage 1）带来的性能提升远大于机器人视频微调（Stage 2）。
  - 完全使用人类数据预训练即可超越使用大规模机器人数据（OpenX）预训练的OpenVLA。
  - 4D表示（3D+时间）比2D表示（如ATM）更有效，且与机器人状态存在线性关系，便于迁移。
  - 模型对相机变化、本体差异具有一定通用性（跨机器人的泛化）。
  - 对动态扰动具有鲁棒性（物体移动、光照变化等），但桌面干扰物会显著降低性能。

## 7. 优点

1. **创新性表示**：首次将4D（3D点跨时间跟踪）表示用于机器人预训练，结合了空间几何与时间动态，比纯2D或纯3D更丰富。
2. **数据高效**：仅用人类视频预训练即可超越需要大量机器人数据的竞争对手，大幅降低对昂贵机器人标注的依赖。
3. **三阶段迁移流程清晰**：从人类→机器人场景→机器人控制，逐步适配，设计合理。
4. **广泛实验验证**：覆盖仿真、真实机器人、跨本体、鲁棒性等多种场景，消融实验完整。
5. **开源与复现性**：论文提供了项目主页和训练细节，便于后续研究。

## 8. 不足与局限

1. **3D点跟踪的坐标系耦合**：点跟踪在相机坐标系中进行，无法区分物体运动与相机运动（尤其是人类视频的自我中心视角），限制了模型对绝对运动的泛化。论文提出未来可使用动态SLAM（如MonST3R）改进。
2. **跟踪点选择简单**：均匀网格初始点，可能覆盖无效区域（背景）或遗漏细小物体。未来可考虑动态选择关键点。
3. **实验覆盖有限**：
   - 仿真任务只有12个，且未报告方差。
   - 真实机器人仅两类（Kinova、Franka），未测试其他主流平台（如UR5、Aloha等）。
   - 未测试复杂长时序任务（如多步操作、工具使用）。
4. **任务数量偏少**：每个任务只用190/200个演示，虽比基线少，但部分任务（如stack blocks）成功率仅4%，说明仍有较大改进空间。
5. **未进行大规模图像预训练比较**：ViT预训练组合了ImageNet+OpenX，但未与纯ImageNet预训练或CLIP预训练做消融。
6. **潜在偏差风险**：人类视频主要来源于厨房活动（Epic-Kitchens），可能导致模型偏向厨房场景的交互模式（但实验已迁移到非厨房任务，部分缓解）。
7. **实时性未讨论**：未报告推理速度或是否满足实时控制要求。

（完）
