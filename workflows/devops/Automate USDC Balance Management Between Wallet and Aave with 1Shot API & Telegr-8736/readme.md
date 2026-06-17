## 简介
**Automate USDC Balance Management Between Wallet and Aave with 1Shot API & Telegram**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8736

---

# Automate USDC Balance Management Between Wallet and Aave with 1Shot API & Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| approve USDC | 一次性同步 |
| Deposit USDC into Aave L2Pool | 一次性同步 |
| Schedule Trigger | 定时触发器 |
| Calculate Excess Funds | Code |
| Deposit Confirmation | Telegram |
| Calculate Insufficient Funds | Code |
| Withdraw from Aave | 一次性同步 |
| Withdraw Confirmation | Telegram |
| Savings Configs | Code |
| Check User's Aave Savings | 一次性执行 |
| Check User's USDC Balance | 一次性执行 |
| Switch | Switch 路由 |
| No Change, Send Account Status | Telegram |
| Insufficient Savings Warning | Telegram |
| Deposit Failure Notification | Telegram |
| Withdraw Failure Notification | Telegram |
| Confirm User's USDC Balance After Withdraw | 一次性执行 |
| Confirm User's Aave Savings After Withdraw | 一次性执行 |
| Confirm User's USDC Balance After Deposit | 一次性执行 |
| Confirm User's Aave Savings After Deposit | 一次性执行 |
| Check User Has Sufficient Savings | IF 判断 |



## 功能说明

API 集成接口，连接和编排多个第三方服务，定时执行。

定时触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：21
- 触发方式：定时触发

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：devops
