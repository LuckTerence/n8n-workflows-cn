## 简介
**AI-Powered Interview Preparation System using Local LLM for Campus Placements**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4761

---

# AI-Powered Interview Preparation System using Local LLM for Campus Placements


## 节点清单

| 节点 | 类型 |
|------|------|
| Merge | 数据合并 |
| Ollama Chat Model | Ollama Chat Model |
| Merge1 | 数据合并 |
| Ollama Chat Model1 | Ollama Chat Model |
| Gemini Search Tool | geminiSearchToolTool |
| Merge2 | 数据合并 |
| Merge3 | 数据合并 |
| Parse Uploaded CSV of Candidates | 表单触发器 |
| create a sheet in google spreadsheet | Google Sheets |
| extract csv data | 从文件提取 |
| Add csv data to google spreadsheet | Google Sheets |
| Select first row based on selected column | Google Sheets |
| Job Interview Preparation Agent | AI Agent |
| change item name to markdown | Code |
| Create PDF files | apiTemplateIo |
| Email prompt Agent | AI Agent |
| Send Email with PDF | Email 发送 |
| Update the selected column to spreadsheet | Google Sheets |



## 功能说明

AI-Powered Interview Preparation System using Loca（AI 增强)表单提交触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：18
- 触发方式：表单提交触发

## 触发方式
- Parse Uploaded CSV of Candidates 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：16
- 输出节点：1
- 分类：workflow-automation
