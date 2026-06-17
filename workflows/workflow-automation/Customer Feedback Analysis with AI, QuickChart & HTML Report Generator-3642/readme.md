## 简介
**Customer Feedback Analysis with AI, QuickChart & HTML Report Generator**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3642

---

# Customer Feedback Analysis with AI, QuickChart & HTML Report Generator


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Google Sheets | Google Sheets |
| OpenAI Chat Model | OpenAI Chat Model |
| Prepare Prompts1 | Function |
| Structured Output Parser | 结构化输出解析器 |
| analysis topics proposal | AI Agent |
| OpenAI Chat Model1 | OpenAI Chat Model |
| Structured Output Parser1 | 结构化输出解析器 |
| Merge original table and the prompts | 数据合并 |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Unified AI Agent for analysis | AI Agent |
| Transform results into columns | Code |
| All unique elements merge | Code |
| Structured Output Parser2 | 结构化输出解析器 |
| proposal refinement agent | AI Agent |
| OpenAI Chat Model3 | OpenAI Chat Model |
| Second iteration of analysis | AI Agent |
| Structured Output Parser3 | 结构化输出解析器 |
| Merge | 数据合并 |
| Summarization of the unalysed results | AI Agent |
| OpenAI Chat Model4 | OpenAI Chat Model |
| Structured Output Parser4 | 结构化输出解析器 |
| OpenAI Chat Model5 | OpenAI Chat Model |
| Final report editor | AI Agent |
| Structured Output Parser5 | 结构化输出解析器 |
| Revisor and HTML formating agent | AI Agent |
| OpenAI Chat Model6 | OpenAI Chat Model |
| Get the first n rows | 过滤器 |
| wrap up the whole results into one Json file | Code |
| Merging first sample rows | Code |
| Completion agents (optional) | AI Agent |
| OpenAI Chat Model7 | OpenAI Chat Model |
| Edit Fields | 数据设置 |
| Gmail | Email 发送 |



## 功能说明

表单问卷工具，自动收集和处理用户反馈。

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

- 节点总数：34
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：34
- 触发节点：1
- 处理节点：32
- 输出节点：1
- 分类：workflow-automation
