---
title: "SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding"
title_zh: SECOND：通过选择性与对比解码缓解视觉-语言模型中的感知幻觉
authors: "Woohyeon Park, Woojin Kim, Jaeik Kim, Jaeyoung Do"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=SbyrpBNNs4"
tags: ["query:vla"]
score: 4.0
evidence: 通过选择性与对比解码缓解视觉-语言模型中的幻觉问题
tldr: 针对视觉-语言模型（VLM）中严重的对象幻觉问题，本文提出SECOND方法，通过渐进式选择并整合多尺度视觉信息，以对象为中心进行对比解码。该方法显著降低了感知幻觉，并在多个基准上优于现有方法，为VLM在具身智能中的可靠视觉理解提供了支持。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 708, \"height\": 747, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 827, \"height\": 1121, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1406, \"height\": 860, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 847, \"height\": 631, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 844, \"height\": 346, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 838, \"height\": 337, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-sbyrpbnns4/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1448, \"height\": 536, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1767, \"height\": 714, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1755, \"height\": 678, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 868, \"height\": 283, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 858, \"height\": 405, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 553, \"height\": 212, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1079, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-sbyrpbnns4/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1779, \"height\": 626, \"label\": \"Table\"}]"
motivation: 视觉-语言模型中的对象幻觉严重影响了视觉理解的准确性。
method: 提出选择性与对比解码，逐步选择多尺度视觉信息并以对象为中心进行对比。
result: 显著减少了感知幻觉，在多个VLM基准上表现优异。
conclusion: 多尺度视觉信息的选择与对比能有效提升VLM的视觉理解可靠性。
---

## Abstract
Despite significant advancements in Vision-Language Models (VLMs), the performance of existing VLMs remains hindered by object hallucination, a critical challenge to achieving accurate visual understanding. To address this issue, we propose SECOND: Selective and Contrastive Decoding, a novel approach that enables VLMs to effectively leverage multi-scale visual information with an object-centric manner, closely aligning with human visual perception. SECOND progressively selects and integrates multi-scale visual information, facilitating a more precise interpretation of images. By contrasting these visual information iteratively, SECOND significantly reduces perceptual hallucinations and outperforms a wide range of benchmarks. Our theoretical analysis and experiments highlight the largely unexplored potential of multi-scale application in VLMs, showing that prioritizing and contrasting across scales outperforms existing methods.

---

## 论文详细总结（自动生成）

## 论文总结：SECOND：通过选择性与对比解码缓解视觉-语言模型中的感知幻觉

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：视觉‑语言模型（VLM）在实际应用中普遍存在**对象幻觉（object hallucination）**——模型生成的回答看似合理，但事实与视觉内容不符（例如回答“有狗”而图像中无狗）。该问题严重制约了VLM在高可靠性场景（如自动驾驶、医疗影像）中的部署。
- **研究动机**：现有缓解幻觉的方法（如数据增强、抑制语言先验、改进视觉编码器）大多采用单尺度视觉表示或对多尺度信息不加区分地整合，未能充分利用多尺度视觉信息的内在层次结构，且缺乏对视觉注意与幻觉之间关系的理论分析。
- **整体含义**：提出一种无需额外训练的**SECOND**框架，通过**选择性整合多尺度视觉块**和**多阶段对比解码**，模拟人类视觉由粗到精的感知过程，系统性地降低感知幻觉，提升VLM的视觉理解可靠性。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：
  - 人类视觉系统通过**选择性注意**和**对比处理**进行感知。SECOND将这一直觉引入VLM：在多个视觉分辨率阶段（stage）中，逐步选择与目标对象相关的视觉块（patches），并利用阶段间的输出差异进行对比解码，从而强化对象相关的细粒度信息，抑制无关干扰。
- **关键技术细节**：
  1. **多尺度视觉特征集成**：
     - 训练无关地扩展视觉编码器：通过双线性插值位置编码，将低分辨率图像输入已有编码器，生成多个尺度的视觉token（例如84×84、168×168、336×336、672×672）。
     - 保持patch尺寸不变，不同分辨率对应不同数量的patches，从而实现由粗到精的视觉密度递增。
  2. **动态块选择机制**：
     - 每阶段基于前阶段的**视觉注意力图**（融合自注意力和交叉注意力）选择当前阶段需要保留的patches。
     - 选择比例由超参数λ和注意力图的熵H(V)决定：  
       `pselect = (exp(λ·H(V)) - 1) / (exp(λ) - 1)`  
       当注意力集中（熵低）时选择较少patches；当注意力分散（熵高）时选择更多patches以补充细粒度信息。
  3. **多阶段对比解码**：
     - 将早期阶段（粗分辨率、未选择）产生的输出视为**业余（amateur）**，最终阶段（高分辨率、选择性整合）的输出视为**专家（expert）**。
     - 通过线性组合各阶段logits进行对比解码：  
       `logit_SECOND = logit_expert + α(logit_expert - logit_{amateur3}) + β(logit_{amateur3} - logit_{amateur2}) + γ(logit_{amateur2} - logit_{amateur1})`  
       其中α, β, γ ∈ [0,1]为可调超参数。
- **理论支撑**：论文证明了**注意力Dice系数**（衡量注意力与真实对象掩码的重合程度）随多阶段选择单调递增（Theorem 3.3），从而降低幻觉概率（Observation）。

### 3. 实验设计：数据集、基准、对比方法
- **数据集与基准**：
  - **POPE**（三个子集：MSCOCO、A-OKVQA、GQA，各3000个“是/否”问题，评估Recall/Accuracy/F1）
  - **VQAv2 (lite)**（500个开放性问题）
  - **MMStar**（1500个问题，涵盖感知和推理）
  - **MMBench (lite)**（500个问题，综合评估）
- **对比方法**：
  - **基线**：原始VLM（LLaVA‑NeXT、LLaVA‑OneVision、Yi‑VL）的标准解码
  - **VCD**（Visual Contrastive Decoding）：采用噪声图像进行单阶段对比解码的代表性方法
- **评估配置**：
  - 在三种VLM上测试，涵盖不同视觉编码器（CLIP-336、SigLIP-384、CLIP-448）和不同LLM（Vicuna-7B、Mistral-7B、Qwen2-0.5B、Yi-6B）。

### 4. 资源与算力
- 论文**未明确说明**使用的GPU型号、数量或训练时长。由于SECOND是**训练无关**框架，仅在推理阶段进行多尺度处理和对比解码，因此不需要额外训练。其计算开销主要体现在多阶段前向传播和注意力图计算，作者提到默认4阶段配置比基线慢约1.4倍。

### 5. 实验数量与充分性
- **实验组数**：主要结果（表1、表2）覆盖12个POPE子场景和4个一般任务，共16组对比。消融实验包括：
  - 阶段配置（表3，5种配置）
  - 选择策略（表4，7种固定/动态策略对比）
  - 单阶段 vs 多阶段对比解码（图5，两个基准）
  - 超参数λ敏感性（图6a，20个取值）
  - 超参数α, β, γ全搜索（图6b，共1331组合）
  - 各阶段独立性能（附录表5）
- **充分性与公平性**：
  - 实验覆盖了多个VLM、两种LLM规模、多个领域的数据集，对比方法VCD是当前主流，实验设计较全面。
  - 消融实验系统地验证了各组成部分的贡献；超参数分析展示了方法的鲁棒性。
  - 不足：所有实验均基于相对较小的模型（≤7B参数），未在更大规模VLM（如LLaVA-13B、Qwen2-VL-72B）上验证；且仅在固定QA格式下测试，未涉及多轮对话或开放生成任务。

### 6. 论文的主要结论与发现
- **核心结论**：SECOND在**11/12个POPE子场景**中取得最佳F1/Acc，在**VQAv2、MMStar、MMBench**上一致优于基线和VCD。这表明**选择性多尺度视觉信息整合**与**多阶段对比解码**能显著缓解感知幻觉，同时不损害推理能力。
- **理论发现**：论文通过注意力Dice系数与幻觉概率的负相关关系（图2）证明了**视觉关注与对象掩码的对齐程度是幻觉的关键决定因素**；多阶段选择保证该系数单调递增（Theorem 3.3）。
- **设计启示**：单纯增加分辨率（所有patches无差别放大）会引入背景噪声，而**按注意力优先级选择相关patches**更为有效；多阶段对比解码比单一业余-专家对比更具优势（图5）。

### 7. 优点：方法或实验设计上的亮点
- **训练无关**：无需额外训练或微调，可直接应用于现有的CLIP/SigLIP类VLM，实用性强。
- **理论驱动**：从注意力Dice系数出发，给出了幻觉概率降低的理论保证，使方法有据可依。
- **多阶段渐进式设计**：模拟人类“先粗看后细看”的视觉策略，具有认知启发性。
- **对比解码创新**：从传统的单阶段业余-专家对比扩展为多阶段对比，更好地利用不同粒度视觉信息之间的差异。
- **实验全面性**：在多个模型、多个数据集上验证，消融实验覆盖了各组件（阶段数、选择策略、CD变体）的影响，超参数分析证实了稳定性。

### 8. 不足与局限
- **依赖内部注意力图**：块选择基于模型自身的注意力分布，如果注意力本身校准不良（例如被语言先验主导），则选择可能失效，导致错误累积（论文本身提及）。
- **计算成本增加**：4阶段配置带来约1.4倍推理时间，在实时性要求高的场景中可能受限。
- **超参数敏感**：虽然图6显示多数配置优于基线，但λ、α、β、γ的最优值在任务间有波动（附录表6、7），需要针对不同模型和任务进行调整。
- **评估范围有限**：仅测试了静态QA类基准（POPE、VQAv2、MMBench等），未在对话、长视频理解、高分辨率或具身智能场景中验证；且模型规模限于7B以下，缺乏对更大LLM的泛化性验证。
- **公平性隐患**：对比方法VCD固定使用噪声图像作为业余，而SECOND的业余来自早期阶段，二者设计不同，但论文未讨论这种差异可能带来的偏向。

（完）
