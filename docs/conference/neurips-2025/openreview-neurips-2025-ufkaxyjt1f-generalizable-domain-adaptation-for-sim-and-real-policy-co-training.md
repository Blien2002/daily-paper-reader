---
title: Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training
title_zh: 可泛化的仿真与真实策略联合训练的域适应方法
authors: "Shuo Cheng, Liqian Ma, Zhenyang Chen, Ajay Mandlekar, Caelan Reed Garrett, Danfei Xu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ufKaXYJt1F"
tags: ["query:vla"]
score: 7.0
evidence: 仿真与真实联合训练可泛化的操纵策略
tldr: 机器人操纵策略依赖大规模真实演示，成本高昂。本文提出统一仿真-真实联合训练框架，通过对齐跨域观察-动作联合分布学习域不变特征，仅需少量真实演示即可实现良好泛化。实验表明该方法在多种操纵任务上显著缩小了仿真到真实的差距，为数据高效策略学习提供了新思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1448, \"height\": 493, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1417, \"height\": 456, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1443, \"height\": 410, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1442, \"height\": 447, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1006, \"height\": 769, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1152, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 866, \"height\": 335, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1441, \"height\": 594, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 816, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1439, \"height\": 350, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-ufkaxyjt1f/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1448, \"height\": 648, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1468, \"height\": 299, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1073, \"height\": 256, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1456, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1438, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1273, \"height\": 101, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 720, \"height\": 527, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1085, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 718, \"height\": 538, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1521, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-ufkaxyjt1f/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 993, \"height\": 279, \"label\": \"Table\"}]"
motivation: 真实演示数据昂贵，仿真数据存在域差异，需要域适应方法。
method: 提出联合训练框架，学习域不变的观察-动作联合分布特征空间。
result: 在多种机器人操纵任务上，仅用少量真实数据即达到与大量真实数据训练相当的性能。
conclusion: 域不变特征学习可有效利用仿真数据提升机器人操纵策略的泛化性。
---

## Abstract
Behavior cloning has shown promise for robot manipulation, but real-world demonstrations are costly to acquire at scale. While simulated data offers a scalable alternative, particularly with advances in automated demonstration generation, transferring policies to the real world is hampered by various simulation and real domain gaps. In this work, we propose a unified sim-and-real co-training framework for learning generalizable manipulation policies that primarily leverages simulation and only requires a few real-world demonstrations. Central to our approach is learning a domain-invariant, task-relevant feature space. Our key insight is that aligning the joint distributions of observations and their corresponding actions across domains provides a richer signal than aligning observations (marginals) alone. We achieve this by embedding an Optimal Transport (OT)-inspired loss within the co-training framework, and extend this to an Unbalanced OT framework to handle the imbalance between abundant simulation data and limited real-world examples. We validate our method on challenging manipulation tasks, showing it can leverage abundant simulation data to achieve up to a 30\% improvement in the real-world success rate and even generalize to scenarios seen only in simulation.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机与背景）

- **问题**：机器人操纵策略的主流方法是行为克隆（Behavior Cloning），但获取大规模真实世界演示数据成本高昂，限制了可扩展性。
- **动机**：仿真数据可通过自动化生成工具（如 MimicGen）低成本、大规模获取，但存在“仿真到真实”域差距（视觉外观、传感器噪声、动作动力学等），导致策略在真实世界部署时性能下降。
- **整体目标**：提出一种统一的仿真-真实联合训练框架，主要利用仿真数据，仅需少量真实演示，学习可泛化的操纵策略。核心思想是通过对齐跨域观察-动作的联合分布，学习域不变且任务相关的特征空间，从而缩小域差距，使策略能泛化到仅存在于仿真数据的场景。

## 2. 方法论

### 核心思想
- 直接对齐两域的观察边缘分布（如 MMD）不足以保留动作相关信息；反过来，对齐**观察-动作联合分布**可提供更丰富的监督信号，使特征编码器学习到域不变且动作可预测的表示。
- 采用**最优传输（Optimal Transport, OT）**作为对齐目标，并扩展为**非平衡最优传输（Unbalanced OT, UOT）**以处理仿真数据远多于真实数据的不平衡问题。

### 关键技术细节
1. **特征对齐框架**：
   - 对源域（仿真）和目标域（真实）的样本对，构建联合代价函数：
     \[
     C_{\phi}((f_{\phi}(o^{\text{src}}), a^{\text{src}}), (f_{\phi}(o^{\text{tgt}}), a^{\text{tgt}})) = \alpha_1 d_Z(f_{\phi}(o^{\text{src}}), f_{\phi}(o^{\text{tgt}})) + \alpha_2 d_A(a^{\text{src}}, a^{\text{tgt}})
     \]
   - 实践中，因动作表示可能存在跨域不一致，改用**本体感受（proprioception，如末端执行器位姿）**替代动作作为代价计算的一部分。
2. **非平衡最优传输（UOT）**：
   - 放松标准 OT 的严格边际约束，引入 KL 散度惩罚项，允许部分质量传输，从而忽略不匹配的样本对。
   - 损失函数：
     \[
     L_{\text{UOT}}(f_{\phi}) = \min_{\Pi} \langle \Pi, \hat{C}_{\phi} \rangle_F + \epsilon \cdot \Omega(\Pi) + \tau \cdot \text{KL}(\Pi\mathbf{1} \| p) + \tau \cdot \text{KL}(\Pi^\top \mathbf{1} \| q)
     \]
     其中 \(\epsilon\) 为熵正则化强度，\(\tau\) 控制边际松弛程度。
3. **时间对齐采样策略**：
   - 为提升 mini-batch 中配对质量，利用**动态时间规整（DTW）**计算仿真与真实轨迹间的相似度，然后按相似度权重选择轨迹对，再从中提取时刻样本，使 mini-batch 中包含更多状态相似的配对。
4. **联合训练目标**：
   - 总损失：\(L(f_{\phi}, \pi_{\theta}) = L_{\text{BC}}(f_{\phi}, \pi_{\theta}) + \lambda L_{\text{UOT}}(f_{\phi})\)
   - 行为克隆损失（MSE）监督策略输出，UOT损失正则化编码器，使特征空间域不变且动作相关。

## 3. 实验设计

### 数据集与场景
- **仿真环境**：基于 Robosuite，使用 MimicGen 自动生成 200–1000 条仿真轨迹作为源域数据。
- **真实环境**：Franka Emika Panda 机器人，Intel RealSense D435 相机，采集 10–25 条真实演示。
- **任务套件**：6 种桌面操纵任务：Lift, BoxInBin, Stack, Square, MugHang, Drawer。
- **域迁移设置**：
  - **Sim-to-Sim**：引入视角旋转、点云扰动、纹理变化等视觉域迁移。
  - **Sim-to-Real**：真实世界部署，含分布内（目标区域）和分布外（OOD：新形状、新纹理、新初始位姿）两种测试。
- **观测模态**：RGB 图像 + 点云，分别采用 Diffusion Policy + ResNet18 和 3D Diffusion Policy + PointNet。

### 对比方法
- Source-only：仅用仿真数据训练。
- Target-only：仅用真实数据训练。
- MMD：最小化源-目标域特征均值嵌入距离。
- Co-training：混合仿真和真实数据直接联合训练。
- Ours：本文完整方法。

### 评估指标
- 任务成功率（成功率分为 grasp 和 full task 或 reach/grasp/place 等阶段）。

## 4. 资源与算力
- **文中未明确说明**使用的 GPU 型号、数量及训练总时长。仅在附录的“Experiments compute resources”章节表示已提供充分细节，但实际文本中缺失具体数值（如 GPU 类型、训练轮数等）。因此无法总结具体算力消耗。

## 5. 实验数量与充分性
- **实验数量**充足：包括 6 个任务、2 种观测模态、2 种迁移场景（sim-to-sim 和 sim-to-real）、多种 OOD 变体。
- **消融实验**：
  - 采样策略对比（无采样 vs. 时间对齐采样 vs. Oracle 完美配对）。
  - 超参数敏感性分析（熵正则化系数 \(\epsilon\)、KL 惩罚 \(\tau\)、窗口大小）。
  - 仿真数据量缩放实验（100–1000 条轨迹）。
- **公平性**：所有方法采用相同骨干网络和训练超参数，对比基线合理（包含无域适应、边缘对齐、简单联合训练），且报告了多次 rollout 的平均成功率。
- **充分性**：实验覆盖了多种难度的操纵任务，验证了泛化性；但 OOD 实验次数（如表 2 中每条件仅一个数值）未提供多次重复的方差，论文提及“error bars 不现实”以解释。

## 6. 主要结论与发现
- **H1（复杂任务学习）**：方法在仿真和真实环境中均能有效学习复杂操纵，真实世界平均成功率图像策略 0.73，点云策略 0.77。
- **H2（泛化到仅仿真场景）**：在 OOD 测试中，方法显著优于所有基线（如真实世界 BoxInBin Texture OOD 成功率 0.7 vs. Co-training 的 0.3）。
- **H3（多模态适用性）**：图像和点云输入下均有一致性能提升。
- **H4（仿真数据规模影响）**：增加仿真数据量可显著提升 OOD 泛化性能（见图 4b）。
- **t-SNE 可视化**：本文方法使源和目标特征分布高度重叠，说明成功学习到域不变表示。
- **传输计划可视化**：UOT 能正确对齐状态相似的跨域样本。

## 7. 优点
- **创新性**：首次将非平衡最优传输引入仿真-真实联合训练，巧妙处理数据不平衡问题。
- **实用性**：仅需少量真实演示（10–25 条），大幅降低数据收集成本。
- **通用性**：支持多种观测模态（图像、点云）、多种任务和多种域迁移类型。
- **理论合理**：对齐联合分布优于边缘分布，UOT 允许选择性匹配，避免强制对齐不相似样本。
- **实验完整性**：包含消融、超参数敏感性、数据规模增益分析，验证了每个设计的必要性。

## 8. 不足与局限
- **仅解决视觉域差距**：未处理动作动力学差异，适用于准静态抓取任务。
- **数据依赖**：需要与仿真行为对齐的真实演示（通过相同任务设置），现实适用场景受限。
- **工具限制**：使用 MimicGen 生成仿真数据，继承其局限（仅适用于可抓取、准静态任务）。
- **实验可重复性**：未提供误差棒（error bars），虽说明因真实实验成本高但可能影响统计可靠性。
- **算力细节缺失**：未公开 GPU 型号、训练时间等资源信息，不利于复现与比较效率。

（完）
