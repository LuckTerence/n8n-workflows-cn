## 简介
**AI-Powered Personal Assistant for Telegram with Memory & Task Management**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8837

---

# AI-Powered Personal Assistant for Telegram with Memory & Task Management


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Merge1 | 数据合并 |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Window Buffer Memory1 | 记忆缓冲区 |
| Telegram Response | Telegram |
| User Tele Memory | Airtable 工具 |
| Zeus Text Memory | Airtable 工具 |
| Grocery Search | Airtable 工具 |
| Grocery Create | Airtable 工具 |
| Grocery Delete | Airtable 工具 |
| Get Memories | Airtable |
| Aggregate | 数据聚合 |
| OpenAI | OpenAI |
| Switch | Switch 路由 |
| Telegram | Telegram |
| Get Events | Google Calendar 工具 |
| Create Events | Google Calendar 工具 |
| Delete Events | Google Calendar 工具 |
| Update Events | Google Calendar 工具 |
| To-Do Search | Airtable 工具 |
| To-Do Create | Airtable 工具 |
| To-Do Delete | Airtable 工具 |
| Zeus Tele | AI Agent |
| Create Recurring Events | Google Calendar 工具 |
| SerpAPI | SerpApi 工具 |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：25
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：25
- 触发节点：1
- 处理节点：22
- 输出节点：2
- 分类：ai-agent
