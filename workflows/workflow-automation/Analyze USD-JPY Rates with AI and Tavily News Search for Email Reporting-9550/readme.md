## 简介
**Analyze USD-JPY Rates with AI and Tavily News Search for Email Reporting**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/9550

---

# Analyze USD-JPY Rates with AI and Tavily News Search for Email Reporting


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
