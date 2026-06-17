## 简介
**Optimize Unstructured Data for RAG with Blockify IdeaBlocks Technology**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Drive)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7475

---

# Optimize Unstructured Data for RAG with Blockify IdeaBlocks Technology


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Query Data Tool | vectorStoreInMemory |
| AI Agent | AI Agent |
| RAG Chatbot | Chat 触发器 |
| Chunk Text | Code |
| Loop Over Chunks | 分批处理 |
| Simple IdeaBlock Vector Store | vectorStoreInMemory |
| Default Data Loader | 文档加载器 |
| Embed Individual IdeaBlocks (Already Separated) | textSplitterCharacterTextSplitter |
| Embeddings OpenAI | OpenAI Embeddings |
| OpenAI Chat Model | OpenAI Chat Model |
| Extract Text from .TXT File | 从文件提取 |
| Download .TXT File for Ingest | Google Drive |
| Blockify Ingest API | HTTP Request |
| Extract IdeaBlocks from API Response | 数据设置 |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- RAG Chatbot 触发

## 统计
- 节点总数：15
- 触发节点：2
- 处理节点：12
- 输出节点：1
- 分类：knowledge-rag
