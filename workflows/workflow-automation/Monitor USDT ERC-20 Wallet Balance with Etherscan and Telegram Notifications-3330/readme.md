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

## 触发方式
- Check Balance Every 5 Minutes 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：3
- 输出节点：3
- 分类：workflow-automation
