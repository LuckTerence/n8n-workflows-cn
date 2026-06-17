## 简介
**Proxmox AI Agent with n8n and Generative AI Integration**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2749

---

# Proxmox AI Agent with n8n and Generative AI Integration


## 节点清单

| 节点 | 类型 |
|------|------|
| HTTP Request1 | HTTP Request |
| Proxmox API Documentation | HTTP 工具 |
| Auto-fixing Output Parser | 自动修复输出解析器 |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Proxmox | HTTP 工具 |
| HTTP Request | HTTP Request |
| Google Gemini Chat Model2 | OpenAI Chat Model |
| When chat message received | Chat 触发器 |
| Telegram Trigger | Telegram 触发器 |
| Gmail Trigger | Gmail 触发器 |
| Webhook | Webhook |
| Proxmox API Wiki | HTTP 工具 |
| Structure Response | Code |
| Structgure Response from Proxmox | Code |
| Format Response and Hide Sensitive Data | Code |
| If | IF 判断 |
| HTTP Request2 | HTTP Request |
| Merge | 数据合并 |
| HTTP Request3 | HTTP Request |
| Google Gemini Chat Model | OpenAI Chat Model |
| AI Agent1 | AI Agent |
| If1 | IF 判断 |
| HTTP Request4 | HTTP Request |
| Merge1 | 数据合并 |
| AI Agent | AI Agent |
| Switch | Switch 路由 |

## 触发方式
- When chat message received 触发
- Telegram Trigger 触发
- Gmail Trigger 触发
- Webhook 触发

## 统计
- 节点总数：27
- 触发节点：4
- 处理节点：15
- 输出节点：8
- 分类：ai-agent
