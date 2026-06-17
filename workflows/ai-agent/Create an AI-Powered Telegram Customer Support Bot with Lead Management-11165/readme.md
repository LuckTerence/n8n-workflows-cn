# Create an AI-Powered Telegram Customer Support Bot with Lead Management

https://n8nworkflows.xyz/workflows/11165

## 节点清单

| 节点 | 类型 |
|------|------|
| OpenRouter Chat Model | OpenRouter Chat Model |
| Simple Memory | 记忆缓冲区 |
| Telegram - Incoming Message | Telegram 触发器 |
| Log - User Message | 数据表 |
| Log - Bot Message | 数据表 |
| DB - Get Lead by User ID | 数据表 |
| DB - Create Lead | 数据表 |
| DB - Update Lead | dataTableTool |
| AI - Smart Support Assistant | AI Agent |
| DB - Get FAQ | dataTableTool |
| DB - Get Services | dataTableTool |
| DB - Get Settings | dataTableTool |
| Telegram - Send Response | Telegram |
| Build Assistant Context | Code |
| Check – Lead Record | IF 判断 |

## 触发方式
- Telegram - Incoming Message 触发

## 统计
- 节点总数：15
- 触发节点：1
- 处理节点：13
- 输出节点：1
- 分类：ai-agent
