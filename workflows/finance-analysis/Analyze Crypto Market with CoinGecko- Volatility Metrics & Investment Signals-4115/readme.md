# Analyze Crypto Market with CoinGecko: Volatility Metrics & Investment Signals

https://n8nworkflows.xyz/workflows/4115

## 节点清单

| 节点 | 类型 |
|------|------|
| Fetch Crypto Data | HTTP Request |
| Calculate Market Metrics | Function |
| IF 24h Price Up >5% | IF 判断 |
| IF 24h Price Down >5% | IF 判断 |
| IF High Volatility | IF 判断 |
| Set Uptrend Data | 数据设置 |
| Set Downtrend Data | 数据设置 |
| Set Volatility Data | 数据设置 |
| Set Stable Data | 数据设置 |
| Merge Results | 空操作 |
| Set High Risk Rating | 数据设置 |
| Set Medium Risk Rating | 数据设置 |
| Set Low Risk Rating | 数据设置 |
| Set Default Risk Rating | 数据设置 |
| Final Merge | 空操作 |
| Format Final Analysis | Function |
| Collect All Analyses | 空操作 |
| Generate Portfolio Summary | Function |
| Loop Over Items | 分批处理 |
| Switch by Market Score | Switch 路由 |
| Split Out | 数据拆分 |
| Respond to Webhook | 响应 Webhook |
| Webhook | Webhook |

## 触发方式
- Webhook 触发

## 统计
- 节点总数：23
- 触发节点：1
- 处理节点：20
- 输出节点：2
- 分类：finance-analysis
