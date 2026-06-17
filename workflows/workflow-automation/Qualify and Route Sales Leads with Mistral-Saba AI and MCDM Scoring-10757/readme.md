# Qualify and Route Sales Leads with Mistral-Saba AI and MCDM Scoring

https://n8nworkflows.xyz/workflows/10757

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Workflow Configuration | 数据设置 |
| Fetch Demographic Data | HTTP Request |
| Fetch Behavioral Data | HTTP Request |
| Fetch Transactional Data | HTTP Request |
| Merge Lead Data Sources | 数据聚合 |
| MCDM Scoring Engine (AHP-TOPSIS) | Code |
| AI Lead Qualification Agent | AI Agent |
| Lead Enrichment Tool | 代码工具 |
| Prepare Lead Scores | 数据设置 |
| Route by Lead Quality | Switch 路由 |
| Assign to Enterprise Sales Team | HTTP Request |
| Assign to Mid-Market Team | HTTP Request |
| Assign to SMB Team | HTTP Request |
| Send to Nurture Campaign | HTTP Request |
| Collect Routing Results | 数据聚合 |
| Update CRM with Lead Scores | HTTP Request |
| Calculate Performance KPIs | Code |
| Log KPIs to Analytics Dashboard | HTTP Request |
| OpenRouter Chat Model | OpenRouter Chat Model |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：20
- 触发节点：1
- 处理节点：10
- 输出节点：9
- 分类：workflow-automation
