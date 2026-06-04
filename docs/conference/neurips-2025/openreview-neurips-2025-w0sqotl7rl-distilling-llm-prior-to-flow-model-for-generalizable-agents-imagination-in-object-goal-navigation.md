---
title: Distilling LLM Prior to Flow Model for Generalizable Agent’s Imagination in Object Goal Navigation
title_zh: 将LLM先验蒸馏到流模型以实现泛化的目标导航智能体想象
authors: "Badi Li, Ren-Jie Lu, Yu Zhou, Jingke Meng, Wei-Shi Zheng"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=W0sqoTL7rL"
tags: ["query:vla"]
score: 4.0
evidence: 将LLM先验蒸馏到流模型用于目标导航
tldr: 目标导航中现有方法难以泛化到未知环境，因为确定性语义补全忽略了布局不确定性。GOAL提出生成式流框架，利用LLM先验概率场注入到语义地图中，在随机采样中完成场景想象。实验表明该方法在多种未知环境中显著优于判别式方法，体现了LLM知识与生成模型的结合价值。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1312, \"height\": 490, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1458, \"height\": 830, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1439, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 558, \"height\": 224, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1475, \"height\": 450, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 640, \"height\": 511, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1435, \"height\": 1157, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1127, \"height\": 396, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1123, \"height\": 1213, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1339, \"height\": 495, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-w0sqotl7rl/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1126, \"height\": 1246, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1239, \"height\": 490, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 644, \"height\": 275, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1455, \"height\": 238, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 712, \"height\": 431, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 764, \"height\": 266, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1405, \"height\": 727, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1403, \"height\": 422, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-w0sqotl7rl/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 577, \"height\": 305, \"label\": \"Table\"}]"
motivation: 现有语义地图补全方法忽视不确定性，导致泛化能力弱。
method: 提出GOAL框架，利用LLM先验编码为高斯场注入流模型以生成语义分布。
result: 在未知环境目标导航任务中，GOAL显著提升成功率，优于判别式方法。
conclusion: 生成式模型与LLM先验的结合有效提升导航泛化能力。
---

## Abstract
The Object Goal Navigation (ObjectNav) task challenges agents to locate a specified object in an unseen environment by imagining unobserved regions of the scene. Prior approaches rely on deterministic and discriminative models to complete semantic maps, overlooking the inherent uncertainty in indoor layouts and limiting their ability to generalize to unseen environments. In this work, we propose GOAL, a generative flow-based framework that models the semantic distribution of indoor environments by bridging observed regions with LLM-enriched full-scene semantic maps. During training, spatial priors inferred from large language models (LLMs) are encoded as two-dimensional Gaussian fields and injected into target maps, distilling rich contextual knowledge into the flow model and enabling more generalizable completions. Extensive experiments demonstrate that GOAL achieves state-of-the-art performance on MP3D and Gibson, and shows strong generalization in transfer settings to HM3D.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

*   **研究动机**：Object Goal Navigation (ObjectNav) 任务要求智能体在未知环境中通过想象未观测区域来定位指定物体。现有方法大多采用**确定性判别模型**进行语义地图补全（如预测完整地图），忽略了室内布局的**内在不确定性**，导致其对未知环境的**泛化能力有限**。
*   **核心问题**：面对部分观测的语义地图，可能存在多种合理的完整场景语义分布，而确定性模型只能输出单一结果，限制了多样性。
*   **整体含义**：本文提出**生成式建模**思路，认为智能体的“想象”应当是一个概率生成过程，并引入**大语言模型 (LLM) 的外部常识知识**来增强生成能力，使模型在未见过的环境中也能产生合理且多样的语义分布，从而提升导航泛化性能。

### 2. 论文提出的方法论

*   **核心思想**：采用**流匹配 (Flow Matching)** 生成式框架，通过构建**数据依赖耦合 (data-dependent couplings)**，将部分观测地图直接与 LLM 增强的完整地图关联，避免传统扩散模型中复杂的条件机制。同时，将 LLM 提供的物体共现先验**蒸馏**为二维高斯场，注入训练过程中的目标地图，提升生成质量。
*   **关键技术细节**：
    1.  **LLM 先验提取**：利用 Chain-of-Thought、角色设定等提示技术，让 LLM 输出物体对之间的典型距离和置信度，形成距离矩阵 D 和置信度矩阵 C。
    2.  **高斯先验构建**：对于部分观测地图中的每个物体，根据阈值选择共现候选物体，将其预测位置（沿物体到最近前沿方向）建模为各向同性二维高斯分布，叠加得到 LLM 先验图 p_LLM。
    3.  **数据依赖耦合**：源样本 X0 由可见区域（γ）的完整地图加上不可见区域的高斯噪声构成；目标样本 X1 由完整地图加上 LLM 先验（仅不可见区域）构成。两者共享相同的可见性掩码 γ，形成强结构化耦合。
    4.  **训练**：使用线性插值 X_t = (1-t)X0 + tX1，以 MSE 损失学习预测速度场 u_θ，梯度由 X1 - X0 提供。
    5.  **语义地图构建**：采用**3D场景分割**（基于稀疏卷积网络）将累积的点云投影到鸟瞰图，替代传统的单帧 2D 语义分割，获得更一致、更准确的场景理解。
*   **算法流程**：训练时，从完整地图中采样部分可见路径，构建 X0 和 X1，计算 LLM 先验并加入 X1，然后进行流匹配训练。推理时，将当前局部地图作为 X0，通过迭代欧拉积分生成完整地图，选取目标通道中最大值点作为长期航点。

### 3. 实验设计

*   **数据集与场景**：
    *   训练与主评测：**Gibson** (tiny-split，25训练/5验证场景，6个目标类别，1000验证episode)、**MP3D** (56训练/11验证场景，21个目标类别，2195验证episode)。
    *   迁移评测：**HM3D** (20验证场景，6个目标类别，2000验证episode)，仅作为目标域，训练在 MP3D 上。
*   **Benchmark 对比方法**：
    *   传统模块化方法：SemExp、PONI、L2M、SSC-Nav、Stubborn、3DAware、CoW、T-Diff、SGM 等。
    *   LLM 辅助方法：L3MVN、SG-Nav、UniGoal。
    *   零样本方法：ZSON、PixNav、ESC、VoroNav。
*   **评估指标**：Success Rate (SR)、Success weighted by Path Length (SPL)、Distance To Goal (DTS)。

### 4. 资源与算力

*   **GOAL 流模型训练**：4 张 NVIDIA RTX 4090 GPU，每张 batch size 64，训练 25 个 epoch。
*   **场景分割模型训练**：2 张 NVIDIA RTX 4090 GPU，总 batch size 64。
*   **推理（导航中）**：在 6 线程并行设置下，GOAL 的平均 FPS 为 1.2-1.8，内存开销约为每线程 350MB（相比 PONI 的 20GB 总内存略增）。

### 5. 实验数量与充分性

*   **实验数量**：包括主实验（Gibson、MP3D 上的最终对比）、跨域迁移实验（MP3D→HM3D）、多种消融实验（场景分割、LLM 先验、不同 LLM 版本、模型大小、数据依赖 vs 独立耦合、Flow Matching vs MAE 等）、超参数调优（欧拉步数 n、扩展比例 ϵ）以及多次随机种子评估。
*   **充分性与客观性**：
    *   **充分性**：消融实验逐一验证了各个核心组件的贡献（场景分割单独提升 6.4% SR，加 LLM 先验再提升 2.9% SR）；对比了不同 LLM（ChatGLM、DeepSeek、GPT-4）和模型规模（DiT-B vs DiT-L）；验证了生成多样性（图10）。
    *   **客观性**：迁移设置公平（训练集固定，目标域完全不参与训练）；与 SOTA 方法的比较引用官方实现或报告结果；多次随机种子（5个种子）报告了平均 41.6%±0.4% 的 SR，表明结果稳定。
    *   但作者也承认，当前评测数据集规模较小且存在偏差，可能无法充分体现不同 LLM 的差异（表4中各 LLM 性能接近）。

### 6. 论文的主要结论与发现

1.  **生成式建模优于确定性建模**：Flow Matching 框架与 LLM 先验结合，在多个数据集上取得 SOTA 结果（Gibson SR 83.5，MP3D SR 41.7，HM3D 迁移 SR 48.8）。
2.  **数据依赖耦合高效**：直接耦合部分地图与目标地图，避免了额外条件机制，降低了模型复杂度和推理时间（表2：GFLOPs 从 29.34 降至 24.12，速度提升 38%）。
3.  **LLM 先验蒸馏有效**：尽管场景分割已建立强基线，加入 LLM 先验仍能带来显著增益（MP3D SR 从 38.8 升至 41.7）。
4.  **3D 场景分割提高理解一致性**：相比单帧 2D 分割，3D 点云分割减少了地图构建误差。
5.  **跨域泛化能力强**：在训练集 MP3D 上训练后，直接迁移到 HM3D 超过所有对比方法（包括在 HM3D 上训练的方法），证明了生成式模型和外部知识的泛化价值。

### 7. 优点

*   **方法创新性**：首次将流匹配生成模型应用于 ObjectNav，并巧妙地将 LLM 先验以高斯场形式嵌入训练过程，避免了推理时调用 API 的开销。
*   **高效性**：采用数据依赖耦合代替传统独立耦合，简化了网络结构，降低了计算成本和推理延迟。
*   **鲁棒性**：使用 3D 场景分割替代 2D 分割，提升了地图构建的时空一致性，减少累积误差。
*   **泛化能力**：跨域迁移实验表明，即使没有 LLM 先验，生成式模型本身也优于判别式模型，加 LLM 后更强。
*   **实验严谨性**：多次随机种子、超参数调优、消融分析齐全，结果可靠。

### 8. 不足与局限

*   **训练数据模拟偏差**：使用路径规划模拟可见区域（矩形掩码），与真实导航时的扇形视野存在较大差距，可能导致训练和推理不匹配（图4）。
*   **固定类别限制**：语义地图通道对应固定类别集合，无法处理零样本或开放词汇的新物体，限制了实际部署灵活性。
*   **模型复杂度与样本效率**：增大模型规模（DiT-L 相比 DiT-B）并未带来性能提升，反而可能过拟合，表明当前数据集规模有限时需谨慎选择模型容量。
*   **NFE 与实时性折衷**：欧拉步数 n 越大效果越好（饱和于 96 步），但增加推理开销；作者指出可通过最新蒸馏技术加速，但本文未涉及。
*   **LLM 先验依赖提示质量**：不同 LLM 的响应差异虽小，但提示工程可能影响结果，且当前基准无法清晰反映其效果差异。

（完）
