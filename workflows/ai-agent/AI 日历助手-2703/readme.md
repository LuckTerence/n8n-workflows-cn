## 简介
**AI 日历助手**

Telegram Bot AI 日程管理

> 分类：AI Agent | 适配等级：A（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
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



## 功能说明

AI 日历助手。

Chat 消息触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：6
- 触发方式：Chat 消息触发

## 触发方式

Telegram 消息触发

## 适配修改

- OpenAI → DeepSeek：Base URL 改为 `https://api.deepseek.com`，Model 改为 `deepseek-chat`
- Google Calendar 节点需手动替换为飞书日历 HTTP Request（参考飞书开放平台日历 API 文档）

## 统计

