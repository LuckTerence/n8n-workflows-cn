# Build a Multichannel Customer Support AI Assistant with Chatwoot & OpenRouter

https://n8nworkflows.xyz/workflows/8260

## 节点清单

| 节点 | 类型 |
|------|------|
| Chatwoot Webhook | Webhook |
| Squize Webhook Data | 数据设置 |
| Check If Incoming Message | IF 判断 |
| Load Chatwoot Conversation History | HTTP Request |
| Process Loaded History | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Chatwoot Assistant | LLM Chain |
| Send Message | HTTP Request |

## 触发方式
- Chatwoot Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
