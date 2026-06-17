# Dynamic Media Library with On-demand Downloads for Radarr-Sonarr and Plex

https://n8nworkflows.xyz/workflows/6980

## 节点清单

| 节点 | 类型 |
|------|------|
| Respond to Webhook | 响应 Webhook |
| Format JustWatch results | Code |
| Call JustWatch API | HTTP Request |
| Remove unmonitored tag | HTTP Request |
| If tag unmonitored exists | IF 判断 |
| If Radarr | IF 判断 |
| If tag unmonitored exists Sonarr | IF 判断 |
| Remove unmonitored tag Sonarr | HTTP Request |
| Webhook Arrs Dummy file update | Webhook |
| Switch eventType | Switch 路由 |
| Create dummy file for movie1 | SSH |
| Refresh movie1 | HTTP Request |
| Refresh series1 | HTTP Request |
| Refresh Plex | HTTP Request |
| Refresh Plex Series | HTTP Request |
| Sonarr runtime s01e01 | HTTP Request |
| Create dummy file for series with runtime | SSH |
| Radarr movie | HTTP Request |
| Sonarr series | HTTP Request |
| Create dummy file | SSH |
| Search movie | HTTP Request |
| Respond 200 | 响应 Webhook |
| Monitor movie | HTTP Request |
| Respond  | 响应 Webhook |
| Monitor series | HTTP Request |
| Monitor all seasons | HTTP Request |
| If movie4 | IF 判断 |
| Get Radarr information from tmdbId | HTTP Request |
| Get Sonarr information from tvdbId | HTTP Request |
| Webhook Tautulli | Webhook |
| Check if collection is not empty | IF 判断 |
| If objectType is movie | IF 判断 |
| Respond to Webhook1 | 响应 Webhook |
| Format JustWatch results add tvdbId | Code |
| Sonarr serie lookup1 | HTTP Request |
| Webhook Arrs custom list JustWatch | Webhook |
| Webhook Arrs custom list Trakt | Webhook |
| Call Trakt API | HTTP Request |
| Format JustWatch results1 | Code |
| Respond to Webhook2 | 响应 Webhook |
| Get all items in collection1 | HTTP Request |
| Check if collection contains items1 | IF 判断 |
| Split Out Collection Items1 | 数据拆分 |
| Loop Over Items1 | 分批处理 |
| Remove item from collection1 | HTTP Request |
| Get collection1 | HTTP Request |
| Loop Over Items3 | 分批处理 |
| Get GUID from imdbId | HTTP Request |
| Add item to collection2 | HTTP Request |
| Add item to collection3 | HTTP Request |
| Get ratingKey from GUID1 | HTTP Request |
| Move collection item2 | HTTP Request |
| If found Plex GUID1 | IF 判断 |
| Merge1 | 数据合并 |
| Code | Code |
| Merge | 数据合并 |
| Merge2 | 数据合并 |
| Create dummy file for movie | SSH |
| Get Overseerr users | HTTP Request |
| Filter Overseerr user | Code |
| Check if Overseerr user is found | IF 判断 |
| Make Overseerr request | HTTP Request |
| Get last 20 Overseerr requests from user | HTTP Request |
| Check if request already exists | Code |
| Check if no existing request for media exist for Overseerr user | IF 判断 |
| Terminate Tautulli sessions for dummy | HTTP Request |
| Get all active sessions for file | Code |
| Monitor all seasons1 | HTTP Request |
| Remove all dummy files | SSH |
| If deletedFiles exist | IF 判断 |
| Get active Tautulli sessions | HTTP Request |
| Refresh series | HTTP Request |
| Get Sonarr information for series | HTTP Request |
| Search series2 | HTTP Request |
| Search series season | HTTP Request |
| Code1 | Code |
| Merge3 | 数据合并 |
| Search season pack | HTTP Request |
| Search season pack1 | HTTP Request |
| Set fields for collection | 数据设置 |
| Wait 5 minutes before process collection in Plex | 等待 |

## 触发方式
- Webhook Arrs Dummy file update 触发
- Webhook Tautulli 触发
- Webhook Arrs custom list JustWatch 触发
- Webhook Arrs custom list Trakt 触发

## 统计
- 节点总数：81
- 触发节点：4
- 处理节点：34
- 输出节点：43
- 分类：workflow-automation
