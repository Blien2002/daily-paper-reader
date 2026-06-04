---
title: "DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation"
title_zh: DynaRend：通过掩码未来渲染学习3D动态以辅助机器人操纵
authors: "Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, lijiayi, Gang Hua"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=r4dzaP61QH"
tags: ["query:vla"]
score: 7.0
evidence: 通过三维动态预测学习机器人操纵表征
tldr: 机器人操纵策略泛化受限于真实数据匮乏，现有自监督方法未能联合学习几何、语义和动态。本文提出DynaRend，一种表征学习框架，通过掩码重建和未来预测学习三维感知且动态知情的三平面特征。该特征同时编码几何、语义和动态信息，有效提升下游操纵策略的性能和泛化性，在多种任务上超越现有预训练方法。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1398, \"height\": 457, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1423, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 659, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 561, \"height\": 343, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 881, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 880, \"height\": 449, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1383, \"height\": 1330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1391, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1391, \"height\": 1333, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-r4dzap61qh/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1385, \"height\": 488, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1446, \"height\": 531, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 724, \"height\": 430, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 653, \"height\": 340, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 896, \"height\": 476, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 574, \"height\": 725, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1439, \"height\": 590, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1440, \"height\": 244, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1447, \"height\": 612, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1439, \"height\": 652, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 585, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-r4dzap61qh/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1443, \"height\": 1977, \"label\": \"Table\"}]"
motivation: 现有自监督表征学习未能联合捕获操纵所需的几何、语义和动力学信息。
method: 提出通过掩码重建和未来预测学习三维感知的三平面特征，融合几何、语义和动态。
result: 在多个模拟和真实操纵任务中，DynaRend学习到的特征显著提升了策略成功率和泛化性。
conclusion: DynaRend为机器人操纵提供了一种有效的自监督表征学习方法。
---

## Abstract
Learning generalizable robotic manipulation policies remains a key challenge due to the scarcity of diverse real-world training data. While recent approaches have attempted to mitigate this through self-supervised representation learning, most either rely on 2D vision pretraining paradigms such as masked image modeling, which primarily focus on static semantics or scene geometry, or utilize large-scale video prediction models that emphasize 2D dynamics, thus failing to jointly learn the geometry, semantics, and dynamics required for effective manipulation. In this paper, we present DynaRend, a representation learning framework that learns 3D-aware and dynamics-informed triplane features via masked reconstruction and future prediction using differentiable volumetric rendering. By pretraining on multi-view RGB-D video data, DynaRend jointly captures spatial geometry, future dynamics, and task semantics in a unified triplane representation. The learned representations can be effectively transferred to downstream robotic manipulation tasks via action value map prediction. We evaluate DynaRend on two challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic experiments, demonstrating substantial improvements in policy success rate, generalization to environmental perturbations, and real-world applicability across diverse manipulation tasks.

---

## 论文详细总结（自动生成）

# 论文结构化总结：DynaRend

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：机器人操作策略的泛化能力受限于真实世界多样化训练数据的稀缺。现有自监督表征学习方法存在局限：2D视觉预训练（如掩码图像建模）主要关注静态语义或场景几何，而大规模视频预测模型强调2D动态，无法联合学习操作所需的几何、语义和动力学信息。
- **整体含义**：本文提出 **DynaRend**，一种表征学习框架，通过掩码重建和未来预测，结合可微分体渲染，学习**3D感知且动力学知情**的三平面特征，同时捕获空间几何、未来动态和任务语义，提升下游操作策略的成功率和泛化性。

## 2. 论文提出的方法论

- **核心思想**：利用多视角RGB-D视频数据进行自监督预训练，通过**重建当前场景**和**预测未来关键帧**两个互补目标，学习统一的3D三平面表征，并使用体渲染将特征解码为RGB、深度和语义图进行监督。
- **关键技术细节**：
    1. **三平面构建**：从多视角RGB-D图像重建点云，通过MLP提取逐点特征，经轴对齐最大池化投影到三个正交平面（xy, xz, yz），得到特征体积 V = {f_xy, f_xz, f_yz}。
    2. **掩码未来预测**：随机掩码部分三平面特征，替换为可学习的掩码嵌入，输入语言指令（CLIP编码）后，依次通过**重建网络** E_recon 和**预测网络** E_pred，分别输出当前场景和未来关键帧的三平面特征。
    3. **体渲染**：对每个三平面特征独立进行可微分体渲染，沿光线采样点，插值三平面特征，经MLP头部预测密度、RGB和语义特征，最后积分得到渲染结果。使用RGB、语义（来自RADIOv2.5）和深度（SiLog损失）进行监督。
    4. **目标视图增强**：利用预训练的多视图扩散模型See3D合成新视角作为监督，减少对密集摄像头设置的依赖，增强真实世界适用性。
    5. **下游任务适配**：以RVT风格预测动作热图，训练动作解码器（卷积+上采样预测平移热图，MLP预测旋转和夹爪状态）。
- **公式或算法流程**（文字说明）：
    - 输入多视角RGB-D → 点云 → 三平面特征 → 掩码 → 重建网络E_recon → 当前特征V_now → 预测网络E_pred → 未来特征V_future。
    - 对V_now和V_future分别渲染，计算重建损失L_recon和预测损失L_pred（包含RGB、语义、深度项），总损失L_pretrain = λ_recon L_recon + λ_pred L_pred。
    - 微调阶段：取消掩码，提取特征，预测动作热图，损失为交叉熵（平移、旋转、夹爪）。

## 3. 实验设计

- **数据集/场景**：
    - **模拟环境**：RLBench（18任务子集和71任务全集）、Colosseum（20任务，12种环境扰动：物体颜色/纹理/大小、背景/光照/摄像机位姿等）。
    - **真实世界**：5个操作任务（Put Item in Drawer, Close Pot, Stack Blocks, Sort Shape, Stack Cups），每个任务30个专家演示，测试时引入干扰物。
- **Benchmark**：RLBench是标准机器人操作基准；Colosseum专门评估泛化性（域迁移）。
- **对比方法**：
    - 模拟：PerAct, RVT, 3D-MVP, 3D Diffuser Actor, RVT-2, SPA, VC-1, MVP, MoCov3, MAE, DINOv2, CLIP等。
    - 真实世界：3D Diffuser Actor (3DA), RVT, RVT-2。

## 4. 资源与算力

- **文中明确说明**：预训练约60k步，微调约30k步；批量大小256；初始学习率1e-4，余弦衰减；使用**8块NVIDIA RTX 3090 GPU**。具体训练总时长未给出，但可推断为GPU小时内级别。

## 5. 实验数量与充分性

- **实验数量**：大量且全面。
    - RLBench-18任务（平均成功率+标准差，5种种子）、RLBench-71任务（两组35/36任务）。
    - Colosseum：20任务×12扰动类别，详细报告每个类别成功率。
    - 真实世界：5任务×20回合，有/无干扰物两种设置。
    - 消融实验：6组（无预训练、仅重建、仅预测、缺失RGB/语义/深度损失、不同掩码比例、无目标视图增强）。
    - 额外对比：在域内预训练（RLBench-18数据）与其他预训练方法对比。
- **充分性评估**：实验设计较为充分，覆盖多种任务、扰动、预训练策略对比，消融验证各组件贡献。结果报告标准偏差，具有统计意义。对比基线丰富（包括2D和3D预训练方法），公平性较好（统一架构RVT-2）。

## 6. 论文的主要结论与发现

- DynaRend在RLBench-18上平均成功率83.2%，显著优于RVT-2（81.4%）和3D Diffuser Actor（81.3%）；在RLBench-71上平均76.6%，超过SPA（70.8%）等。
- 在Colosseum上，DynaRend几乎所有扰动下表现最佳，尤其对纹理变化稳健。
- 真实世界5任务平均成功率57%（无干扰）和45%（有干扰），远超RVT-2（37%/16%）。
- 消融实验表明：预训练带来+6.5%提升；未来预测比重建贡献更大；两者结合最佳；RGB和语义损失关键；掩码比例0.2~0.6最优；目标视图增强带来+3.4%提升。

## 7. 优点

- **方法创新**：首次将**掩码重建+未来预测**与**可微分体渲染**结合，统一学习3D几何、未来动态和语义，三平面表示高效且可扩展。
- **技术亮点**：
    - 目标视图增强：利用预训练扩散模型合成新视角，摆脱对多摄像头的依赖，提升真实世界实用性。
    - 损失设计：融合RGB、语义（从视觉基础模型蒸馏）、深度三重监督，使特征语义和几何丰富。
    - 动作解码：基于热图的预测，高效且可微。
- **实验充分**：跨模拟-真实、多任务、多扰动、多消融，结果有说服力。
- **可落地性**：真实世界仅用两个摄像头和少量演示，仍能取得显著提升，展示良好迁移能力。

## 8. 不足与局限

- **依赖运动规划器**：论文自身指出，仍需要外部低层运动规划器将预测的关键帧动作转换为可执行轨迹，未实现完全端到端。
- **预训练数据规模有限**：预训练仅使用任务相关的多视角RGB-D视频，未探索大规模互联网数据预训练，可能限制通用性。
- **真实世界实验规模较小**：仅5个任务，每个任务30个演示，测试20回合，样本量和任务多样性有限，可能存在偏差。
- **计算开销**：体渲染和扩散模型生成新视角可能带来额外计算成本，文中未详细分析推理效率（但提及推理速度与RVT相当）。
- **泛化边界**：Colosseum扰动类型虽多，但均为合成扰动；真实世界干扰物仅测试少量，对更复杂环境（如光照巨变、遮挡）的鲁棒性待验证。

（完）
