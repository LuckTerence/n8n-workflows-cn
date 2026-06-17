## 简介
**Complete Lesson Automation for Modern UK Teachers**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Zoom/Google Docs/Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4927

---

# Complete Lesson Automation for Modern UK Teachers


## 节点清单

| 节点 | 类型 |
|------|------|
| Teacher Input Form | 表单触发器 |
| Content Creation Agent | AI Agent |
| Assessment & Marking Agent | AI Agent |
| AI Integration Agent | AI Agent |
| Package Compiler | Code |
| Format Document | Code |
| Create Google Doc | Google Docs |
| Add Content to Doc | Google Docs |
| Schedule Prep Reminder | Google Calendar |
| Send Confirmation Email | Email 发送 |
| OpenAI Chat Model | OpenAI Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Fetch File From Drive | Google Drive |



## 功能说明

Complete Lesson Automation for Modern UK Teachers（AI 增强)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：14
- 触发方式：表单提交触发

## 触发方式
- Teacher Input Form 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：12
- 输出节点：1
- 分类：workflow-automation
