## 简介
**AI-Powered Stock Analysis with Danelfin, TwelveData and Alpha Vantage**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7261

---

# AI-Powered Stock Analysis with Danelfin, TwelveData and Alpha Vantage


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
| Send report | Email 发送 |
| Trend + Technical Agent | AI Agent |
| MAIN AGENT | AI Agent |
| Grok 4 | OpenRouter Chat Model |
| Call trend + technical Agent | 工作流工具 |
| Markdown to HTML | Markdown |
| Slack Trigger | slackTrigger |
| Telegram Trigger | Telegram 触发器 |
| Gmail Trigger | Gmail 触发器 |
| WhatsApp Trigger | whatsAppTrigger |
| Set message variable | 数据设置 |
| When chat message received | Chat 触发器 |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警。

Chat 消息触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：54
- 触发方式：Telegram 消息触发, Chat 消息触发

## 触发方式
- Slack Trigger 触发
- Telegram Trigger 触发
- Gmail Trigger 触发
- WhatsApp Trigger 触发
- When chat message received 触发

## 统计
- 节点总数：54
- 触发节点：5
- 处理节点：39
- 输出节点：10
- 分类：workflow-automation
