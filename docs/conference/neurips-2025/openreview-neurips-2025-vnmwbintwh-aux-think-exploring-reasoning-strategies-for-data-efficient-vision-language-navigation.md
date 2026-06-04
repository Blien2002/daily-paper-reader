---
title: "Aux-Think: Exploring Reasoning Strategies for Data-Efficient Vision-Language Navigation"
title_zh: Aux-Think：面向数据高效视觉语言导航的推理策略探索
authors: "Shuo Wang, Yongcai Wang, Wanting Li, Xudong Cai, Yucheng Wang, Maiyue Chen, kaihui.wang, Zhizhong Su, Deying Li, Zhaoxin Fan"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=vNmWbINtwH"
tags: ["query:vla"]
score: 6.0
evidence: 探索视觉语言导航中的推理策略，属于具身AI中的VLA任务
tldr: 现有视觉语言导航方法多直接预测动作，缺乏对推理策略的系统研究。本文首次评估了No-Think、Pre-Think等多种推理策略在导航任务中的效果，发现预先推理能够显著提升数据效率和任务成功率，为VLA导航提供了新的方法思路。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 557, \"height\": 460, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 577, \"height\": 463, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1427, \"height\": 885, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1397, \"height\": 710, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1364, \"height\": 652, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 594, \"height\": 442, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1286, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vnmwbintwh/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1297, \"height\": 394, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1311, \"height\": 658, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1312, \"height\": 487, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 905, \"height\": 232, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 672, \"height\": 338, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 626, \"height\": 292, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1171, \"height\": 431, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vnmwbintwh/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1045, \"height\": 410, \"label\": \"Table\"}]"
motivation: 现有视觉语言导航方法缺乏对推理策略的探索，限制了导航效率。
method: 系统比较No-Think、Pre-Think等推理策略在导航任务中的表现。
result: 预推理策略在数据效率和任务成功率上均优于直接动作预测。
conclusion: 推理策略是提升VLA导航性能的关键因素。
---

## Abstract
Vision-Language Navigation is a critical task for developing embodied agents that can follow natural language instructions to navigate in complex real-world environments.  Recent advances by finetuning large pretrained models have significantly improved generalization and instruction grounding compared to traditional approaches. However, the role of reasoning strategies in navigation—an action-centric, long-horizon task—remains underexplored, despite Chain-of-Thought reasoning's demonstrated success in static tasks like question answering and visual reasoning. To address this gap, we conduct the first systematic evaluation of reasoning strategies for VLN, including No-Think (direct action prediction), Pre-Think (reason before action), and Post-Think (reason after action). Surprisingly, our findings reveal the Inference-time Reasoning Collaps issue, where inference-time reasoning degrades navigation accuracy, highlighting the challenges of integrating reasoning into VLN. Based on this insight, we propose Aux-Think, a framework that trains models to internalize structured reasoning patterns through CoT supervision during training, while preserving No-Think inference for efficient action prediction. To support this framework, we release R2R-CoT-320k, a large-scale Chain-of-Thought annotated dataset.  Empirically, Aux-Think significantly reduces training effort without compromising performance.

---

## 论文详细总结（自动生成）

好的，以下是根据您提供的论文内容生成的中文总结。

---

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：视觉-语言导航任务要求具身智能体根据自然语言指令在复杂环境中导航。尽管链式思维推理在问答等静态任务中取得了成功，但在动作导向、长程规划的导航任务中，推理策略的作用尚未被系统研究。
- **研究动机**：现有VLN方法多直接预测动作，缺乏对推理策略的探索。本文旨在填补这一空白，首次系统比较不同推理策略对导航性能的影响，并解决测试时推理带来的问题。
- **整体含义**：提出了一种新的推理范式——Aux-Think，利用链式思维推理作为训练时的辅助监督信号，在测试时则直接预测动作，从而兼顾推理的知识引导和测试效率。该工作为VLN中的推理建模提供了新视角，并释放了首个大规模VLN链式思维数据集。

---

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将链式思维推理与导航动作解耦——训练时模型通过辅助任务学习推理模式，测试时隐式利用推理知识直接预测动作，避免显式推理带来的错误累积和延迟。
- **关键技术细节**：
    1. **推理策略系统比较**：对比三种主流策略：
        - **No-Think**: 直接预测动作，无显式推理。
        - **Pre-Think**: 先生成推理链，再基于推理预测动作。
        - **Post-Think**: 先预测动作，再生成推理链解释动作。
    2. **Aux-Think框架**：
        - **训练阶段**：联合训练三个任务：
            - **主任务——滚动时域动作规划**：基于当前和历史观测、指令，预测未来n步动作。
            - **辅助任务1——基于CoT的推理**：生成当前步骤的推理轨迹（使用R2R-CoT-320k数据集）。
            - **辅助任务2——基于指令的推理**：根据观测序列重建指令文本。
        - **损失函数**：三个任务的损失之和。
        - **测试阶段**：仅激活动作预测部分，不生成显式推理，快速执行一步动作。
    3. **R2R-CoT-320k数据集**：利用Qwen-2.5-VL-72B为R2R-CE基准的每一步生成详细推理注释，包含32万条推理轨迹。
- **算法流程**：通过切换提示（prompt）实现多任务学习，训练时同时优化三个损失；测试时使用动作预测提示，模型输出下一个动作。

---

### 3. 实验设计

- **数据集与场景**：
    - **R2R-CE**：在连续环境下的Room-to-Room导航基准。
    - **RxR-CE**：跨语言、更自然指令和更长轨迹的导航基准。
- **基准（Benchmark）**：标准VLN-CE设置，包括：
    - **指标**：成功率、Oracle成功率、成功率加权路径长度、导航误差。
- **对比方法**：
    - 传统方法：BEVBert、ETPNav、Seq2Seq、CMA等。
    - 基于大模型的方法：NaVid、Uni-NaVid、NaVILA（均为近两年SOTA）。
    - 推理策略消融：No-Think、Pre-Think、Post-Think。

---

### 4. 资源与算力

- **训练配置**：使用8块NVIDIA H20 GPU，训练1个epoch（约60小时）。
- **基础模型**：NVILA-lite 8B（包含SigLIP视觉编码器+Qwen2 LLM），从NVILA-lite第二阶段开始监督微调。
- **数据规模**：训练时除R2R-CE训练集外，额外使用了R2R-CoT-320k推理数据集（无额外大规模数据）；在最终对比中，Aux-Think还可扩展使用RxR训练集、DAgger数据和网络数据。

---

### 5. 实验数量与充分性

- **实验数量**：
    - **主对比实验**：在R2R-CE和RxR-CE val-unseen上的完整方法对比。
    - **推理策略对比**：No-Think、Pre-Think、Post-Think与Aux-Think的直接比较。
    - **消融实验**：
        - 不同辅助任务（CoT推理、指令推理、滚动规划）的贡献。
        - 滚动规划中预测步数（1-5步）的影响。
        - CoT损失权重对Pre-Think和Post-Think的影响。
    - **跨数据集测试**：仅用R2R-CoT-320k训练，在RxR-CE上零样本评估。
- **充分性**：实验设计较为全面，覆盖了标准基准、多种方法对比、核心组件消融、超参数分析以及跨领域泛化。对比方法均为近两年顶级会议/期刊成果，设置公平（区分是否使用大模型、是否使用额外数据）。但仅在两个数据集上评估，环境多样性有限（仅室内场景）。

---

### 6. 论文的主要结论与发现

- **发现1——测试时推理崩溃**：Pre-Think和Post-Think策略在测试时表现显著差于No-Think，说明在动态部分可观测环境中显式推理会导致误差累积和性能下降。
- **发现2——Aux-Think的有效性**：提出的Aux-Think框架在仅使用R2R-CoT-320k数据训练时，即达到与使用大量额外数据的SOTA方法相当的性能，在数据效率和成功率之间取得了Pareto最优。
- **发现3——辅助监督的互补性**：CoT推理和指令重建两种辅助任务互补，结合滚动规划能达到最佳效果。
- **发现4——跨数据泛化**：Aux-Think在RxR-CE跨数据集测试中取得最优SR，证明其鲁棒泛化能力。

---

### 7. 优点

- **方法创新**：首次系统研究VLN中的推理策略，提出训练-测试解耦的Aux-Think范式，有效避免测试时推理崩溃。
- **数据集贡献**：释放R2R-CoT-320k，是首个面向VLN的大规模CoT数据集，可推动后续研究。
- **数据高效性**：Aux-Think在数据量仅为Uni-NaVid/NaVILA的三分之一左右时，SR与SOTA持平或超越，显示极强的数据效率。
- **实验严谨性**：控制变量对比，细致分析推理损失权重、预测步数、辅助任务等影响。

---

### 8. 不足与局限

- **实验覆盖**：仅在两个室内导航数据集（R2R-CE和RxR-CE）上验证，未涉及室外或更复杂动态场景。数据集环境为仿真器Habitat，与现实世界可能有差距。
- **偏差风险**：CoT数据由Qwen-2.5-VL-72B自动生成，可能带有模型偏见或错误，尽管进行了人工审核，但质量难以完全保证。
- **应用限制**：方法依赖单目RGB输入，缺乏深度或全景信息，在需要精确空间定位时可能受限。论文也指出这为未来融入深度、定位等提供了方向。
- **其他**：仅使用监督微调，未尝试强化学习或在线交互训练；动作空间离散化（固定的角度和位移），可能限制灵活性；未报告测试时延的详细数据分析。

（完）
