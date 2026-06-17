## 简介
**Simple Scheduling and Internal Document Query Bot with Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（需替换Pinecone/Google Sheets/Google Docs/Gmail)（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/11234

---

# Simple Scheduling and Internal Document Query Bot with Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| MCP Google Docs e Sheet | MCP 触发器 |
| Troubleshooting - Lista de Problemas e Soluções | Google Sheets 工具 |
| Valores dos Serviços | Google Sheets 工具 |
| Guia da Loja de TI | googleDocsTool |
| MCP Client Google Calendario | MCP 客户端 |
| MCP Client Google Docs | MCP 客户端 |
| Date & Time | dateTimeTool |
| Send a text message | Telegram |
| Telegram Trigger | Telegram 触发器 |
| Update an event in Google Calendar | Google Calendar 工具 |
| Get many events in Google Calendar | Google Calendar 工具 |
| Delete an event in Google Calendar | Google Calendar 工具 |
| Create an event in Google Calendar | Google Calendar 工具 |
| MCP Google Calendario | MCP 触发器 |
| Google Gemini Chat Model | OpenAI Chat Model |
| AI Agent | AI Agent |
| Redis Chat Memory | memoryRedisChat |

## 触发方式
- MCP Google Docs e Sheet 触发
- Telegram Trigger 触发
- MCP Google Calendario 触发

## 统计
- 节点总数：17
- 触发节点：3
- 处理节点：13
- 输出节点：1
- 分类：workflow-automation
