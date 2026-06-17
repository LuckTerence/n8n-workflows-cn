## 简介
**Create Secure Human-in-the-Loop Approval Flows with Postgres and Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发。

Webhook触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建
- 数据库连接信息

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Webhook 触发

## 触发方式
- 01 Webhook Trigger: Approval Decision 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：workflow-automation
