# Intelligent Purchase Order Generator with AI Supplier Selection

https://n8nworkflows.xyz/workflows/10680

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Trigger | Webhook |
| Validate Request | Code |
| Prepare AI Context | 数据设置 |
| AI Supplier Selector | AI Agent |
| Enrich with Supplier Data | Code |
| Needs Approval? | IF 判断 |
| Request Approval | Email 发送 |
| Generate PO Document | Code |
| HTML to PDF | htmlcsstopdf |
| Archive in Drive | Google Drive |
| Email to Supplier | Email 发送 |
| Log in Procurement System | Code |
| Notify Procurement Team | HTTP Request |
| OpenAI Chat Model | OpenAI Chat Model |

## 触发方式
- Webhook Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：workflow-automation
