# Building RAG Chatbot for Movie Recommendations with Qdrant and Open AI

https://n8nworkflows.xyz/workflows/2440

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| GitHub | github |
| Extract from File | 从文件提取 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Token Splitter | textSplitterTokenSplitter |
| Qdrant Vector Store | Qdrant 向量存储 |
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Call n8n Workflow Tool | 工作流工具 |
| Window Buffer Memory | 记忆缓冲区 |
| Execute Workflow Trigger | 执行工作流触发器 |
| Merge | 数据合并 |
| Split Out | 数据拆分 |
| Split Out1 | 数据拆分 |
| Merge1 | 数据合并 |
| Aggregate | 数据聚合 |
| AI Agent | AI Agent |
| Embedding Recommendation Request with Open AI | HTTP Request |
| Embedding Anti-Recommendation Request with Open AI | HTTP Request |
| Extracting Embedding | 数据设置 |
| Extracting Embedding1 | 数据设置 |
| Calling Qdrant Recommendation API | HTTP Request |
| Retrieving Recommended Movies Meta Data | HTTP Request |
| Selecting Fields Relevant for Agent | 数据设置 |

## 触发方式
- When clicking ‘Test workflow’ 触发
- When chat message received 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：25
- 触发节点：3
- 处理节点：18
- 输出节点：4
- 分类：ai-agent
