---
title: "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference"
title_zh: SparseVLM：面向高效视觉语言模型推理的视觉令牌稀疏化
authors: "Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis A Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, Shanghang Zhang"
date: 2025-05-01
pdf: "https://openreview.net/pdf?id=80faIPZ67S"
tags: ["query:vla"]
score: 4.0
evidence: 通过令牌稀疏化实现高效VLM推理
tldr: 针对VLM中视觉令牌计算开销大的问题，提出无需额外训练的训练时免调优令牌优化机制。利用视觉相关文本令牌在自注意力矩阵中的重要性评分，渐进修剪无关视觉令牌，显著降低推理开销同时保持性能，可应用于VLA模型的高效部署。
source: ICML-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1651, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1759, \"height\": 600, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1763, \"height\": 621, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1719, \"height\": 459, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 867, \"height\": 564, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1722, \"height\": 631, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1739, \"height\": 833, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1677, \"height\": 1093, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1672, \"height\": 1080, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1386, \"height\": 924, \"label\": \"Figure\"}, {\"url\": \"assets/figures/openreview/openreview-icml-2025-80faipz67s/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1527, \"height\": 2356, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/openreview/openreview-icml-2025-80faipz67s/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1791, \"height\": 1530, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-80faipz67s/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 875, \"height\": 363, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-80faipz67s/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 871, \"height\": 421, \"label\": \"Table\"}, {\"url\": \"assets/tables/openreview/openreview-icml-2025-80faipz67s/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 823, \"height\": 411, \"label\": \"Table\"}]"
motivation: VLM中视觉令牌计算开销大，现有方法需额外训练。
method: 利用文本令牌评分视觉令牌重要性，渐进修剪无关令牌。
result: 显著降低推理开销且保持性能。
conclusion: 为VLM高效推理提供即用方案，可扩展至VLA。
---

## Abstract
In vision-language models (VLMs), visual tokens usually consume a significant amount of computational overhead, despite their sparser information density compared to text tokens. To address this, most existing methods learn a network to prune redundant visual tokens and require additional training data. Differently, we propose an efficient training-free token optimization mechanism dubbed **SparseVLM** without extra parameters or fine-tuning costs. Concretely, given that visual tokens complement text tokens in VLMs for linguistic reasoning, we select visual-relevant text tokens to rate the significance of vision tokens within the self-attention matrix extracted from the VLMs. Then we progressively prune irrelevant tokens. To maximize sparsity while retaining essential information, we introduce a rank-based strategy to adaptively determine the sparsification ratio for each layer, alongside a token recycling method that compresses pruned tokens into more compact representations. Experimental results show that our SparseVLM improves the efficiency of various VLMs across a range of image and video understanding tasks. In particular, when LLaVA is equipped with SparseVLM, it achieves a 54\% reduction in FLOPs, lowers CUDA time by 37\%, and maintains an accuracy rate of 97\%. Our code is available at https://github.com/Gumpest/SparseVLMs.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义

**研究动机**：在视觉语言模型（VLM）中，视觉令牌通常占大量计算开销（如LLaVA将672×672图像编码为2304个令牌），而视觉信息密度远低于文本。现有方法（如VoCo-LLaMA、FastV）需要额外训练网络来修剪冗余视觉令牌，且忽视文本提示的指导。

**核心贡献**：提出**SparseVLM**——首个**训练免费**、**文本引导**的视觉令牌稀疏化框架，无需额外参数或微调，即可显著降低VLM推理开销，同时保持任务性能。

## 2. 方法论

### 核心思想
- 利用VLM解码器自注意力矩阵中文本令牌与视觉令牌的交互，自动评估每个视觉令牌的重要性。
- 仅选择与视觉内容相关的文本令牌作为“评分者”，避免无关文本（如介词、代词）的干扰。
- 基于注意力矩阵的秩（rank）自适应确定每层的剪枝比例，并回收被剪枝令牌以压缩为更紧凑的表示。

### 关键技术细节

1. **视觉令牌重要性估计**  
   从自注意力矩阵 \(P \in \mathbb{R}^{L_t \times L_v}\) 中提取文本到视觉的交互部分，然后计算所有文本评分者注意力分数的平均值：
   \[
   \tilde{p} = \frac{1}{L_t} \sum_{i=1}^{L_t} P_i
   \]
   值越大表示对应视觉令牌越重要。

2. **文本评分者选择**  
   先计算每个文本令牌与所有视觉令牌的余弦相似度（经Softmax），取平均值 \(\mathbf{r}\)，设定阈值 \(\mathbf{m} = \text{mean}(\mathbf{r})\)，仅保留 \(\mathbf{r}_i \geq \mathbf{m}\) 的文本令牌作为评分者。公式：
   \[
   s = \{ i \mid r_i \geq m \}, \quad r = \frac{1}{L_v} \sum_{j=1}^{L_v} \text{Softmax}(H_v H_q^\top)_j
   \]

3. **自适应稀疏化比例**  
   使用注意力矩阵 \(P\) 的秩（rank）衡量冗余度。删除令牌数：
   \[
   N = \lambda \times (L_v - \text{rank}(P))
   \]
   其中 \(\lambda\) 为缩放因子。若某层 \(N=0\) 则跳过该层。

4. **令牌回收（Token Recycling）**  
   - **聚合**：从被剪枝令牌中回收分数最高的 \(\tau \%\)，使用密度峰值聚类（基于k近邻局部密度和距离指标）将它们分组为 \(C\) 个簇。
   - **重构**：每个簇内令牌通过逐元素求和压缩为单一重构令牌：
     \[
     T_k = \sum_{i=1}^{N_k} T[i], \quad k \in \{1,\dots,C\}
     \]
   - **复杂度**：额外开销远小于减少的计算量，整体FLOPs节省显著。

## 3. 实验设计

### 数据集 / 场景
- **图像理解**：GQA、MMBench、MME、POPE、ScienceQA、SEED-Bench、TextVQA、MMVet。
- **视频理解**：TGIF-QA、MSVD-QA、MSRVTT-QA、ActivityNet-QA（使用ChatGPT评分工具）。

### Benchmark
- 以原始VLM（100%准确率）为上限，比较不同修剪比率下的相对准确率、FLOPs和CUDA延迟。

### 对比方法
- **训练免费方法**：ToMe（Token Merging）、FastV、PDrop（PyramidDrop训练免费版本）。
- **基线**：原始未经剪枝的VLM。

### 模型框架
- LLaVA-1.5 7B/13B、Mini-Gemini、Qwen2-VL（图像）。
- VideoLLaVA（视频）。

## 4. 资源与算力

- 所有实验在**单张NVIDIA A100-80G GPU**上进行。
- 由于方法为**训练免费**，仅需推理阶段开销，论文未报告训练时间或GPU数量。

## 5. 实验数量与充分性

| 实验类别 | 数量/范围 | 说明 |
|---------|-----------|------|
| 图像任务 | 8个数据集 × 3种修剪配置（192/128/64 tokens） × 3种框架 | LLaVA、MGM、Qwen2-VL |
| 视频任务 | 4个基准 × 1种修剪（194 tokens） | VideoLLaVA |
| 消融实验 | 2项 | 文本评分者选择、令牌回收 |
| 效率对比 | 3项 | CUDA时间、FLOPs、KV缓存 |
| 可视化 | 多组 | 注意力热图/令牌保留模式 |

**充分性评估**：实验覆盖主流VLM架构、多种修剪比率、多模态任务，对比了最先进的训练免费方法，并进行消融验证，结果客观公平。但视频任务仅测试一个修剪比率（194 tokens），覆盖率略低。

## 6. 主要结论与发现

1. **显著效率提升**：LLaVA使用SparseVLM（保留192 tokens）时，FLOPs降低约54%（从4.62T降至2.14T），CUDA延迟降低37%（从57.82ms降至36.50ms），同时保持99.1%平均准确率。
2. **优于现有方法**：在相同延迟下，SparseVLM在LLaVA上比FastV准确率高11.2%~17.3%，在MGM上高9.2%~20.4%，在VideoLLaVA上高14.7%。
3. **自适应有效**：基于秩的剪枝比率可自动调整，避免过度剪枝。
4. **令牌回收收益随修剪率增大而增加**：当从192 tokens剪至64 tokens时，回收使POPE准确率提升从1.5%增至17.7%。

## 7. 优点

- **训练免费**：无需额外数据或微调，即插即用。
- **文本引导自适应**：根据问题动态保留关键视觉区域，比固定比率或簇类方法更精准。
- **令牌回收机制**：有效减少信息损失，尤其在高压缩率时优势明显。
- **兼容FlashAttention**：设计双pass方法，可高效提取注意力矩阵而不牺牲内存优化。
- **理论复杂度低**：额外开销（评分者选择、秩计算、聚类）远小于节省的计算量。

## 8. 不足与局限

- **实验覆盖**：视频任务仅测试一个剪枝比率（194 tokens），未探索多压缩率下的性能-效率权衡。
- **依赖文本质量**：文本评分者选择依赖于文本与视觉的余弦相似度，若问题简短或抽象（如“描述图片”），可能难以有效筛选相关文本令牌。
- **秩计算代价**：SVD计算秩的复杂度为 \(O(L_t L_v \min(L_t, L_v))\)，在极长序列（如多图或高帧率视频）中可能成为瓶颈，论文未分析大尺度下的扩展性。
- **未讨论幻觉影响**：修剪可能导致模型忽略边缘细节，可能在对抗性场景或细粒度任务中加剧幻视。
- **应用限制**：需要访问自注意力矩阵，某些黑盒API模型不支持；回收令牌数量由超参数\(\tau\)和\(\theta\)控制，需手动调节。

（完）
