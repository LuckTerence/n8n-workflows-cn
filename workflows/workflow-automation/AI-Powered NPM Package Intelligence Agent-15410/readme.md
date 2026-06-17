## 简介
**AI-Powered NPM Package Intelligence Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：B（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/15410

---

# AI-Powered NPM Package Intelligence Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Commit deatils | 数据设置 |
| Github details | 数据设置 |
| /search in Firecrawl | Firecrawl 工具 |
| /scrape in Firecrawl | Firecrawl 工具 |
| OpenAI Chat Model | OpenAI Chat Model |
| Enter Package Name | 表单触发器 |
| Normalize Input | 数据设置 |
| Search NPM URL | Firecrawl |
| Search GitHub Repo | Firecrawl |
| Merge Search Results | 数据合并 |
| Extract Clean URLs | Code |
| Fetch GitHub Stats | github |
| Fetch Last Commit | HTTP Request |
| Fetch NPM Downloads | HTTP Request |
| Merge All Metrics | 数据合并 |
| Compute Health Metrics | 数据设置 |
| Check Package Valid | IF 判断 |
| Package Not Found Handler | 数据设置 |
| AI Analysis Engine | AI Agent |
| Structured Output Parser | 结构化输出解析器 |
| Send Slack Report | Slack |
| Send Slack Report_01 | Slack |
| OpenRouter Chat Model | OpenRouter Chat Model |
| OpenAI Chat Model1 | OpenAI Chat Model |

## 触发方式
- Enter Package Name 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：19
- 输出节点：4
- 分类：workflow-automation
