---
title: Object-centric 3D Motion Field for Robot Learning from Human Videos
title_zh: 面向机器人从人类视频学习的物体中心3D运动场
authors: "Zhao-Heng Yin, Sherry Yang, Pieter Abbeel"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=kp9B9iQDIt"
tags: ["query:vla"]
score: 6.0
evidence: 通过物体中心3D运动场从人类视频学习机器人控制策略
tldr: 从人类视频学习机器人控制的关键在于有效动作表示。本文提出物体中心3D运动场表示，并设计去噪提取管道，从单目视频中恢复精细物体运动。该表示可直接用于零样本机器人控制，无需策略训练，在多个任务上验证了有效性，为机器人模仿学习提供了紧凑且信息丰富的表示形式。
source: NeurIPS-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1229, \"height\": 342, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1419, \"height\": 729, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1437, \"height\": 482, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1440, \"height\": 517, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 568, \"height\": 405, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1450, \"height\": 407, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1449, \"height\": 249, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-neurips-2025-kp9b9iqdit/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1435, \"height\": 386, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-neurips-2025-kp9b9iqdit/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1421, \"height\": 325, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-neurips-2025-kp9b9iqdit/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 531, \"height\": 264, \"label\": \"Table\"}]"
motivation: 现有动作表示（如光流、点云流）存在建模复杂或信息损失问题。
method: 提出物体中心3D运动场表示，并训练去噪估计器从视频中提取该运动场用于零样本控制。
result: 在多个机器人操作任务上实现了零样本模仿，无需额外训练。
conclusion: 物体中心3D运动场是一种高效且可用于零样本机器人学习的动作表示。
---

## Abstract
Learning robot control policies from human videos is a promising direction for scaling up robot learning. However, how to extract action knowledge (or action representations) from videos for policy learning remains a key challenge. Existing action representations such as video frames, pixelflow, and pointcloud flow have inherent limitations such as modeling complexity or loss of information. In this paper, we propose to use object-centric 3D motion field to represent actions for robot learning from human videos, and present a novel framework for extracting this representation from videos for zero-shot control. We introduce two novel components. First, a novel training pipeline for training a ``denoising'' 3D motion field estimator to extract fine object 3D motions from human videos with noisy depth robustly. Second, a dense object-centric 3D motion field prediction architecture that favors both cross-embodiment transfer and policy generalization to background. We evaluate the system in real world setups. Experiments show that our method reduces 3D motion estimation error by over 50% compared to the latest method, achieve 55% average success rate in diverse tasks where prior approaches fail ($\lesssim 10$\%), and can even acquire fine-grained manipulation skills like insertion.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

机器人学习的主要瓶颈是数据收集——大规模高质量的真实世界机器人数据既昂贵又费时。人类与物体交互视频（如互联网或可穿戴设备录制的视频）作为一种可扩展的数据源受到关注。然而，从这些视频中提取有效的动作表示用于策略学习仍是一大挑战。现有表示（如视频帧、2D 像素流、点云流、SE(3) 位姿变换）均存在局限：视频帧过于冗余且噪声大；像素流丢失 3D 信息；点云流噪声大、精度低；SE(3) 位姿提取依赖物体 3D 模型且仅适用于刚体。因此，寻找一种既紧凑、信息充分、又易于提取和跨本体迁移的中间表示至关重要。

## 2. 方法论：核心思想、关键技术细节

### 2.1 核心思想
- **物体中心 3D 运动场**：定义为一个 4 通道图像张量（H×W×4），第一通道为深度值，后三通道为每个像素在相机坐标系下的 3D 运动向量（dx, dy, dz）。该表示是图像基、物体中心、本体无关的，保留了机器人控制所需的最小充分 3D 信息。
- **学习框架分为两阶段**：
  - **Phase I**：学习从含噪 RGBD 视频中估计干净的 3D 运动场（去噪估计器）。
  - **Phase II**：用该估计器标注人类视频，训练策略网络预测 3D 运动场，再通过 Kabsch 算法（结合 RANSAC）将预测的运动场解算为机器人末端的 SE(3) 动作，实现零样本控制。

### 2.2 关键技术细节
- **Phase I – 去噪 3D 运动场估计器**：
  - 数据集：在仿真中（ShapeNet + 随机刚体）生成 800 万样本（256×256），通过光线投射和随机刚体运动生成含噪输入（含噪深度、含噪 3D 像素流）和干净标签。
  - 数据增强：模拟真实深度噪声（缺失值、白噪声、错误值）、像素流噪声（高斯噪声、随机丢弃）、遮挡掩码等。
  - 模型：双头 UNet 架构，分别预测深度（fdepth）和运动（fmotion）。关键设计是在输入中拼接一个**密集内参图**（Imap ∈ R^{H×W×4}），包含 ((y-cy)/fy, (x-cx)/fx, 1/fy, 1/fx)，以提供 CNN 无法自学习的投影几何信息。
  - 损失：加权的 Huber 损失，仅在物体掩码上计算。
- **Phase II – 策略学习与部署**：
  - 用 Phase I 的估计器处理真实人类视频（RGBD），结合 SAM2 分割和 CoTracker3 跟踪，得到物体 3D 运动场标签。
  - 策略网络 π 同样基于双头 UNet（可选用扩散模型或高斯模型），输入为分割后的 RGBD 图像，输出预测的物体 3D 运动场。
  - 训练损失与 Phase I 类似（加权的 Huber 损失）。
  - 部署时：利用预测运动场，通过 Kabsch 算法（带 RANSAC）求解 SE(3) 变换，再转换到机器人基座坐标系执行。

### 2.3 关键假设
- 拥有可靠的抓取/释放策略（假设 1）。
- 使用 RGBD 视频（假设 2），相机内参已知。

## 3. 实验设计

### 3.1 评估场景与任务
- **3D 运动场估计器评估**：真实世界抓取随机物体并运动，读取机器人夹爪位姿作为 ground truth，计算 SE(3) 误差。使用 Intel D435 相机（640×480，裁剪为 480×480 再缩放至 256×256），物体距相机 40-50 cm。
- **机器人控制任务（5 个真实世界任务）**：
  1. 拾取-旋转-放置
  2. 线跟踪（笔状手电筒跟踪电缆）
  3. 工具使用-推（用工具将物体推至目标）
  4. 扳手拧螺母（高精度）
  5. 插入（2.5 mm 公差）

### 3.2 基线方法
- 主要基线：**GFlow (General Flow)** [59]（代表点云流方法）。
- 其他对比方法：UniPi [9], ATM [49], Track2Act [3], Im2Flow2Act [52], SPOT [15], TI [6]（在 Table 2 中从技术特性上比较）。

### 3.3 数据集
- 每个任务收集 50-150 个人类演示视频，采集时间 2-15 分钟。

### 3.4 实验充分性
- 在 5 个真实任务上评估零样本成功率（3 个种子取平均）。
- 消融实验包括：内参图影响、扩散模型 vs 高斯模型、掩码扩散、数据增强。
- 对抗鲁棒性测试（注入高斯噪声）。
- 定量比较 3D 运动场估计误差（位置 MSE 和旋转矩阵 Frobenius 范数）。

## 4. 资源与算力

论文明确说明：
- **Phase I 仿真数据生成**：1 块 NVIDIA L40 GPU，12 小时内生成 800 万样本（256×256）。
- **Phase I 模型训练**：16 块 NVIDIA A100-40GB GPU，约 1 天。
- **Phase II 策略训练**：未明确说明具体 GPU 数量和时间，但提到与 Phase I 类似架构，推测算力需求相近。

## 5. 实验数量与充分性

| 实验类型 | 数量/详情 | 评估标准 |
|----------|-----------|----------|
| 3D 运动场估计误差 | 1 组定量对比（baseline vs 本方法） | 位置 MSE、旋转误差 |
| 鲁棒性测试 | 不同 σ 噪声注入 | 同上 |
| 内参图消融 | 3 组（无内参/无焦距/全量） | 3D 运动场误差 |
| 机器人任务成功率 | 5 个任务 × 3 种子 | 成功率 |
| 策略消融（细粒度任务） | 4 组（无扩散/无掩码/无数据增强/全量） | 成功率 |

**充分性评价**：实验覆盖了核心组件消融、基线对比、鲁棒性、多任务泛化，且对细粒度任务专门做了消融，设计较为完整。但在真实世界任务中仅使用一种机器人（XArm7）和一种夹具（平行爪），未测试灵巧手或多机器人。此外，仅在 5 个特定任务上测试，泛化性证据有限。

## 6. 主要结论与发现

1. **3D 运动场估计**：本方法将 SE(3) 运动估计误差降低超过 50%（相比直接法基线），且对深度噪声鲁棒。
2. **机器人零样本控制**：在 5 个真实任务中平均成功率达 ~55%，而基线方法（GFlow）成功率 ≤10%。特别是插入任务（2.5mm 公差）取得 35% 成功率（消融全配置），这是首次在仅用人类视频训练下实现精细操作。
3. **关键设计验证**：
   - 密集内参图对运动场预测至关重要（移除后误差显著上升）。
   - 扩散模型优于高斯模型（细粒度任务中从 0% 提升至 35%）。
   - 掩码扩散和数据增强均有效。

## 7. 优点

- **表示创新**：物体中心 3D 运动场结合了图像基表示的灵活性和 3D 几何信息的完整性，相比纯图像或点云流更有利于机器人控制。
- **去噪管道设计精巧**：利用仿真数据训练去噪估计器，有效克服了真实深度和跟踪的噪声，且几何任务（无纹理）的 sim-to-real 迁移效果好。
- **零样本迁移**：直接从人类视频学习，无需机器人特定数据，实现了跨本体和背景的泛化。
- **高效部署**：从运动场到 SE(3) 动作的转换计算快速（300-1000 Hz），几乎不增加控制延迟。
- **消融实验严谨**：详细验证了内参图、扩散模型、掩码、数据增强等设计的重要性。

## 8. 不足与局限

- **完全遮挡未处理**：仅处理部分遮挡或完全可见片段，完全遮挡下的动作知识提取未涉及。
- **仅限刚体**：假设物体为刚性（通过 SE(3) 提取），软体（如布料）无法处理，需扩展为局部运动场。
- **固定相机假设**：当前实验假设静态相机，虽提出可扩展到移动相机的方向，但未实现验证。
- **机器人类型局限**：仅使用平行爪夹爪，未验证灵巧手场景。对于手部需运动条件策略而非直接优化 SE(3)。
- **数据集规模较小**：每个任务仅 50-150 个演示，可能限制模型泛化能力。
- **成功率仍有提升空间**：尤其是插入任务成功率为 35%，且观察到“bang-bang”调整行为，未达到人类一步到位能力。
- **实验泛化性有限**：仅在单一机器人平台、固定相机视角下测试，未报告跨物体、跨场景的零样本测试。

（完）
