# Enrich up to 1500 emails per hour with Dropcontact batch requests

https://n8nworkflows.xyz/workflows/2272

## 节点清单

| 节点 | 类型 |
|------|------|
| Aggregate | 数据聚合 |
| PROFILES QUERY | PostgreSQL |
| BULK DROPCONTACT REQUESTS | HTTP Request |
| Loop Over Items2 | 分批处理 |
| Split Out | 数据拆分 |
| Postgres | PostgreSQL |
| BULK DROPCONTACT DOWNLOAD | HTTP Request |
| Wait2 | 等待 |
| DATA TRANSFORMATION | Code |
| Slack | Slack |
| Schedule Trigger | 定时触发器 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
