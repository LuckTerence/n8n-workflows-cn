## 简介
**Send Automated Patient Appointment Reminders via Email & SMS with Multi-Database Support**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Twilio/Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6548

---

# Send Automated Patient Appointment Reminders via Email & SMS with Multi-Database Support


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook: New Appointment | Webhook |
| Extract Appointment Data | 数据设置 |
| Format & Validate Data | Code |
| Store in Google Sheets | Google Sheets |
| Store in Airtable | Airtable |
| Wait: 3 Days Before | 等待 |
| Send 3-Day Email Reminder | Email 发送 |
| Send 3-Day SMS Reminder | twilio |
| Update Google Sheets: 3-Day Sent | Google Sheets |
| Update Airtable: 3-Day Sent | Airtable |
| Wait: 1 Day Before | 等待 |
| Send 1-Day Email Reminder | Email 发送 |
| Send 1-Day SMS Reminder | twilio |
| Update Google Sheets: 1-Day Sent | Google Sheets |
| Update Airtable: 1-Day Sent | Airtable |
| Store in PostgreSQL | PostgreSQL |
| Update PostgreSQL: 3-Day Sent | PostgreSQL |
| Update PostgreSQL: 1-Day Sent | PostgreSQL |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Webhook触发，通过 邮箱 + 在线表格 + 数据库 + HTTP API 实现自动化。

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

- 节点总数：18
- 触发方式：Webhook 触发

## 触发方式
- Webhook: New Appointment 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
