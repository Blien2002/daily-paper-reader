---
title: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models"
title_zh: EfficientVLA：视觉-语言-动作模型的无训练加速与压缩
authors: "Yantai Yang, Yuhao Wang, Zichen Wen, Luo Zhongwei, Chang Zou, Zhipeng Zhang, Chuan Wen, Linfeng Zhang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=SELYlDHZk2"
tags: ["query:vla"]
score: 9.0
evidence: 对视觉-语言-动作模型的无训练加速与压缩
tldr: 视觉-语言-动作模型在具身智能中潜力巨大，但高计算和内存需求限制了部署。本文提出EfficientVLA，一个结构化、无需训练的推理加速框架，通过协同利用多重冗余（如时间、空间、通道冗余）系统消除瓶颈。该方法无需微调即可显著降低推理开销，在保持性能的同时实现数倍加速，为VLA模型的实际应用铺平道路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-selyldhzk2/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1439, \"height\": 625, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-selyldhzk2/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1396, \"height\": 540, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-selyldhzk2/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1323, \"height\": 268, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-selyldhzk2/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1412, \"height\": 353, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1433, \"height\": 550, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1434, \"height\": 354, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 714, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1233, \"height\": 472, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 712, \"height\": 157, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1438, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-selyldhzk2/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1436, \"height\": 349, \"label\": \"Table\"}]"
motivation: 现有VLA模型计算和内存需求过高，阻碍其实时部署，且现有加速方案未能全面解决整个流水线的瓶颈。
method: 提出EfficientVLA，利用时间、空间和通道多重冗余，以结构化方式实现无训练推理加速。
result: 在多种VLA模型上实现数倍加速且性能几乎无损，证明了方法的普适性和有效性。
conclusion: EfficientVLA为VLA模型的高效部署提供了即插即用解决方案，推动了具身智能的实际应用。
---

## Abstract
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability.  We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features.
We apply our method to a standard VLA model CogACT, yielding a $1.93\times$ inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

---

## 论文详细总结（自动生成）

# EfficientVLA：视觉-语言-动作模型的无训练加速与压缩 —— 论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **问题**：扩散式视觉-语言-动作（VLA）模型在具身智能中展现出巨大潜力，但其推理时计算和内存开销极高，严重制约了在资源受限机器人平台上的实时部署。现有加速方法往往只针对单一模块（如仅剪枝视觉token或仅缓存静态token），未能系统性地解决整个VLA流水线中的计算和内存瓶颈，导致整体加速效果有限。
- **动机**：通过对标准VLA模型（CogACT）的模块级分析，发现语言模块（LLM）和迭代扩散动作头是主要的延迟和计算瓶颈；视觉token剪枝在计算受限场景下有效，但很快受限于LLM的内存带宽；LLM层间存在深度冗余，扩散步间存在时间冗余。因此需要一种结构化、全局优化的加速框架。

## 2. 方法论：核心思想、关键技术细节

### 2.1 整体框架
EfficientVLA是一种**无需训练**（training-free）的结构化推理加速框架，协同整合三项策略：

1. **语言模块层剪枝**：基于层间冗余分析，移除功能无关层。
2. **视觉token剪枝**：任务感知式选择，平衡任务关键性与信息多样性。
3. **扩散动作头特征缓存**：利用时间冗余，缓存中间注意力/MLP特征。

### 2.2 语言模块层剪枝
- **冗余分析**：计算每层输入与输出的余弦相似度，相似度越高表示该层变换效果越小，冗余度越高。
- **重要性分数**：\( I(\ell) = 1 - \frac{1}{|D|}\sum_{i}\frac{1}{L}\sum_{j}\frac{x_{i,j}^{(\ell)}\cdot x_{i,j}^{(\ell+1)}}{\|x_{i,j}^{(\ell)}\|_2\|x_{i,j}^{(\ell+1)}\|_2} \)，分数越低代表该层越冗余。
- **剪枝策略**：将所有层按重要性排序，保留分数最高的前N'层，直接移除其余层（非连续剪枝）。

### 2.3 视觉token剪枝
- **任务相关性量化**：利用VLM交叉注意力分数，对每个视觉token计算其与语言指令token的注意力均值，归一化得到相关性分数\( s_i \)。
- **第一阶段：选取关键token**：保留相关性最高的\( K_{\text{key}} \)个token（经验值4-8个）。
- **第二阶段：平衡任务性与多样性**：剩余token池中，按比例\(\alpha\)选取：一部分按相关性继续选取（任务驱动）；另一部分按与已选token的最大余弦距离选取（多样性驱动）。最终保留\( K_{\text{final}} \)个token。

### 2.4 扩散动作头特征缓存
- **观察**：相邻去噪步中自注意力和MLP输出高度相似（时间冗余）。
- **方法**：采用固定间隔N的静态缓存。仅在步数\(t \mod N = 0\)时重算并更新缓存；其余步直接读取缓存中的注意力/MLP输出，跳过计算。N可取1~5等，平衡加速与精度。

## 3. 实验设计

### 3.1 数据集与场景
- **主基准**：SIMPLER环境（仿真桌面操作），用于Google Robot，支持两种设置：
  - **Visual Matching**：高度模拟真实外观。
  - **Variant Aggregation**：加入光照、背景、纹理等变化。
- **任务**：4个——Pick Coke Can、Move Near、Open/Close Drawer、Open Top Drawer and Place Apple。
- **额外泛化实验**：LIBERO基准（4个任务套件：Spatial, Object, Goal, 10）。

### 3.2 对比方法
- **CogACT**（基线VLA模型）
- **Random Dropping**：随机保留112个视觉token
- **FastV**：基于注意力分数的视觉token剪枝
- **VLA-Cache**：基于帧间缓存的加速方法
- **EfficientVLA**的多种配置（保留22/28层，56/112 token）

### 3.3 消融与扩展
- 对每个模块（层剪枝、MLP压缩、视觉token剪枝、动作头缓存）进行消融实验。
- 评估不同token保留比例（56/72/96/112/256）和不同缓存间隔（1~5）。
- 在CogACT Small/Base/Large三种规模上测试可扩展性。
- 在π0模型+LIBERO上测试泛化性。
- 在LLaVA-1.5-7B上测试视觉语言任务（GQA, MMB, MME等）。

## 4. 资源与算力

- **GPU**：所有实验在NVIDIA A40 GPU上运行。
- **推理时间**报告为平均单步推理时长。
- **训练**：该方法无需训练（training-free），因此未涉及训练时长或算力。文中未明确说明预训练模型本身的训练资源。

## 5. 实验数量与充分性

- **数量**：主实验包含SIMPLER上8种配置（不同层数+token数）的结果，外加消融实验（7组）、token/缓存间隔影响（各5组）、可扩展性（3种模型大小）、泛化实验（LIBERO+π0，4任务）、视觉语言任务（8个基准）。
- **充分性**：实验设计较为全面，涵盖不同模块组合、超参数扫描、多模型规模和跨任务泛化。与现有方法（FastV, VLA-Cache, Random Dropping）公平对比，使用相同环境与评估指标。消融实验清晰展示了每项技术的贡献。
- **客观性**：报告了平均成功率、FLOPs、推理时间，并指出随机剪枝导致严重性能下降（20.9%），突显方法优势。对性能波动（如某些任务下成功率反而提升）亦有解释。

## 6. 主要结论与发现

- EfficientVLA在CogACT+SIMPLER上实现**1.93倍推理加速**，FLOPs降至原始模型的**28.9%**，平均成功率仅下降**0.6%**（从74.8%到74.2%）。
- 单独优化视觉token（如VLA-Cache）仅获得1.38倍加速，因未解决LLM内存瓶颈；结构化框架是必要且有效的。
- 层剪枝+视觉token剪枝+动作头缓存三者协同效果远优于单一模块优化。
- 该方法在更大模型（CogACT-Large）上获得更显著加速（2.0倍），且性能损失仅0.6%。
- 在π0+LIBERO上取得1.71倍加速，在LLaVA-1.5-7B上视觉语言任务平均准确率保持96.6%（128 token下），验证了跨模型和任务的泛化能力。

## 7. 优点

1. **完全无需训练**：即插即用，无缝应用于预训练VLA模型，降低部署成本。
2. **结构化系统性**：同时优化视觉、语言、动作三大模块，而非孤立优化，克服了单一方法的内存/计算瓶颈。
3. **任务感知+多样性平衡**：视觉token剪枝兼顾关键任务信息与全局覆盖，优于纯注意力剪枝（FastV）或随机丢弃。
4. **简单高效**：所有策略仅基于推理时的统计量（余弦相似度、注意力分数），计算开销极小。
5. **可扩展性强**：在不同模型大小、不同VLA架构（Diffusion-based, Flow-based）上均表现良好。

## 8. 不足与局限

1. **固定缓存间隔**：动作头缓存采用静态N，未实现自适应调整，可能在某些去噪步动态变化大的场景下引入误差。
2. **仅验证了有限开源模型**：目前主要实证在CogACT和π0上，更多Diffusion-based VLA模型（如OpenVLA, RT-2等）尚未验证。参数设置（如Kkey=4, α=50%）可能需针对新模型调整。
3. **无训练方法的上限**：训练感知方法（如知识蒸馏、结构重参）理论上可获得更优压缩比，本文未与之进行公平对比（但作者指出是设计选择而非缺陷）。
4. **未报告误差棒**：各实验结果仅为单次运行，未提供多次重复的统计显著性。
5. **应用局限**：该方法针对扩散式VLA设计，不直接适用于自回归式动作解码或其他架构的VLA模型。
6. **潜在偏差风险**：SIMPLER仿真环境虽努力对齐真实场景，但仍有sim-to-real gap；实际部署效果有待真实机器人实验验证。

（完）
