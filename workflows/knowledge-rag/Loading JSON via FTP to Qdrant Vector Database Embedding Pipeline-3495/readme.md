# Loading JSON via FTP to Qdrant Vector Database Embedding Pipeline

https://n8nworkflows.xyz/workflows/3495

## 节点清单

| 节点 | 类型 |
|------|------|
| Qdrant Vector Store | Qdrant 向量存储 |
| When clicking ‘Test workflow’ | 手动触发 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Character Text Splitter | textSplitterCharacterTextSplitter |
| List all the files | FTP |
| Loop over one item | 分批处理 |
| Downloading item | FTP |

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：7
- 输出节点：0
- 分类：knowledge-rag
