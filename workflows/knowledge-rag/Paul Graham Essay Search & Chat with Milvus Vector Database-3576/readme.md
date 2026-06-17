# Paul Graham Essay Search & Chat with Milvus Vector Database

https://n8nworkflows.xyz/workflows/3576

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Fetch Essay List | HTTP Request |
| Extract essay names | HTML |
| Split out into items | 数据拆分 |
| Fetch essay texts | HTTP Request |
| Limit to first 3 | 数据限制 |
| Extract Text Only | HTML |
| Recursive Character Text Splitter1 | 文本分割器 |
| Milvus Vector Store | vectorStoreMilvus |
| AI Agent | AI Agent |
| When chat message received | Chat 触发器 |
| Default Data Loader | 文档加载器 |
| Milvus Vector Store as tool | vectorStoreMilvus |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model | OpenAI Chat Model |
| Embeddings OpenAI1 | OpenAI Embeddings |

## 触发方式
- When clicking "Execute Workflow" 触发
- When chat message received 触发

## 统计
- 节点总数：16
- 触发节点：2
- 处理节点：12
- 输出节点：2
- 分类：knowledge-rag
