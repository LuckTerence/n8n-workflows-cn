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



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发、Telegram 消息触发，通过 Telegram 通知 实现自动化。

> 适配等级：Tier A — 可直接使用（国内环境配好 API Key 即可）

## 前置准备

导入前请准备以下服务的 API 凭证：

- Telegram Bot Token → @BotFather 创建

## 使用步骤

1. 下载 `workflow.json`
2. 在 n8n 中点击 **Import from File** 导入
3. 按上方「前置准备」填入对应服务的 API Key
4. 点击 **Execute Workflow** 测试运行

## 统计

- 节点总数：32
- 触发方式：定时触发, Telegram 消息触发

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
