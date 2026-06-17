# Audit SharePoint Online external sharing and anonymous links with Microsoft Graph

https://n8nworkflows.xyz/workflows/12495

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Sharepoint - Get Sites | HTTP Request |
| Split Out - Sites | 数据拆分 |
| SharePoint - Get Drives | HTTP Request |
| Split Out - Drives | 数据拆分 |
| SharePoint - Get Item Permissions | HTTP Request |
| Filter Items based on permissions | Code |
| SharePoint - Get Items | HTTP Request |
| Split Out - Items | 数据拆分 |
| If Item is not a folder | IF 判断 |
| If Input is a Folder | IF 判断 |
| SharePoint - Get Child Items | HTTP Request |
| Call 'Audit SharePoint for externally shared Items and anonymous permissions' | 执行工作流 |
| Subworkflow - Get Items | 执行工作流触发器 |
| Recursive call Get Items | 执行工作流 |
| Return All Data | 数据设置 |
| Keept Items and Folders | 数据合并 |
| Merge | 数据合并 |
| Rename Output for Permissions | 数据设置 |
| Rename Output for Item | 数据设置 |
| Set Variables | 数据设置 |
| Filter sites | 过滤器 |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Subworkflow - Get Items 触发

## 统计
- 节点总数：22
- 触发节点：2
- 处理节点：15
- 输出节点：5
- 分类：workflow-automation
