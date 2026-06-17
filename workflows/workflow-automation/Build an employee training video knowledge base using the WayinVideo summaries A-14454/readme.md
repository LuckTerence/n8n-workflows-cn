# Build an employee training video knowledge base using the WayinVideo summaries API

https://n8nworkflows.xyz/workflows/14454

## 节点清单

| 节点 | 类型 |
|------|------|
| 2. WayinVideo — Submit Summary Request | HTTP Request |
| 3. Wait — 30 Seconds | 等待 |
| 4. WayinVideo — Fetch Summary Result | HTTP Request |
| 5. Check — Highlights Ready? | IF 判断 |
| 6. Save — Append Row to Google Sheet | Google Sheets |
| 1. Form — Video URL + Topic1 | 表单触发器 |

## 触发方式
- 1. Form — Video URL + Topic1 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
