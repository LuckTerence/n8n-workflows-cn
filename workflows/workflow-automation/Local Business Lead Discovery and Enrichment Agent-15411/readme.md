# Local Business Lead Discovery and Enrichment Agent

https://n8nworkflows.xyz/workflows/15411

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

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：18
- 输出节点：1
- 分类：workflow-automation
