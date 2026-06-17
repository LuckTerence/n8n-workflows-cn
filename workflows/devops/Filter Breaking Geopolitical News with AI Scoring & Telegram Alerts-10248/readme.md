# Filter Breaking Geopolitical News with AI Scoring & Telegram Alerts

https://n8nworkflows.xyz/workflows/10248

## 节点清单

| 节点 | 类型 |
|------|------|
| Every 30 Minutes | 定时触发器 |
| NYT RSS Feed | RSS Feed |
| TOI RSS Feed | RSS Feed |
| Al Jazeera RSS Feed | RSS Feed |
| BBC RSS Feed | RSS Feed |
| Dynamic Filter | Code |
| Send Breaking News Alert | Telegram |
| Breaking News Analyzer | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Structured Output Parser | 结构化输出解析器 |
| If | IF 判断 |
| SCMP RSS Feed | RSS Feed |
| NDTV RSS Feed | RSS Feed |
| Check for Duplicates | 数据表 |
| Record Analyzed Article | 数据表 |
| Cleanup Old Records | 数据表 |
| Merge | 数据合并 |
| Aggregate Alerts | Code |
| Dynamic AI Prompt Generator | Code |
| RSS_Cleanup_Node | Code |
| Load Config from Google Drive | HTTP Request |
| Re-attach Config | Code |

## 触发方式
- Every 30 Minutes 触发
- NYT RSS Feed 触发
- TOI RSS Feed 触发
- Al Jazeera RSS Feed 触发
- BBC RSS Feed 触发
- SCMP RSS Feed 触发
- NDTV RSS Feed 触发

## 统计
- 节点总数：22
- 触发节点：7
- 处理节点：13
- 输出节点：2
- 分类：devops
