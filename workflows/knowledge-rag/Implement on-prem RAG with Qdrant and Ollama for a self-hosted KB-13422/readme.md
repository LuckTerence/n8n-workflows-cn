## 简介
**Implement on-prem RAG with Qdrant and Ollama for a self-hosted KB**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13422

---

# Implement on-prem RAG with Qdrant and Ollama for a self-hosted KB


## 节点清单

| 节点 | 类型 |
|------|------|
| Default Data Loader | 文档加载器 |
| Embeddings Ollama | Ollama Embeddings |
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Simple Memory | 记忆缓冲区 |
| Add to Qdrant Vector Store | Qdrant 向量存储 |
| Read from Qdrant Vector Store | Qdrant 向量存储 |
| Upload document | 表单触发器 |

## 触发方式
- When chat message received 触发
- Upload document 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：7
- 输出节点：0
- 分类：knowledge-rag
