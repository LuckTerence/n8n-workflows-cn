# Fix & Resend Guest Order Emails in Magento 2 via REST API

https://n8nworkflows.xyz/workflows/6707

## 节点清单

| 节点 | 类型 |
|------|------|
| On form submission | 表单触发器 |
| Get Order By Increment ID | HTTP Request |
| Checks If Order Exist | IF 判断 |
| Code | Code |
| Update Guest Order Email | MySQL |
| resend order confirmation | HTTP Request |
| Checks for Resend | IF 判断 |

## 触发方式
- On form submission 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：4
- 输出节点：2
- 分类：workflow-automation
