---
title: "DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge"
title_zh: DreamVLA：用全面世界知识梦境化的视觉-语言-动作模型
authors: "Wenyao Zhang, Hongsi Liu, Zekun Qi, Yunnan Wang, XinQiang Yu, Jiazhao Zhang, Runpei Dong, Jiawei He, He Wang, Zhizheng Zhang, Li Yi, Wenjun Zeng, Xin Jin"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=PK07eretkF"
tags: ["query:vla"]
score: 9.0
evidence: DreamVLA：具有世界知识预测的视觉-语言-动作模型
tldr: 现有VLA模型在机器人操纵中缺乏全面的世界知识（动态、空间、语义）。本文提出DreamVLA，引入动态区域引导的世界知识预测，结合逆动力学建模，形成感知-预测-动作循环。实验证明该方法显著提升了泛化能力和推理准确性。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1422, \"height\": 366, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1436, \"height\": 693, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1400, \"height\": 361, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 642, \"height\": 634, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 667, \"height\": 605, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1418, \"height\": 393, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1448, \"height\": 1960, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1403, \"height\": 1226, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1393, \"height\": 1214, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-pk07eretkf/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1408, \"height\": 1319, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1462, \"height\": 650, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1368, \"height\": 372, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1439, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1418, \"height\": 296, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 698, \"height\": 187, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 696, \"height\": 188, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 700, \"height\": 194, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 698, \"height\": 199, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1378, \"height\": 342, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1080, \"height\": 571, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 753, \"height\": 495, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 871, \"height\": 201, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-pk07eretkf/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 917, \"height\": 360, \"label\": \"Table\"}]"
motivation: 当前VLA模型缺乏全面世界知识，限制泛化与推理。
method: 集成动态区域引导的世界知识预测模块，实现逆动力学建模。
result: 在操纵任务上提升了泛化性和推理精度。
conclusion: 世界知识预测是增强VLA模型的有效途径。
---

## Abstract
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation.  However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information.
To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. 
Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction,  integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning.
This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting.
To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled.
Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features.
Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7 success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

---

## 论文详细总结（自动生成）

# DreamVLA 论文详细总结

## 1. 论文的核心问题与整体含义

**研究动机**：现有视觉-语言-动作（VLA）模型直接从观测和语言指令映射到动作，缺乏对未来世界知识的闭环预测能力。已有的融合未来预测的方法（如生成未来帧或子目标图像）存在以下问题：  
- 预测的像素信息冗余，与当前观测高度重叠；  
- 缺乏显式的3D空间信息（深度）；  
- 缺少高层语义知识（如物体身份、功能）。  
因此，模型无法像人类一样在行动前形成抽象的多模态推理链。

**研究目标**：提出 DreamVLA，将**全面的世界知识预测**（动态区域、深度、语义）集成进 VLA 框架，建立“感知—预测—动作”循环，提升机器人操控的泛化性和推理能力。

## 2. 方法论

### 2.1 核心思想
将 VLA 建模为**逆动力学问题**，通过预测未来世界知识作为中间推理步骤，辅助动作生成。具体预测三种模态的知识：
- **动态区域**：基于光流模型（CoTracker）识别未来运动的像素区域，避免全帧重建冗余；
- **深度图**：通过 Depth-Anything 估计未来深度，提供3D空间信息；
- **高层语义特征**：预测未来 DINOv2 和 SAM 的特征，提供物体级语义。

### 2.2 关键技术细节
1. **世界嵌入提取**：语言（CLIP）、图像（MAE ViT）、机器人状态（MLP）编码后，与可学习的 `<dream>` 查询（分为动态、深度、语义三个子查询）拼接，送入 GPT-2 模型得到潜在世界嵌入 \( w_{t+n} \)。
2. **块状结构化注意力（Block-wise Structured Attention）**：子查询之间禁止相互注意力，只关注视觉、语言、状态令牌，防止跨模态信息泄露，保持特征解耦。
3. **世界知识预测解码器**：轻量 ViT 解码器将世界嵌入分别映射为动态区域掩码、深度图、语义特征，训练时使用相应损失函数：
   - 动态区域：基于掩码重建的 ELBO 损失；
   - 深度：尺度归一化 MSE 损失；
   - 语义：InfoNCE 对比损失。
4. **动作生成**：通过 `<action>` 查询从世界嵌入中聚合动作相关信息，再用**扩散变换器（DiT）**从噪声中逐步去噪生成多步动作序列。

### 2.3 公式或算法流程
- 世界嵌入：\( w_{t+n} = M(l, o_t, s_t | \text{<dream>}) \)  
- 知识预测：\( \hat{p}_{t+n} = P(w_{t+n}) = \{\hat{f}_{t+n}, \hat{d}_{t+n}, \hat{c}_{t+n}\} \)  
- 动作生成：\( \hat{a}_{t:t+n-1} = D(M(l, o_t, s_t, \text{<dream>} | \text{<action>})) \)  
- 总损失：\( L = \lambda_{\text{dyn}} L_{\text{dyn}} + \lambda_{\text{depth}} L_{\text{depth}} + \lambda_{\text{sem}} L_{\text{sem}} + \lambda_{\text{DiT}} L_{\text{DiT}} \)

## 3. 实验设计

### 3.1 使用数据集与场景
- **仿真**：CALVIN（ABC-D 基准，环境A/B/C训练，D测试）、LIBERO（Spatial/Object/Goal/Long 四个子套件）。
- **真实世界**：Franka Panda 机器人，两个 RealSense D415 相机（第三视角+腕装），共4类别物体（瓶子、玩偶、香蕉、辣椒）进行抓取与放置任务，以及抽屉开闭任务。

### 3.2 对比方法
对比包括：Roboflamingo、Susie、GR-1、3D Diffusor Actor、OpenVLA、RoboDual、UNIVLA、π₀、CLOVER、UP-VLA、Robovlm、Seer、VPP、Diffusion Policy、Octo-Base、CoT-VLA 等。

### 3.3 评价指标
- CALVIN：连续5个任务完成率及平均长度（Avg. Len.）。
- LIBERO：每个子套件成功率。
- 真实世界：Pick/Place/Drawer 任务成功率（每任务100轨迹，最多20次尝试）。

## 4. 资源与算力

论文明确说明：  
- 使用 **8 张 NVIDIA A800 GPU** 训练。  
- 优化器 AdamW，学习率 1e-3，权重衰减 1e-4，余弦学习率调度，5%线性预热。  
- 批量大小 64，训练 20 个 epoch。  
- 预训练在 CALVIN 的无语言部分和 DROID 数据集上进行。  
- 附录提到训练时 SAM 特征预计算，节省 GPU 内存。  
- 推理时在 RTX 4090 上 11 Hz（91ms）。

## 5. 实验数量与充分性

**实验数量**：  
- CALVIN ABC-D 上报告了完整成功率和平均长度（表1）；  
- LIBERO 四个子套件（表2）；  
- 真实世界 3 个任务（表3）；  
- 消融实验（表4-8，图6）：涵盖各模态贡献、预测 vs 辅助任务、动态区域 vs 光流、结构化注意力 vs 因果注意力、共享 vs 分离查询、查询数量影响。  
- 附录还补充了特征可视化（动态区域、深度预测）和推理延迟。

**充分性与公平性**：  
- 对比方法均为近期代表性工作，采用相同仿真设置（CALVIN ABC-D 标准协议）。  
- 真实世界实验与 Diffusion Policy、Octo-Base、OpenVLA 微调对比（同样100轨迹），条件一致。  
- 消融实验全面，逐步剥离每个组件验证必要性。  
- 但未报告多轮随机种子下的方差/置信区间，可能对稳定性有影响。

## 6. 论文的主要结论与发现

- **核心结论**：在世界知识预测的辅助下，VLA 模型能显著提升操控性能，预测动态区域收益最大，深度和语义带来互补收益。  
- **关键发现**：  
  1. 若仅预测深度或语义，单独使用会损害性能（梯度噪声干扰）；联合预测则协同提升。  
  2. 使用动态区域（二值掩码）比直接预测光流更有效，计算更轻量。  
  3. 结构化注意力块比因果注意力大幅提高长时序成功率。  
  4. 分离的 `<dream>` 子查询优于共享查询。  
  5. **SOTA 结果**：CALVIN ABC-D 平均长度 4.44，LIBERO 平均 92.6%，真实世界 76.7% 成功率。

## 7. 优点

- **新颖性**：首次系统提出用动态区域 + 深度 + 语义三种紧凑世界知识作为 VLA 的中间推理，更符合人类认知。  
- **高效性**：预测仅为令牌级，推理时无需解码图像，额外计算极少（3ms）。  
- **通用性**：兼容多种视觉编码器和大语言模型，可扩展到不同操控平台。  
- **充分消融**：清晰揭示了每种知识的作用与交互，设计决策有理有据。  

## 8. 不足与局限

- **实验覆盖**：主要限于平行夹爪的桌面操作，未涉及灵巧手或全身移动操作。  
- **数据依赖**：动态区域监督依赖光流模型，深度依赖深度估计器，在极端场景（低纹理、快速运动）可能不准。  
- **无统计误差**：未报告多次实验的标准差或置信区间，结果稳定性存疑。  
- **场景偏好**：视觉输入为 RGB，缺乏 3D 点云、触觉等多模态融合，未在复杂几何变化场景中验证。  
- **长时序扩展**：当前预测 n 步（实验中 n=3），更长时序规划需要更多研究。  
- **资源需求**：预训练需大算力（8 A800），对资源有限团队不友好。

（完）
