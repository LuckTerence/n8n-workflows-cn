## 简介
**Save Costs In RAG Workflows using the Q&A Tool With Multiple Models**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5011

---

# Save Costs In RAG Workflows using the Q&A Tool With Multiple Models


## 节点清单

| 节点 | 类型 |
|------|------|
| Upload your file here | 表单触发器 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Insert Data to Store | vectorStoreInMemory |
| Query Data Tool | vectorStoreInMemory |
| AI Agent | AI Agent |
| When chat message received | Chat 触发器 |
| Answer questions with a vector store | 向量存储工具 |
| Expensive model | OpenAI Chat Model |
| Cheap Model | OpenAI Chat Model |

## 触发方式
- Upload your file here 触发
- When chat message received 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：knowledge-rag
