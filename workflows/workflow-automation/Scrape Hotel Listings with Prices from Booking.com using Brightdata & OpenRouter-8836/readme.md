# Scrape Hotel Listings with Prices from Booking.com using Brightdata & OpenRouter AI

https://n8nworkflows.xyz/workflows/8836

## 节点清单

| 节点 | 类型 |
|------|------|
| parameters | 数据设置 |
| OpenRouter Chat Model2 | OpenRouter Chat Model |
| check Snapshot Again | 空操作 |
| Wait | 等待 |
| check if result ready | IF 判断 |
| Initiate batch extraction from URL | brightData |
| Check the status of a batch extraction | brightData |
| hotels | 分批处理 |
| Download the snapshot content | brightData |
| clean data | 数据设置 |
| When chat message received | Chat 触发器 |
| Aggregate | 数据聚合 |
| Human Friendly Results | AI Agent |
| Calculator | 计算器工具 |

## 触发方式
- When chat message received 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：13
- 输出节点：0
- 分类：workflow-automation
