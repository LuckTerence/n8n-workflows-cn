# Postgres Data Freshness Monitoring with Email Alerts

https://n8nworkflows.xyz/workflows/6190

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| Loop Over Items | 分批处理 |
| Aggregate Stale Tables | 数据聚合 |
| Get most recent row from table | PostgreSQL |
| Calculate lag | 日期时间 |
| Add back table name | 数据设置 |
| Remove fresh tables | 过滤器 |
| Produce tables + date columns | Code |
| Send alerts | 执行工作流 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：8
- 输出节点：0
- 分类：devops
