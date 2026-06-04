---
title: "UniDomain: Pretraining a Unified PDDL Domain from Real-World Demonstrations for Generalizable Robot Task Planning"
title_zh: "UniDomain: 从真实世界演示预训练统一PDDL领域用于泛化机器人任务规划"
authors: "Haoming Ye, Yunxiao Xiao, Cewu Lu, Panpan Cai"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=hVYp0WzyLK"
tags: ["query:vla"]
score: 5.0
evidence: 从演示中预训练机器人任务规划
tldr: 机器人任务规划常依赖手工设计的领域知识，缺乏泛化性。UniDomain从大量真实操作视频中自动提取并统一PDDL领域，构建了包含数千操作符和谓词的大规模领域。在线规划时，系统检索相关原子领域并推理出动作序列，显著提升了跨任务规划的泛化能力。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1429, \"height\": 584, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1434, \"height\": 810, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1399, \"height\": 482, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1411, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 801, \"height\": 372, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1306, \"height\": 956, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1299, \"height\": 873, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 659, \"height\": 502, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 659, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 660, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 659, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 660, \"height\": 501, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 659, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 659, \"height\": 500, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1436, \"height\": 970, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 728, \"height\": 734, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 982, \"height\": 531, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-018.webp\", \"caption\": \"\", \"page\": 0, \"index\": 18, \"width\": 1441, \"height\": 1251, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-019.webp\", \"caption\": \"\", \"page\": 0, \"index\": 19, \"width\": 1451, \"height\": 207, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-hvyp0wzylk/fig-020.webp\", \"caption\": \"\", \"page\": 0, \"index\": 20, \"width\": 1391, \"height\": 741, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1472, \"height\": 535, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1468, \"height\": 902, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1474, \"height\": 367, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1455, \"height\": 69, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1463, \"height\": 144, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1470, \"height\": 180, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1481, \"height\": 546, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1471, \"height\": 251, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1454, \"height\": 140, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1466, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1469, \"height\": 279, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1449, \"height\": 1742, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-hvyp0wzylk/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 1449, \"height\": 1777, \"label\": \"Table\"}]"
motivation: LLM规划依赖手工领域，难以泛化。
method: 从操作视频预训练统一PDDL领域。
result: 构建包含大量操作符的领域，支持在线规划。
conclusion: 数据驱动领域学习可提升机器人规划泛化性。
---

## Abstract
Robotic task planning in real-world environments requires reasoning over implicit constraints from language and vision. While LLMs and VLMs offer strong priors, they struggle with long-horizon structure and symbolic grounding. Existing meth-
ods that combine LLMs with symbolic planning often rely on handcrafted or narrow domains, limiting generalization. We propose UniDomain, a framework that pre-trains a PDDL domain from robot manipulation demonstrations and applies it for online robotic task planning. It extracts atomic domains from 12,393 manipulation videos to form a unified domain with 3137 operators, 2875 predicates, and 16481 causal edges. Given a target class of tasks, it retrieves relevant atomics from the unified domain and systematically fuses them into high-quality meta-domains for zero-shot planning. Experiments on diverse real-world tasks show that UniDomain solves complex, unseen tasks in a zero-shot manner, achieving up to 58% higher task success and 160% improvement in plan optimality over state-of-the-art LLM and LLM-PDDL baselines.

---

## 论文详细总结（自动生成）

# UniDomain：从真实世界演示预训练统一PDDL领域用于泛化机器人任务规划 —— 深度总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：机器人任务规划需要处理自然语言指令和视觉观察中隐含的复杂约束（如“把堆叠的积木按奇偶顺序升序排列”），现有LLM和VLM虽具备强先验，但难以建模动作前提/效果、生成连贯的长时规划。将LLM与符号规划（PDDL）结合的方法通常依赖手工或窄领域，限制了泛化能力。
- **研究动机**：利用大规模真实机器人操作演示（如DROID数据集）自动学习可复用的PDDL领域知识，使规划器能在未见任务中实现零样本泛化。
- **整体含义**：UniDomain首次提出从大规模真实演示预训练统一PDDL领域，通过数据驱动的领域学习替代手工设计，显著提升任务规划的成功率与最优性。

## 2. 方法论：核心思想、关键技术细节

### 2.1 核心思想
- 将机器人操作演示（视频+语言指令）转化为符号化PDDL原子领域，通过闭式验证确保正确性；再将相关原子领域融合为紧凑、连贯的元领域，支持在线零样本规划。

### 2.2 关键技术细节（三阶段）

#### 阶段一：领域预训练（Domain Pretraining）
- **输入**：DROID数据集中的12,393个真实操作视频及语言指令。
- **关键帧提取**：基于能量法的无监督方法。计算每帧灰度图强度平方和（能量），通过滑动窗口检测局部极值作为关键帧。相比基于CLIP/SigLIP的相似性方法，速度更快（0.6秒 vs 47.8秒），准确率更高。
- **原子领域生成**：
  1. 对每对相邻关键帧，调用VLM（如GPT-4V）推断动作名称、前提和效果，构建初始领域D0。
  2. LLM进行整体修订，确保语法正确、谓词复用和命名一致，得到Dr。
  3. **可满足性检查**：用Dr生成K=5个测试问题，由PDDL规划器求解，若可满足性得分S(Dr)<0.6，则将规划器完整反馈（含搜索日志、验证错误）返回LLM进行领域细化，直至通过。
  4. **求解验证**：对最难测试问题的规划结果，由LLM检查是否符合物理常识（如不能抓取被遮挡物体、不能堆叠到自身），若发现违规则反馈给LLM进一步细化。
  5. 重复上述嵌套检查最多L=5次，若仍未收敛则丢弃该原子领域。
- **统一领域**：将12,393个原子领域取并集（直接覆盖重叠节点），形成包含3,137个操作符（170个语义类别）、2,875个谓词、16,481条因果边的大规模符号知识图。

#### 阶段二：领域融合（Domain Fusion）
- **检索**：基于语言指令相似性或LLM推断，检索与目标任务类相关的原子领域子集（实验中40个）。
- **二叉树融合**：
  - 将检索到的原子领域任意配对，沿二叉树自底向上递归融合。
  - 每次融合分两步：
    - **谓词合并**：使用MPNet嵌入计算余弦相似度，保留阈值τp=0.3以上的候选对，再经LLM验证语义等价，合并等价谓词。
    - **操作符合并**：更新所有引用合并谓词的操作符，通过操作符名称嵌入相似度（阈值τo=0.3）筛选候选对，LLM判断功能等价性后合并，继承前提与效果的并集。
- 最终生成紧凑的元领域（实验中含78个谓词、61个操作符、332条因果边）。

#### 阶段三：在线规划（Online Planning）
- **谓词分组**：将元领域中的谓词预分为四类（对象类别、状态属性、空间关系、功能相关），辅助LLM理解。
- **谓词与操作符过滤**：
  1. VLM读入元领域、场景图像和指令，生成初始问题P0，提取其中使用的谓词集P0。
  2. 从元领域操作符中找出前提或效果涉及P0的操作符，构成缩减操作符集O′。
  3. 用O′和P0构建紧凑领域Dnew，再由LLM生成细化问题Pnew。
- **符号规划**：调用Fast Downward规划器求解(Dnew, Pnew)，得到最优动作序列。

## 3. 实验设计

### 3.1 数据集与任务场景
- **预训练数据**：DROID数据集中的12,393个真实操作演示。
- **测试任务**：4个未见任务域，共100个任务实例：
  - **BlockWorld**：积木排序与堆叠（含顺序约束）。
  - **Desktop**：抽屉使用、擦拭、折叠、文件整理。
  - **Kitchen**：物体转移、食物工具操作。
  - **Combination**：混合以上所有域，测试跨上下文泛化。

### 3.2 基准方法
- **LLM/VLM只作为规划器**：
  - Code-as-Policies：直接生成Python式代码计划。
  - ReAct：通过闭环推理提高鲁棒性。
  - VLM-CoT：零样本视觉链式思考。
- **LLM+PDDL混合方法**：
  - ISR-LLM：将指令转PDDL，迭代修正。
  - VLM-PDDL：视觉-语言接地生成PDDL，经典规划器求解。
  - BoN-iVML：Best-of-N采样+言语反馈生成领域。

### 3.3 评估指标
- **成功率（SR）**：计划执行成功比例。
- **成功加权相对路径长度（SPL）**：考虑最优路径长度的成功率加权。
- **最优率（OR）**：计划代价ci在最优c*_i的K阈值内的比例（K=2,1,0）。
- 额外报告**思考时间（LLM运行时间）**和**LLM调用次数**。

### 3.4 实验设置
- 所有LLM方法使用GPT-4.1 API，温度0.0。
- 评估采用半自动：LLM初步评估+人类专家最终验证，假设完美底层控制（人类遥控操作），排除低层感知干扰。

## 4. 资源与算力

- 论文未提供训练统一领域所需的完整GPU型号、数量、总时长等细节。
- 仅在第7.3节消融实验中比较了关键帧提取的计算成本：
  - 能量法：在i7-14700HX CPU（32GB RAM）上单线程平均0.6秒/演示。
  - 相似性法（SigLIP-2）：在NVIDIA A800 GPU（80GB VRAM）上批量并行平均47.8秒/演示。
- 融合及在线规划阶段依赖GPT-4.1 API，未报告具体耗时或成本。

## 5. 实验数量与充分性

- **主要对比实验**：在4个域100个任务上评估9种方法（包括UniDomain及其变体），涵盖三类指标，结果以标准误表示（图3）。
- **消融实验**：
  - **领域学习消融**（图4a）：基于40个演示，比较完整方法 vs 删除LLM修订/可满足性检查/求解验证/所有闭环等变体，以及单次能量法/相似性法，共7组。
  - **领域融合消融**（图4b）：完整方法 vs 无融合（直接检索最近原子领域） vs 无结构化融合（直接LLM合并），每组测试4个指标（语法有效、可满足、求解有效、任务成功）。
  - **规划方法消融**（图5）：完整方法 vs 无语义分组 vs 无过滤，按任务域分别报告成功率。
- **充分性**：实验覆盖了方法核心组件的拆解验证，且对每个变体报告了统计误差；但未进行跨LLM（如换用不同模型）或跨数据集（如其他操作数据集）的进一步泛化测试。总体充分、客观、公平。

## 6. 论文的主要结论与发现

- UniDomain在100个未见任务上达到85%成功率和83%最优率（K=0），显著优于最强基线（ISR-LLM成功率~65%，BoN-iVML最优率~30%）。
- 相比LLM-only方法，成功率提升高达58%；相比LLM-PDDL混合方法，最优性提升高达160%。
- 消融实验证明：闭式验证、结构化融合、谓词分组与过滤是取得优异性能的关键。
- 预训练统一领域的内在语义丰富性（3,137个操作符、16,481条因果边）是实现组成泛化的基础。

## 7. 优点

- **创新性**：首次从大规模真实机器人操作演示中预训练可泛化的PDDL领域，将数据驱动与符号规划结合。
- **自动闭环验证**：通过可满足性检查和求解验证两阶段闭环，无需人工介入即可生成高质量原子领域。
- **结构化解构**：能量法关键帧提取简单高效；二叉树融合有效解决语义不一致问题，生成紧凑元领域。
- **零样本泛化**：无需新任务演示或在线调整，直接应用于未见任务，展现了强大的组成泛化能力。
- **效率**：在线规划阶段通过谓词分组和过滤显著降低符号噪声，减少LLM调用和思考时间。

## 8. 不足与局限

- **表述形式局限**：仅支持PDDL 1.0，缺乏对时间约束、数值函数、代价敏感规划的支持。
- **可观测性假设**：假定完全可观测，未考虑真实世界中的遮挡、感知噪声等挑战。
- **自动检索可能冗余**：自动检索的原子领域可能包含不相关内容，使融合耗时增加且偶有无效冗余。
- **实验限制**：
  - 评估依赖人类遥控作为低层执行，未集成真实机器人系统（虽提供了视频演示）。
  - 仅测试单臂操作，未考虑双臂或移动操作。
  - 消融实验仅在40个演示上进行，未在大规模上验证组件对各种任务影响的稳定性。
- **计算开销**：虽在线部分效率高，但预训练阶段从12K+演示逐一生成原子领域（部分需多次闭式交互）总耗时可能较大，未完整披露。

（完）
