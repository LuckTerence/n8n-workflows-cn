# Send Indian tender email reports from TendersInfo.net results

https://n8nworkflows.xyz/workflows/15886

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger1 | Webhook |
| Parse Tender Response1 | Code |
| Select Email Fields1 | 数据设置 |
| Fetch Tender Data from API1 | HTTP Request |
| Filter GEM Tenders Only1 | 过滤器 |
| Respond to Webhook1 | 响应 Webhook |
| Build HTML Table | Code |

## 触发方式
- Webhook Trigger1 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
