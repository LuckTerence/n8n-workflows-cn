# Discover, enrich & store cryptocurrency data with CoinMarketCap API

https://n8nworkflows.xyz/workflows/10969

## 节点清单

| 节点 | 类型 |
|------|------|
| CLEAN CMC FIELDS | 数据设置 |
| Split Out | 数据拆分 |
| CMC SPLIT IN BATCHES | 分批处理 |
| Generate Random Page | Code |
| No Operation, do nothing3 | 空操作 |
| ADD TO CMC | 分批处理 |
| Every 3 Days At 10AM | 定时触发器 |
| Get Token Details From CMC | HTTP Request |
| EXTRACT WEBSITE | 数据设置 |
| CLEAN WEBSITE | 数据设置 |
| Wait 1 Min | 等待 |
| Clean up Output | 数据设置 |
| CMC Token DATA | Code |
| ADD TO CMC Sheet | NocoDB |
| Get 100 Tokens From CMC | HTTP Request |
| DATA | Code |

## 触发方式
- Every 3 Days At 10AM 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：finance-analysis
