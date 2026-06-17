## 简介
**AI邮件自动回复RAG**

RAG增强的邮件自动回复系统

> 分类：工作流自动化 | 适配等级：A（需替换Google Docs/Google Drive/Gmail/Notion/Pinecone)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/4748

---

# AI邮件自动回复RAG


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Answer questions with a vector store | 向量存储工具 |
| Pinecone Vector Store1 | Pinecone 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Get Brand brief | 工作流工具 |
| Gmail Trigger | Gmail 触发器 |
| OpenAI Chat Model2 | OpenAI Chat Model |
| If | IF 判断 |
| Simple Memory | 记忆缓冲区 |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Gmail | Gmail |
| Search Information | AI Agent |
| Response writer | AI Agent |
| Set Data | 数据设置 |
| Google Drive Trigger | Google Drive 触发器 |
| Google Drive | Google Drive |
| Pinecone Vector Store | Pinecone 向量存储 |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| When Executed by Another Workflow | 执行工作流触发器 |
| Notion | Notion |
| Aggregate | 数据聚合 |
| Edit Fields | 数据设置 |
| Google Docs | Google Docs |
| Check if Question | LLM Chain |

## 触发方式
- Gmail Trigger 触发
- Google Drive Trigger 触发
- When Executed by Another Workflow 触发

## 统计
- 节点总数：27
- 触发节点：3
- 处理节点：24
- 输出节点：0
- 分类：workflow-automation
