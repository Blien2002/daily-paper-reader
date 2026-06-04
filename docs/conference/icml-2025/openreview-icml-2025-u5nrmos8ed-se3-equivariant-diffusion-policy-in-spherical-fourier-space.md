---
title: SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space
title_zh: 球面傅里叶空间中的SE(3)等变扩散策略
authors: "Xupeng Zhu, Fan Wang, Robin Walters, Jane Shi"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=U5nRMOs8Ed"
tags: ["query:vla"]
score: 9.0
evidence: 用于机器人操作的SE(3)等变扩散策略
tldr: 扩散策略在操作任务中效果好，但泛化到新物体排列困难。本文提出球面扩散策略(SDP)，一种SE(3)等变扩散策略，通过将状态、动作和去噪过程嵌入球面傅里叶空间实现等变性，并设计球面FiLM层和去噪时间U-Net。实验表明，SDP在多个操作任务中显著提升了泛化能力和实际性能，为端到端操作策略提供了有效的等变方法。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 801, \"height\": 641, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1700, \"height\": 548, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1760, \"height\": 485, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1643, \"height\": 326, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1766, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 787, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1388, \"height\": 905, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1683, \"height\": 1222, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1640, \"height\": 1549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1697, \"height\": 1484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-u5nrmos8ed/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1433, \"height\": 849, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1500, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1666, \"height\": 454, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 866, \"height\": 214, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 855, \"height\": 291, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 801, \"height\": 166, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 827, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1653, \"height\": 297, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-u5nrmos8ed/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1357, \"height\": 496, \"label\": \"Table\"}]"
motivation: 现有扩散策略对三维空间新物体排列泛化性差。
method: 将状态、动作和去噪过程嵌入球面傅里叶空间实现SE(3)等变。
result: 在操作任务中提升泛化能力和实际性能。
conclusion: SE(3)等变是提升操作策略泛化的有效方法。
---

## Abstract
Diffusion Policies are effective at learning closed-loop manipulation policies from human demonstrations but generalize poorly to novel arrangements of objects in 3D space, hurting real-world performance. To address this issue, we propose Spherical Diffusion Policy (SDP), an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene. Such equivariance is achieved by embedding the states, actions, and the denoising process in spherical Fourier space. Additionally, we employ novel spherical FiLM layers to condition the action denoising process equivariantly on the scene embeddings. Lastly, we propose a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency. In the end, SDP is end-to-end SE(3) equivariant, allowing robust generalization across transformed 3D scenes. SDP demonstrates a large performance improvement over strong baselines in 20 simulation tasks and 5 physical robot tasks including single-arm and bi-manual embodiments. Code is available at https://github.com/amazon-science/Spherical_Diffusion_Policy.

---

## 论文详细总结（自动生成）

# 论文总结：SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有扩散策略（Diffusion Policy）在模仿人类演示学习闭环操作策略方面效果良好，但在面对三维空间中物体新的排列（如任意3D位姿）时泛化能力差，导致真实世界性能下降。主要原因是缺乏对场景3D变换的适应性，需要大量数据覆盖所有可能的3D排列。
- **意义**：提出一种**SE(3)等变扩散策略**，使模型能够自动适应场景的3D旋转和平移变化，无需额外数据即可泛化到未见过的3D场景，显著提升样本效率和真实世界部署能力。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：通过将状态、动作和去噪过程嵌入**球面傅里叶空间**，实现端到端的SE(3)等变性（旋转等变+平移不变）。平移不变性通过相对动作公式（将状态/动作规范化到夹爪坐标系）实现；旋转等变性通过球面傅里叶系数和等变网络结构保证。
- **关键技术细节**：
  - **球面傅里叶表示**：将端效应器的6D位姿（位置+旋转+夹爪开度）表示为球面傅里叶系数（位置和旋转用degree-1向量，夹爪开度为标量）。点云观测通过EquiformerV2编码为球面特征。
  - **球面去噪时间U-Net (SDTU)**：1D U-Net结构，使用混合通道时间卷积（在每个球面傅里叶degree上分别做时间卷积）实现时空等变。包含下采样/上采样、球面激活、球面FiLM层。
  - **球面FiLM层 (SFiLM)**：扩展Feature-wise Linear Modulation，从场景条件C中投影出缩放γ和偏移β（均为球面特征），然后对隐藏特征hl进行调制：`SFiLM(hl|γl,βl) = (γl^T hl) * (hl/||hl||) + βl`，并证明该操作是SO(3)等变的。
- **公式与算法流程**：去噪过程遵循标准DDPM公式：`A^{k-1} = α(A^k - γ ε_θ(S, A^k, k)) + z`，其中去噪函数ε_θ由编码器、SDTU和SFiLM组成。训练目标为预测添加的噪声：`L = ||ε_θ(S, A^0 + ε, k) - ε||^2`。

## 3. 实验设计
- **数据集/场景**：
  - **仿真实验**：使用MimicGen环境（基于MuJoCo），包含20个任务（4个带SE(3)初始化的任务 + 12个原始SE(2)初始化任务）。观测为RGBD图像，可重建体素或点云。
  - **物理实验**：5个真实机器人任务（单臂：转杠杆、推橡皮；双臂：抓盒子、翻书、打包），使用两个UR5e机械臂，两个RGBD相机采集点云。
- **Benchmark**：对比方法包括：
  - EquiDiff (SO(2)等变，基于图像或体素)
  - DiffPo-C/T (原始扩散策略，卷积/Transformer骨干)
  - EquiBot (SO(3)等变，仅degree-1表示，需分割预处理)
  - DP3 (点云扩散策略)
  - ACT (动作分块Transformer)
  - BC-RNN (GMM+RNN)
  - ET-SEED (未参与仿真对比，因代码未公开)
- **评估指标**：成功率（仿真取50次rollout平均，物理取20次）。

## 4. 资源与算力
- 论文**未明确说明**训练使用的GPU型号、数量、训练时长。
- 仅在表6中提及推理时间测试使用“a commercial GPU with 24GB RAM”（未指定型号），SDP推理时间0.44秒，训练批量大小32。其他基线如ET-SEED在同样GPU上推理需29.4秒且批量仅1。
- 因此，算力信息不完整，无法量化。

## 5. 实验数量与充分性
- **实验数量**：仿真20个任务（4个SE(3)变体 + 12个SE(2)），物理5个任务。每个任务多次随机种子（仿真3个种子）和rollout（仿真50次、物理20次）。此外进行了多组消融实验（6种变体）、degree l的影响、样本效率分析（不同数据集大小）和推理速度对比。
- **充分性与公平性**：
  - 对比了多种主流基线，覆盖不同等变类型（离散SO(2)、SO(3)、无等变）。
  - 物理实验中与仿真中表现最好的两个基线（EquiDiff、DiffPo-C）对比，且使用相同训练演示数（仅30-66个）。
  - 消融实验剥离了相对动作、球面表示、等变等关键组件，验证各组件贡献。
  - 样本效率分析展示了SDP在数据量较少时的优势（100个演示即达48.5%成功率，是EquiDiff的2.4倍）。
  - 但物理实验仅使用一个种子（未说明多随机种子），且部分任务（如Flip Book）SDP仍有显著失败情况，公平性略受限于种子数。

## 6. 主要结论与发现
- SDP在大多数仿真和物理任务上显著优于所有基线，尤其在SE(3)初始化（随机倾斜桌面）的大角度偏移下，优势更加明显（表1）。
- 球面傅里叶表示（degree≥2）比Vector Neuron（仅degree-1）更有效，能捕获更丰富的形状信息。
- 相对动作公式（平移不变性）对泛化至关重要，但球面表示比相对动作更重要（消融对比表4）。
- 样本效率：SDP用100个演示即达到EquiDiff用1000个演示的性能（48.5% vs 44.5%），体现10倍数据效率提升。
- 推理速度：SDP比最慢的ET-SEED快约67倍，且无需预处理（分割物体），适合实时控制。

## 7. 优点
- **方法层面**：
  - 首次将连续SO(3)等变与紧凑的球面傅里叶特征结合用于闭环扩散策略，避免了离散化误差和繁重的SO(3)不可约表示计算。
  - 提出的球面FiLM层实现等变条件调制，支持高阶球面谐波（degree>1），表达能力优于Vector Neuron。
  - SDTU实现时空等变U-Net，兼顾效率与等变性。
  - 端到端SE(3)等变，无需任务特定物体分割，适用于多物体场景。
- **实验层面**：
  - 覆盖大量仿真任务和真实物理任务，包括单臂和双臂，验证了泛化能力。
  - 消融实验系统全面，揭示了各组件贡献和相对重要性。
  - 样本效率分析清楚说明等变性带来的数据节省优势。

## 8. 不足与局限
- **实验覆盖**：
  - 物理实验仅使用一个种子，未报告多随机种子统计结果，可靠性有待重复验证。
  - 仿真中SE(3)任务仅4个，且最大倾斜角度30°，更大角度（如60°）未测试。
  - 未在更复杂场景（如多物体堆叠、动态障碍）中评估。
- **方法局限**：
  - 仅考虑位置控制，忽略接触力，导致在需要力交互的任务（如翻书）中发生保护性停机。
  - 点云分辨率低（1024点）时难以捕获精细细节（如推橡皮任务中需要2048点才能提升性能）。
  - 视角依赖：仅靠前方和手内相机可能导致遮挡问题（样本效率实验提到）。
  - 训练数据来自MimicGen（基于少数人类演示生成），增加演示数量可能不增加多样性，导致性能饱和。
- **其他**：
  - 未提供训练计算资源的具体细节（GPU型号/数量/时长），难以复现与比较效率。
  - 未与最新方法如ET-SEED进行直接对比（代码缺失）。
  - 潜在危险：方法缺乏对常见场景的意识，可能产生危险动作（论文影响声明中提及）。

（完）
