## 简介
**Automated Job Hunter: Upwork Opportunity Aggregator & AI-Powered Notifier**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4733

---

# Automated Job Hunter: Upwork Opportunity Aggregator & AI-Powered Notifier


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Upwork Job Trigger | 定时触发器 |
| Fetch Upwork Jobs (Apify) | HTTP Request |
| Format Job Fields | 数据设置 |
| Log Jobs to Google Sheet | Google Sheets |
| Summarize Job Listings | AI Agent |
| Send Job Summary Email | Email 发送 |
| OpenAI Job Summarizer | OpenAI Chat Model |
| Parse Summary Output | 结构化输出解析器 |

## 触发方式
- Daily Upwork Job Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
