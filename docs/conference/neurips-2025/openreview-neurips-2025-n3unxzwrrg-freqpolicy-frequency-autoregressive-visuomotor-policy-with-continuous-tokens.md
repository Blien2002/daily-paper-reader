---
title: "FreqPolicy: Frequency Autoregressive Visuomotor Policy with Continuous Tokens"
title_zh: FreqPolicy：基于连续token的频域自回归视觉运动策略
authors: "Yiming Zhong, Yumeng Liu, Chuyang Xiao, Zemin Yang, Youzhuo Wang, Yufei Zhu, Ye Shi, Yujing Sun, Xinge Zhu, Yuexin Ma"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=N3UNXzWRRG"
tags: ["query:vla"]
score: 8.0
evidence: 频域自回归视觉运动策略用于机器人操作
tldr: FreqPolicy针对机器人操作中动作表示和网络架构的局限，提出将动作分解为频率域的低频全局模式和高频局部细节，并采用连续token自回归生成策略。该方法能根据任务复杂度自适应分配建模精度，在多个模拟和真实操作任务中实现了更高成功率与更低推理延迟。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 455, \"height\": 395, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1445, \"height\": 858, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1459, \"height\": 666, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 454, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1386, \"height\": 260, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1450, \"height\": 501, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1450, \"height\": 486, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1452, \"height\": 524, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1450, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1453, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1447, \"height\": 484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1446, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1446, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1449, \"height\": 524, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1447, \"height\": 484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1446, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1446, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1448, \"height\": 524, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1448, \"height\": 484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1447, \"height\": 526, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1446, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1448, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 1445, \"height\": 484, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 1446, \"height\": 523, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-025.webp\", \"caption\": \"\", \"page\": 0, \"index\": 25, \"width\": 1446, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-026.webp\", \"caption\": \"\", \"page\": 0, \"index\": 26, \"width\": 1448, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-027.webp\", \"caption\": \"\", \"page\": 0, \"index\": 27, \"width\": 1447, \"height\": 485, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-028.webp\", \"caption\": \"\", \"page\": 0, \"index\": 28, \"width\": 1447, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-029.webp\", \"caption\": \"\", \"page\": 0, \"index\": 29, \"width\": 1447, \"height\": 525, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-n3unxzwrrg/fig-030.webp\", \"caption\": \"\", \"page\": 0, \"index\": 30, \"width\": 1449, \"height\": 524, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1455, \"height\": 310, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1454, \"height\": 309, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1452, \"height\": 157, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1453, \"height\": 247, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1444, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1453, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1029, \"height\": 962, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1454, \"height\": 772, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1446, \"height\": 410, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1443, \"height\": 181, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1455, \"height\": 1042, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-n3unxzwrrg/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1338, \"height\": 142, \"label\": \"Table\"}]"
motivation: 现有视觉运动策略在动作表示和网络架构上存在效率与精度的权衡问题。
method: 将动作表示为频域分量，并用连续token的自回归模型按频带生成。
result: 在多个操作任务上优于基线方法，兼具高精度和低延迟。
conclusion: 频域分解有效捕捉动作结构，为视觉运动策略提供新范式。
---

## Abstract
Learning effective visuomotor policies for robotic manipulation is challenging, as it requires generating precise actions while maintaining computational efficiency. Existing methods remain unsatisfactory due to inherent limitations in the essential action representation and the basic network architectures. We observe that representing actions in the frequency domain captures the structured nature of motion more effectively: low-frequency components reflect global movement patterns, while high-frequency components encode fine local details. Additionally, robotic manipulation tasks of varying complexity demand different levels of modeling precision across these frequency bands. Motivated by this, we propose a novel paradigm for visuomotor policy learning that progressively models hierarchical frequency components. To further enhance precision, we introduce continuous latent representations that maintain smoothness and continuity in the action space. Extensive experiments across diverse 2D and 3D robotic manipulation benchmarks demonstrate that our approach outperforms existing methods in both accuracy and efficiency, showcasing the potential of a frequency-domain autoregressive framework with continuous tokens for generalized robotic manipulation.Code is available at https://github.com/4DVLab/Freqpolicy

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

现有视觉运动策略（visuomotor policy）主要分为扩散模型和自回归（AR）方法。扩散模型精度高但推理慢；AR方法速度快但易累积误差，且常用离散化表示导致连续动作空间信息损失。两类方法均未充分利用动作信号的**结构特性**——在频域中，低频分量对应全局运动模式，高频分量对应精细局部细节。不同复杂度的操作任务对频段精度的需求不同（简单任务可用低频，复杂任务需要高频）。因此，论文提出从频域角度重新表示动作，并设计一种**层级频域自回归生成范式**，以实现高效、高精度的策略学习。

### 2. 方法论：核心思想、关键技术细节

- **核心思想**：将动作序列变换到频域，采用**由粗到细（coarse-to-fine）的多阶段渐进生成**，先建模低频全局结构，再逐步补全高频细节。同时使用**连续潜在表示（continuous latent tokens）** 代替离散token，避免量化损失。
- **关键技术细节**：
  - **离散余弦变换（DCT）**：对动作序列每一维度独立做DCT，得到频域系数。保留前k个系数（k-level）可重建出平滑版本的动作。
  - **FreqPolicy架构**：包含一个观察编码器、一个FreqPolicy编码器‑解码器。编码器将当前频段重建动作`y^k`、观察特征和频段索引映射为连续token`z^k`，解码器再将其作为条件输入给一个扩散模型，用于重建原始全频动作。
  - **训练**：随机采样一个频段k，用逆DCT得到k-level重建，将其与观测、索引一同编码，扩散模型学习从噪声还原完整动作。损失函数为扩散损失（公式4）。采用**频域感知掩码策略**：低频段使用更高掩码率，节省计算。
  - **推理**：从零开始，迭代Niter次。第i次以上一次输出的li-1-level重建为输入，生成全频动作，再截取li-level用于下一步。最终输出全频动作。
- **算法流程**（文字描述）：
  1. 对真实动作序列做DCT，获得频域系数。
  2. 随机选择频段k，保留前k个系数，逆DCT得到k-level重建。
  3. 将观测、k-level重建、频段索引输入FreqPolicy编码器，得到条件潜在表示z。
  4. 扩散模型以z为条件，从噪声中还原原始全频动作。
  5. 推理时重复该过程：初始为0，逐步增加保留的频段数，直至全频。

### 3. 实验设计：数据集、基准与对比方法

- **数据集与基准**：
  - **2D任务**（仅图像观测）：Robomimic（Lift、Can、Square、Transport）、Push T。
  - **3D任务**（点云+RGB/状态）：Adroit（ShadowHand，26-28DoF）、DexArt（Allegro Hand，22DoF）、MetaWorld（平行夹爪，10DoF，含Easy/Medium/Hard/Very Hard共45个任务）、RoboTwin（双臂夹爪，14DoF）。
  - 真实世界实验：ShadowHand手递物任务（RGB-D相机，30Hz）。
- **对比方法**：
  - 扩散类：Diffusion Policy（DP-C/DP-T）、3D Diffusion Policy（DP3）、Mamba Policy。
  - 自回归离散类：BeT、CARP。
  - 论文内消融基线：无DCT分解的版本（ours(w/o DCT)）。
- **评价指标**：任务成功率（%），推理时间，以及Pareto分析。

### 4. 资源与算力

- 仿真实验：使用 **NVIDIA RTX 2080Ti GPU**，模型参数量63M（DP3为255M），占用约4.5GB内存。
- 真实世界实验：使用 **NVIDIA RTX 4090 GPU**，单次推理可达70 FPS（DP3为25 FPS）。
- 训练轮数：Adroit、DexArt、MetaWorld为3000 epochs；Robomimic、Push-T为1000 epochs；RoboTwin为500 epochs。
- 论文未明确说明训练总时长或使用的GPU数量，但给出了明确的硬件配置和训练配置。

### 5. 实验数量与充分性

- **实验总量**：涵盖2D/3D仿真共约 **48个任务**（MetaWorld 45 + Adroit 3 + DexArt 4），RoboTwin 7个任务，以及10个详细对比任务表。
- **消融实验**：包括预测horizon（Th）对比（表8）、有无频域掩码的对比（表9）。
- **噪声鲁棒性**：低质量演示和不同强度高斯噪声下的性能测试（表5）。
- **泛化性**：DexArt unseen环境、少样本（10/100演示）实验（表4）。
- **效率与精度权衡**：Pareto分析不同迭代次数的影响（图4）。
- **公平性**：对于基线方法，采用相同演示数据复现（标注*），并保持参数和观测处理一致。实验随机种子3次取平均和标准差。
- **评价**：实验覆盖全面，对比公平，统计充分，结果可信。

### 6. 论文的主要结论与发现

- 频域表示能有效捕捉动作的结构化特征：低频提供全局趋势，高频提供细节。
- FreqPolicy在多数任务上取得**最高成功率**（平均67.9%），优于DP3（64.6%）和Mamba Policy（65.8%）。
- 连续token相比于离散token（BeT、CARP）显著提升性能，尤其在需要精细控制的任务中。
- 推理速度**快约10倍**（0.21s vs 2.11s），且可通过调整迭代次数灵活平衡速度与精度。
- 在高噪声环境下（std=0.1）具有**强鲁棒性**（33%成功率，基线为19-23%），在Hammer任务中基线完全失效时仍保持15-70%。
- 真实世界实验达到70 FPS，满足实时控制需求。

### 7. 优点：方法或实验设计上的亮点

- **创新性**：首次将频域分解与连续token自回归结合，提出“由粗到细”的频域生成范式。
- **效率与精度双赢**：AR框架的低延迟 + 扩散模型的连续精确建模。
- **噪声鲁棒性**：低频优先的渐进生成天然具有抗噪特性。
- **灵活性**：推理时可自由选择迭代次数，实现速度-精度折中。
- **实验全面**：覆盖2D/3D、仿真/真实、多种自由度、不同噪声场景，并与多个基线公平对比。
- **开源计划**：提供项目页面和代码（GitHub），便于复现。

### 8. 不足与局限

- **条件输入未探索**：实验条件输入与DP/DP3保持一致，未测试改变观测编码方式的影响（论文自述）。
- **2D任务仍有差距**：在Robomimic等图像观测任务中，性能虽好但未完全超越扩散模型（如Transport任务成功率较低）。
- **频域划分过细导致下降**：过细的分频会损害性能（论文自述）。
- **代码尚未公开**：目前仅有项目页面，代码还未发布（但声称将在接收后公开）。
- **VLA任务未深入**：论文在附录初步测试了RoboCasa多任务，但未达到专用VLA模型（GR00T-N1）的水平，需进一步融合语言理解。
- **计算资源要求**：虽推理高效，但训练仍需较大GPU内存（4.5GB），对资源受限场景可能不友好。

（完）
