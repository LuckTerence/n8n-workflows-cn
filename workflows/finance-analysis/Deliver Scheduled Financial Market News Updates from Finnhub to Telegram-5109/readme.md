# Deliver Scheduled Financial Market News Updates from Finnhub to Telegram

https://n8nworkflows.xyz/workflows/5109

## 节点清单

| 节点 | 类型 |
|------|------|
| Set API Key for Finhubb | 数据设置 |
| Get Latest News | HTTP Request |
| Code | Code |
| Schedule Trigger - Every 4 Hours | 定时触发器 |
| Download Image (optional) | HTTP Request |
| Send Text Updates via Telegram | Telegram |
| Send Image (with text update) - Optional | Telegram |

## 触发方式
- Schedule Trigger - Every 4 Hours 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：2
- 输出节点：4
- 分类：finance-analysis
