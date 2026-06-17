## 简介
**Analyze DEX Liquidity, Trades & Spot Pairs with CoinMarketCap AI Agent**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：12 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3424

---

# Analyze DEX Liquidity, Trades & Spot Pairs with CoinMarketCap AI Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| CoinMarketCap DEXScan Agent | AI Agent |
| DEXScan Agent Brain | OpenAI Chat Model |
| DEXScan Agent Memory | 记忆缓冲区 |
| DEX Metadata | HTTP 工具 |
| DEX Networks List | HTTP 工具 |
| DEX Listings Quotes | HTTP 工具 |
| DEX Pair Quotes Latest | HTTP 工具 |
| DEX OHLCV Historical | HTTP 工具 |
| DEX OHLCV Latest | HTTP 工具 |
| DEX Trades Latest | HTTP 工具 |
| DEX Spot Pairs Latest | HTTP 工具 |

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：12
- 触发节点：1
- 处理节点：3
- 输出节点：8
- 分类：workflow-automation
