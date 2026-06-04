---
title: "STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization"
title_zh: STAR：通过旋转增强向量量化学习多样化机器人技能抽象
authors: "Hao Li, Qi Lv, Rui Shao, Xiang Deng, Yinchuan Li, Jianye HAO, Liqiang Nie"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=n1cqQK4hhC"
tags: ["query:vla"]
score: 7.0
evidence: 通过旋转增强向量量化学习机器人操作技能抽象
tldr: 针对VQ-VAE学习技能抽象时的码本崩溃和技能因果建模问题，本文提出STAR框架，通过旋转增强残差技能量化（RaRSQ）防止码本崩溃，并改进技能学习与组合。该方法为复杂机器人操作提供了更稳健的技能表征，有助于构建可复用的机器人基础模型。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 858, \"height\": 607, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1434, \"height\": 855, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 853, \"height\": 603, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 853, \"height\": 585, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1579, \"height\": 957, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1768, \"height\": 266, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1765, \"height\": 1170, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1600, \"height\": 1338, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-n1cqqk4hhc/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1741, \"height\": 2155, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-n1cqqk4hhc/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1605, \"height\": 415, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n1cqqk4hhc/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1604, \"height\": 230, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n1cqqk4hhc/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 644, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n1cqqk4hhc/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 645, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-n1cqqk4hhc/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1770, \"height\": 182, \"label\": \"Table\"}]"
motivation: 现有技能抽象方法存在码本崩溃和技能间因果关系建模不足的问题。
method: 提出旋转增强残差技能量化（RaRSQ），通过编码器输出间的相对角度指导梯度更新，防止码本崩溃。
result: 有效学习到多样且可组合的技能抽象，提升复杂行为的完成能力。
conclusion: 旋转增强量化是改善技能学习稳定性和组合性的有效手段。
---

## Abstract
Transforming complex actions into discrete skill abstractions has demonstrated strong potential for robotic manipulation.Existing approaches mainly leverage latent variable models, e.g., VQ-VAE, to learn skill abstractions through learned vectors (codebooks), while they suffer from codebook collapse and modeling the causal relationship between learned skills. To address these limitations, we present **S**kill **T**raining with **A**ugmented **R**otation (**STAR**), a framework that advances both skill learning and composition to complete complex behaviors. Specifically, to prevent codebook collapse, we devise rotation-augmented residual skill quantization (RaRSQ).It encodes relative angles between encoder outputs into the gradient flow by rotation-based gradient mechanism. Points within the same skill code are forced to be either pushed apart or pulled closer together depending on gradient directions.Further, to capture the casual relationship between skills, we present causal skill transformer (CST) which explicitly models dependencies between skill representations through an autoregressive mechanism for coherent action generation.Extensive experiments demonstrate the superiority of STAR on both LIBERO benchmark and realworld tasks, with around 12% improvement over the baselines.

---

## 论文详细总结（自动生成）

# 论文总结：STAR: Learning Diverse Robot Skill Abstractions through Rotation-Augmented Vector Quantization

## 1. 核心问题与整体含义（研究动机和背景）

现有方法（如 VQ-VAE）将连续机器人动作转化为离散的技能抽象，用于多任务操作。然而，它们面临两个关键局限：

- **码本崩溃（codebook collapse）**：训练中大部分码本向量未被使用，只有少数向量被反复选用，导致技能表示多样性严重不足。作者指出，这源于直通估计器（STE）将相同的梯度分配给所有映射到同一码本向量的编码器输出，忽略了它们之间的几何关系。
- **技能间因果关系建模不足**：现有方法在组合多个技能完成长时任务时，未能显式建模技能之间的依赖关系，导致生成的动作序列不连贯。

为解决上述问题，本文提出 **STAR** 框架，通过旋转增强残差技能量化（RaRSQ）和因果技能 Transformer（CST）分别提升技能学习的多样性和技能组合的连贯性，从而在复杂机器人操作中取得显著性能提升。

## 2. 方法论：核心思想、关键技术细节

STAR 采用两阶段训练策略：第一阶段训练 RaRSQ 学习技能抽象，第二阶段固定 RaRSQ 训练 CST 用于技能组合。

### 2.1 旋转增强残差技能量化（RaRSQ）

- **核心思想**：在残差量化过程中，利用旋转变换将编码器输出与码本向量对齐，并通过梯度传播引入几何关系，使同一码本内的不同编码器输出获得不同的梯度更新，从而防止码本崩溃。
- **关键技术细节**：
  - 给定动作序列 \(a_{t:t+T}\)，编码器得到潜在向量 \(z\)。
  - 迭代进行深度 \(d=1,...,D\) 的量化：
    - 最近邻查找：\(k_d = \arg\min_k \|r_{d-1} - e_{(d,k)}\|_2^2\)
    - 计算旋转矩阵 \(R_d\) 对齐残差 \(r_{d-1}\) 与所选码本向量 \(e_{(d,k_d)}\)。
    - 应用旋转与缩放：\(\tilde{q}_d = \text{sg}\!\left[\frac{\|e_{(d,k_d)}\|}{\|r_{d-1}\|} R_d\right] r_{d-1}\)（sg 为停止梯度）
    - 更新残差：\(r_d = r_{d-1} - \tilde{q}_d\)
  - 最终量化表示：\(\hat{z} = \sum_{d=1}^D \tilde{q}_d\)，解码器重建动作。
  - 训练损失：重建损失 + 承诺损失（包含旋转后的残差与码本向量的距离）。

- **算法流程（文字说明）**：输入动作序列 → 编码得到潜在向量 → 逐层进行残差量化（每次先找最近邻码本，计算旋转矩阵并旋转缩放残差，更新残差）→ 求和所有层的旋转后量化向量 → 解码重建动作。反向传播时梯度通过旋转矩阵流动，使同一码本内不同点获得不同更新。

### 2.2 因果技能 Transformer（CST）

- **核心思想**：通过自回归方式显式建模技能之间的依赖关系，结合动作偏移预测实现精确连续控制。
- **关键技术细节**：
  - 输入：多模态观测（视觉、本体感知、任务指令）经编码后得到上下文特征 \(g_t\)。
  - 分层技能预测：\(P(k_1,...,k_D|o,\tau) = \prod_{d=1}^D P(k_d|k_{<d}, g_t)\)，每个深度 \(d\) 的预测头输出码本索引的类别分布。
  - 动作细化：在技能解码基础上增加偏移预测头 \(\zeta_{\text{ref}}\)，输出连续偏移量，最终动作为 \(\hat{a}_t = \psi(\sum_d R_d e_{d,k_d}) + \zeta_{\text{ref}}(g_t)\)。
  - 训练损失：技能预测交叉熵损失 + 动作重建 L2 损失。

- **推理流程**：给定当前观测和任务指令 → CST 自回归采样技能代码（核采样）→ 解码并加上偏移 → 执行动作序列；滚动更新观测。

## 3. 实验设计

- **模拟 benchmark**：
  - **LIBERO**：包含五个套件（Object、Spatial、Goal、Long、90），共 130 个任务。每个任务 50 条专家演示。
  - **MetaWorld MT50**：50 个不同的操作任务，每个任务 100 条演示。
- **真实世界任务**：使用 Cobot Agilex ALOHA 机器人平台，两个长时顺序任务（抽屉操作、顺序物体放置），各 45 条人类遥操作演示，测试 10 次。

- **对比方法**：
  - 离散 LVM 方法：VQ-BeT、QueST
  - 端到端模仿学习：ResNet-T、Diffusion Policy、ACT
  - 大规模 VLA 模型：Octo、OpenVLA

- **评价指标**：成功率（Success Rate），每个任务 50 个 episodes，3 个随机种子。

## 4. 资源与算力

论文附录 A.4 明确说明：
- **GPU 型号与数量**：8 块 Nvidia RTX L40S 48GB GPU。
- **训练时长**：RaRSQ 训练 100 个 epochs，CST 训练 500 个 epochs。
- **其他细节**：使用 AdamW 优化器，余弦学习率衰减，warmup 10 个 epochs；所有模型可单 GPU 运行。

文中未提及总训练耗时（如小时数），但提供了关键配置。

## 5. 实验数量与充分性

- **数据量**：LIBERO 每个任务 50 条演示，MetaWorld 每个任务 100 条演示，真实世界每个任务 45 条演示。
- **实验组数**：
  - 主实验：LIBERO 5 个套件 × 50 任务 × 3 种子 = 750 个 run；MetaWorld 50 任务 × 3 种子 = 150 个 run。
  - 消融实验：表 2 对比了去掉 AR、去掉 Rotation、同时去掉两种组件，共 4 种变体，在每个套件上分别测试（5 套件 × 3 种子 = 15 run 每种变体）；表 B.1 还做了去掉动作细化的消融。
  - 码本利用率分析（图 4）、技能依赖模式可视化（图 7-8）、量化损失曲线（图 9）等附加分析。
- **充分性评价**：实验覆盖了多个模拟 benchmark（不同复杂度）和真实世界场景，对比了 7 种以上基线方法，消融验证了各组件作用。但真实世界任务仅 2 个，每个 10 次试次，样本量较小，可能存在偶然性。总体而言，实验设计较为系统、对比公平（均使用相同输入模态和编码器设置），结论可信。

## 6. 主要结论与发现

1. **STAR 显著超越基线**：在 LIBERO 上整体成功率 93.6%，较此前 SOTA QueST 提升 12.1%；在 MetaWorld MT50 上达 92.7%，提升 2.1%-5.4%。
2. **RaRSQ 有效防止码本崩溃**：所有 16 个码本向量均被活跃使用（VQ-VAE 仅 7 个），且分布更均匀。
3. **消融验证每个组件必要**：移除自回归预测或旋转机制均导致性能下降，尤其在长时任务上；同时移除下降最多（87.8% vs 93.6%）。
4. **动作细化至关重要**：去掉后 LIBERO-Long 成功率从 88.5% 跌至 37.6%，整体下降 34.6%。
5. **真实世界**：STAR 在顺序抽屉操作任务中完整完成率 30%（VQ-BeT 10%，QueST 0%），顺序放置任务完成率 60%（VQ-BeT 30%，QueST 40%）。

## 7. 优点

- **创新方法**：将旋转矩阵引入残差量化，编码几何关系，从根源上缓解码本崩溃，思路新颖且有效。
- **两阶段框架清晰**：先学技能表示，再学技能组合，解耦了表示学习和序列建模。
- **全面实验**：覆盖多个模拟 benchmark（LIBERO 多套件、MetaWorld）和真实世界，对比多种基线（含大规模 VLA 模型），消融完备。
- **理论与实验结合**：通过码本利用率、量化损失曲线、技能依赖矩阵等分析，深入揭示了方法为何有效。
- **通用性**：框架不依赖特定网络架构，可应用于多种机器人设置。

## 8. 不足与局限

- **超参数敏感**：码本大小 \(K\) 和量化深度 \(D\) 需手动调整，文中未讨论自动搜索方法，可能限制泛用性。
- **依赖专家演示**：作为模仿学习方法，性能受限于演示质量与数量；缺少演示时可能失效。
- **真实世界实验规模小**：仅 2 个任务各 10 次试次，统计显著性有限，且未展示不同光照、物体位置变化等泛化能力。
- **未评估跨任务泛化**：虽然多任务训练，但未测试在未见过的任务或物体上的零样本迁移。
- **计算资源提及有限**：虽给出 GPU 型号与数量，但未报告单次训练总耗时及推理效率，不利于复现比较。
- **对比基线版本**：部分基线结果引用原始论文（如 Octo、OpenVLA 标记†），可能因环境差异导致不公平，但作者在附录中尝试统一输入设定。

（完）
