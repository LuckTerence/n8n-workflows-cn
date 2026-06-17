## 简介
**Create Secure Human-in-the-Loop Approval Flows with Postgres and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：20 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/9039

---

# Create Secure Human-in-the-Loop Approval Flows with Postgres and Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| 01 Webhook Trigger: Approval Decision | Webhook |
| 02 FN: Verify Signature + TTL | Code |
| 04c DB: Update Ticket Status | PostgreSQL |
| 04c1 DB: Get Ticket Owner | PostgreSQL |
| 04c1a IF: Resolved or In Progress | IF 判断 |
| 05c1a Telegram: Notify Resolved | Telegram |
| 05c1b Telegram: Notify In Progress | Telegram |
| 05c Telegram: Update Confirmation | Telegram |
| Notify Failed? | IF 判断 |
| Execute a SQL query | PostgreSQL |
| 04c2 DB: Insert Audit Row | PostgreSQL |
| Text (reject) | Telegram |
| 04r0 DB: Get Ticket ID | PostgreSQL |
| Execute a SQL query1 | PostgreSQL |
| If Resolved | IF 判断 |
| If in_progress | IF 判断 |
| Actions | Switch 路由 |
| 04e DB: Insert Audit Expired | PostgreSQL |
| 04i DB: Insert Audit Invalid | PostgreSQL |
| 05e Telegram: Notify Expired | Telegram |
| 05i Telegram: Alert Invalid | Telegram |

## 触发方式
- 01 Webhook Trigger: Approval Decision 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：workflow-automation
