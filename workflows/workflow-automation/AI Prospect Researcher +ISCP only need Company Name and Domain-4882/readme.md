## 简介
**AI Prospect Researcher +ISCP only need Company Name and Domain**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4882

---

# AI Prospect Researcher +ISCP only need Company Name and Domain


## 节点清单

| 节点 | 类型 |
|------|------|
| Hunter | hunter |
| Perplexity Search | HTTP Request |
| Wait1 | 等待 |
| Company LinkedIn Account POST | HTTP Request |
| Company LinkedIn Account GET | HTTP Request |
| Set Results Company | 数据设置 |
| Search profile | Airtop |
| Scrape webpage | Airtop |
| Analyze scraped Page | LLM Chain |
| OpenAI Chat Model | OpenAI Chat Model |
| Merge | 数据合并 |
| Add report to doc | Google Docs |
| Create doc | Google Docs |
| OpenAI Chat Model2 | OpenAI Chat Model |
| Aggregate | 数据聚合 |
| Hunter Results | 数据设置 |
| Perplexity Results | 数据设置 |
| Generate report | LLM Chain |
| Get Offer | Google Docs |
| OpenAI Chat Model3 | OpenAI Chat Model |
| ISCP score | LLM Chain |
| Structured Output Parser | 结构化输出解析器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| On form submission | 表单触发器 |
| Google Sheets | Google Sheets |
| Loop Over Items | 分批处理 |
| Set company name and domain | 数据设置 |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- On form submission 触发

## 统计
- 节点总数：27
- 触发节点：2
- 处理节点：22
- 输出节点：3
- 分类：workflow-automation
