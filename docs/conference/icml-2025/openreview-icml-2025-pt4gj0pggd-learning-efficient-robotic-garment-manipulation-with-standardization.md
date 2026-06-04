---
title: Learning Efficient Robotic Garment Manipulation with Standardization
title_zh: 通过标准化学习高效机器人衣物操作
authors: "Changshi Zhou, Feng Luan, hujiarui, Shaoqiang Meng, Zhipeng Wang, Yanchao Dong, Yanmin Zhou, Bin He"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=pT4gJ0PgGD"
tags: ["query:vla"]
score: 4.0
evidence: 机器人衣物操作与标准化
tldr: 衣物操作因复杂动力学和自遮挡困扰机器人，现有方法忽视标准化。本文提出APS-Net，统一展开与标准化框架，采用双臂多原语策略，动态抖动快速展开、抓放精确对齐。实验证明该方法显著提升后续折叠等任务效率。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1576, \"height\": 780, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1778, \"height\": 986, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1656, \"height\": 650, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 777, \"height\": 252, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 869, \"height\": 308, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1730, \"height\": 883, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 861, \"height\": 286, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 849, \"height\": 323, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 863, \"height\": 530, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1733, \"height\": 943, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 865, \"height\": 294, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1753, \"height\": 845, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 861, \"height\": 216, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1780, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1730, \"height\": 663, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 864, \"height\": 803, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 848, \"height\": 719, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-pt4gj0pggd/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 863, \"height\": 308, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 894, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 646, \"height\": 173, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 857, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 859, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 794, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 561, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-pt4gj0pggd/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 610, \"height\": 136, \"label\": \"Table\"}]"
motivation: 现有衣物展开方法忽视标准化对下游任务的重要性。
method: 提出统一展开与标准化的APS-Net，使用双臂多原语策略（动态抖动与抓放）。
result: 在衣物操作任务上取得高成功率和标准化效果。
conclusion: 标准化是简化衣物操作的关键，APS-Net有效结合展开与对齐。
---

## Abstract
Garment manipulation is a significant challenge for robots due to the complex dynamics and potential self-occlusion of garments. Most existing methods of efficient garment unfolding overlook the crucial role of standardization of flattened garments, which could significantly simplify downstream tasks like folding, ironing, and packing. This paper presents APS-Net, a novel approach to garment manipulation that combines unfolding and standardization in a unified framework. APS-Net employs a dual-arm, multi-primitive policy with dynamic fling to quickly unfold crumpled garments and pick-and-place(p&p)  for precise alignment. The purpose of garment standardization during unfolding involves not only maximizing surface coverage but also aligning the garment’s shape and orientation to predefined requirements. To guide effective robot learning, we introduce a novel factorized reward function for standardization, which incorporates garment coverage (Cov), keypoint distance (KD), and intersection-over-union (IoU) metrics. Additionally, we introduce a spatial action mask and an Action Optimized Module to improve unfolding efficiency by selecting actions and operation points effectively. In simulation, APS-Net outperforms state-of-the-art methods for long sleeves, achieving 3.9% better coverage, 5.2% higher IoU, and a 0.14 decrease in KD (7.09% relative reduction). Real-world folding tasks further demonstrate that standardization simplifies the folding process. Project page: https://hellohaia.github.io/APS/

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：机器人对衣物等柔性物体的操作极具挑战性，尤其在下游任务（如折叠、熨烫、包装）中，现有衣物展开方法普遍忽视了“标准化”（standardization）的关键作用——即不仅最大化衣物展开面积，还需将衣物的形状、朝向与预设目标对齐，保持关键点可见。
- **研究动机**：现有方法（如单臂多次抓取或仅依赖动态抖动）虽能提高覆盖率，但未能保证标准化，导致后续折叠等下游任务失败率高、效率低。本文旨在将展开与标准化统一到一个框架中，简化后续操作。
- **整体含义**：通过双臂多原语策略（动态抖动+精确抓放）实现快速展开与精确对齐，证明标准化显著提升下游折叠的成功率与效率。

## 2. 方法论：核心思想、关键技术细节与算法流程
- **核心思想**：提出Action-Primitive Selector Network (APS-Net)，一个自监督学习网络，根据当前RGB-D图像智能选择动作原语（动态fling或精细p&p），以最少的步骤将任意揉皱的衣物展开成标准状态。
- **关键技术细节**：
  - **动作原语定义**：
    - *Fling*：双臂抓取衣物上两个预定义点，提升、拉伸，然后向前-向后摆动并逐渐放下。
    - *Pick-and-place (p&p)*：单臂抓取指定点，提升，移动到目标放置点，释放。
    - *Fold*：基于关键点检测执行启发式折叠。
  - **APS-Net结构**：输入为一批经过旋转和缩放的RGB-D图像，通过三个编码器（分别对应覆盖率、IoU、关键点奖励）产生两个解码器对（fling和p&p），输出空间动作图。选择最大期望值的动作类型和参数。
  - **因子化奖励函数**：`R_CIK = α·Cov + β·IoU + (1-α-β)·R_Keypoint`，其中Cov为覆盖率，IoU为与目标模板的交并比，Keypoint为关键点距离（负值）。
  - **空间动作掩码 (SAM)**：过滤无效动作（如超出工作空间或导致双臂碰撞），通过工作空间掩码与衣物掩码交集，将概率设为-∞来排除。
  - **动作优化模块 (AOM)**：在fling动作中，若预测的抓取点与肩部关键点距离<5像素，则替换为肩部关键点，加速平整。
- **算法流程**（文字说明）：
  1. 输入当前观测RGB-D图，经16种旋转和5种缩放得到80个变换图。
  2. APS-Net计算每个变换图上fling和p&p的空间动作图。
  3. 取所有变换图的最大值，比较fling组与p&p组的最大值，选择动作原语。
  4. 应用空间动作掩码，选出最优点(x,y)及对应的旋转角θ和宽度w。
  5. 执行选定动作（fling或p&p），获得新状态。
  6. 重复直至覆盖率>0.8，进入折叠阶段。
  7. 折叠阶段：DeepLabv3检测关键点，基于启发式规则（根据衣物类型）执行多步折叠。

## 3. 实验设计
- **数据集与场景**：
  - **模拟环境**：基于PyFleX和SoftGym搭建的Cloth Action Gym，支持加载CLOTH3D数据集中的衣物网格（长袖、裤子、裙子）。训练集每个类别2000个任务，测试集50个未见衣物网格。
  - **真实世界**：两台UR5 + Robotiq 2F-85夹爪，Azure Kinect和Realsense D455顶置RGB-D相机。采用Grounded-SAM分割衣物，通过仿射变换减小sim-to-real gap。
- **基准方法**：
  - *P&P*：仅准静态抓放。
  - *S-FLING*：仅单次fling。
  - *FLINGBOT*：双臂动态抖动，以覆盖率为奖励。
  - *CLOTH FUNNELS*：结合p&p和fling，基于粒子距离的因子化奖励。
- **评价指标**：覆盖率(Cov)、交并比(IoU)、关键点距离(KD)、成功率(SR)。
- **对比方式**：每种方法在模拟中对长袖衣物进行50次随机初始状态试验；真实世界中每组15次试验。

## 4. 资源与算力
- 文中附录E明确给出：所有实验在 **NVIDIA RTX 4090 GPU (24GB)**、**Intel i9-13900K CPU (5.80 GHz)**、**64GB RAM**、**Ubuntu 18.04 LTS** 上运行。
- APS-Net训练100,000步，关键点检测训练200 epochs。
- 未提及具体训练总时长或使用的GPU数量（推测为单卡RTX 4090）。

## 5. 实验数量与充分性
- **模拟实验**：对长袖衣物，每个方法做50次试验，共4个基线+本方法=5种方法，总计250次模拟试验。此外对裤子和裙子各50次测试本方法。
- **消融实验**：3种消融（去除AOM、去除IoU奖励、去除关键点奖励），每种50次。
- **参数敏感性**：5组α/β组合测试。
- **真实世界实验**：长袖衣物每个方法15次（共4×15=60次）；其余衣物（裤子、裙子）各15次折叠试验。
- **充分性评价**：实验数量在学术论文中属中等水平，覆盖了主要对比和消融。但真实世界仅15次/组，统计显著性略弱；未对不同颜色、纹理、初始褶皱程度进行系统变化（仅文中图16展示了4种不同颜色和纹理）。总体较充分，但可进一步增加真实世界试验次数及更多样化场景。

## 6. 主要结论与发现
- APS-Net在模拟中显著优于所有基线：长袖衣物覆盖率91.1%（比最佳基线CLOTH FUNNELS高3.9%），IoU 79.3%（高5.2%），KD 1.832（降低7.09%）。
- 真实世界中，APS-Net的展开覆盖率86.3%（比CLOTH FUNNELS高4.1%），IoU 70.5%（高5.3%）；折叠成功率12/15（80%），远超其他方法。
- 标准化（覆盖率+对齐+关键点保持）是简化下游折叠任务的关键因素；因子化奖励函数、空间动作掩码和动作优化模块各自贡献显著。
- 方法在不同衣物类别（长袖、裤子、裙子）上具有泛化能力。

## 7. 优点
- **统一框架**：首次将展开与标准化端到端结合，通过动作选择网络自动切换粗粒度fling和细粒度p&p，兼顾效率与精度。
- **因子化奖励函数**：明确融合覆盖率、IoU和关键点距离，直接指导标准化，避免仅优化覆盖率导致的局部最优。
- **空间动作掩码**：有效过滤无效动作，减少无效尝试，提高样本效率和安全性。
- **动作优化模块**：通过关键点先验知识引导fling动作，加速平整。
- **使用RGB-D输入**：在模拟中引入随机质量、刚度、程序化褶皱，减小sim-to-real gap，实现模拟到真实的迁移。
- **真实实验验证**：不仅评估展开，还评估下游折叠，证明标准化的实际价值。

## 8. 不足与局限
- **真实世界试验数量偏少**：每组仅15次，统计波动可能较大，未能提供置信区间或显著性检验。
- **衣物类型覆盖有限**：仅测试了长袖、裤子、裙子三类，且均来自CLOTH3D数据集；未测试更复杂的衣物（如带扣、开衫、多层衣物）。
- **依赖关键点检测质量**：折叠阶段使用DeepLabv3检测关键点，其性能受训练数据质量和sim-to-real gap影响，未评估关键点检测错误对折叠成功率的影响。
- **未与多种最新方法对比**：基线中未包含近期基于大模型或扩散策略的方法（如UniGarmentManip、GPT-Fabric等）。
- **未讨论失败案例分析**：文中未分析失败试验的具体原因（如抓取失败、关键点检测错误、碰撞等），削弱了可解释性。
- **假设标准化的目标模板已知**：论文假设预定义的目标形状和关键点位置，对于未见衣物类型需重新定义模板，限制了即时泛化能力。
- **计算开销**：每次动作需处理80个变换图（16旋转×5尺度），实时性可能受限；未报道实际动作耗时或推理时间。

（完）
