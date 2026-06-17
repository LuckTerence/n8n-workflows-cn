## 简介
**AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Google Drive/Supabase)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2183

---

# AI Crew to Automate Fundamental Stock Analysis - Q&A Workflow


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Google Drive | Google Drive |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter1 | 文本分割器 |
| Qdrant Vector Store | Qdrant 向量存储 |
| When chat message received | Chat 触发器 |
| Webhook | Webhook |
| Retrieval QA Chain | chainRetrievalQa |
| Vector Store Retriever | retrieverVectorStore |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| OpenAI Chat Model | OpenAI Chat Model |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Embeddings OpenAI | OpenAI Embeddings |
| Respond to Webhook | 响应 Webhook |

## 触发方式
- When clicking "Execute Workflow" 触发
- When chat message received 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：3
- 处理节点：10
- 输出节点：1
- 分类：workflow-automation
