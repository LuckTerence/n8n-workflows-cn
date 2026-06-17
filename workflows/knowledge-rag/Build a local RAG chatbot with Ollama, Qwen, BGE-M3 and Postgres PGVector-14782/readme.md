## 简介
**Build a local RAG chatbot with Ollama, Qwen, BGE-M3 and Postgres PGVector**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14782

---

# Build a local RAG chatbot with Ollama, Qwen, BGE-M3 and Postgres PGVector


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Sub-Queries | 数据拆分 |
| Aggregate Matching Chunks | 数据聚合 |
| Aggregate All Retrieval Results | 数据聚合 |
| Any chunk? | IF 判断 |
| Clean RAG output | 数据设置 |
| Keep score over 0.4 | 过滤器 |
| Say no chunk match | 数据设置 |
| Prepare loop output | 数据设置 |
| Postgres Chat Memory (Small Talk) | PostgreSQL 聊天记忆 |
| Remove Think Tags (RAG Path) | Code |
| Switch | Switch 路由 |
| JSON Formatter | Code |
| Small Talk AI Agent | AI Agent |
| Ollama Chat Model (Small Talk — Qwen3:14b) | Ollama Chat Model |
| Ollama Chat Model (Classifier — Qwen2.5:7b) | Ollama Chat Model |
| Postgres Chat Memory (RAG Answer) | PostgreSQL 聊天记忆 |
| Answer Generator AI Agent | AI Agent |
| Ollama Chat Model (Answer Generator — Qwen3:14b) | Ollama Chat Model |
| Loop Over Sub-Queries | 分批处理 |
| Ollama Embeddings (BGE-M3) | Ollama Embeddings |
| PGVector Store — Retrieve Chunks | PGVector 向量存储 |
| Remove Think Tags (Small Talk Path) | Code |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Understand Request | LLM Chain |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：23
- 输出节点：1
- 分类：knowledge-rag
