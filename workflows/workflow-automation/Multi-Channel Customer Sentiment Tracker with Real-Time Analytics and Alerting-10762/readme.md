## 简介
**Multi-Channel Customer Sentiment Tracker with Real-Time Analytics and Alerting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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

## 触发方式
- Schedule Trigger - Poll Data Sources 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：16
- 输出节点：9
- 分类：workflow-automation
