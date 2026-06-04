---
title: "Knowledge Insulating Vision-Language-Action Models: Train Fast, Run Fast, Generalize Better"
title_zh: 知识绝缘的视觉-语言-动作模型：快速训练、快速推理、更好泛化
authors: "Danny Driess, Jost Tobias Springenberg, brian ichter, LILI YU, Adrian Li-Bell, Karl Pertsch, Allen Z. Ren, Homer Walke, Quan Vuong, Lucy Xiaoyang Shi, Sergey Levine"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=cb0xbZ3APM"
tags: ["query:vla"]
score: 9.0
evidence: 具备高效连续控制的视觉-语言-动作模型
tldr: 该论文针对VLA模型在实时控制中面临的大模型推理慢和输出需连续化的问题，提出知识绝缘方法：将VLM的语义知识与动作头分离，保留VLM预训练知识的同时使用轻量连续控制模块。实验表明该方法训练和推理速度显著提升，且泛化到新任务能力强于现有VLA模型。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1442, \"height\": 425, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 872, \"height\": 298, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1426, \"height\": 238, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1436, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1155, \"height\": 520, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 843, \"height\": 424, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1251, \"height\": 496, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 611, \"height\": 352, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 553, \"height\": 356, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-cb0xbz3apm/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 730, \"height\": 510, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-cb0xbz3apm/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 668, \"height\": 256, \"label\": \"Table\"}]"
motivation: 现有VLA模型因使用大型VLM导致实时推理困难，且输出为离散token不适用于连续控制。
method: 将VLM语义知识与连续动作头绝缘，保留预训练知识并采用轻量连续模块。
result: 训练和推理速度大幅提升，在新任务泛化上优于现有VLA。
conclusion: 知识绝缘策略有效平衡了VLA模型的语义能力和实时控制需求。
---

## Abstract
Vision-language-action (VLA) models provide a powerful approach to training control policies for physical systems, such as robots, by combining end-to-end learning with transfer of semantic knowledge from web-scale vision-language model (VLM) training. However, the constraints of real-time control are often at odds with the design of VLMs: the most powerful VLMs have tens or hundreds of billions of parameters, presenting an obstacle to real-time inference, and operate on discrete tokens rather than the continuous-valued outputs that are required for controlling robots. To address this challenge, recent VLA models have used specialized modules for efficient continuous control, such as action experts or continuous output heads, which typically require adding new untrained parameters to the pretrained VLM backbone. While these modules improve real-time and control capabilities, it remains an open question whether they preserve or degrade the semantic knowledge contained in the pretrained VLM, and what effect they have on the VLA training dynamics. In this paper, we study this question in the context of VLAs that include a continuous diffusion or flow matching action expert, showing that naively including such experts significantly harms both training speed and knowledge transfer. We provide an extensive analysis of various design choices, their impact on performance and knowledge transfer, and propose a technique for insulating the VLM backbone during VLA training that mitigates this issue. Videos are available at https://pi.website/research/knowledge_insulation and open-source model weights are available at https://github.com/Physical-Intelligence/openpi.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **背景**：视觉-语言-动作模型（VLA）通过结合端到端学习与从网络规模 VLM 中迁移的语义知识，为机器人控制提供了强大范式。然而，实时控制要求与 VLM 的设计冲突：最强大的 VLM 参数多达数百亿，无法实时推理；且输出为离散 token，而机器人需要连续值控制。
- **现有解决方案**：近期 VLA 模型引入专用连续控制模块（如动作专家 diffusion/flow matching），但随机初始化这些模块会干扰预训练 VLM 骨干，导致训练速度下降、语言理解退化、知识迁移损失。
- **核心问题**：如何在不损失 VLM 预训练知识的前提下，使 VLA 同时具备快速训练、快速推理和良好泛化能力？

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：**知识绝缘（Knowledge Insulation）**——将 VLM 骨干与连续动作专家（action expert）的梯度流隔离，同时利用离散化的动作 token 作为表示学习信号，使 VLM 适应机器人控制任务而不被随机初始化专家干扰。
- **关键技术细节**：
  - **联合训练（Joint-training）**：同时训练两个动作表示路径——离散 FAST token（用于表示学习，训练时用交叉熵损失）与连续 flow matching 动作专家（用于推理时产生连续动作）。
  - **梯度停止（Stop-gradient）**：在注意力层中，来自动作专家的查询/值投影的梯度不反向传播到 VLM 骨干的键/值投影（使用 `sg` 操作符）。公式（5）（6）详细描述了具体实现：注意力概率矩阵中 `Pab` 部分的键和值都经过 stop-gradient。
  - **注意力掩码（Attention Mask）**：离散 FAST 动作 token 与连续动作 token 互不关注，防止信息泄露。
  - **VLM 数据共训练（Co-training with VLM data）**：在训练时混合通用视觉语言数据（图像描述、VQA、物体定位等），增强知识迁移。
  - **动作表示**：离散动作使用 FAST（基于离散余弦变换 + 字节对编码的压缩 token 化）；连续动作使用 flow matching（从噪声去噪生成动作块）。
  - **损失函数**：`L_CO-VLA = Cross-entropy loss on discrete tokens + α * Flow matching loss on continuous actions`，α 默认设为 1。
- **推理阶段**：仅使用轻量动作专家（约 3 亿参数）进行快速流去噪，无需缓慢的自回归 token 解码。

## 3. 实验设计：数据集、基准、对比方法

- **数据集/场景**：
  - **真实世界任务**：静态单臂机器人（table bussing、items in drawer）、静态双臂机器人（shirt folding）、移动双臂机器人（make bed、dish in sink、mobile items in drawer、laundry in basket）。部分场景在完全未见过环境中评估。
  - **公开基准**：LIBERO（模拟基准：Spatial、Object、Goal、95/100 变体）、DROID（真实世界中桌面操作任务）。
  - **训练数据**：专有大型机器人数据集（12 种机器人构型，含多种任务）+ 开源 OXE 数据集 + 通用 VLM 数据（CapsFusion、COCO、VQAv2、Cambrian-7M 等）。
- **对比方法**：
  - π0（原始连续动作专家，仅机器人数据训练）
  - π0-FAST（自回归 FAST token，仅机器人数据）
  - OpenVLA-OFT（并行解码，双向注意力）
  - Transfusion（同一 Transformer 内去噪连续输入）
  - HybridVLA（同时训练离散/连续动作但允许 token 双向交互）
  - 消融变体：joint-training（无 stop-gradient）、w/o VLM data、freeze backbone 等。

## 4. 资源与算力

- 论文 **未明确说明** 使用的 GPU 型号、数量及具体训练时长。仅提及：
  - 模型骨干为 2B 参数的 PaliGemma，动作专家约 300M 参数。
  - 联合训练相比纯连续训练增加约 **20% 的计算开销**，但由于收敛速度快，总实耗反而更少。
  - 训练使用内部基础设施，未提供精确硬件配置。

## 5. 实验数量与充分性

- **实验数量**：覆盖 7 个真实世界任务（含多种机器人）、2 个公开基准（LIBERO 多个子套件、DROID），并进行了大量消融实验：
  - 知识绝缘影响（stop-gradient vs 无）
  - VLM 数据共训练影响
  - 不同状态表示（text state、special token state、continuous state）
  - 不同动作表示（FAST vs naive tokenization）
  - 收敛速度比较（训练步数-性能曲线）
  - 语言遵循程度定量分析
- **充分性评估**：实验设计全面，涵盖了主要对比方法、关键组件消融、不同场景和评价指标。所有真实世界实验均报告 10 次重复的均值和统计显著性（双侧 t 检验）。公开基准实验也提供标准差。整体而言，实验充分、客观、公平。

## 6. 论文的主要结论与发现

- **知识绝缘有效提升语言遵循**：停止动作专家梯度可防止预训练 VLM 被干扰，使模型更准确地根据语言指令执行任务（如 items in drawer 任务中语言遵循率显著高于 π0 和 joint-training）。
- **联合离散+连续训练加速收敛**：训练速度与纯离散 FAST 方法相当（约 7.5 倍快于纯流匹配 π0），同时保持连续动作推理的高频（10 Hz）。
- **VLM 数据共转移增强泛化**：在未见物体泛化测试（mobile manipulation）中，加入 VLM 数据的模型显著优于仅机器人数据训练的模型。
- **在 LIBERO 上达到 SOTA**：在 LIBERO-90 和 LIBERO-Spatial 上超越所有基线，在 LIBERO-10 上略逊于 MoDE。
- **DROID 表现**：得分 0.55±0.09，优于 π0（0.49）和 π0-FAST（0.45）。
- **冻结骨干不可行**：VLM 预训练缺乏机器人表示，冻结后性能极差（0% 或很低）。

## 7. 优点

- **方法设计精巧**：知识绝缘理念简单有效，通过梯度停止解决了随机初始化专家对预训练知识的破坏，无需复杂训练技巧。
- **兼顾多目标**：同时实现快速训练、快速推理、高精度连续控制、语言跟随和知识迁移。
- **实验全面详实**：覆盖多种真实机器人、模拟基准、多种消融，并提供开源模型权重和网站展示视频，可重复性强。
- **实用性突出**：在多个任务上达到最高绝对性能，且推理速度（~10 Hz）远快于自回归 VLA（~1.3 Hz）。

## 8. 不足与局限

- **计算开销**：训练时需同时计算离散 token 和连续动作的损失，增加约 20% 训练计算量。但收敛速度提升可抵消部分开销。
- **语言遵循仍不完美**：尽管优于基线，但训练数据中的相关偏差仍可能导致模型偶尔忽略语言指令，尤其在复杂长时间任务中。
- **依赖 FAST token 质量**：离散表示学习依赖于 FAST tokenizer，若 tokenizer 引入误差会传递到表示学习。
- **应用限制**：主要验证于桌面操作和移动操作，未在更复杂（如高动态、多机器人协作）场景验证；且训练数据包含大量专有数据，复现需相似规模的数据。
- **算力报告不足**：未提供精确的 GPU 型号、数量及训练时间，不利于直接复现成本评估。

（完）
