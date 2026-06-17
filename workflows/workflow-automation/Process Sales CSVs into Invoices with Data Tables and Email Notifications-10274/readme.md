## 简介
**Process Sales CSVs into Invoices with Data Tables and Email Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Gmail)（基本改完，配置 API Key 应该就能跑）
> 节点数：17 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/10274

---

# Process Sales CSVs into Invoices with Data Tables and Email Notifications


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
