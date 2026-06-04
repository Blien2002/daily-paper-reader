---
title: "HybridVLA: Collaborative Autoregression and Diffusion in a Unified Vision-Language-Action Model"
title_zh: HybridVLA：统一视觉-语言-动作模型中的协作自回归与扩散
authors: "Jiaming Liu, Hao Chen, Pengju An, Zhuoyang Liu, Renrui Zhang, Chenyang Gu, Xiaoqi Li, Ziyu Guo, Sixiang Chen, Mengzhen Liu, Chengkai Hou, Mengdi Zhao, KC alex Zhou, Pheng-Ann Heng, Shanghang Zhang"
date: 2025-05-10
pdf: "https://openreview.net/pdf?id=8VyjwyLuSl"
tags: ["query:vla"]
score: 9.0
evidence: 结合自回归和扩散的统一视觉-语言-动作模型
tldr: 自回归VLA方法量化动作损失连续性，扩散VLA方法未充分利用VLM推理能力。本文提出HybridVLA，将VLM的自回归推理与扩散模型的连续动作预测统一在同一框架中，既保留了常识推理又实现了精细控制。在多个机器人操纵基准上，HybridVLA超越了纯自回归或纯扩散方法，为VLA模型设计提供了新方向。
source: NeurIPS-2025-Rejected-Public
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1439, \"height\": 400, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1427, \"height\": 699, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 732, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1450, \"height\": 657, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1410, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 661, \"height\": 554, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1395, \"height\": 781, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-8vyjwylusl/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1398, \"height\": 790, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 734, \"height\": 111, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1451, \"height\": 239, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 714, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 710, \"height\": 377, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 730, \"height\": 1478, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1449, \"height\": 159, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-8vyjwylusl/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 638, \"height\": 131, \"label\": \"Table\"}]"
motivation: 现有VLA模型要么损失动作连续性，要么牺牲推理能力。
method: 设计统一框架，自回归部分从VLM生成动作token序列，扩散部分建模连续动作分布，两者联合训练。
result: 在多个机器人基准上，HybridVLA同时实现了高精度控制与强语义理解，性能领先。
conclusion: 结合自回归与扩散可以兼顾VLA模型的推理能力与动作连续性。
---

## Abstract
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM’s pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心矛盾**：现有的视觉-语言-动作（VLA）模型主要分为两类——自回归类方法和扩散类方法。自回归VLA（如OpenVLA、RT-2）继承了VLM的常识推理能力，通过下一个token预测生成离散动作，但量化动作会破坏连续性，影响精细控制；扩散VLA（如π0、CogACT）在VLM后附加独立的扩散头以预测连续动作，但仅将VLM作为特征提取器，未能通过token级生成充分挖掘VLM预训练的推理能力。
- **研究目标**：如何将自回归的语义推理与扩散的连续动作预测优雅地统一在单个大语言模型（LLM）中，实现两者的相互增强，而非简单拼接。
- **整体含义**：提出HybridVLA，首个在单一LLM内同时集成扩散与自回归动作生成能力的VLA框架，既保留连续动作的精细控制，又发挥VLM的上下文推理优势，在仿真和真实世界任务中均达到SOTA。

## 2. 方法论：核心思想、关键技术细节

### 2.1 核心思想
- 在同一个LLM（基于LLaMA-2 7B或Phi-2 2.7B）中同时进行扩散动作生成和自回归动作生成，并让两者通过共享骨干网络相互增强。
- 设计协作训练策略（Collaborative Training Recipe）弥合两种生成范式的差异，并通过协作动作集成（Collaborative Action Ensemble）根据自回归置信度自适应融合预测结果。

### 2.2 关键技术细节
#### 架构设计
- **视觉编码器**：7B版本使用DINOv2和SigLIP双编码器，2.7B版本使用CLIP；多视角图像通过共享编码器后沿token维度拼接。
- **LLM输入**：语言prompt经tokenizer编码，视觉特征经MLP投影，机器人状态经MLP映射为嵌入，三者与扩散噪声/时间步嵌入拼接。
- **Token序列设计**：按顺序组织为 `[视觉token，语言token，机器人状态嵌入，<BOD>，扩散token，<EOD>，自回归token]`。扩散token位于自回归token之前，避免信息泄露；特殊标记<BOD>/<EOD>明确边界。
- **扩散动作生成**：训练时，将加噪动作和去噪时间步通过MLP投影到LLM嵌入空间；推理时使用DDIM 4步去噪，每一步迭代送入LLM预测噪声。引入KV缓存复用条件信息，消除冗余计算。
- **自回归动作生成**：将7-DOF/14-DOF动作量化离散化为token，使用交叉熵损失训练。

#### 混合目标函数
- `L_hybrid = L_diff + L_ce`，其中`L_diff`是扩散噪声的MSE损失，`L_ce`是自回归token的交叉熵损失。两个损失共同反向传播，使LLM同时学习连续动作表示和语义推理表示。

#### 训练流程
1. **大规模预训练**：在35个公开机器人数据集（共760K轨迹、33M帧，涵盖Open X-Embodiment、DROID、ROBOMIND等）上训练5个epoch。
2. **下游微调**：在自收集的仿真（RLBench）和真实数据上微调300 epoch，每个任务100个演示。

#### 协作动作集成
- 计算自回归动作token的平均置信度`c`；若`c ≥ 0.96`，则取扩散动作与自回归动作的平均；否则仅用扩散动作。该阈值通过消融实验确定。

## 3. 实验设计

### 3.1 仿真实验
- **Benchmark**：RLBench（CoppeliaSim模拟器），包含10种桌面任务（如Close box、Close laptop、Toilet seat down、Sweep to dustpan、Close fridge、Phone on base、Take umbrella out、Frame off hanger、Wine at rack、Water plants），使用Franka Panda单臂机器人。
- **数据**：每个任务100条轨迹，基于预定义路点和OMPL采样。
- **对比方法**：ManipLLM (7B)、OpenVLA (7B)、π0 (2.6B)、CogACT (7B)，均加载官方预训练权重。
- **评估**：每个任务20次rollout，重复3次，报告平均成功率及方差。

### 3.2 真实世界实验
- **单臂任务**（Franka Research 3，前视+腕部相机）：Pick and place、Unplug charger、Open drawer and place inside、Pour water、Wipe blackboard（各100演示）。
- **双臂任务**（AgileX双臂机器人，外部+左右腕部相机）：Pick and place、Lift ball and place、Place bottles at rack、Wipe blackboard、Fold shorts（各100演示）。
- **对比**：单臂与CogACT、π0对比；双臂仅与π0对比（CogACT不支持多视角输入）。
- **评估**：每个任务20次rollout，人工判定成功。

### 3.3 泛化实验
- 设计4种场景：未见过物体、杂乱背景、非平面高度变化、不同光照。
- 单臂Pick and place任务对比CogACT，双臂Lift ball and place任务对比π0。

## 4. 资源与算力
- **预训练**：35个数据集总计760K轨迹/33M帧，使用A800 GPU，训练超过10K GPU小时。
- **微调**：仿真和真实微调均在8块NVIDIA A800 GPU上完成，使用混合精度训练，每阶段300 epoch。
- **推理**：单块NVIDIA 4090D GPU测试，bfloat16精度，不使用action chunking。HybridVLA-dif (7B) 达9.4 Hz，HybridVLA (7B) 为6.1 Hz。

## 5. 实验数量与充分性
- **仿真**：10个任务 × 20 rollouts × 3次重复 → 充分覆盖多种操作类型。
- **真实**：单臂5任务、双臂5任务各20 rollouts → 涵盖精确放置、旋转、长时序、双臂协调等挑战。
- **消融实验**：共6组对比（Ex0–Ex6），验证协作训练、大规模预训练、机器人状态嵌入、token序列设计、置信度阈值、KV缓存、去噪步数等组件有效性。
- **泛化实验**：4种不可见场景对比两种基线，每个条件20 rollouts。
- **缺陷分析**：提供了三类失败案例（旋转偏差、超出自由度限制、双臂协调错误）。
- **公平性**：所有基线使用官方预训练权重，相同训练设置；HybridVLA仅修改架构和损失，基础视觉/语言骨干一致。

## 6. 主要结论与发现
- HybridVLA (7B) 在仿真10任务中平均成功率74%，超越CogACT（60%）14%，超越OpenVLA（41%）33%。
- 真实世界单臂平均83%，双臂平均71%，优于π0（45%和55%）和CogACT（61%）。
- 扩散和自回归在不同任务上表现互补：扩散适合精细操作，自回归适合语义推理。协作集成进一步提升鲁棒性。
- 协作训练使两者相互增强：仅用扩散的版本（HybridVLA-dif）也优于先前扩散VLA方法。
- 在4种泛化场景中，HybridVLA性能下降幅度最小，证明其综合了连续动作和语义推理的优势。

## 7. 优点
- **方法创新**：首次将扩散和自回归动作生成集成在同一LLM内，而非附加独立头，充分利用VLM预训练的token级推理能力。
- **协作训练与集成机制**：序列设计有效避免范式冲突；置信度引导的集成自适应权衡两种预测，鲁棒性强。
- **性能SOTA**：仿真14%、真实19%的绝对提升，且支持单臂/双臂、多视角输入。
- **工程优化**：KV缓存、DDIM 4步采样，兼顾速度（9.4 Hz）与精度。
- **实验全面**：消融、泛化、失败分析覆盖充分，对比方法均为近两年顶级工作。

## 8. 不足与局限
- **推理速度**：全HybridVLA模式（自回归+扩散）仅为6.1 Hz，低于CogACT的9.8 Hz和π0的13.8 Hz；但提供了仅扩散的快速变体HybridVLA-dif（9.4 Hz）。
- **依赖大规模预训练**：需要760K轨迹的预训练，算力消耗大（>10K GPU小时），可能限制可复制性。
- **动作维度固定**：仅支持7-DOF（单臂）和14-DOF（双臂），未测试更复杂的高自由度操作（如灵巧手）。
- **真实世界任务量有限**：单臂与双臂各5个任务，且每个任务仅100演示，未在更大规模众包数据集上验证。
- **未开源代码和权重**：论文仅说明已发布，但未在提交时提供，可复现性暂不确定。
- **缺乏与其他统一框架的对比**：如DiVLA（同时做扩散和自回归但解耦为两个网络），实验未纳入该基线。

（完）
