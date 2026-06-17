# Send pre-meeting context briefings with Outlook, SharePoint, Entra ID and Teams

https://n8nworkflows.xyz/workflows/16107

## 节点清单

| 节点 | 类型 |
|------|------|
| When Every 30 Minutes | 定时触发器 |
| Set Config Parameters | 数据设置 |
| Loop Over VIP Mailboxes | 分批处理 |
| Extract VIP Mailbox Data | Code |
| Fetch Calendar Events | Outlook |
| Filter Events for Briefing | Code |
| Check Events to Brief | IF 判断 |
| No Events Switch Mailbox | 空操作 |
| Loop Through Events | 分批处理 |
| Extract Event Data | Code |
| Post to SharePoint Search API | HTTP Request |
| Build Attendee Request Payload | Code |
| Post to Graph API for Attendees | HTTP Request |
| Compile Event Briefing | Code |
| Dispatch Briefing to Teams | Teams |
| Proceed to Next Event | 空操作 |
| All Mailboxes Completed | 空操作 |
| Teams Briefing Error Notice | Teams |
| Check Briefing Sent Status | IF 判断 |
| Merge Data Before Next Event | 数据合并 |
| Mark Event as Briefed | Code |
| Combine Batch API Response | Code |
| Combine SP Search Response | Code |
| Check for Attendee Requests | IF 判断 |
| Skip Attendee Batch Processing | Code |
| Build SharePoint Query | Code |

## 触发方式
- When Every 30 Minutes 触发

## 统计
- 节点总数：26
- 触发节点：1
- 处理节点：20
- 输出节点：5
- 分类：workflow-automation
