---
title: "RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks"
title_zh: RDD：面向长时域任务规划器对齐的检索式演示分解器
authors: "Mingxuan Yan, Yuping Wang, Zechun Liu, Jiachen Li"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=zY5J1vp7tZ"
tags: ["query:vla"]
score: 9.0
evidence: RDD方法改进VLA规划器在长时域任务中的对齐
tldr: 针对层次化VLA框架中长时域操作任务，现有VLM规划器需要带细粒度分解的标注数据。RDD方法通过检索自动分解视频演示为子任务，无需人工标注，显著提升任务成功率。该方法有效对齐高层规划与底层策略，为VLA系统提供可扩展的分解方案。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-zy5j1vp7tz/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1415, \"height\": 540, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zy5j1vp7tz/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1315, \"height\": 745, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zy5j1vp7tz/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 438, \"height\": 331, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-zy5j1vp7tz/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1440, \"height\": 558, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1379, \"height\": 596, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 384, \"height\": 389, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 350, \"height\": 273, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 452, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 518, \"height\": 312, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 441, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 454, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1342, \"height\": 595, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1307, \"height\": 700, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1170, \"height\": 489, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1301, \"height\": 417, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1031, \"height\": 452, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1147, \"height\": 363, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-zy5j1vp7tz/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 860, \"height\": 136, \"label\": \"Table\"}]"
motivation: 层次化VLA框架中VLM规划器需要人工分解演示，成本高且易不匹配底层策略。
method: 提出基于检索的自动视频演示分解方法，从数据集中检索并分解子任务演示。
result: 在多种长时域操作任务上，RDD显著提升了任务成功率，无需额外标注。
conclusion: RDD为VLA系统提供自动对齐规划器与策略的有效途径。
---

## Abstract
To tackle long-horizon tasks, recent hierarchical vision-language-action (VLAs) frameworks employ vision-language model (VLM)-based planners to decompose complex manipulation tasks into simpler sub-tasks that low-level visuomotor policies can handle. Typically, the VLM planner needs finetuning to learn to decompose a new task, which requires target task demonstrations segmented into sub-tasks by either human annotation or heuristic rules. However, without prior knowledge, the heuristic sub-tasks can deviate significantly from the visuomotor policy's training data, thereby degrading task performance. To address these issues, we propose a Retrieval-based Demonstration Decomposer (RDD) that automatically decomposes video demonstrations into sub-tasks with prior by aligning the visual features of the decomposed sub-task intervals with those from the training data of the low-level visuomotor policies. RDD outperforms the state-of-the-art sub-task decomposer on both simulation and real-world tasks, demonstrating robustness across diverse settings. Code and more results are available at https://rdd-neurips.github.io

---

## 论文详细总结（自动生成）

```markdown
## 1. 核心问题与研究动机
- **背景**：层次化视觉-语言-动作（VLA）框架利用 VLM 作为高层规划器，将长时域复杂任务分解为简单子任务，由底层视觉运动策略执行。该框架需要微调 VLM 规划器，而微调数据需要将演示视频分解为带标签的子任务区间。
- **问题**：现有分解方法依赖人工标注（成本高、主观性强）或启发式规则（如基于运动速度、夹爪状态变化等），但这些规则生成的子任务区间可能与底层策略训练数据分布严重不匹配，导致规划器输出策略难以执行的指令，降低任务成功率。
- **核心目标**：提出一种**自动、免训练、计算高效**的演示分解方法，使分解出的子任务区间与底层策略的训练数据对齐，从而协调高层规划器与低层策略。

## 2. 方法论：RDD（检索式演示分解器）
- **核心思想**：将子任务识别建模为**最优划分问题**，通过动态规划高效求解，并利用**基于检索**的区间评分函数，促使分解结果与底层策略训练集中的子任务在视觉和时长特征上相似。
- **关键技术细节**：
  - **问题形式化**：给定演示视频序列 \(S_i\)，寻找最优划分 \(P^*\) 使得累加评分函数 \(J(P)=\sum_{I\in P}\tilde{J}(I)\) 最大。评分函数 \(\tilde{J}(I)\) 定义为区间长度与区间相似度的乘积：\(\tilde{J}(I_{ij}) = |I_{ij}| \cdot \text{sim}(I_{ij}, \text{ANNS}(\mathcal{V}(I_{ij}), \mathcal{D}_{\text{train}}^{\text{aug}}))\)。
  - **区间表示**：使用视觉编码器（如 LIV）将区间起始帧和结束帧的 RGB 图像编码为特征向量，拼接作为该区间的视觉表示 \( \mathcal{V}(I) = \text{concat}(E(o_b), E(o_e)) \)。
  - **近似最近邻搜索（ANNS）**：从底层策略训练集 \(\mathcal{D}_{\text{train}}^{\text{aug}}\) 中检索最相似的子区间，采用 Annoy 或 FAISS 加速。
  - **相似度函数**：结合视觉特征距离（angular distance）和时间长度相对差：\(\text{sim}(I, \tilde{I}) = -[\delta(\mathcal{V}(I), \mathcal{V}(\tilde{I})) + \alpha(1 - |I|/|\tilde{I}|)]\)。
  - **动态规划求解**：利用区间评分函数的可加性和最优子结构性质，采用 DP 算法（复杂度 \(O(N^2)\)，若子任务时长有上界则降至 \(O(N)\)）求得全局最优划分。
  - **OOD 子任务处理**：当演示中存在底层策略未学习过的新子任务时，RDD 可切换到另一种相似度度量，结合通用启发式（如 UVD）的分数 \(\beta G(I)\) 进行平衡。

## 3. 实验设计
- **数据集与基准**：
  - **仿真**：RLBench（机器人操作基准，18 个任务，但主要报告 13 个成功率>35% 的任务）。
  - **真实世界**：AgiBotWorld-Alpha 的“超市”任务（152 个演示构建数据库，37 个测试）。
  - **OOD 场景**：LIBERO（RoboCerebra 数据集，560 个演示建库，140 个测试）。
- **对比方法**：
  - **Expert**：任务特定启发式分解器（作为性能上界）。
  - **UVD**：基于视觉特征变化点检测的无任务分解器。
  - **Uniform**：均匀划分为 10 段。
  - **w/o Finetune**：预训练 VLM 不微调。
- **评估指标**：多任务成功率（平均成功率及排名），OOD 场景采用平均交并比（mIoU）。

## 4. 资源与算力
- 论文明确说明：微调过程使用 **4 块 NVIDIA 6000 Ada GPU**，**约 5 分钟**完成（2 epoch，LoRA rank=128）。
- 动态规划及 ANNS 检索在 CPU 上完成（AMD EPYC 9254，单核），但强调可并行化，且支持 GPU 加速（FAISS）。未提供完整训练 VLM 或底层策略的算力开销。

## 5. 实验数量与充分性
- **总计实验组数**：主实验（Table 1）10 个随机种子；消融实验包括：多种视觉编码器（7 种，Table 2）、权重参数 \(\alpha\)（4 种，Table 3）、演示数量（1 个 vs 3 个，Table 4）、OOD 场景（3 个 \(\beta\) 值，Table 5）、对比 Gemini-2.5-pro（Table 7）、免目标任务微调（Table 6）等，均给出了平均成功率与排名，并附标准差。
- **充分性与公平性**：实验覆盖仿真、真实、OOD 场景，对比方法包括专家、无任务、均匀等强基线，所有方法基于同一底层策略（RVT）和 VLM 规划器（LLaVa-8B），控制变量充分。多次随机种子重复，结果具有统计显著性。

## 6. 主要结论与发现
- RDD 在 RLBench 上平均成功率 **74.9%**，接近 Expert 的 75.1%，显著优于 UVD（71.4%）和 Uniform（71.3%），且方差更低。
- RDD 对视觉编码器选择鲁棒，多数编码器（LIV、R3M、CLIP、DINOv2、ResNet）均优于 UVD。
- 在真实世界任务（AgiBotWorld）上，RDD 的 mIoU 为 0.706，UVD 仅 0.506；OOD 场景下 RDD（\(\beta=0.1\)）达 0.630，UVD 0.598。
- 少量演示（1 个即可）即可取得优于 UVD 的效果，数据效率高。
- 对比商用 VLM（Gemini-2.5-pro），RDD 表现更好，表明领域对齐的重要性。
- 动态规划算法在子任务时长有上界时呈线性复杂度，可扩展到大规模数据。

## 7. 优点
- **方法创新**：首次将高层次规划器与低层次策略协调问题形式化为基于检索的最优划分问题，自动生成与策略训练集对齐的子任务，无需人工标注或启发式规则。
- **即插即用**：免训练，仅利用现有视觉编码器和 ANNS，可直接应用于任何层级 VLA 框架。
- **鲁棒性**：在多种视觉编码器、不同任务、真实世界及 OOD 场景下均表现稳定，且参数敏感度低。
- **可扩展性**：DP 算法高效，支持大规模数据库（如 10M 条目的 FAISS 检索仅需 115 秒处理 500 帧视频）。
- **理论完整性**：给出最优性原理证明、复杂度分析，并设计处理 OOD 子任务的扩展。

## 8. 不足与局限
- **实验覆盖**：主要基于 RLBench 和少量真实场景，未在更多样化平台（如大门类、灵巧手）验证；仅测试单种底层策略（RVT），需更多策略验证泛化性。
- **数据质量依赖**：RDD 的性能受底层策略训练集 \(\mathcal{D}_{\text{train}}^{\text{aug}}\) 质量影响。若训练集中存在噪声或低质量子任务，对齐可能导致规划器学习错误模式。论文提及可结合数据集筛选方法（如 CUPID），但未集成实验。
- **相似度定义局限**：区间表示仅基于起始帧和结束帧图像，可能丢失中间动态信息，对于需要时序建模的子任务（如连续推操作）可能不够鲁棒。
- **OOD 处理启发式**：OOD 场景下依赖 UVD 作为通用启发式，引入超参数 \(\beta\)，易受 UVD 本身缺陷影响，且未在真实 OOD 任务上评估最终任务成功率（仅用 mIoU）。
- **未见端到端迁移实验**：RDD 生成的子任务标签是否可直接用于底层策略的再训练（如扩大 skill 库）仅作为未来工作提及，未实验验证。

（完）
```
