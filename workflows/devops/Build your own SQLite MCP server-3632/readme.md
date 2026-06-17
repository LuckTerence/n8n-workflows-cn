## 简介
**Build your own SQLite MCP server**

（待补充中文描述）

> 分类：DevOps | 适配等级：A（基本改完，配置 API Key 应该就能跑）
> 节点数：11 | 难度：⭐⭐ 进阶
> 原始来源：https://n8nworkflows.xyz/workflows/3632

---

# Build your own SQLite MCP server


## 节点清单

| 节点 | 类型 |
|------|------|
| When Executed by Another Workflow | 执行工作流触发器 |
| Operation | Switch 路由 |
| SQLite MCP Server | MCP 触发器 |
| CreateRecord | Code |
| UpdateRecord | Code |
| ReadRecords | Code |
| DescribeTables | 代码工具 |
| ListTables | 代码工具 |
| CreateRecords | 工作流工具 |
| UpdateRows | 工作流工具 |
| ReadRows | 工作流工具 |

## 触发方式
- When Executed by Another Workflow 触发
- SQLite MCP Server 触发

## 统计
- 节点总数：11
- 触发节点：2
- 处理节点：9
- 输出节点：0
- 分类：devops
