# Manage Cloudflare DNS Records with AI-powered Chat Assistant

https://n8nworkflows.xyz/workflows/6844

## 节点清单

| 节点 | 类型 |
|------|------|
| When chat message received | Chat 触发器 |
| OpenAI Chat Model | OpenAI Chat Model |
| Chat Agent | AI Agent |
| Get TLDs | HTTP Request |
| Json | Code |
| Switch | Switch 路由 |
| Postgres Chat Memory | PostgreSQL 聊天记忆 |
| CloudFlare tool | 工作流工具 |
| End | 空操作 |
| SubCall | 执行工作流触发器 |
| Host details | 数据拆分 |
| Getter | HTTP Request |
| Setter | HTTP Request |

## 触发方式
- When chat message received 触发
- SubCall 触发

## 统计
- 节点总数：13
- 触发节点：2
- 处理节点：8
- 输出节点：3
- 分类：workflow-automation
