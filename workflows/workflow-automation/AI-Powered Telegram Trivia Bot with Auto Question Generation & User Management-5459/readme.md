## 简介
**AI-Powered Telegram Trivia Bot with Auto Question Generation & User Management**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5459

---

# AI-Powered Telegram Trivia Bot with Auto Question Generation & User Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Parse Telegram Data | Code |
| Check Existing User | NocoDB |
| User Exists? | IF 判断 |
| Create New User | NocoDB |
| Merge User Data | Code |
| Is Command? | IF 判断 |
| Command Router | Switch 路由 |
| Handle Basic Commands | Code |
| Format Question | Code |
| Update User Game State | NocoDB |
| Get Leaderboard | NocoDB |
| Format Leaderboard | Code |
| Valid Answer? | IF 判断 |
| Get Current Question | NocoDB |
| Process Answer | Code |
| Update User Stats | NocoDB |
| Handle Unknown Text | Code |
| Telegram | Telegram |
| Merge | 数据合并 |
| OpenAI | OpenAI |
| NocoDB | nocoDbTool |
| Daily Question Generator | 定时触发器 |
| Get Possible Categories | Code |
| Send New Questions Available Notification | Telegram |
| Merge1 | 数据合并 |
| Aggregate | 数据聚合 |
| Get User History | NocoDB |
| Mark Question As Answered | NocoDB |
| Aggregate1 | 数据聚合 |
| Get Random Question | NocoDB |

## 触发方式
- Telegram Trigger 触发
- Daily Question Generator 触发

## 统计
- 节点总数：31
- 触发节点：2
- 处理节点：27
- 输出节点：2
- 分类：workflow-automation
