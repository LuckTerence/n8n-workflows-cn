## 简介
**Build hybrid RAG search over PDFs with Qdrant and Ollama**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16040

---

# Build hybrid RAG search over PDFs with Qdrant and Ollama


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Extract from File | 从文件提取 |
| Read/Write Files from Disk | 读写文件 |
| Check If Collection Exists | qdrant |
| If | IF 判断 |
| Create Collection | qdrant |
| Embeddings Ollama | Ollama Embeddings |
| Qdrant Vector Store | Qdrant 向量存储 |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Merge | 数据合并 |
| When chat message received | Chat 触发器 |
| Split Out | 数据拆分 |
| Aggregate | 数据聚合 |
| Update Vectors | qdrant |
| Get All Points | qdrant |
| Edit Fields | 数据设置 |
| Generate the embeddings of the query | HTTP Request |
| Query Points (using the embeddings) | qdrant |
| Extract sparse from Qdrant | Code |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- When chat message received 触发

## 统计
- 节点总数：20
- 触发节点：2
- 处理节点：17
- 输出节点：1
- 分类：knowledge-rag
