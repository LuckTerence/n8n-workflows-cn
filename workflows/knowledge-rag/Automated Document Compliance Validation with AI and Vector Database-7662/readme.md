## 简介
**Automated Document Compliance Validation with AI and Vector Database**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7662

---

# Automated Document Compliance Validation with AI and Vector Database


## 节点清单

| 节点 | 类型 |
|------|------|
| Audit Document Upload | Webhook |
| Procedure Submission | Webhook |
| Fetch Document (Microsoft Graph) | HTTP Request |
| Delete Old Document Vectors | Code |
| Extract PDF Text | 从文件提取 |
| Generate Document Embeddings | Ollama Embeddings |
| Insert Vectors into Qdrant | Qdrant 向量存储 |
| Load Document Metadata | 文档加载器 |
| Split Text into Chunks | 文本分割器 |
| Format Procedure Payload | Code |
| AI Compliance Validator | AI Agent |
| Language Model (AI Agent) | Ollama Chat Model |
| Retrieve Relevant Document Chunks | Qdrant 向量存储 |
| Generate Query Embeddings | Ollama Embeddings |
| Language Model (Structured Output) | Ollama Chat Model |
| Parse AI Response | 结构化输出解析器 |
| Return Compliance Report | 响应 Webhook |

## 触发方式
- Audit Document Upload 触发
- Procedure Submission 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：13
- 输出节点：2
- 分类：knowledge-rag
