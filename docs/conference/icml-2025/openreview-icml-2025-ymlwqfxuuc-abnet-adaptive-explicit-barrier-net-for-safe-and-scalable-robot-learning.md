---
title: "ABNet: Adaptive explicit-Barrier Net for Safe and Scalable Robot Learning"
title_zh: ABNet：面向安全与可扩展机器人学习的自适应显式屏障网络
authors: "Wei Xiao, Tsun-Hsuan Wang, Chuang Gan, Daniela Rus"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=ymlwqfxuUc"
tags: ["query:vla"]
score: 4.0
evidence: 使用显式屏障函数的安全机器人学习，可扩展到基础模型
tldr: 针对机器人安全学习的可扩展性和稳定性问题，本文提出自适应显式屏障网络（ABNet），将屏障函数以闭式显式纳入模型，保证安全。通过多头部学习不同特征的控制策略，ABNet能逐步扩展到更大的安全基础模型。该工作为具身智能中的安全部署提供了理论保障。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1248, \"height\": 426, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 877, \"height\": 411, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 629, \"height\": 976, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 625, \"height\": 955, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 614, \"height\": 892, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 608, \"height\": 988, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1645, \"height\": 582, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 822, \"height\": 269, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 757, \"height\": 575, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 619, \"height\": 264, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1674, \"height\": 593, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1677, \"height\": 818, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ymlwqfxuuc/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1660, \"height\": 597, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-ymlwqfxuuc/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 863, \"height\": 799, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ymlwqfxuuc/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1762, \"height\": 597, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ymlwqfxuuc/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1761, \"height\": 589, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ymlwqfxuuc/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1764, \"height\": 571, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ymlwqfxuuc/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1754, \"height\": 564, \"label\": \"Table\"}]"
motivation: 现有安全学习方法难以扩展、训练困难且易受噪声干扰，亟需可部署的安全方案。
method: 提出ABNet，将屏障函数以闭式显式形式嵌入模型，并通过多头部分别学习不同观测特征的安全控制策略。
result: ABNet在保证安全的同时具备良好的可扩展性，能逐步构建更大规模的安全基础模型。
conclusion: 显式屏障网络为机器人安全学习提供了高效、可扩展的解决方案。
---

## Abstract
Safe learning is central to AI-enabled robots where a single failure may lead to catastrophic results. Existing safe learning methods are not scalable, inefficient and hard to train, and tend to generate unstable signals under noisy inputs that are challenging to be deployed for robots. To address these challenges, we propose Adaptive explicit-Barrier Net (ABNet) in which barriers explicitly show up in the closed-form model that guarantees safety. The ABNet has the potential to incrementally scale toward larger safe foundation models.  Each head of ABNet could learn safe control policies from different features and focuses on specific part of the observation. In this way, we do not need to directly construct a large model for complex tasks, which significantly facilitates the training of the model while ensuring its stable output. Most importantly, we can still formally prove the safety guarantees of the ABNet. We demonstrate the efficiency and strength of ABNet in 2D robot obstacle avoidance, safe robot manipulation, and vision-based end-to-end autonomous driving, with results showing much better robustness and guarantees over existing models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：机器人学习需要可扩展的训练和海量数据，但现有大规模模型（如用于操作、运动、自动驾驶的模型）不具备可信性和安全保证。已有的将保证或证书纳入神经网络的方法（如BarrierNet、dQP）不可扩展、训练困难，且在噪声输入下产生不稳定信号，难以部署到真实机器人上。
- **整体含义**：本文提出一种既能保证安全性、又能高效训练、可逐步扩展到更大安全基础模型的新架构，旨在解决安全机器人学习中可扩展性、效率和稳定性三大挑战。

## 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：提出**自适应显式屏障网络（ABNet）**，将屏障函数以闭式（closed-form）显式形式嵌入模型，保证安全性；通过多头（multi-head）结构，每个头关注观测的不同特征或不同部分，学习安全控制策略；最终通过加权融合各头输出，实现可扩展和鲁棒的控制。
- **关键技术细节**：
  - **显式屏障（Explicit-Barrier）**：基于控制屏障函数（CBF）和高阶CBF（HOCBF），将原始安全约束转化为二次规划问题。通过将多个安全约束合并为两个（如使用最小函数或对数指数平滑），推导出闭式解析解：  
    \( u_k = -\lambda_1(x)H^{-1}L_g\psi_{I,m-1} - \lambda_2(x)H^{-1}L_g\psi_{II,m-1} - H^{-1}F \)，  
    其中 \(\lambda_1, \lambda_2\) 为门控函数（gate functions），显式体现屏障作用，使模型更具可解释性和训练效率。
  - **多头自适应机制**：每个头 \(k\) 可基于不同观测特征 \(z_k\) 或相同观测学习安全策略；头间通过共享参数 \(\theta_p\) 实现交叉连接（cross connection），确保安全证明的一致性。
  - **融合方式**：各头输出加权求和：\( u = \sum_{k=1}^h w_k u_k \)，其中 \(w_k \ge 0, \sum w_k = 1\)，可训练或根据测试损失确定。
  - **安全性证明**：定理3.1证明，若系统初始安全，则ABNet输出保证状态始终在安全集内；定理3.2证明多个ABNet再次融合仍保持安全性。
- **算法流程**（Algorithm 1）：
  1. 公式化每个显式屏障头。
  2. 通过共享参数构建交叉连接。
  3. 按(5)式融合所有头。
  4. 可选择增量训练（分别训练各头，再融合）或一次性直接训练（反向传播）。

## 3. 实验设计

- **数据集/场景**：
  - **2D机器人避障**：仿真环境，自行车模型，障碍物为圆形区域。
  - **安全机器人操作**：两连杆平面机械臂抓取任务，避免与障碍物碰撞。
  - **视觉端到端自动驾驶**：使用开源VISTA模拟器（基于真实驾驶数据），包含约40万图像-控制对，障碍物为静态和停放的车辆。
- **Benchmark & 对比方法**：
  - 基线方法：端到端模型（E2E, V-E2E）。
  - 安全保证模型：BarrierNet (BNet)、Deep Forward-Backward (DFB)。
  - 策略/模型融合方法：BarrierNet-UP（不确定性传播）、E2Es-MCD（Monte-Carlo Dropout）、E2Es-DR（Deep Resembles）。
  - 本方法：ABNet-10-SC（可扩展训练10头）、ABNet-10（一次性训练10头）、ABNet-100（一次性训练100头）；视觉任务中还测试了ABNet-att（注意力图像10头）和ABNet-SC（可扩展融合两个ABNet，共20头）。
- **评估指标**：安全性（SAFETY，最小值≥0表示安全）、保守性（CONSER.）、均方误差（MSE）、控制不确定性（u1/u2 UNCERTAINTY）、理论安全保证（THEORET. GUAR.）、碰撞率（CRASH）、通过率（PASS）。

## 4. 资源与算力

- 论文在附录C中明确指出：
  - 2D机器人避障：RTX-3090 GPU，训练约1小时（20 epochs）。
  - 安全机器人操作：RTX-3090 GPU，训练约2小时（10 epochs）。
  - 视觉自动驾驶：RTX-3090 GPU，训练约15小时（5 epochs）。
- 未提及GPU数量，推测为单卡。所有实验均在RTX-3090上完成。

## 5. 实验数量与充分性

- **实验数量**：共三大类任务（2D避障、操作、驾驶）。每类任务中测试了多种不同模型（6~9种对比方法），且每种方法在100次独立运行（N=100）上报告结果，包含均值和标准差。
- **消融实验**：
  - 头数影响：对比了10头、100头（ABNet-10, ABNet-100）及可扩展训练（ABNet-10-SC）。
  - 注意力机制：ABNet vs ABNet-att（视觉任务）。
  - 噪声鲁棒性：附加了50%噪声的消融实验（表4）。
  - 可扩展性：可视化训练过程中头数增加对性能的影响（图4,5,6）。
- **充分性评价**：实验覆盖了简单动力学（2D）、多连杆操作（6维状态）和真实视觉任务，对比方法全面（包括无安全保证、有安全保证、模型融合类），评价指标多样，消融实验合理。但在真实机器人上未部署，仅在模拟器中闭环测试，是合理的局限性。

## 6. 主要结论与发现

- ABNet在**计算效率**上远优于基于dQP的BarrierNet，训练时间与普通神经网络相当，而dQP极易给出糟糕解（见图7）。
- ABNet在**安全性**上严格满足约束（所有测试中安全指标≥0），而E2E、MCD、DR等无安全保证方法均出现负值（碰撞）。
- ABNet的**控制不确定性**显著低于BarrierNet和DFB，且随头数增加进一步降低（如ABNet-100优于ABNet-10）。
- 在**视觉驾驶任务**中，ABNet达到0%碰撞率、100%障碍物通过率，而BarrierNet和DFB通过率仅33%~39%，因它们倾向于减速而非转向避障。
- **可扩展性**：增量训练可有效提升性能，且融合后的ABNet仍保持安全保证（定理3.2）。

## 7. 优点（方法或实验设计亮点）

- **创新性**：首次提出显式闭式屏障函数，避免了dQP求解的效率和稳定性问题，并实现了可解释性。
- **结构优雅**：多头加权融合机制，既保证了安全（定理3.1），又提供了自然噪声滤波（权重在[0,1]之间），输出平滑。
- **可扩展性**：支持增量训练，可逐步添加新技能（新头）而不破坏已有安全保证，为构建安全基础模型奠定基础。
- **理论完备**：提供严格安全证明，且证明过程清晰。
- **实验设计严谨**：多种对比方法、多个指标、多次运行、含噪声鲁棒测试，结果统计完整。

## 8. 不足与局限

- **安全约束统一**：所有ABNet头必须使用相同的安全约束集合，无法融合具有不同安全规范的模型（作者作为未来工作提出）。
- **依赖已知安全规范**：需要人工定义安全约束（如障碍物位置和大小），若约束未知或难以建模，则需另学安全规范（如Robey et al.）。文中未实验自动学习约束的情况。
- **融合仅在输出空间**：目前仅在输出控制级加权求和，未在参数空间融合（作者也将其列为未来工作）。
- **未涉及接触处理**：实验未包含需要与环境接触的任务（如抓取），作者说明未来会探索。
- **潜在偏差风险**：训练数据来自HOCBF-QP或NMPC生成的标签，若标签本身有偏差（如保守性过强），则模型学习会继承该偏差。
- **模拟环境局限性**：所有实验均在模拟器（2D、操作、VISTA）中闭环测试，未在真实机器人上验证，尽管VISTA是基于真实数据的模拟器，但仍存在sim-to-real gap。
- **计算资源**：仅报告单卡RTX-3090训练时间，未讨论多卡并行或更大模型（如100头以上）的扩展时间，但文中已展示100头训练仍快于BarrierNet。

（完）
