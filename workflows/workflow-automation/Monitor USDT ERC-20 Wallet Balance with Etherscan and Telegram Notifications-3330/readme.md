## 简介
**Monitor USDT ERC-20 Wallet Balance with Etherscan and Telegram Notifications**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3330

---

# Monitor USDT ERC-20 Wallet Balance with Etherscan and Telegram Notifications


## 节点清单

| 节点 | 类型 |
|------|------|
| Balance Changed? | IF 判断 |
| Balance Changed. | Telegram |
| Balance Not Changed. | Telegram |
| userData | 数据设置 |
| balanceChecker | Code |
| Check Balance Every 5 Minutes | 定时触发器 |
| Fetch USDT Balance from Etherscan | HTTP Request |



## 功能说明

Telegram 机器人，消息驱动自动化流程。

手动触发，通过 Telegram 通知 实现自动化。

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

- 节点总数：7
- 触发方式：手动或子流程调用

## 触发方式
- Check Balance Every 5 Minutes 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
