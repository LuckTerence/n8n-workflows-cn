# Advanced AI Demo (Presented at AI Developers #14 meetup)

https://n8nworkflows.xyz/workflows/2358

## 节点清单

| 节点 | 类型 |
|------|------|
| Send message | Slack |
| Execute JavaScript | Code |
| Recursive Character Text Splitter | 文本分割器 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Embeddings OpenAI2 | OpenAI Embeddings |
| Vector Store Retriever | retrieverVectorStore |
| Download PDF | HTTP Request |
| PDFs to download | 空操作 |
| Read Pinecone Vector Store | Pinecone 向量存储 |
| Question and Answer Chain | chainRetrievalQa |
| Anthropic Chat Model | OpenAI Chat Model |
| Get calendar availability | HTTP 工具 |
| Appointment booking agent | AI Agent |
| Window Buffer Memory | 记忆缓冲区 |
| Insert into Pinecone vector store | Pinecone 向量存储 |
| Book appointment | HTTP 工具 |
| When chat message received | Chat 触发器 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Add automation label | Email 发送 |
| On new email to nathan's inbox | Gmail 触发器 |
| Add music label | Email 发送 |
| Assign label with AI | 文本分类器 |
| Webhook | Webhook |
| Whether email contains n8n | IF 判断 |

## 触发方式
- When chat message received 触发
- On new email to nathan's inbox 触发
- Webhook 触发

## 统计
- 节点总数：26
- 触发节点：3
- 处理节点：17
- 输出节点：6
- 分类：workflow-automation
