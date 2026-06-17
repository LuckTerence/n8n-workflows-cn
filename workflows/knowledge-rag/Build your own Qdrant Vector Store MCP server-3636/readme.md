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



## 功能说明

MCP 协议工具服务，为 AI Agent 暴露 API 接口。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：37
- 触发方式：手动触发

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
