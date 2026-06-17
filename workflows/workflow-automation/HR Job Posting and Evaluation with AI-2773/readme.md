## 简介
**HR Job Posting and Evaluation with AI**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2773

---

# HR Job Posting and Evaluation with AI


## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Airtable | Airtable |
| Upload CV to google drive | Google Drive |
| applicant details | 数据设置 |
| download CV | Google Drive |
| Extract from File | 从文件提取 |
| AI Agent | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Airtable1 | Airtable 工具 |
| Structured Output Parser | 结构化输出解析器 |
| shortlisted? | IF 判断 |
| Rejected | Airtable |
| Potential Hire | Airtable |
| Airtable2 | Airtable 工具 |
| generate questionnaires | OpenAI |
| questionnaires | 表单 |
| update questionnaires | Airtable |
| job_posting | Airtable 工具 |
| candidate_insights | Airtable 工具 |
| Personalize email | OpenAI |
| Edit Fields | 数据设置 |
| Send Email | Email 发送 |
| Book Meeting | OpenAI |
| Google Calendar | Google Calendar 工具 |
| update phone meeting time | Airtable |
| Screening Questions | OpenAI |
| job_posting1 | Airtable 工具 |
| candidate_insights1 | Airtable 工具 |
| screening questions | Airtable |
| Edit Fields1 | 数据设置 |



## 功能说明

AI 招聘助手，简历筛选或面试流程自动化（Job)表单提交触发，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

，通过 邮箱 + 在线表格 + HTTP API 实现自动化。

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
- On form submission 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：28
- 输出节点：1
- 分类：workflow-automation
