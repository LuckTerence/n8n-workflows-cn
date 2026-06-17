## 简介
**Dynamic Website Assistant with DeepSeek AI, Pinecone Vectorstore & Site-Based Routing**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6295

---

# Dynamic Website Assistant with DeepSeek AI, Pinecone Vectorstore & Site-Based Routing


## 节点清单

| 节点 | 类型 |
|------|------|
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Pinecone Vector Store5 | Pinecone 向量存储 |
| Embeddings Cohere | Cohere Embeddings |
| Pinecone Vector Store6 | Pinecone 向量存储 |
| Embeddings Cohere6 | Cohere Embeddings |
| Pinecone Vector Store7 | Pinecone 向量存储 |
| Embeddings Cohere7 | Cohere Embeddings |
| Pinecone Vector Store9 | Pinecone 向量存储 |
| Embeddings Cohere9 | Cohere Embeddings |
| Pinecone Vector Store10 | Pinecone 向量存储 |
| Embeddings Cohere10 | Cohere Embeddings |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Switch | Switch 路由 |
| Postgres Chat Memory1 | PostgreSQL 聊天记忆 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Pinecone Vector Store8 | Pinecone 向量存储 |
| Embeddings Cohere8 | Cohere Embeddings |
| Respond to Webhook1 | 响应 Webhook |
| AI Agent for groton | AI Agent |
| AI Agent1 ghostwritingpartner | AI Agent |
| Postgres Chat Memory2 | PostgreSQL 聊天记忆 |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Pinecone Vector Store11 | Pinecone 向量存储 |
| Embeddings Cohere11 | Cohere Embeddings |
| Respond to Webhook2 | 响应 Webhook |
| AI Agent ebook-wr | AI Agent |



## 功能说明

Dynamic Website Assistant with DeepSeek AI、Pineco（AI 增强)Webhook 触发，通过 数据库 + HTTP API 实现自动化。

Webhook触发，通过 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：28
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：24
- 输出节点：3
- 分类：knowledge-rag
