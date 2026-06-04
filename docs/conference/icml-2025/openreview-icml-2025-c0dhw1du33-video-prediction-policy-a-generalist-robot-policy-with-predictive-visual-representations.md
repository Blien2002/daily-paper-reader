---
title: "Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations"
title_zh: 视频预测策略：具有预测视觉表征的通用机器人策略
authors: "Yucheng Hu, Yanjiang Guo, Pengchao Wang, Xiaoyu Chen, Yen-Jen Wang, Jianke Zhang, Koushil Sreenath, Chaochao Lu, Jianyu Chen"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=c0dhw1du33"
tags: ["query:vla"]
score: 9.0
evidence: 使用视频预测的通用机器人操作策略
tldr: 该论文针对通用机器人策略中视觉表征忽视动态信息的问题，提出视频预测策略（VPP），利用视频扩散模型产生同时包含静态与未来动态信息的表征来指导动作学习。实验表明VPP在多种具身任务上表现出色，证明了预测性视觉表征对于机器人学习的价值。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 822, \"height\": 519, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1705, \"height\": 651, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 707, \"height\": 398, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1774, \"height\": 423, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1695, \"height\": 758, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1761, \"height\": 292, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 856, \"height\": 504, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1679, \"height\": 1329, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1658, \"height\": 737, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-c0dhw1du33/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1757, \"height\": 2253, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1765, \"height\": 693, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1026, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 852, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 856, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 854, \"height\": 380, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 820, \"height\": 754, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 836, \"height\": 1420, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1214, \"height\": 596, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 876, \"height\": 132, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1001, \"height\": 127, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 956, \"height\": 130, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1155, \"height\": 304, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-c0dhw1du33/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1602, \"height\": 897, \"label\": \"Table\"}]"
motivation: 传统视觉编码器捕捉静态信息为主，忽略了机器人任务所需的动态预测能力。
method: 利用视频扩散模型提取同时包含当前静态和未来动态的视觉表征，直接指导机器人动作策略学习。
result: 在多个机器人操作任务上，VPP显著优于基于静态或对比学习的视觉编码器方法。
conclusion: 预测性视觉表征是构建通用机器人策略的有效途径。
---

## Abstract
Visual representations play a crucial role in developing generalist robotic policies. Previous vision encoders, typically pre-trained with single-image reconstruction or two-image contrastive learning, tend to capture static information, often neglecting the dynamic aspects vital for embodied tasks. 
Recently, video diffusion models (VDMs) demonstrate the ability to predict future frames and showcase a strong understanding of physical world. 
We hypothesize that VDMs inherently produce visual representations that encompass both current static information and predicted future dynamics, thereby providing valuable guidance for robot action learning. 
Based on this hypothesis, we propose the Video Prediction Policy (VPP), which learns implicit inverse dynamics model conditioned on predicted future representations inside VDMs. 
To predict more precise future, we fine-tune pre-trained video foundation model on robot datasets along with internet human manipulation data.
In experiments, VPP achieves a 18.6\% relative improvement on the Calvin ABC-D generalization benchmark compared to the previous state-of-the-art, and demonstrates a 31.6\% increase in success rates for complex real-world dexterous manipulation tasks. For your convenience, videos can be found at https://video-prediction-policy.github.io/

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：现有机器人通用策略中的视觉编码器（如基于单图像重建的MAE、基于图像对比学习的CLIP等）主要捕捉静态信息，忽略了机器人任务所需的动态信息（如物体移动、机械臂轨迹）。这些编码器仅观察当前帧或两帧，无法显式预测未来状态。
- **背景**：视频扩散模型（VDMs）在视频生成中展现了强大的物理世界理解能力，能够预测未来帧。论文假设VDMs内部的隐层表征天然蕴含了当前静态信息和预测的未来动态信息，可用于指导机器人动作学习，从而构建更具泛化能力的策略。
- **整体含义**：提出一种利用视频扩散模型内部“预测性视觉表征”来学习逆动力学模型的方法，将视频预测能力迁移到机器人策略中，提升操作任务的泛化性能和成功率。

## 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：将视频扩散模型作为视觉编码器，提取其内部表征（仅需一次前向传播，避免了完整去噪的低效），该表征同时包含当前观测和预测的未来帧信息。机器人策略通过跟踪预测表征中的机械臂运动，隐式学习逆动力学模型，从而生成动作。

- **关键技术细节**：
  1. **第一阶段：文本引导视频预测（TVP）模型微调**  
     - 基础模型：Stable Video Diffusion (SVD) 1.5B参数。
     - 改进：加入CLIP语言嵌入（通过交叉注意力层）；输出分辨率调整为16×256×256；保留原有U-Net结构。
     - 训练数据：互联网人类操作数据集（Something-something-v2，191,642条轨迹）、互联网机器人数据集（RT-1、Bridge、BC-Z等，共约158,000条轨迹）、下游任务数据集（Calvin、Metaworld、自采数据）。
     - 损失函数：视频扩散损失，加权平衡不同数据集（公式4）。
     - 训练完成后冻结TVP模型参数，用于第二阶段。
  2. **第二阶段：基于预测视觉表征的动作学习**  
     - **预测视觉表征提取**：将当前图像s0与最终噪声潜变量拼接输入TVP模型，仅执行一次前向去噪步骤（而非完整30步），从多个上采样层提取中间特征。通过线性插值和通道拼接得到多尺度表征Fp（形状T×ΣCm×Wp×Hp）。
     - **Video Former聚合**：初始化可学习查询令牌，通过时空注意力（先空间注意再时间注意）和多视角融合，聚合表征为固定长度的令牌Q''。
     - **动作生成**：使用扩散策略头（DiT架构），以Q''为条件对动作序列进行去噪（10次采样步），输出动作序列a0（长度chunk=10）。  
     - **整体流程**：观测s0 → TVP单次前向 → 提取表征 → Video Former → 扩散策略 → 动作序列。
  3. **推理速度**：TVP作为编码器仅需一次前向（<160ms），配合动作chunking实现7-10Hz闭环控制（RTX 4090）。

- **公式/算法（文字说明）**：
  - 视频训练损失：L_video = λ_H L_DH + λ_R L_DR + λ_C L_DC（公式4）
  - 动作扩散损失：L_diff(ψ; A) = E[∥D_ψ(a_k, l_emb, Q'') - a_0∥²]（公式6）
  - 特征聚合：对每层特征插值到相同尺寸，然后通道拼接。
  - Video Former：对每帧进行空间注意力，再跨帧进行时间注意力，然后FFN。

## 3. 实验设计

- **数据集/场景**：
  - **模拟**：CALVIN（ABC→D零样本泛化，训练在环境A/B/C，测试在未见过环境D）；Metaworld（50个任务，基于官方Oracle策略采集每任务50条轨迹）。
  - **真实世界**：Franka Panda机械臂（30+任务，2000轨迹，类别：抓取、放置、按压、移动、开抽屉等）；Xarm+12自由度灵巧手（100+任务，4000轨迹，类别：抓取、堆叠、倒水、使用工具等）。包含已见和未见任务（新物体/新背景），以及挑战性的工具使用任务（勺子、锤子、电钻、移液器）。

- **Benchmark**：CALVIN ABC→D的平均任务完成长度；Metaworld 50个任务的成功率；真实世界分类别成功率。

- **对比方法**：
  - 直接动作学习：RT-1、Diffusion Policy、Robo-Flamingo
  - 未来预测相关：Uni-Pi、MDT、Susie、GR-1、Vidman
  - 3D方法：RoboUniview
  - 所有基线基于官方实现或原论文结果，Diffusion Policy使用CLIP条件。

## 4. 资源与算力

- **第一阶段（TVP微调）**：8张NVIDIA A100 GPU，训练2-3天。
- **第二阶段（策略训练）**：4张NVIDIA A100 GPU，训练6-12小时（不同环境）。
- **推理**：消费级NVIDIA RTX 4090，单次推理<160ms，控制频率7-10Hz。
- 论文明确说明了GPU型号、数量和训练时长。

## 5. 实验数量与充分性

- **实验数量**：
  - 模拟环境：CALVIN（全量数据 + 10%数据效率）；Metaworld（50任务）；多组消融实验。
  - 真实环境：Franka Panda（200+次评估）；灵巧手（500+次评估）；包括已见/未见/工具使用任务。
  - 消融实验：替换视觉编码器（Stable-VAE, VC-1, Voltron）；移除互联网数据、视频预训练、Video Former、特征聚合；不同层特征、不同去噪步数；单视角 vs 多视角；时间注意力模块等。
- **充分性与公平性**：
  - 对比了多个强基线，包括最新的Vidman、RoboUniview等。
  - 严格控制变量（如替换编码器时保持策略头部一致）。
  - 结果统计明确（成功率、完成长度），且报告了延迟。
  - 消融实验覆盖了主要组件，验证了各模块贡献。
- **客观性**：结果均基于多次评估，部分来自原论文或官方实现复现。

## 6. 论文的主要结论与发现

- VPP在CALVIN ABC→D上平均完成长度达4.33（之前SOTA为3.65），提升18.6%；在Metaworld 50任务上平均成功率68.2%（GR-1为57.4%）。
- 仅用10%数据时，VPP仍取得3.25完成长度，优于多数使用全数据的方法。
- 真实世界：Franka Panda已见任务成功率85.6%、未见73.7%；灵巧手已见74.9%、未见60.5%、工具使用68%，显著优于基线（GR-1、Susie、Diffusion Policy）。
- 预测视觉表征（VDM内部特征）优于传统重建/对比学习表征。
- 视频预训练、互联网人类数据、Video Former、特征聚合均对性能有贡献。
- 单步前向表征已能提供有效的未来运动轨迹信息（可视化验证）。

## 7. 优点

- **方法创新性**：首次利用视频扩散模型内部隐层表征作为“预测性视觉表征”，避免了完整去噪的时间开销，同时继承了视频模型的物理理解能力。
- **效率高**：闭环控制频率达7-10Hz，适合实时机器人控制；相比Susie、Uni-Pi等需要完整去噪的方法更具实用性。
- **泛化能力强**：通过互联网预训练和微调，能够泛化到未见物体、背景和简单工具任务。
- **实验全面**：覆盖模拟和真实、多任务、多基线、多消融，验证充分。
- **模块化设计**：TVP冻结后作为编码器，可复用；Video Former可灵活聚合多视角；扩散策略头可处理多模态动作分布。

## 8. 不足与局限

- **计算资源要求高**：第一阶段的TVP微调需要8张A100训练数天，对普通实验室不友好。
- **依赖预训练模型**：使用Stable Video Diffusion，其性能受限于基础模型；若未来有更强模型需重新微调。
- **长时程任务**：论文未讨论非常长的任务链（如超过5步）或误差累积问题；CALVIN仅5步长时评估。
- **真实世界任务数量有限**：虽然超过100+，但相比开放世界的无穷性仍有限；未见任务仅改变了物体/背景，未涉及光照、视角剧烈变化等。
- **未对比强化学习方法**：仅与模仿学习基线对比，未与基于RL的方法（如DRL）比较，可能限制结论范围。
- **动作空间**：灵巧手使用低层PD控制器平滑动作，策略是否直接适用于软体或欠驱动机器人未验证。
- **消融实验**：未对Video Former的令牌数量、注意力头数等超参数进行系统调优探索。

（完）
