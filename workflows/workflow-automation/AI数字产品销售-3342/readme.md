## 简介
**AI数字产品销售**

GPT-4o驱动的SaaS产品销售自动化

> 分类：工作流自动化 | 适配等级：B（需替换Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
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

## 触发方式
- MANUAL TRIGGER: Start Workflow 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：25
- 输出节点：3
- 分类：workflow-automation
