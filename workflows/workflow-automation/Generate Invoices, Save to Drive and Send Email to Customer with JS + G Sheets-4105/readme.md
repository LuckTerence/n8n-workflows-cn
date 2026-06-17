## 简介
**Generate Invoices, Save to Drive and Send Email to Customer with JS + G Sheets**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Google Sheets/Google Drive)（基本改完，配置 API Key 应该就能跑）
> 节点数：10 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/4105

---

# Generate Invoices, Save to Drive and Send Email to Customer with JS + G Sheets


## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook Simulator | Webhook |
| Generate Invoice ID | Code |
| Check if ID Already Exists | Google Sheets |
| If Does not Exist | IF 判断 |
| Set Fields | 数据设置 |
| Create Invoice HTML | Code |
| HTML to PDF | HTTP Request |
| Upload PDF to GDrive | Google Drive |
| Email Invoice to Customer | Email 发送 |
| Append Details to Invoices Sheet | Google Sheets |
| Download PDF from API | HTTP Request |

## 触发方式
- Webhook Simulator 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：7
- 输出节点：3
- 分类：workflow-automation
