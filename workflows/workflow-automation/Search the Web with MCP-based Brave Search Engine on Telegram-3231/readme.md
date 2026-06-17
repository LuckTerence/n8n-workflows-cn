## 简介
**Search the Web with MCP-based Brave Search Engine on Telegram**

（待补充中文描述）

> 分类：工作流自动化 | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 原始来源：https://n8nworkflows.xyz/workflows/3231

---

# Search the Web with MCP-based Brave Search Engine on Telegram


## 节点清单

| 节点 | 类型 |
|------|------|
| List Brave Tools | mcpClient |
| Exec Brave tool | mcpClient |
| Clean query | Code |
| Send message | Telegram |
| Get Message | Telegram 触发器 |
| Search with Brave? | IF 判断 |
| Get Text | 数据设置 |

## 触发方式
- Get Message 触发

## 统计
- 节点总数：7
- 触发节点：1
- 处理节点：5
- 输出节点：1
- 分类：workflow-automation
