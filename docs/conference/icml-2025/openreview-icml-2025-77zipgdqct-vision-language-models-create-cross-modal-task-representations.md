---
title: Vision-Language Models Create Cross-Modal Task Representations
title_zh: 视觉语言模型创建跨模态任务表征
authors: "Grace Luo, Trevor Darrell, Amir Bar"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=77ziPGdQct"
tags: ["query:vla"]
score: 4.0
evidence: 研究VLM中的任务表征，与最先进VLA理解相关
tldr: 发现自回归视觉语言模型能够创建跨模态任务向量，该向量对模态和格式不变，可在文本和图像之间实现任务迁移。实验表明单个任务向量优于完整提示，揭示了VLM处理机制，对理解VLA模型内部表征有启示。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 855, \"height\": 606, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 836, \"height\": 528, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 840, \"height\": 836, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1301, \"height\": 1224, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 779, \"height\": 283, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 774, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 858, \"height\": 1177, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1755, \"height\": 570, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1425, \"height\": 575, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1594, \"height\": 1118, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1798, \"height\": 684, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1517, \"height\": 2303, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1137, \"height\": 2225, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-77zipgdqct/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1432, \"height\": 1476, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1795, \"height\": 565, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1763, \"height\": 609, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 765, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1115, \"height\": 282, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1342, \"height\": 171, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 869, \"height\": 546, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 799, \"height\": 144, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1446, \"height\": 391, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1522, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1573, \"height\": 231, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1498, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1527, \"height\": 494, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-77zipgdqct/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 793, \"height\": 331, \"label\": \"Table\"}]"
motivation: 理解VLM处理多任务能力的内部表征。
method: 通过跨模态迁移实验度量任务向量的对齐程度。
result: 单个任务向量在跨模态迁移中优于完整提示。
conclusion: 揭示VLM的压缩任务表征机制，助力VLA模型理解。
---

## Abstract
Autoregressive vision-language models (VLMs) can handle many tasks within a single model, yet the representations that enable this capability remain opaque. We find that VLMs align conceptually equivalent inputs into a shared task vector, which is invariant to modality (text, image) and format (examples, instruction), and may simplify VLM processing. We measure this alignment via cross-modal transfer--the ability of a task vector derived in one modality to trigger the correct generation in another--on a range of tasks and model architectures. Although the task vector is highly compressed, we find that this single vector outperforms prompting the model with the full task information, unique to this cross-modal case. Furthermore, we show that task vectors can be transferred from a base language model to its fine-tuned vision-language counterpart, and that they can be derived solely from instructions without the need for examples. Taken together, our findings shed light on how VLMs internally process task information, and how they map different modalities into common semantic representations.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：自回归视觉语言模型（VLM）能够在单一模型中处理多种任务，但其内部表征机制仍不透明。理解VLM如何压缩和共享不同任务信息，对于提升模型的可解释性、可控性和跨模态泛化能力至关重要。
- **核心问题**：VLMs是否会将概念上等价的不同输入（文本示例、图像示例、文本指令）映射到一个共享的任务表征（task vector）上？该表征是否对模态和格式具有不变性？
- **背景**：已有工作（如Hendel et al., 2023; Todd et al., 2024）在纯语言模型中发现了任务向量，但在多模态语境下，跨模态任务向量的存在及其对齐程度尚未被探索。

## 2. 方法论

- **核心思想**：通过在VLM的某一隐藏层提取特定位置的激活（即“任务向量”），并利用激活补丁（activation patching）技术将其从一个模态迁移到另一个模态，从而验证任务表征的跨模态对齐。
- **关键技术细节**：
  - 定义三种任务规范：文本示例、图像示例、文本指令。
  - **跨模态补丁（Cross-Modal Patching）**：首先从源模态的规范中提取任务向量（位于最后一个分隔符token的层输出），然后将其注入到目标模态查询的对应层和位置，诱导模型生成正确的任务输出，而不显式提供任务信息。
  - 对比基线：few-shot prompting（将完整规范与查询一起输入模型）。
  - 任务向量提取位置遵循纯语言研究的惯例（最后查询-答案对之间的分隔符token）。
- **算法流程**（文字描述）：
  1. 给定任务t和模型f，对源模态规范p_txt（如文本示例）执行正向传播，从第l层分隔符token处获取隐藏状态h_{l,txt}。
  2. 对目标模态查询x_img执行正向传播，在第l层对应token位置将h_{l,txt}替换为源任务向量（即补丁），然后继续生成，得到输出y_img。
  3. 通过比较生成的首个token与真实标签的准确率来评估跨模态迁移性能。

## 3. 实验设计

- **数据集/场景**：
  - **主要评估集**：6个自建跨模态任务（Country-Capital, Country-Currency, Animal-Latin, Animal-Young, Food-Color, Food-Flavor）。每个任务包含30个验证样本和100个测试样本，分别提供文本示例、图像示例和文本指令。
  - **扩展VQA任务**：从VQAv2中筛选出3个子任务（Food-Class, Shirt-Color, Man-Holding），使用LLaVA-NeXT生成的密集文本描述作为文本示例，图像-答案对作为图像示例。
  - **任务覆盖（Task Overriding）**：4种冲突场景（语义、语法、创意生成、事实回忆），使用VQAv2、OK-VQA、A-OKVQA等数据集。
- **基准方法**：
  - 无上下文（No Context）、随机猜测（Random）
  - 同模态基线和跨模态基线：few-shot prompting（Prompt）和激活补丁（Patch）设置下的文本示例/图像示例/指令。
  - 对比模型：LLaVA-v1.5（late-fusion）、Mantis-Fuyu（early-fusion）、Idefics2（late-fusion，多模态ICL优化）。
- **评价指标**：首要生成token与预定义标签的精确匹配准确率（任务覆盖中使用GPT-4o自动评分）。

## 4. 资源与算力

- 文中未明确说明使用的GPU型号、数量、训练时长等具体算力信息。
- 仅在第A.2节提到计算开销：对于N=30的文本示例，patching比prompting减少11倍运行时间和2.4倍显存消耗（prompting: 2.20s, 20.02GB；patching: 0.20s, 8.21GB）。但未提及模型训练所需算力。

## 5. 实验数量与充分性

- **实验数量**：
  - 主要跨模态迁移实验：3个模型 × 6个任务 × 3个种子，共54组结果（表2）。
  - LLM到VLM迁移：2个模型 × 6个任务（表3）。
  - 指令任务向量实验：Idefics2上6个任务，对比指令、示例、集成（图6）。
  - 扩展VQA任务：3个任务（表4）。
  - 任务覆盖：4种场景，每种含1000个（前三种）或148个（第四种）样本（表5）；使用GPT-4o评估。
  - 消融实验：模板格式（附录表10）、所有模态组合（附录表12）、噪声指令（附录表9）。
  - 表征演化分析：logit lens解码、t-SNE可视化、三阶段演化图（图8、13、14、15）。
- **充分性与公平性**：
  - 覆盖了late-fusion和early-fusion两种架构，以及不同ICL能力的模型，具有代表性。
  - 对比了多种基线（无上下文、random、prompt、同模态patch），并进行了消融验证。
  - 但主要任务集为合成任务（6个），规模较小；扩展VQA任务仅3个，可能不足以完全反映真实场景的多样性。
  - 任务覆盖使用GPT-4o评分，可能引入评估偏差，但提供了合理替代方案。

## 6. 主要结论与发现

- **发现1**：VLMs难以直接进行跨模态few-shot prompting（文本示例→图像查询），但通过激活补丁可以显著提升性能（平均提升14-33%）。
- **发现2**：跨模态补丁中，文本示例优于图像示例（超出8-13%），表明文本提供了更清晰的任务表示。
- **发现3**：任务向量可以从基础LLM迁移到对应的微调VLM，且余弦相似度高达0.89-0.95，提示VLM保留了语言任务函数。
- **发现4**：任务向量不仅可从示例定义，也可从指令定义，且指令与示例集成的任务向量可提高样本效率（提升18%）。
- **发现5**：表征演化分为三个阶段（早期→输入、中期→任务摘要、后期→答案），且文本ICL与图像ICL的演化模式相似，但任务向量聚类按任务而非模态（t-SNE验证）。
- **发现6**：任务覆盖（overriding）中，补丁比系统提示更有效（语义/创意/事实回忆场景中高出27-59%）。

## 7. 优点

- **方法创新**：首次系统研究VLM中任务向量的跨模态特性，提出跨模态补丁方法量化对齐程度。
- **全面的实验设计**：覆盖多种任务规范（示例/指令、文本/图像）、多个模型架构（late-fusion/early-fusion），并包含LLM→VLM迁移、任务覆盖等深入场景。
- **可视化分析**：使用logit lens和t-SNE揭示表征演化动态和聚类结构，直观支持结论。
- **实用性**：发现跨模态补丁在计算效率（加速11倍、减显存2.4倍）和样本效率（集成指令）上的优势，具有应用潜力。

## 8. 不足与局限

- **实验覆盖**：主要任务集规模较小（6个合成任务），缺乏对更复杂真实世界任务的广泛测试；扩展VQA任务仅3个，统计显著性有限。
- **偏差风险**：任务向量提取位置和层选择基于验证集优化，可能过拟合特定设置；GPT-4o评分可能存在主观偏差。
- **理论解释**：未提供为什么VLMs会形成跨模态任务表示的严谨理论解释，仅提出假设（如结构同构、数据驱动收敛）。
- **应用限制**：任务补丁在复杂或开放生成任务上的鲁棒性未充分评估；依赖模型内部表示的访问，对黑盒API模型不适用。
- **模型范围**：仅测试了7B-8B参数规模的三类VLM，未涵盖更大规模或不同预训练策略的模型。

（完）
