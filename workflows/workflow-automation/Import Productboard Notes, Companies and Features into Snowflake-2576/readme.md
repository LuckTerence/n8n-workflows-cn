## 简介
**Import Productboard Notes, Companies and Features into Snowflake**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/2576

---

# Import Productboard Notes, Companies and Features into Snowflake


## 节点清单

| 节点 | 类型 |
|------|------|
| Manual mapping feature | 数据设置 |
| get productboard companies | HTTP Request |
| Manual mapping companies | 数据设置 |
| get productboard notes | HTTP Request |
| Manual mapping notes | 数据设置 |
| Split features | 数据拆分 |
| Split companies | 数据拆分 |
| Split notes | 数据拆分 |
| Split features in notes | 数据拆分 |
| Combine Feature ID + Note ID | 数据设置 |
| get productboard features | HTTP Request |
| Update Productboard Notes | Snowflake |
| Empty Table Productboard Notes | Snowflake |
| [CREATE] PRODUCTBOARD_NOTES | Snowflake |
| [CREATE] PRODUCTBOARD_COMPANIES | Snowflake |
| Update Productboard Companies | Snowflake |
| Manual mapping companies db | 数据设置 |
| Manual mapping notes db | 数据设置 |
| Empty Table Productboard Companies | Snowflake |
| [CREATE] PRODUCTBOARD_NOTES_FEATURES | Snowflake |
| Manual mapping feature note IDs db | 数据设置 |
| Update Productboard Note and Feature IDs | Snowflake |
| Empty Table Productboard Note and Feature IDs | Snowflake |
| Loop Over Items notes | 分批处理 |
| Loop Over Items features notes | 分批处理 |
| [CREATE] PRODUCTBOARD_FEATURES | Snowflake |
| Empty Table Productboard Features | Snowflake |
| Loop Over Items features | 分批处理 |
| Manual mapping features db | 数据设置 |
| Update Productboard Features | Snowflake |
| Schedule Trigger | 定时触发器 |
| Slack | Slack |
| Count Notes Last 7 days and Unprocessed | Snowflake |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：33
- 触发节点：1
- 处理节点：28
- 输出节点：4
- 分类：workflow-automation
