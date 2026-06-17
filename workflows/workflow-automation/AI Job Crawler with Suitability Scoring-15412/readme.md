## 简介
**AI Job Crawler with Suitability Scoring**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15412

---

# AI Job Crawler with Suitability Scoring


## 节点清单

| 节点 | 类型 |
|------|------|
| Score Filter1 | IF 判断 |
| OpenAI Chat Model5 | OpenAI Chat Model |
| HTML1 | HTML |
| Code in JavaScript1 | Code |
| Rate suitablility | AI Agent |
| Firecrawl Execute | 手动触发 |
| WeAreDevelopers Query | Code |
| Indeed Query | Code |
| Edit Fields | 数据设置 |
| Code in JavaScript2 | Code |
| Edit Fields1 | 数据设置 |
| Code in JavaScript3 | Code |
| Merge | 数据合并 |
| OpenAI Chat Model6 | OpenAI Chat Model |
| /scrape in Firecrawl1 | Firecrawl 工具 |
| /search in Firecrawl1 | Firecrawl 工具 |
| Crawl a website and scrape all pages in Firecrawl1 | Firecrawl 工具 |
| LinkedIn Query | Code |
| Detailled Research | AI Agent |
| JSON Suitability Format | 结构化输出解析器 |
| HTML Success Research | HTML |
| JSON Job Format1 | 结构化输出解析器 |
| scrape URL Dev | Firecrawl |
| OpenAI Chat Model7 | OpenAI Chat Model |
| JSON Job Format2 | 结构化输出解析器 |
| Process Date AI | AI Agent |
| Code with Posted Date | Code |
| Fetch Jobs from Linkedin1 | HTTP Request |
| Extract Job Links1 | HTML |
| scrape URL indeed | Firecrawl |
| If | IF 判断 |
| /scrape exchange rates | Firecrawl 工具 |
| /search in Firecrawl | Firecrawl 工具 |
| Reduce to job data | 数据设置 |
| Stepstone Query | Code |
| scrape URL stepstone | Firecrawl |
| Edit Fields3 | 数据设置 |
| Edit Fields4 | 数据设置 |
| Xing Query | Code |
| scrape URL Xing | Firecrawl |
| Code in JavaScript4 | Code |
| HTML | HTML |
| No Jobs Mail | Email 发送 |
| Job Mail | Email 发送 |
| Add Link | Code |
| Loop over all jobs | 分批处理 |
| Raw Values | 数据设置 |
| Schedule Trigger | 定时触发器 |
| Valid only | 过滤器 |
| /scrape1 | Firecrawl |
| Loop Over Items | 分批处理 |
| OpenAI Chat Model | OpenAI Chat Model |
| JSON Job Format | 结构化输出解析器 |
| Process Scraped Data | AI Agent |
| HTML Failed Research | HTML |

## 触发方式
- Firecrawl Execute 触发
- Schedule Trigger 触发

## 统计
- 节点总数：55
- 触发节点：2
- 处理节点：50
- 输出节点：3
- 分类：workflow-automation
