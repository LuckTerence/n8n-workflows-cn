## 简介
**Find high-mismatch local business leads with Firecrawl and Groq**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15363

---

# Find high-mismatch local business leads with Firecrawl and Groq


## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Monday 9AM | 定时触发器 |
| Configuration | 数据设置 |
| Generate Category Signals | Code |
| Basic LLM Chain2 | LLM Chain |
| Groq Chat Model2 | Groq Chat Model |
| Parse Category Signals | Code |
| Discovery Search | Firecrawl |
| Format Search Context | Code |
| Basic LLM Chain | LLM Chain |
| Groq Chat Model | Groq Chat Model |
| Parse Business List | Code |
| Fetch Existing Leads | 数据表 |
| Filter New Leads | Code |
| Process Each Lead | 分批处理 |
| Rate Limit Delay | 等待 |
| Scrape Business Profile | Firecrawl |
| Has Website? | IF 判断 |
| Scrape Website | Firecrawl |
| Merge Website | Code |
| No Website Path | Code |
| Find Competitors | Firecrawl |
| Filter Competitors | Code |
| Split Competitors | Code |
| Scrape Competitor | Firecrawl |
| Merge Competitors | Code |
| Search Reviews | Firecrawl |
| Extract Review Snippets | Code |
| Basic LLM Chain1 | LLM Chain |
| Groq Chat Model1 | Groq Chat Model |
| The Mismatch Engine | Code |
| Aggregate All Leads | 数据聚合 |
| Rank and Deduplicate | Code |
| Filter Valid Leads | Code |
| Save to n8n Table | 数据表 |
| Aggregate for Report | 数据聚合 |
| Build HTML Report | Code |
| Build Slack Report | Code |
| Send Slack | Slack |



## 功能说明

数据采集工具，自动抓取网页或 API 数据，定时执行。

定时触发，通过 Slack + HTTP API 实现自动化。

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

- 节点总数：38
- 触发方式：定时触发

## 触发方式
- Weekly Monday 9AM 触发

## 统计
- 节点总数：38
- 触发节点：1
- 处理节点：36
- 输出节点：1
- 分类：workflow-automation
