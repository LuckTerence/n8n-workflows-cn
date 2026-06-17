## 简介
**Create a Witty Telegram Bot with AI-Powered Humor, Roasts & Stats using OpenRouter**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7655

---

# Create a Witty Telegram Bot with AI-Powered Humor, Roasts & Stats using OpenRouter


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Telegram | Telegram 触发器 |
| OpenRouter Commands | OpenRouter Chat Model |
| Init Database | PostgreSQL |
| Log message + statistics | PostgreSQL |
| Adding a schedule | PostgreSQL |
| Schedule | 定时触发器 |
| Get scheduled posts | PostgreSQL |
| Chat history | PostgreSQL |
| Mention Analysis | Code |
| Get user statistics | PostgreSQL |
| Get top users | PostgreSQL |
| AI response to command | AI Agent |
| Generating an information response | Code |
| Response type | IF 判断 |
| Send info reply | Telegram |
| Send AI response | Telegram |
| AI response to mention | AI Agent |
| Reply to Mention | Telegram |
| AI post generation | AI Agent |
| Submit scheduled post | Telegram |
| Save Bot Response | PostgreSQL |
| If | IF 判断 |
| Switch | Switch 路由 |
| Log command | PostgreSQL |
| If1 | IF 判断 |
| Save Bot Response2 | PostgreSQL |



## 功能说明

Telegram 机器人，消息驱动自动化流程，定时执行。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：Telegram 消息触发, 定时触发

## 触发方式
- Webhook Telegram 触发
- Schedule 触发

## 统计
- 节点总数：26
- 触发节点：2
- 处理节点：20
- 输出节点：4
- 分类：workflow-automation
