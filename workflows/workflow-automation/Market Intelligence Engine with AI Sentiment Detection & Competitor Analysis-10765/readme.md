## 简介
**Market Intelligence Engine with AI Sentiment Detection & Competitor Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10765

---

# Market Intelligence Engine with AI Sentiment Detection & Competitor Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Data Collection | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch News Articles | HTTP Request |
| Fetch Blog Posts | HTTP Request |
| Fetch Social Media | HTTP Request |
| Fetch Academic Papers | HTTP Request |
| Fetch Code Repos | HTTP Request |
| Fetch Forum Discussions | HTTP Request |
| Fetch Product Docs | HTTP Request |
| Merge All Sources | 数据合并 |
| Normalize Content Schema | Code |
| Deduplicate Content | 去重 |
| Extract Entities & Topics | OpenAI |
| Parse Technical Signals | Code |
| Store Raw Data | PostgreSQL |
| Time-Series Analytics | Code |
| Topic Modeling & Velocity | Code |
| Sentiment Analysis | Code |
| Changepoint Detection | Code |
| Novelty Scoring | Code |
| Merge Analytics Signals | 数据合并 |
| MCDM Signal Fusion | Code |
| Rank Trends by Impact | Code |
| Store Trend Rankings | PostgreSQL |
| Check Alert Threshold | IF 判断 |
| Generate Trend Summary | OpenAI |
| Send Slack Alert | Slack |
| Send Email Report | Email 发送 |
| Trigger Workflow Actions | HTTP Request |
| Store Dashboard Data | PostgreSQL |
| Track KPIs | PostgreSQL |



## 功能说明

Market Intelligence Engine with AI Sentiment Detec（AI 增强)定时触发，通过 邮箱 + 数据库 + Slack + HTTP API 实现自动化。

定时触发，通过 邮箱 + 数据库 + Slack + HTTP API 实现自动化。

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

- 节点总数：31
- 触发方式：定时触发

## 触发方式
- Schedule Data Collection 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：20
- 输出节点：10
- 分类：workflow-automation
