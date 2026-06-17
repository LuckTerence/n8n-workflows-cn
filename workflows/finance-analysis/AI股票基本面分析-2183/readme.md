## 简介
**AI股票基本面分析**

自动分析股票基本面并生成Q&A报告

> 分类：金融分析 | 适配等级：A（需替换Google Drive/Supabase)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2183

---

# AI股票基本面分析


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| Google Drive | Google Drive |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter1 | 文本分割器 |
| Qdrant Vector Store | Qdrant 向量存储 |
| When chat message received | Chat 触发器 |
| Webhook | Webhook |
| Retrieval QA Chain | chainRetrievalQa |
| Vector Store Retriever | retrieverVectorStore |
| Qdrant Vector Store1 | Qdrant 向量存储 |
| OpenAI Chat Model | OpenAI Chat Model |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Embeddings OpenAI | OpenAI Embeddings |
| Respond to Webhook | 响应 Webhook |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，Webhook 触发。

Webhook触发、Chat 消息触发、手动触发，通过 HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：手动触发, Chat 消息触发, Webhook 触发

## 触发方式
- When clicking "Execute Workflow" 触发
- When chat message received 触发
- Webhook 触发

## 统计
- 节点总数：14
- 触发节点：3
- 处理节点：10
- 输出节点：1
- 分类：finance-analysis
