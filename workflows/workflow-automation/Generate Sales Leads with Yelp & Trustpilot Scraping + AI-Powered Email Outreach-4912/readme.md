## 简介
**Generate Sales Leads with Yelp & Trustpilot Scraping + AI-Powered Email Outreach**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4912

---

# Generate Sales Leads with Yelp & Trustpilot Scraping + AI-Powered Email Outreach


## 节点清单

| 节点 | 类型 |
|------|------|
| Form Trigger - Get User Input | 表单触发器 |
| AI Location Analyzer | AI Agent |
| Split Sub-locations | Code |
| Loop Yelp Locations | 分批处理 |
| Yelp Scraper | HTTP Request |
| Check Yelp Scrape Progress | HTTP Request |
| Wait (1 min) Yelp Completion | 等待 |
| Verify Yelp Ready | IF 判断 |
| If Yelp Has Records | IF 判断 |
| Fetch Yelp Results | HTTP Request |
| Save Yelp Data to Sheet | Google Sheets |
| Clean Unique Websites | Code |
| Read Yelp Sheet Websites | Google Sheets |
| Make Trustpilot URLs | Code |
| Remove Duplicate TP URLs | Code |
| Loop Trustpilot URLs | 分批处理 |
| Trigger Trustpilot Scraper | HTTP Request |
| Check Trustpilot Scrape Progress | HTTP Request |
| Verify Trustpilot Scraper Ready | IF 判断 |
| Wait (1 min) Trustpilot Completion | 等待 |
| If Trustpilot Has Records | IF 判断 |
| Download Trustpilot Data | HTTP Request |
| Save Trustpilot Data to Sheet | Google Sheets |
| Read Emails from Trustpilot Sheet | Google Sheets |
| Get Unique Emails | Code |
| AI Generate Email Content | AI Agent |
| Parse Email JSON | Code |
| Send Outreach Email | Email 发送 |
| Gemini - Location AI Model | OpenAI Chat Model |
| Claude - Email AI Model | OpenAI Chat Model |



## 功能说明

邮件自动化处理，AI 分类整理或。

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

- 节点总数：30
- 触发方式：表单提交触发

## 触发方式
- Form Trigger - Get User Input 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：22
- 输出节点：7
- 分类：workflow-automation
