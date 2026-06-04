---
title: "PointMapPolicy: Structured Point Cloud Processing for Multi-Modal Imitation Learning"
title_zh: PointMapPolicy：结构化点云处理用于多模态模仿学习
authors: "Xiaogang Jia, Qian Wang, Anrui Wang, Han A. Wang, Balázs Gyenes, Emiliyan Gospodinov, Xinkai Jiang, Ge Li, Hongyi Zhou, Weiran Liao, Xi Huang, Maximilian Beck, Moritz Reuss, Rudolf Lioutikov, Gerhard Neumann"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=ZR2mdBrhJX"
tags: ["query:vla"]
score: 8.0
evidence: 基于结构化点云网格的扩散策略用于机器人操纵模仿学习
tldr: 机器人操纵系统需要几何和语义信息的互补，但现有点云方法丢失细节、RGB方法缺乏几何意识。本文提出PointMapPolicy，将扩散策略条件建立在结构化点网格上，无需下采样保留细粒度几何信息。该数据表示易于提取形状和空间关系，支持参考帧变换。在多项操纵任务中，该方法在精度和泛化性上显著优于现有基线。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1147, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1423, \"height\": 477, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 647, \"height\": 170, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1444, \"height\": 574, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1447, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1406, \"height\": 332, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 783, \"height\": 331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1159, \"height\": 687, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1163, \"height\": 695, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1160, \"height\": 691, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1161, \"height\": 693, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1157, \"height\": 687, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zr2mdbrhjx/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1161, \"height\": 692, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-zr2mdbrhjx/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1435, \"height\": 598, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zr2mdbrhjx/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1284, \"height\": 726, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zr2mdbrhjx/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 616, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zr2mdbrhjx/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1443, \"height\": 868, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zr2mdbrhjx/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1441, \"height\": 552, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zr2mdbrhjx/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1013, \"height\": 767, \"label\": \"Table\"}]"
motivation: 现有点云和RGB方法在机器人操纵中分别面临细粒度丢失和几何信息不足的问题。
method: 提出结构化点网格表示，在不下采样的情况下将扩散策略条件建立在规则网格上，增强几何感知。
result: 在多个操纵任务上实现更高精度和泛化性，证明结构化点云表示的有效性。
conclusion: PointMapPolicy为多模态模仿学习提供了一种高效、精确的点云处理范式。
---

## Abstract
Robotic manipulation systems benefit from complementary sensing modalities, where each provides unique environmental information.
Point clouds capture detailed geometric structure, while RGB images provide rich semantic context. Current point cloud methods struggle to capture fine-grained detail, especially for complex tasks, which RGB methods lack geometric awareness, which hinders their precision and generalization. We introduce PointMapPolicy, a novel approach that conditions diffusion policies on structured grids of points without downsampling. The resulting data type makes it easier to extract shape and spatial relationships from observations, and can be transformed between reference frames. Yet due to their structure in a regular grid, we enable the use of established computer vision techniques directly to 3D data. Using xLSTM as a backbone, our model efficiently fuses the point maps with RGB data for enhanced multi-modal perception.
Through extensive experiments on the RoboCasa and CALVIN benchmarks and real robot evaluations, we demonstrate that our method achieves state-of-the-art performance across diverse manipulation tasks. The overview and demos are available on our project page: https://point-map.github.io/Point-Map/

---

## 论文详细总结（自动生成）

# 论文总结：PointMapPolicy

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：机器人操纵系统依赖多模态感知（点云提供几何结构，RGB提供语义信息），但现存方法存在关键缺陷：
  - 现有点云方法（如DP3）通过最远点采样（FPS）过度下采样，丢失细粒度几何细节，难以满足精确操纵需求。
  - RGB 方法缺乏三维几何感知，对视角和光照变化敏感，在复杂三维场景中精度和泛化性不足。
- **整体含义**：需要一种既能保留密集几何信息、又能利用成熟二维视觉处理技术的结构化三维表示方法，以弥合3D几何与2D视觉架构之间的鸿沟，提升多模态模仿学习的性能。

## 2. 方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：将深度图转换为**点地图（Point Map）**——一种与 RGB 图像具有相同空间维度的规则网格，每个像素存储对应的三维点坐标（XYZ）。点地图保留了密集几何细节，且可直接输入标准视觉编码器（如 ResNet、ConvNeXt、ViT），无需 FPS、KNN 等昂贵操作。将点地图与 RGB 图像以多种方式融合，并基于 xLSTM 骨干网络构建扩散策略。
- **关键技术细节**：
  1. **点地图生成**：利用相机内参将深度图 \( D \) 反投影为世界坐标下的点地图 \( M_t = \phi(D, K_{\text{int}}^{-1}) \in \mathbb{R}^{H \times W \times 3} \)，并剔除超出深度范围的像素。多视图点地图可通过外参变换到统一参考帧并拼接。
  2. **多模态融合**：探索三种融合策略：**Add**（逐元素相加）、**Cat**（直接拼接所有模态和视图的token）、**Attn**（使用交叉注意力模块融合）。实验发现 **Cat** 略优，作为最终方案。
  3. **骨干网络**：采用 **xLSTM** 作为扩散策略骨干（X-Block），替代传统 Transformer。xLSTM 具有线性复杂度，在保持序列建模能力的同时显著降低计算和内存开销，适合实时或资源受限场景。
  4. **扩散策略**：基于 EDM 框架进行连续时间动作扩散，使用分数匹配损失训练神经网络 \( D_\theta \)：  
     \[
     L_{\text{SM}} = \mathbb{E}_{\sigma, \bar{a}, \epsilon} \left[ \alpha(\sigma_t) \| D_\theta(\bar{a} + \epsilon, s, \sigma_t) - \bar{a} \|_2^2 \right]
     \]  
     推理时采用 DDIM 求解器，仅需 4 步去噪即可生成动作序列。
- **算法流程**：  
  输入多视图 RGB-D 图像 + 语言指令 → 将深度图转换为点地图 → 分别用视觉编码器提取 RGB 和点地图的 token → 拼接所有 token（含语言 token）→ 加入可学习位置编码 → 送入 xLSTM X-Block 进行扩散去噪 → 输出动作序列。

## 3. 实验设计
- **数据集 / 场景**：
  - **RoboCasa**：大规模家庭操纵模拟基准，选取 16 个任务（涵盖拾取、抽屉、旋钮、杠杆、按钮、插入等 6 类技能），每个任务提供 50 个人工演示。
  - **CALVIN**：长期语言条件操纵基准，采用标准 **ABC→D** 设置（在 A/B/C 环境训练，零样本迁移到 D 环境），评估 1000 条任务链的平均完成长度。
  - **真实机器人**：Franka Panda 机械臂 + 两个 Orbbec Femto Bolt 相机，包含 6 个任务（整理、折叠、叠杯、抽屉、倒水、清扫），每任务 45–120 个演示。
- **对比方法**：
  - **RoboCasa 基线**：Behavioral Cloning (BC)、GR00T-N1、DP3、3D Diffuser Actor (3DA)，以及仅 RGB / 仅 Depth 的消融版本。
  - **CALVIN 基线**：RoboFlamingo、SuSIE、GR-1、OpenVLA、CLOVER、MoDE、Seer 等，区分是否使用预训练。
  - **点云编码消融**：PointNet-xyz、PointNet-color、PointPatch、3D-Lifting，均基于相同 xLSTM 骨干。
  - **融合消融**：Add、Cat、Attn。
  - **视觉编码器消融**：ResNet50、ConvNeXt-v2、DaViT。

## 4. 资源与算力
- **CALVIN 实验**：4 × Nvidia RTX 6000 Ada GPU，batch size 512（每 GPU 128），10 个 x-Block（512 隐层），147M 参数。每 epoch ~13 分钟，完整训练 25 epoch 约 6 小时（不含评估）。
- **RoboCasa 实验**：1 × NVIDIA A100-SXM4-40GB，batch size 128，8 个 x-Block（768 隐层），111M 参数。
- **真实机器人实验**：1 × Nvidia RTX 6000 Ada GPU，batch size 128，6 个 x-Block（256 隐层），96M 参数。
- **推理速度**（单 Nvidia RTX 5080，batch size=1）：PMP-xyz 平均 2.9 ms，PMP 平均 3.9 ms，满足实时要求。

## 5. 实验数量与充分性
- **实验数量**：
  - RoboCasa：16 个任务 × 5 种方法（+ 多种消融变体），每任务 50 个测试 episode，3 个随机种子，报告最佳 checkpoint 结果及标准差。
  - CALVIN：1000 条指令链评估，报告 1–5 步的成功率及平均长度。对比了 17 种方法（含预训练和从头训练）。
  - 真实世界：6 个任务 × 3 种方法（RGB、PMP-xyz、PMP），每任务 20 次评估，取最佳 checkpoint。
  - 消融研究：点云编码 4 种、融合 3 种、视觉编码器 3 种，均在 RoboCasa 的 6 大类任务上报告平均成功率。
- **充分性与公平性**：
  - 在 RoboCasa 和 CALVIN 上，PMP 与当前最优方法（包括 DP3、3DA、Seer、MoDE 等）进行系统比较，控制骨干架构或确保相同实验条件。
  - 消融实验固定骨干网络，只改变点云编码或融合方式，有效隔离了贡献来源。
  - 结果包含标准差/置信区间，实验设置清晰，结论具有统计显著性。

## 6. 主要结论与发现
- **PMP 在多基准上达到或超越 SOTA**：RoboCasa 上 PMP-xyz 平均成功率达 49.12%（领先 DP3 约 20%）；CALVIN 上 PMP 平均完成长度 4.01（从头训练的方法中最高，甚至超过部分预训练方法如 Seer-Large scratch 的 3.83）。
- **点地图优于传统点云编码**：在相同 xLSTM 骨干下，PMP-xyz 显著优于 PointNet、PointPatch、3D-Lifting 等编码方式。
- **多模态融合的优势**：PMP 融合 RGB 和点地图后，在形状任务和颜色任务上均取得最佳结果，而纯几何（PMP-xyz）在颜色依赖任务（CALVIN）上明显下降，说明语义与几何互补。
- **视觉编码器通用性**：ConvNeXt-v2 在点地图处理上表现最优，但 ResNet50 和 DaViT 同样有效，证明点地图可直接利用成熟 2D 架构。
- **计算效率高**：xLSTM 骨干训练速度快（CALVIN 仅 6 小时），推理延迟低至 3.9 ms。

## 7. 优点
- **结构化表示创新**：将无序点云转化为规则网格，无需下采样即保留完整几何信息，同时兼容标准卷积/注意力架构，简化了模型设计。
- **高效融合框架**：通过将点地图与 RGB 在同等空间分辨率下编码，支持多种灵活融合策略，且基于 xLSTM 的扩散策略在内存和速度上大幅优于 Transformer 方案。
- **广泛的实验验证**：在模拟和真实机器人上均进行严格评估，覆盖多种任务类型、消融分析及与多种基线的公平对比，结论可靠。
- **可观的实际部署潜力**：推理延迟极低，算力需求适中，适合实时机器人控制。

## 8. 不足与局限
- **融合方式可能不够精细**：当前最佳融合（Cat）仅是简单拼接，可能未充分利用模态间的互补关系，更复杂的交叉注意力或自适应融合可能提升性能。
- **点地图编码器缺乏预训练**：RGB 编码器得益于 ImageNet 预训练，而点地图编码器从头训练，限制了特征表达能力。后续可研究点地图专用预训练目标。
- **对颜色信息的依赖**：在颜色区分关键的场景（如 CALVIN “红色方块” 指令），纯几何表示（PMP-xyz）表现较差，暗示多模态融合对任务领域有敏感性。
- **深度传感器噪声敏感性**：点地图依赖于深度图质量，在真实环境中可能因传感器噪声或遮挡引入误差，文中未专门分析鲁棒性。
- **泛化性评估范围有限**：虽然包含零样本迁移（CALVIN ABC→D），但未测试跨物体类别、跨机器人构型等更极端的泛化场景。

（完）
