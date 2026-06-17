# Multi-Jurisdiction Smart Contract Compliance Monitor with Automated Alerts

https://n8nworkflows.xyz/workflows/6075

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Compliance Check | 定时触发器 |
| Compliance Settings | 数据设置 |
| Monitor EU Regulations | HTTP Request |
| Monitor US Federal Register | HTTP Request |
| Monitor UK Legislation | HTTP Request |
| Get Active Contracts | PostgreSQL |
| Analyze Compliance Impact | Code |
| Filter Critical Compliance Issues | IF 判断 |
| Send Critical Legal Alert | Email 发送 |
| Filter High Risk Issues | IF 判断 |
| Send High Risk Alert | Email 发送 |
| Filter Medium Risk Issues | IF 判断 |
| Send Medium Risk Alert | Email 发送 |
| Log Compliance Check | Google Sheets |

## 触发方式
- Daily Compliance Check 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：7
- 输出节点：6
- 分类：workflow-automation
