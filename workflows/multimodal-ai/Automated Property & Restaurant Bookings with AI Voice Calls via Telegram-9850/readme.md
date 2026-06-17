## 简介
**Automated Property & Restaurant Bookings with AI Voice Calls via Telegram**

（待补充中文描述）

> 分类：多模态 AI | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9850

---

# Automated Property & Restaurant Bookings with AI Voice Calls via Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| Gemini 2.0 Flash | OpenAI Chat Model |
| Retell Create Call | HTTP Request |
| Retell Webhook | Webhook |
| AI Agent Parse Call | AI Agent |
| Gemini 2.0 Flash 2 | OpenAI Chat Model |
| Notify Success | Telegram |
| Get an event in Google Calendar | Google Calendar 工具 |
| Structured Output Parser | 结构化输出解析器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| Filter | 过滤器 |
| Create an event in Google Calendar | Google Calendar 工具 |
| Telegram Trigger | Telegram 触发器 |
| Send a text message | Telegram |
| Gemini 2.0 Flash1 | OpenAI Chat Model |
| Retell Create Call1 | HTTP Request |
| Get an event in Google Calendar1 | Google Calendar 工具 |
| Structured Output Parser1 | 结构化输出解析器 |
| Google Gemini Chat Model1 | OpenAI Chat Model |
| AI Agent Reserva Restaurantes | AI Agent |
| Switch | Switch 路由 |
| AI Agent: Property Viewings | AI Agent |



## 功能说明

Telegram 机器人，消息驱动自动化流程，Webhook 触发。

Webhook触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：21
- 触发方式：Webhook 触发, Telegram 消息触发

## 触发方式
- Retell Webhook 触发
- Telegram Trigger 触发

## 统计
- 节点总数：21
- 触发节点：2
- 处理节点：15
- 输出节点：4
- 分类：multimodal-ai
