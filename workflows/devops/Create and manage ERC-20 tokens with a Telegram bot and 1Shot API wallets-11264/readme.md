## 简介
**Create and manage ERC-20 tokens with a Telegram bot and 1Shot API wallets**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11264

---

# Create and manage ERC-20 tokens with a Telegram bot and 1Shot API wallets


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| Create a User Wallet | 一次性执行 |
| Send User Wallet Address | Telegram |
| Switch on User Button Choice | Switch 路由 |
| Send Action Keyboard Options | Telegram |
| Get the name of the token | Telegram |
| Get the token Symbol | Telegram |
| Creation Confirmation | Telegram |
| Reply with Token Address | Telegram |
| Try Again | Telegram |
| Check for Existing User | 数据表 |
| Only respond to /start Messages | IF 判断 |
| Does the User Have A Wallet | IF 判断 |
| Record User Wallet | 数据表 |
| Callback or Message | Switch 路由 |
| Get User's Tokens | 数据表 |
| Generate Message | Code |
| Record New Token | 数据表 |
| Lookup User Wallet | 数据表 |
| Get User Wallet Balance | 一次性执行 |
| Which Token? | Telegram |
| How Many? | Telegram |
| To What Address? | Telegram |
| Reply with TX Hash | Telegram |
| Send Token List | Telegram |
| Send Tokens | 一次性同步 |
| Failure to Send Tokens | Telegram |
| Deploy User Token | 一次性同步 |
| Max Supply | Telegram |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

Telegram 消息触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：29
- 触发方式：Telegram 消息触发

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：29
- 触发节点：1
- 处理节点：14
- 输出节点：14
- 分类：devops
