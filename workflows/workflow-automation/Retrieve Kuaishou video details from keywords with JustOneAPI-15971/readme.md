# Retrieve Kuaishou video details from keywords with JustOneAPI

https://n8nworkflows.xyz/workflows/15971

## 节点清单

| 节点 | 类型 |
|------|------|
| Manual Trigger Start | 手动触发 |
| Prepare API and Research Fields | 数据设置 |
| Search Kuaishou Videos via API | HTTP Request |
| Output Search Video Results | 数据设置 |
| Extract Video IDs with Code | Code |
| Output Extracted Video IDs | 数据设置 |
| If Video ID Exists | IF 判断 |
| Fetch Video Details via API | HTTP Request |
| Build Video Details with Code | Code |
| Output Video Details List | 数据设置 |

## 触发方式
- Manual Trigger Start 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：workflow-automation
