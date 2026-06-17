# Process Sales CSVs into Invoices with Data Tables and Email Notifications

https://n8nworkflows.xyz/workflows/10274

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Sales CSV | Webhook |
| Check Upload Type | IF 判断 |
| Extract CSV Text | 从文件提取 |
| Parse & Validate CSV | Code |
| Enrich with Product Data | Code |
| Calculate Invoice Totals | Code |
| Check for Duplicates | Code |
| Has Valid Invoices? | IF 判断 |
| Prepare Email Notifications | Code |
| Merge Results | Code |
| Return Success Response | 响应 Webhook |
| Return Duplicate Error | 响应 Webhook |
| Load Product Catalog | 数据表 |
| Insert row | 数据表 |
| Aggregate | 数据聚合 |
| Email Output Preview | 数据设置 |
| Extract from File | 从文件提取 |
| Return Validation Error | 响应 Webhook |

## 触发方式
- Receive Sales CSV 触发

## 统计
- 节点总数：18
- 触发节点：1
- 处理节点：14
- 输出节点：3
- 分类：workflow-automation
