## 简介
**Automate Token Purchases with Dollar Cost Averaging on Uniswap V3 & 1Shot API**

（待补充中文描述）

> 分类：知识库 RAG | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/8044

---

# Automate Token Purchases with Dollar Cost Averaging on Uniswap V3 & 1Shot API


## 节点清单

| 节点 | 类型 |
|------|------|
| Calculate TWAP | Code |
| Fetch Pool TWA Observations | 一次性执行 |
| Get Swap Qoute | 一次性执行 |
| Swap Tokens | 一次性同步 |
| Schedule Trigger | 定时触发器 |
| Failure Details | Telegram |
| Give Approval to Router | 一次性同步 |
| Success Details | Telegram |
| Get Remaining DCA Funds Balance | 一次性执行 |
| Swap Configs | Code |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：10
- 触发节点：1
- 处理节点：7
- 输出节点：2
- 分类：knowledge-rag
