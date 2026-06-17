## 简介
**Build a local RAG chatbot with Ollama, Qwen, BGE-M3 and Postgres PGVector**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14782

---

# Build a local RAG chatbot with Ollama, Qwen, BGE-M3 and Postgres PGVector


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Sub-Queries | 数据拆分 |
| Aggregate Matching Chunks | 数据聚合 |
| Aggregate All Retrieval Results | 数据聚合 |
| Any chunk? | IF 判断 |
| Clean RAG output | 数据设置 |
| Keep score over 0.4 | 过滤器 |
| Say no chunk match | 数据设置 |
| Prepare loop output | 数据设置 |
| Postgres Chat Memory (Small Talk) | PostgreSQL 聊天记忆 |
| Remove Think Tags (RAG Path) | Code |
| Switch | Switch 路由 |
| JSON Formatter | Code |
| Small Talk AI Agent | AI Agent |
| Ollama Chat Model (Small Talk — Qwen3:14b) | Ollama Chat Model |
| Ollama Chat Model (Classifier — Qwen2.5:7b) | Ollama Chat Model |
| Postgres Chat Memory (RAG Answer) | PostgreSQL 聊天记忆 |
| Answer Generator AI Agent | AI Agent |
| Ollama Chat Model (Answer Generator — Qwen3:14b) | Ollama Chat Model |
| Loop Over Sub-Queries | 分批处理 |
| Ollama Embeddings (BGE-M3) | Ollama Embeddings |
| PGVector Store — Retrieve Chunks | PGVector 向量存储 |
| Remove Think Tags (Small Talk Path) | Code |
| Webhook | Webhook |
| Respond to Webhook | 响应 Webhook |
| Understand Request | LLM Chain |



## 功能说明

RAG 检索增强生成系统，基于文档向量库的知识问答，Webhook 触发。

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

- 节点总数：25
- 触发方式：Webhook 触发

## 触发方式
- Webhook 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：23
- 输出节点：1
- 分类：knowledge-rag
