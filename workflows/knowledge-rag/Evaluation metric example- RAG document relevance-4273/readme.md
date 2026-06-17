## 简介
**Evaluation metric example: RAG document relevance**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4273

---

# Evaluation metric example: RAG document relevance


## 节点清单

| 节点 | 类型 |
|------|------|
| When fetching a dataset row | evaluationTrigger |
| Evaluating? | 条件评估 |
| When chat message received | Chat 触发器 |
| Match chat format | 数据设置 |
| Return chat response | 空操作 |
| Set metrics | 条件评估 |
| Get dataset | Google Sheets |
| Remove Duplicates | 去重 |
| Simple Vector Store | vectorStoreInMemory |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Calculate doc relevance metric | OpenAI |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Extract documents | 数据设置 |
| Simple Vector Store1 | vectorStoreInMemory |
| Embeddings OpenAI1 | OpenAI Embeddings |

## 触发方式
- When fetching a dataset row 触发
- When chat message received 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：19
- 触发节点：3
- 处理节点：16
- 输出节点：0
- 分类：knowledge-rag
