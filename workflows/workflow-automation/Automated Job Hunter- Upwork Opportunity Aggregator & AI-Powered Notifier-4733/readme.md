## 简介
**Automated Job Hunter: Upwork Opportunity Aggregator & AI-Powered Notifier**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Slack/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4733

---

# Automated Job Hunter: Upwork Opportunity Aggregator & AI-Powered Notifier


## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Upwork Job Trigger | 定时触发器 |
| Fetch Upwork Jobs (Apify) | HTTP Request |
| Format Job Fields | 数据设置 |
| Log Jobs to Google Sheet | Google Sheets |
| Summarize Job Listings | AI Agent |
| Send Job Summary Email | Email 发送 |
| OpenAI Job Summarizer | OpenAI Chat Model |
| Parse Summary Output | 结构化输出解析器 |



## 功能说明

通知推送系统，多渠道消息分发，定时执行。

定时触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：8
- 触发方式：定时触发

## 触发方式
- Daily Upwork Job Trigger 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：workflow-automation
