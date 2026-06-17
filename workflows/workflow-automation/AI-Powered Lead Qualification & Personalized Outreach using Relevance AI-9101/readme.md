## 简介
**AI-Powered Lead Qualification & Personalized Outreach using Relevance AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Zoom/Gmail/Notion/Google Sheets/Stripe/Slack)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9101

---

# AI-Powered Lead Qualification & Personalized Outreach using Relevance AI


## 节点清单

| 节点 | 类型 |
|------|------|
| Form | 表单触发器 |
| Router | Switch 路由 |
| Edit Fields | 数据设置 |
| score individual (Relevance) | HTTP Request |
| score company (Relevance) | HTTP Request |
| Summarize_N_score | LLM Chain |
| Structured Output | Code |
| Deepseek | OpenRouter Chat Model |
| Gemini | OpenAI Chat Model |
| Deepseek R1 | OpenRouter Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Email Personalizer (HOT) | LLM Chain |
| Email Personalizer (WARM) | LLM Chain |
| Email Personalizer (COLD) | LLM Chain |
| Create a draft | Email 发送 |
| Update CRM | Google Sheets |
| Notify team | Slack |
| Set data | 数据设置 |
| Merge data | 数据合并 |
| Send email | Email 发送 |
| Merge data+mail | 数据合并 |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据（Powered)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

，通过 邮箱 + HTTP API 实现自动化。

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
- 触发方式：表单提交触发

## 触发方式
- Form 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：15
- 输出节点：5
- 分类：workflow-automation
