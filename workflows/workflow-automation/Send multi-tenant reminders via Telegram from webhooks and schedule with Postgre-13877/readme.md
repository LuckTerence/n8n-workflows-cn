## 简介
**Send multi-tenant reminders via Telegram from webhooks and schedule with Postgres logging**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/13877

---

# Send multi-tenant reminders via Telegram from webhooks and schedule with Postgres logging


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



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Webhook触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：18
- 触发方式：定时触发, Webhook 触发, 表单提交触发

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
