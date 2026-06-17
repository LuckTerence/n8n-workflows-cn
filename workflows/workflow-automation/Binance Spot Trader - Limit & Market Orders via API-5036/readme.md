## 简介
**Binance Spot Trader - Limit & Market Orders via API**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5036

---

# Binance Spot Trader - Limit & Market Orders via API


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Set Account Query | 数据设置 |
| Signature Get Account | 加密 |
| Account Info Query | Code |
| Order Query | Code |
| LimitBuy Parmeter | 数据设置 |
| Set Credentials | 数据设置 |
| Get Account Info | HTTP Request |
| LimitSale Parameter | 数据设置 |
| Sale Query | Code |
| Execute Limit SELL | HTTP Request |
| Execute Limit BUY | HTTP Request |
| Market Buy Query | Code |
| MarketBuy Parameter | 数据设置 |
| Signature MarketBuy | 加密 |
| Signature Limit BUY | 加密 |
| Signature Limit SELL | 加密 |
| Execute MarketBuy | HTTP Request |
| MarketSell Parameter | 数据设置 |
| Market Sell Query | Code |
| Signature MarketSell | 加密 |
| Execute MarketSell | HTTP Request |
| OpenOrder Query | Code |
| Open Orders Params | 数据设置 |
| Signature OpenOrder | 加密 |
| Get Open Orders | HTTP Request |
| Cancel All Order Params | 数据设置 |
| CancelAllOrder Query | Code |
| Signature Cancel All Order | 加密 |
| Cancell All Order | HTTP Request |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：22
- 输出节点：7
- 分类：workflow-automation
