---
title: "Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning"
title_zh: 迈向可靠的代码即策略：用于具身任务规划的神经符号框架
authors: "Sanghyun Ahn, Wonje Choi, Junyong Lee, Jinwoo Park, Honguk Woo"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=VaC4sa96EI"
tags: ["query:vla"]
score: 7.0
evidence: 提出神经符号框架，将LLM代码生成与符号验证结合用于具身任务规划
tldr: 基于LLM的代码作为策略方法在动态环境中因缺乏环境基础而生成不完整代码。本文提出神经符号框架，在代码生成过程中引入显式符号验证和交互验证，生成探索性代码以纠正错误。实验表明该方法在部分可观测场景下任务成功率显著提升。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1442, \"height\": 618, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1419, \"height\": 535, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1430, \"height\": 325, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 438, \"height\": 259, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1434, \"height\": 668, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1404, \"height\": 466, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1162, \"height\": 634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1287, \"height\": 634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1391, \"height\": 1892, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vac4sa96ei/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1419, \"height\": 2022, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1446, \"height\": 449, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1430, \"height\": 1143, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1430, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 938, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 895, \"height\": 287, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 528, \"height\": 290, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1457, \"height\": 378, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vac4sa96ei/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1454, \"height\": 378, \"label\": \"Table\"}]"
motivation: LLM生成的代码作为策略在动态环境下缺乏环境基础，导致失败率上升。
method: 在代码生成中加入符号验证循环和交互式探索验证。
result: 在部分可观测场景下任务成功率显著优于纯LLM方法。
conclusion: 神经符号验证能有效增强LLM规划代码的可靠性。
---

## Abstract
Recent advances in large language models (LLMs) have enabled the automatic generation of executable code for task planning and control in embodied agents such as robots, demonstrating the potential of LLM-based embodied intelligence. However, these LLM-based code-as-policies approaches often suffer from limited environmental grounding, particularly in dynamic or partially observable settings, leading to suboptimal task success rates due to incorrect or incomplete code generation. In this work, we propose a neuro-symbolic embodied task planning framework that incorporates explicit symbolic verification and interactive validation processes during code generation. In the validation phase, the framework generates exploratory code that actively interacts with the environment to acquire missing observations while preserving task-relevant states. This integrated process enhances the grounding of generated code, resulting in improved task reliability and success rates in complex environments. We evaluate our framework on RLBench and in real-world settings across dynamic, partially observable scenarios. Experimental results demonstrate that our framework improves task success rates by 46.2\% over Code as Policies baselines and attains over 86.8\% executability of task-relevant actions, thereby enhancing the reliability of task planning in dynamic environments.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **研究动机**：基于大型语言模型（LLM）的“代码即策略”（Code-as-Policies）方法在具身智能任务规划中展现出潜力，但在动态或部分可观测环境下，由于缺乏对环境状态的充分感知，生成的代码往往不完整或错误，导致任务成功率低。
- **核心问题**：如何让 LLM 生成的机器人控制代码在不确定性环境中具有可靠的环境基础（grounding），避免因缺失观测而执行不可逆的失败动作。
- **整体含义**：提出一种神经符号（Neuro-Symbolic）框架，通过显式的符号验证和交互式校验过程，主动探索环境、获取缺失信息，从而提升代码执行的可靠性与任务成功率。

### 2. 提出的方法论
- **核心思想**：借鉴软件工程中的“验证与校验”（Verification & Validation）原则，在 LLM 代码生成过程中引入两个递归执行的阶段：
  1. **神经符号代码验证（Neuro-symbolic Code Verification）**：使用 LLM 生成任务规范 `T_spec` 和策略代码 `π_main`，然后通过符号求解器（如 Z3 SMT）静态检查代码是否满足规范。若失败，将反馈信息输给 LLM 迭代修正，直到通过验证。
  2. **神经符号代码校验（Neuro-symbolic Code Validation）**：对验证通过后的策略代码中的每个技能 `f_n` 逐步骤评估其环境可行性。定义一个神经符号置信度 `NeSyConf = CSC × LC`：
     - **常识置信度 (CSC)**：由校验 LLM 基于当前观测、领域知识和演示示例评估技能的成功可能性（通过困惑度归一化得到）。
     - **逻辑置信度 (LC)**：由符号校验工具（如 PDDL 规划器 Fast Downward）检查技能的前提条件是否在当前观测下成立，成立则 LC=1，否则 LC=0。
   - 当 `NeSyConf` 低于阈值 `ε` 时，系统生成**安全探测策略代码** `π_probe`，该代码会执行安全的探索动作（如调整视角、检查抽屉是否锁住、打开灯等）以获取缺失观测。
   - `π_probe` 同样经过验证和校验的递归流程，确保其安全性后再执行。执行后更新观测，然后重启原策略代码的校验过程，更新该技能片段。
   - 递归过程直到所有技能都通过校验，最终输出完全环境基础化的策略代码。
- **关键流程**：LLM 生成 → 符号验证 → 逐技能校验 → 若置信度低则生成探测代码 → 递归验证/校验探测代码 → 执行探测更新观测 → 重新生成/修正原技能 → 重复直至全部通过 → 执行主策略。

### 3. 实验设计
- **数据集/场景**：
  - **RLBench 模拟器**：使用 Franka Emika Panda 机器人，包含 7 个随机摆放的物体（西红柿、垃圾桶、三层抽屉等）。设置四种可观测性水平：高不完备（High）、低不完备（Low）、随机不完备（Stochastic）、完全（Complete）。
  - **真实世界**：7-DoF Franka Research 3 机器人，Intel RealSense D435 相机，10 个物体（骰子、垃圾、抽屉等）。同样按四种任务类型和部分可观测设置测试。
- **任务类型**：对象重定位、对象交互、辅助操作、长时任务（Long-Horizon）。
- **对比基线**：Code as Policies (CaP)、CaP w/ Lemur (SMT 验证)、CaP w/ CodeSift (多阶段语法语义校验)、LLM-Planner (执行感知重规划)、AutoGen (多智能体协作)。
- **评估指标**：成功率（SR）、目标条件完成度（GC）、不可逆动作次数（IA，仅真实世界）。

### 4. 资源与算力
- 文中**未明确给出训练时长或精确 GPU 数**，但描述了计算资源：
  - 本地机器：Intel Core i7-9700KF CPU，NVIDIA GeForce RTX 4080 GPU（16GB VRAM），RLBench 仿真使用最多 32GB 系统内存。符号验证和 PDDL 规划在 CPU 运行。
  - 对于更大模型（如 Llama-3.1-8B、Qwen3-30B-A3B），使用云 CUDA 集群，配备约 82GB VRAM 的 GPU。
  - 所有 OpenAI 模型（GPT-4o-mini 等）通过 API 调用。
- 结论：算力消耗适中，局部实验单 GPU 可完成，大模型依赖云端或 API。

### 5. 实验数量与充分性
- **实验组数**：
  - 模拟实验（表2）：4 种任务类型 × 4 种可观测水平 × 10 次随机试验 = 160 组，每个条件给出均值和标准差。
  - 真实世界实验（表3）：4 种任务类型 × 2 种可观测水平（高/低平均） × 多次试验 + NESYRO-Complete 条件，总约 40+ 次。
  - 消融实验（表4-6）：不同 LLM 类型、是否包含 LC/CSC、不同 CSC 模型规模，均基于长时任务在部分可观测下进行，每组多次重复。
  - 额外分析了编译错误率（图4）。
- **充分性**：实验覆盖模拟和真实场景、多基线、多任务、多可观测程度，包含消融和鲁棒性分析，统计误差带报告充分，结论可信。但未覆盖所有可能的任务类型（如移动操作、复杂装配），可能存在一定偏差。

### 6. 主要结论与发现
- NESYRO 在部分可观测条件下，平均任务成功率相比最佳基线（AutoGen 和 CaP w/ CodeSift）提升 26.3%（模拟）和 47.0%（真实世界），GC 提升 24.3%（模拟）和 42.6%（真实世界）。
- 在完全可观测条件下，NESYRO 性能与基线相当或略优，不影响全观测性能。
- 在真实世界中，NESYRO 将不可逆动作数从基线的 29 次降低至 7 次，体现了安全探索的优势。
- 消融实验表明，同时保留常识置信度 (CSC) 和逻辑置信度 (LC) 至关重要，任一缺失都会导致显著性能下降（SR 平均降低 21.2%）。
- CSC 的计算对 LLM 规模相对鲁棒，3B 以上模型即能达到稳定效果。
- 更强 LLM（如 o3）在所有方法上提升性能，但 NESYRO 始终优于对应 CaP，且更接近 NESYRO-Complete 上界。

### 7. 优点
- **方法创新**：将软件工程中经典的验证与校验（V&V）范式引入 LLM 生成的机器人代码，构建递归的神经符号闭环。
- **安全探索**：通过主动生成安全探测代码来获取缺失观测，避免直接执行可能造成不可逆损坏的动作，提升实际部署安全性。
- **可解释性与鲁棒性**：符号工具提供清晰的逻辑检查和反馈，LLM 辅助的常识评估提供柔性可行性估计，二者互补。
- **实验全面**：在模拟和真实环境中均进行了多任务、多可观测水平、多基线的系统评估，消融实验充分。
- **实用性强**：不要求预定义所有可能环境状态，通过递归探索自适应地补齐信息，适用于动态、部分可观测场景。

### 8. 不足与局限
- **逻辑置信度（LC）的局限性**：当前为二元（0/1），忽略概率性可行性（如抓手夹取可能存在概率失败），论文提及未来可引入概率 PDDL。
- **领域知识依赖**：需要预定义技能的前提条件和效果（PDDL 形式），这限制了向完全未知任务或全新操作原语的泛化。
- **真实世界辅助操作任务执行上限低**：如开灯等物理交互精度不足，导致即使感知和规划正确，实际成功率仍受底层执行能力限制（NESYRO-Complete 在该任务上也仅 20% SR）。
- **计算开销**：递归验证-校验过程可能多次调用 LLM 和符号工具，在长时任务中延迟较大（未量化报告）。
- **未见更多复杂场景测试**：仅测试了桌面式操作环境，未验证在动态人类环境、非结构化家庭场景中的表现。

（完）
