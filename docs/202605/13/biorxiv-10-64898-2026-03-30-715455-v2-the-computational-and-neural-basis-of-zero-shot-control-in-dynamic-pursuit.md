---
title: The Computational and Neural Basis of Zero-Shot Control in Dynamic Pursuit
title_zh: 动态追逐中零样本控制的计算与神经基础
authors: "Kim, D., Lee, J. J., Hayden, B. Y., Yoo, S. B. M."
date: 2026-05-10
pdf: "https://www.biorxiv.org/content/10.64898/2026.03.30.715455v2.full.pdf"
tags: ["query:vla"]
score: 6.5
evidence: 具身动态任务中灵活控制的计算基元
tldr: 本研究探讨了生物体在无需额外训练的情况下灵活适应新目标的计算原理。研究者提出了关系结构、聚光灯注意力和可负担性计算三个核心认知构件，并构建了一个多模块图卷积网络模型。该模型在动态追踪任务中实现了零样本迁移，并展现出类似生物的“改变主意”行为。通过对灵长类背侧前扣带回皮层的神经记录分析，验证了该计算架构的生物学合理性，为理解灵活控制的神经机制提供了新视角。
source: biorxiv
selection_source: fresh_fetch
motivation: 旨在揭示生物体如何在没有额外训练的情况下，通过计算原理灵活适应新目标和环境需求。
method: 提出了由关系结构、注意力和可负担性计算组成的认知构件，并利用多模块图卷积网络在动态追踪任务中进行实现。
result: 模型成功实现了跨场景的零样本迁移，并产生了“改变主意”行为，且其计算逻辑得到了灵长类神经生理数据的支持。
conclusion: 关系结构、注意力和可负担性计算是实现灵活控制的最小计算基元，为理解大脑的动态决策提供了理论框架。
---

## 摘要
生物智能体能够灵活地调整其行为以适应新的目标和环境需求，而无需额外的训练，但实现这种控制的计算原理仍不清楚。在此，我们提出三个认知构念构成了灵活控制的最小计算基元：关系结构、聚光灯注意力和可负担性计算。我们研究了这些构念是否支撑了具身动态追逐任务中的灵活控制，该任务需要持续整合实体间关系、奖励和动作可行性，使其成为实时控制的理想试验场。通过在多模块图卷积网络中实现这些构念，我们展示了该模型在无需额外训练的情况下，实现了跨新追逐场景的零样本迁移。尽管没有经过明确训练，该模型还表现出了“改变主意”行为，这是生物智能体所表现出的灵活控制的一个标志。来自灵长类动物背侧前扣带回皮层的神经记录揭示了将这些构念与神经动力学联系起来的群体水平特征，为所提出的计算架构提供了生物学支持。

## Abstract
Biological agents flexibly adapt their behavior to novel goals and environmental demands without additional training, yet the computational principles enabling such control remain unclear. Here, we propose that three cognitive constructs constitute minimal computational motifs for flexible control: relational structure, spotlight attention, and affordance computation. We examine whether these constructs underpin flexible control in an embodied dynamic pursuit task requiring continuous integration of inter-entity relations, reward, and action feasibility, making it a suitable testbed for real-time control. By implementing these constructs within a multi-module graph convolutional network, we show that the model achieves zero-shot transfer across novel pursuit scenarios without additional training. Although not explicitly trained to do so, the model also exhibits change-of-mind behavior, a hallmark of flexible control exhibited by biological agents. Neural recordings from the primate dorsal anterior cingulate cortex revealed population-level signatures linking these constructs to neural dynamics, providing biological support for the proposed computational architecture.