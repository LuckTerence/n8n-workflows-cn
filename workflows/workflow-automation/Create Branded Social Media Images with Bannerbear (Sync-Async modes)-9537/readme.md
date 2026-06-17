# Create Branded Social Media Images with Bannerbear (Sync-Async modes)

https://n8nworkflows.xyz/workflows/9537

## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| SetParameters | 数据设置 |
| SynchronouslyCreateImage | HTTP Request |
| GetImageUrlAndSize | 数据设置 |
| Webhook_OnImageCreated | Webhook |
| GetUidAndStatus | 数据设置 |
| GetCompletedImageInfo | 数据设置 |
| IfSynchrounousCall | IF 判断 |
| AsynchronouslyCreateImage | bannerbear |

## 触发方式
- When clicking ‘Execute workflow’ 触发
- Webhook_OnImageCreated 触发

## 统计
- 节点总数：9
- 触发节点：2
- 处理节点：6
- 输出节点：1
- 分类：workflow-automation
