# AI-Powered Local Event Finder with Multi-Tool Search

https://n8nworkflows.xyz/workflows/4816

## 节点清单

| 节点 | 类型 |
|------|------|
| Google Gemini Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| brave_web_search | MCP 客户端 |
| brave_local_search | MCP 客户端 |
| find_events | 工作流工具 |
| even_finder_workflow | 执行工作流触发器 |
| event_finder_agent | AI Agent |
| local_event_finder | MCP 触发器 |
| google_gemini_event_search | geminiSearchToolTool |
| jina_ai_web_page_scraper | jinaAiTool |

## 触发方式
- even_finder_workflow 触发
- local_event_finder 触发

## 统计
- 节点总数：10
- 触发节点：2
- 处理节点：8
- 输出节点：0
- 分类：workflow-automation
