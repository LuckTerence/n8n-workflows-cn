## 简介
**Scrape, search and browse the web with a Firecrawl AI agent webhook**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/14167

---

# Scrape, search and browse the web with a Firecrawl AI agent webhook


## 节点清单

| 节点 | 类型 |
|------|------|
| Create browser session in Firecrawl | Firecrawl 工具 |
| Execute browser code in Firecrawl | Firecrawl 工具 |
| List browser sessions in Firecrawl | Firecrawl 工具 |
| Delete browser session in Firecrawl | Firecrawl 工具 |
| Receive Scrape Request | Webhook |
| Validate Output Schema | Code |
| Return Schema Error | 响应 Webhook |
| Research & Extract Web Data | AI Agent |
| Return Structured Results | 响应 Webhook |
| Primary Chat Model | OpenRouter Chat Model |
| Fallback Chat Model | OpenRouter Chat Model |
| Parser Chat Model | OpenRouter Chat Model |
| Scrape Webpage Content | Firecrawl 工具 |
| Search the Web | Firecrawl 工具 |
| Get Browser Context | Firecrawl 工具 |
| Format Response to Schema | 结构化输出解析器 |

## 触发方式
- Receive Scrape Request 触发

## 统计
- 节点总数：16
- 触发节点：1
- 处理节点：13
- 输出节点：2
- 分类：workflow-automation
