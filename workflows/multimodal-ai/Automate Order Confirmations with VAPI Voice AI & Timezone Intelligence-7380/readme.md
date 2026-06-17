# Automate Order Confirmations with VAPI Voice AI & Timezone Intelligence

https://n8nworkflows.xyz/workflows/7380

## 节点清单

| 节点 | 类型 |
|------|------|
| Order Webhook | Webhook |
| Validate Order Data | IF 判断 |
| Check Timezone & Calling Hours | Code |
| Can Call Now? | IF 判断 |
| Format Order Data | Code |
| Initiate VAPI Call | HTTP Request |
| Check Call Status | IF 判断 |
| Update Order Status | Airtable |
| Schedule Call for Later | Airtable |
| Scheduled Call Checker | schedule |
| Get Scheduled Calls | Airtable |
| VAPI Webhook Handler | Webhook |
| Check Webhook Type | IF 判断 |
| Process Call Results | Code |
| Update Final Status | Airtable |
| Check if Followup Needed | IF 判断 |
| Send Follow-up Alert | Email 发送 |
| Send Confirmation Email | Email 发送 |
| Validation Error Response | 响应 Webhook |
| Call Error Response | 响应 Webhook |
| Success Response | 响应 Webhook |
| Scheduled Response | 响应 Webhook |
| Webhook Response | 响应 Webhook |
| Increment Call Attempts | Airtable |

## 触发方式
- Order Webhook 触发
- VAPI Webhook Handler 触发

## 统计
- 节点总数：24
- 触发节点：2
- 处理节点：14
- 输出节点：8
- 分类：multimodal-ai
