## 简介
**Lightweight Support Desk with Telegram and Postgres Database Tracking**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8789

---

# Lightweight Support Desk with Telegram and Postgres Database Tracking


## 节点清单

| 节点 | 类型 |
|------|------|
| 01 Telegram Trigger: Intake + Status | Telegram 触发器 |
| 02 Switch: Route by Command | Switch 路由 |
| 03a FN: Normalize + Hash | Code |
| 04a DB: Upsert Ticket | PostgreSQL |
| 05a Telegram Ack | Telegram |
| 03b FN: Parse Status Command | Code |
| 04b DB: Get Ticket Status | PostgreSQL |
| 05b Telegram: Status Reply | Telegram |
| 03b1 IF: Has Correlation ID | IF 判断 |
| 05b Telegram: Status Reply (Error) | Telegram |
| Telegram: Invalid Command | Telegram |
| 03c FN: Parse Update Command | Code |
| 03c1 IF: Has Correlation ID | IF 判断 |
| Send a text message | Telegram |
| 03c2 IF: Valid Status | IF 判断 |
| 05c Telegram: Invalid Status | Telegram |
| 04c DB: Update Ticket Status | PostgreSQL |
| 03c0 IF: Is Operator | IF 判断 |
| 05c0 Telegram: Unauthorized Update Attempt | Telegram |
| 04c1 DB: Get Ticket Owner | PostgreSQL |
| 04b1 IF: Ticket Belongs To User | IF 判断 |
| 05b1 Telegram: Unauthorized Status Check | Telegram |
| 04c1a IF: Resolved or In Progress | IF 判断 |
| 05c1a Telegram: Notify Resolved | Telegram |
| 05c1b Telegram: Notify In Progress | Telegram |
| 05c Telegram: Update Confirmation | Telegram |
| 04b0 IF: DB Lookup Failed? | IF 判断 |
| 05b0 Telegram: Status DB Error | Telegram |
| 05c0 IF: Operator Reply Failed? | IF 判断 |
| Telegram: Admin Alert — Operator Reply Failed | Telegram |
| Notify Failed? | IF 判断 |
| Execute a SQL query | PostgreSQL |
| 04c2 DB: Insert Audit Row | PostgreSQL |
| 04b1 IF: No Ticket Found | IF 判断 |
| Send a text message1 | Telegram |
| 03b IF: Has Valid Correlation ID Format | IF 判断 |
| Send a text message2 | Telegram |
| Welcome Message | Telegram |
| Send a text message3 | Telegram |
| Check Admin | IF 判断 |
| DB: List Tickets | PostgreSQL |
| Send a text message4 | Telegram |
| Code in JavaScript | Code |

## 触发方式
- 01 Telegram Trigger: Intake + Status 触发

## 统计
- 节点总数：43
- 触发节点：1
- 处理节点：24
- 输出节点：18
- 分类：workflow-automation
