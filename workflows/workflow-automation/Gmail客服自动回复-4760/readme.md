## 简介
**Gmail客服自动回复**

Ollama+Pinecone RAG

> 分类：工作流自动化 | 适配等级：A（需替换Pinecone/Gmail)（AI模型已本地化Ollama，Pinecone/Gmail需手动替换）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4760

---

# Gmail客服自动回复


## 节点清单

| 节点 | 类型 |
|------|------|
| Gmail Trigger | Gmail 触发器 |
| Text Classifier | 文本分类器 |
| AI Agent | AI Agent |
| Pinecone Vector Store | Pinecone 向量存储 |
| Label | Gmail |
| Send | Gmail |
| Ollama Model | lmOllama |
| Embeddings Ollama | Ollama Embeddings |
| Ollama Chat Model | Ollama Chat Model |
| Simple Memory | 记忆缓冲区 |

## 触发方式
- Gmail Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：9
- 输出节点：0
- 分类：workflow-automation
