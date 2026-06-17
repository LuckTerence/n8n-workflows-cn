## 简介
**Aggregate Crypto and Stock Market News Feed from Multiple Sources**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：32 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/11103

---

# Aggregate Crypto and Stock Market News Feed from Multiple Sources


## 节点清单

| 节点 | 类型 |
|------|------|
| Schedule Trigger | 定时触发器 |
| RSS Read - Coindesk | RSS Feed |
| RSS Read - Google news | RSS Feed |
| RSS Read - X Posts | RSS Feed |
| Source set - Coindesk | 数据设置 |
| Source set - Google news | 数据设置 |
| Source set - Cointelegraph | 数据设置 |
| Source set - X Posts | 数据设置 |
| Merge - Coindesk + Google news | 数据合并 |
| Merge - X posts + CoinTelegraph | 数据合并 |
| Merge - Merge previous two merges | 数据合并 |
| Code - Keywords Filter | Code |
| Code - Array bind | Code |
| Webhook | Webhook |
| Merge | 数据合并 |
| Init RunConfig | Code |
| IF Gate - Coindesk | IF 判断 |
| IF Gate - Google news | IF 判断 |
| IF Gate - CoinTelegraph | IF 判断 |
| IF Gate - X | IF 判断 |
| X Batches | 分批处理 |
| IF - More X batches? | IF 判断 |
| Code - Finalize X batches (emit combined) | Code |
| Code - Accumulate X items | Code |
| Code - Reset X accumulator | Code |
| Code - URL Build - XCancel | Code |
| Code - Tag topic - Google news | Code |
| Code - Tag topic - Coin desk | Code |
| Code - Tag topic - X | Code |
| Code - URL build - Google news | Code |
| HTTP Request - Send to your backend | HTTP Request |
| Loop back – X Batches | 空操作 |
| Code - Tag topic - Coin telegraph | Code |
| RSS Read - CoinTelegraph | RSS Feed |

## 触发方式
- Schedule Trigger 触发
- RSS Read - Coindesk 触发
- RSS Read - Google news 触发
- RSS Read - X Posts 触发
- Webhook 触发
- RSS Read - CoinTelegraph 触发

## 统计
- 节点总数：34
- 触发节点：6
- 处理节点：27
- 输出节点：1
- 分类：finance-analysis
