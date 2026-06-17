## 简介
**Find Content Gaps in Competitors' Websites with InfraNodus GraphRAG for SEO**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（需替换Google Sheets/Google Docs)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4403

---

# Find Content Gaps in Competitors' Websites with InfraNodus GraphRAG for SEO


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking "Execute Workflow" | 手动触发 |
| HTTP Request | HTTP Request |
| HTML Extract | htmlExtract |
| Merge | 数据合并 |
| Clean Content | Code |
| Split In Batches | 分批处理 |
| InfraNodus GraphRAG Content Enhancer | HTTP Request |
| Google Docs | Google Docs |
| Aggregate | 数据聚合 |
| Read a Google Sheets File | Google Sheets |
| Update Google Sheets with Content Insights | Google Sheets |
| Wait to avoid API overload | 等待 |
| If Node: did we process all the data? | IF 判断 |
| Get the content from Google Sheets | Google Sheets |
| InfraNodus AI Advice | HTTP Request |
| Merge1 | 数据合并 |
| InfraNodus Question Generator | HTTP Request |
| Perplexity Research | HTTP Request |
| On form submission | 表单触发器 |
| OpenAI | OpenAI |
| Google Sheets | Google Sheets |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |

## 触发方式
- When clicking "Execute Workflow" 触发
- On form submission 触发

## 统计
- 节点总数：23
- 触发节点：2
- 处理节点：16
- 输出节点：5
- 分类：knowledge-rag
