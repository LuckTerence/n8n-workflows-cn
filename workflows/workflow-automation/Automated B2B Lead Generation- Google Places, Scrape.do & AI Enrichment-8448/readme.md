## 简介
**Automated B2B Lead Generation: Google Places, Scrape.do & AI Enrichment**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8448

---

# Automated B2B Lead Generation: Google Places, Scrape.do & AI Enrichment


## 节点清单

| 节点 | 类型 |
|------|------|
| Generate Report | Function |
| Error Logging | Function |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| When clicking ‘Execute workflow’ | 手动触发 |
| 1. Set Search Parameters | 数据设置 |
| 2. Find Businesses (Google Places) | HTTP Request |
| 3. Parse & Score Leads | Function |
| 4. Filter High-Quality Leads | IF 判断 |
| 5. Loop Through Each Lead | 分批处理 |
| 6a. Scrape Website with Scrape.do | HTTP Request |
| 6b. Check if Scrape Was Successful | IF 判断 |
| 6c. Extract Footer from HTML | HTML |
| 6d. Extract Contact Info with AI | AI Agent |
| 7. Save Enriched Lead to Google Sheets | Google Sheets |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：12
- 输出节点：2
- 分类：workflow-automation
