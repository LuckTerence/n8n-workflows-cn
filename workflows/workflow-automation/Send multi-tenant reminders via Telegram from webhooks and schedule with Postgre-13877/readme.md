# Send multi-tenant reminders via Telegram from webhooks and schedule with Postgres logging

https://n8nworkflows.xyz/workflows/13877

## 节点清单

| 节点 | 类型 |
|------|------|
| Every minute - check due events | 定时触发器 |
| Log success to database | PostgreSQL |
| Mark reminder as sent | PostgreSQL |
| Render Template | Code |
| Log error to database | PostgreSQL |
| Send reminder via Telegram | Telegram |
| Receive event via webhook | Webhook |
| Validate tenant token | Code |
| Map webhook fields | 数据设置 |
| Tenant registration form | 表单触发器 |
| Organize form data | Code |
| Show registration success | 表单 |
| Fetch events due for reminder | PostgreSQL |
| Fetch tenant config | PostgreSQL |
| Insert tenant rule | PostgreSQL |
| Insert tenant | PostgreSQL |
| No events due - skip | 空操作 |
| Route by channel type | IF 判断 |

## 触发方式
- Every minute - check due events 触发
- Receive event via webhook 触发
- Tenant registration form 触发

## 统计
- 节点总数：18
- 触发节点：3
- 处理节点：14
- 输出节点：1
- 分类：workflow-automation
