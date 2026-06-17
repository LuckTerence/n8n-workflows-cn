# Clean up stale Entra B2B guest accounts with Microsoft Graph, Teams, and SharePoint

https://n8nworkflows.xyz/workflows/16118

## 节点清单

| 节点 | 类型 |
|------|------|
| Weekly Trigger at 8am Monday | 定时触发器 |
| Set Config Parameters | 数据设置 |
| Initialize Pagination Loop | Code |
| Fetch Guest Page via URL | HTTP Request |
| Accumulate Guests from Page | Code |
| If More Pages Available | IF 判断 |
| Set Next URL | 数据设置 |
| Filter Stale Guest Accounts | Code |
| Check Stale Guests Presence | IF 判断 |
| Notify No Stale Guests | Teams |
| Unpack Stale Guests Array | Code |
| Loop Over Stale Guests | 分批处理 |
| Fetch Guest Manager | HTTP Request |
| Prepare Guest and Sponsor Data | 数据设置 |
| Send Notification to Sponsor | Teams |
| Wait 72 Hours for Reply | 等待 |
| Delete Stale Guest Account | HTTP Request |
| Check Deletion Success | IF 判断 |
| Log Deletion in SharePoint | HTTP Request |
| Alert Deletion Error | Teams |
| Merge Data for Next Guest | 数据合并 |
| Proceed to Next Guest | 空操作 |
| Final Guest Processed | 空操作 |
| Post Process Summary in Teams | Teams |

## 触发方式
- Weekly Trigger at 8am Monday 触发

## 统计
- 节点总数：24
- 触发节点：1
- 处理节点：15
- 输出节点：8
- 分类：workflow-automation
