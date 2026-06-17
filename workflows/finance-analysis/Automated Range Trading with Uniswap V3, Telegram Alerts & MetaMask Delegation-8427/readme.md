## 简介
**Automated Range Trading with Uniswap V3, Telegram Alerts & MetaMask Delegation**

（待补充中文描述）

> 分类：金融分析 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8427

---

# Automated Range Trading with Uniswap V3, Telegram Alerts & MetaMask Delegation


## 节点清单

| 节点 | 类型 |
|------|------|
| Calculate TWAP | Code |
| Fetch Pool TWA Observations | 一次性执行 |
| Schedule Trigger | 定时触发器 |
| Swap Configs | Code |
| Buy, Sell or Hold | Switch 路由 |
| Confirm Buy | Telegram |
| Purchase Cancelled | Telegram |
| Buy or Cancel? | IF 判断 |
| Check Remaining Funds | 一次性执行 |
| Confirm Sell | Telegram |
| Sell or Cancel? | IF 判断 |
| Sell Cancelled | Telegram |
| Give Approval to Router (Sell) | 一次性同步 |
| Give Approval to Router (Buy) | 一次性同步 |
| Buy ETH | 一次性同步 |
| Sell ETH | 一次性同步 |
| Success Details (Sell) | Telegram |
| Success Details (Buy) | Telegram |
| Buy Failure Notification | Telegram |
| Sell Failure Notification | Telegram |
| Check New Funds | 一次性执行 |
| Get Buy Qoute | 一次性执行 |
| Get Sell Qoute | 一次性执行 |
| Get Last Trade Type | 一次性执行 |
| Parse Last Trade | Code |
| Don't Repeat Buys | IF 判断 |
| Don't Repeat Sells | IF 判断 |
| List wallets | 一次性执行 |
| When clicking ‘Execute workflow’ | 手动触发 |
| Assure WETH Methods | 一次性执行 |
| Assure USDC Methods | 一次性执行 |
| Assure QuoterV2 Methods | 一次性执行 |
| Assure SwapRouter02 Methods | 一次性执行 |
| Assure ETH/USDC Pool Methods | 一次性执行 |
| If | IF 判断 |
| Create wallet | 一次性执行 |
| Get Wallet ID | Code |



## 功能说明

金融数据分析系统，市场行情采集与 AI 分析告警，定时执行。

定时触发、手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：37
- 触发方式：定时触发, 手动触发

## 触发方式
- Schedule Trigger 触发
- When clicking ‘Execute workflow’ 触发

## 统计
- 节点总数：37
- 触发节点：2
- 处理节点：27
- 输出节点：8
- 分类：finance-analysis
