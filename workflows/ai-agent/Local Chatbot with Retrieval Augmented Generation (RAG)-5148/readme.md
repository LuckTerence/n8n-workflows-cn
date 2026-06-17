## 简介
**Local Chatbot with Retrieval Augmented Generation (RAG)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/5148

---

# Local Chatbot with Retrieval Augmented Generation (RAG)


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings Ollama | Ollama Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Simple Memory | 记忆缓冲区 |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Embeddings Ollama1 | Ollama Embeddings |

## 触发方式
- On form submission 触发
- When chat message received 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：9
- 输出节点：0
- 分类：ai-agent
