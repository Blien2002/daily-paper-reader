---
title: Exploring the Limits of Vision-Language-Action Manipulation in Cross-task Generalization
title_zh: 探索VLA操作模型在跨任务泛化中的极限
authors: "Jiaming Zhou, Ke Ye, Jiayi LIU, Teli Ma, Zifan Wang, Ronghe Qiu, Kun-Yu Lin, Zhilin Zhao, Junwei Liang"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=h6xQClTm4W"
tags: ["query:vla"]
score: 9.0
evidence: 通过新基准评估VLA操作模型的跨任务泛化能力
tldr: VLA模型的跨任务泛化能力对通用操作至关重要，但缺乏系统评估。本文提出AGNOSTOS基准，包含23个未见操作任务和两种难度级别，系统评测发现现有VLA模型泛化能力严重不足，为未来机器人基础模型研究提供了重要参考和测试平台。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1431, \"height\": 1132, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1430, \"height\": 1144, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1449, \"height\": 299, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 649, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1450, \"height\": 1321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1446, \"height\": 356, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1445, \"height\": 464, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1382, \"height\": 1210, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1440, \"height\": 993, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-h6xqcltm4w/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1163, \"height\": 527, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1459, \"height\": 423, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1438, \"height\": 1467, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 766, \"height\": 124, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 766, \"height\": 220, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1411, \"height\": 1097, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1042, \"height\": 267, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1272, \"height\": 225, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1150, \"height\": 344, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-h6xqcltm4w/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 864, \"height\": 197, \"label\": \"Table\"}]"
motivation: 现有VLA模型的跨任务零样本泛化能力缺乏系统评估。
method: 构建包含23个新任务的AGNOSTOS基准，并设计两种泛化难度级别。
result: 现有VLA模型在跨任务泛化上表现不佳，揭示了显著缺陷。
conclusion: 跨任务泛化是VLA模型实现通用机器人的关键瓶颈，需要进一步研究。
---

## Abstract
The generalization capabilities of vision-language-action (VLA) models to unseen tasks are crucial to achieving general-purpose robotic manipulation in open-world settings.
However, the cross-task generalization capabilities of existing VLA models remain significantly underexplored.
To address this gap, we introduce **AGNOSTOS**, a novel simulation benchmark designed to rigorously evaluate cross-task zero-shot generalization in manipulation. 
AGNOSTOS comprises 23 unseen manipulation tasks for test—distinct from common training task distributions—and incorporates two levels of generalization difficulty to assess robustness. 
Our systematic evaluation reveals that current VLA models, despite being trained on diverse datasets, struggle to generalize effectively to these unseen tasks. 
To overcome this limitation, we propose **Cross-Task In-Context Manipulation (X-ICM)**, 
a method that conditions large language models (LLMs) on in-context demonstrations from seen tasks to predict action sequences for unseen tasks.
Additionally, we introduce a **dynamics-guided sample selection** strategy that identifies relevant demonstrations by capturing cross-task dynamics. 
On AGNOSTOS, X-ICM significantly improves cross-task zero-shot generalization performance over leading VLAs, achieving improvements of 6.0\% over $\pi_0$ and 7.9\% over VoxPoser.
We believe AGNOSTOS and X-ICM will serve as valuable tools for advancing general-purpose robotic manipulation.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：视觉-语言-动作（VLA）模型在已知任务内的视觉变化泛化（within-task generalization）上取得了显著进展，但跨任务泛化（cross-task generalization）——即零样本应对从未见过的物体组合、目标和动作——对于实现开放世界的通用机器人操作至关重要。目前缺乏针对VLA模型零样本跨任务泛化能力的系统性评估。
- **核心问题**：现有VLA模型在面对全新任务时能否有效泛化？其极限在哪里？
- **背景与贡献**：作者首先提出了一个新基准 AGNOSTOS，包含23个与常用训练任务语义不同的未见测试任务，并划分两种难度级别；然后对三大类VLA模型（Foundation VLA、Human-video VLA、In-domain VLA）进行了全面评估，发现它们普遍难以泛化到未见任务；最后提出了X-ICM方法，利用LLM的上下文学习能力和动力学引导的样本选择策略，显著提升了跨任务零样本泛化性能。

---

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：利用大型语言模型（LLM）的上下文学习（in-context learning）能力，从已见任务中选取相关演示作为提示，引导LLM为未见任务预测动作序列。
- **关键技术细节**：
    1. **动力学引导的样本选择（Dynamics-guided Sample Selection）**：
        - 训练一个动力学扩散模型 G，以初始视觉观察 \(v_{si,1}\) 和语言描述 \(L_{si}\) 为输入，预测最终观察 \(v_{si,T}\)（即任务完成时的场景）。
        - 训练损失：\(\min_G \mathbb{E}_{i,z,\epsilon} \left[ \| \epsilon - \epsilon_G(v_{si,T,z}, z, v_{si,1}, L_{si}) \|^2 \right]\)。
        - 训练后，用 G 提取特征 \(f_{si} = [f_{s,vis}^i, f_{s,lang}^i]\)，并按余弦相似度选出与未见任务最相关的 K 个已见演示。
    2. **跨任务上下文预测（Cross-task In-context Prediction）**：
        - 对选出的 K 个演示，提取物体3D中心位置和关键动作序列，并文本化为“[指令, {物体:坐标}] → [动作序列]”格式。
        - 将所有文本化演示按相似度降序拼接，加上系统提示和未见任务的文本化输入，形成LLM输入。LLM输出未见任务的关键动作序列。
- **算法流程**（文字说明）：
    1. 使用动力学扩散模型对每个已见演示提取动态特征。
    2. 对于每个未见任务，计算其动态特征与所有已见演示特征的余弦相似度，选择 top-K 演示。
    3. 将这些演示文本化，构建上下文提示。
    4. 输入LLM（如Qwen2.5-7B/72B），得到预测的关键动作序列，再通过插值等方式生成完整动作序列。

---

### 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **Benchmark（AGNOSTOS）**：
    - 基于 RLBench 模拟环境。
    - 训练集：18个常用已见任务，每个任务200条演示，共3600条。
    - 测试集：23个未见任务，分为 Level-1（13个，与已见任务在物体或动作上有部分语义相似）和 Level-2（10个，完全新颖，无重叠物体或动作）。
    - 每个任务测试3次不同种子，每次25次 rollout，报告成功率的均值和标准差。
- **对比方法**：
    - **In-domain VLA**：PerAct, RVT, RVT2, Sigma-Agent, Instant Policy。
    - **Human-video VLA**：R3M, D4R, R3M-Align, D4R-Align。
    - **Foundation VLA**：OpenVLA, RDT, π0, LLARVA, SAM2Act, 3D-LOTUS++, VoxPoser。
    - 所有方法均在已见任务上微调后进行零样本跨任务测试。X-ICM使用Qwen2.5-7B-Instruct和72B-Instruct。

---

### 4. 资源与算力

- 文中明确提及：
    - X-ICM使用Qwen2.5-7B-Instruct和72B-Instruct，部署在2或8块A6000 GPU上。
    - 微调OpenVLA使用LoRA，rank=32，学习率5e-4，训练2000步（收敛），使用batch size=16。
    - RDT微调400,000步，batch size=16，使用了front和wrist RGB图像。
    - π0微调100,000步，batch size=64，使用LoRA，使用front、wrist、overhead RGB图像。
- 未详细说明动力学扩散模型的训练时长、总GPU小时数等，但提供了训练损失曲线表明收敛。

---

### 5. 实验数量与充分性

- **实验数量**：
    - 主实验（Table 2）：在23个未见任务上对比了10余种基线方法，每个任务3次种子×25 rollout，共约23×3×25×（方法数）≈大量rollout。
    - 消融实验（Table 3、4，Figure 3）：
        - 动力学引导选择 vs 随机选择（Table 3）。
        - 不同LLM backbone（Qwen2.5, Deepseek-R1-Distill, Llama3, Ministral, InternLM3）。
        - 不同上下文演示数量（1~24，Figure 3）。
        - 不同模型规模（7B、14B、72B，Table A5）。
        - 不同动态特征组合（Table A4）。
    - 真实机器人实验：5个任务，每个20次 rollout，零样本跨任务测试。
    - 长时域任务实验：1个任务（clean the table）含3个子任务，20次 rollout。
- **充分性和公平性**：
    - 覆盖了三大类主流VLA方法，公平对比均基于官方微调流程。
    - 消融实验系统，验证了各个模块的贡献。
    - 真实实验验证了仿真结果的可迁移性。
    - 存在一定偏差：真实场景仅使用xArm7机器人，未涵盖多种机器人类型；部分方法因训练任务重叠而被标记为N/A（如3D-LOTUS++的Level-1任务中几个被移除）；评价指标仅用成功率，未考虑任务难度差异。

---

### 6. 论文的主要结论与发现

- 现有VLA模型在零样本跨任务泛化上普遍表现差，没有任何模型在所有23个未见任务上成功率为正数，且多数模型在至少8个任务上完全失败（成功率0%）。
- X-ICM方法显著优于所有基线：X-ICM (72B) 在Level-1上平均37.6%（第二好π0为21.7%），Level-2上20.3%（第二好SAM2Act为15.9%），总体30.1%（第二好π0为17.5%）。X-ICM (72B) 在所有23个任务上均有非零成功率，而所有基线均存在至少8个零成功任务。
- 动力学引导的样本选择是关键：相比随机选择，大幅提升性能和稳定性（All 30.1% vs 25.2%）。
- 上下文演示数量存在最优区间（12个左右），过多可能引入噪声。
- 不同LLM backbone性能差异大，选择能力强的LLM重要。

---

### 7. 优点

- **基准创新**：首次系统定义和评估VLA模型的零样本跨任务泛化，并设计两个难度级别，细粒度揭示泛化瓶颈。
- **方法简洁有效**：X-ICM不修改模型参数，仅通过上下文提示和动力学引导选择快速提升泛化能力，易于部署。
- **实验全面**：覆盖三大类VLA方法（含近年SOTA），做了丰富的消融和真实验证，结果可信。
- **代码开源承诺**：提供项目页面和代码，便于复现。

---

### 8. 不足与局限

- **性能仍有限**：X-ICM在Level-2任务平均仅20.3%，尤其在处理全新物体和动作的任务上（如scoop、basketball）成功率仍低（低于10%）。LLM的预训练知识和上下文长度限制了外推能力。
- **视觉信息利用不足**：仅将物体位置文本化，忽略了丰富的视觉上下文（如物体颜色、纹理、场景布局等），可能遗漏重要线索。
- **依赖外部感知模型**：物体检测（GroundingDINO）和深度/相机信息在真实场景中可能噪声大，影响泛化。
- **评估范围局限**：仿真环境RLBench场景相对简单；真实实验仅5个任务、单个机器人平台，未验证跨实施例泛化。
- **计算开销**：大模型推理（72B）需要多GPU，实时性受限；动力学扩散模型训练和推理也增加了附加成本。
- **长时域任务零样本泛化极差**：在long-horizon任务上仅5%成功率，远不够实用。

---

（完）
