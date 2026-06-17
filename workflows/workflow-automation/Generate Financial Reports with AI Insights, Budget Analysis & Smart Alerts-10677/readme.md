# Generate Financial Reports with AI Insights, Budget Analysis & Smart Alerts

https://n8nworkflows.xyz/workflows/10677

## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Monthly | 定时触发器 |
| Calculate Period | Code |
| Fetch Current P&L | HTTP Request |
| Fetch Previous P&L | HTTP Request |
| Merge Data | 数据合并 |
| Analyze Financial Data | Code |
| Prepare AI Context | 数据设置 |
| AI Financial Insights | AI Agent |
| OpenAI Chat Model | OpenAI Chat Model |
| Prepare Report Data | Code |
| Requires CFO Review? | IF 判断 |
| Request CFO Review | Email 发送 |
| Generate Report HTML | Code |
| HTML to PDF | htmlcsstopdf |
| Save to Google Drive | Google Drive |
| Send to Stakeholders | Email 发送 |
| Health Critical? | IF 判断 |
| Alert - Critical | HTTP Request |
| Notify - Standard | HTTP Request |

## 触发方式
- Schedule Monthly 触发

## 统计
- 节点总数：19
- 触发节点：1
- 处理节点：12
- 输出节点：6
- 分类：workflow-automation
