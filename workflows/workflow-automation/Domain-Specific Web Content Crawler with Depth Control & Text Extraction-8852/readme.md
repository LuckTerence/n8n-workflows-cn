# Domain-Specific Web Content Crawler with Depth Control & Text Extraction

https://n8nworkflows.xyz/workflows/8852

## 节点清单

| 节点 | 类型 |
|------|------|
| Webhook | Webhook |
| Loop Links (Batches) | 分批处理 |
| IF Crawl Depth OK? | IF 判断 |
| Extract Body & Links | HTML |
| Attach URL/Depth to HTML | Code |
| Fetch HTML Page | HTTP Request |
| Seed Root Crawl Item | 数据合并 |
| Collect Pages & Emit When Done | Code |
| Store Page Data | 数据设置 |
| Merge Web Pages | 数据合并 |
| Combine & Chunk | Code |
| Respond to Webhook | 响应 Webhook |
| Init Globals | Code |
| Init Crawl Params | 数据设置 |
| Requeue Link Item | Code |
| Queue & Dedup Links | Code |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
