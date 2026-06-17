# Local Document Question Answering with Ollama AI, Agentic RAG & PGVector

https://n8nworkflows.xyz/workflows/10157

## 节点清单

| 节点 | 类型 |
|------|------|
| Default Data Loader | 文档加载器 |
| Extract Document Text | 从文件提取 |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| Set File ID | 数据设置 |
| Respond to Webhook | 响应 Webhook |
| Edit Fields | 数据设置 |
| When chat message received | Chat 触发器 |
| Webhook | Webhook |
| Extract PDF Text | 从文件提取 |
| Aggregate | 数据聚合 |
| Summarize | 文本摘要 |
| RAG AI Agent | AI Agent |
| Switch | Switch 路由 |
| Extract from Excel | 从文件提取 |
| Set Schema | 数据设置 |
| Extract from CSV | 从文件提取 |
| Create Document Metadata Table | PostgreSQL |
| Create Document Rows Table (for Tabular Data) | PostgreSQL |
| List Documents | PostgreSQL 工具 |
| Get File Contents | PostgreSQL 工具 |
| Query Document Rows | PostgreSQL 工具 |
| Loop Over Items | 分批处理 |
| Insert Document Metadata | PostgreSQL |
| Insert Table Rows | PostgreSQL |
| Update Schema for Document Metadata | PostgreSQL |
| Local File Trigger | localFileTrigger |
| Read/Write Files from Disk | 读写文件 |
| Embeddings Ollama | Ollama Embeddings |
| Embeddings Ollama1 | Ollama Embeddings |
| Recursive Character Text Splitter | 文本分割器 |
| Ollama (Change Base URL) | OpenAI Chat Model |
| Delete Old Doc Records | PostgreSQL |
| Delete Old Data Records | PostgreSQL |
| Postgres PGVector Store | PGVector 向量存储 |
| Postgres PGVector Store1 | PGVector 向量存储 |

## 触发方式
- When chat message received 触发
- Webhook 触发
- Local File Trigger 触发

## 统计
- 节点总数：35
- 触发节点：3
- 处理节点：31
- 输出节点：1
- 分类：knowledge-rag
