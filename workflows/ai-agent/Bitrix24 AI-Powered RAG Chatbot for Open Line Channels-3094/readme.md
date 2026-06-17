## 简介
**Bitrix24 AI-Powered RAG Chatbot for Open Line Channels**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3094

---

# Bitrix24 AI-Powered RAG Chatbot for Open Line Channels


## 节点清单

| 节点 | 类型 |
|------|------|
| Bitrix24 Handler | Webhook |
| Credentials | 数据设置 |
| Validate Token | IF 判断 |
| Route Event | Switch 路由 |
| Process Message | Function |
| Process Join | Function |
| Process Install | Function |
| Register Bot | HTTP Request |
| Send Message | HTTP Request |
| Send Join Message | HTTP Request |
| Process Delete | 空操作 |
| Success Response | 响应 Webhook |
| Error Response | 响应 Webhook |
| Merge parameters for Subworkflow | 数据合并 |
| Get a list of available storages | HTTP Request |
| Get a list of List of Files and Folders | HTTP Request |
| Get a list of Folders files | HTTP Request |
| Download file | HTTP Request |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Split Out folder files and folders | 数据拆分 |
| Filter for files | 过滤器 |
| Move files to Vector stored folder | HTTP Request |
| Execute Workflow Trigger | 执行工作流触发器 |
| Qdrant Vector Store | Qdrant 向量存储 |
| Embeddings Ollama | Ollama Embeddings |
| Vector Store Retriever | retrieverVectorStore |
| Question and Answer Chain | chainRetrievalQa |
| Prepare output parameters | 数据设置 |
| Embeddings Ollama1 | Ollama Embeddings |
| Google Gemini Chat Model | OpenAI Chat Model |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| Execute subworkflow | 执行工作流 |

## 触发方式
- Bitrix24 Handler 触发
- Execute Workflow Trigger 触发

## 统计
- 节点总数：33
- 触发节点：2
- 处理节点：21
- 输出节点：10
- 分类：ai-agent
