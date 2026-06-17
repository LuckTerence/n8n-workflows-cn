# Create Detailed Security Tickets from SentinelOne Threats with MITRE Analysis

https://n8nworkflows.xyz/workflows/7312

## 节点清单

| 节点 | 类型 |
|------|------|
| New SentinelOne Threat | Webhook |
| Extract Threat Intelligence | Code |
| Fetch Autotask Users | HTTP Request |
| Load Client Companies | HTTP Request |
| Process Company Data | 数据拆分 |
| Retrieve Ticket Fields | HTTP Request |
| Parse Field Options | Code |
| Map Client Company | Code |
| Create Security Ticket | HTTP Request |
| Rate Limit Delay 1 | 等待 |
| Rate Limit Delay 2 | 等待 |
| Wait | 等待 |

## 触发方式
- New SentinelOne Threat 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
