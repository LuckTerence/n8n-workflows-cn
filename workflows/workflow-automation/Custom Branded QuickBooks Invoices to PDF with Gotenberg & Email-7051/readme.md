## 简介
**Custom Branded QuickBooks Invoices to PDF with Gotenberg & Email**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7051

---

# Custom Branded QuickBooks Invoices to PDF with Gotenberg & Email


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
