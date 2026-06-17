# Automated Email Blast with Follow-Ups & Response Tracking

https://n8nworkflows.xyz/workflows/7175

## 节点清单

| 节点 | 类型 |
|------|------|
| Daily Trigger | 定时触发器 |
| Fetch Contact Data  | Google Sheets |
| Iterate Contacts | 分批处理 |
| Determine Follow-Up Stage | IF 判断 |
| Route by Follow-Up Stage | Switch 路由 |
| Send Follow-Up Email 1  | Email 发送 |
| Send Follow-Up Email 2 | Email 发送 |
| Update Sheet with Follow-Up Status | Google Sheets |
| Check Email Responses | Email 读取 |
| Update Sheet with Response  | Google Sheets |

## 触发方式
- Daily Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：6
- 输出节点：3
- 分类：workflow-automation
