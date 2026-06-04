---
title: "EgoBridge: Domain Adaptation for Generalizable Imitation from Egocentric Human Data"
title_zh: EgoBridge：基于域适应的可泛化模仿学习——从自我中心人类数据到机器人
authors: "Ryan Punamiya, Dhruv Patel, Patcharapong Aphiwetsa, Pranav Kuppili, Lawrence Y. Zhu, Simar Kareer, Judy Hoffman, Danfei Xu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=FGMBxzpgis"
tags: ["query:vla"]
score: 8.0
evidence: 提出用于机器人操作端到端模仿学习的域适应方法
tldr: 人类第一人称数据为机器人操作模仿学习提供了丰富资源，但域差异阻碍迁移。EgoBridge使用最优传输对齐策略潜在空间，保留动作相关信息，在多个操作任务上显著提升了迁移成功率，为利用人类数据扩展机器人学习提供了有效框架。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1441, \"height\": 412, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 750, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1378, \"height\": 411, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1380, \"height\": 494, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1438, \"height\": 511, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1418, \"height\": 476, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1431, \"height\": 993, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1419, \"height\": 807, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1433, \"height\": 1250, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-fgmbxzpgis/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1435, \"height\": 1525, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1375, \"height\": 348, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 620, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1442, \"height\": 850, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1099, \"height\": 477, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1144, \"height\": 673, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 930, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1350, \"height\": 398, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-fgmbxzpgis/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1032, \"height\": 241, \"label\": \"Table\"}]"
motivation: 人类自我中心数据与机器人数据之间存在显著域差异，阻碍了模仿学习的迁移。
method: 提出EgoBridge协同训练框架，通过最优传输对齐策略潜在空间，实现域适应。
result: 在多个机器人操作任务上，迁移成功率大幅提升。
conclusion: 域适应是提升人类数据到机器人模仿学习泛化性的关键。
---

## Abstract
Egocentric human experience data presents a vast resource for scaling up end-to-end imitation learning for robotic manipulation. However, significant domain gaps in visual appearance, sensor modalities, and kinematics between human and robot impede knowledge transfer. This paper presents EgoBridge, a unified co-training framework that explicitly aligns the policy latent spaces between human and robot data using domain adaptation. Through a measure of discrepancy on the joint policy latent features and actions based on Optimal Transport (OT), we learn observation representations that not only align between the human and robot domain but also preserve the action-relevant information critical for policy learning. EgoBridge achieves a significant absolute policy success rate improvement by 44% over human-augmented cross-embodiment baselines in three real-world single-arm and bimanual manipulation tasks. EgoBridge also generalizes to new objects, scenes, and tasks seen only in human data, where baselines fail entirely. Videos and additional information can be found at https://ego-bridge.github.io/

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：机器人行为克隆需要大量高质量示范数据，但采集机器人遥操作数据成本高、难以规模化。人类自我中心数据（如穿戴设备录制的第一人称视频）丰富且易获取，但人类与机器人在视觉外观、传感器模态、运动学等方面存在显著域差异，阻碍知识迁移。
- **核心问题**：如何有效利用大量人类自我中心数据辅助机器人策略学习，克服跨实体域差异，实现从人类到机器人的泛化迁移（包括新物体、新场景乃至新行为）。
- **整体含义**：提出一种统一协同训练框架，通过域适应对齐人类与机器人策略潜在空间，使机器人能从人类示范中学习，从而大幅扩展机器人学习的规模与泛化能力。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将人类-机器人跨实体学习形式化为域适应问题，利用最优传输（Optimal Transport, OT）对齐联合的潜在特征-动作分布，同时保留动作相关信息。
- **关键技术细节**：
  - **联合域适应损失**：对每个小批量的人类和机器人数据，计算Sinkhorn正则化OT计划，对齐联合分布（潜在特征 + 动作轨迹）。损失 `L_OT-joint` 作用于特征编码器 `f_ϕ`。
  - **动作感知成本函数设计**：使用动态时间规整（DTW）计算人类与机器人动作序列的距离，找出每个机器人样本最相似的人类样本作为“伪配对”，并在OT成本矩阵中对该配对给予折扣（乘以小系数 λ），鼓励OT将行为相似的样本对齐。
  - **协同训练目标**：总损失 = 行为克隆损失（`L_BC-cotrain`）+ α · `L_OT-joint`，联合优化编码器 `f_ϕ` 和策略解码器 `π_θ`。
  - **网络架构**：共享Transformer编码器-解码器结构。编码器包含模态特定的stem（视觉、本体感觉、手腕相机等）和共享的trunk；解码器采用DETR风格，含可学习动作token，通过自注意力和交叉注意力生成动作块。
- **算法流程**（文字说明）：
  1. 从人类数据集和机器人数据集中各采样一批大小为B的样本。
  2. 通过共享编码器提取潜在特征 `z_H` 和 `z_R`。
  3. 计算DTW成本矩阵 `A`，找出每个机器人样本最优匹配的人类样本 `i*(j)`。
  4. 构造形状化成本矩阵 `C̃`：对最优配对成本乘以 λ < 1，其余为特征欧氏距离。
  5. 计算Sinkhorn OT计划，得到 `L_OT-joint`。
  6. 计算BC损失（预测动作 vs 真实动作）。
  7. 联合优化编码器和策略解码器。

## 3. 实验设计：数据集/场景、benchmark、对比方法

- **模拟实验**（Push-T平面推物体任务）：
  - 源域（人类）: 蓝色圆形推杆，紫色背景、镜像T形物体；目标域（机器人）: 三角推杆，白色背景、标准T形。
  - 评估三种泛化情形：原始场景、仅背景色变化、背景色+镜像T。
  - benchmark：平均奖励（max IoU）和成功率（≥0.9）。
  - 对比方法：Target-only BC、Co-train、Standard OT（边际对齐）、MMD（最大均值差异）。
- **真实世界实验**（三个操作任务）：
  - **Drawer（抽屉）**：抓取玩具放入抽屉并关闭。机器人数据覆盖3/4抽屉象限，人类数据覆盖全部4象限。评估行为泛化（新象限）。
  - **Scoop Coffee（舀咖啡）**：用勺舀咖啡豆倒入目标容器。机器人数据仅含一个场景和一个目标（罐），人类数据含两个场景和一个新目标（研磨机）。评估物体泛化和场景泛化。
  - **Laundry（洗衣）**：双臂折叠衬衫。机器人数据含3种衬衫，人类数据更丰富。评估泛化。
  - 对比方法：Robot-only BC、Co-train、EgoMimic、MimicPlay、ATM。每个任务报告成功率（SR）和子任务得分（Pts）。
- **消融实验**：在Drawer任务上对EgoBridge的DTW配对、联合OT、去除对齐损失进行消融。

## 4. 资源与算力

- **真实世界实验**：在单张NVIDIA L40s GPU上训练，Drawer任务训练100k迭代，Scoop Coffee 120k迭代，Laundry 110k迭代，约需24小时。
- **模拟实验**：在单张NVIDIA A40 GPU上训练130k迭代，约2小时。
- **超参数**：批量大小32，学习率5e-5（真实）或1e-4（模拟），优化器AdamW，学习率调度器线性衰减（真实）或余弦退火（模拟），OT损失权重α=0.7（真实）或0.2（模拟），DTW折扣系数λ=0.05，Sinkhorn正则化ε=0.05（真实）或0.01（模拟）。

## 5. 实验数量与充分性

- **实验数量**：涉及1个模拟环境 + 3个真实任务；共对比6种基线；在真实任务中进行了9组子实验（in-distribution、物体泛化、场景泛化、行为泛化）；消融实验1组；额外在Laundry上进行了2组泛化测试（表8）；模拟实验中进行了3组评估。
- **充分性与公平性**：
  - 实验设计覆盖了从模拟到真实、从域内到域外、从物体/场景泛化到行为泛化的多层次评估。
  - 所有基线均采用相同或匹配的骨干网络；使用固定随机种子；多次重复（如Drawer任务48次试验，Scoop Coffee 15次，Laundry 18次）。
  - 实验较为充分，结果具有说服力。但未报告误差棒（由于物理机器人实验成本，作者说明了理由），但总体实验设计客观。

## 6. 论文的主要结论与发现

- **H1 验证**：在域内任务上，EgoBridge比所有基线提升显著（绝对成功率提升7%~44%），表明对齐潜在空间有助于跨实体迁移。
- **H2 验证**：在物体泛化（Scoop Coffee新目标/新场景）、行为泛化（Drawer新象限）上，EgoBridge表现突出（27%~33%成功率），而大多基线完全失败。
- **H3 验证**：TSNE可视化显示EgoBridge的潜在空间比基线更高度重叠（Wasserstein距离更小），且K近邻配对语义更一致（相同动作阶段）。
- **消融结论**：DTW配对比MSE配对更重要；联合OT优于边际对齐；移除对齐损失导致泛化能力丧失。

## 7. 优点

- **方法论创新**：将最优传输用于跨实体模仿学习的潜在空间对齐，且利用DTW构建动作感知的成本函数，保留了动作相关信息，避免传统域适应丢失细节。
- **实验设计全面**：从模拟到真实，从域内到域外，涵盖物体、场景、行为多种泛化层次；对比了多种最新基线。
- **结果显著**：在最具挑战性的行为泛化（Drawer新象限）上实现了33%成功率，而其他方法几乎为0，证明了方法的有效性。
- **消融充分**：验证了每个设计组件的必要性，提供了深入的分析。

## 8. 不足与局限

- **DTW局限性**：DTW成本假设动作序列可比较，在多任务联合学习场景下可能不够信息丰富（例如不同任务的动作模式差异大）。
- **未涉及无动作标签数据**：当前方法依赖人类数据中的动作标签（如手部姿态），未探索从互联网无标签视频中学习，限制了数据来源的扩展。
- **计算成本**：需要联合训练编码器和策略，训练时长约24小时（真实任务），对计算资源有一定要求。
- **实验覆盖**：虽然任务多样，但仍限于单一桌面操作场景；未测试动态环境或长时间序任务；未提供误差棒，统计显著性未明确展示。
- **应用限制**：当前针对单任务迁移，未来需扩展至多任务或开放世界场景。

（完）
