---
title: "BiAssemble: Learning Collaborative Affordance for Bimanual Geometric Assembly"
title_zh: BiAssemble：学习协作可学习操纵用于双臂几何组装
authors: "Yan Shen, Ruihai Wu, Yubin Ke, Xinyuan Song, Zeyi Li, Xiaoqi Li, Hongwei Fan, Haoran Lu, Hao Dong"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=OxzPgnkbB1"
tags: ["query:vla"]
score: 6.0
evidence: 双臂组装任务与可学习操纵
tldr: 几何组装任务要求机器人识别几何线索进行抓取和双臂协作，现有方法缺乏对协作可学习操纵的利用。本文提出BiAssemble，学习点级可学习操纵的协作感知，用于长序列双臂几何组装。引入新评估指标解决碎片几何多样性带来的歧义。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1711, \"height\": 1288, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1751, \"height\": 1246, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1751, \"height\": 706, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1759, \"height\": 467, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1728, \"height\": 839, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1752, \"height\": 1076, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1760, \"height\": 685, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1767, \"height\": 635, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1768, \"height\": 1702, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1657, \"height\": 2041, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-oxzpgnkbb1/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1687, \"height\": 600, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-oxzpgnkbb1/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1706, \"height\": 410, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-oxzpgnkbb1/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 959, \"height\": 806, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-oxzpgnkbb1/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 741, \"height\": 200, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-oxzpgnkbb1/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1396, \"height\": 308, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-oxzpgnkbb1/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 916, \"height\": 309, \"label\": \"Table\"}]"
motivation: 双臂几何组装需要识别协作可学习操纵，现有方法忽视协作点级信息。
method: 提出点级可学习操纵的协作学习框架，结合长序列动作。
result: 在多种碎片组装任务中取得高成功率。
conclusion: 协作可学习操纵是双臂组装的关键，BiAssemble有效利用点级信息。
---

## Abstract
Shape assembly, the process of combining parts into a complete whole, is a crucial skill for robots with broad real-world applications. Among the various assembly tasks, geometric assembly—where broken parts are reassembled into their original form (e.g., reconstructing a shattered bowl)—is particularly challenging. This requires the robot to recognize geometric cues for grasping, assembly, and subsequent bimanual collaborative manipulation on varied fragments. In this paper, we exploit the geometric generalization of point-level affordance, learning affordance aware of bimanual collaboration in geometric assembly with long-horizon action sequences. To address the evaluation ambiguity caused by geometry diversity  of broken parts, we introduce a real-world benchmark featuring geometric variety and global reproducibility. Extensive experiments demonstrate the superiority of our approach over both previous affordance-based and imitation-based methods.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究问题**：几何形状组装（geometric assembly）——将破碎的物体碎片（如打碎的碗）重新组装成原始形状——是机器人领域一项极具挑战性的任务。与家具组装不同，几何组装中碎片形状不规则、无语义标签，且需要双臂协作完成长序列精细操作（抓取、对齐、装配）。现有方法多专注于计算机视觉中的部件位姿预测，忽略了机器人执行过程中的碰撞和协作问题。
- **核心挑战**：观测空间和动作空间巨大。碎片几何任意，抓取点需兼顾后续装配动作；动作序列长且接触密集，需考虑双臂协作和几何约束。
- **研究动机**：利用点级可学习操纵（point-level affordance）的几何泛化能力，并将其扩展到对后续长序列双臂协作动作的感知，从而解决几何组装中的复杂操作问题。
- **论文贡献**：
  - 提出 **BiAssemble** 框架，通过学习协作性可学习操纵（collaborative affordance）实现双臂几何组装。
  - 引入逆过程（从装配到拆卸）来获取对齐位姿，简化长序列规划。
  - 设计真实世界基准，包含多种品牌物体和可重复的碎片，便于公平评估。
  - 实验证明优于已有基于可学习操纵和模仿学习的方法。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
- 将双臂几何组装分解为三个步骤：**拾取**、**对齐**、**装配**。
- 通过“从装配到拆卸”的思路，从想象装配形状中预测无碰撞的拆卸方向，进而得到对齐位姿。
- 利用点级可学习操纵预测每步动作，并使其感知后续协作需求。

### 关键技术细节

1. **拆卸方向预测（Disassembly Prediction）**
   - 输入：想象装配形状 \(S\)（任意位姿的点云）。
   - 使用 **VN-DGCNN** 提取 SO(3)-等变特征 \(f_S\)，利用等变性解耦形状几何与位姿。
   - 条件变分自编码器（cVAE）预测无碰撞的拆卸方向 \(v\)，损失包括余弦相似度和KL散度。

2. **变换预测（Transformation Prediction）**
   - 目的：预测 SE(3) 变换 \(M\)，将想象装配形状 \(S\) 和拆卸方向 \(v\) 映射到对齐位姿，使机器人能从初始无碰撞操作到对齐位姿。
   - 输入：初始观测点云 \(O\) 的全局特征 \(f_O\) 和方向特征 \(f_v\)。
   - 同样使用 cVAE，预测平移（L1损失）和旋转（6D向量 + 测地线损失）。

3. **BiAffordance 预测器（BiAffordance Predictor）**
   - 分解为两个条件子模块，分别预测两个机械臂的动作。
   - **第一个子模块**：Affordance Network 输出每个点的可操作得分，选最高分点 \(p_1^*\)；Actor Network（cVAE）预测抓取方向 \(r_1\)。
   - **第二个子模块**：以第一个动作 \(g_1=(p_1^*, r_1)\) 为条件，同样预测 \(g_2\)。
   - 训练时引入 Critic Network 评估第一个动作的协作质量，通过 L1 损失和二元交叉熵损失监督。
   - 输入特征包括：点特征 \(f_p\)、变换后形状全局特征 \(f_{S'}\)、变换后方向特征 \(f_{v'}\)。

4. **对齐与装配动作计算**
   - 假设抓取后相对位姿不变，通过公式计算抓取位姿与装配位姿的关系：\(g_{\text{asm}} = g_{\text{pick}} \cdot q_{\text{pick}} \cdot (q_{\text{init}})^{-1} \cdot M^{-1}\)。
   - 对齐位姿：\(q_{\text{align}} = M \cdot q_{\text{init}} + v'\)。

5. **训练流程**
   - 拆卸预测器与变换预测器联合训练（约20小时）。
   - BiAffordance预测器分步训练：先训练第二个子模块，再用其对第一个子模块进行指导训练（约48小时）。
   - 使用7,000正样本 + 7,000负样本（从仿真中收集）。

## 3. 实验设计：数据集、基准、对比方法

### 仿真环境与数据集
- **平台**：SAPIEN，使用两个 Franka Panda 机械臂。
- **数据集**：Breaking Bad 数据集（Sellan et al., 2022）的 EverydayColorPieces 子集，包含15个类别、445个形状、11,820个碎片对。其中10个类别用于训练（237个形状，6,403对），5个类别用于测试（77个形状，1,779对）。
- **数据划分**：训练类别中60%形状训练，40%作为 novel instances（形状级泛化测试）；5个未见类别用于类别级泛化测试。

### 真实世界基准
- 扫描6类物体（酒杯、盘子、啤酒瓶、碗、马克杯、茶壶），使用智能手机、COLMAP、Grounded SAM2、Depth Anything V2、SDFStudio 重建3D网格。
- 碎片通过 Blender 编辑得到，并标注真实装配位姿。
- 使用 Azure Kinect 相机、ROS 控制、frankapy 库。

### 对比方法
- **ACT** (Zhao et al., 2023)：基于 Transformer 的模仿学习，增加深度、位姿和目标图像输入。
- **Heuristic**：手工规则（类似数据收集中的启发式）。
- **SE(3)-Equiv** (Wu et al., 2023c)：视觉位姿预测，结合启发式抓取。
- **DualAfford** (Zhao et al., 2022)：短时双臂可学习操纵，仅用于抓取，对齐和装配用启发式。
- **消融版本**：
  - w/o SE(3)：替换 VN-DGCNN 为 PointNet++。
  - w/ GT Target：提供真实拆卸方向和变换。
  - 额外消融：去掉 Affordance Network、去掉 Transformation Predictor、使用启发式方向。

### 评估指标
- 成功标准：两个碎片的相对距离和旋转角度小于预设阈值。每个类别测试100个样本。

## 4. 资源与算力

- **GPU**：单个 NVIDIA V100 GPU。
- **训练时间**：
  - 拆卸预测器 + 变换预测器：约20小时。
  - BiAffordance 预测器：约48小时。
  - 总时长约48小时（可同时训练）。
- **推理资源**：仅需1600 MB GPU内存，每个数据点平均0.1秒。
- **标注**：论文未详细说明训练数据收集的计算成本，但提到使用了启发式策略提高效率。

## 5. 实验数量与充分性

### 实验数量
- **仿真实验**：
  - 主实验：10个训练类别的 novel instances 和5个未见类别，每个类别100样本，报告成功率和平均值。
  - 消融实验：6组（w/o SE(3), w/ GT Target, w/o Affordance, w/o Transformation, w/ heuristic v, 以及基础版本），同样在两组数据集上评估。
  - 额外实验：多碎片（3碎片）组装、瓶盖关闭任务、不完美想象装配形状输入。
- **真实世界实验**：展示6类物体（碗、茶杯、盘子、酒杯、啤酒瓶等）的操作过程，并配有视频（附录），但未提供定量成功率。

### 充分性与公平性
- **充分性**：对比了模仿学习、手工策略、视觉位姿方法、短时可学习操纵方法，消融充分，覆盖了关键组件。额外实验验证了方法在多碎片和不同任务上的泛化性。
- **客观性**：所有方法在相同初始观测下测试，随机采样100个样本，统计成功率的平均值。评估指标明确。
- **局限性**：真实世界实验仅为定性展示，未给出定量对比；多碎片实验仅限三个碎片，未扩展更多；不完美输入实验使用预训练模型产生，但未对不同噪声水平做系统测试。

## 6. 主要结论与发现

- BiAssemble 在仿真中显著优于所有基线：在 novel instances 上平均成功率24.10%（对比 DualAfford 8.40%、Heuristic 4.20%、ACT 0.30%）；在未见类别上平均17.40%（对比 DualAfford 7.20%、Heuristic 4.40%）。
- 点级可学习操纵能有效泛化到不同形状和类别，且通过感知后续协作动作，避免了接缝区域等不利抓取。
- 拆卸预测和变换预测是成功对齐与装配的关键，消融实验证明其不可或缺。
- 真实世界实验验证了方法可以从仿真迁移到现实场景。

## 7. 优点

- **方法创新**：首次将点级可学习操纵用于长序列双臂几何组装，通过“逆拆卸”思想简化对齐规划。
- **几何泛化性**：利用 SO(3)-等变表示和点级特征，在形状级和类别级均表现出良好泛化。
- **协作性设计**：条件分解的双臂预测器，并通过 critc 网络使第一个动作意识到后续协作。
- **基准贡献**：构建了真实世界可重复基准，包含多种国际品牌物体，便于公平比较和复现。
- **实验全面**：覆盖仿真、真实、多碎片、不同任务，消融深入。

## 8. 不足与局限

- **对想象装配形状的依赖**：假设已有精确的想象装配形状（可由视觉方法预测），但实际中预测可能不完美。论文虽做了容忍性测试（精度下降约3%），但未系统研究噪声影响。
- **真实实验缺乏定量评估**：仅展示定性结果，未在真实基准上给出成功率对比，说服力不足。
- **抓取能力受限**：对重、光滑、扁平碎片易失败（失败案例分析），未引入预操作（如推到桌边）来改善。
- **多碎片扩展有限**：仅测试了三个碎片，更复杂场景（4个以上）未验证。
- **训练耗时**：48小时训练时间较长，且需要大量仿真数据采集（7,000正样本+负样本）。
- **动作空间简化**：假设抓取后相对位姿不变，实际中可能因滑移或接触变形而失效；未考虑力控或自适应调整。

（完）
