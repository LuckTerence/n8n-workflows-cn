## 简介
**AAVE投资组合Agent**

Telegram+Email+GPT-4o加密投资分析

> 分类：金融分析 | 适配等级：B（需替换Notion/Google Sheets/Gmail)（AI模型已替换为DeepSeek，部分边角节点可能仍需手动调整）
> 原始来源：https://n8nworkflows.xyz/workflows/4267

---

# AAVE投资组合Agent


## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram | Telegram |
| Schedule Trigger | 定时触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| getDefiSummary | HTTP Request 工具 |
| getDefiPositionsSummary | HTTP Request 工具 |
| getDefiPositionsByProtocol | HTTP Request 工具 |
| Gmail | Gmail |
| Format Email | Code |
| AAVE Portfolio Professional AI Agent | AI Agent |
| Wallet Addresses to Monitor | Google Sheets |
| Edit Fields | 数据设置 |

## 触发方式
- Schedule Trigger 触发

## 统计
- 节点总数：11
- 触发节点：1
- 处理节点：6
- 输出节点：4
- 分类：finance-analysis
