---
title: "Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy"
title_zh: 动态测试时计算扩展：困难感知随机插值策略
authors: "Inkook Chun, Seungjae Lee, Michael Samuel Albergo, Saining Xie, Eric Vanden-Eijnden"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=oDoPiR8wZJ"
tags: ["query:vla"]
score: 7.0
evidence: DA-SIP自适应调整机器人操作策略的计算资源
tldr: 现有扩散策略在机器人操作中采用固定推理预算，导致简单子任务计算浪费而复杂任务精度不足。DA-SIP通过困难度分类器实时调整积分步数，在保持高性能的同时降低计算开销。在多种操作任务上，该方法显著提升效率，尤其适用于长程复杂操作。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-odopir8wzj/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1435, \"height\": 381, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-odopir8wzj/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1449, \"height\": 470, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-odopir8wzj/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1391, \"height\": 816, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1326, \"height\": 278, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1483, \"height\": 420, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 379, \"height\": 317, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 399, \"height\": 369, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 569, \"height\": 351, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1431, \"height\": 433, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1310, \"height\": 396, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1188, \"height\": 395, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1144, \"height\": 346, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1361, \"height\": 455, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1270, \"height\": 420, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1441, \"height\": 298, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1415, \"height\": 803, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1438, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1415, \"height\": 570, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1370, \"height\": 705, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1351, \"height\": 531, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1432, \"height\": 895, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1117, \"height\": 391, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 804, \"height\": 312, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-021.webp\", \"caption\": \"\", \"page\": 0, \"index\": 21, \"width\": 1013, \"height\": 354, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-022.webp\", \"caption\": \"\", \"page\": 0, \"index\": 22, \"width\": 1441, \"height\": 391, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-023.webp\", \"caption\": \"\", \"page\": 0, \"index\": 23, \"width\": 556, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-odopir8wzj/table-024.webp\", \"caption\": \"\", \"page\": 0, \"index\": 24, \"width\": 588, \"height\": 275, \"label\": \"Table\"}]"
motivation: 固定推理预算无法适应不同难度的操作子任务，造成计算浪费或性能不足。
method: 提出DA-SIP框架，利用RGB-D观测的困难度分类器动态选择积分步数。
result: 在多个操作基准上，DA-SIP在保持或提升成功率的同时大幅降低推理时间。
conclusion: 自适应推理是提升机器人操作策略效率的有效方法。
---

## Abstract
Diffusion- and flow-based policies deliver state-of-the-art performance on long-horizon robotic manipulation and imitation-learning tasks. However, these controllers employ a fixed inference budget at every control step, regardless of task complexity, leading to computational inefficiency for simple subtasks while potentially underperforming on challenging ones. To address these issues, we introduce Difficulty-Aware Stochastic Interpolant Policy (DA-SIP), a framework that enables robotic controllers to adaptively adjust their integration horizon in real-time based on task difficulty. Our approach employs a difficulty classifier that analyzes RGB-D observations to dynamically select the step budget, the optimal solver variant, and ODE/SDE integration at each control cycle. DA-SIP builds upon the stochastic interpolant formulation to provide a unified framework that unlocks diverse training and inference configurations for diffusion- and flow-based policies. Through comprehensive benchmarks across diverse manipulation tasks, DA-SIP achieves 2.6-4.4× reduction in total computation time while maintaining task-success rates comparable to fixed maximum-computation baselines. By implementing adaptive computation within this framework, DA-SIP transforms generative robot controllers into efficient, task-aware systems that intelligently allocate inference resources where they provide the greatest benefit.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：现有的扩散（diffusion）和流（flow）策略在机器人操作和模仿学习任务中表现优异，但在每个控制步骤都采用固定的推理预算（相同的求解器、步数、插值路径），无论任务复杂度如何。这导致简单子任务浪费计算资源，而复杂子任务可能因预算不足而性能下降。
- **背景**：大型语言模型（LLM）通过自适应推理（如思维链）在困难问题上分配更多计算资源。机器人操作任务同样存在异构性：粗放运动（如自由空间移动）所需计算少，而亚毫米级精确放置需要高计算量。受此启发，作者提出**Difficulty-Aware Stochastic Interpolant Policy (DA-SIP)**，将自适应测试时计算（test-time compute scaling）引入机器人控制策略。
- **整体含义**：DA-SIP使得机器人控制器能够根据任务难度动态调整积分步数、求解器类型和ODE/SDE模式，在保持任务成功率的条件下大幅降低总计算时间，推动生成式机器人控制向高效、任务感知的方向发展。

## 2. 论文提出的方法论

### 2.1 核心思想
- 基于**随机插值（Stochastic Interpolant, SI）** 框架统一扩散和流策略，该框架支持灵活的插值路径（线性、VP、GVP）和训练目标（速度、分数、噪声），且训练后的策略网络可同时支持ODE和SDE推理。
- 训练一个**难度分类器**，利用当前RGB-D观测预测子任务难度等级，然后根据难度等级动态选择推理配置三元组：步数、求解器类型、ODE/SDE模式。

### 2.2 关键技术细节

#### 随机插值策略（SIP）
- 定义随机插值过程：\( I_t = \alpha_t x^* + \sigma_t \varepsilon \)（\( t \in [0,1] \)），从动作序列 \( x^* \) 插值到标准高斯噪声 \( \varepsilon \)。
- 学习速度场 \( v(x,t,o) = E[\dot{I}_t | I_t = x, o] \) 通过最小化均方损失；或学习分数 \( s(x,t,o) \)。
- 通过反向SDE生成动作：\( dX_t = [v - \frac{1}{2} w_t s] dt + \sqrt{w_t} d\bar{W}_t \)，其中 \( w_t \) 可调。
- 支持三种插值：Linear、Variance-Preserving (VP)、Generalized VP (GVP)。

#### 难度分类方法
- **轻量CNN分类器**：ResNet-18骨干 + 分类头，训练于300张标注图像/任务，推理约20ms。
- **少样本VLM分类器**：使用预训练VLM（如Qwen2.5-VL）配合1-3张示例图像进行上下文分类，推理约500-1000ms。
- **微调VLM分类器**：使用LoRA微调Qwen2.5-VL-7B，训练于300张图像，推理约300-400ms，准确率最高。

#### 自适应计算分配
- 难度级别 \( d \in \{1,2,3\} \) 映射为配置三元组：
  - Easy (\( d=1 \)): 5步, Euler, ODE
  - Medium (\( d=2 \)): 10步, Heun, ODE
  - Hard (\( d=3 \)): 20步, RK4, SDE
- 映射通过验证集经验确定，平衡性能与效率。

### 2.3 算法流程（文字说明）
1. 训练阶段：使用SI框架训练一个统一的策略网络（支持速度/分数预测），同时训练难度分类器（CNN/VLM）。
2. 推理阶段：在每个控制周期，获取RGB-D观测，难度分类器预测难度级别，映射为推理配置三元组，SIP使用该配置生成动作序列，执行动作后进入下一状态。

## 3. 实验设计

### 3.1 数据集/场景
- **仿真环境**：RoboMimic（Can, Lift, Square, Tool Hang）、Block Push（Fetch）、Push-T、Kitchen、Multimodal Ant（DM Control）。这覆盖了简单操作、精密操作、探索性操作、运输放置等多样化任务。
- **难度标注数据集**：收集约20,000个标记状态（由8名标注者通过多数投票确定6个难度类别：初始、接近、抓取、随机、连续推、结束），用于训练分类器。

### 3.2 Benchmark
- 对比基线：固定最大计算（如100步Heun SDE）、固定最小计算（1步Euler ODE）、以及固定中间配置。
- 方法对比：SIP与扩散策略（DDPM、DDIM）的性能和效率比较。
- 分类器对比：轻量CNN vs. 少样本VLM vs. 微调VLM。

### 3.3 评价指标
- 任务成功率（Success Rate）
- 总计算时间（秒）及加速倍数
- 难度分类准确率

## 4. 资源与算力

- **策略训练**：使用NVIDIA L40S GPU（表1脚注提及，未说明具体数量），每配置训练5,000个epoch，3个随机种子。
- **分类器训练**：CNN在单GPU上训练100 epoch；VLM微调使用单GPU（可能8-bit量化，LoRA）。
- **推理时间**：每控制周期CNN约0.023s（分类）+ 0.3s（SIP策略推理）≈1.357s总时间；微调VLM约0.362s+0.127s≈1.535s。
- 总体算力消耗未给出精确数字，但实验规模中等。

## 5. 实验数量与充分性

- **实验充分性**：覆盖6+个仿真任务，每种任务评估多种配置（步数、求解器、ODE/SDE变体），并报告“最终10个检查点的平均成功率”（每检查点50个episode，每种子3个推理种子，共9次运行/配置）。实验设计较为严谨。
- **消融实验**：
  - 分类器数据量消融（100、200、300、500、2000张图像），证明300张即可接近平台期。
  - 求解器与插值消融（Table 1, 11-15）。
  - 噪声鲁棒性测试（高斯噪声σ从0到2.0）。
  - 少样本示例数量消融（1、2、3张/类）。
  - 真实机器人数据验证（Push-T真实数据训练MSE）。
- **客观公平性**：与标准扩散策略（DDPM、DDIM）在同一设置下比较，使用了公开数据集和基准。未采用不公平的蒸馏技术。但Tool Hang任务中SIP性能显著低于扩散策略，作者已指出。

## 6. 论文的主要结论与发现

1. **无单一最优配置**：不同任务需要不同的求解器、步数和积分模式，不存在适用于所有任务的固定配置。
2. **自适应计算有效**：DA-SIP实现2.6–4.4×总计算时间减少，同时维持与最大计算基线相当的成功率（平均成功率差异仅1.3–4.7%）。
3. **分类器性能**：轻量CNN在准确率和效率上最佳（～90%准确率，20ms推理）；微调VLM取得最佳平衡（高准确率+合理延迟）。
4. **简单任务极度高效**：如Lift和Can仅需1步即可达到100%成功率，无需大量计算。
5. **探索性任务需适中型计算**：Tool Hang和Multimodal Ant在中等步数（25-50）达到最佳，步数更多反而有害，说明需要受控随机性。

## 7. 优点

- **统一框架**：基于随机插值统一了扩散和流策略，暴露了丰富的训练-推理设计空间（预测目标、插值路径、ODE/SDE），无需重训练即可调整推理配置。
- **实际部署价值高**：自适应计算显著降低推理延迟，适合资源受限的物理机器人平台；轻量CNN分类器延迟极低。
- **实验全面**：在多种任务类型、多种求解器/步数组合、多种分类器下进行了系统评价，消融实验充分。
- **方法简洁有效**：不需要修改底层策略网络，仅通过外部分类器实现自适应，即插即用。
- **开源友好**：使用公开环境和数据集，代码疑似将开源。

## 8. 不足与局限

- **主要局限**：实验全部在仿真环境中进行，缺乏真实机器人部署验证（仅附录有真实数据训练MSE，未执行实际轨迹）。作者承认未来需“转移到真实机器人”。
- **分类器标注依赖**：训练分类器需要人工标注约300张/任务，虽然标注量不大但人工成本仍存在，且不同任务需重新标注。
- **VLM方法效率低**：少样本和微调VLM分类器推理延迟高（数百毫秒），可能不适合高频率控制；少数场景VLM准确率不到50%（如Square工具挂载）。
- **Tool Hang任务性能劣于扩散策略**：SIP在该任务上成功率显著低于DDPM/DDIM（0.381 vs 0.534），作者归因于SI框架在该任务上优化不足，但未给出解决方案。
- **缺乏安全与鲁棒性讨论**：未考虑接触丰富任务中的安全监控，自适应计算可能因分类失误导致危险。
- **泛化性有限**：分类器需按任务训练，难以直接迁移到未见过任务（除非使用VLM少样本但效果差）。框架未支持跨任务泛化。
- **算力报告不完整**：未提供GPU数量、训练总时长等细节，影响可复现性评估。

（完）
