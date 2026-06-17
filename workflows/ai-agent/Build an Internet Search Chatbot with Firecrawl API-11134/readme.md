# Build an Internet Search Chatbot with Firecrawl API

https://n8nworkflows.xyz/workflows/11134

## 节点清单

| 节点 | 类型 |
|------|------|
| Receive search query | Webhook |
| Search the web (Firecrawl) | Firecrawl |
| Answer search query | 响应 Webhook |
| Terminate service flow | 空操作 |
| Receive chat message | Chat 触发器 |
| Query search server (HTTP) | HTTP Request |
| Reply to the user in the chat | 聊天 |
| Terminate interface flow | 空操作 |
| Format search response (Python) | Code |
| Define constants | 数据设置 |
| Manual Trigger | 手动触发 |
| Verify Firecrawl Account Credit Balance | Firecrawl |
| Terminate Monitor Flow | 空操作 |

## 触发方式
- Receive search query 触发
- Receive chat message 触发
- Manual Trigger 触发

## 统计
- 节点总数：13
- 触发节点：3
- 处理节点：7
- 输出节点：3
- 分类：ai-agent
