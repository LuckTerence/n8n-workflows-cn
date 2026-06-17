## 简介
**Gumroad Clientbell: Auto-Log Sales, Ping Telegram, & Thank via Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Twilio/Notion/Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3469

---

# Gumroad Clientbell: Auto-Log Sales, Ping Telegram, & Thank via Email


## 节点清单

| 节点 | 类型 |
|------|------|
| Google Sheets | Google Sheets |
| This is SET to Clean & Extract | 数据设置 |
| Gumroad Sales Trigger | gumroadTrigger |
| Telegram | Telegram |
| If | IF 判断 |
| Prepare a manual email to replicate | 数据设置 |
| Gmail | Email 发送 |
| Ready to take this to the next level? We at Innovatio are cheering for you!!! Best of luck and great successes to you all <3 Velebit from Innovatio | 空操作 |
| Airtable1 | Airtable |
| HubSpot | hubspot |
| Notion | Notion |
| Twilio | twilio |
| Send Email | Email 发送 |
| Microsoft Outlook | Outlook |
| Email Writer Agent | AI Agent |



## 功能说明

邮件自动化处理，AI 分类整理或。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：15
- 触发方式：手动或子流程调用

## 触发方式
- Gumroad Sales Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：10
- 输出节点：4
- 分类：workflow-automation
