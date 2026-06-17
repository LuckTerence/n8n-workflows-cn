# Send Automated Patient Appointment Reminders via Email & SMS with Multi-Database Support

https://n8nworkflows.xyz/workflows/6548

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

## 触发方式
- Webhook: New Appointment 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
