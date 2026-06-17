## 简介
**AI-Powered NPM Package Intelligence Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15410

---

# AI-Powered NPM Package Intelligence Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Commit deatils | 数据设置 |
| Github details | 数据设置 |
| /search in Firecrawl | Firecrawl 工具 |
| /scrape in Firecrawl | Firecrawl 工具 |
| OpenAI Chat Model | OpenAI Chat Model |
| Enter Package Name | 表单触发器 |
| Normalize Input | 数据设置 |
| Search NPM URL | Firecrawl |
| Search GitHub Repo | Firecrawl |
| Merge Search Results | 数据合并 |
| Extract Clean URLs | Code |
| Fetch GitHub Stats | github |
| Fetch Last Commit | HTTP Request |
| Fetch NPM Downloads | HTTP Request |
| Merge All Metrics | 数据合并 |
| Compute Health Metrics | 数据设置 |
| Check Package Valid | IF 判断 |
| Package Not Found Handler | 数据设置 |
| AI Analysis Engine | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Send Slack Report | Slack |
| Send Slack Report_01 | Slack |
| OpenRouter Chat Model | OpenRouter Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |



## 功能说明

AI-Powered NPM Package Intelligence Agent（AI 增强)表单提交触发，通过 Slack + Git + HTTP API 实现自动化。

，通过 Slack + Git + HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：24
- 触发方式：表单提交触发

## 触发方式
- Enter Package Name 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：19
- 输出节点：4
- 分类：workflow-automation
