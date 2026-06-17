## 简介
**Create Structured Company Profiles with Mistral AI, Firecrawl & Competitor Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Drive/Supabase)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/10097

---

# Create Structured Company Profiles with Mistral AI, Firecrawl & Competitor Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Supabase | Supabase |
| Mistral Cloud Chat Model3 | Mistral Chat Model |
| list tools | MCP 客户端 |
| execute tools | MCP 客户端 |
| find competitor | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Supabase4 | Supabase |
| Crawl and Scrape | crawleeNode |
| On form submission | 表单触发器 |
| Switch | Switch 路由 |
| basic web scraper | AI Agent |
| social media db | Supabase |
| keywords | Supabase |
| Mistral Cloud Chat Model5 | Mistral Chat Model |
| Information Extractor1 | 信息提取器 |
| Mistral Cloud Chat Model6 | Mistral Chat Model |
| Google Drive2 | Google Drive |
| Firecrawl tools1 | MCP 客户端 |
| Mistral Cloud Chat Model2 | Mistral Chat Model |
| Firecrawl list1 | MCP 客户端 |
| Structured Output Parser1 | 结构化输出解析器 |
| Web Search tool | HTTP 工具 |
| No Operation, do nothing | 空操作 |
| MCP based scraper FIRECRAWLER | AI Agent |
| Convert to File for storage | 转换为文件 |
| Convert to File for storage1 | 转换为文件 |
| save to Google Drive1 | Google Drive |
| save to Supabase | Supabase |



## 功能说明

数据采集工具，自动抓取网页或 API 数据（Structured)表单提交触发，通过 HTTP API 实现自动化。

，通过 HTTP API 实现自动化。

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

- 节点总数：28
- 触发方式：表单提交触发

## 触发方式
- On form submission 触发

## 统计
- 节点总数：28
- 触发节点：1
- 处理节点：26
- 输出节点：1
- 分类：workflow-automation
