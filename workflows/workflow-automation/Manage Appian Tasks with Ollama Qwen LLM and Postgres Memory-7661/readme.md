# Manage Appian Tasks with Ollama Qwen LLM and Postgres Memory

https://n8nworkflows.xyz/workflows/7661

## 节点清单

| 节点 | 类型 |
|------|------|
| Template Vars | 数据设置 |
| When chat message received | Chat 触发器 |
| Webhook | Webhook |
| Normalize Chat Input | 数据设置 |
| AI Agent | AI Agent |
| Ollama Chat Model | Ollama Chat Model |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| List Tasks (Appian) | HTTP Request 工具 |
| List Task Types (Appian) | HTTP Request 工具 |
| Create Task (Appian) | HTTP Request 工具 |
| Prepare Response | 数据设置 |
| Respond to Webhook | 响应 Webhook |

## 触发方式
- When chat message received 触发
- Webhook 触发

## 统计
- 节点总数：12
- 触发节点：2
- 处理节点：6
- 输出节点：4
- 分类：workflow-automation
