# Automatically Send a Direct Message (DM) to New Followers on Bluesky using Baserow

https://n8nworkflows.xyz/workflows/2827

## 节点清单

| 节点 | 类型 |
|------|------|
| Create Bluesky Session | HTTP Request |
| Run Daily at 9 AM | 定时触发器 |
| Set Bluesky Credentials | 数据设置 |
| Extract Followers Array | Code |
| Create Follower Record | baserow |
| Get Follower Record | baserow |
| If Follower Exists | IF 判断 |
| Limit | 数据限制 |
| Get All New Followers | baserow |
| Send Welcome Message | HTTP Request |
| Create Welcome Message | Code |
| Loop New Followers | 分批处理 |
| Loop Followers | 分批处理 |
| END OF WORKFLOW | 空操作 |
| Double Check If Welcome Has Already Been Sent | IF 判断 |
| Wait Follower Loop | 等待 |
| Wait New Follower Loop | 等待 |
| Get Firstname | Code |
| Update Follower Record to SentWelcome = TRUE | baserow |
| Get Latest Followers | HTTP Request |
| Get ConvoId | HTTP Request |

## 触发方式
- Run Daily at 9 AM 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：16
- 输出节点：4
- 分类：workflow-automation
