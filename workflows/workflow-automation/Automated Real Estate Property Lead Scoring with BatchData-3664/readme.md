# Automated Real Estate Property Lead Scoring with BatchData

https://n8nworkflows.xyz/workflows/3664

## 节点清单

| 节点 | 类型 |
|------|------|
| CRM New Lead Webhook | Webhook |
| Fetch Lead Data | HTTP Request |
| BatchData Property Lookup | HTTP Request |
| Score And Qualify Lead | Code |
| Update CRM Lead | HTTP Request |
| Is High-Value Lead? | IF 判断 |
| Create Immediate Follow-up Task | HTTP Request |
| Send Slack Notification | Slack |

## 触发方式
- CRM New Lead Webhook 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：2
- 输出节点：5
- 分类：workflow-automation
