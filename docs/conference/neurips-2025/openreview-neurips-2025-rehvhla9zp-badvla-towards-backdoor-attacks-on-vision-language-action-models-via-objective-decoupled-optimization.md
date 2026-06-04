---
title: "BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models via Objective-Decoupled Optimization"
title_zh: BadVLA：通过目标解耦优化对视觉-语言-动作模型的后门攻击
authors: "Xueyang Zhou, Guiyao Tie, Guowen Zhang, Hecheng Wang, Pan Zhou, Lichao Sun"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=rEhVHla9zp"
tags: ["query:vla"]
score: 8.0
evidence: 针对视觉-语言-动作模型的后门攻击
tldr: BadVLA首次揭示视觉-语言-动作（VLA）模型在后门攻击下的脆弱性。提出目标解耦优化方法，分两阶段注入后门：先学习触发模式，再与合法任务目标联合优化。实验表明在多个VLA基准上攻击成功率极高且保持任务性能，警示了VLA模型在训练即服务范式下的安全风险。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1430, \"height\": 567, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1439, \"height\": 446, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 670, \"height\": 566, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1429, \"height\": 976, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1425, \"height\": 483, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1423, \"height\": 930, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1419, \"height\": 935, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1428, \"height\": 929, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1424, \"height\": 948, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1433, \"height\": 441, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1434, \"height\": 441, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-rehvhla9zp/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1434, \"height\": 441, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1445, \"height\": 443, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 510, \"height\": 387, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1440, \"height\": 290, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1439, \"height\": 300, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1438, \"height\": 305, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1438, \"height\": 370, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 894, \"height\": 386, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 989, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1324, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 847, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1432, \"height\": 475, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-rehvhla9zp/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 703, \"height\": 139, \"label\": \"Table\"}]"
motivation: VLA模型在机器人控制中广泛应用，但其安全漏洞（尤其是后门攻击）尚未被研究。
method: 提出目标解耦优化，分两阶段注入后门触发并保持任务性能。
result: 在多个VLA基准上实现高攻击成功率和低任务性能损失。
conclusion: VLA模型存在严重后门风险，需在部署前加强安全防护。
---

## Abstract
Vision-Language-Action (VLA) models have advanced robotic control by enabling end-to-end decision-making directly from multimodal inputs. However, their tightly coupled architectures expose novel security vulnerabilities. Unlike traditional adversarial perturbations, backdoor attacks represent a stealthier, persistent, and practically significant threat—particularly under the emerging Training-as-a-Service paradigm—but remain largely unexplored in the context of VLA models. To address this gap, we propose **BadVLA**, a backdoor attack method based on Objective-Decoupled Optimization, which for the first time exposes the backdoor vulnerabilities of VLA models. Specifically, it consists of a two-stage process: (1) explicit feature-space separation to isolate trigger representations from benign inputs, and (2) conditional control deviations that activate only in the presence of the trigger, while preserving clean-task performance. Empirical results on multiple VLA benchmarks demonstrate that BadVLA consistently achieves near-100\% attack success rates with minimal impact on clean task accuracy. Further analyses confirm its robustness against common input perturbations, task transfers, and model fine-tuning, underscoring critical security vulnerabilities in current VLA deployments. Our work offers the first systematic investigation of backdoor vulnerabilities in VLA models, highlighting an urgent need for secure and trustworthy embodied model design practices.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：视觉-语言-动作（VLA）模型通过端到端多模态输入实现机器人控制，但其紧密耦合的架构带来了新的安全漏洞。传统对抗扰动研究较多，但后门攻击（更隐蔽、持久、实际威胁大）在VLA领域尚未被探索。尤其在“训练即服务”（TaaS）范式下，用户将模型训练外包给第三方，后门注入风险显著增加。
- **整体含义**：本文首次系统性地揭示了VLA模型在后门攻击下的脆弱性。提出了一种名为BadVLA的后门攻击方法，证明了攻击者可以在不影响正常任务性能的前提下，植入不可察觉的视觉触发器，在部署后导致策略行为失控。这项工作为后续VLA安全防御研究奠定了基础。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：通过“目标解耦优化”（Objective-Decoupled Optimization），将后门注入过程分解为两个独立阶段，分别处理特征空间分离和任务性能保持，从而避免传统联合优化中任务性能与攻击效能互相干扰的问题。
- **关键技术细节**：
  - 模型分解：将VLA模型分为感知模块（\(f_p\)）、骨干模块（\(f_b\)）和动作模块（\(f_a\)）。
  - **阶段一（触发注入）**：冻结骨干和动作模块，仅优化感知模块。使用参考对齐对比训练：一方面保持干净输入下目标模型与参考模型输出一致（保留原本能力），另一方面确保带触发输入的特征与干净特征在隐空间显著分离。损失函数为：
    \[
    L_{\text{trig}} = \frac{1}{N}\sum \|f_\theta(x_i)-f_{\text{ref}}(x_i)\|_2^2 - \alpha \cdot \frac{1}{N}\sum \|f_\theta(T(x_i,\delta))-f_\theta(x_i)\|_2^2
    \]
    其中 \(\alpha\) 为权衡超参数，\(T\) 为触发注入函数。
  - **阶段二（干净任务增强）**：冻结已注入后门的感知模块，仅优化骨干和动作模块。在干净数据上以负对数似然损失微调，确保正常任务性能。由于感知模块已固化，干净输入对应正常特征空间，触发生成的异常特征未被训练覆盖，导致动作输出偏离正常轨迹。
- **算法流程**（文字描述）：
  1. 初始化目标模型参数（从参考模型复制感知模块参数）。
  2. **阶段一**：设置感知模块可训练，其他模块冻结；对每个干净样本生成带触发版本；计算干净特征、触发特征和参考特征；计算触发损失并更新感知模块参数；重复 \(N_1\) 个epoch。
  3. **阶段二**：冻结感知模块，解冻骨干和动作模块；对每个干净样本预测动作序列；计算干净任务损失并更新骨干和动作模块参数；重复 \(N_2\) 个epoch。
  4. 返回最终后门注入模型。

## 3. 实验设计

- **数据集与场景**：
  - 主要使用 **LIBERO** 基准，包含四个任务套件：LIBERO-Spatial、LIBERO-Object、LIBERO-Goal、LIBERO-100（Long）。每个套件分别训练和评估OpenVLA模型的不同变体。
  - 另外使用 **SimplerEnv** 环境评估 SpatialVLA 模型（更简单的机器人任务，如取可乐罐、移动物体等）。
- **Benchmark**：以任务成功率（SR，Success Rate）衡量干净性能，以攻击成功率（ASR，Attack Success Rate）衡量后门有效性。ASR定义基于有无触发器时成功率的相对变化。
- **对比方法**：
  - **数据投毒（Data-Poisoned）**：BadNet风格，给输入加上固定视觉触发器并配随机动作标签，混合干净数据训练。
  - **模型投毒（Model-Poisoned）**：使用UADA最大化触发下动作偏差，通过7维动作离散化后计算soft预测与目标背离标签的均方误差损失。
  - **基线（Baseline）**：正常训练的模型（无后门）。
- **触发器类型**：像素块（Block）、红色杯子（Mug）、红色棒（Stick），以及不同大小和位置的合成块触发器。

## 4. 资源与算力

- 论文在附录A中明确说明：所有实验在 **8块 NVIDIA A800 GPU** 的分布式设置上完成。
- 对于OpenVLA变体：阶段一训练3000步（batch size 2），阶段二训练30000步（batch size 4）。对于SpatialVLA：阶段一1000步（batch size 4），阶段二100个epoch（batch size 16）。算力投入适中，但未报告具体时长。

## 5. 实验数量与充分性

- **实验组数**：涵盖四大LIBERO套件（各独立训练OpenVLA），三种触发器类型（Block、Mug、Stick），以及SpatialVLA在三个简单任务上的验证。此外还包括：
  - 触发器大小/位置分析（3种大小×3种位置）
  - 跨模态触发评估（文本 vs. 图像）
  - 轨迹分析（定性可视化）
  - 特征空间余弦相似度分析
  - 消融实验（去掉阶段二、去掉参考对齐损失、去掉触发分离损失）
  - 鲁棒性测试：JPEG压缩（5个级别）、高斯噪声（5个级别）、重微调（跨任务迁移）、物理扰动（光照、遮挡、视角）
  - 防御评估：剪枝微调（Fine-Pruning，5个剪枝率）、图像净化（3种强度）
  - 超参数分析（λ和学习率）
- **充分性与客观性**：实验设计较为全面，覆盖了多种攻击场景、多种模型架构、多种防御手段和物理扰动，对比基线合理，消融实验揭示了各组件的必要性。但未报告误差条或重复运行统计，可能影响对结果稳定性的判断。总体而言，实验在广度和深度上都较充分。

## 6. 主要结论与发现

- **攻击有效性**：BadVLA在LIBERO所有套件上，对OpenVLA模型达到平均ASR 96.1%~98.8%，而干净任务SR仅下降0.8%左右；SpatialVLA上ASR最高达100%。基线方法完全失效（ASR=0或SR=0）。
- **触发器隐蔽性**：即使1%图像面积的微小触发器也能达到高ASR（>90%），且位置变化不影响攻击效能。
- **物理鲁棒性**：在光照变化、遮挡、视角偏移等物理扰动下，ASR仍保持89%~100%，说明触发器在物理世界可稳定激活。
- **防御鲁棒性**：JPEG压缩、高斯噪声、剪枝微调、图像净化等现有防御手段对BadVLA效果有限；剪枝微调下ASR仍>94%，强净化虽降低ASR但严重破坏正常性能。
- **跨任务持久性**：将后门模型在新任务上微调后，干净性能恢复，但后门仍然存活（ASR在90%以上），表明后门嵌入在深层特征中，不易被简单微调消除。
- **本质**：后门行为表现为轨迹逐渐偏离正常路径，而非瞬间突变，具有隐蔽性和累积性。

## 7. 优点

- **方法创新性**：首次提出针对VLA模型的专用后门攻击框架，目标解耦的两阶段优化策略巧妙平衡了触发有效性与任务保真性，避免传统联合优化的问题。
- **攻击实用性**：支持多种触发器（像素级、语义物体），大小位置可调，且在物理世界扰动下鲁棒，适用于实际部署场景。
- **实验全面性**：涵盖多个模型（OpenVLA、SpatialVLA）、多个数据集、多种防御和扰动，消融实验清楚验证了各组件贡献。
- **开源贡献**：代码已公开，便于复现和后续研究。

## 8. 不足与局限

- **实验覆盖偏差**：
  - 仅使用LIBERO和SimplerEnv两种仿真环境，未在真实机器人上验证（论文未提及，但物理扰动实验在仿真中模拟）。
  - 仅评估了OpenVLA和SpatialVLA两种模型架构，对更多VLA模型（如RT-2、Octo等）的适用性未知。
- **方法局限**：
  - 主要针对非目标后门（untargeted backdoor），未探索目标后门（使机器人执行特定错误动作）是否同样有效。论文在结论中承认这一限制。
  - 只能通过视觉模态注入后门，对语言模态攻击无效（如图3所示，当前VLA模型对语言指令扰动不敏感）。
  - 需要白盒访问模型参数和架构（阶段一中利用参考模型），在完全黑盒的TaaS场景中可能受限（但论文认为开源模型生态下白盒假设合理）。
- **评价指标**：ASR公式基于成功率比值，可能对极低SR情况不够敏感。论文中基线方法SR为0时ASR也为0，但原因是模型完全失效而非后门未激活。
- **重复性**：未报告多次实验的标准差或置信区间，无法评估结果统计稳定性。

（完）
