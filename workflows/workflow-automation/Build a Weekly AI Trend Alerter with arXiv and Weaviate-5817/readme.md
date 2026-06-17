## 简介
**Build a Weekly AI Trend Alerter with arXiv and Weaviate**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5817

---

# Build a Weekly AI Trend Alerter with arXiv and Weaviate


## 节点清单

| 节点 | 类型 |
|------|------|
| Weaviate Vector Store | vectorStoreWeaviate |
| Default Data Loader | 文档加载器 |
| Query arXiv | HTTP Request |
| Convert XML to JSON | XML |
| Remove Duplicates | 去重 |
| Simple Memory | 记忆缓冲区 |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Weaviate Vector Store1 | vectorStoreWeaviate |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Date & Time | 日期时间 |
| Markdown | Markdown |
| Recursive Character Text Splitter1 | 文本分割器 |
| Structured Output Parser | 结构化输出解析器 |
| Schedule Trigger | 定时触发器 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| Merge | 数据合并 |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Get Current Date | 日期时间 |
| Split Results | 数据拆分 |
| Prep Data for Weaviate | 数据设置 |
| Enrich Articles with Topic Classification | AI Agent |
| Remove Fields | 数据设置 |
| Aggregate Uploaded arXiv IDs | 数据聚合 |
| Add Static sessionId | 数据设置 |
| Agentic RAG for Trend Analysis | AI Agent |
| Post Process Data | 数据设置 |
| Send email | Email 发送 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：28
- 输出节点：2
- 分类：workflow-automation
