---
title: "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching"
title_zh: VLA-Cache：通过自适应令牌缓存实现高效视觉-语言-动作操纵
authors: "Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, Chang Xu"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=QZYZ0Xm58q"
tags: ["query:vla"]
score: 9.0
evidence: 基于令牌缓存的视觉-语言-动作操纵
tldr: VLA模型在实时机器人控制中计算成本高。本文提出VLA-Cache，一种无需训练的推理加速方法，通过自适应缓存和重用帧间变化小的视觉令牌，利用时序连续性减少冗余计算。实验表明在不损失性能的情况下显著加速推理，使VLA模型更适用于实时场景。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 807, \"height\": 626, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1429, \"height\": 610, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1295, \"height\": 549, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1441, \"height\": 811, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1448, \"height\": 1362, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1162, \"height\": 543, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-qzyz0xm58q/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1452, \"height\": 1202, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 658, \"height\": 251, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1441, \"height\": 251, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1451, \"height\": 389, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 688, \"height\": 375, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1418, \"height\": 193, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1433, \"height\": 262, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1054, \"height\": 222, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1469, \"height\": 218, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1402, \"height\": 376, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1390, \"height\": 376, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-qzyz0xm58q/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1413, \"height\": 375, \"label\": \"Table\"}]"
motivation: VLA模型计算成本高，难以满足机器人实时控制需求。
method: 自适应缓存并重用帧间静态视觉令牌，减少冗余计算。
result: 在保持性能的同时显著加速VLA推理。
conclusion: 为VLA模型实时应用提供了有效的加速方案。
---

## Abstract
Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner. However, their substantial computational cost poses a challenge for real-time robotic control, where rapid decision-making is essential. This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. Exploiting the temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations. Additionally, to maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information. To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation. Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7× speedup in CUDA latency and a 15\% increase in control frequency, with negligible loss on task success rate. The code and videos can be found at our project page: https://vla-cache.github.io.

---

## 论文详细总结（自动生成）

# VLA-Cache: 高效视觉-语言-动作操纵的自适应令牌缓存

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：Vision-Language-Action (VLA) 模型在机器人操纵中展现了强大的多模态推理能力，能够从视觉感知和语言指令直接端到端生成动作。然而，其计算开销巨大，难以满足实时机器人控制所需的快速决策。现有加速方法（如模型轻量化、量化、早退）通常需要修改架构或重新训练，且缺乏针对 VLA 任务特性的设计，在推理速度与动作精度之间难以取得最优平衡。
- **核心问题**：VLA 任务本质上是时序连续的视觉观测流，相邻帧之间存在大量空间冗余（尤其背景区域）。反复处理这些静态且与动作决策无关的视觉令牌造成了大量计算浪费。
- **整体含义**：本文提出一种无需训练的推理加速方法 VLA-Cache，通过自适应地缓存和重用帧间几乎不变的视觉令牌的键值（Key-Value）表示，有效利用时序连续性减少冗余计算，从而在不牺牲决策质量的前提下显著加速 VLA 模型推理，使 VLA 模型更适合实时机器人控制场景。

## 2. 论文提出的方法论

### 核心思想
利用机器人操纵场景中相邻帧之间大量视觉内容（尤其是背景）几乎不变的特性，选择性地缓存和重用这些静态令牌的 KV 表示，避免每个时间步重复计算全部视觉令牌。同时，通过轻量级的注意力机制过滤掉那些虽视觉静态但语义动态的任务相关令牌（如夹爪、目标物体），确保动作精度。此外，引入层自适应令牌重用策略，根据解码器各层注意力集中程度动态调整每层的重用比例，进一步优化效率。

### 关键技术细节

1. **静态令牌选择**：
   - 将当前帧和前一帧图像划分为 N×N 个不重叠的 patch，计算对应 patch 之间的余弦相似度。
   - 保留相似度超过阈值 τ 且排名前 top-k 的 patch 作为静态令牌候选。

2. **剔除任务相关令牌**：
   - 利用解码器中文本到视觉的交叉注意力分数来衡量每个视觉令牌的任务相关性。
   - 计算平均注意力分数，设定阈值 τtask，识别出任务相关令牌。
   - 最终可重用令牌集合为静态令牌集合减去任务相关令牌集合。

3. **层自适应令牌重用**：
   - 计算每一层的注意力熵，衡量注意力集中程度。
   - 定义熵比 Rl = (E_{l-1} - E_l)/E_{l-1}，正值表示注意力更集中。
   - 累积熵比得到每一层的重用比例 αl = min(k * sum_{j=1}^{l} Rj, 1)，注意力越集中的层重用比例越高。

4. **跨帧 KV 缓存机制**：
   - 在每一时间步，对可重用令牌直接复制前一帧的 KV 缓存，对其他令牌（动态或任务相关）重新计算。
   - 该机制无需修改模型架构或重新训练，兼容标准 KV 缓存和自回归解码。

### 公式/算法流程（文字说明）
- 静态令牌选择：计算 patch 相似度 → 阈值过滤 → top-k 筛选 → 得到 Pstatic。
- 剔除任务相关令牌：计算交叉注意力 → 平均注意力分数 → 阈值筛选 → 得到 Ptask-relevant → 可重用令牌 Preuse = Pstatic \ Ptask-relevant。
- 层自适应：计算各层注意力熵 → 熵比累积 → 确定每层重用比例 αl → 在每层按比例从 Preuse 中选择实际重用的子集。
- 最终推理时，对于选中的令牌，Kt(i) = K_{t-1}(i), Vt(i) = V_{t-1}(i)；否则计算全量。

## 3. 实验设计

### 数据集/场景
- **模拟环境**：
  - **LIBERO 基准**：包含 Spatial、Object、Goal、Long 四个任务套件，每个套件含10个子任务。
  - **SIMPLER 环境**：包含 Visual Matching 和 Variant Aggregation 两种设置，在 Google 机器人臂上评估4种操纵任务（PickCan, MoveNear, Drawer, DrawerApple）。
- **真实机器人**：Kinova Jaco2 机械臂，配备前置摄像头，执行4个任务（PickPot, PlaceCube, PutSausage, WipeTable），通过遥操作收集 150-200 条轨迹/任务。

### 对比方法
- **基线**：OpenVLA、OpenVLA-OFT、CogAct（均为开源 VLA 模型）。
- **VLM 加速方法**：SparseVLM、FastV（应用于 OpenVLA）。
- **消融实验**：VLA-Cache 自身不同组件（仅静态 + 剔除任务相关 + 层自适应）。

### 评估指标
- 任务成功率（Success Rate）
- 控制频率（Control Frequency, Hz）
- FLOPs（理论计算量）
- CUDA 延迟（实际 GPU 运行时间）

## 4. 资源与算力

- 论文明确说明所有实验在 **单张 NVIDIA RTX 4090 GPU** 上完成（模拟环境）。
- 真实机器人实验也使用同一台 GPU。
- 使用 BF16 精度进行推理。
- 未明确说明训练时长（VLA-Cache 本身无需训练，但真实机器人任务中使用了 LoRA 微调 OpenVLA，微调了 50,000 步）。

## 5. 实验数量与充分性

- **模拟环境实验**：
  - LIBERO 上：对 OpenVLA 和 OpenVLA-OFT 进行完整四个套件测试（每个套件10个子任务，多个 episodes）。
  - SIMPLER 上：对 CogAct 模型进行两种设置（Visual Matching 和 Variant Aggregation）下四个任务测试。
  - 消融实验：不同 token 重用/剪枝数量（50,100,200）下与 SparseVLM、FastV 对比。
  - 消融实验：评估不同组件（静态重用、剔除任务相关、层自适应）的贡献。
  - 敏感性分析：改变静态令牌预算 k 和任务相关阈值 τ。
- **真实机器人实验**：4个任务，共100个试验（每个任务20-30次），随机初始位置和配置。
- **额外实验**：动态背景下的鲁棒性测试；注意力 vs 物体掩码作为任务相关性指标的对比。

- **充分性评析**：实验覆盖两个模拟平台和真实场景，对比了多种 SOTA 方法，进行了充分的消融和敏感性分析，结果客观公平。但未报告误差棒（由于计算开销大），不过单次试验数量足够。

## 6. 论文的主要结论与发现

- VLA-Cache 在 LIBERO 上实现 **1.63× 延迟加速**（51.91 ms → 31.83 ms），**27.31% FLOPs 减少**，成功率仅下降 0.3%（75.0% → 74.7%）。
- 在 OpenVLA-OFT 上进一步将控制频率提升约 **14 Hz**（65.10→78.98 Hz），成功率反而提升（96.8%→97.4%）。
- 在 SIMPLER 上，CogAct 模型加速约 **1.37×**，成功率保持或略有提升。
- 在真实机器人上，平均成功率从 82.1% 提升至 84.6%，在动态背景干扰下稳定性更强。
- 对比 SparseVLM 和 FastV，VLA-Cache 在保持性能的同时显著加速，而 VLM 加速方法由于破坏空间保真度或针对长序列设计，在 VLA 短动作序列任务中效果不佳。
- 层自适应策略进一步恢复性能，优于统一重用。

## 7. 优点

- **无需训练**：完全即插即用，不修改模型架构，可直接应用于现有 VLA 模型。
- **针对 VLA 特点设计**：充分利用时序冗余，不同于单帧内 token 剪枝/合并方法。
- **轻量级过滤机制**：利用解码器交叉注意力分数识别任务相关令牌，计算开销小且有效。
- **层自适应**：根据注意力熵动态调整重用比例，在效率与精度间取得更好平衡。
- **兼容性广**：适用于不同 VLA 骨干（LLaMA2）、不同动作头（直接预测、扩散策略）以及高帧率架构（OpenVLA-OFT）。
- **真实环境验证**：在真实机器人上展示了实际加速和鲁棒性提升，包括动态背景干扰场景。

## 8. 不足与局限

- **加速收益受环境动态性影响**：当场景中大量区域快速变化时，可重用静态令牌减少，加速增益降低。论文已通过动态背景实验展示了部分鲁棒性，但未量化极端动态场景的退化程度。
- **模型/架构受限**：目前仅验证了基于 LLaMA2 解码器的 VLA 模型（OpenVLA、CogAct、OpenVLA-OFT），其他架构（如 Gemma2、π0）尚未验证。
- **缺乏误差统计**：未报告多次运行的标准差或置信区间，虽然单次试验规模尚可，但统计鲁棒性信息不完整。
- **超参数敏感性**：静态令牌阈值 τ、top-k 数量、任务相关性阈值 τtask 等需手动设定，虽在附录中测试了敏感性，但未给出自动化调参方案。
- **任务类型局限**：仅测试了桌面操纵任务，未涉及复杂长序列任务或动态交互（如多物体堆叠、移动目标跟踪）。
- **未与训练式加速方法比较**：虽然方法无需训练是一大优势，但未与同等计算预算下的量化感知训练（QAIL）、动态深度控制（DeeR-VLA）等端到端优化方法直接比较性能-效率权衡。

（完）
