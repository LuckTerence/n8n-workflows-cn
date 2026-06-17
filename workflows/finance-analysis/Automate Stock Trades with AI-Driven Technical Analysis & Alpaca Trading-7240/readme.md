## 简介
**Automate Stock Trades with AI-Driven Technical Analysis & Alpaca Trading**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7240

---

# Automate Stock Trades with AI-Driven Technical Analysis & Alpaca Trading


## 节点清单

| 节点 | 类型 |
|------|------|
| Think | 思考工具 |
| Supabase Vector Store | Supabase 向量存储 |
| Supabase Vector Store1 | Supabase 向量存储 |
| Embeddings OpenAI | OpenAI Embeddings |
| Default Data Loader | 文档加载器 |
| Recursive Character Text Splitter | 文本分割器 |
| Embeddings OpenAI1 | OpenAI Embeddings |
| Reranker Cohere | rerankerCohere |
| ranking | HTTP Request 工具 |
| sectors | HTTP Request 工具 |
| industries | HTTP Request 工具 |
| Technical Analysis Tool1 | 工作流工具 |
| Trends Analysis Tool1 | 工作流工具 |
| Think2 | 思考工具 |
| Edit Fields1 | 数据设置 |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| Download Chart | HTTP Request |
| Get Chart URL | HTTP Request |
| Get Price History | HTTP Request |
| Get Bollinger Bands | HTTP Request |
| Get MACD | HTTP Request |
| Merge | 数据合并 |
| Calculate Support Resistance | Code |
| Organizing Data | Code |
| Merge-2 | 数据合并 |
| Set Variable | 数据设置 |
| Warp as JSON for GPT | Code |
| Set Final Response | 数据设置 |
| Set Stock Symbol and API Key | 数据设置 |
| First Technical Analysis | OpenAI |
| Edit Fields | 数据设置 |
| Aggregate1 | 数据聚合 |
| Code | Code |
| Generate Variables For API1 | Code |
| Get News Data1 | HTTP Request |
| Split Out2 | 数据拆分 |
| Limit1 | 数据限制 |
| Aggregate2 | 数据聚合 |
| Split Out3 | 数据拆分 |
| Edit Fields3 | 数据设置 |
| Code1 | Code |
| Edit Fields4 | 数据设置 |
| Edit Fields5 | 数据设置 |
| Calculator | 计算器工具 |
| save order info | PostgreSQL 工具 |
| POST endpoints | HTTP Request 工具 |
| GET endpoints | HTTP Request 工具 |
| Trader Agent | AI Agent |
| strategy agent | AI Agent |
| GET cash | HTTP Request 工具 |
| Think1 | 思考工具 |
| Calculator1 | 计算器工具 |
| Schedule Trigger | 定时触发器 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| GET cash1 | HTTP Request 工具 |
| Strategy Agent | agentTool |
| Think3 | 思考工具 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| OpenRouter Chat Model3 | OpenRouter Chat Model |
| HTTP Request1 | HTTP Request |
| Filter | 过滤器 |
| Send report | Email 发送 |
| Trend + Technical Agent | AI Agent |
| MAIN AGENT | AI Agent |
| current trades | PostgreSQL 工具 |
| current trades1 | PostgreSQL 工具 |
| Grok 4 | OpenRouter Chat Model |
| Call trend + technical Agent | 工作流工具 |
| Markdown to HTML | Markdown |
| Anthropic Chat Model | OpenAI Chat Model |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发，通过 邮箱 + 数据库 + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：70
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：70
- 触发节点：1
- 处理节点：54
- 输出节点：15
- 分类：finance-analysis
