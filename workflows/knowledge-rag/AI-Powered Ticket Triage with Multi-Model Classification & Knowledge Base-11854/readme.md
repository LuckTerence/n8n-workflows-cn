## 简介
**AI-Powered Ticket Triage with Multi-Model Classification & Knowledge Base**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11854

---

# AI-Powered Ticket Triage with Multi-Model Classification & Knowledge Base


## 节点清单

| 节点 | 类型 |
|------|------|
| Incoming Ticket Webhook | Webhook |
| Workflow Configuration | 数据设置 |
| Ticket Classifier Agent | AI Agent |
| OpenAI Chat Model - Classifier | OpenAI Chat Model |
| Classification Output Parser | 结构化输出解析器 |
| MCP Server Tools | MCP 客户端 |
| Knowledge Base Search | PGVector 向量存储 |
| Embeddings OpenAI - Search | OpenAI Embeddings |
| Check If Solution Found | IF 判断 |
| Format Auto-Resolution | 数据设置 |
| AI Solution Generator | AI Agent |
| OpenAI Chat Model - Solution | OpenAI Chat Model |
| Solution Output Parser | 结构化输出解析器 |
| Create Diagnostic Logs | Code |
| Check If Engineer Needed | IF 判断 |
| Notify Engineer | Slack |
| Update Ticket Status | PostgreSQL |
| Add to Knowledge Base | PGVector 向量存储 |
| Embeddings OpenAI - Insert | OpenAI Embeddings |
| Document Loader | 文档加载器 |
| Prepare KB Entry | 数据设置 |
| MCP Server Tools1 | MCP 客户端 |



## 功能说明

AI-Powered Ticket Triage with Multi-Model Classifi（AI 增强)Webhook 触发，通过 数据库 + HTTP API 实现自动化。

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

- 节点总数：22
- 触发方式：Webhook 触发

## 触发方式
- Incoming Ticket Webhook 触发

## 统计
- 节点总数：22
- 触发节点：1
- 处理节点：20
- 输出节点：1
- 分类：knowledge-rag
