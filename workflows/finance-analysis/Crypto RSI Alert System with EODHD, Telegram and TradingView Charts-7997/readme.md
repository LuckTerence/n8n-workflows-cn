## 简介
**Crypto RSI Alert System with EODHD, Telegram and TradingView Charts**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/7997

---

# Crypto RSI Alert System with EODHD, Telegram and TradingView Charts


## 节点清单

| 节点 | 类型 |
|------|------|
| When clicking ‘Execute workflow’ | 手动触发 |
| Edit Fields (watchlist) | 数据设置 |
| Split Out | 数据拆分 |
| Loop Over Items | 分批处理 |
| HTTP Request (EODHD intraday 1h) | HTTP Request |
| Code (RSI + message) | Code |
| IF (has signal?) | IF 判断 |
| Send a text message | Telegram |

## 触发方式
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：5
- 输出节点：2
- 分类：finance-analysis
