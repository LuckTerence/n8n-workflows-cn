## 简介
**Build a PDF Search System with Mistral OCR and Weaviate DB**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：9 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/7339

---

# Build a PDF Search System with Mistral OCR and Weaviate DB


## 节点清单

| 节点 | 类型 |
|------|------|
| Cohere Embeddings | Cohere Embeddings |
| Document Loader | 文档加载器 |
| Cohere Reranker | rerankerCohere |
| MCP Knowledge Server | MCP 触发器 |
| Search Knowledge Base | vectorStoreWeaviate |
| Text Splitter | 文本分割器 |
| Upload PDF | 表单触发器 |
| Extract Text from PDF | mistralAi |
| Prepare Document Data | 数据设置 |
| Store in Vector Database | vectorStoreWeaviate |

## 触发方式
- MCP Knowledge Server 触发
- Upload PDF 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
