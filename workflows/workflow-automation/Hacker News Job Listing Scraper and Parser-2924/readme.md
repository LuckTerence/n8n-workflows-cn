## 简介
**Hacker News Job Listing Scraper and Parser**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
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

## 触发方式
- When clicking ‘Test workflow’ 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：11
- 输出节点：3
- 分类：workflow-automation
