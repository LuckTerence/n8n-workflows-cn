## 简介
**Scalable Multi-Agent Chat Using @mentions**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3473

---

# Scalable Multi-Agent Chat Using @mentions


## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| AI Agent | AI Agent |
| Loop Over Items | 分批处理 |
| Extract mentions | Code |
| Simple Memory | 记忆缓冲区 |
| Set last Assistant message as input | 数据设置 |
| Set user message as input | 数据设置 |
| First loop? | IF 判断 |
| Set lastAssistantMessage | 数据设置 |
| Combine and format responses | Code |
| Define Global Settings | Code |
| Define Agent Settings | Code |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：13
- 触发节点：1
- 处理节点：12
- 输出节点：0
- 分类：ai-agent
