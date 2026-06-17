## 简介
**Chat with Your Email History using Telegram, Mistral and Pgvector for RAG**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3763

---

# Chat with Your Email History using Telegram, Mistral and Pgvector for RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Loop Over Items | 分批处理 |
| Came from Telegram? | IF 判断 |
| When chat message received | Chat 触发器 |
| Postgres PGVector Store | PGVector 向量存储 |
| Call the SQL composer Workflow | 工作流工具 |
| Embeddings Ollama | Ollama Embeddings |
| Beautify chat response | 数据设置 |
| Split text into chunks | Code |
| Respond on Telegram in batches | Telegram |
| Escape Markdown | Code |
| No Operation, do nothing | 空操作 |
| Simple Memory | 记忆缓冲区 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Generate session id | 数据设置 |

## 触发方式
- Telegram Trigger 触发
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：13
- 输出节点：1
- 分类：knowledge-rag
