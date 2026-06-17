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

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：21
- 触发节点：1
- 处理节点：14
- 输出节点：6
- 分类：devops
