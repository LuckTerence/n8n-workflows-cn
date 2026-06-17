## 简介
**Manage Cloudflare DNS Records with AI-powered Chat Assistant**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A-adapted（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/6844

---

# Manage Cloudflare DNS Records with AI-powered Chat Assistant


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
