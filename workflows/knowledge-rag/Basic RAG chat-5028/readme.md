## 简介
**Basic RAG chat**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Pinecone/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5028

---

# Basic RAG chat


## 节点清单

| 节点 | 类型 |
|------|------|
| Recursive Character Text Splitter | 文本分割器 |
| Default Data Loader | 文档加载器 |
| Question and Answer Chain | chainRetrievalQa |
| Vector Store Retriever | retrieverVectorStore |
| When clicking 'Test Workflow' button | 手动触发 |
| When clicking 'Chat' button below | Chat 触发器 |
| Read/Write Files from Disk | 读写文件 |
| In-Memory Vector Store1 | vectorStoreInMemory |
| In-Memory Vector Store | vectorStoreInMemory |
| Embeddings Cohere | Cohere Embeddings |
| Groq Chat Model | Groq Chat Model |
| Embeddings Cohere1 | Cohere Embeddings |

## 触发方式
- When clicking 'Test Workflow' button 触发
- When clicking 'Chat' button below 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：10
- 输出节点：0
- 分类：knowledge-rag
