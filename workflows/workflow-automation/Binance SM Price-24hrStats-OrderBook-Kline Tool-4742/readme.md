## 简介
**Binance SM Price-24hrStats-OrderBook-Kline Tool**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/4742

---

# Binance SM Price-24hrStats-OrderBook-Kline Tool


## 节点清单

| 节点 | 类型 |
|------|------|
| getCurrentPrice | HTTP 工具 |
| get24hrStats | HTTP 工具 |
| getOrderBook | HTTP 工具 |
| getKlines | HTTP 工具 |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| When Executed by Another Workflow | 执行工作流触发器 |
| Binance SM Price-24hrStats-OrderBook-Kline Agent | AI Agent |

## 触发方式
- When Executed by Another Workflow 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：3
- 输出节点：4
- 分类：workflow-automation
