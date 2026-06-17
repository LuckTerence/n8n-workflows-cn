# Automated 4-Stage Email Follow-Up System with AI Personalization and Database Tracking

https://n8nworkflows.xyz/workflows/9108

## 节点清单

| 节点 | 类型 |
|------|------|
| Get many rows | NocoDB |
| Filter | 过滤器 |
| Switch | Switch 路由 |
| Groq Chat Model | Groq Chat Model |
| Groq Chat Model1 | Groq Chat Model |
| Groq Chat Model2 | Groq Chat Model |
| Groq Chat Model3 | Groq Chat Model |
| Send email | Email 发送 |
| Send email1 | Email 发送 |
| Send email2 | Email 发送 |
| Send email3 | Email 发送 |
| Update a row | NocoDB |
| Update a row1 | NocoDB |
| Update a row2 | NocoDB |
| Update a row3 | NocoDB |
| Schedule Trigger | 定时触发器 |
| Filter1 | 过滤器 |
| Follow Up Message 1 | LLM Chain |
| Follow Up Message 2 | LLM Chain |
| Follow Up Message 3 | LLM Chain |
| Follow Up Message 4 | LLM Chain |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：16
- 输出节点：4
- 分类：workflow-automation
