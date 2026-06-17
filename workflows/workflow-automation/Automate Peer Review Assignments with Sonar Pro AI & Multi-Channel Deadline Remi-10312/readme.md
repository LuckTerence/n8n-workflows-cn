## 简介
**Automate Peer Review Assignments with Sonar Pro AI & Multi-Channel Deadline Reminders**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10312

---

# Automate Peer Review Assignments with Sonar Pro AI & Multi-Channel Deadline Reminders


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger | 手动触发 |
| Schedule Trigger | 定时触发器 |
| Webhook - Assignment Submission | Webhook |
| Extract Submission Data | 数据设置 |
| Read Assignment File | readPDF |
| AI Evaluation - Technical Criteria | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Store Evaluation Results | 数据设置 |
| Split Peer Reviewers | 数据拆分 |
| Create Evaluation Template | 数据设置 |
| Send Teams Notification | Teams |
| Send Discord Notification | Discord |
| Send Email with Template | Email 发送 |
| Save to Google Sheets - Grading | Google Sheets |
| Check Review Deadlines | Google Sheets |
| Filter Approaching Deadlines | 过滤器 |
| Send Deadline Reminder - Teams | Teams |
| Send Deadline Reminder - Discord | Discord |
| Send Deadline Reminder - Email | Email 发送 |
| Webhook Response | 响应 Webhook |
| OpenRouter Chat Model | OpenRouter Chat Model |



## 功能说明

Automate Peer Review Assignments with Sonar Pro AI（AI 增强)手动触发、定时触发、Webhook 触发，通过 邮箱 + 在线表格 + Discord + HTTP API 实现自动化。

定时触发、Webhook触发、手动触发，通过 邮箱 + 在线表格 + Discord + HTTP API 实现自动化。

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

- 节点总数：21
- 触发方式：手动触发, 定时触发, Webhook 触发

## 触发方式
- Manual Trigger 触发
- Schedule Trigger 触发
- Webhook - Assignment Submission 触发

## 统计
- 节点总数：21
- 触发节点：3
- 处理节点：11
- 输出节点：7
- 分类：workflow-automation
