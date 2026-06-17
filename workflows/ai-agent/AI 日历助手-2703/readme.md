## 简介
**AI 日历助手**

Telegram Bot AI 日程管理

> 分类：AI Agent | 适配等级：A-adapted（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/2703

---

# AI 日历助手


通过 Telegram Bot 接收自然语言指令，由 AI Agent 理解意图后调用日历工具完成日程管理。

## 节点

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| AI Agent | AI Agent |
| OpenAI Chat Model → **DeepSeek** | OpenAI Chat Model（已替换） |
| Google Calendar Tool | 日历工具 |
| Webhook Response | 响应输出 |

## 触发方式

Telegram 消息触发

## 适配修改

- OpenAI → DeepSeek：Base URL 改为 `https://api.deepseek.com`，Model 改为 `deepseek-chat`
- Google Calendar 节点需手动替换为飞书日历 HTTP Request（参考飞书开放平台日历 API 文档）

## 统计

- 节点数：5 · 分类：ai-agent
