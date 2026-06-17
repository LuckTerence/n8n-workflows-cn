## 简介
**Local Business Lead Discovery and Enrichment Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Supabase/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15411

---

# Local Business Lead Discovery and Enrichment Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| AI Agent — enrichment | AI Agent |
| GPT-5. | OpenAI Chat Model |
| Enrich Selected 10 — Parse | Code |
| Enrich Selected 10 — Scrape Website | Firecrawl 工具 |
| Enrich Selected 10 — Scrape Listing | Firecrawl 工具 |
| Enrich Selected 10 — Prep | Code |
| Compute Fingerprint | Code |
| Parse Refill Output | Code |
| AI Agent — Discover Fresh | AI Agent |
| /search in Firecrawl | Firecrawl 工具 |
| GPT-5.1 | OpenAI Chat Model |
| /scrape in Firecrawl | Firecrawl 工具 |
| Gmail — Send Weekly Summary | Email 发送 |
| Build Email HTML | Code |
| Aggregate New Leads | 数据聚合 |
| Postgres — Insert Lead | PostgreSQL |
| Schedule Trigger | 定时触发器 |
| Rotation Seed | Code |
| Fetch Seen Fingerprints | PostgreSQL |
| Filter Unseen (Top 10) | Code |



## 功能说明

客户关系管理工具，自动管理销售线索和客户数据，定时执行。

定时触发，通过 邮箱 + 数据库 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- DeepSeek API Key → https://platform.deepseek.com
- 邮箱 SMTP/IMAP 账号密码
- 数据库连接信息

> AI 模型已替换为 DeepSeek（已替换 OpenAI/Claude/Gemini)请确保已注册并获取 API Key。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：20
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：18
- 输出节点：1
- 分类：workflow-automation
