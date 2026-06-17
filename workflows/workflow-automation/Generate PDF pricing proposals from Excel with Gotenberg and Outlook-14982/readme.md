# Generate PDF pricing proposals from Excel with Gotenberg and Outlook

https://n8nworkflows.xyz/workflows/14982

## 节点清单

| 节点 | 类型 |
|------|------|
| Pricing Request Webhook | Webhook |
| Fetch Pricing Sheet | microsoftExcel |
| Process & Price | Code |
| Build HTML Proposal | Code |
| Gotenberg → PDF | HTTP Request |
| Send a message | Outlook |

## 触发方式
- Pricing Request Webhook 触发

## 统计
- 节点总数：6
- 触发节点：1
- 处理节点：3
- 输出节点：2
- 分类：workflow-automation
