# Automated Forex and Gold Trading Signal Handler with MetaTrader 5 via Webhooks

https://n8nworkflows.xyz/workflows/11439

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive Signal (POST) | Webhook |
| Store Signal | Code |
| Respond to POST | 响应 Webhook |
| Get Pending Signals (GET) | Webhook |
| Fetch Pending Signals | Code |
| Return Signals | 响应 Webhook |
| Confirm Signal Processed (POST) | Webhook |
| Mark as Processed | Code |
| Confirm Response | 响应 Webhook |
| clear all signals | Code |
| Clear all signals (POST) | Webhook |
| Market Order (POST) | Webhook |
| market order code | Code |
| Respond to Webhook | 响应 Webhook |
| Limit Order (POST) | Webhook |
| limit order code | Code |
| Respond to Limit Order | 响应 Webhook |
| confirm signals are cleared | 响应 Webhook |

## 触发方式
- Receive Signal (POST) 触发
- Get Pending Signals (GET) 触发
- Confirm Signal Processed (POST) 触发
- Clear all signals (POST) 触发
- Market Order (POST) 触发
- Limit Order (POST) 触发

## 统计
- 节点总数：18
- 触发节点：6
- 处理节点：6
- 输出节点：6
- 分类：finance-analysis
