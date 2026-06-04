---
title: Empowering World Models with Reflection for Embodied Video Prediction
title_zh: 用反思赋能世界模型用于具身视频预测
authors: "Xiaowei Chi, Chun-Kai Fan, Hengyuan Zhang, Xingqun Qi, Rongyu Zhang, Anthony Chen, Chi-Min Chan, Wei Xue, Qifeng Liu, Shanghang Zhang, Yike Guo"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=onumui0nHi"
tags: ["query:vla"]
score: 8.0
evidence: 结合VLM的世界模型用于具身视频预测
tldr: 具身场景中视频预测模型缺乏鲁棒理解，难以进行多步预测或处理分布外场景。本文提出RoG（生成反思），利用预训练视觉-语言模型和视频生成模型的互补优势作为世界模型，通过中间推理策略增强预测。同时引入EVA-Bench基准评估。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 800, \"height\": 433, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1737, \"height\": 1216, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1757, \"height\": 585, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1759, \"height\": 1223, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1737, \"height\": 773, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1443, \"height\": 1170, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1778, \"height\": 544, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1723, \"height\": 900, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1669, \"height\": 434, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1502, \"height\": 531, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1447, \"height\": 1780, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 918, \"height\": 921, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-onumui0nhi/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 843, \"height\": 1004, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1707, \"height\": 490, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 858, \"height\": 402, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 854, \"height\": 355, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 857, \"height\": 240, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 854, \"height\": 293, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 824, \"height\": 366, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1075, \"height\": 963, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1457, \"height\": 361, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1771, \"height\": 167, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1768, \"height\": 169, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-onumui0nhi/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1774, \"height\": 762, \"label\": \"Table\"}]"
motivation: 现有视频预测模型缺乏鲁棒理解，无法处理多步和分布外场景。
method: 提出RoG，结合视觉-语言和视频生成模型作为世界模型，利用中间推理策略。
result: RoG在EVA-Bench上显著提升预测准确性和鲁棒性。
conclusion: 结合VLM与生成模型的世界模型可有效支持具身预测任务。
---

## Abstract
Video generation models have made significant progress in simulating future states, showcasing their potential as world simulators in embodied scenarios. However, existing models often lack robust understanding, limiting their ability to perform multi-step predictions or handle Out-of-Distribution (OOD) scenarios.  To address this challenge, we propose the Reflection of Generation (RoG), a set of intermediate reasoning strategies designed to enhance video prediction.  It leverages the complementary strengths of pre-trained vision-language and video generation models, enabling them to function as a world model in embodied scenarios. To support RoG, we introduce Embodied Video Anticipation Benchmark(EVA-Bench), a comprehensive benchmark that evaluates embodied world models across diverse tasks and scenarios, utilizing both in-domain and OOD datasets. Building on this foundation, we devise a world model, Embodied Video Anticipator (EVA), that follows a multistage training paradigm to generate high-fidelity video frames and apply an autoregressive strategy to enable adaptive generalization for longer video sequences. Extensive experiments demonstrate the efficacy of EVA in various downstream tasks like video generation and robotics, thereby paving the way for large-scale pre-trained models in real-world video prediction applications. The video demos are available at https://sites.google.com/view/icml-eva.

---

## 论文详细总结（自动生成）

# 论文中文详细总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：现有视频生成模型在模拟未来状态方面取得进展，可作为具身场景中的世界模拟器。然而，现有模型缺乏鲁棒理解能力，难以进行多步预测或处理分布外（OOD）场景，往往依赖人工干预，限制了它们在具身机器人等实际任务中的应用。
- **核心问题**：如何将视觉理解与视频生成能力有机结合，使世界模型具备自我反思、迭代修正和长时域预测能力，从而在具身场景下完成复杂任务级预测。
- **整体目标**：提出**Reflection of Generation (RoG)** 框架，利用预训练的视觉-语言模型（VLM）和视频生成模型（VDM）互补优势，构建统一的具身世界模型；并设计EVA模型和EVA-Bench基准以验证效果。

## 2. 方法论
### 2.1 核心思想
- **Reflection of Generation (RoG)**：将中间推理步骤（反思）融入视频生成过程，实现自我修正和深层理解。将理解任务和生成任务解耦，使VLM和VDM可组合为统一世界模型。
- **视频预测层次**：定义三个复杂度层次：帧级预测、任务级预测、串行任务级预测。本文聚焦**任务级预测**，作为桥接帧级生成和任务推理的核心。
- **RoG世界模型形式化**：

\[
W_{RoG}(O_0, I) = \text{Reflect}(H) \cdot P(\{O_t\}_{t=1}^T | O_0, I, H)
\]

其中，\(H\)为编码的隐状态，Reflect()提供三种响应：**extend**（扩展预测）、**regenerate**（重新生成）、**output**（输出最终结果）。算法（Algorithm 1）通过迭代直到任务完成。

### 2.2 关键技术细节
- **模型结构 EVA**：
  - **VLM骨干**：7B参数（基于ChatUniVi + Vicuna-v1.5），使用CLIP ViT-L/14视觉编码器，采用参数自由的token聚类减少视频token开销。
  - **VDM骨干**：1.5B参数（基于Dynamicrafter），生成16帧/2秒视频，条件包含图像、FPS、语言嵌入。
  - **Ensemble-LoRA**：为不同领域（人类自我中心、真实机器人、仿真机器人）训练低秩适应模块，通过任务token控制的门控系统组合，实现多域泛化。
  - **跨注意力生成适配器**：将VLM隐特征线性变换到VDM文本嵌入空间，用扩散去噪损失优化。
- **多阶段训练策略**：
  - Stage 1：视频-标题对齐（COCO、CC3M子集）。
  - Stage 2：QA指令微调（融入VideoChatGPT等开源数据 + EVA指令数据集）。
  - Stage 3：整体管道适应，训练生成适配器和VDM的Ensemble-LoRA。
- **自回归帧扩展**：基于RoG，生成初始视频（16帧），检查任务是否完成；若未完成，取最后1帧和t帧作为下一轮输入，重复生成直到任务完成。

### 2.3 RoG任务分解
- 四个元任务：
  - **Action-Description**：生成简短文本描述（主语+动词+宾语+位置+目的地），评估理解能力。
  - **Finish-Thinking**：判断是否应扩展帧以完成任务（二元输出Yes/No）。
  - **How-To**：将任务指令转换为视觉输出和文本响应。
  - **Next-Step**：预测视频序列中的下一步动作（语言和视觉）。

## 3. 实验设计
### 3.1 数据集与场景
- **训练数据集**：EVA-Instruct，共500K QA对，来源包括：
  - 仿真机器人：CALVIN (23k)
  - 真实机器人：RoboVQA (800k, 按权重0.1采样)、RT-1 (70k)
  - 人类活动：Ego4D (3.5M, 权重0.01)、Ego-Exo4D keystep (21k)
- **评估基准**：EVA-Bench，包含125个精心挑选的高质量样本，涵盖真实机器人、仿真机器人、自我中心人类活动，并包含in-domain和OOD场景。
- **OOD评估**：专家手动修改prompt中的主体或对象（如“Place coke can into the bottom drawer”改为“Please close bottom drawer”）。

### 3.2 对比方法
- **VQA任务**：与ChatUniVi、LLAVA-NI、LLAVA-NV、LLAVA-O、Minicpmv2、Qwen2-VL、GPT-4o等VLM对比零样本性能；以及LoRA/全参数微调版本。
- **视频生成质量**：与Dynamicrafter（DC）、DC-Tune、EVA-Gen（仅VDM模块）、两阶段方法（ChatUniVi+DC、Qwen2+DC等）对比。
- **机器人规划**：在RT-1上对比AVDC、EVA w/o RoG、EVA；在CALVIN上对比w/o RoG + CMLP、EVA+CMLP等。

### 3.3 评估指标
- **语言指标**：BLEU-1, METEOR, ROUGE-L, CIDEr, SPICE, CLIP score, GPT-4o作为评判者（评分基于对象、动作类型、位置、属性四个维度）。
- **视频指标**：Subject Consistency (SC), Background Consistency (BC), Motion Smoothness (MS), Fréchet Video Distance (FVD), Goal Completion Estimation (GCE)。
- **任务成功率**：人工评估任务完成率（RT-1实验）和仿真环境成功率（CALVIN实验）。

## 4. 资源与算力
- 论文在附录A.5表7中给出了训练超参数，但**未明确说明总训练硬件和时长**。仅提及“Training hardware: 8 Nvidia A800 chips”，训练步数20000 steps（Stage 3），但未给出各阶段总耗时。此外，VLM Stage 1和Stage 2使用了更大batch size（128），但未说明具体算力。总体而言，算力信息不完整。

## 5. 实验数量与充分性
- **主要实验组**：
  - VQA性能对比（表1）：对比8种基线，含零样本和微调版本。
  - 视频生成质量（表2）：对比10种配置（含不同VLM+VDM组合）。
  - How-To和Next-Step任务级生成（表3）：对比4种配置。
  - 机器人规划RT-1（表4）：3种方法，分in-domain和OOD共65次试验（人工评估）。
  - CALVIN（表5）：4种任务，含视频评估和仿真评估，共多种条件。
- **消融实验**：通过对比EVA w/o RoG、EVA-2Stage、不同VLM组合等，验证了RoG和完整管道的重要性。但未做更细粒度消融（如反思模块各成分、帧扩展步长影响等）。
- **充分性判断**：实验覆盖了理解、生成、机器人规划三大维度，且包含OOD测试，较为全面。但人工评估样本量偏小（RT-1共65次，CALVIN视频评估每个任务约41-157次）。GPT-4o评判可能存在偏差（作者已指出），但补充了传统指标。总体上实验设计合理，结论可信。

## 6. 主要结论与发现
- **RoG有效性**：引入反思机制（中间推理步骤）显著提升了任务完成率和长视频生成一致性。在RT-1 OOD任务中，EVA比w/o RoG多完成7个成功案例（表4）。
- **EVA性能**：EVA在VQA（GPT-4o评分62.63 vs 次优Qwen2的29.58）、视频质量（SC 97.11, FVD 184.81）和机器人规划成功率（RT-1 in-domain 84% vs AVDC 58%）上均大幅领先基线。
- **理解与生成的正相关性**：EVA-S中的语言分数（EVAS-L）与视频分数（EVAS-V）呈正相关，表明提升理解能力可直接改善生成质量。
- **多域泛化**：Ensemble-LoRA和分阶段训练使模型能适应人-自我中心、机器人等不同域，并有效应对OOD场景。

## 7. 优点
- **创新性强**：首次将“反思”思路系统性地引入视频预测，提出层次化任务分解和迭代自修正框架。
- **模块化设计**：解耦理解与生成，支持任意VLM和VDM组合，具有可扩展性。
- **数据集与基准建设**：构建了EVA-Instruct（500K QA对）和EVA-Bench（125样本，含OOD），涵盖多场景、多任务，为领域提供标准化评估工具。
- **实验全面**：覆盖语言、视频、机器人模拟三大维度，且包含OOD测试和人工评估，结果可信。
- **开源可复现**：提供视频演示网站，代码和数据应可获取（论文未明确声明，但提供了匿名链接）。

## 8. 不足与局限
- **数据集偏差风险**：EVA-Instruct主要来源于Ego4D、Ego-Exo4D、Open-X-Embodiment等，偏重室内操作任务，缺乏户外、动态环境、多智能体交互等场景，可能限制泛化。
- **OOD评估人工标注**：RT-1 OOD任务仅15次试验，样本量较小，统计显著性不足。CALVIN仿真评估样本量中等。
- **反思机制依赖VLM输出**：VLM可能在判断任务完成时产生误差，从而影响迭代终止时机，文中未深入分析错误传播。
- **计算资源未公开**：缺少总训练时长、成本等细节，不利于复现和横向比较。
- **长视频生成限制**：尽管使用自回归扩展，但每次生成固定16帧，扩展次数未给出上限，长序列一致性可能随帧数增多而下降（文中未评估极长视频）。
- **与纯强化学习世界模型对比缺失**：未与基于状态建模的传统世界模型（如Dreamer）对比，仅与视频生成类方法比较。

（完）
