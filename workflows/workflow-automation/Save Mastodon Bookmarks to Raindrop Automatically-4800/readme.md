# Save Mastodon Bookmarks to Raindrop Automatically

https://n8nworkflows.xyz/workflows/4800

## 节点清单

| 节点 | 类型 |
|------|------|
| Allows manual testing of the workflow | 手动触发 |
| Triggers the workflow on a set interval | 定时触发器 |
| Retrieves the last processed min_id to avoid duplicates | Code |
| Makes authenticated request to Mastodon’s bookmarks API | HTTP Request |
| Ensures the response has bookmarks before continuing | IF 判断 |
| Extracts pagination data (like next min_id) from HTTP headers | Code |
| Saves the new min_id to workflow static data | Code |
| Splits API response into individual bookmark items | 数据拆分 |
| Filters out invalid or incomplete bookmark data | IF 判断 |
| Saves valid bookmark using post metadata (e.g., title, card.url) | raindrop |
| Saves bookmark using alternate fields if card data is missing | raindrop |

## 触发方式
- Allows manual testing of the workflow 触发
- Triggers the workflow on a set interval 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：8
- 输出节点：1
- 分类：workflow-automation
