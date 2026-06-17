## 简介
**Build your own Qdrant Vector Store MCP server**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3636

---

# Build your own Qdrant Vector Store MCP server


## 节点清单

| 节点 | 类型 |
|------|------|
| Insert | 工作流工具 |
| Search | 工作流工具 |
| Recommend | 工作流工具 |
| Qdrant MCP Server | MCP 触发器 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Operation | Switch 路由 |
| Compare | 工作流工具 |
| Recommend API | HTTP Request |
| Get Embeddings | HTTP Request |
| Preferences to Items | Code |
| Aggregate Embeddings | 数据聚合 |
| Get Embeddings1 | HTTP Request |
| Aggregate Embeddings1 | 数据聚合 |
| Group Search API | HTTP Request |
| Has Results? | IF 判断 |
| Simplify Group Results | 数据设置 |
| Empty Compare Response | 数据设置 |
| Aggregate Compare Response | 数据聚合 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Simplify Recommend Response | 数据设置 |
| Get Insert Response | 数据设置 |
| Get Search Response | 数据聚合 |
| Insert Reviews | Qdrant 向量存储 |
| Search Reviews | Qdrant 向量存储 |
| Split Out Companies | 数据拆分 |
| Filter By CompanyId | 过滤器 |
| Aggregate Recommend Response | 数据聚合 |
| Has Results?1 | IF 判断 |
| Empty Compare Response1 | 数据设置 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| ListCompanies | 工作流工具 |
| List by Facet API | HTTP Request |
| Create Facet Index | HTTP Request |
| Create Collection | HTTP Request |
| When clicking ‘Test workflow’ | 手动触发 |

## 触发方式
- Qdrant MCP Server 触发
- When Executed by Another Workflow 触发
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：37
- 触发节点：3
- 处理节点：27
- 输出节点：7
- 分类：knowledge-rag
