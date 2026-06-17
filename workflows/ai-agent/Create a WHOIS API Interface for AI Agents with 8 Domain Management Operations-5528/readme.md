## 简介
**Create a WHOIS API Interface for AI Agents with 8 Domain Management Operations**

（待补充中文描述）

> 分类：AI Agent | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/5528

---

# Create a WHOIS API Interface for AI Agents with 8 Domain Management Operations


## 节点清单

| 节点 | 类型 |
|------|------|
| Bulk WHOIS MCP Server | MCP 触发器 |
| Get your batches | HTTP Request 工具 |
| Create batch. Batch is then being processed until  | HTTP Request 工具 |
| Delete batch | HTTP Request 工具 |
| Get batch | HTTP Request 工具 |
| Query domain database | HTTP Request 工具 |
| Check domain availability | HTTP Request 工具 |
| Check domain rank (authority). | HTTP Request 工具 |
| WHOIS query for a domain | HTTP Request 工具 |

## 触发方式
- Bulk WHOIS MCP Server 触发

## 统计
- 节点总数：9
- 触发节点：1
- 处理节点：0
- 输出节点：8
- 分类：ai-agent
