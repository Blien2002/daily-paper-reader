---
title: Hierarchical Planning for Complex Tasks with Knowledge Graph-RAG and Symbolic Verification
title_zh: 基于知识图谱增强检索与符号验证的分层复杂任务规划
authors: "Flavio Petruzzellis, Cristina Cornelio, Pietro Lio"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=vfqdJy12Kk"
tags: ["query:vla"]
score: 7.0
evidence: 基于LLM的分层次规划与符号验证用于机器人任务
tldr: 大型语言模型作为机器人规划器在长时域复杂任务中表现不佳，尤其是需要外部知识的场景。本文提出神经符号方法，使用知识图谱增强检索辅助LLM进行分层规划，将复杂任务分解为可执行原子动作序列，并用符号验证确保正确性。在多个机器人规划基准上，该方法显著提高了规划的成功率和正确性，为LLM在机器人领域的应用提供了更可靠的途径。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-vfqdjy12kk/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1752, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vfqdjy12kk/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 865, \"height\": 443, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vfqdjy12kk/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 862, \"height\": 328, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vfqdjy12kk/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1446, \"height\": 744, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-vfqdjy12kk/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1447, \"height\": 799, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 812, \"height\": 547, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1767, \"height\": 549, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1468, \"height\": 720, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1068, \"height\": 720, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1767, \"height\": 432, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1524, \"height\": 407, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1766, \"height\": 321, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1242, \"height\": 341, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1764, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1765, \"height\": 331, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1767, \"height\": 358, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1765, \"height\": 416, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1765, \"height\": 306, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1586, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1762, \"height\": 261, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1766, \"height\": 311, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1767, \"height\": 350, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-vfqdjy12kk/table-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1767, \"height\": 381, \"label\": \"Table\"}]"
motivation: LLM作为规划器在长时域和需要外部知识的任务中容易出错。
method: 结合知识图谱增强检索和符号验证，指导LLM进行分层任务分解和原子动作序列生成。
result: 在机器人规划基准上，该方法相比纯LLM规划取得了更高的任务完成率和更少的错误分解。
conclusion: 该工作证明知识图谱和符号验证能有效增强LLM在机器人规划中的可靠性和准确性。
---

## Abstract
Large Language Models (LLMs) have shown promise as robotic planners but often struggle with long-horizon and complex tasks, especially in specialized environments requiring external knowledge. While hierarchical planning and Retrieval-Augmented Generation (RAG) address some of these challenges, they remain insufficient on their own and a deeper integration is required for achieving more reliable systems. To this end, we propose a neuro-symbolic approach that enhances LLMs-based planners with Knowledge Graph-based RAG for hierarchical plan generation. This method decomposes complex tasks into manageable subtasks, further expanded into executable atomic action sequences. To ensure formal correctness and proper decomposition, we integrate a Symbolic Validator, which also functions as a failure detector by aligning expected and observed world states. Our evaluation against baseline methods demonstrates the consistent significant advantages of integrating hierarchical planning, symbolic verification, and RAG across tasks of varying complexity and different LLMs. Additionally, our experimental setup and novel metrics not only validate our approach for complex planning but also serve as a tool for assessing LLMs' reasoning and compositional capabilities. Code available at https://github.com/corneliocristina/HVR.

---

## 论文详细总结（自动生成）

# 论文总结：基于知识图谱增强检索与符号验证的分层复杂任务规划

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：大型语言模型（LLM）作为机器人规划器在长时域和复杂任务中表现脆弱，尤其需要外部专业知识的环境（如厨房、医疗）。单独使用分层规划或检索增强生成（RAG）仍有不足，集成不深导致幻觉、逻辑错误和不可靠执行。
- **整体含义**：本文旨在通过神经符号方法，深度融合LLM的灵活性与符号知识的严谨性，提升机器人规划的正确性、可验证性和适应性。成果对推动LLM在安全关键领域（如手术、自动驾驶）的应用具有重要价值。

## 2. 论文提出的方法论（核心思想、关键技术细节）

- **方法名称**：HVR（Hierarchical planning, symbolic Verification, and RAG over Knowledge Graphs）
- **核心思想**：将复杂任务分层分解为宏动作（macro-actions）和原子动作（atomic actions），利用知识图谱增强检索（KG-RAG）提供上下文，并用符号验证器保证形式和执行的正确性。
- **关键技术细节**：
  - **本体与动态知识图（Ontology & Dynamic KG）**：基于OntoThor本体初始化知识图，包含物体类、属性、状态、关系。执行过程中实时更新场景图（视觉、听觉转三元组）。
  - **知识图谱RAG**：LLM根据任务描述从KG中选出相关物体子图（类型、属性、当前状态），作为生成计划的上下文。
  - **分层规划**：
    - 宏计划生成 φ(t)：LLM将自然语言任务 t 映射为宏动作序列⟨ma₁,…,maₘ⟩。
    - 原子动作块生成 π(maᵢ)：每个宏动作通过LLM+动作映射器展开为原子动作序列⟨aaᵢ₁,…,aaᵢₖ⟩，并映射到有限动作集A中的有效动作（余弦相似度匹配）。
  - **符号验证与修正**：
    - 基于PDDL的符号验证器（自研）检查宏动作的条件和原子动作的可行性，返回具体错误信息。
    - 宏层修正：LLM根据验证反馈调整预/后置条件。
    - 原子层修正：LLM根据误差修改动作序列（含一个上下文示例）。
  - **运行时故障检测**：验证“理想世界”状态（PDDL推演）与场景图（实际视觉）是否对齐，如不一致则触发修正。
  - **宏动作库**：执行成功后的宏动作存储到知识图，并可聚类共享，支持知识迁移。

## 3. 实验设计（数据集/场景、基准、对比方法）

- **模拟器与场景**：AI2Thor 3D厨房模拟器，使用OntoThor本体描述环境。12个任务（6个中等复杂度：6~20步；6个高复杂度：26~41步），包括新增的T11（番茄鸡蛋吐司）、T12（复杂摆盘）和T5bis（通用温热杯水）。
- **评估指标**：自建6个指标：
  1. Plan Correctness (PC)：与真实计划对齐度。
  2. Execution Success (ES)：正确计划在模拟器中的执行成功率。
  3. Length Discrepancy (LD)：计划长度与最小真实计划之差。
  4. Expanded Plan Verification (EPV)：原子计划验证通过比例（修正后）。
  5. Macro Plan Verification (MPV)：宏计划验证通过比例（修正前/后）。
  6. Atomic Action Block Verification (AABV)：原子动作块验证通过比例（修正前/后）。
- **对比方法（消融基线）**：
  - HV（去RAG）：全知识图作为上下文 + 验证
  - HR（去验证）：分层+RAG
  - VR（去分层）：验证+RAG
  - R（仅RAG）
  - LLM（无分层、无RAG、无验证）
- **LLM选择**：Phi-3-mini-4k-instruct（小模型）和Gemini-1.5-flash（大模型），均为免费模型确保可复现。
- **额外对比**（附录）：与Smart-LLM（12个任务）和ProgPrompt（7个厨房任务）比较，HVR均100%成功完成。

## 4. 资源与算力

- **文中未明确说明**：未提及使用的GPU型号、数量或训练时长。仅提到LLM为预训练冻结，不需要微调，计算开销主要来自推理和验证。
- **效率分析**：附录给出平均执行时间（Gemini 1.5 flash 下 HVR约3285秒，Gemini 2.0 flash下约682秒），但未说明硬件配置。强调HVR耗时最长但正确率最高（图5）。

## 5. 实验数量与充分性

- **数量**：主实验在12个任务上运行6种方法×2个LLM，共144组配置，产生完整指标数据。消融充分（分别移除H、V、R三要素）。额外对比实验7-12个任务。
- **充分性与客观性**：
  - 指标设计全面覆盖生成、执行、形式验证、修正、最小性。
  - 提示使用固定模板和相同示例，减少人为偏差。
  - 使用小模型和大模型体现泛化性。
  - 但**所有实验仅在单一模拟器（AI2Thor）和厨房领域**进行，缺乏跨场景、跨机器人硬件的验证，存在过适配风险。

## 6. 主要结论与发现

- HVR在所有任务和两个LLM上**显著优于所有基线**：小模型依赖RAG（正确率55.5% vs HV 18.9%），大模型依赖分层（正确率85.3% vs HR 49.0%），组合最优（HVR达94.2%）。
- 正式正确性（EPV）与计划正确性（PC）强相关，表明符号验证能有效提升计划质量。
- LLM生成的计划普遍过长（HVR使长度增加约100%~200%），修正过程会引入额外步骤。
- 模拟器执行成功率仅约95%，揭示当前模拟器稳定性不足，凸显运行时故障检测的必要性。
- LLM在定义明确的目标任务（如“用微波炉加热水”）上表现良好，在开放目标（如“得到温水”）上表现下降。

## 7. 优点（方法或实验设计亮点）

- **创新性融合**：首次将KG-RAG、分层规划和符号验证深度整合到统一的LLM规划框架中，发挥各自优势。
- **完整评估体系**：提出6个新指标，覆盖计划生成、执行、形式验证、最小性、修正效果，分析维度丰富。
- **可复现性**：使用免费开源LLM，代码公开，提示模板固定，便于独立验证。
- **知识迁移**：提出宏动作库和聚类共享机制，支持跨机器人能力复用。
- **实际应用导向**：运行时故障检测机制直接应对真实世界中的执行不确定性。

## 8. 不足与局限

- **领域局限**：仅在AI2Thor厨房环境验证，未在更复杂或不同领域（如医疗、太空）实验，泛化性存疑。
- **依赖预定义本体**：需专家手工构建初始本体和动作集合，更新成本高，难以自动化适应新环境。
- **计划线性限制**：仅支持完全顺序的原子计划，不支持偏序或并行执行，在部分可交换任务中可能产生冗余。
- **提示敏感性**：LLM对提示措辞敏感，虽声称已优化，但未系统测试不同提示变体影响。
- **修正孤立性**：宏层和原子层的修正独立进行，未建模跨层次错误依赖，可能无法解决深层因果错误。
- **计算开销**：分层处理+多轮验证+多次LLM调用导致耗时显著增加（尤其大模型），实时性受影响。
- **缺乏与SOTA规划系统的直接比较**：因环境不兼容未能与PDDL求解器或其他神经符号规划器定量对比。

（完）
