## 简介
**AI-Powered Telegram Task Manager with MCP Server**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3656

---

# AI-Powered Telegram Task Manager with MCP Server


## 节点清单

| 节点 | 类型 |
|------|------|
| Incoming Message | Telegram 触发器 |
| MCP Server Trigger | MCP 触发器 |
| AI Agent | AI Agent |
| MCP Client | MCP 客户端 |
| OpenAI Chat Model | OpenAI Chat Model |
| Simple Memory | 记忆缓冲区 |
| chatInput | 数据设置 |
| create_todays_task | googleTasksTool |
| chatOutput | 数据设置 |
| sendMessage | Telegram |
| create_upcoming_task | googleTasksTool |
| complete_task | googleTasksTool |
| get_todays_tasks | googleTasksTool |
| get_upcoming_tasks | googleTasksTool |
| Switch | Switch 路由 |
| audio_id | 数据设置 |
| download_audio | Telegram |
| transcribeAudio | OpenAI |
| audioInput | 数据设置 |

## 触发方式
- Incoming Message 触发
- MCP Server Trigger 触发

## 统计
- 节点总数：19
- 触发节点：2
- 处理节点：15
- 输出节点：2
- 分类：workflow-automation
