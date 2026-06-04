---
title: "VIP: Vision Instructed Pre-training for Robotic Manipulation"
title_zh: VIP：面向机器人操作的视觉指导预训练
authors: "Zhuoling Li, LiangLiang Ren, Jinrong Yang, Yong Zhao, Xiaoyang Wu, Zhenhua Xu, Xiang Bai, Hengshuang Zhao"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=ccUNMIbpcf"
tags: ["query:vla"]
score: 8.0
evidence: 视觉指导的机器人操作预训练
tldr: 针对机器人操作中文本指令理解困难的问题提出使用视觉指令（目标图像）来指定任务训练策略从当前观测和未来图像间预测中间动作。在多个操作基准上显著优于基于文本的方法表明视觉指令更有效且可扩展。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 859, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1604, \"height\": 596, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 850, \"height\": 291, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 859, \"height\": 911, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 853, \"height\": 371, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 846, \"height\": 329, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 859, \"height\": 629, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 856, \"height\": 273, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-ccunmibpcf/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 861, \"height\": 264, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-ccunmibpcf/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1772, \"height\": 443, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ccunmibpcf/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 858, \"height\": 296, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ccunmibpcf/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 858, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ccunmibpcf/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 856, \"height\": 335, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-ccunmibpcf/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 862, \"height\": 255, \"label\": \"Table\"}]"
motivation: 现有机器人数据难以训练策略理解文本指令视觉指令更直观。
method: 利用当前观测和未来图像作为视觉指令预测中间动作序列进行预训练。
result: 在多个操作任务上取得显著性能提升优于文本指令方法。
conclusion: 视觉指令预训练是一种有效的操作学习范式可替代文本指令。
---

## Abstract
The effectiveness of scaling up training data in robotic manipulation is still limited. A primary challenge in manipulation is the tasks are diverse, and the trained policy would be confused if the task targets are not specified clearly. Existing works primarily rely on text instruction to describe targets. However, we reveal that current robotic data cannot train policies to understand text instruction effectively, and vision is much more comprehensible. Therefore, we introduce utilizing vision instruction to specify targets. A straightforward implementation is training a policy to predict the intermediate actions linking the current observation and a future image. Nevertheless, a single future image does not describe the task target in insufficient detail. To handle this problem, we propose to use sparse point flows to provide more detailed information. Extensive tasks are designed based on real and simulated environments to evaluate the effectiveness of our vision instructed pre-training (VIP) method. The results indicate VIP improves the performance on diverse tasks significantly, and the derived policy can complete competitive tasks like ``opening the lid of a tightly sealed bottle''.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：机器人操作任务具有高度多样性，现有预训练方法主要依赖**文本指令**（如“拿起绿色方块”）来指示任务目标。但论文发现，当前机器人数据集规模不足以让策略网络有效理解文本指令（需要数百万图像-文本对才能实现跨模态对齐），导致策略无法正确聚焦目标物体（例如注意力图抓错颜色块）。
- **整体含义**：提出利用**视觉指令**（如未来图像或目标物体的裁剪区域）来替代文本指令，因为视觉指令与观察同属视觉域，无需跨模态对齐，对当前数据量下的策略网络更易于理解。这类似于教婴儿时“展示”比“讲解”更有效。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：预训练策略π，使其能够根据当前观测图像、未来目标图像以及**稀疏点流**（sparse point flows）来预测动作序列。稀疏点流描述了场景中移动区域（如机械手）的运动动态，比使用完整视频帧更高效。
- **关键技术细节**：
  - **VIP预训练框架**：输入包括当前观测图像I₁、未来图像I_T以及稀疏点流。使用共享编码器（如ResNet或DINOv2-based Transformer编码器）提取特征F₁、F_T，稀疏点流经MLP转换为特征F_p。这些特征输入动作解码器（Transformer解码器）预测T个动作a_t及不确定性σ_t。
  - **损失函数**：基于Laplacian分布的负对数似然损失：  
    \( L = \frac{1}{T} \sum_{t=1}^T \left( \frac{\sqrt{2} |a_t - \bar{a}_t|}{\sigma_t} + \log \sigma_t \right) \)  
    其中σ_t为可学习的不确定性，高不确定性对应动作歧义大，惩罚减少。
  - **稀疏点流生成**：使用CoTracker，先均匀采样点，过滤静态点，再在运动区域周围增采样，保证高效描述动作动态。
  - **渐进式掩码**：预训练过程中逐步增加稀疏点流的掩码比例α_n = min(1.25 × n/N, 1)，最终完全移除，强制策略学习从视觉观测中推理动作，同时消减预训练与推理间的信息鸿沟。
  - **推理时的视觉指令**：由于未来图像无法在线获得，采用**目标物体裁剪图像**（来自当前观测，如通过YOLOv10检测得到）作为视觉指令。该设计排除背景干扰，且支持动态指定操作顺序（如按颜色顺序清理盘子）。
- **策略网络VIRT**：全Transformer架构，编码器初始化自DINOv2，输入图像随机掩码τ=50%像素以增强对细节的敏感性；动作解码器为三个Transformer解码器，使用T个可学习查询生成动作和不确定性。

### 3. 实验设计：数据集/场景、Benchmark、对比方法

- **数据集**：
  - 预训练使用**Droid**数据集（大规模真实机器人操作数据，1.7B数据量）。
  - 微调数据：在真实环境每个任务收集100条演示；在模拟环境每个任务收集50-100条演示。
- **场景**：
  - **真实机器人**：Cobot Magic机器人（4臂，双主臂+双从臂），三台相机。三个真实任务：Pour Blueberries（多步骤）、Open the Lid（精确操作）、Clean the Table（按颜色顺序清理盘子，指令随机指定）。
  - **模拟环境**：基于Isaac Gym，Franka Panda机械臂，四台相机；人类通过Leap Motion实时遥操作采集数据。三个模拟任务：Move a Single Box（单个箱子运输）、Transport the Specified Box（从5个颜色箱子中运输指定颜色箱子）、Stack the Specified Boxes（按顺序将两个箱子堆叠）。
- **对比方法**：
  - ConvMLP（CNN+MLP显式策略）、Diffusion Policy（扩散隐式策略）、ACT（CNN+Transformer编码器解码器二段式策略）。
  - 所有方法均使用相同视觉指令（裁剪图像）进行预训练和微调，以公平比较。
- **评价指标**：每个任务测试100次，报告成功率以及推理速度（单RTX4090）。

### 4. 资源与算力

- **训练细节**：Pre-training 120K iterations，Fine-tuning 8K iterations；优化器AdamW，学习率1e-5；动作预测范围T=20，图像掩码比τ=0.5。
- **硬件**：文中未明确说明使用的GPU型号和数量，仅提及推理测试在单张RTX4090上进行。预训练阶段未披露具体算力消耗，但根据1.7B数据量和120K迭代，推测需要多GPU训练数天至数周（通常类似工作使用8×A100或类似配置）。

### 5. 实验数量与充分性

- **实验组数**：包括6个任务（3实+3模）的完整评估；对比方法4种（含基线）；消融实验3组（表3）；指令类型对比实验（表2）；数据缩放律分析（表4）；鲁棒性分析（表5）。合计至少10+组实验。
- **充分性**：
  - **客观公平**：所有对比策略使用相同视觉指令，预训练+微调流程一致；多次测试（100次）报告成功率，降低随机性。
  - **覆盖全面**：验证了指令类型、预训练有效性、各种架构、数据量影响、环境扰动鲁棒性等。
  - **不足**：真实机器人任务仅3个，且每个任务仅100条演示；模拟任务中未与更多SOTA方法（如VLA类）对比（但论文聚焦预训练范式，对比了典型策略）。

### 6. 论文的主要结论与发现

- **视觉指令远优于文本指令**：文本指令在有多物体时抓错目标，视觉指令正确聚焦目标（图1，表2）。
- **VIP预训练显著提升所有策略性能**：ConvMLP、Diffusion、ACT、VIRT在预训练后成功率均上升（表1）。
- **VIRT结合VIP达到最佳性能**：综合了Transformer大感受野、DINOv2视觉基础、不确定性学习、图像随机掩码等设计。
- **数据缩放规律**：增加预训练和微调数据量均有益；但预训练数据过少（10%）会损害性能（过拟合预训练域）。
- **鲁棒性**：对亮度变化、模糊、噪声具有一定鲁棒性，对噪声最敏感。

### 7. 优点：方法或实验设计上的亮点

- **新颖视角**：首次系统揭示文本指令在现有机器人数据下难以有效理解，提出视觉指令并验证其优势。
- **高效信息表示**：采用稀疏点流取代完整视频序列，计算开销低且能描述动作动态。
- **渐进式掩码**巧妙解决预训练与推理的信息不对称，使策略自主学习从观测中推理动作。
- **推理时用裁剪图像替代未来图像**：解决世界模型预测未来图像不准确的问题，且支持动态指定操作顺序。
- **实验设计严谨**：在真实和模拟双平台验证，对比多种基线，消融实验全面。
- **机器人遥操作数据采集**：在模拟环境中使用真实人手姿态映射，使数据更贴近真实分布（优于脚本生成的演示）。

### 8. 不足与局限

- **实验规模有限**：真实任务仅3个，每个100条演示；缺乏更复杂长时任务（如桌面整理、装配等）的验证。
- **文本指令对比不够充分**：未与大型VLA模型（如RT-2、OpenVLA）对比，这些模型可能通过大规模预训练改善文本理解。论文场景仅基于小规模微调数据。
- **稀疏点流依赖额外跟踪器**：需CoTracker离线生成，增加预处理步骤；且跟踪质量影响预训练效果。
- **裁剪图像依赖外部检测模型**：推理时需YOLOv10检测目标，引入依赖和潜在错误传播。
- **未公开算力细节**：预训练具体GPU型号、数量、耗时未给出，影响可复现性。
- **鲁棒性测试不够深入**：仅测试了三种扰动（亮度、噪声、模糊），未考虑光照方向变化、遮挡、目标变形等。
- **遗憾**：未讨论视觉指令在跨机器人迁移或开放世界中的泛化能力。

（完）
