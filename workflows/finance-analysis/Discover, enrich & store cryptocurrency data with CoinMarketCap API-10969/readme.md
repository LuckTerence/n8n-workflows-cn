## 简介
**Discover, enrich & store cryptocurrency data with CoinMarketCap API**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 节点数：15 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/10969

---

# Discover, enrich & store cryptocurrency data with CoinMarketCap API


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
