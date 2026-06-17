## 简介
**Reduce LLM Costs with Semantic Caching using Redis Vector Store and HuggingFace**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10887

---

# Reduce LLM Costs with Semantic Caching using Redis Vector Store and HuggingFace


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Redis Chat Memory | memoryRedisChat |
| When chat message received | Chat 触发器 |
| Analyze results from store | Code |
| Check for similar prompts | vectorStoreRedis |
| Respond to Chat (from semantic cache) | 聊天 |
| Respond to Chat (from LLM) | 聊天 |
| LLM Agent | AI Agent |
| Store entry in cache | vectorStoreRedis |
| Add response as metadata | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Is this a cache hit? | IF 判断 |
| Embeddings HuggingFace Inference | embeddingsHuggingFaceInference |
| Embeddings HuggingFace Inference1 | embeddingsHuggingFaceInference |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：knowledge-rag
