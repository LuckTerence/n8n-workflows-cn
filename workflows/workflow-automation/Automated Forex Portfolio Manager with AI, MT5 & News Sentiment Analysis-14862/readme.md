## 简介
**Automated Forex Portfolio Manager with AI, MT5 & News Sentiment Analysis**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：26 | 难度：⭐⭐⭐ 高级
> 原始来源：https://n8nworkflows.xyz/workflows/14862

---

# Automated Forex Portfolio Manager with AI, MT5 & News Sentiment Analysis


## 节点清单

| 节点 | 类型 |
|------|------|
| Every Hour Trigger | 定时触发器 |
| Config | 数据设置 |
| Get Portfolio from Signal Handler | HTTP Request |
| NewsAPI Headlines | HTTP Request |
| FinnHub Market News | HTTP Request |
| Alpha Vantage Macro Sentiment | HTTP Request |
| Fear & Greed Index | HTTP Request |
| Forex Factory Calendar | HTTP Request |
| Merge All Data | 数据合并 |
| Build Full Context | Code |
| AI Portfolio Analyst | LLM Chain |
| Parse AI Response | Code |
| Format Discord Update | Code |
| Send Update to Discord | Discord |
| Extract Actions | Code |
| Has Actions? | IF 判断 |
| Action Type? | Switch 路由 |
| Buy: Market or Limit? | Switch 路由 |
| Buy Market Order | HTTP Request |
| Buy Limit Order | HTTP Request |
| Sell: Market or Limit? | Switch 路由 |
| Sell Market Order | HTTP Request |
| Sell Limit Order | HTTP Request |
| Close Position Signal | HTTP Request |
| Build Execution Confirmation | Code |
| Send Trade Confirmation | Discord |
| Anthropic Chat Model | OpenAI Chat Model |

## 触发方式
- Every Hour Trigger 触发

## 统计
- 节点总数：27
- 触发节点：1
- 处理节点：13
- 输出节点：13
- 分类：workflow-automation
