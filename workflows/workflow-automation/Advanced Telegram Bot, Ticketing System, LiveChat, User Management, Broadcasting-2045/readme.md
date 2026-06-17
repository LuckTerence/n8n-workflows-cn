## 简介
**Advanced Telegram Bot, Ticketing System, LiveChat, User Management, Broadcasting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2045

---

# Advanced Telegram Bot, Ticketing System, LiveChat, User Management, Broadcasting


## 节点清单

| 节点 | 类型 |
|------|------|
| New User ? | IF 判断 |
| Format | Code |
| Bot-Fields | 数据设置 |
| Create Topic (Chat Ticket) | HTTP Request |
| Save Topic ID | Redis |
| Get User Chat Topic | Redis |
| Forward New Message | HTTP Request |
| IF No Topic Created | IF 判断 |
| ReCreate Topic (Chat Ticket) | HTTP Request |
| ReSave Topic ID | Redis |
| Update User Data | Redis |
| Save User Data | Redis |
| Support Forum | IF 判断 |
| From Ticket | IF 判断 |
| Forward Support Reply To User | HTTP Request |
| IF Topic Created | IF 判断 |
| Forward New Message to the recrated topic | HTTP Request |
| No Operation, do nothing | 空操作 |
| Check User in Database | Redis |
| Send User Ticket Created Notification | Telegram |
| Bot-Config | 数据设置 |
| Telegram-Bot | Telegram 触发器 |
| 1st | Switch 路由 |
| Split In Batches1 | 分批处理 |
| Wait1 | 等待 |
| Format Users | Code |
| Broadcast Channel Post into Users | HTTP Request |
| Set Blocked Member | Redis |
| IF Verified Channel | IF 判断 |
| Filter Blocked Users | 过滤器 |
| Retrieve all users in DB | Redis |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：31
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram-Bot 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：23
- 输出节点：7
- 分类：workflow-automation
