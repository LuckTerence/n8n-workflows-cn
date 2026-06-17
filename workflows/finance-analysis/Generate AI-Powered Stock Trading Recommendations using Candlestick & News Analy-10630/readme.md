# Generate AI-Powered Stock Trading Recommendations using Candlestick & News Analysis

https://n8nworkflows.xyz/workflows/10630

## 节点清单

| 节点 | 类型 |
|------|------|
| Telegram Trigger | Telegram 触发器 |
| 15 min Interval | HTTP Request |
| 1 min Interval | HTTP Request |
| 1 hour Interval | HTTP Request |
| Merge | 数据合并 |
| Aggregate | 数据聚合 |
| Code in JavaScript | Code |
| News Aggregator | HTTP Request |
| Message a model | OpenAI Chat Model |
| Merge1 | 数据合并 |
| Aggregate1 | 数据聚合 |
| AI Agent | AI Agent |
| Google Gemini Chat Model | OpenAI Chat Model |
| Send a text message | Telegram |
| Account Check | Switch 路由 |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：9
- 输出节点：5
- 分类：finance-analysis
