# Custom Branded QuickBooks Invoices to PDF with Gotenberg & Email

https://n8nworkflows.xyz/workflows/7051

## 节点清单

| 节点 | 类型 |
|------|------|
| Listen for New QuickBooks Invoice | Webhook |
| Get Invoice Data from QuickBooks | QuickBooks |
| Fetch Company Logo Image | HTTP Request |
| Fetch Company Signature Image | HTTP Request |
| Convert Logo to Base64 | 从文件提取 |
| Convert Signature to Base64 | 从文件提取 |
| Combine Invoice, Logo & Signature | 数据合并 |
| Prepare All Data for Template | Code |
| Build HTML Invoice from Data | HTML |
| Convert HTML to Binary File | 转换为文件 |
| Generate PDF via Gotenberg | HTTP Request |
| Email PDF Invoice to Customer | Email 发送 |

## 触发方式
- Listen for New QuickBooks Invoice 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：7
- 输出节点：4
- 分类：workflow-automation
