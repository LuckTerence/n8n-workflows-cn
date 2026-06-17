## 简介
**Automate B2B SaaS Renewal Risk Management with CRM, Support & Usage Data**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11469

---

# Automate B2B SaaS Renewal Risk Management with CRM, Support & Usage Data


## 节点清单

| 节点 | 类型 |
|------|------|
| analytivcs | HTTP Request |
| Get data related to an organization | zendesk |
| daily trigger | 定时触发器 |
| Init config & thresholds | 数据设置 |
| Fetch subscriptions expiring in J+30 | PostgreSQL |
| Process subscriptions in batches | 分批处理 |
| HubSpot – Get engagement history | hubspot |
| Salesforce – Get account details | salesforce |
| Pipedrive – Get deal activities | pipedrive |
| Pipedrive – Get deal products | pipedrive |
| Analytics API – Feature usage | HTTP Request |
| Scoring API – Call | HTTP Request |
| Normalize scoring response | 数据设置 |
| Compute churn score & level | 数据设置 |
| Route by churn risk (HIGH / MEDIUM / LOW) | Switch 路由 |
| Build daily summary | 数据聚合 |
| Email – LOW info | Email 发送 |
| Email – CSM/AM HIGH | Email 发送 |
| Email – CSM/ AM MEDIUM | Email 发送 |
| jira ticket | jira |
| Slack notification | Slack |
| Data personalisation | 空操作 |
| Prepare log payload | 数据设置 |
| Build summary line | 数据设置 |
| Engagement call | HTTP Request |
| Reporting email | Email 发送 |
| prepare daily summary | PostgreSQL |
| Trello Create MEDIUM risk card1 | trello |
| Trello Create HIGH risk card | trello |
| Data merge | 数据合并 |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发，通过 邮箱 + 数据库 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：30
- 触发方式：定时触发

## 触发方式
- daily trigger 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：20
- 输出节点：9
- 分类：workflow-automation
