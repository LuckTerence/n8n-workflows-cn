# Airbnb Telegram Agent - AI-powered accommodation search with voice support

https://n8nworkflows.xyz/workflows/4494

## 节点清单

| 节点 | 类型 |
|------|------|
| Simple Memory | 记忆缓冲区 |
| OpenAI Chat Model | OpenAI Chat Model |
| Airbnb MCP Client - List Tools | MCP 客户端 |
| Airbnb MCP Client - Execute Tools | MCP 客户端 |
| Airbnb Agent | AI Agent |
| Telegram Trigger | Telegram 触发器 |
| Text or Voice | Switch 路由 |
| Get Voice Message | Telegram |
| Prepare Text Message for AI Agent | 数据设置 |
| Send Text Response | Telegram |
| Send Voice Response | Telegram |
| Create Voice Response | OpenAI |
| Summarize Response for Voice | LLM Chain |
| Transcribe Voice Message | OpenAI |

## 触发方式
- Telegram Trigger 触发

## 统计
- 节点总数：14
- 触发节点：1
- 处理节点：10
- 输出节点：3
- 分类：multimodal-ai
