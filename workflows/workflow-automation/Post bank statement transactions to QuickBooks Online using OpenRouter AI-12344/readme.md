# Post bank statement transactions to QuickBooks Online using OpenRouter AI

https://n8nworkflows.xyz/workflows/12344

## 节点清单

| 节点 | 类型 |
|------|------|
| Extract PDF Text | 从文件提取 |
| Transaction Extractor AI | AI Agent |
| JSON Output Parser | 结构化输出解析器 |
| Create QuickBooks SalesReceipt | HTTP Request |
| Bank Statement Form | 表单触发器 |
| OpenRouter Chat Model | OpenRouter Chat Model |
| Split Transactions | 数据拆分 |
| Loop Over Items | 分批处理 |
| Build Salesreceipt Payload | Code |
| Get many customers | QuickBooks |
| Create Vendor | QuickBooks |
| Vendor Exists? | IF 判断 |
| Find Vendor | QuickBooks |
| Search Categories | HTTP Request |
| Create Items | HTTP Request |
| Collect All Item Mappings | Code |
| Need to Create Items? | IF 判断 |
| Get All QB Items | QuickBooks |
| Check Which Items to Create | Code |
| Credit or Debit? | Switch 路由 |
| Customers Exists?1 | IF 判断 |
| Create a Customer | QuickBooks |
| Create QuickBooks Expense | HTTP Request |
| Build Expense Payload | Code |

## 触发方式
- Bank Statement Form 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：19
- 输出节点：4
- 分类：workflow-automation
