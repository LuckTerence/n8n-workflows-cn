# Automate Telegram Support Handover from AI to Humans with GPT4 and Email Alerts

https://n8nworkflows.xyz/workflows/9987

## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Configuration | 数据设置 |
| Confirm Operator | Telegram |
| User Approved | IF 判断 |
| Alert Operator | Email 发送 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Operator Confirmed | IF 判断 |
| Operator Attendance | Telegram |
| Operator Declined Attendance | Telegram |
| AI Agent | AI Agent |
| Simple Memory | 记忆缓冲区 |
| Reply To User | Telegram 工具 |
| Human Requested | IF 判断 |
| Azure OpenAI Chat Model | Azure OpenAI Chat Model |
| Update Last Message | 数据表 |
| Last Message Exists | 数据表 |
| Row is Empty | IF 判断 |
| Create Temporary Message | 数据表 |
| Update Temporary Message | 数据表 |
| Get Temporary Message | 数据表 |
| Message Router | Switch 路由 |
| Personal | 数据设置 |
| Create Topic | HTTP Request |
| Text Message | IF 判断 |
| Stop Workflow | 空操作 |
| Forward Message To Group | HTTP Request |
| Topic Message | IF 判断 |
| Chat Admins | HTTP Request |
| Forward Message | HTTP Request |
| Personal Trigger | Telegram 触发器 |
| Exit | IF 判断 |
| Close Topic | HTTP Request |
| Update Closed Topic | 数据表 |

## 触发方式
- Telegram Trigger 触发
- Personal Trigger 触发

## 统计
- 节点总数：33
- 触发节点：2
- 处理节点：21
- 输出节点：10
- 分类：devops
