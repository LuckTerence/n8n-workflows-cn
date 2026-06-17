## 简介
**Natural Language Database Queries with Dual-Agent AI & PostgreSQL Integration**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5012

---

# Natural Language Database Queries with Dual-Agent AI & PostgreSQL Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Query agent | AI Agent |
| Think | 思考工具 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| OpenRouter Chat Model1 | OpenRouter Chat Model |
| Think1 | 思考工具 |
| Download File1 | Telegram |
| Transcribe1 | OpenAI |
| Telegram Trigger1 | Telegram 触发器 |
| Voice or Text | Switch 路由 |
| Text | 数据设置 |
| Merge | 数据合并 |
| Main agent | AI Agent |
| SEND MESSAGE | Telegram |
| CALL QUERY AGENT | 工作流工具 |
| ACCES DATABASE WITH DYNAMIC QUERYS | PostgreSQL |

## 触发方式
- When Executed by Another Workflow 触发
- Telegram Trigger1 触发

## 统计
- 节点总数：17
- 触发节点：2
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
