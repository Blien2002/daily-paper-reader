---
title: Human-assisted Robotic Policy Refinement via Action Preference Optimization
title_zh: 通过动作偏好优化实现人类辅助的机器人策略精炼
authors: "Wenke Xia, Yichu Yang, Hongtao Wu, Xiao Ma, Tao Kong, Di Hu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=dlQ1iUpQNf"
tags: ["query:vla"]
score: 8.0
evidence: 通过人类偏好对齐对部署后的VLA模型进行精炼
tldr: VLA模型依赖离线专家演示，部署后无法在线优化。本文提出动作偏好优化（APO），通过人机协作收集交互轨迹并应用偏好对齐算法，使VLA模型能在真实环境中迭代改进。实验证明APO显著提升策略成功率与鲁棒性，为机器人系统的持续学习提供了实用方法。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1446, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1419, \"height\": 159, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1440, \"height\": 280, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1448, \"height\": 373, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1439, \"height\": 602, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1417, \"height\": 159, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-dlq1iupqnf/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1444, \"height\": 420, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1449, \"height\": 403, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 672, \"height\": 307, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 721, \"height\": 306, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 716, \"height\": 226, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 678, \"height\": 227, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 382, \"height\": 281, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-dlq1iupqnf/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 494, \"height\": 281, \"label\": \"Table\"}]"
motivation: VLA模型部署后无法利用环境反馈进行精炼，可靠性不足。
method: 提出APO方法，先通过人机协作收集失败修正轨迹，再利用偏好对齐优化VLA策略。
result: 在多个操纵任务上，APO精炼后的策略成功率显著高于基线。
conclusion: 人类辅助的偏好对齐可有效提升VLA模型的部署后性能。
---

## Abstract
Establishing a reliable and iteratively refined robotic system is essential for deploying real-world applications. 
    While Vision-Language-Action (VLA) models are widely recognized as the foundation model for such robotic deployment, their reliance on offline expert demonstrations critically limits their capacity for post-deployment refinement. 
    To mitigate this limitation, we introduce Action Preference Optimization (APO), a method designed to refine VLA models by human-assisted preference alignment gathered through interaction with environments.
    This method begins with a human-robot collaboration framework for reliable failure correction and interaction trajectory collection through human intervention.  
    However, directly leveraging these interaction trajectories for preference optimization is non-trivial due to the challenges of irreversible robotic actions and token distribution mismatch. To solve this, APO proposes an adaptive reweighting algorithm with binary desirability signals derived from interaction, empowering VLA models effectively suppress failure-prone actions while enhancing corrective action adaptation.
    Ultimately, APO equips VLA models with the crucial capability to learn from failure, paving the way for their iterative refinement and reliable deployment in dynamic environments.
    The experiments conducted in simulation and real-world scenarios prove superior generalization and robustness of our human-assisted framework across a variety of manipulation tasks. We believe this work could bring insights for efficient and stable optimization of VLA models through human-robot collaboration. The code and dataset are released at https://github.com/GeWu-Lab/Action-Preference-Optimization.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有的视觉-语言-动作（VLA）模型（如OpenVLA）主要依赖大规模离线专家演示数据集进行训练，缺乏部署后从环境反馈中持续学习和精炼的能力，导致在遇到失败或新场景时无法自适应改进，限制了其在动态真实世界中的可靠部署。
- **研究动机**：机器人系统需要在部署过程中不断从失败中学习、自我修正，而现有的行为克隆（BC）无法利用失败轨迹，强化学习（RL）在大模型训练中不稳定且难以扩展。因此需要一种既稳定又能充分挖掘失败信号的方法。
- **整体含义**：通过人类辅助的偏好对齐，使VLA模型获得“从失败中学习”的能力，实现部署后的迭代精炼和性能提升，为机器人系统在实际环境中的持续优化提供了可行路径。

## 2. 方法论：核心思想、关键技术细节

### 2.1 核心思想
- 提出**动作偏好优化（Action Preference Optimization, APO）**，通过人机协作部署收集交互轨迹，并将轨迹中的动作按成败标注为二元合意性信号，利用前景理论构建偏好对齐目标函数，同时设计自适应重加权策略解决VLA模型特有的动作不可逆和token概率不匹配两大挑战。

### 2.2 关键技术细节
- **人机协作部署框架**（Algorithm 1中的DEPLOYMENT函数）：
  - 先用专家演示数据通过行为克隆（BC）训练初始策略 \(\pi^0_\theta\)。
  - 在策略执行过程中，人类操作员实时监控，当机器人遇到困难时，人类通过SpaceMouse设备介入修正动作（标记 \(c_t=2\)），同时将干预前 \(K\) 步的动作自动标注为失败动作（标记 \(c_t=0\)），其余策略执行的动作标记为成功（\(c_t=1\)）。
  - 收集到的交互轨迹 \(D_h\) 与专家演示 \(D_e\) 混合用于后续优化。

- **动作偏好优化**（Algorithm 1中的OPTIMIZATION函数）：
  - **二元合意性效用函数**：基于Kahneman & Tversky前景理论，定义效用函数 \(v(o, \hat{a})\) ：
    - 对于合意动作：\(v = \lambda_D \sigma(r_\theta - z_0)\)
    - 对于不合意动作：\(v = \lambda_U \sigma(z_0 - r_\theta)\)
    - 其中 \(r_\theta(o,\hat{a}) = \log(\pi_\theta/\pi_{\text{ref}})\) 为隐性奖励，\(z_0 = KL(\pi_\theta || \pi_{\text{ref}})\) 为KL散度约束。
    - 损失函数：\(L = \mathbb{E}_{(o,a,c)\sim D_h}[-v(o,a)]\)，通过最小化损失使模型倾向于合意动作、避免不合意动作。
  - **自适应重加权**：针对VLA模型将连续动作离散化为token导致的概率与回归损失不匹配问题，提出基于连续动作L1损失的样本级动态权重：
    - 计算每个样本的连续动作预测误差 \(l_i = |\pi_\theta(o_i) - a_i|_1\)（解码后的连续动作）。
    - 批内归一化权重 \(w_i = l_i / \sum_{j=1}^B l_j\)。
    - 利用权重调整公式（5）和（6）中的 \(\lambda_D=1-e^{-\beta_D w}\) 和 \(\lambda_U=e^{-\beta_U w}\)，实现：合意样本中误差大的获得高权重，不合意样本中接近失败动作的获得高权重，从而精细控制每个样本的贡献。

- **平衡采样**：保证每批次中专家动作（\(c=1\)）占50%、人类干预动作（\(c=2\)）占25%、失败动作（\(c=0\)）占25%。

### 2.3 算法流程（文字说明）
1. **Warm-start**：用专家演示 \(D_e\) 通过BC训练初始策略 \(\pi^0_\theta\)。
2. **部署-优化循环**（重复多次）：
   - 设置参考模型 \(\pi_{\text{ref}} = \pi^i_\theta\)。
   - 部署当前策略，执行DEPLOYMENT函数收集新的交互轨迹加入 \(D_h\)。
   - 执行OPTIMIZATION函数：平衡采样、计算L1误差和自适应权重、基于损失函数 \(L\) 更新模型得到 \(\pi^{i+1}_\theta\)。

## 3. 实验设计

### 3.1 仿真环境与任务
- **数据集/场景**：使用RoboMimic仿真环境中的四个精细操作任务：Coffee_D0、StackThree_D0、ThreePieceAssembly_D0、Square_D0。每个任务提供300个专家演示。
- **基准方法**：对比了Dagger（BC）、Sirius（加权BC）、DPO（合成负样本）、TPO（轨迹级偏好优化）、KTO（二元信号偏好优化）。
- **评估指标**：每个任务在50次试验下报告平均成功率。

### 3.2 泛化实验（新颖场景）
- **三种干扰设置**：位置干扰（Square_D0中改变初始位置）、背景干扰（StackThree_D0中更换背景颜色）、纹理干扰（ThreePiece_D0中将红色块换成木纹块）。
- **终身学习实验**：每收集20次交互轨迹后更新模型，持续评估策略成功率和人类干预频率。
- **不同VLA模型**：额外测试π0-FAST模型（支持动作chunk预测），验证APO跨架构有效性。

### 3.3 真实世界实验
- **任务**：“插入方块到圆棒”、“将杯子挂到架子上”、“将柠檬放到盘子中”等精细操作。
- **设置**：收集100个专家演示训练基模型，再收集20条人类干预轨迹进行偏好优化。评估包括分布内和三种干扰场景（位置、背景、纹理变化）。

## 4. 资源与算力

- **文中明确说明**：
  - 基模型微调（BC阶段）：使用8块NVIDIA A100 GPU，batch size为16，LoRA秩r=32。
  - 偏好优化阶段：使用4块NVIDIA A100 GPU，batch size为8，学习率5e-5。
- **未明确说明**：训练总时长、迭代轮数等细节未提供，但可推测训练规模合理。

## 5. 实验数量与充分性

- **实验数量**：
  - 仿真环境：4个任务 × 3个随机种子 × 多次测试（50次试验），覆盖主比较、泛化、终身学习。
  - 真实世界：3个任务，每个评估20次试验。
  - 模型泛化：额外测试π0-FAST模型。
- **充分性分析**：
  - 正面：实验覆盖了分布内、分布外干扰、终身学习、不同模型架构、真实场景，对比了多种主流方法（BC、DPO、TPO、KTO），统计平均成功率，结果具有可重复性。
  - 不足之处：缺少对APO内部各组件的消融实验（例如：去除自适应重加权、固定权重、使用全配对偏好等），也未分析不同K值（失败标注步数）的影响，评估指标仅使用成功率单一指标，未分析人类干预成本或训练稳定性。

## 6. 主要结论与发现

1. **APO在仿真任务上平均成功率比基模型提升7.5个百分点（40.5%→48.0%）**，优于所有对比方法（如KTO为43.5%，TPO为41.5%），且仅APO在所有四项任务上均获得稳定提升。
2. 在干扰场景下，APO泛化性能最好（平均28.0%），同时保持了对原始任务的记忆（45.3%），而BC方法出现明显遗忘。
3. **终身学习实验中**，APO能通过持续交互不断改进策略成功率，并伴随人类干预频率下降，而BC随数据量增加后无法继续提升。
4. 在π0-FAST模型上，APO同样获得一致提升（如Square任务从85%→95%）。
5. 真实世界实验中，APO在分布内和三种干扰场景下均显著优于基线，平均成功率从基模型65%提升至85%+。
6. **APO使模型学会从失败中自我修正**（如重抓取、调整插入位置），而不仅仅是避免失败。

## 7. 优点

- **方法创新性**：首次将LLM领域的偏好对齐方法（基于前景理论）扩展到VLA机器人模型，并针对动作不可逆和token不匹配设计了自适应重加权，解决了直接迁移的困难。
- **实用性**：人机协作框架在部署时自动收集数据，无需额外标注，可不断迭代改进，工程可行性高。
- **实验全面性**：覆盖仿真和真实环境、多个任务、多种干扰、终身学习、不同VLA模型，实验设计较为严谨，对比方法多样。
- **性能稳定**：在所有实验中APO均能实现正向改进，无退化现象，优于其他偏好优化方法（如TPO在某些任务上反而下降）。
- **开放资源**：代码和数据集已开源，便于复现和进一步研究。

## 8. 不足与局限

- **模型架构局限**：仅测试了自回归VLA模型（OpenVLA、π0-FAST），未覆盖回归式策略或扩散策略（如Diffusion Policy），APO的通用性有待验证。
- **人类依赖**：需要实时人类干预才能收集交互轨迹，对于大规模部署可能成本较高；论文未讨论如何减少人类干预次数或利用自动失败检测。
- **消融实验缺乏**：未对自适应重加权、平衡采样、KL约束等组件进行系统性消融，也未分析不同K值（失效标注步数）的影响。
- **评估指标单一**：仅使用成功率，未报告动作误差、干预频率、训练损失曲线等，对算法稳定性、效率的讨论不足。
- **训练效率未讨论**：未说明APO相对于BC或RL的计算开销、训练时间等。
- **终身学习分析有限**：仅展示了短期迭代（20次一次），未测试长期多次迭代下的稳定性或灾难性遗忘边界。

（完）
