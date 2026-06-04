---
title: Unifying 2D and 3D Vision-Language Understanding
title_zh: 统一2D与3D视觉语言理解
authors: "Ayush Jain, Alexander Swerdlow, Yuzhou Wang, Sergio Arnaud, Ada Martin, Alexander Sax, Franziska Meier, Katerina Fragkiadaki"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=FcTeo26AfZ"
tags: ["query:vla"]
score: 6.0
evidence: 面向具身系统的统一2D/3D视觉语言模型
tldr: 针对3D视觉语言数据稀缺问题，提出UniVLG统一架构，初始化权重来自预训练2D模型，共享语言条件掩码解码器在RGB和RGB-D图像中定位物体。结合2D转3D提升策略，在具身系统任务中表现优于基线，缩小2D与3D域差距。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-fcteo26afz/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1779, \"height\": 773, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-fcteo26afz/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1778, \"height\": 934, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-fcteo26afz/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1776, \"height\": 1332, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-fcteo26afz/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1776, \"height\": 1254, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-fcteo26afz/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1776, \"height\": 390, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-fcteo26afz/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1769, \"height\": 2068, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1748, \"height\": 687, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 889, \"height\": 190, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 878, \"height\": 277, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 310, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 441, \"height\": 148, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 418, \"height\": 144, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 868, \"height\": 161, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 870, \"height\": 218, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 381, \"height\": 149, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 874, \"height\": 181, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 876, \"height\": 393, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 853, \"height\": 193, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-013.webp\", \"caption\": \"\", \"page\": 0, \"index\": 13, \"width\": 891, \"height\": 288, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-014.webp\", \"caption\": \"\", \"page\": 0, \"index\": 14, \"width\": 1528, \"height\": 319, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-015.webp\", \"caption\": \"\", \"page\": 0, \"index\": 15, \"width\": 1509, \"height\": 383, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-016.webp\", \"caption\": \"\", \"page\": 0, \"index\": 16, \"width\": 1397, \"height\": 277, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-fcteo26afz/table-017.webp\", \"caption\": \"\", \"page\": 0, \"index\": 17, \"width\": 1764, \"height\": 320, \"label\": \"Table\"}]"
motivation: 3D视觉语言数据稀缺，需利用2D预训练模型。
method: 提出统一架构，共享掩码解码器并加入2D转3D提升。
result: 在具身任务中优于基于框的方法。
conclusion: 缩小2D与3D域差距，增强具身视觉语言能力。
---

## Abstract
Progress in 3D vision-language learning has been hindered by the scarcity of large-scale 3D datasets. We introduce UniVLG, a unified architecture for 2D and 3D vision-language understanding that bridges the gap between existing 2D-centric models and the rich 3D sensory data available in embodied systems. Our approach initializes most model weights from pre-trained 2D models and trains on both 2D and 3D vision-language data. We propose a novel language-conditioned  mask decoder shared across 2D and 3D modalities to ground objects effectively in both RGB and RGB-D images, outperforming box-based approaches. To further reduce the domain gap between 2D and 3D, we incorporate 2D-to-3D lifting strategies, enabling UniVLG to utilize 2D data to enhance 3D performance. With these innovations, our model achieves state-of-the-art performance across multiple 3D vision-language grounding tasks, demonstrating the potential of transferring advances from 2D vision-language learning to the data-constrained 3D domain. Furthermore, co-training on both 2D and 3D data enhances performance across modalities without sacrificing 2D capabilities. By removing the reliance on 3D mesh reconstruction and ground-truth object proposals, UniVLG sets a new standard for realistic, embodied-aligned evaluation. Code and additional visualizations are available at https://univlg.github.io.

---

## 论文详细总结（自动生成）

# 论文结构化中文总结：UniVLG

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：3D视觉语言理解任务面临大规模3D数据集稀缺、标注成本高昂的瓶颈，导致预训练3D编码器性能远不如2D模型（如CLIP）。如何利用丰富的2D数据和预训练模型来提升3D理解能力成为关键挑战。
- **整体含义**：论文提出UniVLG，一个统一2D和3D视觉语言理解的架构，旨在缩小2D-centric模型与具身系统中丰富3D传感器数据之间的鸿沟。通过复用2D预训练权重、共享参数和2D-3D提升策略，实现利用2D数据增强3D性能，同时保持2D能力不退化，为具身AI提供更实用、更符合实际传感器输入的基线。

## 2. 方法论
- **核心思想**：构建一个端到端模型，同时处理单目RGB图像（2D）和多视角带位姿的RGB-D图像（3D）。所有参数在2D和3D通路之间完全共享，仅通过**位置编码**（2D图像用像素网格坐标，3D场景用X,Y,Z坐标）区分模态。对2D图像，使用2D-to-3D lifting模型（如MoGE）预测点图，从而统一输入格式。
- **关键技术细节**：
  - **视觉编码器**：使用冻结的DINOv2 ViT编码单帧RGB图像，随后叠加3D k-NN注意力层（相对位置编码）融合多视角特征。
  - **语言编码器**：采用JinaCLIP（支持长文本）将语言查询编码为token序列。
  - **语言条件掩码解码器**：借鉴Mask2Former但做出关键改进——在查询-文本-视觉特征之间交替使用**掩码交叉注意力**和自注意力，并**更新视觉特征**（而不仅仅是查询），这对于3D referential grounding至关重要。最终通过查询与视觉特征的**点积**预测3D掩码。
  - **文本解码器**：使用冻结的T5解码器，基于更新后的对象查询生成QA答案。
  - **损失函数**：`L_total = λ_mask L_mask + λ_text L_text + λ_box L_box + λ_gen L_gen`。其中L_mask为BCE+Dice损失；L_text为查询与文本token的跨度匹配损失（BCE）；L_box为新提出的**预测掩码包围框损失**（L1+GIoU），用于惩罚掩码中包含的离群点/多实例合并；L_gen为QA的交叉熵损失。
- **训练策略**：联合训练所有3D和2D数据集，2D数据有50%概率被提升到3D并通过全部层，否则跳过3D层。测试时2D数据保持原始空间以避免提升噪声。

## 3. 实验设计
- **数据集与Benchmark**：
  - **3D Referential Grounding**：SR3D、NR3D（提供GT proposals）、ScanRefer（不提供GT proposals）。使用**传感器点云**（由RGB-D直接反投影）和**网格点云**（标准benchmark提供）两种输入。
  - **2D Referential Grounding**：RefCOCO、RefCOCO+、RefCOCOg。
  - **3D Question Answering**：ScanQA、SQA3D。
  - **3D Instance Segmentation**：ScanNet200、Matterport3D（语言prompted方式）。
  - **Out-of-Domain评估**：L3DD数据集（包含ScanNet++、HM3D、ARKitScenes、ScanNet变体）。
- **对比方法**：
  - 3D grounding: 3D-VisTA, PQ3D, LLaVA-3D, BUTD-DETR, ODIN, InstanceRefer, SAT-2D等。
  - 2D grounding: LAVT, ReSTR, X-Decoder。
  - QA: 3D-LLM, NaviLLM, 3D-VisTA, PQ3D。
- **评估指标**：
  - 3D grounding：Top-1 Acc@25/50/75（IoU），Det（无GT proposals）和GT（有GT proposals）两种设置。
  - QA：Exact Match (EM@1)，额外报告BLEU-1, ROUGE, METEOR, CIDEr。
  - 3D实例分割：mAP, mAP25。
  - 2D grounding：Top-1 Acc。

## 4. 资源与算力
- **GPU配置**：32块NVIDIA A100 80G GPU，数据并行训练。
- **有效batch size**：64。
- **模型规模**：可训练参数约108M，加上冻结的视觉编码器（DINOv2，304M）和文本编码器（JinaCLIP，220M）。主实验使用DINOv2 backbone，消融实验使用Swin backbone（88M）。
- **训练时长**：论文未明确说明训练具体小时数，但提及处理90帧场景约1050ms、显存约15GB。
- **备注**：训练消耗较高，但推理效率可接受。

## 5. 实验数量与充分性
- **实验数量**：非常丰富，包含：
  - 主要结果表（表1、2、3、4、9）覆盖5+数据集上的referential grounding、QA、实例分割。
  - 消融实验（表5a、5b、5c、表6、表7）：分别探究框头 vs 掩码头、参数化 vs 非参数化查询、是否更新视觉特征、2D预训练权重影响、掩码框损失、2D训练策略（是否lifting）。
  - 2D-3D泛化测试（表8）：在AI2-THOR模拟器上分离2D和3D监督类别，验证lifting的效果。
  - 噪声鲁棒性分析（附录图6）：对位姿和深度注入噪声，对比BUTD-DETR。
  - 不同backbone对比（表11）：Swin vs DINOv2。
  - 是否微调backbone对比（表10）。
- **充分性与公平性**：
  - 对比方法全面，包括当前SOTA且复现了传感器点云条件下的基线（3D-VisTA、BUTD-DETR）。
  - 评估设置区分了GT proposals和Det两种现实程度，并首次在传感器点云上系统评测。
  - 消融实验设计合理，验证了每个关键组件的必要性。
  - 不足之处：未与更大的2D VLM（如GLIP、Grounding DINO）对比2D grounding；3D实例分割仅评估语言prompted方式，与闭集方法略有不可比；训练未使用更多2D数据（如RefCOCO外的大规模数据集），但作者承认这是未来工作。

## 6. 主要结论与发现
- **SOTA性能**：UniVLG在3D referential grounding上超越所有先前方法15%+（Det设置），在3D QA上也达到最佳。联合2D训练进一步提升3D性能（表1、2、9）。
- **掩码解码优于框解码**：在相同设置下掩码头准确率远高于框头，尤其在IoU@0.75时（表5c）。
- **2D-3D提升策略有效**：将2D图像提升到3D点图并在所有层共享参数，比跳过3D层带来更优性能（表6）。
- **2D能力不退化**：联合训练后2D referential grounding精度与纯2D版本一致（表4）。
- **对噪声鲁棒**：在位置/深度噪声下表现显著优于BUTD-DETR（附录图6）。
- **不依赖GT proposals和网格重建**：UniVLG可直接使用传感器点云，更贴近实际具身系统。

## 7. 优点
- **统一架构**：真正实现参数共享的2D-3D模型，无需两个编码器或不同输出头。
- **创新性设计**：
  - 语言条件掩码解码器中**更新视觉特征**，这是3D grounding的关键。
  - 提出**掩码框损失**，有效缓解掩码模型常见的离群点和多实例合并问题。
  - 利用**2D-to-3D lifting**将2D数据无缝融入3D训练。
- **现实评估**：首次在传感器点云上系统评测3D grounding，并去除了GT proposals依赖，推动更实用的基准。
- **实验全面**：覆盖多种任务、不同输入、跨域泛化、噪声分析、详细消融。

## 8. 不足与局限
- **掩码预测固有缺陷**：仍存在包含离群点、多个实例合并等问题（图5），导致Mask→Box转换时精度损失。
- **2D-3D泛化仍有差距**：在AI2-THOR测试中，2D监督的类别在3D测试下仍远低于完全3D监督的上限（53.8 vs 84.2，表8）。
- **2D数据利用不足**：仅使用了RefCOCO/+/g等小规模2D grounding数据，未探索大规模2D VLM数据（如GLIP、Grounding DINO）的潜力。
- **静态场景局限**：当前仅适用于静态3D场景，动态场景（如机器人操作）未涉及。
- **计算资源较高**：依赖32块A100 GPU，训练成本对部分研究组可能不友好。
- **未见与最新2D VLM对比**：未与将3D信息注入2D VLM的方法（如Spatial-RGPT）直接比较。
- **代码开源但未提供完整checkpoint**：仅提供可视化网站，实验可复现性依赖后续更新。

（完）
