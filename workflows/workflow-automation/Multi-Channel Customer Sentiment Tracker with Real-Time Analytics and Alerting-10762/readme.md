## 简介
**Multi-Channel Customer Sentiment Tracker with Real-Time Analytics and Alerting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10762

---

# Multi-Channel Customer Sentiment Tracker with Real-Time Analytics and Alerting


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger - Poll Data Sources | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch Social Media Feedback | HTTP Request |
| Fetch Email Feedback | HTTP Request |
| Fetch Support Tickets | HTTP Request |
| Fetch Chat Transcripts | HTTP Request |
| Fetch Product Reviews | HTTP Request |
| Merge All Feedback Sources | 数据合并 |
| Clean and Normalize Text Data | Code |
| Unify Data Schema | 数据设置 |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Sentiment Analysis - Positive/Neutral/Negative | sentimentAnalysis |
| OpenAI - Emotion Detection | OpenAI |
| OpenAI - Entity Extraction | OpenAI |
| Combine Analysis Results | 数据设置 |
| Store Feedback in Database | PostgreSQL |
| Calculate Sentiment Trends | Code |
| Aggregate by Entity and Time Period | 数据聚合 |
| Check for Negative Spike | IF 判断 |
| Check for Sudden Sentiment Shift | IF 判断 |
| Send Alert to Slack | Slack |
| Send Alert Email | Email 发送 |
| Update Dashboard - Google Sheets | Google Sheets |
| Sync to CRM System | HTTP Request |
| Sync to Marketing Automation | HTTP Request |
| Generate Insights Report | Code |



## 功能说明

监控告警系统，异常检测并发送通知，定时执行。

定时触发，通过 邮箱 + 在线表格 + 数据库 + Slack + HTTP API 实现自动化。

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

- 节点总数：26
- 触发方式：定时触发

## 触发方式
- Schedule Trigger - Poll Data Sources 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：16
- 输出节点：9
- 分类：workflow-automation
