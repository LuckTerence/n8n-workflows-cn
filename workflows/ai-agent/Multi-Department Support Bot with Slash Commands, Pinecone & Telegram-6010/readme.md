## 简介
**Multi-Department Support Bot with Slash Commands, Pinecone & Telegram**

（待补充中文描述）

> 分类：AI Agent | 适配等级：B（需替换Pinecone/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6010

---

# Multi-Department Support Bot with Slash Commands, Pinecone & Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Switch | Switch 路由 |
| return policy | Telegram |
| talk technical | Telegram |
| billing | Telegram |
| Pinecone Vector Store3 | Pinecone 向量存储 |
| Google Drive Trigger | Google Drive 触发器 |
| Download file | Google Drive |
| Embeddings Cohere3 | Cohere Embeddings |
| Default Data Loader | 文档加载器 |
| Character Text Splitter | textSplitterCharacterTextSplitter |
| Pinecone Vector Store4 | Pinecone 向量存储 |
| Google Drive Trigger1 | Google Drive 触发器 |
| Download file1 | Google Drive |
| Embeddings Cohere4 | Cohere Embeddings |
| Default Data Loader1 | 文档加载器 |
| Character Text Splitter1 | textSplitterCharacterTextSplitter |
| Pinecone Vector Store5 | Pinecone 向量存储 |
| Google Drive Trigger2 | Google Drive 触发器 |
| Download file2 | Google Drive |
| Embeddings Cohere5 | Cohere Embeddings |
| Default Data Loader2 | 文档加载器 |
| Character Text Splitter2 | textSplitterCharacterTextSplitter |
| Telegram Trigger | Telegram 触发器 |
| Send a text message | Telegram |
| Switch1 | Switch 路由 |
| Send a text message4 | Telegram |
| AI Agent3 | AI Agent |
| Pinecone Vector Store6 | Pinecone 向量存储 |
| Embeddings Cohere6 | Cohere Embeddings |
| OpenRouter Chat Model3 | OpenRouter Chat Model |
| Simple Memory3 | 记忆缓冲区 |
| Pinecone Vector Store7 | Pinecone 向量存储 |
| Embeddings Cohere7 | Cohere Embeddings |
| Pinecone Vector Store8 | Pinecone 向量存储 |
| Embeddings Cohere8 | Cohere Embeddings |
| Send a text message1 | Telegram |
| Execute a SQL query | PostgreSQL |
| Execute a SQL query1 | PostgreSQL |
| Select rows from a table | PostgreSQL |
| Execute a SQL query2 | PostgreSQL |
| Send a text message2 | Telegram |
| return policy1 | PostgreSQL |
| tech questions | PostgreSQL |
| billing1 | PostgreSQL |
| Execute a SQL query3 | PostgreSQL |
| Send a text message3 | Telegram |

## 触发方式
- Google Drive Trigger 触发
- Google Drive Trigger1 触发
- Google Drive Trigger2 触发
- Telegram Trigger 触发

## 统计
- 节点总数：46
- 触发节点：4
- 处理节点：34
- 输出节点：8
- 分类：ai-agent
