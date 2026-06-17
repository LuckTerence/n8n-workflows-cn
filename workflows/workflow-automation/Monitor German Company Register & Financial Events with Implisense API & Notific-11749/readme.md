# Monitor German Company Register & Financial Events with Implisense API & Notifications

https://n8nworkflows.xyz/workflows/11749

## 节点清单

| 节点 | 类型 |
|------|------|
| Split Batches | 分批处理 |
| Rate Limit | 等待 |
| API Success? | IF 判断 |
| Normalize Events | Code |
| Log API Error | Code |
| Merge Results | 数据合并 |
| Filter Relevant | IF 判断 |
| Deduplicate | 去重 |
| Prepare Notification | Code |
| Notification Sent? | IF 判断 |
| Log Success | Code |
| Log Failed | Code |
| Merge Notifications | 数据合并 |
| Loop Continue | 空操作 |
| Create Summary | Code |
| Lookup Company | HTTP Request |
| Get Events | HTTP Request |
| Config | 数据设置 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Mock Lead Input | Function |
| Email, Chat, Webhook etc. | 空操作 |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：18
- 输出节点：2
- 分类：workflow-automation
