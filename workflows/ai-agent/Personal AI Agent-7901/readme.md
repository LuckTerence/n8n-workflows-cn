## 简介
**Personal AI Agent**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7901

---

# Personal AI Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent | AI Agent |
| Send | Gmail 工具 |
| Reply | Gmail 工具 |
| Delete | Gmail 工具 |
| Get Many | Gmail 工具 |
| Gemini | OpenAI Chat Model |
| Telegram Trigger | Telegram 触发器 |
| Send a text message | Telegram |
| Gmail Trigger | Gmail 触发器 |
| Create Event | Google Calendar 工具 |
| Get Many2 | Google Calendar 工具 |
| Delete2 | Google Calendar 工具 |
| Send a text message1 | Telegram |
| If | IF 判断 |
| No Operation, do nothing | 空操作 |
| Date & Time | dateTimeTool |
| Basic LLM Chain | LLM Chain |
| Text Classifier | 文本分类器 |
| Update | Google Calendar 工具 |
| Reply to a message | Email 发送 |
| Not Business | Email 发送 |
| Reply to a message1 | Email 发送 |
| Get Contacts | Google Sheets 工具 |
| Add Contacts | Google Sheets 工具 |
| Client | Email 发送 |
| Sponsorship Request | Email 发送 |
| Simple Memory | 记忆缓冲区 |
| Gemini1 | OpenAI Chat Model |



## 功能说明

Personal AI Agent（AI 增强)Telegram 消息触发，通过 Telegram + 邮箱 + HTTP API 实现自动化。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- Telegram Bot Token → @BotFather 创建
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：28
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发
- Gmail Trigger 触发

## 统计
- 节点总数：28
- 触发节点：2
- 处理节点：19
- 输出节点：7
- 分类：ai-agent
