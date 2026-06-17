## 简介
**AI Chatbot Call Center: Taxi Booking Support (Production-Ready, Part 7)**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
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



## 功能说明

AI 聊天机器人，支持多轮对话和智能回复，定时执行。

定时触发，通过 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：11
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：10
- 输出节点：0
- 分类：ai-agent
