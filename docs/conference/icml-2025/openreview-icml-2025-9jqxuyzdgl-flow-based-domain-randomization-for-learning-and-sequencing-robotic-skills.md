---
title: Flow-based Domain Randomization for Learning and Sequencing Robotic Skills
title_zh: 基于流的域随机化用于学习与排序机器人技能
authors: "Aidan Curtis, Eric Li, Michael Noseworthy, Nishad Gothoskar, Sachin Chitta, Hui Li, Leslie Pack Kaelbling, Nicole E Carey"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=9JQXuyzdGL"
tags: ["query:vla"]
score: 7.0
evidence: 基于流的域随机化学习机器人技能
tldr: 针对强化学习中域随机化分布需手工设定的问题，提出用归一化流自动学习采样分布。通过熵正则化奖励最大化，该架构比已有方法更灵活、鲁棒性更强，并在机器人技能学习与排序任务中验证有效性，有助于具身智能策略训练。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1707, \"height\": 721, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1766, \"height\": 616, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1768, \"height\": 358, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1722, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1682, \"height\": 736, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1768, \"height\": 351, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1771, \"height\": 351, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1771, \"height\": 352, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1771, \"height\": 357, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1767, \"height\": 355, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1769, \"height\": 351, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1769, \"height\": 352, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1773, \"height\": 356, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-9jqxuyzdgl/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1725, \"height\": 1144, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-9jqxuyzdgl/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1317, \"height\": 172, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-9jqxuyzdgl/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1764, \"height\": 465, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-9jqxuyzdgl/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1309, \"height\": 426, \"label\": \"Table\"}]"
motivation: 手工指定域随机化分布成本高且不灵活。
method: 用归一化流通过熵正则化奖励最大化自动发现分布。
result: 比现有方法更灵活且鲁棒性更强。
conclusion: 可自动生成鲁棒控制策略，助力机器人学习。
---

## Abstract
Domain randomization in reinforcement learning is an established technique for increasing the robustness of control policies learned in simulation. By randomizing properties of the environment during training, the learned policy can be robust to uncertainty along the randomized dimensions. While the environment distribution is typically specified by hand, in this paper we investigate the problem of automatically discovering this sampling distribution via entropy-regularized reward maximization of a neural sampling distribution in the form of a normalizing flow. We show that this architecture is more flexible and results in better robustness than existing approaches to learning simple parameterized sampling distributions. We demonstrate that these policies can be used to learn robust policies for contact-rich assembly tasks. Additionally, we explore how these sampling distributions, in combination with a privileged value function, can be used for out-of-distribution detection in the context of an uncertainty-aware multi-step manipulation planner.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：在强化学习的仿真到现实迁移中，域随机化（Domain Randomization）是提高策略鲁棒性的关键技术，但传统方法需要手工指定随机化参数的分布（如高斯/均匀分布），这一过程耗时且不灵活。分布过宽会导致策略收敛到次优局部最优，过窄则导致现实泛化能力差。
- **背景**：机器人接触式装配任务（如齿轮插入）对不确定性敏感，现有自动学习方法（如ADR、LSDR、DORAEMON）多采用简单的参数化分布（如高斯、独立Beta分布），表达能力有限，难以处理参数间复杂依赖和多模态分布。
- **整体含义**：本文提出一种基于归一化流（Normalizing Flow）的自动域随机化方法（GoFlow），旨在自动发现最优的采样分布，最大化策略对未知目标环境的泛化能力，并进一步将该分布用于多步操作规划中的离群检测。

## 2. 方法论
- **核心思想**：将域随机化分布建模为归一化流，通过熵正则化奖励最大化联合优化策略和采样分布，同时引入KL散度正则化保证训练稳定性。
- **关键技术细节**：
  - **归一化流模型**：采用神经样条流（Neural Spline Flow）作为可逆变换，将标准正态基分布映射到复杂的多模态目标分布，参数为\(\phi\)。
  - **联合优化目标**：  
    \[
    \max_{p,\pi} \left\{ \mathbb{E}_{\xi \sim p}[J_\xi(\pi)] + \alpha H(p) - \beta D_{KL}(p_{\text{old}} \| p) \right\}
    \]  
    其中\(H(p)\)为微分熵，鼓励分布广；\(D_{KL}\)约束分布不剧烈变化。
  - **重要性采样**：从均匀分布\(u(\xi)\)采样，通过重要性权重\(\frac{p_\phi(\xi)}{u(\xi)}\)计算奖励和熵的估计，避免分布坍塌。
  - **Actor-Critic架构**：策略网络\(\pi_\theta\)仅接收观测（不含随机化参数\(\xi\)），而评论家网络\(V_\psi(s,\xi)\)可访问特权信息\(\xi\)，降低价值估计方差。
  - **算法流程**（Algorithm 1）：  
    ① 初始化策略参数\(\theta\)和流参数\(\phi\)；  
    ② 每轮迭代从当前流\(p_\phi\)采样环境参数训练策略；  
    ③ 从均匀分布采样测试参数，通过策略回滚估计回报\(J_\xi(\pi)\)；  
    ④ 保存旧分布\(p_{\phi_{\text{old}}}\)；  
    ⑤ 进行K步流参数更新，利用重要性采样估计奖励、熵和KL散度的梯度。

## 3. 实验设计
- **数据集/场景**：
  - **模拟环境**：Cartpole、Ant、Quadcopter、Quadruped、Humanoid（基于IsaacLab库），以及自定义的Gears（齿轮插入）接触式操作任务。
  - **真实世界**：Franka Emika机器人执行齿轮插入任务，随机化夹爪位姿误差。
- **基准测试**：衡量策略在均匀测试分布下的**覆盖率**（Coverage），即参数空间中奖励超过阈值\(J_T\)的比例。
- **对比方法**：
  - 无随机化（NoDR）、全随机化（FullDR，均匀采样）
  - ADR（OpenAI 2019）：学习均匀区间，边界采样渐近扩展
  - LSDR（Mozifian 2019）：学习多变量高斯分布，带KL正则化
  - DORAEMON（Tiboni 2024）：学习独立Beta分布，最大熵约束
- **实验充分性**：
  - 每个环境5个随机种子（Figure 3），报告均值和标准误。
  - 超参数搜索覆盖关键参数（\(\alpha, \beta\)等，见Appendix A.5）。
  - 附加实验：覆盖率随参数范围缩放（Figure 12）、覆盖率随阈值变化（Figure 13）。
  - 真实世界实验：每种方法10次试验（Table 1），进行统计显著性检验（p<0.05，z检验）。

## 4. 资源与算力
- 论文未明确说明使用的GPU型号、数量、训练时长等计算资源信息。从文中推断，训练在标准深度学习服务器上进行（使用PyTorch及IsaacLab模拟器），但具体硬件细节缺失。

## 5. 实验数量与充分性
- **实验数量**：共6个模拟域 + 1个真实域，每个模拟域5个随机种子，覆盖6种基线方法（含本文方法），超参数搜索涉及数十组配置。真实世界10次/方法。
- **充分性**：实验设计较为全面，覆盖不同复杂度（低维到高维）、不同参数依赖结构（如Gears域具有多模态依赖）。附有覆盖率-阈值敏感性分析、范围缩放分析，以及统计假设检验。
- **客观性与公平性**：所有基线共享相同的PPO实现和神经架构，超参数均通过搜索选择最优值。论文报告了统计显著性结果（Table 2），标注了与最优方法无显著差异的方法，态度客观。

## 6. 主要结论与发现
- GoFlow在**所有模拟环境**中的最终覆盖率匹配或超过所有基线，尤其在参数空间不平坦、具有多模态依赖时优势明显（如图2示例）。
- 在**真实世界齿轮插入**任务中，GoFlow成功率达9/10，显著优于其他方法（FullDR 6/10，其他5/10）。
- 学习到的采样分布和特权价值函数可用于**信念空间规划中的离群检测**：通过阈值\(\epsilon\)和\(\eta\)过滤低概率/低价值区域，构建技能的前提条件，从而使机器人能在信息不足时主动执行检查动作。

## 7. 优点
- **灵活性**：归一化流可建模任意复杂的参数分布（多模态、非凸、参数间依赖），远超高斯或独立Beta分布的表达能力。
- **自动性**：无需手工指定方差或边界，通过联合优化自动发现“可求解且多样化”的分布。
- **鲁棒性**：通过重要性采样从均匀分布计算奖励和熵，避免分布过早坍塌。
- **实用价值**：在真实接触式装配任务中表现优异，且可将流分布与价值函数结合用于不确定性感知的高层规划。
- **可扩展性**：方法可无缝集成到演员-评论家框架中，与PPO等主流算法兼容。

## 8. 不足与局限
- **训练不稳定**：归一化流偶尔可能出现训练不稳定，增大\(\beta\)可缓解但会降低样本效率（Appendix A.5）。
- **手动调参**：用于信念空间规划时需要手动选择阈值\(\epsilon\)和\(\eta\)，依赖环境特性和人工经验。\(\eta\)可转化为成本但\(\epsilon\)难以移除。
- **价值函数可信区域**：区分“价值函数校准”与“未校准”区域（通过\(\epsilon\)）的方法较为粗糙，缺乏严格的不确定性量化。
- **计算开销**：流网络的训练和重要性采样增加了每轮迭代计算量，虽未明确对比效率，但理论上比简单参数化方法更重。
- **实验覆盖**：虽涉及多种环境，但所有任务均为sim-to-real，未测试纯在线学习或动态环境变化场景；真实实验仅针对一种齿轮插入，泛化性有待更多验证。

（完）
