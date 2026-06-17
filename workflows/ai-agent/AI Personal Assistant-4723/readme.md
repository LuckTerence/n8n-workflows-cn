## 简介
**AI Personal Assistant**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4723

---

# AI Personal Assistant


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Get Email | Gmail 工具 |
| Anthropic Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| Google Calendar | Google Calendar 工具 |
| Check Sent | Gmail 工具 |
| Anthropic Chat Model1 | OpenAI Chat Model |
| Unread Emails - FYI | Gmail 工具 |
| Unread Emails - To Respond | Gmail 工具 |
| Email Assistant | AI Agent |
| Follow Up Assistant | AI Agent |
| Fetch FireFlies | HTTP Request 工具 |
| Check Sent1 | Gmail 工具 |
| Master Orchestrator Agent | AI Agent |
| Anthropic Chat Model2 | OpenAI Chat Model |
| Slack | slackTool |
| Slack1 | Slack |
| Check Slack Mentions | slackTool |
| Check Thread Mentions | slackTool |
| Get User | slackTool |
| Slack Assistant | AI Agent |
| Anthropic Chat Model3 | OpenAI Chat Model |
| Google Sheets | Google Sheets |
| Slack2 | Slack |
| Previous To Do | Google Sheets 工具 |
| Schedule Trigger | 定时触发器 |



## 功能说明

AI Personal Assistant（AI 增强)手动触发、定时触发，通过 邮箱 + 在线表格 + Slack + HTTP API 实现自动化。

定时触发、手动触发，通过 邮箱 + 在线表格 + Slack + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：26
- 触发方式：手动触发, 定时触发

## 触发方式
- When clicking ‘Test workflow’ 触发
- Schedule Trigger 触发

## 统计
- 节点总数：26
- 触发节点：2
- 处理节点：21
- 输出节点：3
- 分类：ai-agent
