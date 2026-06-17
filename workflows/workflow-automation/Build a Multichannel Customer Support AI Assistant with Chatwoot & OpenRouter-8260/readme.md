## 简介
**Build a Multichannel Customer Support AI Assistant with Chatwoot & OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8260

---

# Build a Multichannel Customer Support AI Assistant with Chatwoot & OpenRouter


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
