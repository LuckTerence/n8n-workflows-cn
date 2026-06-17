## 简介
**AI Chatbot Call Center: Demo Call Center (Production-Ready, Part 2)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4045

---

# AI Chatbot Call Center: Demo Call Center (Production-Ready, Part 2)


## 节点清单

| 节点 | 类型 |
|------|------|
| Session | Redis |
| Input | 数据设置 |
| Test Trigger | Chat 触发器 |
| Test Fields | 数据设置 |
| Flow Trigger | 执行工作流触发器 |
| Rate Limit | Redis |
| If Rated | IF 判断 |
| Rated Output | 数据设置 |
| Chat Memory | 数据设置 |
| Channel Switch | Switch 路由 |
| AI Agent | AI Agent |
| xAI @grok-2-1212 | lmChatXAiGrok |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| Load User Memory | PostgreSQL 工具 |
| Save User Memory | PostgreSQL 工具 |
| Taxi Service | 工作流工具 |
| Provider | Redis |
| New Session | Redis |
| Output | 数据设置 |
| Code | Code |
| Test Output | 数据设置 |
| Chat Switch | Switch 路由 |
| Provider Switch | Switch 路由 |
| Error Output | 数据设置 |
| Taxi Service Redirect | 执行工作流 |
| Call Back | 执行工作流 |
| Taxi Booking Worker | 执行工作流 |

## 触发方式
- Test Trigger 触发
- Flow Trigger 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：25
- 输出节点：0
- 分类：ai-agent
