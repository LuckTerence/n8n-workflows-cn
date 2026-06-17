# B2B lead qualification

https://n8nworkflows.xyz/workflows/5404

## 节点清单

| 节点 | 类型 |
|------|------|
| New Lead Captured | Google Sheets 触发器 |
| Initiate Voice Call (VAPI) | HTTP Request |
| Save Qualified Lead to CRM Sheet | Google Sheets |
| Send Call Data Acknowledgement | 响应 Webhook |
| Receive Lead Details from VAPI | Webhook |

## 触发方式
- New Lead Captured 触发
- Receive Lead Details from VAPI 触发

## 统计
- 节点总数：5
- 触发节点：2
- 处理节点：1
- 输出节点：2
- 分类：workflow-automation
