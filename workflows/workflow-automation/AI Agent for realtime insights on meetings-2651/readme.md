# AI Agent for realtime insights on meetings

https://n8nworkflows.xyz/workflows/2651

## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI1 | OpenAI |
| Insert Transcription Part | PostgreSQL |
| Create Note | PostgreSQL 工具 |
| Create Recall bot | HTTP Request |
| Create OpenAI thread | HTTP Request |
| Create data record | Supabase |
| Scenario 1 Start - Edit Fields | 数据设置 |
| Scenario 2 Start - Webhook | Webhook |
| If Jimmy word | IF 判断 |

## 触发方式
- Scenario 2 Start - Webhook 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
