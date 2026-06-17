## 简介
**AI Chatbot Call Center: Taxi Booking Support (Production-Ready, Part 7)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4051

---

# AI Chatbot Call Center: Taxi Booking Support (Production-Ready, Part 7)


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| xAI @grok-2-1212 | lmChatXAiGrok |
| Status Switch | Switch 路由 |
| Set Cancel Booking | PostgreSQL |
| Schedule Trigger | 定时触发器 |
| Booking | 数据设置 |
| Call Back | 执行工作流 |
| Open Hold Booking | PostgreSQL |
| If Hold Expired | IF 判断 |
| If Open Expired | IF 判断 |
| Delete Event | Google Calendar |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：ai-agent
