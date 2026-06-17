# Fetch Odoo Customer Data and Export to JSON or Excel

https://n8nworkflows.xyz/workflows/10599

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Company Request1 | Webhook |
| Prepare Dynamic Filter1 | Function |
| Prepare Output Data1 | Function |
| Check If Excel Required1 | IF 判断 |
| Convert to Excel1 | 转换为文件 |
| Respond with File1 | 响应 Webhook |
| Respond with JSON1 | 响应 Webhook |
| Fetch Customer | odoo |
| Return all data for create binary file | Code |

## 触发方式
- Receive Company Request1 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
