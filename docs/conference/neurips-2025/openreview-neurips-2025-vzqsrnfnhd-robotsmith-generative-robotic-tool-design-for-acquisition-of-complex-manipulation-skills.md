---
title: "RobotSmith: Generative Robotic Tool Design for Acquisition of Complex Manipulation Skills"
title_zh: RobotSmith：用于获取复杂操作技能的生成式机器人工具设计
authors: "Chunru Lin, Haotian Yuan, Yian Wang, Xiaowen Qiu, Tsun-Hsuan Wang, Minghao Guo, Bohan Wang, Yashraj Narang, Dieter Fox, Chuang Gan"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=VZQSrNfNHd"
tags: ["query:vla"]
score: 7.0
evidence: 用于机器人操作技能的生成式工具设计
tldr: RobotSmith提出自动化工具设计流水线，使机器人能够自主生成针对复杂操作任务的工具（如适应机械手的擀面杖），解决了现有方法依赖预先模板或通用3D生成不优化的问题。通过迭代优化工具形状和抓取策略，机器人能执行原本不可解的任务，显著扩展了操作能力边界。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1440, \"height\": 509, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1447, \"height\": 672, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1432, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 865, \"height\": 493, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1311, \"height\": 297, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1444, \"height\": 740, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1476, \"height\": 852, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1449, \"height\": 1116, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-vzqsrnfnhd/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1017, \"height\": 611, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-vzqsrnfnhd/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1462, \"height\": 510, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-vzqsrnfnhd/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 960, \"height\": 243, \"label\": \"Table\"}]"
motivation: 现有机器人依赖人类设计工具，但很多工具不适合机器人使用，限制操作能力。
method: 提出自动管线，结合3D生成和物理仿真迭代优化工具形状。
result: 生成的工具使机器人完成原先无法实现的操作任务。
conclusion: 自主工具设计是提升机器人操作泛化性的有效途径。
---

## Abstract
Endowing robots with tool design abilities is critical for enabling them to solve complex manipulation tasks that would otherwise be intractable. While recent generative frameworks can automatically synthesize task settings—such as 3D scenes and reward functions—they have not yet addressed the challenge of tool-use scenarios. Simply retrieving human-designed tools might not be ideal since many tools (e.g., a rolling pin) are difficult for robotic manipulators to handle. Furthermore, existing tool design approaches either rely on predefined templates with limited parameter tuning or apply generic 3D generation methods that are not optimized for tool creation.
To address these limitations, we propose **RobotSmith**, an automated pipeline that leverages the implicit physical knowledge embedded in vision-language models (VLMs) alongside the more accurate physics provided by physics simulations to design and use tools for robotic manipulation. Our system (1) iteratively proposes tool designs using collaborative VLM agents, (2) generates low-level robot trajectories for tool use, and (3) jointly optimizes tool geometry and usage for task performance.
We evaluate our approach across a wide range of manipulation tasks involving rigid, deformable, and fluid objects. Experiments show that our method consistently outperforms strong baselines in both task success rate and overall performance. Notably, our approach achieves a 50.0\% average success rate, significantly surpassing other baselines such as 3D generation (21.4\%) and tool retrieval (11.1\%). Finally, we deploy our system in real-world settings, demonstrating that the generated tools and their usage plans transfer effectively to physical execution, validating the practicality and generalization capabilities of our approach.

---

## 论文详细总结（自动生成）

# RobotSmith：用于获取复杂操作技能的生成式机器人工具设计 —— 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：机器人要执行复杂操作任务（如擀面团、倒水、切割）通常需要专用工具，但现有方法要么依赖人类设计的工具（不适合机器人操作，如擀面杖对机械臂来说难以抓握和控制），要么使用预设模板（仅优化有限参数，泛化性差），要么采用通用3D生成模型（缺乏功能导向，生成的工具视觉逼真但实际不可用）。
- **研究动机**：机器人需要具备**自主设计工具**的能力，根据具体任务和机器人形态定制工具，从而解锁原本无法完成的操作。现有生成式流水线（如生成3D场景、奖励函数）未覆盖工具设计场景。因此，论文提出将**大模型的常识物理知识**（如空间推理、功能感知）与**物理仿真**的精确反馈相结合，实现自动化的工具设计与使用规划。

## 2. 方法论：核心思想、关键技术细节、算法流程

### 核心思想
RobotSmith是一个全自动流水线，包含三个核心模块：
1. **批评式工具设计器（Critic Tool Designer）**：两个VLM智能体（Proposer和Critic）基于视觉上下文和任务描述，通过多轮迭代建议/反馈来生成工具几何。
2. **工具使用规划器（Tool Use Planner）**：基于设计好的工具和场景，生成高层机器人轨迹（使用三个API：grasp、move、release）。
3. **联合优化器（Joint Optimizer）**：通过物理仿真的任务反馈，联合微调工具几何参数和轨迹参数。

### 关键技术细节
- **工具表示**：采用模块化、参数化表示。每个工具由多个部件组成，每个部件可以是基本几何体（立方体、球、圆柱、环、管）或由文本到3D模型生成的复杂形状。通过装配函数（类似CSG树）定义部件间的空间关系和连接，支持独立缩放、旋转、平移而不破坏结构连贯性。
- **Critic Tool Designer流程**：
  - Proposer接收任务描述和场景配置，输出工具设计（JSON格式），并渲染多视角图像。
  - Critic根据任务约束和设计原则（如所有部件连接、可抓握、足够长避免接触水等）提供反馈。
  - Proposer根据反馈修改设计，循环直到Critic返回“Done”。
- **Tool Use Planner**：使用三个高层API表示轨迹：`grasp(obj, euler)`（采样抓取位姿）、`move(pos, euler)`（运动规划）、`release()`。初始轨迹由LLM代理生成。
- **Joint Optimizer**：使用CMA-ES进化策略，同时优化工具形状参数（如尺寸）和轨迹参数（位置、姿态）。每个参数在初始值的一定范围内变化（形状±50%，平移±0.2m，旋转±π）。每轮采样20个候选解，执行50次迭代。目标函数是任务特定的奖励（由仿真计算）。
- **任务目标函数**：每个任务定义了归一化评分M∈[0,1]，成功定义为评分>0.8。

## 3. 实验设计

### 任务与场景
- 共**9个**机器人操作任务，涵盖刚体、可变形体、流体：
  1. **Reach**：到达工作区外的立方体
  2. **Hold a Phone**：保持手机直立
  3. **Lift a Bowl**：提起大碗（不触碰内表面）
  4. **Lift a Piggy**：提起存钱罐
  5. **Dough Calabash**：使面团成葫芦形
  6. **Flatten Dough**：将面团擀平至高度<0.03
  7. **Cut Dough**：将面团切成均匀两半
  8. **Fill a Bottle**：将水倒入窄口瓶子
  9. **Transport Water**：将水从水箱运到杯子中

### 基准方法
- **No Tool**：仅用末端执行器，LLM生成轨迹+CMA-ES优化
- **Retrieval**：从BlenderKit按语义相似性检索工具，LLM轨迹+优化
- **3D Generation (Meshy)**：使用Meshy文本到3D生成工具，LLM轨迹+优化
- **3D Editing (ShapeTalk)**：使用ShapeTalk进行自然语言驱动的3D编辑迭代，LLM轨迹+优化

### 评估指标
- 每项实验运行**8次**，报告：
  - **P_best**：最佳归一化得分
  - **SR**：成功率（P > 0.8的比例）

## 4. 资源与算力

- **硬件**：使用NVIDIA GeForce RTX 4090 和 RTX 2080 Ti GPU（单卡运行）。
- 大模型部分（O3-Mini、Meshy）通过API调用，不消耗本地算力。
- 仿真优化（CMA-ES+Genesis仿真器）支持CPU或GPU加速，单次优化约50轮×20采样=1000次仿真，具体时间与任务复杂度有关，但论文称许多实验可在单张2080 Ti上完成。

## 5. 实验数量与充分性

- 共**9个任务**×4种方法（No Tool/Retrieval/Meshy/Ours）=36组主要实验，每方法8个随机种子，合计288次仿真运行。
- 额外进行了**消融实验**（4种设置：去掉文本到3D、去掉优化器、去掉工具几何优化、完整系统），每种设置也覆盖9个任务，报告平均P_best和SR。
- **真实世界实验**：将Hold a Phone和Dough Calabash任务设计的工具3D打印，在XArm7机器人上执行；另外进行了长期任务（做芝麻饼）的端到端演示。
- **充分性与公平性**：对比方法覆盖了无工具、检索、生成、编辑等多种范式，优化过程统一使用CMA-ES和相同初始轨迹生成策略（LLM）。但论文未进行随机种子对CMA-ES稳定性的敏感性分析，也未提供置信区间。

## 6. 论文的主要结论与发现

- **性能优势**：RobotSmith在平均成功率（50.0%）上显著优于Meshy（21.4%）、Retrieval（11.1%）、No Tool（2.8%）。
- **消融实验**：去除任何组件都会导致性能大幅下降，其中去除轨迹优化影响最大（成功率从50%降至5%），说明联合优化至关重要。
- **工具多样性**：框架可为同一任务生成多种有效工具（如不同形状的铲、压板）。
- **真实世界可行性**：3D打印工具可在物理机器人上成功执行任务，证明设计的可行性和迁移性。
- **长期任务**：机器人能自主设计多个工具并协调完成多步骤操作（做芝麻饼：压面、舀酱、抹酱、撒芝麻）。

## 7. 优点

- **创新性**：首次将VLM的语义常识与物理仿真优化结合，实现完全自动的工具设计与使用规划，无需人类预定义模板。
- **模块化工具表示**：支持参数化微调，兼顾灵活性和结构有效性（CSG式装配保证物理连接）。
- **双智能体迭代设计**：Critic提供结构化反馈（如连接性、可抓握性），使设计过程可控、可解释。
- **联合优化**：同时优化形状和轨迹，解决了单独优化可能造成的功能不匹配（如工具合适但轨迹错误）。
- **实验全面**：覆盖刚/柔/流体任务，仿真+真实验证，并包含长期任务。
- **开源承诺**：将公开代码和API，促进可重复性。

## 8. 不足与局限

- **优化范围有限**：当前CMA-ES仅支持缩放、旋转、平移，无法进行拓扑变化（如增加/删除部件、改变部件连接方式），限制了工具的结构创新。
- **设计与生成不匹配**：Proposer可能指定一个复杂部件，但Meshy生成的网格尺寸、朝向不可控，导致实际工具与设计意图偏离（如漏斗管道过多）。
- **抓取失败**：抓取API在工具过重或运动剧烈时容易失败，尤其在仿真中未充分鲁棒。
- **轨迹细化不足**：初始轨迹常包含模糊方向（如“翻转90°”），优化器可能无法收敛到精确解，尤其在长轨迹任务中。
- **实验局限性**：未进行跨不同机器人平台（如不同爪手类型、臂长）的泛化测试；真实实验仅验证了两个任务；未分析VLM错误预测（如不合理反馈）带来的风险。
- **依赖大模型**：性能受限于所用VLMs（o3-mini）和文本到3D模型（Meshy）的质量，这些模型本身可能存在偏差或知识缺陷。
- **计算成本**：虽然未详细报告时间，但每任务50次迭代×20采样意味着至少1000次仿真评分，加上VLM多轮对话的API调用成本，整体效率有待提升。

（完）
