## 简介
**Send crypto price alerts, daily digests and -price replies with CoinGecko, Telegram and Sheets**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（需替换Google Sheets)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/16061

---

# Send crypto price alerts, daily digests and -price replies with CoinGecko, Telegram and Sheets


## 节点清单

| 节点 | 类型 |
|------|------|
| Hourly Trigger | 定时触发器 |
| Configure Watchlist | Code |
| Loop Over Assets | 分批处理 |
| Fetch Crypto Prices | HTTP Request |
| Merge Market Data | Code |
| If Price Data Exists | IF 判断 |
| Load Asset State | Code |
| If First Time Running | IF 判断 |
| Store Initial Price | Code |
| Fetch RSI Values | HTTP Request |
| Compute RSI | Code |
| Check Alert Conditions | Code |
| If Alert Needed | IF 判断 |
| If Alert Cooldown Over | IF 判断 |
| Create Alert Message | Code |
| Send Alert on Telegram | Telegram |
| Append Alert to Sheets | Google Sheets |
| Save Alert Status | Code |
| Log Price Without Alert | Code |
| Daily 8am Trigger | 定时触发器 |
| Configure Daily Digest | Code |
| Retrieve All Crypto Prices | HTTP Request |
| Get Fear & Greed Index | HTTP Request |
| Build Daily Digest Message | Code |
| Send Digest on Telegram | Telegram |
| When Telegram Command Received | Telegram 触发器 |
| Decode Telegram Message | Code |
| If Command is /price | IF 判断 |
| Fetch Specific Price | HTTP Request |
| Create Price Reply Message | Code |
| Send Price Reply on Telegram | Telegram |
| Send Unknown Command Alert | Telegram |

## 触发方式
- Hourly Trigger 触发
- Daily 8am Trigger 触发
- When Telegram Command Received 触发

## 统计
- 节点总数：32
- 触发节点：3
- 处理节点：20
- 输出节点：9
- 分类：finance-analysis
