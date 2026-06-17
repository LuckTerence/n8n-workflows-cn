# Secure Web Form to Odoo CRM Lead Creation with UTM Tracking

https://n8nworkflows.xyz/workflows/7289

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook - Lead Webform | Webhook |
| Merge | 数据合并 |
| Create Lead | odoo |
| Prepare Request | Code |
| Execution Data | executionData |
| UTM: Get Source ID | odoo |
| UTM: Get Medium ID | odoo |
| UTM: Get Campaign ID | odoo |
| Success | 响应 Webhook |
| Required data missing? | IF 判断 |
| Bad Request | 响应 Webhook |
| Source ID Validation | Code |
| Medium ID Validation | Code |
| Campaign ID Validation | Code |

## 触发方式
- Webhook - Lead Webform 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：11
- 输出节点：2
- 分类：workflow-automation
