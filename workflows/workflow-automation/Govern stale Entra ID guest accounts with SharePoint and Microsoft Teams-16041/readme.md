## 简介
**Govern stale Entra ID guest accounts with SharePoint and Microsoft Teams**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：50 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/16041

---

# Govern stale Entra ID guest accounts with SharePoint and Microsoft Teams


## 节点清单

| 节点 | 类型 |
|------|------|
| Split Pending Items | Code |
| Mark Pending as Error | SharePoint |
| Log Retention to Teams | Teams |
| Mark Pending as Retained | SharePoint |
| Delete Error Alert | Teams |
| Mark Pending as Deleted | SharePoint |
| Log Deletion to Audit List | SharePoint |
| Delete Succeeded? | IF 判断 |
| Delete Stale Guest Account | microsoftEntra |
| Retention Exception? | IF 判断 |
| Check Retention Exception | SharePoint |
| Nothing Due Today | 空操作 |
| Any Due For Deletion? | IF 判断 |
| Get Overdue Pending Deletions | SharePoint |
| Config (Executioner) | 数据设置 |
| Daily Cron Trigger | 定时触发器 |
| Skip - Already Queued | 空操作 |
| Queue Pending Deletion | SharePoint |
| Not Yet Queued? | IF 判断 |
| Already Queued? | SharePoint |
| Alert IT Security - No Sponsor | Teams |
| Notify Sponsor via Teams Channel | Teams |
| Valid Sponsor Email? | IF 判断 |
| Filter Stale Per Page | Code |
| Get Guest Users | HTTP Request |
| Config | 数据设置 |
| Weekly Cron Trigger | 定时触发器 |
| When Weekly Triggered at 8 AM | 定时触发器 |
| Set Configuration Parameters | 数据设置 |
| Fetch Guest Users from Graph | HTTP Request |
| Filter Stale Accounts | Code |
| Check for Valid Sponsor Email | IF 判断 |
| Notify Sponsor via Teams | Teams |
| Alert IT of Missing Sponsor | Teams |
| Check if Already Queued | SharePoint |
| Check Not Yet Queued | IF 判断 |
| Queue for Pending Deletion | SharePoint |
| Skip This - Already Queued | 空操作 |
| When Daily Triggered at 9 AM | 定时触发器 |
| Set Execution Parameters | 数据设置 |
| Fetch Overdue Pending Deletions | SharePoint |
| Check Due for Deletion | IF 判断 |
| No Deletions Due Today | 空操作 |
| Verify Retention Exception | SharePoint |
| Is Retention Exception Present? | IF 判断 |
| Remove Stale Guest Account | microsoftEntra |
| Verify Deletion Success | IF 判断 |
| Record Deletion in Audit Log | SharePoint |
| Update Status to Deleted | SharePoint |
| Notify Delete Error via Teams | Teams |
| Update Status to Retained | SharePoint |
| Notify Retention via Teams | Teams |
| Update Status to Error | SharePoint |
| Distribute Pending Items | Code |

## 触发方式
- Daily Cron Trigger 触发
- Weekly Cron Trigger 触发
- When Weekly Triggered at 8 AM 触发
- When Daily Triggered at 9 AM 触发

## 统计
- 节点总数：54
- 触发节点：4
- 处理节点：40
- 输出节点：10
- 分类：workflow-automation
