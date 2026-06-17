## 简介
**Allow Users to Send a Sequence of Messages to an AI Agent in Telegram**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2917

---

# Allow Users to Send a Sequence of Messages to an AI Agent in Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Reply | Telegram |
| Receive Message | Telegram 触发器 |
| Wait 10 Seconds | 等待 |
| Add to Queued Messages | Supabase |
| No Operation, do nothing | 空操作 |
| Aggregate | 数据聚合 |
| Delete Queued Messages | Supabase |
| OpenAI Chat Model | OpenAI Chat Model |
| Sort by Message ID | 数据排序 |
| Get Queued Messages | Supabase |
| Check Most Recent Message | IF 判断 |
| AI Agent | AI Agent |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |

## 触发方式
- Receive Message 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：11
- 输出节点：1
- 分类：ai-agent
