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

## 触发方式
- Telegram-Bot 触发

## 统计
- 节点总数：31
- 触发节点：1
- 处理节点：23
- 输出节点：7
- 分类：workflow-automation
