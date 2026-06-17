## 简介
**Connect AI to any chats in Kommo**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2841

---

# Connect AI to any chats in Kommo


## 节点清单

| 节点 | 类型 |
|------|------|
| isVoice | IF 判断 |
| get voice | HTTP Request |
| get_entity | HTTP Request |
| ai | AI Agent |
| model | OpenAI Chat Model |
| memory | 记忆缓冲区 |
| hasStopTag | Switch 路由 |
| transcribe voice | OpenAI |
| setText | 数据设置 |
| Get token | HTTP Request |
| Recieve message | HTTP Request |
| new_message | Webhook |

## 触发方式
- new_message 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
