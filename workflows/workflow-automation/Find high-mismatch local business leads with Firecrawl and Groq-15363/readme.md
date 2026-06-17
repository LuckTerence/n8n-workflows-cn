## 简介
**Find high-mismatch local business leads with Firecrawl and Groq**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
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
| Parse Category Signals  | Code |
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

## 触发方式
- Weekly Monday 9AM 触发

## 统计
- 节点总数：38
- 触发节点：1
- 处理节点：36
- 输出节点：1
- 分类：workflow-automation
