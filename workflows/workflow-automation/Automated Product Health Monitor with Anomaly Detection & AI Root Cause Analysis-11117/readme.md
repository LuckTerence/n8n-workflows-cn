# Automated Product Health Monitor with Anomaly Detection & AI Root Cause Analysis

https://n8nworkflows.xyz/workflows/11117

## 节点清单

| 节点 | 类型 |
|------|------|
| log incident | PostgreSQL |
| daily usage metrics | PostgreSQL |
| anomalies | Code |
| insert incidents | PostgreSQL |
| select open incident | PostgreSQL |
| revenue by country | PostgreSQL |
| revenue by plan | PostgreSQL |
| sum up/ hypothesis | OpenAI |
| root cause summary | Slack |
| update incident status | PostgreSQL |
| daily report trigger | 定时触发器 |
| sum up | Code |
| email alert | Email 发送 |
| daily report email | Email 发送 |
| root cause summary email | Email 发送 |
| log system | PostgreSQL |
| Execute the SQL query | PostgreSQL |
| Trigger RH | 定时触发器 |
| Update notions | Notion |
| slack notification | Slack |
| Condition incident | IF 判断 |
| Merge data | 数据合并 |
| log system final | PostgreSQL |
| anomalies check | Code |
| Slack notification | Slack |
| usage health email | Email 发送 |
| Trigger CS | 定时触发器 |
| Trigger UH | 定时触发器 |
| log system UH | PostgreSQL |
| Execute SQL query incident check | PostgreSQL |
| Notions database creation | Notion |
| log system final1 | PostgreSQL |

## 触发方式
- daily report trigger 触发
- Trigger RH 触发
- Trigger CS 触发
- Trigger UH 触发

## 统计
- 节点总数：32
- 触发节点：4
- 处理节点：21
- 输出节点：7
- 分类：workflow-automation
