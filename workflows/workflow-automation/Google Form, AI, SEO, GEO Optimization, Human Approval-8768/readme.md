## 简介
**Google Form, AI, SEO, GEO Optimization, Human Approval**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8768

---

# Google Form, AI, SEO, GEO Optimization, Human Approval


## 节点清单

| 节点 | 类型 |
|------|------|
| Blog Generator | AI Agent |
| Groq Chat Model | Groq Chat Model |
| Google Sheets Trigger | Google Sheets 触发器 |
| Mistral Cloud Chat Model | Mistral Chat Model |
| fitting into template | AI Agent |
| optimzing for SEO,GEO | AI Agent |
| Mistral Cloud Chat Model1 | Mistral Chat Model |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Send Content for Approval1 | Email 发送 |
| Add Generated Content to Google Sheets1 | Google Sheets |
| Update Topic Status on Google Sheets1 | Google Sheets |
| Approval Result1 | Switch 路由 |
| convert to html for email | AI Agent |
| Revision based on feedback | AI Agent |
| date tool | dateTimeTool |



## 功能说明

SEO 优化工具，关键词分析和内容优化。

手动触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：手动或子流程调用

## 触发方式
- Google Sheets Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：13
- 输出节点：1
- 分类：workflow-automation
