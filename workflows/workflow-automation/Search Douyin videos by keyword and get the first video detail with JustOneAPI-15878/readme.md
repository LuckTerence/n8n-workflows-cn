# Search Douyin videos by keyword and get the first video detail with JustOneAPI

https://n8nworkflows.xyz/workflows/15878

## 节点清单

| 节点 | 类型 |
|------|------|
| Start Workflow Manually | 手动触发 |
| Set API and Search Parameters | 数据设置 |
| Fetch Douyin Video Search Results | HTTP Request |
| Store Raw Search Results | 数据设置 |
| Extract Video IDs from Search | Code |
| Store Extracted Video IDs | 数据设置 |
| Fetch First Video Details | HTTP Request |
| Build Clean Video Detail | Code |
| Store Final Video Details | 数据设置 |

## 触发方式
- Start Workflow Manually 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：6
- 输出节点：2
- 分类：workflow-automation
