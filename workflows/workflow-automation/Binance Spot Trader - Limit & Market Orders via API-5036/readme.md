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



## 功能说明

电商自动化，订单处理或商品管理。

手动触发，通过 HTTP API 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

无需额外 API Key，导入即可运行。

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：30
- 触发方式：手动触发

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：30
- 触发节点：1
- 处理节点：22
- 输出节点：7
- 分类：workflow-automation
