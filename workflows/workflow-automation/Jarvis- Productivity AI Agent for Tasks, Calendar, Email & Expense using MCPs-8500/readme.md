## 简介
**Jarvis: Productivity AI Agent for Tasks, Calendar, Email & Expense using MCPs**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8500

---

# Jarvis: Productivity AI Agent for Tasks, Calendar, Email & Expense using MCPs


## 节点清单

| 节点 | 类型 |
|------|------|
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Gmail MCP | MCP 客户端 |
| Google Tasks MCP | MCP 客户端 |
| Gmail MCP Server | MCP 触发器 |
| Send Email | Gmail 工具 |
| Reply to an Email | Gmail 工具 |
| Get Emails | Gmail 工具 |
| Add Label to Email | Gmail 工具 |
| Get Labels | Gmail 工具 |
| Draft Email | Gmail 工具 |
| Draft Email Reply | Gmail 工具 |
| Check Availability | Google Calendar 工具 |
| Get all Events | Google Calendar 工具 |
| Delete Calendar Event | Google Calendar 工具 |
| Reschedule Event | Google Calendar 工具 |
| Get Event | Google Calendar 工具 |
| Create an event | Google Calendar 工具 |
| Calendar MCP Server | MCP 触发器 |
| Calendar MCP | MCP 客户端 |
| Complete a Task | googleTasksTool |
| Task Manager MCP | MCP 触发器 |
| Telegram Trigger | Telegram 触发器 |
| Switch | Switch 路由 |
| Transcribe audio or video | elevenLabs |
| Finance Tracker | MCP 客户端 |
| Finance Manager MCP Server | MCP 触发器 |
| Get all Expenses | Google Sheets 工具 |
| Create Expense | Google Sheets 工具 |
| Delete Expense | Google Sheets 工具 |
| Get many Tasks | googleTasksTool |
| Delete a Task | googleTasksTool |
| Get a Task | googleTasksTool |
| Create a Task | googleTasksTool |
| Get a file | Telegram |
| Get Contacts | googleContactsTool |
| Google Contacts MCP | MCP 触发器 |
| Google Contacts | MCP 客户端 |
| Send a text message | Telegram |
| Jarvis | AI Agent |
| Only allow me | 过滤器 |
| Set Reply Message | 数据设置 |
| Check Text or Audio | Switch 路由 |
| Send an audio file | Telegram |
| Convert text to speech | elevenLabs |
| Think | 思考工具 |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码
- 通义万相 API Key → https://dashscope.aliyun.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：46
- 触发方式：Telegram 消息触发

## 触发方式
- Gmail MCP Server 触发
- Calendar MCP Server 触发
- Task Manager MCP 触发
- Telegram Trigger 触发
- Finance Manager MCP Server 触发
- Google Contacts MCP 触发

## 统计
- 节点总数：46
- 触发节点：6
- 处理节点：37
- 输出节点：3
- 分类：workflow-automation
