# AI-Powered Invoice Reminder & Payment Tracker for Finance & Accounting

https://n8nworkflows.xyz/workflows/10111

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Daily Check | 定时触发器 |
| Fetch Pending Invoices | PostgreSQL |
| Filter Overdue Invoices | IF 判断 |
| Calculate Reminder Logic | Code |
| Prepare AI Prompt | 数据设置 |
| Format Email | Code |
| Send Email Reminder | Email 发送 |
| Update Reminder Status | PostgreSQL |
| Create Activity Log | 数据设置 |
| Save to Activity Log | PostgreSQL |
| Generate Daily Summary | Code |
| Send Summary to Finance Team | Email 发送 |
| Webhook: Payment Received | Webhook |
| Update Payment Status | PostgreSQL |
| Webhook Response | 响应 Webhook |
| Send Payment Confirmation | Email 发送 |
| Generate Email | OpenAI Chat Model |
| AI Agent For Generate Email Content | AI Agent |

## 触发方式
- Schedule Daily Check 触发
- Webhook: Payment Received 触发

## 统计
- 节点总数：18
- 触发节点：2
- 处理节点：12
- 输出节点：4
- 分类：finance-analysis
