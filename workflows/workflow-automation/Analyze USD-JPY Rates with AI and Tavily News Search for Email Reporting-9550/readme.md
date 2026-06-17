# Analyze USD-JPY Rates with AI and Tavily News Search for Email Reporting

https://n8nworkflows.xyz/workflows/9550

## 节点清单

| 节点 | 类型 |
|------|------|
| Run every 4 hours | 定时触发器 |
| Analyze USD/JPY (AI agent) | AI Agent |
| LLM provider (configure) | OpenRouter Chat Model |
| Tool: Search Forex News (Tavily) | HTTP 工具 |
| Tool: Structured Output Parser | 结构化输出解析器 |
| Send results via Gmail | Email 发送 |
| Set (Fields) — Configure me | 数据设置 |
| Fetch USD/JPY rate (HTTP) | HTTP Request |

## 触发方式
- Run every 4 hours 触发

## 统计
- 节点总数：8
- 触发节点：1
- 处理节点：4
- 输出节点：3
- 分类：workflow-automation
