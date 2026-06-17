## 简介
**Hacker News Job Listing Scraper and Parser**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2924

---

# Hacker News Job Listing Scraper and Parser


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Test workflow’ | 手动触发 |
| Split Out | 数据拆分 |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| Search for Who is hiring posts | HTTP Request |
| Get relevant data | 数据设置 |
| Get latest post | 过滤器 |
| Split out children (jobs) | 数据拆分 |
| Trun into structured data | LLM Chain |
| Extract text | 数据设置 |
| Clean text | Code |
| Limit for testing (optional) | 数据限制 |
| Write results to airtable | Airtable |
| HI API: Get the individual job post | HTTP Request |
| HN API: Get Main Post | HTTP Request |



## 功能说明

数据采集工具，自动抓取网页或 API 数据。

手动触发，通过 在线表格 + HTTP API 实现自动化。

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

- 节点总数：15
- 触发方式：手动触发

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
