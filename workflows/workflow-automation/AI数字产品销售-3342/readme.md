## 简介
**AI数字产品销售**

GPT-4o驱动的SaaS产品销售自动化

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/3342

---

# AI数字产品销售


## 节点清单

| 节点 | 类型 |
|------|------|
| Extract URLs from Google Search | Code |
| Remove Duplicate URLs | 去重 |
| Remove Duplicate Emails | 去重 |
| Split Emails into Items | 数据拆分 |
| Aggregate Email Lists | 数据聚合 |
| Search Google Maps | HTTP Request |
| Filter Out Google/Schema URLs | 过滤器 |
| Loop Through Unique URLs | 分批处理 |
| Fetch Website Content (via URL) | HTTP Request |
| Loop Through Website Content Batches | 分批处理 |
| Extract and Filter Emails | Code |
| Loop Through Search Queries | 分批处理 |
| Wait Before Google Search | 等待 |
| Process AI-Generated Queries | Code |
| Generate Google Maps Queries (OpenAI) | OpenAI |
| Extract Domain from Email | Code |
| Loop Through Unique Emails | 分批处理 |
| Scrape Website Content (Jina.ai) | HTTP Request |
| Check for Scraping Error | IF 判断 |
| Truncate Website Content | Code |
| Check if URL Exists | IF 判断 |
| Send Email via Gmail | Gmail |
| Wait Between Emails | 等待 |
| Generate Random Delay | Code |
| Generate Personalized Email (LLM Chain) | LLM Chain |
| Parse AI Email Output (JSON) | 结构化输出解析器 |
| NoOp (If URL Invalid) | 空操作 |
| MANUAL TRIGGER: Start Workflow | 手动触发 |
| Configure OpenAI Chat Model (GPT-4o-mini) | OpenAI Chat Model |



## 功能说明

AI数字产品销售。

手动触发，通过 邮箱 + HTTP API 实现自动化。

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

- 节点总数：29
- 触发方式：手动触发

## 触发方式
- MANUAL TRIGGER: Start Workflow 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：25
- 输出节点：3
- 分类：workflow-automation
